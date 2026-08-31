#!/usr/bin/env python3
"""
worker_cli.py
Developer Terminal CLI Companion for Chinese Worker LLMs & Aider Engine.
Provides interactive and batch workflows with profile switching, worktree management, and health checks.
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path

# Paths
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


def load_config():
    load_env_vars()
    for p in [USER_CONFIG_PATH, CONFIG_PATH]:
        if p.is_file():
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
    return {
        "default_profile": "minimax-m3",
        "profiles": {
            "minimax-m3": {
                "model_name": "openrouter/minimax/minimax-m3:free",
                "api_base": "https://openrouter.ai/api/v1",
                "env_key": "OPENROUTER_API_KEY",
                "edit_format": "diff"
            }
        }
    }


def get_profile(name=None, task_type=None):
    cfg = load_config()
    profiles = cfg.get("profiles", {})
    affinity = cfg.get("task_affinity", {})

    if name and name in profiles:
        p_name = name
    elif task_type and task_type in affinity and affinity[task_type] in profiles:
        p_name = affinity[task_type]
    else:
        p_name = cfg.get("default_profile", "minimax-m3")

    profile = profiles.get(p_name, list(profiles.values())[0])
    return p_name, profile


def resolve_skills(skill_names):
    resolved = []
    for s in skill_names:
        p = Path(s)
        if p.is_file():
            resolved.append(p)
        else:
            s_dir = SKILLS_BASE_DIR / s
            if (s_dir / "SKILL.md").is_file():
                resolved.append(s_dir / "SKILL.md")
    return resolved


def cmd_chat(args):
    """Starts interactive Aider chat session with selected profile."""
    p_name, profile = get_profile(args.profile, getattr(args, "task_type", None))
    env = os.environ.copy()

    env_key = profile.get("env_key", "")
    alt_key = profile.get("alt_env_key", "")
    api_key = os.getenv(env_key) or (os.getenv(alt_key) if alt_key else "")

    if api_key:
        env["OPENAI_API_KEY"] = api_key
    else:
        print(f"[!] Warning: API Key for '{p_name}' ({env_key}) not found in environment.")

    if profile.get("api_base"):
        env["OPENAI_API_BASE"] = profile["api_base"]

    env["AIDER_CHECK_UPDATE"] = "false"
    env["AIDER_SHOW_MODEL_WARNINGS"] = "false"

    cmd = [
        sys.executable, "-m", "aider",
        "--model", profile["model_name"],
        "--dark-mode"
    ]

    if MODEL_SETTINGS_PATH.is_file():
        cmd.extend(["--model-settings-file", str(MODEL_SETTINGS_PATH)])
    if MODEL_METADATA_PATH.is_file():
        cmd.extend(["--model-metadata-file", str(MODEL_METADATA_PATH)])
    if profile.get("edit_format"):
        cmd.extend(["--edit-format", profile["edit_format"]])

    if args.skills:
        for s in resolve_skills(args.skills):
            cmd.extend(["--read", str(s)])

    if args.files:
        cmd.extend(args.files)

    print(f">>> Launching Aider with profile: [{p_name}] ({profile['model_name']})...")
    try:
        subprocess.run(cmd, env=env)
    except KeyboardInterrupt:
        print("\n[!] Session ended.")


def cmd_run(args):
    """Executes a one-shot batch instruction via Aider."""
    p_name, profile = get_profile(args.profile, getattr(args, "task_type", None))
    env = os.environ.copy()

    env_key = profile.get("env_key", "")
    alt_key = profile.get("alt_env_key", "")
    api_key = os.getenv(env_key) or (os.getenv(alt_key) if alt_key else "")

    if api_key:
        env["OPENAI_API_KEY"] = api_key
    if profile.get("api_base"):
        env["OPENAI_API_BASE"] = profile["api_base"]

    env["AIDER_CHECK_UPDATE"] = "false"
    env["AIDER_SHOW_MODEL_WARNINGS"] = "false"

    cmd = [
        sys.executable, "-m", "aider",
        "--yes-always",
        "--no-auto-commits",
        "--model", profile["model_name"],
        "--message", args.instruction
    ]

    if MODEL_SETTINGS_PATH.is_file():
        cmd.extend(["--model-settings-file", str(MODEL_SETTINGS_PATH)])
    if MODEL_METADATA_PATH.is_file():
        cmd.extend(["--model-metadata-file", str(MODEL_METADATA_PATH)])

    if args.read:
        for r in args.read:
            cmd.extend(["--read", r])

    if args.skills:
        for s in resolve_skills(args.skills):
            cmd.extend(["--read", str(s)])

    if args.files:
        cmd.extend(args.files)

    print(f">>> Running task with [{p_name}]: '{args.instruction}'...")
    res = subprocess.run(cmd, env=env)
    if res.returncode == 0:
        print("\n[+] Task completed successfully.")
    else:
        print(f"\n[X] Task finished with exit code {res.returncode}.")


def cmd_check(args):
    """Diagnoses environment, API keys, packages, and profile metadata."""
    print("=======================================================")
    print(">>> Sub-Worker Health & Diagnostics Check")
    print("=======================================================")
    
    # 1. Package checks
    print("[-] Checking Python dependencies:")
    for pkg in ["aider", "fastmcp", "openai", "pydantic"]:
        try:
            __import__(pkg)
            print(f"    [OK] {pkg} installed.")
        except ImportError:
            print(f"    [FAIL] {pkg} NOT installed (run: pip install {pkg})")

    # 2. Config check
    cfg = load_config()
    profiles = cfg.get("profiles", {})
    affinity = cfg.get("task_affinity", {})

    print(f"\n[-] Task Routing Affinities:")
    for t_type, prof in affinity.items():
        print(f"    - {t_type:<15} -> {prof}")

    print(f"\n[-] Loaded {len(profiles)} profiles from config:")
    for name, p in profiles.items():
        env_k = p.get("env_key", "")
        has_k = bool(os.getenv(env_k) or (os.getenv(p.get("alt_env_key", "")) if p.get("alt_env_key") else False))
        status = "CONFIGURED" if has_k else "KEY MISSING"
        ctx = p.get("context_window", 0)
        max_out = p.get("max_output_tokens", 0)
        print(f"    - {name:<20} -> {p.get('model_name'):<42} [{status}] (Ctx: {ctx:,}, MaxOut: {max_out:,})")

    print("\n=======================================================")
    print(">>> Diagnostics Complete.")


def main():
    parser = argparse.ArgumentParser(description="Sub-Worker CLI Companion (MiniMax / Nemotron / GLM + Aider)")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # chat
    parser_chat = subparsers.add_parser("chat", help="Start interactive Aider session")
    parser_chat.add_argument("profile", nargs="?", default=None, help="Profile name (e.g. minimax-m3, nemotron-550b, glm-5.2)")
    parser_chat.add_argument("--task-type", "-t", default=None, help="Task type (scaffold, low_level, bugfix, tests, docs)")
    parser_chat.add_argument("--skills", "-s", nargs="*", default=[], help="Domain skills to inject")
    parser_chat.add_argument("files", nargs="*", help="Files to edit")

    # run
    parser_run = subparsers.add_parser("run", help="Run batch instruction")
    parser_run.add_argument("instruction", help="Instruction for the worker")
    parser_run.add_argument("--profile", "-p", default=None, help="Profile to use")
    parser_run.add_argument("--task-type", "-t", default=None, help="Task type (scaffold, low_level, bugfix, tests, docs)")
    parser_run.add_argument("--skills", "-s", nargs="*", default=[], help="Domain skills to inject")
    parser_run.add_argument("--files", "-f", nargs="*", default=[], help="Files to edit")
    parser_run.add_argument("--read", "-r", nargs="*", default=[], help="Read-only context files (--read)")

    # check
    subparsers.add_parser("check", help="Run diagnostic health check")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "chat":
        cmd_chat(args)
    elif args.command == "run":
        cmd_run(args)
    elif args.command == "check":
        cmd_check(args)


if __name__ == "__main__":
    main()
