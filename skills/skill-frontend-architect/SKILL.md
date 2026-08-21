---
name: skill-frontend-architect
description: Master Frontend Architecture, Next.js 15+ App Router, React Server Components (RSC), Client Island Boundaries, State Orchestration (Zustand, React Query), WCAG 2.1/2.2 AA Accessibility, and Clean Component Systems. Use when designing application structure, managing server/client boundaries, structuring modular components, orchestrating complex state, or enforcing strict accessibility gates.
---

# Frontend Architect Skill

This skill provides expert architectural guidance for structuring production-grade React and Next.js applications, defining clean client/server module boundaries, orchestrating local and global state, enforcing WCAG 2.1/2.2 AA accessibility standards, and achieving elite Web Vitals.

> [!NOTE]
> * For **Art Direction, Visual Philosophy, Aesthetics, Fontjoy Typography, and Color Theory**, activate [`skill-creative-design`](../skill-creative-design/SKILL.md).
> * For **Motion Animations (motion.dev), CSS Subgrid, Container Queries, and 21st.dev Components (BKLit, Kokonut, Origin, Cult, Animata)**, activate [`skill-design-engineering`](../skill-design-engineering/SKILL.md).

---

## 1. Framework & Application Architecture

Select the simplest architecture that satisfies project constraints and SEO requirements:

| Goal / Context | Recommended Architecture | Primary Rationale & Constraints |
|---|---|---|
| **Public Web App / SEO-driven** | **Next.js 15+ (App Router)** | Hybrid SSR/SSG, React Server Components (RSC), streaming hydration, dynamic routing, and search engine discoverability. |
| **Internal Dashboard / Heavy SPA** | **Vite + React (or TanStack Router)** | Zero server overhead, rapid HMR development cycles, rich client-side data state, and no SSR hydration pitfalls. |
| **Content-First / Marketing** | **Astro** | Islands architecture, zero client-side JavaScript baseline, markdown/MDX native rendering, and instant LCP. |
| **Cross-Platform Mobile** | **React Native / Flutter** | Native compilation, shared mobile business logic, and native hardware access. |

---

## 2. UI Ecosystem & Component Library Decision Matrix

Adhere to the architectural paradigm of the chosen UI library. For the complete catalog, doc links, and install commands of all 30 ecosystem tools, see [`references/ui-ecosystem-matrix.md`](references/ui-ecosystem-matrix.md).

```
                      ┌─────────────────────────────────────────┐
                      │        UI Stack Selection Tree          │
                      └────────────────────┬────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         │                                 │                                 │
         ▼                                 ▼                                 ▼
┌──────────────────┐             ┌──────────────────┐             ┌──────────────────┐
│ Modern Standard  │             │ Enterprise Data  │             │ Creative Motion  │
│ Tailwind+shadcn  │             │ AntD v5 / Mantine│             │ Motion / 21st.dev│
└──────────────────┘             └──────────────────┘             └──────────────────┘
```

### Strategic AI Execution Rules by Paradigm:
*   **Modern Standard (Tailwind CSS + Radix UI + shadcn/ui):**
    *   `shadcn/ui` is **code injection**, not an npm dependency. Never import directly from `shadcn/ui`. Place components in `@/components/ui/` and leverage the CLI (`npx shadcn@latest add <component>`).
    *   Combine with headless Radix primitives to guarantee uncompromised WCAG 2.1/2.2 AA accessibility.
*   **Enterprise & Data-Dense (Ant Design v5, BlueprintJS, PrimeReact):**
    *   **Ant Design v5:** Strictly use `<ConfigProvider theme={{ ... }}>` design tokens. Avoid ad-hoc CSS overrides.
    *   **BlueprintJS:** Desktop-first analytics. Do not use for mobile-first consumer apps.
    *   **PrimeReact / TanStack Table:** Ideal for virtualization, tree-grids, complex multi-column sorting, and cell editing.
