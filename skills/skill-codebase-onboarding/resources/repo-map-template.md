# REPO_MAP: [Project Name]

> Quick Architecture & Operational Reference for AI Agents & Developers.

## 1. Project Overview
- **Name:** [Project Name]
- **Type:** [Web App / CLI / Library / Monorepo / Backend Microservice]
- **Primary Stack:** [e.g., Node.js 20, Next.js 15, TypeScript 5.6, PostgreSQL, Prisma]
- **Package Manager:** [pnpm / npm / uv / cargo]

## 2. Deterministic Commands
| Purpose | Command | Notes / Flags |
| :--- | :--- | :--- |
| **Dev** | `pnpm dev` | Starts local dev server at localhost:3000 |
| **Build** | `pnpm build` | Production bundle generation |
| **Test** | `pnpm test` | Runs unit & integration test suites |
| **Typecheck** | `npx tsc --noEmit` | Strict TS validation |
| **Lint** | `pnpm lint` | ESLint checking |

## 3. Directory Layout & Module Boundaries
```
├── src/
│   ├── app/            # Next.js App Router (Pages, Routes, Layouts)
│   ├── components/     # UI Components (Presentational)
│   ├── lib/            # Shared utilities and helper functions
│   ├── server/         # Backend services, DB queries, business logic
│   └── types/          # TypeScript types & interfaces
├── prisma/             # Database schema & migrations
└── tests/              # End-to-End & Integration test suites
```

## 4. Key Architectural Invariants & Rules
1. **Separation of Concerns:** Components in `src/components/` MUST NOT perform direct database queries.
2. **Type Safety:** No use of `any`. All schemas validated via Zod.
3. **Environment:** Secrets loaded exclusively through `src/env.ts`.

## 5. Main Entrypoints & Schema Locations
- **HTTP / Web Entrypoint:** `src/app/page.tsx`
- **API Entrypoint:** `src/app/api/`
- **Database Schema:** `prisma/schema.prisma`
- **Config / Environment:** `.env.example`
