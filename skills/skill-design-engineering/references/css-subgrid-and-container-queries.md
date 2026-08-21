# CSS Subgrid & Container Queries Engineering Guide

This reference document provides technical patterns for building mathematically aligned Bento Grids and portable, self-aware UI components using native modern CSS features.

---

## 1. CSS Subgrid Architecture (Solving the Misaligned Card Problem)

### The Problem in Traditional Grids:
In standard CSS Grid or Flexbox, each card manages its own internal content height independently. When card titles have differing lengths (1 line vs 3 lines), the card bodies and action footers become misaligned, breaking horizontal rhythm.

### The Subgrid Solution:
By applying `grid-template-rows: subgrid`, child elements within card tiles directly participate in the parent grid's row tracks:

```html
<!-- Parent 3-Column Bento Grid -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 p-6">

  <!-- Card 1 (Spans 3 Rows of Subgrid) -->
  <article class="grid grid-rows-subgrid row-span-3 p-6 rounded-2xl bg-neutral-900 border border-white/10">
    <!-- Row 1: Header / Category -->
    <span class="text-xs font-mono uppercase text-neutral-400">Telemetry</span>
    
    <!-- Row 2: Title & Description (Height automatically equalized across all cards) -->
    <div class="py-2">
      <h3 class="text-xl font-semibold text-white">Compact Title</h3>
      <p class="text-sm text-neutral-400 mt-1">Short subtitle.</p>
    </div>
    
    <!-- Row 3: Footer Button (Perfect horizontal baseline across all 3 cards) -->
    <footer class="pt-4 border-t border-white/10 flex justify-between items-center">
      <span class="text-xs text-neutral-500">Live</span>
      <button class="text-xs text-white font-medium hover:underline">View</button>
    </footer>
  </article>

  <!-- Card 2 (With Long Title - Automatically expands Row 2 for Card 1 & Card 3 as well) -->
  <article class="grid grid-rows-subgrid row-span-3 p-6 rounded-2xl bg-neutral-900 border border-white/10">
    <span class="text-xs font-mono uppercase text-neutral-400">Security</span>
    <div class="py-2">
      <h3 class="text-xl font-semibold text-white">Complex Multi-Line Heading That Wraps Into Three Full Lines</h3>
      <p class="text-sm text-neutral-400 mt-1">Expanded subtitle explaining architecture.</p>
    </div>
    <footer class="pt-4 border-t border-white/10 flex justify-between items-center">
      <span class="text-xs text-neutral-500">Verified</span>
      <button class="text-xs text-white font-medium hover:underline">Audit</button>
    </footer>
  </article>

</div>
```

---

## 2. Container Queries (`@container`)

Container Queries allow individual components to adapt based on the size of the slot they occupy, rather than the entire browser viewport.

### Implementation Pattern:
```html
<!-- Wrapper declares itself as a container -->
<div class="@container/card col-span-1 md:col-span-2">
  <div class="flex flex-col @sm/card:flex-row items-start @sm/card:items-center justify-between p-6 bg-neutral-900 rounded-2xl">
    <div>
      <h4 class="text-base @md/card:text-2xl font-heading text-white">Adaptive Data Tile</h4>
      <p class="text-xs @md/card:text-sm text-neutral-400">Rearranges from vertical stack to horizontal strip when slot width > 400px.</p>
    </div>
    <button class="mt-4 @sm/card:mt-0 px-4 py-2 bg-white text-black rounded-lg text-sm font-medium">
      Action
    </button>
  </div>
</div>
```

### Container Query Units:
*   `cqw`: $1\%$ of query container width.
*   `cqh`: $1\%$ of query container height.
*   `cqmin`: Smaller value of `cqw` or `cqh`.
