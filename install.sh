#!/usr/bin/env bash
# ==============================================================================
# Installer: Multi-Platform Agent Environment & Skill Suite
# Supported: OpenAI Codex, Antigravity / Gemini CLI, Claude Code, Cursor IDE (.mdc)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_AGENTS_DIR="${HOME}/.agents"
TARGET_GEMINI_DIR="${HOME}/.gemini"
TARGET_CLAUDE_DIR="${HOME}/.claude"
TARGET_CURSOR_DIR="${HOME}/.cursor"
TARGET_CODEX_DIR="${HOME}/.codex"

INSTALL_GEMINI=true
INSTALL_CLAUDE=true
INSTALL_CURSOR=true
INSTALL_CODEX=true

# Parse optional arguments
if [ $# -gt 0 ]; then
    case "$1" in
        --gemini)
            INSTALL_CLAUDE=false
            INSTALL_CURSOR=false
            INSTALL_CODEX=false
            ;;
        --claude)
            INSTALL_GEMINI=false
            INSTALL_CURSOR=false
            INSTALL_CODEX=false
            ;;
        --cursor)
            INSTALL_GEMINI=false
            INSTALL_CLAUDE=false
            INSTALL_CODEX=false
            ;;
        --codex)
            INSTALL_GEMINI=false
            INSTALL_CLAUDE=false
            INSTALL_CURSOR=false
            ;;
        --all)
            # Default: install all platforms
            ;;
        --help|-h)
            echo "Usage: ./install.sh [OPTION]"
            echo "Options:"
            echo "  --all       Install configuration for all platforms (default: Codex, Gemini, Claude, Cursor)"
            echo "  --codex     Install configuration for OpenAI Codex only"
            echo "  --gemini    Install configuration for Antigravity / Gemini CLI only"
            echo "  --claude    Install configuration for Claude Code only"
            echo "  --cursor    Install configuration for Cursor IDE only"
            exit 0
            ;;
        *)
            echo "Unknown option: $1. Run with --help for options."
            exit 1
            ;;
    esac
fi

echo "======================================================================"
echo ">>> Rozpoczynam instalacje srodowiska Agenta AI (Multi-Platform)..."
echo "======================================================================"

# 0. Instalacja bazy wspolnej (Rules, Skills, Templates w ~/.agents/)
echo "[+] Kopiowanie wspoldzielonych regul (13), skilli (33) i szablonow do ~/.agents/..."
mkdir -p "${TARGET_AGENTS_DIR}/rules"
mkdir -p "${TARGET_AGENTS_DIR}/skills"
mkdir -p "${TARGET_AGENTS_DIR}/templates"

cp -r "${SCRIPT_DIR}/rules/"* "${TARGET_AGENTS_DIR}/rules/"
cp -r "${SCRIPT_DIR}/skills/"* "${TARGET_AGENTS_DIR}/skills/"
if [ -d "${SCRIPT_DIR}/templates" ]; then
    cp -r "${SCRIPT_DIR}/templates/"* "${TARGET_AGENTS_DIR}/templates/"
fi
echo "    -> Zainstalowano 13 regul, 33 skille oraz szablony w ~/.agents/"

# 1. Konfiguracja dla OpenAI Codex
if [ "$INSTALL_CODEX" = true ]; then
    echo "[+] Konfiguracja srodowiska OpenAI Codex (~/.codex/)..."
    mkdir -p "${TARGET_CODEX_DIR}/skills"

    cp "${SCRIPT_DIR}/core/CODEX.md" "${TARGET_CODEX_DIR}/instructions.md"
    cp "${SCRIPT_DIR}/core/CODEX.md" "${TARGET_CODEX_DIR}/CODEX.md"
    
    if [ ! -f "${TARGET_CODEX_DIR}/config.toml" ]; then
        cp "${SCRIPT_DIR}/config/codex_config.toml" "${TARGET_CODEX_DIR}/config.toml"
        echo "    -> Utworzono ~/.codex/config.toml (szablon z konfiguracja MCP)"
    fi

    # Utworzenie powiazania ze skillami
    if [ ! -L "${TARGET_CODEX_DIR}/skills/custom" ] && [ ! -d "${TARGET_CODEX_DIR}/skills/custom" ]; then
        ln -s "${TARGET_AGENTS_DIR}/skills" "${TARGET_CODEX_DIR}/skills/custom"
        echo "    -> Podpieto skille ~/.agents/skills -> ~/.codex/skills/custom"
    fi
    echo "    -> Zainstalowano CODEX.md oraz instructions.md w ~/.codex/"
