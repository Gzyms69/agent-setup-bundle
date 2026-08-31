# Multi-Platform Agentic AI Engineering Operating System & Sub-Worker Delegation Engine

[![Architecture: Two-Tier Multi-Agent](https://img.shields.io/badge/Architecture-Two--Tier_Cognitive_System-blue.svg)](https://github.com/Gzyms69/agent-setup-bundle)
[![Standard: agentskills.io](https://img.shields.io/badge/Standard-agentskills.io-green.svg)](https://agentskills.io)
[![MCP: FastMCP v1.0](https://img.shields.io/badge/MCP-FastMCP_v1.0-orange.svg)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)
[![Platforms: Linux | macOS | Windows](https://img.shields.io/badge/Platforms-Linux_%7C_macOS_%7C_Windows-lightgrey.svg)](https://github.com/Gzyms69/agent-setup-bundle)

A deterministic, cross-platform engineering suite and operating framework for leading AI coding assistants (**OpenAI Codex**, **Antigravity / Gemini CLI**, **Claude Code**, and **Modern Cursor IDE (.mdc)**) across **Linux**, **macOS**, and **Windows**.

The bundle unifies **16 ironclad operational rules (Prime Directives)**, **36 modular skills (`agentskills.io` standard)**, and an autonomous **Two-Tier Cognitive Architecture** powered by a custom **FastMCP Sub-Worker Delegation Bridge (`chinese-worker`)** and **Aider Headless Engine**. Expensive frontier models (Gemini 3.7 Pro, Claude 3.7 Sonnet) act as high-level architects and orchestrators, delegating repetitive bulk coding tasks (scaffolding 2500+ LOC, TDD unit test generation, JSDoc/docstrings, strict type migrations) to **100% free, mega-context models** (MiniMax M3 1M Context, NVIDIA Nemotron 550B MoE, Zhipu GLM-5.2) in sandboxed Git Worktrees with **Zero Context Bleed** and **Zero Token Cost ($0.00)**.

---

## ⚡ 1-Prompt Autonomous AI Installation

If you are using an AI coding assistant (Claude Code, OpenAI Codex, Cursor Composer, Gemini CLI / Antigravity, Cline, Roo Code, OpenCode, Aider), simply paste this prompt:

### English:
```text
Clone https://github.com/Gzyms69/agent-setup-bundle.git and install the full AI engineering operating system for me following AGENTS.md in the repo.
```

### Polski:
```text
Sklonuj https://github.com/Gzyms69/agent-setup-bundle.git i zainstaluj całe środowisko inżynieryjne według instrukcji w AGENTS.md.
```

Your AI assistant will read [AGENTS.md](AGENTS.md), auto-detect your operating system (Windows, macOS, or Linux), execute the native installer, validate suite integrity, and immediately adopt the **Senior AI Pair Programmer** persona.

---

## 1. Executive Summary & Two-Tier Cognitive Architecture

Traditional single-model AI pair programming ("Just write this feature") fails on complex production codebases due to four fundamental problems:
1. **Economic Inefficiency:** Burning expensive reasoning tokens on repetitive boilerplate, large mock suites, or syntax formatting.
2. **Context Window Degradation:** Dumping thousands of lines of raw logs and intermediate diffs into the primary reasoning context.
3. **Simulation & Mocking Traps:** Writing fake stubs or untested boilerplate without running verification suites.
4. **Monolithic Spaghetti Code:** Coupling business logic to UI frameworks and creating unmaintainable "god files".

`agent-setup-bundle` solves this through a **Two-Tier Cognitive Architecture**:

```mermaid
flowchart TD
    subgraph Tier1_Brain ["Tier 1: High-Reasoning Brain & Orchestrator ($$)"]
        Gemini["Gemini 3.7 Pro / Antigravity CLI"]
        Claude["Claude 3.7 Sonnet / Claude Code"]
        Cursor["Cursor IDE / Composer"]
        Codex["OpenAI Codex CLI"]
        SpecGate["Spec-Driven Development & 5-Axis Code Review Gate"]
        Gemini & Claude & Cursor & Codex --> SpecGate
    end

    subgraph Tier2_FastMCP ["Tier 2: FastMCP Sub-Worker Bridge (chinese-worker) ($0.00)"]
        Router["Intelligent Task Router (Keyword & Task Affinity)"]
        SkillsInj["Dynamic Skill Injector (--read ~/.agents/skills/*/SKILL.md)"]
        WorktreeMgr["Git Worktree Sandbox (.git/worktrees_active/<task-id>)"]
        AiderEngine["Aider Headless Engine (Diff Mode)"]
        SelfHealing["Self-Healing Quality Loop (--auto-test)"]
        
        SpecGate -->|MCP Tool: worker_run_task / worker_generate_tests| Router
        Router --> WorktreeMgr --> AiderEngine
        Router --> SkillsInj --> AiderEngine
        AiderEngine --> SelfHealing
    end

    subgraph Model_Pool ["Free Tier & High-Throughput Model Pool"]
        M3["MiniMax M3 (1M Ctx, 65k Out) -> Mega Scaffolding & Fullstack"]
        N550["NVIDIA Nemotron 550B MoE -> Low-Level, C++, ASM & Math"]
        GLM5["Zhipu GLM-5.2 (LiveCodeBench 74-85%) -> Bugfix & Refactor"]
        NLight["Nemotron 3.5 Lightning -> Rapid TDD Unit Tests"]
        GLM4["Zhipu GLM-4-Flash PAAS -> 100% Guaranteed Direct Fallback"]
        
        Router --> Model_Pool
        Model_Pool --> AiderEngine
    end

    SelfHealing -->|Zero Context Bleed: 3-line Structured Report| SpecGate
    SpecGate -->|Inspection & Approval| Merge["worker_merge_branch"]
```

1. **Tier 1 (Brain & Orchestrator):** Frontier models (Gemini 3.7, Claude 3.7) plan architecture, conduct Spec-Driven Development, and enforce the 5-Axis Code Review Gate.
2. **Tier 2 (Grunt Worker & Token Factory):** FastMCP (`chinese-worker`) delegates bulk implementation tasks to free, specialized models operating inside sandboxed Git Worktrees with an automated **Self-Healing Quality Loop** (`--auto-test`).

---

## 2. Universal 4-Phase Pre-Flight Skill Gate

Before executing file discovery (`grep_search`, `find_by_name`, `view_file`) or making any code changes, agents operating under this system MUST evaluate and activate skills through the **4-Phase Pre-Flight Skill Gate**:

```mermaid
flowchart LR
    P0["Phase 0: Cartography Gate"] --> P1["Phase 1: Planning & Orchestration"]
    P1 --> P2["Phase 2: Domain Specialists"]
    P2 --> P3["Phase 3: QA & Review Gate"]
```

### Complete 36-Skill Matrix (`~/.agents/skills/`):

| Phase | Skill Name | Trigger & Responsibility |
|---|---|---|
| **Phase 0** | `skill-codebase-onboarding` | Mandatory first step for exploring or onboarding any unmapped repository. |
| **Phase 0** | `spec-miner` | Reverse-engineering legacy, undocumented, or poorly structured codebases. |
| **Phase 1** | `spec-driven-development` | Tasks >15 min, >3 files, architectural decisions, or `/plan` invocation. |
| **Phase 1** | `skill-context-engineering` | Attention budget curation, log offloading to `./scratch/`, context compaction. |
| **Phase 1** | `skill-master-orchestrator` | Multi-agent swarm coordination, Task DAG decomposition, barrier synchronization. |
| **Phase 1** | `skill-monorepo-architect` | Monorepo structure management (PNPM, Turborepo, UV workspaces). |
| **Phase 1** | `skill-plugin-architecture` | Extensible microkernel systems, dynamic toolkits, plugin discovery. |
| **Phase 1** | `skill-web-architecture` | Full-stack web architectural standards, module boundaries, API contracts. |
| **Phase 2** | `skill-frontend-architect` | Next.js 15+ App Router, RSC, Client Island boundaries, WCAG 2.1/2.2 AA. |
| **Phase 2** | `skill-design-engineering` | Motion animations (`motion.dev`), CSS Subgrid, Container Queries, 21st.dev UI. |
| **Phase 2** | `skill-creative-design` | Art direction, aesthetics, Fontjoy typography math, OKLCH color physics. |
| **Phase 2** | `skill-backend-architect` | Backend architecture, database schemas, API contracts, zero-downtime migrations. |
| **Phase 2** | `skill-mcp-builder` | Model Context Protocol server development (FastMCP, TypeScript SDK, stdio/SSE). |
| **Phase 2** | `skill-low-level-programming` | C/C++, Rust, Assembly, byte manipulation, memory layout, bitwise arithmetic. |
| **Phase 2** | `c-cpp-systems` | Low-level C/C++ memory safety, pointers, manual RAII, ASan/UBSan sanitizers. |
| **Phase 2** | `wasm-emscripten` | C/C++ to WebAssembly compilation, Emscripten runtime bridging, HEAP views. |
| **Phase 2** | `retro-emulation-engineering`| Retro emulator architecture, hardware coprocessor simulation (CPU/RSP/RDP). |
| **Phase 2** | `skill-emulator-wasm` | WebAssembly retro emulators, WebGL rendering, Web Audio sync, save states. |
| **Phase 2** | `skill-ai-ml` | LLM integrations (Gemini, OpenAI, Anthropic), RAG pipelines, vector DBs. |
| **Phase 2** | `skill-data-science` | Data science workflows, exploratory data analysis (EDA), ingestion pipelines. |
| **Phase 2** | `skill-data-analysis` | Statistical methodology, hypothesis testing, anomaly detection, claim validation. |
| **Phase 2** | `skill-graph-analytics` | Graph databases (Neo4j), Cypher queries, topology analysis, Graph Data Science. |
| **Phase 2** | `skill-graphics-webgl` | 2D/3D graphics, Three.js, WebGL shader optimization, Canvas rendering. |
| **Phase 2** | `skill-stealth-scraping` | Anti-bot evasion, stealth automation, TLS/JA3 fingerprints, reverse API engineering. |
| **Phase 2** | `skill-osint-engineering` | OSINT intelligence pipelines, standardized entity graphs, pivoting engines. |
| **Phase 2** | `skill-system-diagnostics` | Hardware/OS/kernel diagnostics, log analysis, SRE root-cause debugging. |
| **Phase 2** | `skill-devops-cloud` | Docker containerization, CI/CD pipelines, Cloud Run checklists, Kubernetes. |
| **Phase 2** | `skill-research` | Academic and technical literature research with multi-source verification. |
| **Phase 2** | `skill-resume-tailor` | AI developer resume/CV architect (Google XYZ formula, Harvard Tech standard). |
| **Phase 2** | `marketing-copywriting` | Conversion-focused copywriting, value propositions, CTA engineering. |
| **Phase 2** | `avoid-ai-writing` | Strict audit and rewriting protocol eliminating AI writing clichés and fluff. |
| **Phase 2** | `seo-optimization-and-audit` | SEO audit, metadata, head tags, Core Web Vitals optimization. |
| **Phase 2** | `skill-web-performance` | Universal web performance engineering, Lighthouse 100/100, runtime tracing. |
| **Phase 3** | `skill-qa-engineer` | Mandatory Phase 3 QA Gate, TDD Red-Green discipline, TypeScript Safety Gate. |
| **Phase 3** | `skill-code-review` | Mandatory 5-axis review (Correctness, Readability, Architecture, Security, Perf). |
| **Phase 3** | `doubt-driven-development` | Adversarial verification gate challenging false confidence before assertions. |

---

## 3. 16 Operational Rules (The Laws of Robotics)

All operational rules reside in `~/.agents/rules/` and are enforced across all platform manifests:

1. `zero-speculation.md`: Total ban on guessing hardware specs, package versions, API endpoints, or error causes. Verify via live commands or web search.
2. `command-verification.md`: Mandatory verification of CLI tool outcomes before proceeding.
3. `env-integrity.md`: Pre-flight environment audit before modifying codebase configuration.
4. `error-triage.md`: Strict diagnostic triage sequence: Docs -> Web -> Source Code.
5. `full-log-reporting.md`: Zero truncated logs when diagnosing failures.
6. `problem-isolation.md`: Surgical problem isolation without collateral workspace mutation.
7. `subagent-economy.md`: Subagent model routing economy (`flash_lite` -> `flash` -> `pro`) and Chinese worker delegation.
8. `system-identity.md`: Real-time hardware identity and OS verification template.
9. `systemic-excellence.md`: Prohibition of symptomatic patches, workarounds, or defensive masking.
10. `context-engineering.md`: Strict 100-line / 5 KB offloading to `./scratch/` and Attention U-Curve protection.
11. `modular-architecture.md`: Clean/Hexagonal architecture boundaries and anti-god-file constraints.
12. `planning-and-document-integrity.md`: Stateful 3-state planning machine, `Iteration Delta`, and Discovered Facts Lock.
13. `session-handoff.md`: Lossless session transition via `NEXT_SESSION_PLAN.md` and clean SSOT handoff prompts.
14. `skill-orchestration.md`: Universal 4-Phase Pre-Flight Skill Gate activation protocol.
15. `mcp-master-playbook.md`: Standardized Model Context Protocol tool invocation guidelines.
16. `mempalace-discovery.md`: Knowledge graph querying and memory retrieval protocol.

---

## 4. Autonomous FastMCP Sub-Worker Bridge (`chinese-worker`)

The bundle includes a native, high-throughput Model Context Protocol server implemented in Python using **FastMCP** (`scripts/worker_mcp.py`).

### Native FastMCP Tools:

| Tool Name | Parameters | Description |
|---|---|---|
| `worker_run_task` | `instruction`, `editable_files`, `readonly_files`, `skills`, `task_type`, `profile`, `auto_test`, `test_cmd`, `use_worktree` | Executes an autonomous coding task in a dedicated Git Worktree with dynamic skill injection and self-healing test loop. |
| `worker_generate_tests` | `target_file`, `test_file`, `test_framework`, `skills`, `profile` | Generates comprehensive TDD unit tests (pytest, vitest, jest, cargo) with edge case mocking. |
| `worker_generate_docs` | `target_files`, `doc_type`, `profile` | Generates JSDoc, docstrings, or markdown guides preserving exact code functionality. |
| `worker_batch_refactor` | `target_files`, `instruction`, `readonly_files`, `skills`, `profile` | Executes mass refactoring or strict type safety upgrades across multiple files. |
| `worker_continue_task` | `task_id`, `feedback` | Continues refining changes within an existing active worktree sandbox. |
| `worker_get_diff` | `task_id` | Returns the clean unified `git diff` generated by the worker for inspection. |
| `worker_merge_branch` | `task_id`, `target_branch` | Merges the verified task worktree into the main working tree and cleans up. |
| `worker_discard_branch` | `task_id` | Deletes and cleans up a rejected task worktree sandbox. |
| `worker_status` | *(none)* | Lists all active worker worktrees and recent task logs. |

### Intelligent Model Affinity & Task Routing:

```json
{
  "task_affinity": {
    "scaffold": "minimax-m3",
    "fullstack": "minimax-m3",
    "low_level": "nemotron-550b",
    "binary": "nemotron-550b",
    "algorithms": "nemotron-550b",
    "bugfix": "glm-5.2",
    "refactor": "glm-5.2",
    "tests": "nemotron-lightning",
    "unit_tests": "nemotron-lightning",
    "docs": "glm-5.2",
    "fast": "cohere-code"
  }
}
```

1. **MiniMax M3 Free** (`openrouter/minimax/minimax-m3:free`): Tier 0 Chinese Flagship with **1,048,576 Context** and **65,536 Max Output Tokens**. Best for fullstack scaffolding and large multi-file codebases.
2. **NVIDIA Nemotron 3 Ultra 550B MoE** (`openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`): 550 Billion parameter MoE with 1M context. Specialized in low-level systems (C/C++, Rust, Assembly, byte manipulation, and mathematical algorithms).
3. **Zhipu GLM-5.2 Free** (`openrouter/z-ai/glm-5.2:free`): Frontier coding model with LiveCodeBench 74-85% and SWE-bench 68.2%. Specialized in bugfixes, refactoring, and diff generation.
4. **NVIDIA Nemotron 3.5 Lightning** (`openrouter/nvidia/nemotron-3.5-lightning:free`): Ultra-fast MoE for rapid TDD unit test creation.
5. **Zhipu GLM-4-Flash PAAS** (`openai/glm-4-flash`): Direct BigModel PAAS integration serving as 100% guaranteed fallback if OpenRouter free endpoints hit temporary rate limits.

### Developer CLI Companion (`worker`):

The installer provisions a terminal CLI symlink at `~/.local/bin/worker`:
```bash
# Diagnostic health check (validates packages, profiles, API keys)
worker check

# Interactive coding session with MiniMax M3
worker chat minimax-m3 --skills skill-frontend-architect src/App.tsx

# Batch instruction execution with automatic model routing
worker run "Refactor database queries to use parameterized prepared statements" --skills skill-backend-architect -f src/db.ts
```

---

## 5. Model Context Protocol (MCP) Multi-Server Matrix

The bundle provisions unified MCP server configurations across Gemini CLI (`config/mcp_config.json`), Cursor (`config/cursor_mcp.json`), and Claude Code:

| MCP Server | Provider / Package | Purpose |
|---|---|---|
| `chinese-worker` | `scripts/worker_mcp.py` (FastMCP) | High-throughput autonomous sub-worker delegation engine ($0.00). |
| `github` | `@modelcontextprotocol/server-github` | Remote GitHub API operations (PRs, issues, code search, reviews). |
| `chrome-devtools` | `chrome-devtools-mcp@latest` | Headless Chrome browser automation and DOM inspection. |
| `puppeteer` | `@modelcontextprotocol/server-puppeteer` | End-to-end web testing and screenshot capture. |
| `lighthouse-mcp` | `@danielsogl/lighthouse-mcp` | Web performance, Core Web Vitals, and accessibility audits. |
| `postgres` | `@modelcontextprotocol/server-postgres` | PostgreSQL schema introspection and query analysis. |
| `sqlite` | `@modelcontextprotocol/server-sqlite` | Local SQLite database inspection. |
| `docker` | `@modelcontextprotocol/server-docker` | Container lifecycle management and log inspection. |
| `firecrawl` | `firecrawl-mcp` | Web scraping, crawling, and clean Markdown extraction. |
| `ast-grep` | `@ast-grep/mcp` | Structural AST search and code pattern matching. |
| `mempalace` | `mempalace` | Long-term memory palace, AAAK knowledge graph and diary storage. |

---

## 6. Multi-Platform Installation Guide

### Option 1: Native Shell Installers

#### Linux & macOS (Bash):
```bash
git clone https://github.com/Gzyms69/agent-setup-bundle.git
cd agent-setup-bundle
chmod +x install.sh
./install.sh --all
```

#### Windows (PowerShell 5.1 / 7+):
```powershell
git clone https://github.com/Gzyms69/agent-setup-bundle.git
cd agent-setup-bundle
powershell -ExecutionPolicy Bypass -File .\install.ps1 -All
```

#### Universal Python 3 Installer (All OSes):
```bash
python3 install.py --all
```

### Option 2: Selective Installation Flags
- `--codex` / `-Codex`: Install only OpenAI Codex environment (`~/.codex/`).
- `--gemini` / `-Gemini`: Install only Antigravity / Gemini CLI environment (`~/.gemini/`).
- `--claude` / `-Claude`: Install only Claude Code environment (`~/.claude/`).
- `--cursor` / `-Cursor`: Install only Cursor IDE rules (`~/.cursor/rules/`).

---

## 7. Quality Assurance & Automated Testing

Every component in this repository is strictly validated by automated test suites before deployment:

```bash
# 1. Run the master suite integrity validator (16 rules, 36 skills, 4 platforms, worker configs)
python3 scripts/validate_suite.py

# 2. Run the Worker MCP & CLI unit test suite
python3 scripts/tests/test_worker.py

# 3. Run the Sub-Worker environment diagnostics
python3 scripts/worker_cli.py check
```

---

## 8. Directory Topography

```
agent-setup-bundle/
├── AGENTS.md                        # Master repository blueprint & AI installer instructions
├── README.md                        # Master technical documentation & cross-platform guide
├── CAREER_KNOWLEDGE_BANK.md         # Master SSOT for career portfolios, metrics & STAR+R cases
├── PROMPT_FOR_AI.md                 # Universal bootstrap prompts
├── llms.txt                         # Semantic summary for web-enabled LLM agents
├── install.sh                       # Native Bash installer (Linux / macOS)
├── install.ps1                      # Native PowerShell installer (Windows)
├── install.py                       # Universal Python 3 installer (All OSes)
├── core/                            # Platform manifests (CODEX.md, GEMINI.md, CLAUDE.md, cursor)
├── rules/                           # 16 Universal Operational Rules (~/.agents/rules/)
├── skills/                          # 36 Modular Skills (~/.agents/skills/)
├── templates/
│   ├── AGENTS.md                    # Project-level starter template
│   ├── CONVENTIONS.md               # Universal coding conventions for sub-workers
│   └── .aider.conf.yml.template     # Universal Aider configuration template
├── config/
│   ├── worker_profiles.json         # Sub-worker model routing profiles & context bounds
│   ├── .aider.model.settings.yml    # Aider model behavioral settings & diff formats
│   ├── .aider.model.metadata.json   # Aider token limit overrides (1M context / 65k output)
│   ├── mcp_config.json              # Gemini CLI MCP configuration template
│   ├── settings.json                # Gemini CLI general settings
│   ├── codex_config.toml            # OpenAI Codex configuration template
│   └── cursor_mcp.json              # Cursor IDE MCP configuration template
├── policies/                        # MCP tool planning policies
└── scripts/
    ├── worker_mcp.py                # FastMCP server for autonomous sub-worker delegation
    ├── worker_cli.py                # Developer CLI companion (worker)
    ├── tests/
    │   └── test_worker.py           # Unit test suite for worker ecosystem
    └── validate_suite.py            # Quality assurance test suite
```

---

## 9. License

MIT License. Designed and maintained by **Gzymson** for autonomous, deterministic AI pair programming.
