#!/usr/bin/env bash
# ==============================================================================
# Installer: Multi-Platform Agent Environment & Skill Suite
# Supported: Antigravity / Gemini CLI, Claude Code, Modern Cursor IDE (.mdc)
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_AGENTS_DIR="${HOME}/.agents"
TARGET_GEMINI_DIR="${HOME}/.gemini"
TARGET_CLAUDE_DIR="${HOME}/.claude"
TARGET_CURSOR_DIR="${HOME}/.cursor"

INSTALL_GEMINI=true
INSTALL_CLAUDE=true
INSTALL_CURSOR=true

# Parse optional arguments
if [ $# -gt 0 ]; then
    case "$1" in
        --gemini)
            INSTALL_CLAUDE=false
            INSTALL_CURSOR=false
            ;;
        --claude)
            INSTALL_GEMINI=false
            INSTALL_CURSOR=false
            ;;
        --cursor)
            INSTALL_GEMINI=false
            INSTALL_CLAUDE=false
            ;;
        --all)
            # Default
            ;;
        --help|-h)
            echo "Usage: ./install.sh [OPTION]"
            echo "Options:"
            echo "  --all       Install configuration for all environments (default)"
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
echo ">>> Rozpoczynam instalacje srodowiska Agenta AI..."
echo "======================================================================"

# 0. Instalacja bazy wspolnej (Skills & Rules w ~/.agents/)
echo "[+] Kopiowanie wspoldzielonych regul (12) i skilli (33) do ~/.agents/..."
mkdir -p "${TARGET_AGENTS_DIR}/rules"
mkdir -p "${TARGET_AGENTS_DIR}/skills"

cp -r "${SCRIPT_DIR}/rules/"* "${TARGET_AGENTS_DIR}/rules/"
cp -r "${SCRIPT_DIR}/skills/"* "${TARGET_AGENTS_DIR}/skills/"
echo "    -> Zainstalowano 12 regul i 33 skilli w ~/.agents/"

# 1. Tworzenie konfiguracji dla Gemini CLI / Antigravity
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

# 2. Instalacja dla Claude Code
if [ "$INSTALL_CLAUDE" = true ]; then
    echo "[+] Konfiguracja srodowiska Claude Code (~/.claude/)..."
    mkdir -p "${TARGET_CLAUDE_DIR}/agents"
    cp "${SCRIPT_DIR}/core/CLAUDE.md" "${TARGET_CLAUDE_DIR}/CLAUDE.md"
    cp -r "${SCRIPT_DIR}/core/claude/agents/"* "${TARGET_CLAUDE_DIR}/agents/"
    echo "    -> Zainstalowano CLAUDE.md oraz subagentow w ~/.claude/agents/"
fi

# 3. Instalacja dla Cursor IDE (Modern MDC format)
if [ "$INSTALL_CURSOR" = true ]; then
    echo "[+] Konfiguracja regul Modern Cursor (~/.cursor/rules/*.mdc)..."
    mkdir -p "${TARGET_CURSOR_DIR}/rules"
    cp -r "${SCRIPT_DIR}/core/cursor/rules/"* "${TARGET_CURSOR_DIR}/rules/"
    if [ ! -f "${TARGET_CURSOR_DIR}/mcp.json" ]; then
        cp "${SCRIPT_DIR}/config/cursor_mcp.json" "${TARGET_CURSOR_DIR}/mcp.json"
        echo "    -> Utworzono ~/.cursor/mcp.json (szablon)"
    fi
fi

# 4. Podsumowanie
echo "======================================================================"
echo ">>> SUKCES: Srodowisko agenta zostalo w pelni zainstalowane!"
echo ">>> Zainstalowane komponenty:"
echo "    - Shared Suite: ~/.agents/ (12 reguł, 33 skille)"
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
echo "    1. Uzupelnij wlasne klucze API w plikach settings.json / mcp.json (np. GITHUB_PERSONAL_ACCESS_TOKEN)."
echo "    2. W pliku ~/.agents/rules/system-identity.md wpisz bazowe dane swojego sprzetu (CPU, GPU, RAM)."
echo "======================================================================"
