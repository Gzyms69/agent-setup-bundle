---
name: skill-web-performance
description: Universal web performance engineering, Core Web Vitals optimization (LCP, INP, CLS, TBT, TTFB), Lighthouse 100/100 audits, runtime tracing via MCP, asset pipelines, and zero-shift rendering. Use when asked to optimize website performance, improve page speed, fix Core Web Vitals, reduce bundle size, eliminate layout shifts, or conduct performance audits.
---

# Web Performance & Core Web Vitals Engineering Skill

This skill provides comprehensive, battle-tested architectural guidelines and an autonomous agentic optimization workflow to achieve elite performance scores (**Lighthouse 100/100**, **Core Web Vitals "Good" at 75th percentile**) across modern web platforms (Next.js, Astro, Vite/React, SvelteKit, Vanilla Web).

---

## 1. Core Web Vitals & Performance Budgets (2026 Standards)

Every production web application must meet or exceed these thresholds measured on **Mid-Tier Mobile (Slow 4G + 4x CPU Throttling)** and **Desktop Broadband**:

| Metric | Full Name | Focus Area | Elite Target | Good (Pass) | Needs Improvement | Poor |
|---|---|---|---|---|---|---|
| **LCP** | Largest Contentful Paint | Loading Speed | **≤ 1.2s** | **≤ 2.5s** | 2.5s – 4.0s | > 4.0s |
| **INP** | Interaction to Next Paint | Responsiveness | **≤ 50ms** | **≤ 200ms** | 200ms – 500ms | > 500ms |
| **CLS** | Cumulative Layout Shift | Visual Stability | **0.000** | **≤ 0.10** | 0.10 – 0.25 | > 0.25 |
| **TBT** | Total Blocking Time | Main Thread Load | **≤ 50ms** | **≤ 200ms** | 200ms – 600ms | > 600ms |
| **TTFB** | Time to First Byte | Backend & Edge | **≤ 150ms** | **≤ 800ms** | 800ms – 1800ms | > 1800ms |
| **FCP** | First Contentful Paint | Perceived Speed | **≤ 0.8s** | **≤ 1.8s** | 1.8s – 3.0s | > 3.0s |

### Hard Resource Budgets (Initial Page Load)
- **Compressed JavaScript (Gzip/Brotli):** ≤ 150 KB (Hard limit: 300 KB).
- **Compressed CSS:** ≤ 30 KB (Hard limit: 100 KB).
- **Above-the-Fold Critical Assets (Images/Fonts):** ≤ 350 KB.
- **Total Initial Page Weight:** ≤ 1.2 MB.
- **Third-Party Script Weight:** ≤ 100 KB (Deferred or Web-Worker offloaded).

---

## 2. The 7 Pillars of High-Performance Web Engineering

### Pillar 1: Critical Rendering Path & Server Latency (TTFB)
1. **Edge CDN Delivery:** Cache HTML and immutable assets at the CDN edge (Cloudflare, Vercel Edge, Fastly).
2. **HTTP/2 & HTTP/3 Protocol:** Enforce multiplexed connections to eliminate connection handshake overhead.
3. **HTTP 103 Early Hints:** Emit `103 Early Hints` with `Link: </lcp.webp>; rel=preload; as=image` and critical styles while the origin server prepares the `200 OK` response.
4. **Preconnect Optimization:** Restrict `<link rel="preconnect">` strictly to the top 2-3 essential cross-origin domains (e.g. font CDNs or analytics endpoints). Always pair with `crossorigin` where needed.

