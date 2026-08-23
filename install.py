#!/usr/bin/env python3
"""
install.py
Universal Multi-Platform Installer for Agent Engineering Suite
Works natively on Windows, macOS, and Linux without external dependencies.
Supported: OpenAI Codex, Antigravity / Gemini CLI, Claude Code, Cursor IDE (.mdc)
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

def copy_tree(src: Path, dst: Path):
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            copy_tree(item, target)
        else:
            shutil.copy2(item, target)

def create_symlink_or_copy(src: Path, link_target: Path, label: str):
    if link_target.exists() or link_target.is_symlink():
        return
    try:
        link_target.symlink_to(src, target_is_directory=True)
        print(f"    -> Podpieto link symboliczny dla {label}: {link_target}")
    except (OSError, NotImplementedError):
        # Fallback to copy on Windows without developer mode
        copy_tree(src, link_target)
        print(f"    -> Skopiowano katalog dla {label} (brak uprawnien do symlinkow): {link_target}")

def main():
    parser = argparse.ArgumentParser(description="Universal Multi-Platform Agent Suite Installer")
    parser.add_argument("--all", action="store_true", help="Install configuration for all platforms (default)")
    parser.add_argument("--codex", action="store_true", help="Install for OpenAI Codex only")
    parser.add_argument("--gemini", action="store_true", help="Install for Antigravity / Gemini CLI only")
    parser.add_argument("--claude", action="store_true", help="Install for Claude Code only")
    parser.add_argument("--cursor", action="store_true", help="Install for Cursor IDE only")
    args = parser.parse_args()

    # Determine platforms
    specific = any([args.codex, args.gemini, args.claude, args.cursor])
    install_codex  = args.all or args.codex  or not specific
    install_gemini = args.all or args.gemini or not specific
    install_claude = args.all or args.claude or not specific
    install_cursor = args.all or args.cursor or not specific

    script_dir = Path(__file__).resolve().parent
    home_dir = Path.home()

    target_agents_dir = home_dir / ".agents"
    target_gemini_dir = home_dir / ".gemini"
    target_claude_dir = home_dir / ".claude"
    target_cursor_dir = home_dir / ".cursor"
    target_codex_dir  = home_dir / ".codex"

    print("=" * 70)
    print(f">>> Rozpoczynam instalacje srodowiska Agenta AI (Platform: {sys.platform})...")
    print("=" * 70)

    # 0. Shared Base: ~/.agents/ (Rules, Skills, Templates)
    print("[+] Kopiowanie wspoldzielonych regul (13), skilli (33) i szablonow do ~/.agents/...")
    rules_target = target_agents_dir / "rules"
    skills_target = target_agents_dir / "skills"
    templates_target = target_agents_dir / "templates"

    rules_target.mkdir(parents=True, exist_ok=True)
    skills_target.mkdir(parents=True, exist_ok=True)
    templates_target.mkdir(parents=True, exist_ok=True)

    copy_tree(script_dir / "rules", rules_target)
    copy_tree(script_dir / "skills", skills_target)
    if (script_dir / "templates").is_dir():
        copy_tree(script_dir / "templates", templates_target)
    print("    -> Zainstalowano 13 regul, 33 skille oraz szablony w ~/.agents/")

    # 1. OpenAI Codex
    if install_codex:
        print("[+] Konfiguracja srodowiska OpenAI Codex (~/.codex/)...")
        target_codex_dir.mkdir(parents=True, exist_ok=True)
        codex_skills_dir = target_codex_dir / "skills"
        codex_skills_dir.mkdir(parents=True, exist_ok=True)

        codex_md_src = script_dir / "core" / "CODEX.md"
        shutil.copy2(codex_md_src, target_codex_dir / "AGENTS.md")
        shutil.copy2(codex_md_src, target_codex_dir / "instructions.md")
        shutil.copy2(codex_md_src, target_codex_dir / "CODEX.md")

        codex_config = target_codex_dir / "config.toml"
        if not codex_config.exists():
            shutil.copy2(script_dir / "config" / "codex_config.toml", codex_config)
            print("    -> Utworzono ~/.codex/config.toml (szablon)")

        create_symlink_or_copy(skills_target, codex_skills_dir / "custom", "Codex skille")
        print("    -> Zainstalowano AGENTS.md, CODEX.md oraz instructions.md w ~/.codex/")

    # 2. Antigravity / Gemini CLI
    if install_gemini:
        print("[+] Konfiguracja srodowiska Antigravity / Gemini CLI (~/.gemini/)...")
        (target_gemini_dir / "policies").mkdir(parents=True, exist_ok=True)
        (target_gemini_dir / "config").mkdir(parents=True, exist_ok=True)

        shutil.copy2(script_dir / "core" / "GEMINI.md", target_gemini_dir / "GEMINI.md")
        shutil.copy2(script_dir / "policies" / "mcp-planning.toml", target_gemini_dir / "policies" / "mcp-planning.toml")

        settings_json = target_gemini_dir / "settings.json"
        if not settings_json.exists():
            shutil.copy2(script_dir / "config" / "settings.json", settings_json)
            print("    -> Utworzono ~/.gemini/settings.json (szablon)")
        
        mcp_config = target_gemini_dir / "config" / "mcp_config.json"
        if not mcp_config.exists():
            shutil.copy2(script_dir / "config" / "mcp_config.json", mcp_config)
            print("    -> Utworzono ~/.gemini/config/mcp_config.json (szablon)")

    # 3. Claude Code
    if install_claude:
        print("[+] Konfiguracja srodowiska Claude Code (~/.claude/)...")
        (target_claude_dir / "agents").mkdir(parents=True, exist_ok=True)

        shutil.copy2(script_dir / "core" / "CLAUDE.md", target_claude_dir / "CLAUDE.md")
        copy_tree(script_dir / "core" / "claude" / "agents", target_claude_dir / "agents")

        create_symlink_or_copy(skills_target, target_claude_dir / "skills", "Claude skille")

        claude_mcp = target_claude_dir / "mcp.json"
        if not claude_mcp.exists():
            shutil.copy2(script_dir / "config" / "mcp_config.json", claude_mcp)
            print("    -> Utworzono ~/.claude/mcp.json (szablon)")
        print("    -> Zainstalowano CLAUDE.md oraz subagentow w ~/.claude/agents/")

    # 4. Cursor IDE
    if install_cursor:
        print("[+] Konfiguracja regul Modern Cursor (~/.cursor/rules/*.mdc)...")
        cursor_rules_dir = target_cursor_dir / "rules"
        cursor_rules_dir.mkdir(parents=True, exist_ok=True)

        copy_tree(script_dir / "core" / "cursor" / "rules", cursor_rules_dir)
        cursor_mcp = target_cursor_dir / "mcp.json"
        if not cursor_mcp.exists():
            shutil.copy2(script_dir / "config" / "cursor_mcp.json", cursor_mcp)
            print("    -> Utworzono ~/.cursor/mcp.json (szablon)")

    print("=" * 70)
    print(">>> SUKCES: Srodowisko agenta zostalo w pelni zainstalowane!")
    print(">>> Zainstalowane komponenty:")
    print("    - Shared Suite: ~/.agents/ (13 regul, 33 skille, szablony AGENTS.md)")
    if install_codex:
        print("    - OpenAI Codex: ~/.codex/ (AGENTS.md, instructions.md, config.toml, skills link)")
    if install_gemini:
        print("    - Antigravity / Gemini CLI: ~/.gemini/ (GEMINI.md, settings.json, policies)")
    if install_claude:
        print("    - Claude Code: ~/.claude/ (CLAUDE.md, .claude/agents/, skills link, mcp.json)")
    if install_cursor:
        print("    - Cursor IDE: ~/.cursor/ (rules/*.mdc, mcp.json)")
    print()
    print(">>> Wskazowki konfiguracji:")
    print("    1. Skopiuj templates/AGENTS.md do korzenia swoich projektow.")
    print("    2. Uzupelnij klucze API w settings.json / config.toml / mcp.json.")
    print("    3. W ~/.agents/rules/system-identity.md wpisz bazowe dane swojego sprzetu.")
    print("=" * 70)

if __name__ == "__main__":
    main()
