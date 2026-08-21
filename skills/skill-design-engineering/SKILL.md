---
name: skill-design-engineering
description: Master Creative Frontend Engineering, Design Implementation, Motion Animation Engine (motion.dev), CSS Subgrid, Container Queries (@container), 21st.dev Component Ecosystem (BKLit UI, Kokonut UI, Origin UI, Cult UI, Animata, Fancy Components), and 60/120fps Interaction Craftsmanship. Use when implementing high-end UI designs into pixel-perfect React/Next.js code, coding complex layout transitions, implementing physics-based spring animations, building responsive Bento Grids, or orchestrating micro-interactions.
---

# Design Engineering & Creative Frontend Craft Skill

This skill provides expert technical execution for translating high-end visual design and art direction into fluid, performant (60/120fps), accessible production code.

---

## 1. Motion Animation Engine ([motion.dev](https://motion.dev/))

Modern standard for React and JavaScript animation (successor to Framer Motion v12+).

### Core Package & Subpath Standards:
*   **Installation:** `npm install motion`
*   **React Imports:** `import { motion, AnimatePresence, useAnimate, useScroll, useTransform, useSpring, useInView, LazyMotion, domAnimation, m } from "motion/react"`
*   **Vanilla JS / Core Imports:** `import { animate, scroll, inView, stagger, timeline } from "motion"` (or `motion/mini` for ~2.3KB WAAPI).

### Essential Motion Patterns:
1.  **FLIP & Shared Layout Transitions (`layout` / `layoutId`):**
    Use `layout` for automatic FLIP transitions when dimensions change, and `layoutId` for morphing elements across different component states (e.g. active tab indicators, expanding cards):
    ```tsx
    {activeTab === tab.id && (
      <motion.div
        layoutId="activePill"
        className="absolute inset-0 bg-white/10 rounded-lg"
        transition={{ type: "spring", stiffness: 380, damping: 30 }}
      />
    )}
    ```
2.  **Exit Animations (`<AnimatePresence>`):**
    Always wrap unmounting conditional elements in `<AnimatePresence mode="wait" | "popLayout">` with unique, stable `key` props to eliminate layout popping:
    ```tsx
    <AnimatePresence mode="popLayout">
      {isOpen && (
        <motion.div
          key="modal"
          initial={{ opacity: 0, scale: 0.95, y: 10 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 10 }}
          transition={{ type: "spring", stiffness: 400, damping: 32 }}
        />
      )}
    </AnimatePresence>
    ```
3.  **Bundle Optimization with `LazyMotion`:**
    In performance-critical applications, wrap motion components in `<LazyMotion features={domAnimation} strict>` and use `<m.div>` primitives to save ~50KB+ gzip bundle size.
4.  **Imperative Timelines (`useAnimate`):**
    Orchestrate multi-step animations without triggering React component re-renders:
    ```tsx
    const [scope, animate] = useAnimate();
    const handleTrigger = async () => {
      await animate("span", { opacity: 0 }, { duration: 0.2 });
      await animate("svg", { rotate: 180 }, { type: "spring" });
    };
    ```

For exhaustive Motion API recipes, see [`references/motion-dev-mastery.md`](references/motion-dev-mastery.md).

---

## 2. Modern CSS Layout Engineering: Subgrid & Container Queries

Never use hardcoded pixel heights (`h-[450px]`) or brittle viewport queries for modular cards.

### 1. CSS Subgrid Precision:
Subgrid inherits track definitions from parent grids, aligning titles, bodies, and footers across siblings:
```tsx
// Parent Bento Grid
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">
  {/* Subgrid Card Item */}
  <div className="col-span-1 grid grid-rows-subgrid row-span-3 p-6 rounded-2xl bg-neutral-900 border border-white/10">
    <div className="text-xs font-mono text-neutral-400">Header / Badge</div>
    <div className="py-2"><h4 className="text-xl font-heading text-white">Dynamic Title</h4></div>
    <div className="mt-auto pt-4 border-t border-white/10 text-sm">Aligned Footer</div>
  </div>
</div>
```

