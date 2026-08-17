# Multi-Platform Agentic AI Environment & Skill Suite

> Production-ready, cross-platform configuration framework, system rules (Prime Directives), 24 modular skills (`agentskills.io` standard), and MCP configurations for **Antigravity / Gemini CLI**, **Claude Code**, and **Modern Cursor IDE (.mdc)**.

---

## Overview

Modern AI coding agents often suffer from common failure modes:
1. **Simulation & Mocking Traps:** Writing fake stubs or untested boilerplate without running tests.
2. **Context Window Flooding:** Inefficiently dumping thousands of prompt lines instead of on-demand skill discovery.
3. **Monolithic Spaghetti Code:** Creating giant files without clean architecture or boundary isolation.
4. **Hardware & Version Hallucinations:** Speculating about hardware capabilities or package versions without live verification.

**`agent-setup-bundle`** solves this by establishing a unified, multi-platform engineering operating system across your favorite AI coding assistants.

---

## Key Features

### 1. 10 Operational Core Rules (`~/.agents/rules/`)
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

### 2. 24 Production-Grade Skills (`~/.agents/skills/`)
All skills adhere to the open `agentskills.io` standard with progressive disclosure:

| Skill | Description & Trigger |
|---|---|
| **`skill-monorepo-architect`** | Polyglot monorepo management (`uv` Python workspaces + `pnpm`/Turborepo), shared-core pattern. |
| **`skill-plugin-architecture`** | Microkernel architecture, `BasePlugin`, dynamic discovery, and fault isolation. |
| **`skill-osint-engineering`** | Threat intelligence gathering, Pydantic entity graphs, pivoting, and OPSEC protocols. |
| **`skill-stealth-scraping`** | Anti-bot evasion (Cloudflare/DataDome), TLS fingerprint spoofing, headless browser automation. |
| **`spec-driven-development`** | Gated SDLC (Specify -> Plan -> Tasks -> Implement). |
| **`skill-backend-architect`** | Contract-first API design, database schemas, Pydantic/Zod boundaries. |
| **`skill-frontend-architect`** | Clean UI/UX architecture, state separation, accessibility, and performance. |
| **`skill-qa-engineer`** | Test-Driven Development (TDD Red-Green), TypeScript compilation safety gates. |
| **`doubt-driven-development`** | Fresh-context adversarial reviews to challenge false confidence. |
| **`skill-codebase-onboarding`** | Cartography and progressive disclosure for unfamiliar repositories. |
| **`skill-code-review`** | 5-axis systematic code review (correctness, readability, architecture, security, performance). |
| **`skill-system-diagnostics`** | Kernel, OS, hardware, and driver diagnostics. |
| **`skill-devops-cloud`** | Docker containers, CI/CD pipelines, and cloud infrastructure. |
| **`skill-data-science`** | Data ingestion pipelines, exploratory data analysis, and validation. |
| **`skill-data-analysis`** | Statistical analysis, hypothesis testing, and anomaly detection. |
| **`skill-ai-ml`** | LLM model integrations, embeddings, vector databases, and agent workflows. |
| **`skill-graph-analytics`** | Graph databases (Neo4j), topology analysis, and Graph Data Science. |
| **`skill-graphics-webgl`** | 2D/3D WebGL scenes, Three.js, and Canvas animations. |
| **`marketing-copywriting`** | Conversion-focused technical copywriting. |
| **`avoid-ai-writing`** | Detection and removal of AI writing clichés and robotic patterns. |
| **`seo-optimization-and-audit`** | Web metadata, Core Web Vitals, and search ranking optimization. |
| **`skill-research`** | Rigorous technical and academic multi-source research. |
| **`skill-resume-tailor`** | ATS-optimized resume, CV, and cover letter tailoring. |
| **`skill-web-architecture`** | Full-stack web architectural standards and API contracts. |

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
./install.sh --gemini    # Configure Antigravity / Gemini CLI only
./install.sh --claude    # Configure Claude Code only
./install.sh --cursor    # Configure Cursor IDE only
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
