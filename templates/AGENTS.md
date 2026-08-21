# Agent Context & Operational Policy (AGENTS.md)
<!-- Standardized by the Agentic AI Foundation (AAIF) -->

This document establishes the machine-readable operational policy, tech stack conventions, and mandatory quality gates for AI coding agents operating in this repository.

---

## 1. Project Identity & Stack Architecture

- **Project Name:** `<project-name>`
- **Domain / Description:** `<1-2 sentence high-level overview of purpose>`
- **Architecture Pattern:** `<Clean Architecture | Modular Feature-Based | Monorepo | Microkernel>`
- **Core Runtime & Stack:**
  - **Language / Runtime:** `<e.g. TypeScript 5.x / Node 22 / Python 3.12 / Rust 1.80>`
  - **Framework:** `<e.g. Next.js 15 (App Router) | FastAPI | Axum>`
  - **Database & ORM:** `<e.g. PostgreSQL + Drizzle ORM | SQLite + Prisma>`
  - **Styling & UI:** `<e.g. Tailwind CSS v4 + Motion.dev>`

---

## 2. Mandatory Commands (Executable Truth)

AI agents must use these exact commands. Do NOT guess package manager or CLI flags.

| Action | Command | Verification Signal |
|---|---|---|
| **Install Dependencies** | `pnpm install` | Exit code 0, `pnpm-lock.yaml` synced |
| **Development Server** | `pnpm dev` | Server listening on `http://localhost:3000` |
| **Production Build** | `pnpm build` | Clean bundle in `.next/` or `dist/` |
| **Run Unit / Integration Tests** | `pnpm test` | All test suites passing |
| **Typecheck (TypeScript Safety Gate)** | `npx tsc --noEmit` | 0 errors |
| **Linter & Formatter** | `pnpm lint` | 0 lint violations |

---

## 3. Directory Topography & Module Boundaries

```
src/
├── app/                  # Route handlers & React Server Components (Presentation/Entrypoint)
├── components/           # Presentational UI components (Atomic / Bento)
├── domain/               # Pure business models, types, and domain rules (Zero external dependencies)
├── services/             # Application services & business logic
├── adapters/             # External integration adapters (DB, 3rd party APIs)
└── lib/                  # Shared utilities and helpers
```

---

## 4. Invariants & Guardrails (Never-Do Rules)

1. **Modular Boundary Isolation:** Never import database drivers or external API clients directly into UI components or pure domain models.
2. **Anti-Monolith Constraint:** Keep individual files under ~150-200 lines. Refactor multi-concern files into dedicated submodules.
3. **Strict TypeScript & TDD:** Never use `any` or delete functional code to satisfy type errors. Always write tests first for new business logic.
4. **Environment Variables:** Never commit secrets. Reference `.env.example` for all required environment variables.