```html
<!-- Critical Preconnects in <head> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

---

### Pillar 2: LCP Optimization (Largest Contentful Paint)
LCP is broken down into 4 distinct phases:
$$\text{Total LCP} = \text{TTFB} + \text{Resource Load Delay} + \text{Resource Load Duration} + \text{Element Render Delay}$$

1. **Eliminate Resource Load Delay (≤ 10% of LCP):**
   - Preload the LCP asset in `<head>` with `fetchpriority="high"`.
   - Never lazy-load the LCP element (never set `loading="lazy"` on above-fold hero images).
   - Ensure the LCP element exists in the raw server HTML payload (avoid client-side `useEffect` data fetching).
2. **Eliminate Resource Load Duration (≤ 40% of LCP):**
   - Format hierarchy: **AVIF** (preferred) → **WebP** → optimized SVG/PNG.
   - Use responsive `srcset` and accurate `sizes` so mobile devices download appropriately scaled images.
3. **Eliminate Element Render Delay (≤ 10% of LCP):**
   - Inline Critical Path CSS (< 14 KB) directly into `<head>`.
   - Defer non-critical stylesheets.
4. **Speculation Rules API (Zero LCP for Next Navigations):**
   - Prerender high-confidence navigation links on hover:

```html
<script type="speculationrules">
{
  "prerender": [{
    "where": { "href_matches": "/*" },
    "eagerness": "moderate"
  }]
}
</script>
```

---

### Pillar 3: INP & Main Thread Optimization (Interaction to Next Paint)
Total INP consists of: **Input Delay** + **Processing Duration** + **Presentation Delay**.

1. **Yielding to the Main Thread:**
   - Break long synchronous loops (> 50ms) into discrete chunks using `scheduler.yield()`:

```typescript
async function processBatchedTasks<T>(items: T[], processFn: (item: T) => void) {
  const CHUNK_SIZE = 50;
  for (let i = 0; i < items.length; i += CHUNK_SIZE) {
    const chunk = items.slice(i, i + CHUNK_SIZE);
    chunk.forEach(processFn);
    
    if ('scheduler' in window && 'yield' in (window as any).scheduler) {
      await (window as any).scheduler.yield();
    } else {
      await new Promise(resolve => setTimeout(resolve, 0));
    }
  }
}
```

2. **Web Worker Offloading:** Offload heavy computations, JSON parsing, crypto, and telemetry tracking off the UI thread via `Worker` or `Partytown`.
3. **Prevent Layout Thrashing:** Batch DOM reads (`element.offsetWidth`, `getBoundingClientRect()`) before performing DOM writes (`element.style.transform`).
4. **React Transitions:** Wrap non-urgent state updates in `React.startTransition()` or `useDeferredValue()`.

---

### Pillar 4: CLS (Cumulative Layout Shift) & Visual Stability
Target score: **0.000**. Layout shifts damage user trust and search rankings.

1. **Explicit Dimensions & Aspect Ratios:**
   - Every `<img>`, `<video>`, `<iframe>`, and `<canvas>` must define explicit `width`/`height` or CSS `aspect-ratio: width / height`.
2. **Zero-Shift Font Metric Overrides:**
   - When using custom web fonts with `font-display: swap`, configure `@font-face` metric descriptors on fallback fonts to match the exact x-height and ascent/descent of the web font:

```css
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  ascent-override: 90%;
  descent-override: 22.5%;
  line-gap-override: 0%;
  size-adjust: 107%;
}
```
   *(Or leverage Next.js `next/font/google` which injects these adjustments automatically).*
3. **Server-Cookie Layout State:**
   - For collapsible banners, announcement bars, or theme switches, read the state server-side from HTTP cookies before rendering the initial HTML to prevent client-side hydration layout popping.
4. **Reserved Dynamic Containers:**
   - Reserve space for dynamic content (advertisements, async data widgets) using CSS `min-height` and skeleton placeholding.

---

### Pillar 5: JavaScript & Bundle Architecture
1. **Dynamic Code Splitting:**
   - Route-based splitting (`next/dynamic`, `React.lazy`).
   - Component-based splitting for heavy modals, charts, and drawer drawers.
2. **Interaction-Gated Heavy Asset Loading:**
   - Heavy libraries (Three.js, WebGL shaders, Lucide heavy icon sets, Monaco/Tiptap editors, Google Maps) must **NOT** execute during initial hydration.
   - Attach initialization listeners to first user interaction (`pointerenter`, `scroll`, `touchstart`) or wrap in `requestIdleCallback`.
3. **Eliminate Barrel File Bloat:**
   - Avoid `import { Button } from '@/components'` if it pulls 50 unused components into the bundle.
   - Use direct subpath imports or ensure build bundler supports Turbopack/Tree-shaking with `"sideEffects": false`.
4. **Motion (motion.dev) & LazyMotion Architecture:**
   - In React animation projects, replace legacy heavyweight `framer-motion` imports with `motion/react`.
   - Wrap interactive trees in `<LazyMotion features={domAnimation} strict>` and use lightweight `<m.div>` primitives, saving ~50KB+ gzip bundle size.
   - For vanilla JS animations or ultra-lightweight micro-interactions, use `motion/mini` (~2.3KB native WAAPI engine).

---

### Pillar 6: Rendering Engine, Compositor & Animation Performance
1. **`content-visibility: auto`:**
   - Apply `content-visibility: auto` with `contain-intrinsic-size` to all below-the-fold content sections to allow the browser to skip rendering until scrolled into proximity:

```css
.section-below-fold {
  content-visibility: auto;
  contain-intrinsic-size: 0 600px;
}
```

2. **Off-Main-Thread WAAPI Animations:**
   - Continuous ambient animations (marquees, background pulse, glow rings) and Motion transitions must run on the browser **Compositor Thread** using CSS `@keyframes` or native **Web Animations API (WAAPI)** via Motion.
   - Never use JavaScript `requestAnimationFrame` loops for static background decorations or layout properties (`top`, `left`, `width`, `height`). Animate exclusively `transform` (`x`, `y`, `scale`, `rotate`) and `opacity`.
3. **GPU Layer Promotion & DPR Capping:**
   - Promote animating elements with `transform: translateZ(0)` or `will-change: transform`.
   - On canvas/WebGL scenes with heavy backdrop filters, cap `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5))` to protect mobile GPUs.

---

### Pillar 7: Caching, Assets, Fonts & Network Hygiene
1. **Font Loading & Subsetting (Fontjoy Optimization):**
   - Use `next/font/google` or self-hosted WOFF2 with `font-display: swap` and explicit `subsets: ['latin']`.
   - Preload primary headline and body variable fonts; defer decorative display or code fonts.
2. **Immutable Asset Caching:**
   - Static assets (`/_next/static/*`, `/assets/*`) with content hashes must have headers:
     `Cache-Control: public, max-age=31536000, immutable`.
3. **Video Streaming Optimization:**
   - Video previews must set `preload="metadata"` or `preload="none"`. Never use `preload="auto"` across lists of cards or templates.
4. **Modern Image Formats:**
   - Generate AVIF and WebP variants with quality 75-80 (indistinguishable from original, 50-70% file size reduction).

---

## 3. The 5-Phase Agentic Performance Loop

When conducting performance optimization on any codebase or URL, follow this deterministic cycle:

```
[Phase 1: Measure] ──► [Phase 2: Diagnose] ──► [Phase 3: Surgical Fix] ──► [Phase 4: Benchmark] ──► [Phase 5: Document]
        ▲                                                                           │
        └────────────────────────── If Scores < 100 ────────────────────────────────┘
```

### Phase 1: Baseline Measurement
1. **Synthetic Full Audit:**
   - Call `lighthouse-mcp` (or run `npx lighthouse <URL> --output=json --preset=desktop/mobile`) to capture standard scores across Performance, Accessibility, Best Practices, and SEO.
2. **Chromium Runtime Trace:**
   - Use `chrome-devtools` tool `performance_start_trace` to record real page load under 4x CPU Throttling and Slow 4G network.
   - Call `performance_analyze_insight` with `insightName: "LCPBreakdown"` and `insightName: "DocumentLatency"`.

### Phase 2: Root-Cause Diagnosis & Triage
1. Classify bottlenecks by metric:
   - **LCP:** Check hero image discovery, preload priority, CSS blocking time.
   - **INP/TBT:** Identify Long Tasks in flame chart (>50ms); locate synchronous JS execution.
   - **CLS:** Inspect layout shift clusters in trace; check missing dimensions or web font swapping.
   - **Bundle:** Inspect network waterfall and bundle analyzer output (`@next/bundle-analyzer` / `source-map-explorer`).

### Phase 3: Surgical Implementation
1. Apply targeted fixes from the 7 Pillars without deleting user features or compromising architecture.
2. Follow strict Single Source of Truth (SSOT) and zero-workaround protocol.

### Phase 4: Benchmarking & Iteration
1. Re-run `lighthouse-mcp` audit and `chrome-devtools` trace.
2. Compare before/after metrics against targets (LCP ≤ 1.2s, INP ≤ 50ms, CLS = 0.000).
3. If performance score < 100, repeat Phase 2 with specific remaining issues.

### Phase 5: Documentation & Memory Persistence
1. Record final metrics in project `MEMORY.md` or audit log.
2. Persist key architectural decisions and performance baselines to **MemPalace** via `mempalace_diary_write`.

---

## 4. MCP Tools Reference Matrix for Performance

| Task | Primary Tool | Secondary Tool / CLI |
|---|---|---|
| Synthetic Audit & Scores | `lighthouse-mcp` (`@danielsogl/lighthouse-mcp`) | `npx unlighthouse --site <url>` |
| Deep CPU Trace & Long Tasks | `chrome-devtools` (`performance_start_trace`) | Chrome DevTools Flamechart |
| LCP Breakdown Analysis | `chrome-devtools` (`performance_analyze_insight`) | PerformanceObserver API |
| Memory Leaks & Heap Size | `chrome-devtools` (`take_heapsnapshot`) | Heap Profiler |
| Network Waterfall & Payload | `chrome-devtools` (`list_network_requests`) | HAR analysis |
| E2E Multi-step User Interaction | `puppeteer` (`puppeteer_navigate`, `puppeteer_click`) | Playwright trace |
| Architecture & Knowledge Recall | `mempalace` (`mempalace_search`, `mempalace_kg_query`) | Local MEMORY.md |

---

## 5. Verification & QA Checklist

Before concluding any web performance task:
- [ ] **Lighthouse Mobile Score:** Performance ≥ 95 (Desktop: 100).
- [ ] **LCP:** Hero element renders in < 1.2s with `fetchpriority="high"` and AVIF/WebP.
- [ ] **INP:** Zero tasks exceeding 50ms on main thread; UI interactions feel instantaneous.
- [ ] **CLS:** Score is 0.000; all media has explicit dimensions and fonts use zero-shift fallbacks.
- [ ] **Bundle Size:** JS bundle meets budget (< 150KB gzip for critical path).
- [ ] **Compositor:** Continuous animations execute on compositor thread (WAAPI/CSS).
- [ ] **Lazy Hydration:** Heavy 3D/Canvas/widgets gated behind user interaction.
- [ ] **TypeScript Check:** `npx tsc --noEmit` passes without errors.