### 2. Container Queries (`@container`):
Make components self-aware and responsive to their direct parent container width rather than the viewport:
```html
<div className="@container">
  <div className="flex flex-col @sm:flex-row items-center gap-4">
    <div className="text-sm @md:text-xl font-heading">Self-Aware Adaptive Widget</div>
  </div>
</div>
```

For complete Subgrid, `@container`, and `@property` implementations, see [`references/css-subgrid-and-container-queries.md`](references/css-subgrid-and-container-queries.md).

---

## 3. The 21st.dev Component Ecosystem

Leverage modern, copy-paste / CLI component suites that build on shadcn/ui and Tailwind standards:

| Library / Suite | Specialization | Quick Install / Setup | Implementation Strategy |
|---|---|---|---|
| **BKLit UI** (`ui.bklit.com`) | Composable Charts & Data Viz | `npx shadcn@latest add @bklit/[chart]` | Use composable primitives (`Grid`, `XAxis`, `ChartTooltip`, `AreaChart`). Theme dynamically with CSS variables (`chartCssVars`). |
| **Kokonut UI** (`kokonutui.com`) | Creative UI, AI Inputs & Micro-cards | `npx shadcn@latest add [component]` | Copy-paste interactive buttons, prompt inputs, and animated cards with Tailwind and Motion. |
| **Origin UI** (`originui.com`) | Production-grade shadcn expansion | Browse on `originui.com` $\rightarrow$ copy code | 500+ accessible form controls, complex multi-selects, sliders, and navigation tables. |
| **Cult UI** (`cult-ui.com`) | Expressive & animated components | Copy-paste from `cult-ui.com` | Rich motion components designed to elevate standard shadcn layouts. |
| **Animata** (`animate-ui.com`) | Interaction-first micro-blocks | Copy-paste from `animate-ui.com` | Micro-interactions, hover reveals, and engaging entry animations. |
| **Fancy Components** (`fancycomponents.dev`) | Whimsical, physics & variable font UI | Copy-paste from `fancycomponents.dev` | Stacking cards, magnetic physics, and kinetic text animations. |
| **21st.dev Registry** (`21st.dev`) | Universal shadcn component hub | Search on `21st.dev` $\rightarrow$ CLI / Copy | Universal index for discovering vetted community components. |

For detailed component recipes, see [`references/creative-components-ecosystem.md`](references/creative-components-ecosystem.md).

---

## 4. Micro-Interactions, Kinetics & Visual Haptics

Elevate interfaces with sub-pixel micro-interactions that respond intuitively to user intent:
*   **Magnetic Cursor Tracking:** Interpolate the delta between cursor coordinates and element center to smoothly pull interactive buttons toward the pointer.
*   **Kinetic Variable Typography:** Transition variable font axes (`wght`, `wdth`, `slnt`) on hover or scroll.
*   **Border Beam Tracing:** Animate gradient beams along component perimeters using CSS `@property`.

For complete TSX/CSS implementation code, see [`references/micro-interactions-and-tactile-code.md`](references/micro-interactions-and-tactile-code.md).

---

## 5. Verification & Code Quality Gates

Before completing a design engineering implementation:
- [ ] **Motion Performance:** Animations run exclusively on `transform` and `opacity` (WAAPI accelerated).
- [ ] **Layout Stability:** Subgrid and Container Queries eliminate layout shifts (zero CLS).
- [ ] **Exit Integrity:** All conditional animating components utilize `<AnimatePresence>` with stable keys.
- [ ] **Accessibility (WCAG AA):** Respect `useReducedMotion()` for users with vestibular sensitivities.
- [ ] **Bundle Check:** Heavy animations leverage `<LazyMotion>` with `domAnimation`.
