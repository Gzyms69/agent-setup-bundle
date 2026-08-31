#!/usr/bin/env python3
"""
worker_mcp.py
FastMCP Server for Autonomous Sub-Worker Delegation (Aider Engine + Chinese & Free LLMs)
Features:
- Task-Specialized Intelligent Router (MiniMax M3, Nemotron 550B, GLM-5.2, Nemotron Lightning)
- Dynamic Skill Injector (injecting ~/.agents/skills/*/SKILL.md via --read)
- Git Worktree Sandboxing & Zero Context Bleed
- Automated Self-Healing Quality Gate (--auto-test with stack detection)
- Resilient Fallback Chain (OpenRouter Free -> Direct Zhipu BigModel PAAS)
"""

import os
import sys
import json
import uuid
import shutil
import subprocess
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple

from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Initialize FastMCP Server
mcp = FastMCP("chinese-worker", instructions="High-throughput specialized sub-worker delegation server using Aider, Chinese LLMs, and OpenRouter Free Tier.")

# Constants & Paths
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_PATH = ROOT_DIR / "config" / "worker_profiles.json"
USER_CONFIG_PATH = Path.home() / ".agents" / "config" / "worker_profiles.json"
MODEL_SETTINGS_PATH = Path.home() / ".aider.model.settings.yml"
MODEL_METADATA_PATH = Path.home() / ".aider.model.metadata.json"
SKILLS_BASE_DIR = Path.home() / ".agents" / "skills"


def load_env_vars():
    """Loads environment variables from ~/.agents/.env and .env if present."""
    env_paths = [Path.home() / ".agents" / ".env", Path.cwd() / ".env"]
    for env_path in env_paths:
        if env_path.is_file():
            try:
                for line in env_path.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip("'\"")
                        if k not in os.environ:
                            os.environ[k] = v
            except Exception:
                pass

load_env_vars()


def load_profiles() -> Dict[str, Any]:
    """Loads worker profiles from user config or bundle config with fallback."""
    for path in [USER_CONFIG_PATH, CONFIG_PATH]:
        if path.is_file():
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    # Built-in default fallback
    return {
        "default_profile": "minimax-m3",
        "task_affinity": {
            "scaffold": "minimax-m3",
            "low_level": "nemotron-550b",
            "bugfix": "glm-5.2",
            "tests": "nemotron-lightning",
            "docs": "glm-5.2"
        },
        "fallback_chain": ["minimax-m3", "nemotron-550b", "glm-5.2", "nemotron-lightning", "glm-4-flash"],
        "profiles": {
            "minimax-m3": {
                "provider": "openrouter",
                "model_name": "openrouter/minimax/minimax-m3:free",
                "api_base": "https://openrouter.ai/api/v1",
                "env_key": "OPENROUTER_API_KEY",
                "edit_format": "diff",
                "context_window": 1048576,
                "max_output_tokens": 65536
            },
            "glm-4-flash": {
                "provider": "zhipu",
                "model_name": "openai/glm-4-flash",
                "api_base": "https://open.bigmodel.cn/api/paas/v4/",
                "env_key": "ZHIPU_API_KEY",
                "alt_env_key": "BIGMODEL_API_KEY",
                "edit_format": "diff",
                "context_window": 128000,
                "max_output_tokens": 4096
            }
        }
    }


def auto_select_profile(instruction: str, task_type: Optional[str] = None) -> str:
    """
    Task-Specialized Intelligent Router:
    Maps task requirements and keyword heuristics to the optimal worker model.
    """
    config = load_profiles()
    affinity = config.get("task_affinity", {})
    profiles = config.get("profiles", {})

    if task_type and task_type.lower() in affinity:
        selected = affinity[task_type.lower()]
        if selected in profiles:
            return selected

    # Heuristic Keyword Classification
    inst_lower = instruction.lower()
    if any(k in inst_lower for k in ["scaffold", "boilerplate", "entire service", "new module", "full-stack", "create app", "multi-file"]):
        return affinity.get("scaffold", "minimax-m3")
    elif any(k in inst_lower for k in ["binary", "header", "parser", "pointer", "c++", "rust", "low-level", "algorithm", "math", "jpeg", "byte"]):
        return affinity.get("low_level", "nemotron-550b")
    elif any(k in inst_lower for k in ["bug", "fix", "repair", "refactor", "patch", "type error", "strict", "migration"]):
        return affinity.get("bugfix", "glm-5.2")
    elif any(k in inst_lower for k in ["test", "unit test", "pytest", "vitest", "jest", "mock", "tdd", "assertion"]):
        return affinity.get("tests", "nemotron-lightning")
    elif any(k in inst_lower for k in ["docstring", "jsdoc", "documentation", "readme", "guide"]):
        return affinity.get("docs", "glm-5.2")

    return config.get("default_profile", "minimax-m3")