fi

# 2. Tworzenie konfiguracji dla Gemini CLI / Antigravity
if [ "$INSTALL_GEMINI" = true ]; then
    echo "[+] Konfiguracja srodowiska Antigravity / Gemini CLI (~/.gemini/)..."
    mkdir -p "${TARGET_GEMINI_DIR}/policies"
    mkdir -p "${TARGET_GEMINI_DIR}/config"

    cp "${SCRIPT_DIR}/core/GEMINI.md" "${TARGET_GEMINI_DIR}/GEMINI.md"
    cp "${SCRIPT_DIR}/policies/mcp-planning.toml" "${TARGET_GEMINI_DIR}/policies/mcp-planning.toml"

    if [ ! -f "${TARGET_GEMINI_DIR}/settings.json" ]; then
        cp "${SCRIPT_DIR}/config/settings.json" "${TARGET_GEMINI_DIR}/settings.json"
        echo "    -> Utworzono ~/.gemini/settings.json (szablon)"
    fi
    if [ ! -f "${TARGET_GEMINI_DIR}/config/mcp_config.json" ]; then
        cp "${SCRIPT_DIR}/config/mcp_config.json" "${TARGET_GEMINI_DIR}/config/mcp_config.json"
        echo "    -> Utworzono ~/.gemini/config/mcp_config.json (szablon)"
    fi
fi

# 3. Instalacja dla Claude Code
if [ "$INSTALL_CLAUDE" = true ]; then
    echo "[+] Konfiguracja srodowiska Claude Code (~/.claude/)..."
    mkdir -p "${TARGET_CLAUDE_DIR}/agents"
    cp "${SCRIPT_DIR}/core/CLAUDE.md" "${TARGET_CLAUDE_DIR}/CLAUDE.md"
    cp -r "${SCRIPT_DIR}/core/claude/agents/"* "${TARGET_CLAUDE_DIR}/agents/"
    echo "    -> Zainstalowano CLAUDE.md oraz subagentow w ~/.claude/agents/"
fi

# 4. Instalacja dla Cursor IDE (Modern MDC format)
if [ "$INSTALL_CURSOR" = true ]; then
    echo "[+] Konfiguracja regul Modern Cursor (~/.cursor/rules/*.mdc)..."
    mkdir -p "${TARGET_CURSOR_DIR}/rules"
    cp -r "${SCRIPT_DIR}/core/cursor/rules/"* "${TARGET_CURSOR_DIR}/rules/"
    if [ ! -f "${TARGET_CURSOR_DIR}/mcp.json" ]; then
        cp "${SCRIPT_DIR}/config/cursor_mcp.json" "${TARGET_CURSOR_DIR}/mcp.json"
        echo "    -> Utworzono ~/.cursor/mcp.json (szablon)"
    fi
fi

# 5. Podsumowanie
echo "======================================================================"
echo ">>> SUKCES: Srodowisko agenta zostalo w pelni zainstalowane!"
echo ">>> Zainstalowane komponenty:"
echo "    - Shared Suite: ~/.agents/ (13 regul, 33 skille, szablony AGENTS.md)"
if [ "$INSTALL_CODEX" = true ]; then
    echo "    - OpenAI Codex: ~/.codex/ (instructions.md, CODEX.md, config.toml, skills link)"
fi
if [ "$INSTALL_GEMINI" = true ]; then
    echo "    - Antigravity / Gemini CLI: ~/.gemini/ (GEMINI.md, settings.json, policies)"
fi
if [ "$INSTALL_CLAUDE" = true ]; then
    echo "    - Claude Code: ~/.claude/ (CLAUDE.md, .claude/agents/)"
fi
if [ "$INSTALL_CURSOR" = true ]; then
    echo "    - Cursor IDE: ~/.cursor/ (rules/*.mdc, mcp.json)"
fi
echo ""
echo ">>> Wskazowki konfiguracji:"
echo "    1. Skopiuj templates/AGENTS.md do korzenia swoich projektow (np. ~/Dev Projects/MyProject/AGENTS.md)."
echo "    2. Uzupelnij wlasne klucze API w plikach settings.json / config.toml / mcp.json (np. GITHUB_PERSONAL_ACCESS_TOKEN)."
echo "    3. W pliku ~/.agents/rules/system-identity.md wpisz bazowe dane swojego sprzetu (CPU, GPU, RAM)."
echo "======================================================================"
