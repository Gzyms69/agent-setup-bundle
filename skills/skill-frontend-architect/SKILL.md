---
name: skill-frontend-architect
description: Advanced frontend architecture, UI/UX design patterns, library selection, WCAG accessibility, and performance optimization. Use when designing, implementing, or refactoring React/Next.js interfaces, managing complex states/animations, or optimizing performance and WebGL/3D interfaces.
---

# Frontend Architect Skill

This skill provides expert guidance for building high-fidelity, responsive, accessible, and performance-optimized user interfaces.

---

## 1. UI/UX Design & Aesthetic Standards

### Spacing & Layout
*   **8-Point Grid:** Use a consistent 8px scale for all margins, paddings, gap spacing, and dimensions. Never invent arbitrary pixel values (e.g., use `16px` or `12px` instead of `13px`).
*   **Negative Space:** Use generous negative space to create visual hierarchy and separate unrelated layout regions.
*   **Mobile-First Design:** Always build for mobile viewports (320px) first, then progressively enhance layout structure for desktop breakpoints (768px, 1024px, 1440px).

### Typography
*   **Font Limit:** Maximum of two font families (one for headings, one for body text).
*   **Hierarchy:** Establish a clear type scale (e.g., 12, 14, 16, 20, 24, 32px) and do not skip heading levels (e.g., `h1` -> `h2` -> `h3`).
*   **Readability:** Keep body text line-height at 1.5x, with 50-75 characters per line for ideal reading speed.

### Color & Contrast
*   **Structured Palette:** Define primary, secondary, neutral (3-5 shades), and semantic color tokens (success, warning, error, info).
*   **Contrast Compliance:** Ensure all text-to-background combinations meet WCAG AA standards (minimum 4.5:1 for normal text, 3:1 for large text).
*   **Non-Color Coding:** Never rely on color alone to convey state or information. Always supplement color indicators with icons, text labels, or distinct patterns.

---

## 2. Eliminating the "AI Aesthetic"

AI-generated interfaces suffer from predictable defaults. Avoid these patterns to ensure a premium, custom feel:

| AI Default | Why It Is a Problem | Production Quality |
|---|---|---|
| Purple/indigo defaults | Makes every application look identical. | Use the project's actual, verified color palette tokens. |
| Excessive/heavy gradients | Adds visual noise, clashes with brand styles, and decreases readability. | Use flat backgrounds or subtle, brand-harmonized gradients. |
| Unconstrained rounding (`rounded-2xl`) | Signals "friendly" template default without respecting component scale hierarchy. | Match corner radius to the component scale in the design system. |
| Generic hero layouts | Placed as a shortcut instead of tailoring layout to the actual user action. | Content-first layouts tailored to user tasks. |
| Lorem ipsum placeholders | Hides layout overflow, line-wrapping issues, and structural bugs. | Write realistic placeholder content reflecting actual length. |
| Oversized padding | Wastes screen real estate and dilutes layout scanning hierarchy. | Structured spacing scales matching grid density. |
| Shadow-heavy depth | Blurs visual hierarchy and slows CSS render cycles on low-end hardware. | Flat borders, sharp cuts, or extremely subtle, low-blur shadows. |

---

## 3. Component Architecture & State Management

### File Structure (Colocation)
Colocate all assets related to a specific component. Keep component implementations focused (split components exceeding 200 lines):
```
src/components/
  TaskList/
    TaskList.tsx          # Component implementation
    TaskList.test.tsx     # Tests
    use-task-list.ts      # Custom hook for complex local state
    types.ts              # Component-specific types
```

### Component Patterns
*   **Composition over Configuration:** Avoid monolithic components with dozens of layout properties. Use children and sub-components:
    ```tsx
    // Good (Composable)
    <Card>
      <CardHeader><CardTitle>Tasks</CardTitle></CardHeader>
      <CardBody><TaskList tasks={tasks} /></CardBody>
    </Card>
    ```
*   **Container/Presenter Separation:** Separate data fetching logic from presentation rendering to keep components testable and modular.

### State Selection Matrix
Choose the simplest approach that solves the requirement. Avoid prop-drilling deeper than 3 levels:
```
Local state (useState)           → Component-specific UI state
Lifted state                     → Shared between 2-3 sibling components
Context                          → Read-heavy, write-rare configurations (e.g., themes, auth)
URL state (searchParams)         → Filters, pagination, shareable page views
Server state (SWR / React Query) → Fetching, caching, and validating remote data
Global store (Zustand / Redux)    → Complex client state shared app-wide
```

