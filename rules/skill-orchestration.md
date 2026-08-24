# Rule: Mandatory Pre-Flight Skill Gate & Orchestration Protocol

This rule defines the **mandatory, 4-phase cognitive gate** that every AI agent must execute before performing any file discovery, code reading, or state-modifying actions.

---

## 1. The Pre-Flight Invariant (Zero Blind Exploration)

**ABSOLUTE MANDATE:**
Before invoking ANY code-exploring tool (`find_by_name`, `grep_search`, `list_dir`, `view_file` on project source code) or state-modifying command (`write_to_file`, `replace_file_content`, `run_command`), the agent MUST evaluate the user request against the **4-Phase Pre-Flight Skill Gate**.

The agent is **STRICTLY FORBIDDEN** from guessing architectural patterns or blindly grepping repositories without first loading the mandatory phase skills.

---

## 2. The 4-Phase Pre-Flight Skill Gate

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           4-PHASE PRE-FLIGHT SKILL GATE                          │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
    ┌────────────────────────────────────┼────────────────────────────────────┐
    ▼                                    ▼                                    ▼
┌─────────────────────────┐  ┌─────────────────────────┐  ┌─────────────────────────┐
│ Phase 0: Cartography    │  │ Phase 1: Planning/Spec  │  │ Phase 2: Domain Experts │
│ (Workspace Discovery)   │  │ (Architecture & Tasks)  │  │ (Tech Stack Specific)   │
└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘
                                                                      │
                                                                      ▼
                                                          ┌─────────────────────────┐
                                                          │ Phase 3: QA & Safety    │
                                                          │ (TDD, TSC, Verification)│
                                                          └─────────────────────────┘
```

### Phase 0: Workspace Cartography & MemPalace Gate (MANDATORY FIRST STEP)
* **Trigger Condition:** Interacting with, searching, reading, debugging, or adding features to ANY repository/workspace where architecture, stack, entrypoints, and commands have not been mapped in the current conversation.
* **Mandatory Action:**
  1. Query MemPalace first (`mempalace_search` / `mempalace_kg_query`) per `mempalace-discovery.md` to load existing project context, prior decisions, and architecture models.
  2. Call `view_file` on `skill-codebase-onboarding/SKILL.md` (or `spec-miner/SKILL.md` for legacy/undocumented systems).
  3. Execute Phase 1 (Metadata/Rules scan) and Phase 2 (Topography scan) of onboarding BEFORE reading individual source files.
* **Exemption:** The repository has already been systematically mapped earlier in the active conversation transcript.

### Phase 1: Planning, Context & Orchestration Gate
* **Trigger Condition:** Any task that:
  - Is estimated to take >15 minutes or modify >3 files,
  - Involves architectural refactoring, multi-agent swarms, or long conversational trajectories,
  - Is explicitly invoked with `/plan`.
* **Mandatory Action:**
  1. Call `view_file` on `spec-driven-development/SKILL.md` and adhere strictly to `rules/planning-and-document-integrity.md` (Planning Lifecycle State Machine, Iteration Delta, Discovered Facts Lock, Active SSOT).
  2. **Multi-Agent / Swarm:** If coordinating subagents, parallel research, or task DAGs: load `skill-master-orchestrator/SKILL.md`.
  3. **Context / High Token Load:** If managing long-running sessions, heavy logs, or memory compaction: load `skill-context-engineering/SKILL.md`.
  4. If monorepo or plugin system is detected: load `skill-monorepo-architect/SKILL.md` or `skill-plugin-architecture/SKILL.md`.
  5. Formulate an implementation specification artifact before modifying code.

### Phase 2: Domain Specialist Gate
* **Trigger Condition:** Specific technical domains or application layers are involved.
* **Resolution Matrix:**
  * **Frontend & UI:**
    - Next.js / App Router / React Server Components / State: `skill-frontend-architect`
    - Motion animations / Tailwind / Bento / UI Polish: `skill-design-engineering`
    - Aesthetics / Typography / OKLCH / Art Direction: `skill-creative-design`
  * **Backend & Systems:**
    - API design / DB Schema / Query Optimization / Migrations: `skill-backend-architect`
    - MCP Server Architecture / FastMCP / TypeScript SDK: `skill-mcp-builder`
    - Low-level C/C++ / Memory / Pointers / ASan: `c-cpp-systems` + `skill-low-level-programming`
    - WebAssembly / Emscripten runtime: `wasm-emscripten`
    - Retro emulation / Hardware coprocessors: `retro-emulation-engineering` + `skill-emulator-wasm`
  * **Data & AI:**
    - LLMs / Embeddings / Agents / Vector DBs: `skill-ai-ml`
    - Data pipelines / EDA / Datasets: `skill-data-science` + `skill-data-analysis`
    - Graph databases / Neo4j / Network topology: `skill-graph-analytics`
  * **Specialized Workflows:**
    - Scraping / Anti-bot / Fingerprints: `skill-stealth-scraping`
    - OSINT / Entity mapping: `skill-osint-engineering`
    - Resumes / CVs / ATS optimization: `skill-resume-tailor`
    - Copywriting / Marketing: `marketing-copywriting` + `avoid-ai-writing`
    - SEO / Core Web Vitals audits: `seo-optimization-and-audit` + `skill-web-performance`
    - Hardware / OS / Kernel / Driver diagnostics: `skill-system-diagnostics`
    - Research / Academic verification: `skill-research`

### Phase 3: QA & Verification Gate (MANDATORY ON CODE EXECUTION)
* **Trigger Condition:** Any code creation, modification, refactoring, or pre-commit finalization.
* **Mandatory Action:**
  1. Call `view_file` on `skill-qa-engineer/SKILL.md` to enforce TDD (Red-Green) and TypeScript compilation safety gates (`npx tsc --noEmit`).
  2. Execute 5-axis self-review (`skill-code-review/SKILL.md`) auditing Correctness, Readability, Architecture, Security (OWASP), and Performance.
  3. If high-stakes or irreversible changes: load `doubt-driven-development/SKILL.md`.

---

## 3. Pre-Flight Declaration Requirement

During the **Perceive & Reason** phase of every user request, the agent MUST explicitly declare the resolved skills before executing tool actions:

```
[Pre-Flight Skill Gate]
- Phase 0 (Cartography): skill-codebase-onboarding (Loaded)
- Phase 1 (Planning): spec-driven-development, skill-master-orchestrator (Loaded)
- Phase 2 (Domain): skill-backend-architect, skill-mcp-builder (Loaded)
- Phase 3 (QA): skill-qa-engineer, skill-code-review (Active gate)
```