def resolve_profile(requested_profile: Optional[str] = None, task_type: Optional[str] = None, instruction: str = "") -> Tuple[str, Dict[str, Any], str]:
    """
    Resolves the best available profile and API key, executing fallback chain if needed.
    Returns: (profile_name, profile_dict, api_key)
    """
    load_env_vars()
    config = load_profiles()
    profiles = config.get("profiles", {})
    fallback_chain = config.get("fallback_chain", list(profiles.keys()))

    target = requested_profile or auto_select_profile(instruction, task_type)
    if target not in profiles:
        target = config.get("default_profile", "minimax-m3")

    candidates = [target] + [p for p in fallback_chain if p != target]

    for name in candidates:
        if name not in profiles:
            continue
        p = profiles[name]
        env_key = p.get("env_key", "")
        alt_env_key = p.get("alt_env_key", "")
        key_val = os.getenv(env_key) or (os.getenv(alt_env_key) if alt_env_key else None)
        if key_val:
            return name, p, key_val

    # Fallback to target definition even if key empty
    p = profiles.get(target, list(profiles.values())[0])
    return target, p, ""


def resolve_skills(skill_names: List[str]) -> List[Path]:
    """Resolves skill names into full paths to SKILL.md for dynamic context injection."""
    resolved_paths = []
    for sname in skill_names:
        sname_clean = sname.strip()
        # Direct path check
        p = Path(sname_clean)
        if p.is_file():
            resolved_paths.append(p)
            continue
        # Base skill dir check
        skill_dir = SKILLS_BASE_DIR / sname_clean
        if (skill_dir / "SKILL.md").is_file():
            resolved_paths.append(skill_dir / "SKILL.md")
        elif (skill_dir.parent / sname_clean / "SKILL.md").is_file():
            resolved_paths.append(skill_dir.parent / sname_clean / "SKILL.md")
    return resolved_paths


def sanitize_and_resolve_path(repo_dir: Path, rel_path: str) -> Path:
    """Path Traversal Guard: Ensures paths resolve strictly within repository boundaries."""
    clean = os.path.normpath(rel_path).lstrip("/\\")
    resolved = (repo_dir / clean).resolve()
    try:
        resolved.relative_to(repo_dir.resolve())
    except ValueError:
        raise ValueError(f"Path Traversal Violation: '{rel_path}' resolves outside repo root '{repo_dir}'.")
    return resolved


def find_repo_root(start_dir: Optional[str] = None) -> Path:
    """Locates the root git repository directory."""
    current = Path(start_dir or os.getcwd()).resolve()
    while current != current.parent:
        if (current / ".git").exists():
            return current
        current = current.parent
    return Path(start_dir or os.getcwd()).resolve()


def ensure_scratch_dir(repo_dir: Path) -> Path:
    """Ensures scratch directory exists for logging and Zero Context Bleed."""
    scratch = repo_dir / "scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    return scratch


def detect_stack_test_command(work_dir: Path) -> Optional[str]:
    """Auto-detects project stack and returns the most suitable test/linter command."""
    if (work_dir / "tsconfig.json").is_file():
        return "npx tsc --noEmit"
    elif (work_dir / "pytest.ini").is_file() or (work_dir / "pyproject.toml").is_file() or (work_dir / "tests").is_dir():
        if shutil.which("pytest"):
            return "pytest -v --tb=short"
    elif (work_dir / "Cargo.toml").is_file():
        if shutil.which("cargo"):
            return "cargo test --no-run"
    elif (work_dir / "package.json").is_file():
        try:
            pkg = json.loads((work_dir / "package.json").read_text(encoding="utf-8"))
            if "scripts" in pkg and "test" in pkg["scripts"]:
                return "npm test -- --passWithNoTests"
        except Exception:
            pass
    return None


