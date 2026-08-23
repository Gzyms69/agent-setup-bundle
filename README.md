# Multi-Platform Agentic AI Engineering Operating System & Skill Suite

> Production-ready, cross-platform configuration framework, system rules (Prime Directives), 33 modular skills (`agentskills.io` standard), repository blueprints (`AGENTS.md`), and Model Context Protocol (MCP) configurations for **OpenAI Codex**, **Antigravity / Gemini CLI**, **Claude Code**, and **Modern Cursor IDE (.mdc)**.

---

## 1. Executive Summary & Philosophy

Traditional approaches to AI pair programming ("Just write this feature") fail consistently on non-trivial codebases due to four core traps:
1. **Simulation & Mocking Traps:** Writing fake stubs or untested boilerplate without running verification suites.
2. **Context Window Flooding:** Inefficiently dumping thousands of prompt lines instead of on-demand skill discovery.
3. **Monolithic Spaghetti Code:** Creating giant "god files" (>150 lines) that mix state, presentation, networking, and styles.
4. **Hardware & Version Hallucinations:** Speculating about hardware capabilities, compiler flags, or package versions without live verification.

**`agent-setup-bundle`** solves this by establishing a deterministic, multi-platform engineering operating system across all major coding assistants.

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                           MULTI-PLATFORM AGENT OPERATING SYSTEM                          │
├───────────────────┬────────────────────────┬─────────────────────┬───────────────────────┤
│   OpenAI Codex    │ Antigravity / Gemini   │     Claude Code     │    Cursor IDE (.mdc)  │
│ (~/.codex/inst.)  │    (~/.gemini/GEMINI)  │  (~/.claude/CLAUDE) │  (~/.cursor/rules/)   │
└─────────┬─────────┴───────────┬────────────┴──────────┬──────────┴───────────┬───────────┘
          │                     │                       │                      │
          └─────────────────────┴───────────┬───────────┴──────────────────────┘
                                            │
                                            ▼
                    ┌───────────────────────────────────────────────┐
                    │       SHARED SUITE LAYER (~/.agents/)         │
                    ├───────────────────────────────────────────────┤
                    │ • 13 Operational Core Rules (Zero Spec, Root) │
                    │ • 33 Production-Grade Skills (agentskills.io) │
                    │ • Repository-Level Blueprints (AGENTS.md)     │
                    │ • Model Context Protocol (MCP Playbook)       │
                    └───────────────────────────────────────────────┘
```

---

## 2. Core Engineering Mandates (The Laws of Robotics)

Every agent configured with this suite strictly adheres to the following non-negotiable protocols:

1. **PRAR Workflow (Perceive, Reason, Act, Refine):**
   - Agents never write code blindly. Every task begins with environmental analysis (Perceive), architectural design (Reason), surgical modifications (Act), and verification (Refine).
2. **Mandatory 4-Phase Pre-Flight Skill Gate:**
   - Before executing file discovery (`grep`, `find`, `cat`) or modifying code, agents must evaluate and load domain skills in a strict 4-phase sequence.
3. **The Wait-For-GO Mandate:**
   - On tasks requiring architectural decisions, touching >3 files, or introducing new dependencies, agents must present a detailed implementation plan and wait for an explicit user approval ("GO") before mutating files.
4. **Zero Speculation Protocol:**
   - Total ban on guessing hardware specs, software versions, API endpoints, error causes, or compiler flags. Technical facts must be verified using live terminal commands or documentation lookup.
5. **Root Cause Only & Anti-Workaround:**
   - Ban on temporary workarounds, path symlinks, or defensive `try/catch` wrappers that mask failures. Bugs must be resolved at the lowest architectural layer (`Kernel > Driver > OS Config > Runtime > Framework > Application Code`).
6. **Critical TypeScript Safety Gate:**
   - After modifying any `.ts`/`.tsx` file, agents must run `npx tsc --noEmit`. Deleting business logic to bypass type errors is strictly forbidden.
7. **Single Source of Truth (SSOT) & Anti-Duplication:**
   - Duplicate helpers, parallel endpoints, or competing schemas are forbidden. Existing implementations must be reused or refactored in-place.
8. **Anti-Destruction Protocol:**
   - Strict ban on `git clean`, blind mass search-and-replace, or destructive workspace operations without explicit user confirmation.

---

## 3. The 4-Phase Pre-Flight Skill Gate

To prevent context window bloat and eliminate architectural guessing, skills are activated through a gated hierarchy:

```
[Level 0: Metadata & Cartography] ──→ [Level 1: Planning & Spec] ──→ [Level 2: Domain Specialists]
                                                                                │
                                      [Level 3: QA & Verification Gate] ◀───────┘
