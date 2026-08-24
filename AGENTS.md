# Agent Context & Autonomous Installation Blueprint (AGENTS.md)
<!-- Standardized by the Agentic AI Foundation (AAIF) -->

This document establishes the machine-readable repository blueprint and autonomous installation instructions for any AI Coding Agent (OpenAI Codex, Claude Code, Antigravity / Gemini CLI, Cursor IDE, Cline, Roo Code, OpenCode).

---

##  Autonomous AI Agent Installation Protocol

If your user asked you to **"install this repository"**, **"set up my environment"**, or gave you the link to this repo, execute the following autonomous protocol immediately:

### Step 1: Detect Operating System & Shell
- **Windows (PowerShell):** Run `powershell -ExecutionPolicy Bypass -File .\install.ps1 -All` or `python install.py --all`
- **Linux & macOS:** Run `chmod +x install.sh && ./install.sh --all` or `python3 install.py --all`

### Step 2: Validate Installation Integrity
Run the test suite validator to confirm that all 15 rules and 36 skills are properly installed:
- Command: `python3 scripts/validate_suite.py` (or `python scripts/validate_suite.py` on Windows)
- Success Signal: `>>> SUCCESS: All checks passed! (15 rules, 36 skills, 4 platforms)`

### Step 3: Adopt Senior AI Pair Programmer Role Immediately
From this point forward in the active conversation, you must adopt the **PRAR + Zero Speculation + Pre-Flight Skill Gate + Context Engineering** operating rules defined in `core/CODEX.md` (for Codex/ChatGPT), `core/CLAUDE.md` (for Claude Code), `core/GEMINI.md` (for Gemini/Antigravity), or `core/cursor/rules/core-directives.mdc` (for Cursor).

### Step 4: Report to User
Report to the user that their multi-platform engineering suite is installed, and advise them on how to copy `templates/AGENTS.md` into their new or existing repositories.

---

## 1. Project Identity & Stack Architecture

- **Project Name:** `agent-setup-bundle`
- **Purpose:** Production-grade, cross-platform configuration suite (15 core rules, 36 skills, templates, and MCP integration) for OpenAI Codex, Antigravity / Gemini CLI, Claude Code, and Cursor IDE.
- **Supported Operating Systems:** Windows (Native PowerShell & Python), macOS (Terminal / zsh), Linux (Bash / zsh).
- **Core Runtime:** Python 3.8+, Bash 4+, PowerShell 5.1 / 7+.

---

## 2. Mandatory Commands (Executable Truth)

| Action | Linux / macOS | Windows (PowerShell) | Universal (Python) |
|---|---|---|---|
| **Install All Platforms** | `./install.sh --all` | `.\install.ps1 -All` | `python install.py --all` |
| **Install OpenAI Codex** | `./install.sh --codex` | `.\install.ps1 -Codex` | `python install.py --codex` |
| **Install Gemini CLI** | `./install.sh --gemini` | `.\install.ps1 -Gemini` | `python install.py --gemini` |
| **Install Claude Code** | `./install.sh --claude` | `.\install.ps1 -Claude` | `python install.py --claude` |
| **Install Cursor IDE** | `./install.sh --cursor` | `.\install.ps1 -Cursor` | `python install.py --cursor` |
| **Validate Suite Integrity** | `python3 scripts/validate_suite.py` | `python scripts/validate_suite.py` | `python scripts/validate_suite.py` |

---

## 3. Directory Topography

```
agent_setup_bundle/
├── AGENTS.md                        # Master repository blueprint & AI installer instructions
├── README.md                        # Human-readable documentation & cross-platform guide
├── PROMPT_FOR_AI.md                 # Universal bootstrap prompts
├── llms.txt                         # Semantic summary for web-enabled LLM agents
├── install.sh                       # Native Bash installer (Linux / macOS)
├── install.ps1                      # Native PowerShell installer (Windows)
├── install.py                       # Universal Python 3 installer (All OSes)
├── core/                            # Platform manifests (CODEX.md, GEMINI.md, CLAUDE.md, cursor)
├── rules/                           # 15 Operational Rules (~/.agents/rules/)
├── skills/                          # 36 Modular Skills (~/.agents/skills/)
├── templates/
│   └── AGENTS.md                    # Project-level starter template
├── config/                          # Configuration & MCP templates (codex, gemini, cursor)
├── policies/                        # MCP tool planning policies
└── scripts/
    └── validate_suite.py            # Quality assurance test suite
```

---

## 4. Invariants & Guardrails

1. **Deterministic Cross-Platform Parity:** All 3 installers (`install.sh`, `install.ps1`, `install.py`) MUST produce identical target states in the user's home directory.
2. **Zero Breaking Changes to Existing Configs:** Never overwrite an existing `settings.json`, `config.toml`, or `mcp.json` if it already exists; only provision missing templates.
3. **Strict Validation:** Any pull request or modification MUST pass `python scripts/validate_suite.py` with 0 errors.