---

## 4. Next.js 15+ Web Vitals & Hydration Protocol

This protocol defines advanced Next.js 15+ optimization techniques to achieve perfect Lighthouse scores and flawless smooth navigation.

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

---

## 5. Advanced 3D Interaction & Canvas Orchestration

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

## 6. Dynamic CSS, Grid Math, and Brand Theming

### Grid vs Flexbox Layout Integrity
*   **The Percentage + Gap Trap:** When using `display: flex` with column widths defined in percentages (e.g., `flex: 0 0 30%`) and a `gap`, the total width will exceed 100% of the parent container, leading to layout blowout or clipping (if `overflow-x: hidden` is set).
*   **The Grid Solution:** Use `display: grid` with fractional units (`grid-template-columns: 3fr 4.5fr 2.5fr`). Grid mathematically deducts the `gap` from the available space before distributing the fractions, ensuring a perfect 100% fit without clipping.

### Dynamic Brand Variables
*   **CSS Variable Injection:** Avoid hardcoding brand colors. Pass a dynamic hex code via React inline styles: `style={{ "--item-color": project.color } as React.CSSProperties}`.
*   **Intelligent Mixing:** Use native CSS `color-mix(in srgb, var(--item-color) 10%, transparent)` to dynamically generate borders, backgrounds, and hover styles based on that single brand color variable.

### Animation Safety
*   **Pseudo-Element Shimmers:** When using `::before` or `::after` to create sliding hover effects, transition both `transform` (e.g., `translateX(-100%)` to `100%`) and `opacity` (0 to 1). Rest state must be `opacity: 0` to prevent sub-pixel leaks or rendering artifacts.
*   **Framer Motion `layoutId` Boundaries:** Applying `layoutId` to elements confined within strict CSS Grid/Flex containers can cause width clipping or squishing during Shared Layout transitions. Remove `layoutId` from secondary navigation elements if they must organically fill their flex columns.

---

## 7. WCAG 2.1 AA Accessibility (QA Gate)

Every component must meet these accessibility criteria:
*   **Keyboard Accessibility:** Every interactive element must be focusable via `Tab` and triggerable via `Enter` or `Space`. Avoid adding click handlers to static divs unless you explicitly set `role="button"`, `tabIndex={0}`, and handle `onKeyDown`.
*   **ARIA Labelling:** Provide descriptive labels for elements lacking visible text (e.g., `<button aria-label="Close dialog"><XIcon /></button>`) and link input elements to `<label htmlFor="...">` tags.
*   **Focus Trapping:** When a modal, drawer, or dialog is open, trap keyboard focus within that modal window using focus traps. Return focus to the trigger element upon closing.
*   **Skeleton Loading:** Use pulsing skeleton blocks instead of generic full-screen spinner wheels to represent loading states.
*   **Optimistic UI Updates:** Apply optimistic state mutations for user actions (e.g., toggling checklists, liking posts) to make interaction feel instant, rolling back state automatically if the API request fails.

---

## 8. Single Source of Truth (SSOT) & Anti-Duplication Protocol

*   **Audit Existing UI & API Clients:** Before creating any new UI component, modal, input control, or API fetch hook, audit the existing component library (`components/`, `lib/`) using `grep_search` and `list_dir`.
*   **Reuse Core Design System:** Reuse existing buttons, inputs, badge pills, and dialogs. Never introduce ad-hoc CSS classes or alternative button abstractions that clash with the design system.
*   **Unified API Contracts:** Always bind frontend views to canonical REST/GraphQL endpoints rather than creating mock or duplicate API routes. If a component needs extra data, enhance the backend endpoint in-place.
*   **Zero Parallel State Stores:** Maintain single authoritative state models (Zustand/React Query/Context) for user profiles, session tokens, and feature flags.

---

## 9. Verification Checklist

Before completing a frontend task, verify:
- [ ] Codebase audited for existing components, hooks, and endpoints (SSOT & DRY enforced).
- [ ] Component compiles without warning and generates no console runtime errors.
- [ ] Responsive check: interface is usable and free from layout overflow at 320px, 768px, 1024px, and 1440px.
- [ ] Keyboard test: you can navigate through all interactive elements using `Tab` and trigger actions.
- [ ] Contrast ratios and text sizes pass WCAG AA standards.
- [ ] Loading, error, and empty states are designed and handled.
- [ ] Zero layout shifts (CLS) occur during page loads and scroll navigation.