def run_stack_quality_gate(worktree_dir: Path) -> Tuple[bool, str]:
    """Executes automated stack quality checks on generated code."""
    cmd_str = detect_stack_test_command(worktree_dir)
    if not cmd_str:
        return True, "No specific stack test runner detected (Clean)."

    try:
        res = subprocess.run(cmd_str, shell=True, cwd=worktree_dir, capture_output=True, text=True, timeout=120)
        if res.returncode == 0:
            return True, f"[PASS] Quality Gate passed: '{cmd_str}'"
        else:
            err_preview = (res.stderr or res.stdout).strip().splitlines()[-4:]
            return False, f"[FAIL] Quality Gate failed ('{cmd_str}'): {' | '.join(err_preview)}"
    except Exception as e:
        return False, f"[ERROR] Quality Gate error: {str(e)}"


class WorktreeManager:
    """Manages Git Worktrees for isolated task execution."""

    @staticmethod
    def create_worktree(repo_dir: Path, task_id: str) -> Tuple[Path, str]:
        branch_name = f"worker/{task_id}"
        worktree_path = repo_dir / ".git" / "worktrees_active" / task_id
        worktree_path.parent.mkdir(parents=True, exist_ok=True)

        cmd = ["git", "worktree", "add", "-b", branch_name, str(worktree_path)]
        res = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True)
        if res.returncode != 0:
            cmd_fallback = ["git", "worktree", "add", str(worktree_path), branch_name]
            res_fallback = subprocess.run(cmd_fallback, cwd=repo_dir, capture_output=True, text=True)
            if res_fallback.returncode != 0:
                raise RuntimeError(f"Failed to create git worktree: {res.stderr or res_fallback.stderr}")

        return worktree_path, branch_name

    @staticmethod
    def get_diff(repo_dir: Path, worktree_path: Path) -> str:
        res = subprocess.run(["git", "diff", "HEAD"], cwd=worktree_path, capture_output=True, text=True)
        return res.stdout or "No changes detected."

    @staticmethod
    def merge_worktree(repo_dir: Path, task_id: str, commit_message: str = "") -> str:
        branch_name = f"worker/{task_id}"
        worktree_path = repo_dir / ".git" / "worktrees_active" / task_id

        if not worktree_path.exists():
            return f"[ERROR] Worktree for task '{task_id}' does not exist."

        # Commit changes in worktree
        subprocess.run(["git", "add", "."], cwd=worktree_path, capture_output=True)
        msg = commit_message or f"worker(automated): completed task {task_id}"
        subprocess.run(["git", "commit", "-m", msg], cwd=worktree_path, capture_output=True)

        # Merge into parent branch
        res_merge = subprocess.run(["git", "merge", branch_name], cwd=repo_dir, capture_output=True, text=True)
        
        # Cleanup
        subprocess.run(["git", "worktree", "remove", "--force", str(worktree_path)], cwd=repo_dir, capture_output=True)
        subprocess.run(["git", "branch", "-D", branch_name], cwd=repo_dir, capture_output=True)

        if res_merge.returncode != 0:
            return f"[MERGE CONFLICT] Merge failed for branch {branch_name}:\n{res_merge.stderr or res_merge.stdout}"
        return f"[SUCCESS] Branch '{branch_name}' merged cleanly into main workspace."

    @staticmethod
    def discard_worktree(repo_dir: Path, task_id: str) -> str:
        branch_name = f"worker/{task_id}"
        worktree_path = repo_dir / ".git" / "worktrees_active" / task_id

        if worktree_path.exists():
            subprocess.run(["git", "worktree", "remove", "--force", str(worktree_path)], cwd=repo_dir, capture_output=True)
        subprocess.run(["git", "branch", "-D", branch_name], cwd=repo_dir, capture_output=True)
        return f"[SUCCESS] Discarded worktree and deleted branch '{branch_name}'."