```

```mermaid
graph TD
    A[User Request] --> B{Phase 0: Workspace Cartography}
    B -->|Unmapped Repo| B1[skill-codebase-onboarding / spec-miner / AGENTS.md]
    B --> C{Phase 1: Planning & Architecture}
    C -->|>15 min / >3 files / /plan| C1[spec-driven-development / monorepo / plugin]
    C --> D{Phase 2: Domain Specialists}
    D -->|Frontend| D1[skill-frontend-architect / design-engineering / creative-design]
    D -->|Backend/Systems| D2[skill-backend-architect / c-cpp-systems / wasm-emscripten]
    D -->|AI / Data| D3[skill-ai-ml / skill-data-science / skill-graph-analytics]
    D -->|Specialized| D4[skill-stealth-scraping / skill-system-diagnostics / research]
    D --> E{Phase 3: QA & Verification}
    E -->|On Code Execution| E1[skill-qa-engineer: TDD & TSC / skill-code-review: 5-Axis]
```

---

## 4. Project-Level Configuration Standard (`AGENTS.md`)

Global rules in `~/.agents/` define **agent behavior**, but individual repositories require **project-level context**.

This bundle provides the standardized [templates/AGENTS.md](file:///home/gzyms/agent_setup_bundle/templates/AGENTS.md) blueprint based on the Agentic AI Foundation (AAIF) specification.

### How to use `AGENTS.md` in your projects:
1. Copy the blueprint to your project root:
   ```bash
   cp ~/.agents/templates/AGENTS.md ~/Dev\ Projects/MyProject/AGENTS.md
   ```
2. Fill in the 4 core sections:
   - **Project Identity & Stack Architecture:** Language, runtime, framework versions, database ORM, styling system.
   - **Mandatory Commands (Executable Truth):** Exact commands with flags for `install`, `dev`, `build`, `test`, `tsc`, and `lint` (agents will NEVER guess CLI flags).
   - **Directory Topography & Module Boundaries:** Explicit directory layout and boundaries (e.g. `src/domain/`, `src/adapters/`, `src/components/`).
   - **Invariants & Guardrails (Never-Do Rules):** Strict project invariants (e.g. "Never import DB models in client components", "Files must remain under 150 lines").

When OpenAI Codex, Claude Code, Gemini CLI, or Cursor opens your project, it reads `AGENTS.md` as the primary Source of Truth.

---

## 5. 13 Operational Core Rules (`~/.agents/rules/`)

| Rule | File | Purpose & Key Mandate |
|---|---|---|
| **Skill Orchestration** | `skill-orchestration.md` | Mandates the 4-Phase Pre-Flight Skill Gate before file discovery or code modifications. |
| **Zero Speculation** | `zero-speculation.md` | Total ban on guessing versions, APIs, or system specs without live diagnostic verification. |
| **Modular Architecture** | `modular-architecture.md` | Anti-Monolith constraint (max ~150-200 lines), Clean/Hexagonal boundaries, typed contracts. |
| **Systemic Excellence** | `systemic-excellence.md` | Anti-workaround protocol, root-cause fixes, DRY, and Single Source of Truth (SSOT). |
| **System Identity** | `system-identity.md` | Hardware & OS baseline template with auto-discovery commands to prevent hallucinations. |
| **Command Verification** | `command-verification.md` | Mandatory secondary read-only check after any state-modifying command. |
| **Subagent Economy** | `subagent-economy.md` | Dynamic LLM model tiering based on task complexity (Light -> Standard -> Pro). |
| **Problem Isolation** | `problem-isolation.md` | Strict scope containment; zero unrequested refactors or global OS alterations. |
| **Environment Integrity** | `env-integrity.md` | Sanity checks on workspace, lockfiles, and dependencies before modifying files. |
| **Error Triage** | `error-triage.md` | Deterministic diagnostic priority order: Documentation -> Web Search -> Code Inspection. |
| **Full Log Reporting** | `full-log-reporting.md` | Ban on truncated, summarized, or paraphrased error reporting. |
| **MemPalace Discovery** | `mempalace-discovery.md` | Absolute priority of MemPalace memory retrieval before broad filesystem searches. |
| **MCP Master Playbook** | `mcp-master-playbook.md` | 11-server MCP execution matrix, permission boundaries, and synergy workflows. |

---

## 6. 33 Production-Grade Skills (`~/.agents/skills/`)

All skills adhere to the `agentskills.io` standard with YAML frontmatter, progressive disclosure, and anti-rationalization verification gates:

### Domain A: Cartography, Planning & Architecture (5 Skills)
- **`skill-codebase-onboarding`**: Systematic 5-phase repository cartography, entrypoint discovery, and command extraction.
- **`spec-miner`**: Reverse-engineering engine for extracting specifications and dataflows from legacy/undocumented code.
- **`spec-driven-development`**: Gated SDLC workflow (Specify -> Plan -> Tasks -> Implement) with verification matrices.
- **`skill-monorepo-architect`**: Polyglot monorepo management (`uv` Python workspaces, `pnpm` workspaces, Turborepo).
- **`skill-plugin-architecture`**: Microkernel architecture, dynamic plugin discovery, lifecycle hooks, and error boundaries.

### Domain B: Frontend & UI/UX Craftsmanship (5 Skills)
- **`skill-frontend-architect`**: Next.js 15+ App Router, React Server Components (RSC), Client Island boundaries, WCAG 2.2 AA.
- **`skill-design-engineering`**: Creative frontend engineering, Motion.dev spring animations, CSS Subgrid, Container Queries, 21st.dev UI components.
- **`skill-creative-design`**: Art direction, Swiss/Bauhaus aesthetics, Fontjoy typography math, and OKLCH color physics.
- **`skill-web-performance`**: Core Web Vitals optimization (LCP, INP, CLS), Lighthouse 100/100 audits, and runtime tracing.
- **`seo-optimization-and-audit`**: Search engine ranking optimization, structured metadata, semantic HTML, and head audits.

### Domain C: Backend & Low-Level Systems (7 Skills)
- **`skill-backend-architect`**: Contract-first API design, database schemas, migration isolation, and Postgres/SQLite verification.
- **`skill-web-architecture`**: Full-stack architectural standards, module boundaries, and end-to-end API contracts.
- **`c-cpp-systems`**: Memory safety, struct packing (`#pragma pack`), manual RAII, bitwise math, and sanitizers (`ASan`/`UBSan`).
- **`skill-low-level-programming`**: Low-level systems programming, Assembly, byte manipulation, memory layout, and endianness handling.
- **`wasm-emscripten`**: WebAssembly compilation via Emscripten, `ccall`/`cwrap` FFI bindings, virtual FS, and HEAP views.
- **`retro-emulation-engineering`**: Retro hardware simulation (CPU/RSP/RDP), frame timing, dynamic audio resampling, and ROM validation.
- **`skill-emulator-wasm`**: WebAssembly retro emulation engineering, Emscripten bridge lifecycle, WebGL rendering, and cartridge saves.

