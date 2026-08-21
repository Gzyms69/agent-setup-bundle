---
name: skill-codebase-onboarding
description: MANDATORY FIRST STEP for ANY repository exploration, inspection, debugging, or feature work. Systematic repository exploration, architecture cartography, entrypoint discovery, and operational command extraction. MUST ACTIVATE before exploring, searching, reading, debugging, or adding features to ANY repository or codebase unless a complete REPO_MAP is already established in context. DO NOT skip to grep or file reading without this skill.
---

# Codebase Onboarding & Repository Cartography Skill

This skill defines the deterministic, 5-phase protocol for exploring, understanding, and mapping any unfamiliar codebase, tool, or library without flooding the context window or guessing architectural patterns.

---

## 1. Core Philosophy: Progressive Disclosure

Never read entire repositories blindly. Treat the context window as a finite token budget. Gather information systematically from highest abstraction to lowest implementation:

```
[Level 0: Metadata & Rules] ──→ [Level 1: Tree Topography] ──→ [Level 2: Entrypoints & Flow]
                                                                        │
[Level 4: Map & Memory]    ◀── [Level 3: Operational Harness] ◀─────────┘
```

---

## 2. The 5-Phase Onboarding Protocol

### Phase 1: Project Identity & Machine Rules (Metadata Scan)
Before reading source code, identify what the project is and what machine-readable rules already exist.

1. **Check for AI/Agent Instruction Files (First Priority):**
   * `AGENTS.md` (universal Agentic AI Foundation standard)
   * `CLAUDE.md` / `.claude/CLAUDE.md`
   * `.cursor/rules/*.mdc` or `.cursorrules`
   * `.github/copilot-instructions.md`
   * `llms.txt` / `llms-full.txt`
   * `.gemini/rules` or `GEMINI.md`

2. **Inspect Package & Build Manifests (Stack Detection):**
   * **Node/TypeScript:** `package.json`, `pnpm-workspace.yaml`, `tsconfig.json`
   * **Python:** `pyproject.toml`, `requirements.txt`, `Pipfile`, `setup.py`
   * **Rust:** `Cargo.toml`, `Cargo.lock`
   * **Go:** `go.mod`
   * **Java/Kotlin:** `pom.xml`, `build.gradle`, `settings.gradle`
   * **C/C++:** `CMakeLists.txt`, `Makefile`, `meson.build`
   * **PHP/Ruby/Elixir:** `composer.json`, `Gemfile`, `mix.exs`

3. **Read High-Level Human Documentation:**
   * `README.md` (focus on architecture/setup sections, skip marketing fluff)
   * `docs/architecture/` or `ADR/` (Architecture Decision Records) if present.

---

### Phase 2: Topography & Architectural Mapping
Map the repository structure to understand module boundaries and architectural style.

1. **Scan Directory Structure (Depth 1-2):**
   * Use `list_dir` on root and top-level folders.
   * Do NOT run recursive directory listings on un-ignored `node_modules`, `venv`, `target`, `dist`, or `build` dirs.

2. **Identify the Architecture Pattern:**
   * **Monorepo:** Look for `apps/`, `packages/`, `services/`, `libs/` (Turborepo, Nx, Lerna, PNPM Workspaces).
   * **Clean / Hexagonal Architecture:** Look for `domain/`, `application/`, `infrastructure/`, `adapters/`, `ports/`.
   * **Layered MVC:** Look for `controllers/`, `services/`, `models/`, `views/`, `routes/`.
   * **Modular / Feature-Based:** Look for `features/`, `modules/`, `components/`.
   * **Event-Driven / Serverless:** Look for `handlers/`, `functions/`, `events/`, `workers/`.

3. **Record Boundaries:**
   * Identify which modules are isolated and which share common utilities (`common/`, `shared/`, `core/`).

---

### Phase 3: Entrypoints, Schemas & "Request Lifecycle"
Locate how execution begins and how data flows through the application.

