# Multi-Platform Agentic AI Environment & Skill Suite

> Production-ready, cross-platform configuration framework, system rules (Prime Directives), 33 modular skills (`agentskills.io` standard), `AGENTS.md` open template, and MCP configurations for **Antigravity / Gemini CLI**, **Claude Code**, and **Modern Cursor IDE (.mdc)**.

---

## Overview

Modern AI coding agents often suffer from common failure modes:
1. **Simulation & Mocking Traps:** Writing fake stubs or untested boilerplate without running tests.
2. **Context Window Flooding & Skill Misses:** Blindly grepping code without running repository cartography or skipping planning gates.
3. **Monolithic Spaghetti Code:** Creating giant files without clean architecture or boundary isolation.
4. **Hardware & Version Hallucinations:** Speculating about hardware capabilities or package versions without live verification.

**`agent-setup-bundle`** solves this by establishing a unified, multi-platform engineering operating system and a **4-Phase Pre-Flight Skill Gate** across your AI coding assistants.

---

## Key Features

### 1. 13 Operational Core Rules (`~/.agents/rules/`)
* **`skill-orchestration.md`** — **MANDATORY PRE-FLIGHT SKILL GATE:** 4-Phase sequential resolution (Phase 0: Cartography -> Phase 1: Planning -> Phase 2: Domain -> Phase 3: QA).
* **`modular-architecture.md`** — Anti-Monolith constraint (max ~150-200 lines), Clean/Hexagonal architecture, strict layer direction, typed boundary contracts.
* **`zero-speculation.md`** — Total ban on guessing versions, APIs, or system states without live verification.
* **`systemic-excellence.md`** — Anti-workaround protocol, single source of truth (SSOT), and DRY enforcement.
* **`system-identity.md`** — Hardware & OS baseline template to prevent environment hallucinations.
* **`subagent-economy.md`** — Dynamic tiering of LLM models based on task complexity.
* **`problem-isolation.md`** — Strict scope containment and root cause debugging.
* **`command-verification.md`** — Mandatory read-only verification after running commands.
* **`env-integrity.md`** — Environment sanity checks before modifying project files.
* **`error-triage.md`** — Diagnostic priority order (Docs -> Web -> Code).
* **`full-log-reporting.md`** — Ban on truncated or paraphrased error reporting.
* **`mempalace-discovery.md`** — Mandatory MemPalace knowledge retrieval before unconstrained disk searches.
* **`mcp-master-playbook.md`** — Complete 11-server MCP execution matrix, boundaries, and synergies.

### 2. 33 Production-Grade Skills (`~/.agents/skills/`)
All skills adhere to the open `agentskills.io` standard with progressive disclosure and crisp trigger invariants:

| Phase / Category | Skills |
|---|---|
| **Phase 0: Cartography & Discovery** | `skill-codebase-onboarding`, `spec-miner` |
| **Phase 1: Planning & Architecture** | `spec-driven-development`, `skill-monorepo-architect`, `skill-plugin-architecture`, `skill-web-architecture` |
| **Phase 2: Frontend & Design** | `skill-frontend-architect`, `skill-design-engineering`, `skill-creative-design`, `skill-graphics-webgl` |
| **Phase 2: Backend & Systems** | `skill-backend-architect`, `c-cpp-systems`, `skill-low-level-programming`, `wasm-emscripten`, `retro-emulation-engineering`, `skill-emulator-wasm` |
| **Phase 2: AI, Data & Graphs** | `skill-ai-ml`, `skill-data-science`, `skill-data-analysis`, `skill-graph-analytics` |
| **Phase 2: Specialized Workflows** | `skill-stealth-scraping`, `skill-osint-engineering`, `skill-resume-tailor`, `marketing-copywriting`, `avoid-ai-writing`, `seo-optimization-and-audit`, `skill-web-performance`, `skill-system-diagnostics`, `skill-devops-cloud`, `skill-research` |
| **Phase 3: QA & Verification** | `skill-qa-engineer` (TDD, TSC check), `skill-code-review` (5-axis audit), `doubt-driven-development` |

### 3. Open Standards & Tooling
* **`templates/AGENTS.md`** — Standard Agentic AI Foundation (AAIF) repository context specification template.
* **`scripts/validate_suite.py`** — Automated YAML frontmatter, character limit, and cross-platform integrity test suite.

---

## 1-Click Quickstart Installation

Clone and run the installer in your environment:

```bash
git clone https://github.com/Gzyms69/agent-setup-bundle.git
cd agent-setup-bundle
./install.sh
```

### Installation Options:
```bash
./install.sh --all       # Configure all platforms (default)
./install.sh --symlink   # Install with live symlinks for live development (dev mode)
./install.sh --gemini    # Configure Antigravity / Gemini CLI only
./install.sh --claude    # Configure Claude Code only
./install.sh --cursor    # Configure Cursor IDE only
```

### Run Quality Gate Validation:
```bash
python3 scripts/validate_suite.py
```

---

## Configuration & Setup

1. **Configure API Keys:**
   - Update `~/.gemini/settings.json` or `~/.cursor/mcp.json` with your GitHub token (`GITHUB_PERSONAL_ACCESS_TOKEN`) or Google API Key if using MCP servers.
2. **System Baseline:**
   - Customize `~/.agents/rules/system-identity.md` with your system's hardware specs (CPU, GPU, RAM) to prevent the AI from guessing system capabilities.

---

## Supported Environments

| Platform | Manifest Location | Rule Format | Skill Support |
|---|---|---|---|
| **Antigravity / Gemini CLI** | `~/.gemini/GEMINI.md` | `~/.agents/rules/*.md` | `~/.agents/skills/` |
| **Claude Code** | `~/.claude/CLAUDE.md` | `CLAUDE.md` + `.claude/agents/` | `~/.agents/skills/` |
| **Cursor IDE** | Root / Project | `.cursor/rules/*.mdc` | On-demand docs |

---

## License

This project is licensed under the [MIT License](LICENSE).
