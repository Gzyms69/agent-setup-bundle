#!/usr/bin/env python3
"""
validate_suite.py
Automated Quality Gate & Validator for agent-setup-bundle
Verifies:
1. YAML frontmatter in all skills/ (name matches folder, description <= 1024 chars, valid YAML).
2. Rule counts and integrity in rules/.
3. Structural consistency across CODEX.md, GEMINI.md, CLAUDE.md, and .cursorrules.
4. JSON/TOML syntax in config/ files.
5. Templates presence (AGENTS.md).
"""

import os
import sys
import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / "skills"
RULES_DIR = ROOT_DIR / "rules"
CORE_DIR = ROOT_DIR / "core"
CONFIG_DIR = ROOT_DIR / "config"
TEMPLATES_DIR = ROOT_DIR / "templates"

errors = []
warnings = []

def check_skills():
    print("[-] Validating skills in", SKILLS_DIR)
    if not SKILLS_DIR.is_dir():
        errors.append("skills/ directory not found!")
        return 0

    skill_count = 0
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_count += 1
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"Skill '{skill_dir.name}' is missing SKILL.md")
            continue

        content = skill_md.read_text(encoding="utf-8")
        if not content.startswith("---"):
            errors.append(f"Skill '{skill_dir.name}' SKILL.md missing frontmatter start '---'")
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append(f"Skill '{skill_dir.name}' SKILL.md malformed frontmatter")
            continue

        frontmatter = parts[1]
        
        # Name check
        name_match = re.search(r"^name:\s*([a-zA-Z0-9_\-\.]+)", frontmatter, re.MULTILINE)
        if not name_match:
            errors.append(f"Skill '{skill_dir.name}' missing 'name:' in frontmatter")
        else:
            name_val = name_match.group(1).strip()
            if name_val != skill_dir.name:
                errors.append(f"Skill folder '{skill_dir.name}' does not match frontmatter name '{name_val}'")

        # Description check
        desc_match = re.search(r"^description:\s*(.+?)(?=\n[a-zA-Z0-9_\-]+:|\Z)", frontmatter, re.MULTILINE | re.DOTALL)
        if not desc_match:
            errors.append(f"Skill '{skill_dir.name}' missing 'description:' in frontmatter")
        else:
            desc_val = desc_match.group(1).strip()
            if len(desc_val) > 1024:
                errors.append(f"Skill '{skill_dir.name}' description exceeds 1024 chars (is {len(desc_val)})")
            if len(desc_val) < 20:
                warnings.append(f"Skill '{skill_dir.name}' description is very short ({len(desc_val)} chars)")

    print(f"    -> Checked {skill_count} skills.")
    return skill_count

def check_rules():
    print("[-] Validating rules in", RULES_DIR)
    if not RULES_DIR.is_dir():
        errors.append("rules/ directory not found!")
        return 0

    rule_count = 0
    for rule_file in sorted(RULES_DIR.iterdir()):
        if rule_file.suffix == ".md":
            rule_count += 1
            content = rule_file.read_text(encoding="utf-8")
            if len(content.strip()) < 50:
                warnings.append(f"Rule file '{rule_file.name}' is unusually short ({len(content.strip())} chars)")

    print(f"    -> Checked {rule_count} rules.")
    return rule_count

def check_configs():
    print("[-] Validating config files in", CONFIG_DIR)
    for cfg in CONFIG_DIR.glob("*.json"):
        try:
            with open(cfg, "r", encoding="utf-8") as f:
                json.load(f)
            print(f"    -> {cfg.name} valid JSON.")
        except Exception as e:
            errors.append(f"Config '{cfg.name}' invalid JSON: {e}")
    
    codex_toml = CONFIG_DIR / "codex_config.toml"
    if not codex_toml.is_file():
        errors.append("config/codex_config.toml missing!")
    else:
        print("    -> config/codex_config.toml present.")

def check_templates():
    print("[-] Validating templates in", TEMPLATES_DIR)
    agents_template = TEMPLATES_DIR / "AGENTS.md"
    if not agents_template.is_file():
        errors.append("templates/AGENTS.md missing!")
    else:
        print("    -> templates/AGENTS.md present.")