1. **Locate Runtime Entrypoints:**
   * Backend: `src/index.ts`, `server.ts`, `main.py`, `app.py`, `cmd/main.go`, `src/main.rs`.
   * Frontend: `src/App.tsx`, `pages/_app.tsx`, `app/layout.tsx`, `src/main.js`.
   * CLI tools: `bin/`, `cli.ts`, `cmd/`, `__main__.py`.

2. **Map Data Contracts & Schemas:**
   * Database / ORM: `prisma/schema.prisma`, `schema.sql`, `migrations/`, `drizzle.config.ts`, `models/`.
   * API Definitions: `routes/`, `api/`, `openapi.yaml`, `swagger.json`, `schema.graphql`, `trpc/`.
   * Environment / Configuration: `.env.example`, `config/`, `src/env.ts`, `settings.py`.

3. **Trace "One Lifecycle Path":**
   * Trace one representative flow from entry point to persistent layer:
     `Incoming Request / Event ──→ Router/Handler ──→ Business Service ──→ DB Query / Outbound API`

---

### Phase 4: Operational Quality Harness (Executable Truth)
Extract exact, runnable commands rather than guessing tool syntax.

1. **Document Mandatory Commands:**
   * **Install:** `pnpm install` | `npm ci` | `uv sync` | `cargo build` | `go mod download`
   * **Dev Server:** `npm run dev` | `uvicorn app.main:app --reload` | `cargo run`
   * **Build:** `npm run build` | `cargo build --release` | `go build ./...`
   * **Test:** `npm test` | `pytest -v` | `cargo test` | `go test ./...`
   * **Typecheck & Lint:** `npx tsc --noEmit` | `npm run lint` | `ruff check .` | `golangci-lint run`

2. **Inspect CI/CD & Infrastructure Files:**
   * `.github/workflows/*.yml`, `.gitlab-ci.yml` (these contain the definitive ground truth for builds and tests).
   * `Dockerfile`, `docker-compose.yml` (service dependencies like Redis, Postgres, Kafka).

---

### Phase 5: Synthesis, REPO_MAP & Memory Persistence
Consolidate findings so that future interactions do not need to re-read the repository from scratch.

1. **Generate or Update `REPO_MAP.md`:**
   * Create or update a concise `REPO_MAP.md` in the project root or memory directory using the template in `resources/repo-map-template.md`.

2. **MemPalace Long-Term Memory Filing:**
   * When MemPalace is active, write the extracted facts:
     * `mempalace_add_drawer`: Subject `Project: <Name>`, Title `Codebase Architecture & Commands`, content formatted in AAAK.
     * `mempalace_kg_add`: Relate project name to primary stack, key directories, and test framework.

---

## 3. Strict Context Conservation Directives

* **NO FULL FILE DUMPS:** Never call `view_file` on large files (>150 lines) without `StartLine` and `EndLine` slicing.
* **PRECISION GREP FIRST:** Use `grep_search` with specific identifiers (`export function`, `class `, `router.`, `struct `) rather than reading whole directories.
* **EXCLUDE NOISE:** Always ignore lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `Cargo.lock`), minified bundles, sourcemaps, and build outputs (`dist/`, `build/`, `.next/`).

---

## 4. Best Practices Reference for AI Project Standards

### Writing `AGENTS.md` (For Projects)
When creating or recommending an `AGENTS.md` for a project, structure it as follows:
* **Tech Stack:** Exact runtime and framework versions.
* **Key Commands:** Full copy-pasteable build, test, lint, and run commands.
* **Architectural Invariants:** Strict rules (e.g., "Never import DB models directly inside React components").
* **Definition of Done:** Required gates before committing code (e.g., `tsc` pass, tests pass, no lint warnings).

### Writing `llms.txt` (For Web Services & Docs)
* Place at `/llms.txt`.
* Use single H1 for project name.
* Blockquote summary.
* Group curated Markdown doc links under H2 sections with short semantic descriptions.
