---
name: skill-graphics-webgl
description: Specialized guidance for 2D/3D graphics, Three.js, and WebGL performance optimization. Use when Gemini CLI needs to build immersive scenes, optimize rendering pipelines, or handle complex SVG/Canvas animations.
---

# Graphics & WebGL Optimization Skill

This skill provides expert patterns for high-performance visual rendering on the web.

## 1. 3D Graphics (Three.js)
*   **Core Stack:** **Three.js** + **react-three-fiber**.
*   **Stability:** Use `translateZ` within `preserve-3d` contexts for depth hierarchy.
*   **Performance:** Decouple mouse/touch events from elements undergoing heavy 3D transformations. Use a static 2D "Anchor" element to capture input.

## 2. WebGL Performance Mandates
*   **Reflow Protection:** Never call `getBoundingClientRect()` or `offsetWidth` inside `mousemove` or `scroll` handlers. Cache dimensions in a `useRef`.
*   **Interaction-Driven Loading:** Load heavy bundles (>100KB, e.g., Three.js) ONLY after user interaction (scroll/move) or via `requestIdleCallback`.
*   **Compositor Efficiency:** Animations must avoid layout-triggering properties (`top`, `margin`, `width`). Use exclusively `transform` and `opacity`.

## 3. 2D Graphics & Data Viz
*   **Modern Charts:** Use **BKLit UI** (`@bklit/*` on shadcn/ui) for composable, CSS-variable-themed dashboard charts and telemetry widgets.
*   **Custom Data Viz:** Use **SVG + D3.js** for custom resolution-independent mathematical transformations.
*   **Dynamic Scenes:** Use **HTML Canvas API** for high-object-count scenes.
*   **Games:** Use **PixiJS** for WebGL-accelerated 2D sprites and particle effects.

## 4. Animation & 3D Sync Hygiene
*   **Source of Truth:** Never mix CSS transitions (`transition: all`) with JS physics engines (Motion).
*   **MotionValues Sync:** Bridge UI pointer events to WebGL/Three.js render loops by subscribing to `MotionValues` (`useMotionValue`, `useSpring`) rather than triggering React component re-renders.
*   **SVG Containers:** Never animate SVG primitives directly. Wrap moving parts in `<motion.g>` or `<motion.path pathLength={...} />` to prevent transform conflicts.
*   **Origin Locking:** Explicitly set `transformOrigin` in pixels for SVG scale/rotate animations to ensure cross-browser consistency.
