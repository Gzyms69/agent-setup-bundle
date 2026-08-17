# Modular Architecture & Boundary Isolation

## 1. Single Responsibility & The Anti-Monolith Constraint (Max ~150-200 lines)
*   **FORBIDDEN:** Creating monolithic "God Files" that combine business logic, UI rendering, network calls, state management, and styling.
*   **Split Rule:** If a file exceeds ~200 lines or addresses more than one domain concern, it MUST be refactored into:
    - Domain Models / Types (`models/`, `schemas/`, `types/`)
    - Service / Business Logic (`services/`, `engine/`)
    - API / Data Access / Adapters (`api/`, `adapters/`, `repositories/`)
    - Presentation UI (`components/`, `views/`, `styles/`)
*   **Ban on Catch-All Utils:** NEVER create catch-all `utils.py` or `helpers.ts`. Name files strictly by their cohesive domain purpose (e.g. `string_sanitizer.py`, `crypto_hasher.py`, `date_formatter.ts`).

## 2. Dependency Inversion & Strict Layering (Clean / Hexagonal Architecture)
*   **Layer Rules:**
    1. `Domain / Core` (Pure business logic, schemas, domain exceptions) -> **NEVER** imports from API frameworks, Web UI, database drivers, or CLI runners.
    2. `Ports & Adapters` (Database repositories, tool runners, scrapers) -> Implements Core interfaces, never alters or couples to Core domain models.
    3. `Apps & Entrypoints` (CLI, FastAPI, Nuxt/Next) -> Injects adapters into Core and triggers execution.
*   **Circular Dependency Ban:** Dependencies flow strictly downward (`Apps` -> `Adapters` -> `Core`). Circular imports are strictly forbidden.

## 3. Typed Boundary Contracts
*   **Strict Contracts:** Every boundary crossing (module-to-module, backend-to-frontend, CLI-to-core) MUST use typed Pydantic models or TypeScript interfaces.
*   **Zero Untyped Dictionaries:** Never pass arbitrary `dict[str, Any]` or `any` across module boundaries.

## 4. Isolated Failure Envelopes & Error Boundaries
*   Every external integration, plugin, subprocess, or scraper MUST run inside an execution boundary with:
    - Explicit timeouts (`asyncio.wait_for` / `AbortController`).
    - Typed domain error handling (`PluginError`, `TimeoutError`, `RateLimitError`).
    - Zero cascading crashes: a failure in one plugin/task must NEVER crash sibling tasks or the host process.

## 5. Anti-Monolith UI Pattern
*   UI components must follow the Container/Presentational pattern:
    - **Presentational Components:** Pure visual rendering, receive props and emit events, contain NO data fetching.
    - **Container / Composables:** Manage state, lifecycle hooks, and API communication.
    - **Zero CDN Injections:** Third-party libraries (e.g. graph renderers, visualizers) must be installed as managed npm dependencies with proper TypeScript declarations, never injected via loose `<script src="unpkg...">` tags without error boundaries.