### Domain D: AI, Data Science & Intelligence (7 Skills)
- **`skill-ai-ml`**: LLM model integrations, embeddings, vector databases (Redis, ChromaDB), and agentic workflows.
- **`skill-data-science`**: Data ingestion pipelines, exploratory data analysis (EDA), dataframes (Polars/Pandas), and validation.
- **`skill-data-analysis`**: Statistical analysis, hypothesis testing, anomaly detection, and scientific claim verification.
- **`skill-graph-analytics`**: Graph databases (Neo4j), Cypher queries, topology analysis, and Graph Data Science (GDS).
- **`skill-stealth-scraping`**: Anti-bot evasion (Cloudflare/DataDome), TLS fingerprint spoofing, and browser automation.
- **`skill-osint-engineering`**: Open Source Intelligence gathering, Pydantic entity graphs, pivoting engines, and OPSEC.
- **`skill-research`**: Academic and technical literature research, arXiv paper analysis, and multi-source fact checking.

### Domain E: QA, Systems Diagnostics & Conversion (9 Skills)
- **`skill-qa-engineer`**: Test-Driven Development (TDD Red-Green), TypeScript compilation safety gates (`npx tsc --noEmit`).
- **`skill-code-review`**: Systematic 5-axis code review (Correctness, Readability, Architecture, Security, Performance).
- **`doubt-driven-development`**: Adversarial verification gate to challenge false confidence and prevent silent failures.
- **`skill-system-diagnostics`**: Hardware, OS, driver, kernel panic diagnostics, and log analysis.
- **`skill-devops-cloud`**: Docker containers, Docker MCP inspection, CI/CD pipelines, and cloud deployments.
- **`skill-resume-tailor`**: ATS-optimized resume, CV, and cover letter tailoring following the Google XYZ formula.
- **`marketing-copywriting`**: Conversion-focused technical copywriting and value proposition design.
- **`avoid-ai-writing`**: Detection and elimination of AI writing clichés, robotic cadence, and filler words.
- **`mempalace` / `mempalace-recall`**: Long-term memory palace management and historical knowledge retrieval.

