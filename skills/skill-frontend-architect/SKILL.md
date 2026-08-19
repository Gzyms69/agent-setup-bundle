---
name: skill-frontend-architect
description: Advanced frontend architecture, UI/UX design patterns, UI library selection matrix, WCAG accessibility, Next.js 15+ Web Vitals, and 3D/Canvas orchestration. Use when designing, implementing, or refactoring React/Next.js/Vite interfaces, selecting UI stacks, managing complex state/animations, or optimizing frontend performance.
---

# Frontend Architect Skill

This skill provides expert architectural guidance for selecting modern frontend stacks, structuring maintainable components, eliminating generic AI design clichés, enforcing WCAG AA accessibility, and achieving elite-tier Web Vitals performance.

---

## 1. Frontend Architecture & Framework Selection

Select the simplest architecture that satisfies project constraints and SEO requirements:

| Goal / Context | Recommended Architecture | Primary Rationale & Constraints |
|---|---|---|
| **Public Web App / SEO-driven** | **Next.js 15+ (App Router)** | Hybrid SSR/SSG, Server Components, streaming hydration, dynamic routing, and search engine discoverability. |
| **Internal Dashboard / Admin / Heavy SPA** | **Vite + React (or TanStack Router)** | Zero server overhead, rapid HMR development cycles, rich client-side data state, and no SSR hydration pitfalls. |
| **Content-First / Marketing / Documentation** | **Astro** | Islands architecture, zero client-side JavaScript baseline, markdown/MDX native rendering, and instant LCP. |
| **Cross-Platform Mobile** | **Flutter / React Native** | Native compilation, shared mobile business logic, and native hardware access. |

---

## 2. UI Ecosystem & Component Library Decision Matrix