*   **Component Suites & Ecosystems (Mantine v7, HeroUI, MUI, Chakra v3):**
    *   **Mantine v7:** Leverage Mantine hooks (`useDisclosure`, `useForm`) alongside components; adhere strictly to CSS Modules / PostCSS.
    *   **HeroUI (d. NextUI):** Require `HeroUIProvider` at root; utilize Tailwind-based theme tokens.
    *   **Material UI (MUI):** Use `sx` prop for one-off styles, `styled()` for reusable components. Specify Material Design 2 or 3.
*   **Creative Flair & Motion (Motion, Kokonut UI, BKLit UI, Origin UI, Cult UI, 21st.dev):**
    *   Delegate to [`skill-design-engineering`](../skill-design-engineering/SKILL.md) for code recipes, Subgrid layout math, and 120fps motion physics.

---

## 3. Server Components (RSC) & Client Island Boundaries

In Next.js 15+ App Router, enforce strict boundary discipline:
*   **Server Component Primacy:** Keep high-traffic routes (`page.tsx`, `layout.tsx`) as Server Components to stream data with zero client-side JavaScript.
*   **Isolate Client State:** Never add `"use client"` at the top of a page layout. Isolate interactive and animated elements into leaf-node client components:
    ```tsx
    // Good: Small interactive leaf island
    // app/components/ThemeToggle.tsx
    "use client";
    import { useState } from "react";
    export function ThemeToggle() { ... }
    ```
*   **Hydration Isolation:** Wrap dynamic Vanilla JS or Canvas elements in `suppressHydrationWarning` to prevent React from resetting listeners during hydration.

---

## 4. 6-Level State Selection Matrix

Choose the simplest state scope that satisfies requirements. Avoid prop-drilling deeper than 3 levels:
```
1. Local state (useState, useReducer)  → Component-specific UI state (e.g. dropdown open, form input)
2. Lifted state                       → Shared between 2-3 immediate sibling components
3. URL state (searchParams)           → Filters, search query, pagination, shareable view state
4. Context API                        → Read-heavy, write-rare configurations (e.g. theme, locale, auth user)
5. Server state (TanStack Query, SWR) → Remote data fetching, caching, deduplication, optimistic mutations
6. Global store (Zustand)             → Complex client-side state shared app-wide (e.g. audio player, canvas editor)
```

---

## 5. WCAG 2.1 / 2.2 AA Accessibility (QA Gate)

Every component must satisfy these non-negotiable accessibility criteria before deployment:
*   **Keyboard Accessibility:** Every interactive element must be focusable via `Tab` and triggerable via `Enter` or `Space`. Never attach click handlers to static `div` tags without `role="button"`, `tabIndex={0}`, and `onKeyDown`.
*   **Touch Target Size:** Interactive targets must meet minimum physical size criteria (minimum 24x24px, recommended 44x44px bounding area).
*   **ARIA Labelling:** Provide descriptive labels for icon buttons (e.g. `<button aria-label="Close dialog"><XIcon /></button>`) and link input elements to `<label htmlFor="...">` tags.
*   **Focus Trapping:** When a modal, drawer, or dialog is open, trap keyboard focus within the modal window. Return focus to the trigger element upon dismissal.
*   **Reduced Motion:** Respect user preferences via `useReducedMotion()` from `motion/react` or CSS `@media (prefers-reduced-motion: reduce)`.

---

## 6. Verification Checklist

Before completing a frontend architecture task, verify:
- [ ] **SSOT Audit:** Codebase audited for existing components, hooks, and endpoints (no duplicate implementations).
- [ ] **Type & Build Check:** Component compiles without TypeScript errors (`npx tsc --noEmit`) and produces no runtime console warnings.
- [ ] **Boundary Check:** `"use client"` restricted to interactive leaf nodes; page roots remain Server Components where applicable.
- [ ] **Accessibility Gate:** Full keyboard navigation (`Tab`, `Enter`, `Space`, `Esc`) and WCAG 2.1/2.2 AA contrast verified.
- [ ] **Responsive Check:** Free from horizontal overflow across mobile (320px), tablet (768px), and desktop (1440px) viewports.