def execute_aider_core(
    work_dir: Path,
    instruction: str,
    editable_files: List[str],
    readonly_files: List[str],
    skills: List[str],
    profile_name: Optional[str] = None,
    task_type: Optional[str] = None,
    auto_test: bool = True,
    test_cmd: str = "",
    task_id: str = ""
) -> Dict[str, Any]:
    """Core headless Aider executor with dynamic skills and self-healing."""
    p_name, profile, api_key = resolve_profile(requested_profile=profile_name, task_type=task_type, instruction=instruction)
    repo_root = find_repo_root(str(work_dir))
    scratch_dir = ensure_scratch_dir(repo_root)
    log_file = scratch_dir / f"worker_{task_id or uuid.uuid4().hex[:8]}.log"

    env = os.environ.copy()
    if api_key:
        env["OPENAI_API_KEY"] = api_key
    if profile.get("api_base"):
        env["OPENAI_API_BASE"] = profile["api_base"]
    env["AIDER_CHECK_UPDATE"] = "false"
    env["AIDER_SHOW_MODEL_WARNINGS"] = "false"
    env["AIDER_ANALYTICS"] = "false"

    cmd = [
        sys.executable, "-m", "aider",
        "--yes-always",
        "--no-auto-commits",
        "--no-git",
        "--model", profile["model_name"],
        "--message", instruction,
    ]

    # Model settings & metadata injection
    if MODEL_SETTINGS_PATH.is_file():
        cmd.extend(["--model-settings-file", str(MODEL_SETTINGS_PATH)])
    if MODEL_METADATA_PATH.is_file():
        cmd.extend(["--model-metadata-file", str(MODEL_METADATA_PATH)])

    # Edit format
    if profile.get("edit_format"):
        cmd.extend(["--edit-format", profile["edit_format"]])

    # Self-Healing test loop injection
    effective_test_cmd = test_cmd or (detect_stack_test_command(work_dir) if auto_test else "")
    if auto_test and effective_test_cmd:
        cmd.extend(["--auto-test", "--test-cmd", effective_test_cmd])

    # Dynamic Skills Injection (--read)
    resolved_skills = resolve_skills(skills)
    for s_path in resolved_skills:
        cmd.extend(["--read", str(s_path)])

    # Read-only reference files (--read)
    for rfile in readonly_files:
        try:
            r_path = sanitize_and_resolve_path(work_dir, rfile)
            if r_path.is_file():
                cmd.extend(["--read", str(r_path)])
        except Exception:
            pass

    # Target editable files
    for efile in editable_files:
        try:
            e_path = sanitize_and_resolve_path(work_dir, efile)
            cmd.append(str(e_path))
        except Exception:
            pass

    try:
        proc = subprocess.run(
            cmd,
            cwd=work_dir,
            env=env,
            capture_output=True,
            text=True,
            timeout=360
        )
        output_log = f"=== PROFILE: {p_name} ({profile.get('model_name')}) ===\n=== STDOUT ===\n{proc.stdout}\n\n=== STDERR ===\n{proc.stderr}"
        log_file.write_text(output_log, encoding="utf-8")

        return {
            "success": (proc.returncode == 0),
            "returncode": proc.returncode,
            "log_path": str(log_file),
            "profile_used": p_name,
            "model_used": profile.get("model_name"),
            "stderr": proc.stderr
        }
    except Exception as e:
        log_file.write_text(f"Execution Error: {str(e)}", encoding="utf-8")
        return {
            "success": False,
            "error": str(e),
            "log_path": str(log_file),
            "profile_used": p_name
        }


# ==============================================================================
# FastMCP Tools
# ==============================================================================

