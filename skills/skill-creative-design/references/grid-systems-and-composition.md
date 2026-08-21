# Grid Systems, Composition Math & Layout Archetypes

This reference document provides mathematical formulas, spatial rules, and architectural patterns for constructing high-end digital layouts.

---

## 1. Classical Grid Mathematics (Josef Müller-Brockmann)

### Column & Field Equations:
A harmonious grid divides the total viewport width $W$ into $n$ columns of width $c$, separated by gutters $g$, with side margins $m$:
$$W = 2m + n \cdot c + (n - 1)g$$

### Harmonic Proportions & The Golden Section ($\Phi$):
*   **Golden Ratio ($\Phi \approx 1.618$):** The ratio of primary content width to sidebar width should approximate $1.618 : 1$ (e.g. $62\%$ main canvas, $38\%$ supporting panel).
*   **Fibonacci Sequence Spacing (8-point scale):** Use spacing tokens derived from Fibonacci growth: $8\text{px}, 16\text{px}, 24\text{px}, 40\text{px}, 64\text{px}, 104\text{px}$.

---

## 2. Bento Grid Architecture (Modular Asymmetric Tiles)

The Bento Grid (inspired by Japanese bento boxes and perfected by Apple/Linear) organizes diverse functional units into a unified, balanced tapestry.

```
┌────────────────────────────────────────────────────────┬───────────────────────────┐
│                                                        │   SECONDARY MODULE (1x1)  │
│                                                        ├───────────────────────────┤
│                PRIMARY ANCHOR TILE (2x2)               │   SECONDARY MODULE (1x1)  │
│           (Hero Metric / Interactive Graph)            ├───────────────────────────┤
│                                                        │   TERTIARY MODULE (1x1)   │
├───────────────────────────┬────────────────────────────┴───────────────────────────┤
│    ACTION MODULE (1x1)    │              WIDE TELEMETRY STRIP (2x1)                │
└───────────────────────────┴────────────────────────────────────────────────────────┘
```

### Strategic Bento Composition Rules:
1.  **Anchor Tile Priority:** Every bento grid MUST have exactly ONE prominent anchor tile ($2\times2$ or $2\times1$) that occupies $40-50\%$ of the visual weight.
2.  **Visual Density Variation:** Alternate between high-density data tiles (charts, live telemetry) and low-density breathing tiles (minimalist typography, single bold stat).
3.  **Reflow Geometry:** On mobile viewports ($<768\text{px}$), the grid collapses to a single vertical column ($1\times1$), with the anchor tile leading the reading hierarchy.

---

## 3. Swiss International Asymmetric Grid

Instead of centered, predictable layouts, the Swiss grid relies on off-center tension and mathematical column spans:

*   **The 12-Column Split Formula:**
    *   *Columns 1–4:* Massive display headline and category kicker (fixed or sticky anchor).
    *   *Column 5:* Active negative space (gutter breathing lane).
    *   *Columns 6–11:* Multi-paragraph body text with micro-typographic accents.
    *   *Column 12:* Monospaced metadata rail (dates, authors, tags, live telemetry).

---

## 4. Editorial Split View (The Magazine Archetype)

Ideal for storytelling landing pages, product announcements, and case studies:

```
┌──────────────────────────────────────────┬──────────────────────────────────────────┐
│           STICKY VIEWPORT (50%)          │          SCROLLING NARRATIVE (50%)       │
│                                          │                                          │
│   • Fixed 3D canvas / Video / Artwork    │   • Story Section 1: The Origin          │
│   • Synchronized to scroll progress      │   • Story Section 2: Technical Leap      │
│   • Stays fixed in viewport during scroll│   • Story Section 3: Metric Proof        │
│                                          │   • Story Section 4: Call to Action      │
└──────────────────────────────────────────┴──────────────────────────────────────────┘
```

---

## 5. Full-Bleed vs Constrained Content Breakouts

Construct layout sections where backgrounds flow to the screen edges while text and media align with mathematical precision:

```css
/* CSS Full-Bleed Breakout Grid */
.breakout-grid {
  display: grid;
  grid-template-columns:
    [full-start] minmax(1.5rem, 1fr)
    [content-start] min(100% - 3rem, 1200px) [content-end]
    minmax(1.5rem, 1fr) [full-end];
}

.content-constrained {
  grid-column: content;
}

.content-full-bleed {
  grid-column: full;
}
```