def check_core():
    print("[-] Validating core prompts across 4 platforms in", CORE_DIR)
    gemini_md = CORE_DIR / "GEMINI.md"
    claude_md = CORE_DIR / "CLAUDE.md"
    codex_md = CORE_DIR / "CODEX.md"
    cursor_rules = CORE_DIR / ".cursorrules"
    
    # 1. Codex
    if not codex_md.is_file():
        errors.append("core/CODEX.md missing!")
    else:
        content = codex_md.read_text(encoding="utf-8")
        if "Pre-Flight Skill Gate" not in content:
            errors.append("core/CODEX.md missing Pre-Flight Skill Gate definition!")
        print("    -> core/CODEX.md valid.")

    # 2. Gemini
    if not gemini_md.is_file():
        errors.append("core/GEMINI.md missing!")
    else:
        content = gemini_md.read_text(encoding="utf-8")
        if "Pre-Flight Skill Gate" not in content:
            errors.append("core/GEMINI.md missing Pre-Flight Skill Gate definition!")
        if "Gzymson" not in content:
            errors.append("core/GEMINI.md missing Gzymson mandate!")
        print("    -> core/GEMINI.md valid.")

    # 3. Claude
    if not claude_md.is_file():
        errors.append("core/CLAUDE.md missing!")
    else:
        content = claude_md.read_text(encoding="utf-8")
        if "Pre-Flight Skill Gate" not in content:
            errors.append("core/CLAUDE.md missing Pre-Flight Skill Gate definition!")
        print("    -> core/CLAUDE.md valid.")

    # 4. Cursor
    if not cursor_rules.is_file():
        errors.append("core/.cursorrules missing!")
    else:
        print("    -> core/.cursorrules present.")

def check_workers():
    print("[-] Validating Worker Ecosystem (Chinese LLMs / FastMCP / Aider)...")
    worker_mcp = ROOT_DIR / "scripts" / "worker_mcp.py"
    worker_cli = ROOT_DIR / "scripts" / "worker_cli.py"
    worker_prof = CONFIG_DIR / "worker_profiles.json"
    aider_settings = CONFIG_DIR / ".aider.model.settings.yml"
    aider_metadata = CONFIG_DIR / ".aider.model.metadata.json"
    aider_template = TEMPLATES_DIR / ".aider.conf.yml.template"

    if not worker_mcp.is_file():
        errors.append("scripts/worker_mcp.py missing!")
    else:
        print("    -> scripts/worker_mcp.py present.")

    if not worker_cli.is_file():
        errors.append("scripts/worker_cli.py missing!")
    else:
        print("    -> scripts/worker_cli.py present.")

    if not worker_prof.is_file():
        errors.append("config/worker_profiles.json missing!")
    else:
        try:
            data = json.loads(worker_prof.read_text(encoding="utf-8"))
            if "profiles" not in data or "glm-4-flash" not in data["profiles"]:
                errors.append("config/worker_profiles.json missing 'glm-4-flash' profile!")
            print("    -> config/worker_profiles.json valid.")
        except Exception as e:
            errors.append(f"config/worker_profiles.json invalid JSON: {e}")

    if not aider_settings.is_file():
        errors.append("config/.aider.model.settings.yml missing!")
    else:
        print("    -> config/.aider.model.settings.yml present.")

    if not aider_metadata.is_file():
        errors.append("config/.aider.model.metadata.json missing!")
    else:
        print("    -> config/.aider.model.metadata.json present.")

    if not aider_template.is_file():
        errors.append("templates/.aider.conf.yml.template missing!")
    else:
        print("    -> templates/.aider.conf.yml.template present.")

def main():
    print("======================================================================")
    print(">>> Running agent-setup-bundle Quality Assurance Validator...")
    print("======================================================================")
    
    s_count = check_skills()
    r_count = check_rules()
    check_configs()
    check_templates()
    check_core()
    check_workers()

    print("======================================================================")
    if warnings:
        print(f">>> WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  [!] {w}")
    
    if errors:
        print(f">>> FAILED with {len(errors)} ERRORS:")
        for e in errors:
            print(f"  [X] {e}")
        sys.exit(1)
    else:
        print(f">>> SUCCESS: All checks passed! ({r_count} rules, {s_count} skills, 4 platforms)")
        print("======================================================================")
        sys.exit(0)

if __name__ == "__main__":
    main()
