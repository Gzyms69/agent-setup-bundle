#!/usr/bin/env python3
"""
Installer: Multi-Platform Agent Environment & Skill Suite (Universal Python)
Supported: OpenAI Codex, Antigravity / Gemini CLI, Claude Code, Cursor IDE (.mdc)
"""

import sys
import os
import shutil
import argparse
from pathlib import Path

def copy_tree(src: Path, dst: Path):
    """Recursively copy directory tree, overwriting existing files."""
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            copy_tree(item, target)
        else:
            shutil.copy2(item, target)

def create_symlink_or_copy(src: Path, dst: Path, desc: str):
    """Create symlink if possible, fallback to copy."""
    if dst.exists() or dst.is_symlink():
        if dst.is_symlink():
            dst.unlink()
        elif dst.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()
            
    try:
        dst.symlink_to(src, target_is_directory=True)
        print(f"    -> Utworzono dowiazanie symboliczne dla {desc}: {dst} -> {src}")
    except (OSError, NotImplementedError):
        copy_tree(src, dst)
        print(f"    -> Skopiowano {desc} do: {dst} (fallback)")

def main():
    parser = argparse.ArgumentParser(description="Instalator srodowiska Agenta AI")
    parser.add_argument("--all", action="store_true", help="Instaluj dla wszystkich platform (default)")
    parser.add_argument("--codex", action="store_true", help="Instaluj tylko dla OpenAI Codex")
    parser.add_argument("--gemini", action="store_true", help="Instaluj tylko dla Antigravity / Gemini CLI")
    parser.add_argument("--claude", action="store_true", help="Instaluj tylko dla Claude Code")
    parser.add_argument("--cursor", action="store_true", help="Instaluj tylko dla Cursor IDE")

    args = parser.parse_args()

    # Domyslnie instaluj wszystko, jesli nie podano specyficznej platformy
    install_all = not (args.codex or args.gemini or args.claude or args.cursor)
    install_codex  = args.all or args.codex or install_all
    install_gemini = args.all or args.gemini or install_all
    install_claude = args.all or args.claude or install_all
    install_cursor = args.all or args.cursor or install_all

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
    print("[+] Kopiowanie wspoldzielonych regul (16), skilli (36) i szablonow do ~/.agents/...")
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
    print("    -> Zainstalowano 16 regul, 36 skilli oraz szablony w ~/.agents/")

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
    print("    - Shared Suite: ~/.agents/ (16 regul, 36 skilli, szablony AGENTS.md)")
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
    print("    1. Sprawdz plik ~/.gemini/settings.json lub ~/.codex/config.toml")
    print("    2. Aby dodac kontekst projektu, skopiuj ~/.agents/templates/AGENTS.md do katalogu swojego repozytorium")
    print("=" * 70)

if __name__ == "__main__":
    main()