Before implementing components, adhere to the architectural paradigm of the chosen UI library. For full catalog, doc links, and install commands, see [`references/ui-ecosystem-matrix.md`](references/ui-ecosystem-matrix.md).

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
│ Tailwind+shadcn  │             │ AntD / Primereact│             │ Aceternity/Magic │
└──────────────────┘             └──────────────────┘             └──────────────────┘
```

### Strategic AI Execution Rules by Paradigm:
*   **Modern Standard (Tailwind CSS + Radix UI + shadcn/ui):**
    *   `shadcn/ui` is **code injection**, not an npm dependency. Never import directly from `shadcn/ui`. Place components in `@/components/ui/` and leverage the CLI (`npx shadcn@latest add <component>`).
    *   Combine with headless Radix primitives to guarantee uncompromised WCAG accessibility.
*   **Enterprise & Data-Dense (Ant Design, BlueprintJS, PrimeReact):**
    *   **Ant Design v5:** Strictly use `<ConfigProvider theme={{ ... }}>` design tokens. Avoid ad-hoc CSS overrides.
    *   **BlueprintJS:** Desktop-first analytics. Do not use for mobile-first responsive consumer apps.
    *   **PrimeReact / TanStack Table:** Ideal for virtualization, tree-grids, complex multi-column sorting, and cell editing.
*   **Component Suites & Ecosystems (Mantine, HeroUI, MUI, Chakra):**
    *   **Mantine v7:** Leverage Mantine hooks (`useDisclosure`, `useForm`) alongside components; adhere to CSS Modules.
    *   **HeroUI (NextUI):** Require `HeroUIProvider` at root; utilize Tailwind-based theme tokens.
    *   **Material UI (MUI):** Use `sx` prop for one-off styles, `styled()` for reusable components. Specify Material Design 2 or 3.
*   **Creative Flair & Animations (Aceternity UI, Magic UI, Framer Motion):**
    *   Treat Aceternity and Magic UI as copy-paste snippet architectures. Inspect source code and adapt to project Tailwind configurations rather than hallucinating external package imports.

---

## 3. UI/UX Design & Aesthetic Standards

### Spacing & Layout
*   **8-Point Grid:** Use a consistent 8px scale (`8px`, `16px`, `24px`, `32px`, `48px`, `64px`) for all margins, paddings, gap spacing, and dimensions. Never invent arbitrary pixel values (e.g. use `16px` or `12px` instead of `13px` or `17px`).
*   **Negative Space:** Use generous negative space to create visual hierarchy and cleanly separate unrelated layout regions.
*   **Mobile-First Design:** Always build for mobile viewports (`320px`) first, then progressively enhance layout structure for desktop breakpoints (`768px`, `1024px`, `1440px`).

### Typography
*   **Font Limit:** Maximum of two font families (one for headings, one for body text).
*   **Hierarchy:** Establish a clear type scale (e.g., `12px`, `14px`, `16px`, `20px`, `24px`, `32px`, `48px`) and never skip heading levels (`h1` -> `h2` -> `h3`).
*   **Readability:** Keep body text line-height at 1.5x, with 50-75 characters per line for optimal reading ergonomics.

### Color & Contrast
*   **Structured Palette:** Define primary, secondary, neutral (3-5 shades), and semantic color tokens (success, warning, error, info).
*   **Contrast Compliance:** Ensure all text-to-background combinations meet WCAG AA standards (minimum 4.5:1 for normal text, 3:1 for large text).
*   **Non-Color Coding:** Never rely on color alone to convey state or information. Always supplement color indicators with icons, text labels, or distinct patterns.

---

## 4. Eliminating the "AI Aesthetic" (Zero-Tolerance Guardrails)

AI-generated interfaces suffer from predictable template defaults. Eliminate these clichés to guarantee a bespoke, production-grade finish:

| AI Default | Why It Is a Problem | Production Quality |
|---|---|---|
| Fake "Online / Live" Pulsing Dots (`animate-pulse`) | Cringe cliché shouting "cheap AI generated page". Signals amateurish template design. | **TOTAL BAN on fake pulsing green status dots** unless displaying a real WebSocket / SSE live telemetry stream. |
| Fake Live Telemetry / Decorative Dots | Injects visual clutter and artificial status noise without real data. | Eliminate all decorative pulsing dots beside titles, footers, avatars, and headers. |
| Purple/indigo defaults | Makes every application look identical. | Use the project's actual, verified brand color palette tokens. |
| Excessive/heavy gradients | Adds visual noise, clashes with brand styles, and decreases readability. | Use flat backgrounds or subtle, brand-harmonized gradients. |
| Unconstrained rounding (`rounded-2xl` / `rounded-3xl` everywhere) | Signals "friendly" template default without respecting component scale hierarchy. | Match corner radius to the component scale in the design system (`rounded-md` or `rounded-lg`). |
| Truncation Clashing on Badges | Adding `truncate` to flex parents clips status badges (e.g. `[🔒 Private]`). | Protect badges and critical labels with `shrink-0 whitespace-nowrap`. |
| Generic hero layouts | Placed as a shortcut instead of tailoring layout to the actual user action. | Content-first layouts tailored to user tasks. |
| Lorem ipsum placeholders | Hides layout overflow, line-wrapping issues, and structural bugs. | Write realistic placeholder content reflecting actual production data length. |
| Oversized padding | Wastes screen real estate and dilutes layout scanning hierarchy. | Structured spacing scales matching grid density. |
| Shadow-heavy depth | Blurs visual hierarchy and slows CSS render cycles on low-end hardware. | Flat borders, sharp cuts, or extremely subtle, low-blur shadows. |

### Total Ban on Cringe AI Gimmicks:
1. **No Fake Status Dots:** Never add pulsing green/emerald dots (`animate-pulse rounded-full`) to footers, headers, cards, or hero sections to fake "online" or "active" presence.
2. **No Fake Terminal Typing Sequences:** Never add unsolicited typewriter animations or terminal boot logs unless explicitly requested by the user.
3. **No Buzzword Salad:** Ban cliché AI buzzwords ("Unleash", "Elevate", "Next-Gen", "Seamlessly", "Revolutionize", "Tapestry", "Delve").
4. **No Destructive Truncate:** Never place `truncate` on flex containers that hold status badges, action buttons, or interactive chips. Keep badges atomic with `shrink-0 whitespace-nowrap`.

---

## 5. Component Architecture & State Management

### File Structure (Colocation)
Colocate all assets related to a specific component. Keep component implementations focused (split components exceeding 200 lines):
```
src/components/
  TaskList/
    TaskList.tsx          # Component implementation
    TaskList.test.tsx     # Unit & integration tests
    use-task-list.ts      # Custom hook for complex local state
    types.ts              # Component-specific interfaces & contracts
