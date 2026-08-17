---
name: skill-monorepo-architect
description: Expert polyglot and domain-driven monorepo architecture guidance (Python UV workspaces, PNPM workspaces, Turborepo). Use when initializing, structuring, refactoring, or managing monorepos, shared core libraries, dependency graphs, or cross-package build pipelines.
---

# Monorepo Architect Skill

This skill defines deterministic standards and architectural blueprints for building scalable, high-performance, polyglot monorepos without dependency chaos, premature microservices overhead, or circular imports.

---

## 1. Core Philosophy: The Shared-Core-First Pattern

Every large system or toolkit MUST be designed around a **standalone core domain library** before introducing network layers (APIs) or user interfaces (Web/Desktop):

```
                        ┌─────────────────────────────────────────┐
                        │      packages/core (Pure Domain)        │
                        │  - Domain Models (Pydantic / Zod)       │
                        │  - Orchestrator Engine                  │
                        │  - Storage Interfaces & Business Logic  │
                        └────────────────────┬────────────────────┘
                                             │ (Direct Import / Zero Network Hop)
             ┌───────────────────────────────┼───────────────────────────────┐
             ▼                               ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│        apps/cli         │     │     packages/plugins    │     │        apps/api         │
│  - Instant Terminal UX  │     │  - Extensible Toolkits  │     │  - REST / WebSockets    │
│  - No Docker Required   │     │  - Implements BasePlugin│     │  - Exposes Core over Net│
└─────────────────────────┘     └─────────────────────────┘     └────────────┬────────────┘
                                                                             │ (HTTP/WS)
                                                                             ▼
                                                                ┌─────────────────────────┐
                                                                │        apps/web         │
                                                                │  - Nuxt / Next.js UI    │
                                                                └─────────────────────────┘
```

### Invariants:
1. **CLI Never Requires Running Containers:** The CLI directly imports `packages/core` and runs locally. It stores state in SQLite or JSON files.
2. **API is a Thin Adapter:** `apps/api` simply wraps `packages/core` in HTTP/WebSocket handlers. It introduces NO business logic that cannot be called from the CLI.
3. **No Circular Package Dependencies:** Dependencies flow strictly downward: `apps/` -> `packages/plugins` -> `packages/core`.

---

## 2. Polyglot Workspace Layout

A standard polyglot monorepo (Python + TypeScript) follows this root structure:

```
my-monorepo/
├── pyproject.toml              # UV Workspace Root configuration
├── uv.lock                     # Universal Python lockfile
├── pnpm-workspace.yaml         # PNPM Workspace configuration (if TS present)
├── package.json                # Root JS/TS scripts
├── turbo.json                  # Turborepo task pipeline (build, test, lint)
├── Makefile / task.sh          # Global developer ergonomics
│
├── packages/
│   ├── core/                   # Shared domain engine (Python package)
│   │   ├── pyproject.toml
│   │   └── src/core/
│   ├── plugins/                # Modular extensions & tool runners
│   │   ├── pyproject.toml
│   │   └── src/plugins/
│   └── ui/                     # Shared web components (if TS present)
│       ├── package.json
│       └── src/
│
└── apps/
    ├── cli/                    # CLI executable app (Typer/Click)
    │   ├── pyproject.toml
    │   └── src/cli/
    ├── api/                    # Server backend (FastAPI/Express)
    │   ├── pyproject.toml
    │   └── src/api/
    └── web/                    # Frontend client (Nuxt/Next/Vite)
        ├── package.json
        └── src/
```

---

## 3. Python Workspaces via `uv`

Use modern `uv` workspace declarations in root `pyproject.toml`:

```toml
[tool.uv.workspace]
members = ["packages/*", "apps/cli", "apps/api"]

[tool.uv.sources]
core = { workspace = true }
plugins = { workspace = true }

[project]
name = "monorepo-root"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = []
```

### Package Inter-Dependency Example (`apps/cli/pyproject.toml`):
```toml
[project]
name = "cli"
version = "0.1.0"
dependencies = [
    "core",
    "plugins",
    "typer>=0.9.0",
    "rich>=13.0.0",
]
```

---

## 4. TypeScript Workspaces via `pnpm` + `turborepo`

### `pnpm-workspace.yaml`:
```yaml
packages:
  - 'packages/*'
  - 'apps/web'
```

### `turbo.json`:
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", ".output/**"]
    },
    "test": {
      "dependsOn": ["^build"]
    },
    "lint": {}
  }
}
```

---

## 5. Greenfield Step-by-Step Monorepo Construction

When creating a new monorepo from scratch, follow this exact sequence:

1. **Step 1: Workspace Skeleton & Manifests**
   - Create root configuration files (`pyproject.toml`, `pnpm-workspace.yaml`).
   - Define exact Python and Node version gates.
2. **Step 2: Core Domain Modeling (`packages/core`)**
   - Write immutable schemas (Pydantic models) and domain exceptions.
   - Write unit tests for core logic (TDD).
3. **Step 3: Standalone CLI (`apps/cli`)**
   - Implement CLI commands importing `core`.
   - Verify terminal execution end-to-end without Docker.
4. **Step 4: Plugins & Tool Runners (`packages/plugins`)**
   - Implement standard `BasePlugin` interfaces.
5. **Step 5: API Layer (`apps/api`)**
   - Expose core operations over REST / SSE / WebSockets.
6. **Step 6: Web Dashboard (`apps/web`)**
   - Connect frontend to API.

---

## 6. Monorepo Quality Gates

Before approving or committing monorepo changes:
- [ ] Root dependencies run synchronously across all workspaces (`uv sync` / `pnpm install`).
- [ ] No package imports code from sibling packages without a formal workspace dependency declared.
- [ ] CLI runs standalone without external daemon requirements.
- [ ] All unit and integration test suites pass (`pytest`, `vitest`).