@mcp.tool(description="Runs an autonomous coding/refactoring task using specialized Chinese/Free LLMs in a Git Worktree with Zero Context Bleed.")
def worker_run_task(
    instruction: str = Field(description="Actionable instruction describing the requested code changes."),
    editable_files: List[str] = Field(description="Relative file paths that the worker is allowed to edit or create."),
    readonly_files: List[str] = Field(default=[], description="Relative file paths provided as read-only reference context (--read)."),
    skills: List[str] = Field(default=[], description="Domain skills to dynamically inject (e.g. ['skill-backend-architect', 'skill-qa-engineer'])."),
    task_type: Optional[str] = Field(default=None, description="Task archetype ('scaffold', 'low_level', 'bugfix', 'tests', 'docs') for intelligent routing."),
    profile: Optional[str] = Field(default=None, description="Explicit profile override (e.g. 'minimax-m3', 'nemotron-550b', 'glm-5.2')."),
    auto_test: bool = Field(default=True, description="Whether to run the automated self-healing test loop."),
    test_cmd: str = Field(default="", description="Optional custom test command for self-healing."),
    use_worktree: bool = Field(default=True, description="Whether to isolate execution in a dedicated Git Worktree.")
) -> str:
    task_id = uuid.uuid4().hex[:8]
    repo_root = find_repo_root()

    if use_worktree:
        try:
            worktree_dir, branch_name = WorktreeManager.create_worktree(repo_root, task_id)
        except Exception as e:
            return f"[ERROR] Failed to initialize worktree: {str(e)}"
        target_dir = worktree_dir
    else:
        target_dir = repo_root
        branch_name = "current-working-tree"

    res = execute_aider_core(
        work_dir=target_dir,
        instruction=instruction,
        editable_files=editable_files,
        readonly_files=readonly_files,
        skills=skills,
        profile_name=profile,
        task_type=task_type,
        auto_test=auto_test,
        test_cmd=test_cmd,
        task_id=task_id
    )

    if not res.get("success"):
        return (
            f"[FAILED] Task '{task_id}' failed using profile '{res.get('profile_used')}'.\n"
            f"Log: {res.get('log_path')}\n"
            f"Details: {res.get('error') or res.get('stderr')}"
        )

    qg_pass, qg_report = run_stack_quality_gate(target_dir)

    return (
        f"[SUCCESS] Task '{task_id}' completed by {res.get('profile_used')} ({res.get('model_used')}) in branch '{branch_name}'.\n"
        f"Modified Files: {', '.join(editable_files)}\n"
        f"Quality Gate: {qg_report}\n"
        f"Log Saved: {res.get('log_path')}\n"
        f"Action Required: Inspect with 'worker_get_diff(\"{task_id}\")' and merge with 'worker_merge_branch(\"{task_id}\")'."
    )


@mcp.tool(description="Generates comprehensive unit tests (TDD Red-Green) for a file using Nemotron-Lightning / GLM-5.2.")
def worker_generate_tests(
    target_file: str = Field(description="Relative path of the source file to test."),
    test_file: str = Field(description="Relative path of the test file to create/update."),
    test_framework: str = Field(default="auto", description="Testing framework (pytest, vitest, jest, cargo)."),
    skills: List[str] = Field(default=["skill-qa-engineer"], description="Domain skills to inject."),
    profile: Optional[str] = Field(default=None, description="Explicit profile override.")
) -> str:
    instruction = (
        f"Write comprehensive unit tests for '{target_file}' in '{test_file}'. "
        f"Framework: {test_framework}. Follow strict TDD Red-Green discipline, mock external network/disk I/O, cover edge cases and exceptions. "
        "Do not include conversational filler."
    )
    return worker_run_task(
        instruction=instruction,
        editable_files=[test_file],
        readonly_files=[target_file],
        skills=skills,
        task_type="tests",
        profile=profile,
        auto_test=True
    )


@mcp.tool(description="Generates JSDoc, docstrings, or markdown guides without degrading code.")
def worker_generate_docs(
    target_files: List[str] = Field(description="Files to document."),
    doc_type: str = Field(default="jsdoc", description="Documentation type (jsdoc, docstrings, markdown_guide)."),
    profile: Optional[str] = Field(default=None, description="Explicit profile override.")
) -> str:
    instruction = (
        f"Generate and write comprehensive {doc_type} documentation for the specified files. "
        "Document all public functions, parameters, return types, exceptions, and usage examples. "
        "Preserve existing functionality perfectly."
    )
    return worker_run_task(
        instruction=instruction,
        editable_files=target_files,
        task_type="docs",
        profile=profile,
        auto_test=False
    )


@mcp.tool(description="Executes a mass refactoring or type safety upgrade across multiple files.")
def worker_batch_refactor(
    target_files: List[str] = Field(description="Files to refactor."),
    instruction: str = Field(description="Refactoring instructions."),
    readonly_files: List[str] = Field(default=[], description="Reference files (schemas, types)."),
    skills: List[str] = Field(default=[], description="Domain skills to inject."),
    profile: Optional[str] = Field(default=None, description="Explicit profile override.")
) -> str:
    return worker_run_task(
        instruction=instruction,
        editable_files=target_files,
        readonly_files=readonly_files,
        skills=skills,
        task_type="bugfix",
        profile=profile,
        auto_test=True
    )


