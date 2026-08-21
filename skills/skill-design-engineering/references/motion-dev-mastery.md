# Motion Mastery Guide (motion.dev)

Complete technical reference and recipes for [Motion](https://motion.dev/) (formerly Framer Motion v12+) in React and JavaScript.

---

## 1. Installation & Imports

```bash
npm install motion
# or
pnpm add motion
```

```tsx
// React Standard
import { motion, AnimatePresence, useAnimate, useScroll, useTransform, useSpring, useInView, useReducedMotion } from "motion/react";

// Lightweight Bundle Optimization (~50KB+ savings)
import { LazyMotion, domAnimation, m } from "motion/react";

// Vanilla JS / Non-React (WAAPI Engine)
import { animate, scroll, inView, stagger, timeline } from "motion";
```

---

## 2. Shared Layout Transitions (`layout` & `layoutId`)

Enable magical FLIP morphing between sibling components:

```tsx
"use client";

import { useState } from "react";
import { motion } from "motion/react";

const NAV_ITEMS = [
  { id: "overview", label: "Overview" },
  { id: "analytics", label: "Analytics" },
  { id: "settings", label: "Settings" },
];

export function TabNav() {
  const [active, setActive] = useState("overview");

  return (
    <nav className="flex gap-1 p-1 bg-neutral-900 rounded-xl border border-white/10">
      {NAV_ITEMS.map((item) => (
        <button
          key={item.id}
          onClick={() => setActive(item.id)}
          className="relative px-4 py-2 text-sm font-medium transition-colors text-neutral-400 hover:text-white"
        >
          {active === item.id && (
            <motion.div
              layoutId="activeTabGlow"
              className="absolute inset-0 bg-white/10 rounded-lg shadow-sm border border-white/15"
              transition={{ type: "spring", stiffness: 450, damping: 35 }}
            />
          )}
          <span className="relative z-10">{item.label}</span>
        </button>
      ))}
    </nav>
  );
}
```

---

## 3. Exit Animations & PopLayout (`AnimatePresence`)

Prevent layout jumping when cards or list items are removed:

```tsx
"use client";

import { AnimatePresence, motion } from "motion/react";

export function NotificationList({ items, onDismiss }: { items: Array<{ id: string; text: string }>; onDismiss: (id: string) => void }) {
  return (
    <div className="flex flex-col gap-2">
      <AnimatePresence mode="popLayout">
        {items.map((item) => (
          <motion.div
            key={item.id}
            layout
            initial={{ opacity: 0, scale: 0.9, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.85, transition: { duration: 0.15 } }}
            className="flex items-center justify-between p-4 bg-neutral-900 border border-white/10 rounded-xl"
          >
            <span className="text-sm text-white">{item.text}</span>
            <button onClick={() => onDismiss(item.id)} className="text-xs text-neutral-400 hover:text-white">Dismiss</button>
          </motion.div>
        ))}
      </AnimatePresence>
    </div>
  );
}
```

---

## 4. Scroll-Driven & Scroll-Linked Animations

```tsx
"use client";

import { useRef } from "react";
import { motion, useScroll, useTransform, useSpring } from "motion/react";

export function ParallaxHero() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end start"],
  });

  const smoothProgress = useSpring(scrollYProgress, { stiffness: 100, damping: 30 });
  const y = useTransform(smoothProgress, [0, 1], ["0%", "40%"]);
  const opacity = useTransform(smoothProgress, [0, 0.8], [1, 0]);

  return (
    <div ref={containerRef} className="relative h-screen overflow-hidden">
      <motion.div style={{ y, opacity }} className="flex flex-col items-center justify-center h-full">
        <h1 className="text-6xl font-heading text-white">Motion at 120 FPS</h1>
      </motion.div>
    </div>
  );
}
```

---

## 5. Next.js 15+ App Router & Server Components Integration

*   **Boundary Isolation:** Never mark an entire page as `"use client"` just to add entrance animations. Keep `page.tsx` as a React Server Component (RSC), and encapsulate interactive/animated sections in small Client Component islands (`<AnimatedHero />`, `<FadeInView />`).
*   **Accessibility Guardrail:** Always wrap animations in `useReducedMotion()` checks:
    ```tsx
    const shouldReduceMotion = useReducedMotion();
    const transition = shouldReduceMotion ? { duration: 0 } : { type: "spring", stiffness: 300, damping: 25 };
    ```