```

### Component Patterns
*   **Composition over Configuration:** Avoid monolithic components with dozens of boolean layout properties. Use children and sub-components:
    ```tsx
    // Good (Composable & Extensible)
    <Card>
      <CardHeader><CardTitle>Tasks</CardTitle></CardHeader>
      <CardBody><TaskList tasks={tasks} /></CardBody>
    </Card>
    ```
*   **Container/Presenter Separation:** Separate data fetching logic from presentation rendering to keep components modular and purely testable.

### 6-Level State Selection Matrix
Choose the simplest state scope that satisfies requirements. Avoid prop-drilling deeper than 3 levels:
```
1. Local state (useState, useReducer)  → Component-specific UI state (e.g. dropdown open, form input)
2. Lifted state                       → Shared between 2-3 immediate sibling components
3. URL state (searchParams)           → Filters, search query, pagination, shareable view state
4. Context API                        → Read-heavy, write-rare configurations (e.g. theme, locale, auth user)
5. Server state (TanStack Query, SWR) → Remote data fetching, caching, deduplication, optimistic mutations
6. Global store (Zustand, Redux)      → Complex client-side state shared app-wide (e.g. audio player, canvas editor)
```

---

## 6. Next.js 15+ Web Vitals & Hydration Protocol

Optimizations to achieve 100 Lighthouse scores and smooth navigation:

### Layout Stability & Scroll Offset (Lenis + SSR)
*   **The CLS/Lenis Scroll Trap:** Never use client-side lazy loading (e.g., `IntersectionObserver` or `next/dynamic` with `ssr: false`) for sections that are scroll targets or located above them. Lenis calculates target scroll destination coordinates once on load; dynamic layout shifts (CLS) mid-scroll cause navigation offsets.
*   **SSR Mandate for Structural Content:** Always use `next/dynamic` with `ssr: true` for layout-structural HTML/CSS sections. This guarantees that the final DOM height is known at 0ms, eliminating CLS.
*   **Native Offsets:** For sticky headers, use Lenis' native `offset` parameter (`lenis.scrollTo('#id', { offset: -64 })`) or CSS `scroll-margin-top`.

### Critical Path & Style Strategy
*   **Inline CSS Experiment:** Enable CSS inlining via `experimental.inlineCss: true` in `next.config.ts` to eliminate render-blocking CSS links.
*   **Zero-FOUC Fallbacks:** For heavy dynamic assets (e.g., 3D canvas, videos), use pure CSS Mesh Gradients (blurred mix-blend divs) as placeholders to ensure layout completeness at 0ms.
*   **Header Flash Mitigation:** Use inline `<script>` tags in `<head>` to force light/dark background-color class injection before CSS parsing.

### Runtime Bundle and Hydration Efficiency
*   **Idle-Until-Urgent Assets:** Heavy libraries (e.g., Three.js/WebGL) must load ONLY on user interaction (scroll/mouse-move/touch) to protect the initial hydration window and Total Blocking Time (TBT).
*   **LazyMotion Architecture:** Wrap Framer Motion animations in `<LazyMotion features={domAnimation} strict>` and use `m.*` tags instead of standard `motion.*` tags to remove ~50KB+ from the initial JS bundle.
*   **Server Component Primacy:** Keep high-traffic routes (like `page.tsx`) as Server Components. Isolate client-side state into small interactive islands.
*   **Hydration Isolation:** Wrap dynamic Vanilla JS elements (like WebGL canvases) in `dangerouslySetInnerHTML` with `suppressHydrationWarning` to prevent React from resetting listeners during hydration.
*   **Third-Party Deferral:** Wrap non-critical tools (Analytics, SpeedInsights) in deferred, client-side only components after hydration.

---

## 7. Advanced 3D Interaction & Canvas Orchestration

### 3D Perspective Stability (The Proxy Map Pattern)
To prevent "Recursive Hit-Testing Loops" and system instability in 3D perspective scenes (e.g., using `transform-style: preserve-3d`), decouple visual rendering from pointer interaction:
*   **Visual Bypass:** Set `pointer-events: none` on all 3D-transformed rendering elements.
*   **Active Proxy Hitboxes:** Use a flat, 2D transparent overlay layer (z-index 100) containing static 2D rectangles as event targets.
*   **Magnetic Anchor Pattern:** For localized 3D magnetism, cache the element's `getBoundingClientRect()` exactly ONCE during `onPointerEnter`. Use this frozen center coordinates for delta calculations to prevent coordinates from "swimming" during rotation.
*   **Motion Sync:** Update global Framer Motion `MotionValues` from the Proxy hitboxes. Subscribe to these values in the 3D visual layer to ensure 60fps synchronization without React re-renders.

### Oversized Container Strategy (No Clipping)
*   For sprawling background canvas effects (Shaders, Canvas, Particles) that must feel unbounded, use containers larger than the viewport (e.g., `150vw`, `150vh`).
*   Place these effects into a single, unified `fixed inset-0` Layer 0 container with low z-index.
*   When increasing container scale, adjust shader proximity parameters (reduce `baseRadius` or `radiusStep`) and increase particle thickness/line weight to maintain visual density on the expanded canvas.

---

## 8. Dynamic CSS, Grid Math, and Brand Theming

### Grid vs Flexbox Layout Integrity
*   **The Percentage + Gap Trap:** When using `display: flex` with column widths defined in percentages (e.g., `flex: 0 0 30%`) and a `gap`, the total width will exceed 100% of the parent container, leading to layout blowout or clipping (if `overflow-x: hidden` is set).
*   **The Grid Solution:** Use `display: grid` with fractional units (`grid-template-columns: 3fr 4.5fr 2.5fr`). Grid mathematically deducts the `gap` from the available space before distributing the fractions, ensuring a perfect 100% fit without clipping.

### Dynamic Brand Variables
*   **CSS Variable Injection:** Avoid hardcoding brand colors. Pass a dynamic hex code via React inline styles: `style={{ "--item-color": project.color } as React.CSSProperties}`.
*   **Intelligent Mixing:** Use native CSS `color-mix(in srgb, var(--item-color) 10%, transparent)` to dynamically generate borders, backgrounds, and hover styles based on that single brand color variable.

### Animation Safety & Navigation UX
*   **Pseudo-Element Shimmers:** When using `::before` or `::after` to create sliding hover effects, transition both `transform` (e.g., `translateX(-100%)` to `100%`) and `opacity` (0 to 1). Rest state must be `opacity: 0` to prevent sub-pixel leaks or rendering artifacts.
*   **Framer Motion `layoutId` Boundaries:** Applying `layoutId` to elements confined within strict CSS Grid/Flex containers can cause width clipping or squishing during Shared Layout transitions. Remove `layoutId` from secondary navigation elements if they must organically fill their flex columns.
*   **Navigation UX (Active State Preservation):** In side navigation or tabs, never remove the currently active item from the list. Maintain context with an `.active` state and set `cursor: default` on the current page item.

---

## 9. Semantic HTML5 & Native Optimizations

Prioritize native web platform capabilities over heavy JavaScript dependencies:
*   **Native Modals & Drawers:** Prefer native `<dialog>` elements with `showModal()` for accessible backdrop layering and focus trapping.
*   **Native Expandables:** Use `<details>` and `<summary>` for lightweight accordions and FAQ sections without adding React state or JS overhead.
*   **Semantic Landmarks:** Structure layouts with `<header>`, `<nav>`, `<main>`, `<aside>`, `<article>`, and `<footer>` rather than unstructured `<div>` hierarchies.

---

## 10. WCAG 2.1 AA Accessibility (QA Gate)

Every component must satisfy these accessibility requirements before deployment:
*   **Keyboard Accessibility:** Every interactive element must be focusable via `Tab` and triggerable via `Enter` or `Space`. Never attach click handlers to static `div` tags without `role="button"`, `tabIndex={0}`, and `onKeyDown`.
*   **ARIA Labelling:** Provide descriptive labels for icon buttons (e.g. `<button aria-label="Close dialog"><XIcon /></button>`) and link input elements to `<label htmlFor="...">` tags.
*   **Focus Trapping:** When a modal, drawer, or dialog is open, trap keyboard focus within the modal window. Return focus to the trigger element upon dismissal.
*   **Skeleton Loading:** Use pulsing skeleton blocks instead of generic full-screen spinner wheels to represent loading states.
*   **Optimistic UI Updates:** Apply optimistic state mutations for user actions (e.g., toggling checklists, liking posts) to make interaction feel instant, rolling back state automatically if the API request fails.

---

## 11. Single Source of Truth (SSOT) & Anti-Duplication Protocol

*   **Audit Existing UI & API Clients:** Before creating any new UI component, modal, input control, or API fetch hook, audit the existing component library (`components/`, `lib/`) using `grep_search` and `list_dir`.
*   **Reuse Core Design System:** Reuse existing buttons, inputs, badge pills, and dialogs. Never introduce ad-hoc CSS classes or alternative button abstractions that clash with the design system.
*   **Unified API Contracts:** Always bind frontend views to canonical REST/GraphQL endpoints rather than creating mock or duplicate API routes. If a component needs extra data, enhance the backend endpoint in-place.
*   **Zero Parallel State Stores:** Maintain single authoritative state models (Zustand/React Query/Context) for user profiles, session tokens, and feature flags.

---

## 12. Verification Checklist

Before completing a frontend task, verify:
- [ ] **SSOT Audit:** Codebase audited for existing components, hooks, and endpoints.
- [ ] **Type & Build Check:** Component compiles without TypeScript errors (`npx tsc --noEmit`) and produces no runtime console warnings.
- [ ] **Anti-AI Review:** Clean of fake pulsing dots, fake typewriter logs, AI buzzwords, and badge-clipping truncates.
- [ ] **Responsive check:** Usable and free from horizontal overflow at `320px`, `768px`, `1024px`, and `1440px`.
- [ ] **Keyboard test:** Complete keyboard navigation (`Tab`, `Enter`, `Space`, `Esc`) with visible focus outlines.
- [ ] **Contrast check:** Text and interactive elements meet WCAG AA contrast standards (4.5:1 / 3:1).
- [ ] **State handling:** Loading, error, and empty states explicitly designed.
- [ ] **Web Vitals check:** Zero layout shifts (CLS) during page loads and scroll navigation.