@mcp.tool(description="Continues working on an active task worktree branch.")
def worker_continue_task(
    task_id: str = Field(description="Active task ID corresponding to the worktree branch."),
    instruction: str = Field(description="Follow-up instructions or correction prompt."),
    editable_files: List[str] = Field(default=[], description="Additional files to edit."),
    readonly_files: List[str] = Field(default=[], description="Additional read-only files.")
) -> str:
    repo_root = find_repo_root()
    worktree_dir = repo_root / ".git" / "worktrees_active" / task_id
    if not worktree_dir.exists():
        return f"[ERROR] Worktree for task '{task_id}' not found at {worktree_dir}."

    res = execute_aider_core(
        work_dir=worktree_dir,
        instruction=instruction,
        editable_files=editable_files,
        readonly_files=readonly_files,
        skills=[],
        task_id=task_id
    )

    qg_pass, qg_report = run_stack_quality_gate(worktree_dir)
    return (
        f"[SUCCESS] Task '{task_id}' updated.\n"
        f"Quality Gate: {qg_report}\n"
        f"Log: {res.get('log_path')}"
    )


@mcp.tool(description="Inspects the git diff generated on a specific task worktree branch.")
def worker_get_diff(task_id: str = Field(description="Active task ID.")) -> str:
    repo_root = find_repo_root()
    worktree_dir = repo_root / ".git" / "worktrees_active" / task_id
    if not worktree_dir.exists():
        return f"[ERROR] Worktree '{task_id}' does not exist."
    diff_text = WorktreeManager.get_diff(repo_root, worktree_dir)
    return diff_text[:5000] + ("\n... [DIFF TRUNCATED]" if len(diff_text) > 5000 else "")


@mcp.tool(description="Merges the task worktree branch cleanly into current git working branch.")
def worker_merge_branch(
    task_id: str = Field(description="Task ID to merge."),
    commit_message: str = Field(default="", description="Optional custom commit message.")
) -> str:
    repo_root = find_repo_root()
    return WorktreeManager.merge_worktree(repo_root, task_id, commit_message)


@mcp.tool(description="Discards a task worktree and deletes its branch without merging.")
def worker_discard_branch(task_id: str = Field(description="Task ID to discard.")) -> str:
    repo_root = find_repo_root()
    return WorktreeManager.discard_worktree(repo_root, task_id)


@mcp.tool(description="Returns the status of configured providers, available profiles, and active worktrees.")
def worker_status() -> str:
    config = load_profiles()
    profiles = config.get("profiles", {})
    affinity = config.get("task_affinity", {})
    repo_root = find_repo_root()
    
    status_lines = ["=== Worker MCP Status ==="]
    status_lines.append(f"Repository Root: {repo_root}")
    status_lines.append(f"Default Profile: {config.get('default_profile')}")
    
    status_lines.append("\n[Task Routing Affinities]:")
    for task_k, prof_v in affinity.items():
        status_lines.append(f"  - {task_k:<15} -> {prof_v}")

    status_lines.append("\n[Configured Profiles]:")
    for name, p in profiles.items():
        env_key = p.get("env_key", "")
        alt_key = p.get("alt_env_key", "")
        has_key = bool(os.getenv(env_key) or (os.getenv(alt_key) if alt_key else False))
        status_lines.append(
            f"  - {name:<20}: {p.get('model_name')} via {p.get('provider')} "
            f"[Key: {'YES' if has_key else 'NO'}] (Context: {p.get('context_window'):,}, MaxOut: {p.get('max_output_tokens'):,})"
        )

    # Active worktrees
    worktrees_dir = repo_root / ".git" / "worktrees_active"
    active = [d.name for d in worktrees_dir.iterdir()] if worktrees_dir.is_dir() else []
    status_lines.append(f"\n[Active Worktrees]: {', '.join(active) if active else 'None'}")
    
    return "\n".join(status_lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