---

## 7. Model Context Protocol (MCP) Master Playbook

The suite is pre-configured to utilize standard MCP servers with strict execution boundaries:

```
┌─────────────────────────┬────────────────────────────────────────────────────────────────────────┐
│ MCP Server              │ Role & Boundaries                                                      │
├─────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ github                  │ Remote PR/Issue API management (DO NOT use for local git checkout/push)│
│ chrome-devtools         │ Live browser automation, DOM inspection, network waterfall tracing     │
│ puppeteer               │ Headless scraping, PDF generation, screenshot capture                  │
│ lighthouse-mcp          │ Core Web Vitals, accessibility, SEO, and performance score audits      │
│ postgres / sqlite       │ Direct SQL schema and migration verification                           │
│ mempalace               │ Hierarchical memory storage, entity knowledge graphs, and diaries      │
└─────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

> **MCP Boundary Rule:** Always use the `github` MCP server for remote API actions (PR reviews, issue creation) and local `git` CLI for workspace version control (staging, committing, pushing).

---

## 8. Supported Environments & Platform Matrix

| Platform | Manifest / Rule Location | Config Location | Skill Discovery Path |
|---|---|---|---|
| **OpenAI Codex** | `~/.codex/instructions.md` / `CODEX.md` | `~/.codex/config.toml` | `~/.codex/skills/custom` -> `~/.agents/skills` |
| **Antigravity / Gemini CLI** | `~/.gemini/GEMINI.md` | `~/.gemini/settings.json` | `~/.agents/skills/` |
| **Claude Code** | `~/.claude/CLAUDE.md` + `.claude/agents/` | `~/.claude/mcp.json` | `~/.agents/skills/` |
| **Cursor IDE** | `~/.cursor/rules/*.mdc` | `~/.cursor/mcp.json` | On-demand referencing |

---

## 9. 1-Click Quickstart & Installation

Clone and run the unified installer in your environment:

```bash
git clone https://github.com/Gzyms69/agent-setup-bundle.git
cd agent-setup-bundle
./install.sh
```

### Installation Flags:
```bash
./install.sh --all       # Configure all platforms: Codex, Gemini, Claude, Cursor (default)
./install.sh --codex     # Configure OpenAI Codex only (~/.codex/)
./install.sh --gemini    # Configure Antigravity / Gemini CLI only (~/.gemini/)
./install.sh --claude    # Configure Claude Code only (~/.claude/)
./install.sh --cursor    # Configure Cursor IDE only (~/.cursor/)
```

---

## 10. Repository File Structure

```
agent_setup_bundle/
├── core/
│   ├── CODEX.md                     # OpenAI Codex Operating System manifest
│   ├── GEMINI.md                    # Antigravity / Gemini CLI Core Operating System
│   ├── CLAUDE.md                    # Claude Code Engineering Operating System
│   ├── claude/agents/               # Subagents: code-reviewer, researcher, system-architect
│   └── cursor/rules/                # Cursor IDE rules: core-directives, tsc, tdd, etc.
├── rules/                           # 13 Universal Rules (Zero Speculation, Anti-Workaround, etc.)
├── skills/                          # 33 Production Skills (agentskills.io standard)
├── templates/
│   └── AGENTS.md                    # Standardized per-project repository blueprint
├── config/
│   ├── codex_config.toml            # OpenAI Codex configuration & MCP template
│   ├── settings.json                # Gemini CLI / Antigravity settings & MCP template
│   ├── mcp_config.json              # Shared MCP configuration
│   └── cursor_mcp.json              # Cursor IDE MCP configuration
├── policies/
│   └── mcp-planning.toml            # MCP tool policy definitions
├── install.sh                       # Multi-platform 1-click installer
├── PROMPT_FOR_AI.md                 # Universal bootstrap prompt for web/chat interfaces
└── README.md                        # Master technical documentation
```

---

## 11. License

This project is licensed under the [MIT License](LICENSE).
