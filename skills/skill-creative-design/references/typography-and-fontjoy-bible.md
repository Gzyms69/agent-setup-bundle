# Typography Bible & Fontjoy Vector Pairing System

This reference document outlines the rules of typographic craftsmanship, modular type scales, micro-typography, and neural font pairing inspired by Robert Bringhurst and the Fontjoy deep learning model.

---

## 1. The Bringhurst Typographic Canon (*The Elements of Typographic Style*)

1.  **Honor Content:** Typography exists to honor, clarify, and elevate the written word. Never distort type to fit an arbitrary layout box.
2.  **The Measure (Line Length):**
    *   *Optimal:* 45 to 75 characters per line (approx. 66 characters including spaces).
    *   *Mobile Measure:* 35 to 45 characters.
    *   *Short measures (<35 chars):* Cause erratic eye jumping; *Long measures (>85 chars):* Cause reader fatigue and line doubling errors.
3.  **Vertical Rhythm & Leading (Line-Height):**
    *   *Display / Headings:* $1.05\times - 1.15\times$ (tight leading to prevent sprawling).
    *   *Body Text:* $1.4\times - 1.6\times$ (open leading for optical comfort).
    *   *Monospace / Code:* $1.5\times - 1.7\times$.
4.  **Micro-Typography:**
    *   Use true typographical quotation marks (`“` `”`) instead of straight typewriter quotes (`"` `"`).
    *   Use em-dashes (`—`) or en-dashes (`–`) with spaces for parenthetical thoughts; never double hyphens (`--`).
    *   Apply hanging punctuation for blockquotes and list bullets so the left vertical margin stays razor-sharp.

---

## 2. Fontjoy Vector Embedding & Contrast Theory

Fontjoy utilizes deep neural networks to project typefaces into a high-dimensional feature space based on weight, width, stroke modulation, and x-height.

### The Contrast vs Harmony Slider:
*   **High Contrast (Distance > 0.7):** Pairings with dramatic stylistic tension (e.g. Renaissance Serif with Geometric Sans). Best for editorial, luxury, and high-impact storytelling.
*   **Moderate Contrast (Distance 0.4 – 0.6):** Balanced pairings sharing common proportions but differing in classification. Best for modern SaaS, productivity apps, and documentation.
*   **Low Contrast / Single Superfamily (Distance < 0.3):** Using a versatile superfamily (e.g., `Geist Sans` + `Geist Mono`, or `Inter` + `Inter Tight`). Best for ultra-clean developer tools and data-dense dashboards.

### Curated Production Font Pairings (Google Fonts / Modern Web):

| Archetype / Mood | Headline Font (`--font-heading`) | Body Font (`--font-body`) | Metadata Font (`--font-mono`) |
|---|---|---|---|
| **Editorial Prestige** | `Newsreader` / `Instrument Serif` | `Geist Sans` / `Inter` | `Geist Mono` |
| **High-Tech Modernism** | `Space Grotesk` / `Syne` | `Plus Jakarta Sans` | `JetBrains Mono` |
| **Swiss Rationalism** | `Inter` / `Helvetica Now` | `Inter` | `Roboto Mono` |
| **Industrial / Hardware** | `Cabinet Grotesk` / `Chivo` | `DM Sans` | `Space Mono` |
| **Mindful / Warm Editorial** | `Fraunces` / `Lora` | `Outfit` / `Satoshi` | `Fira Code` |
| **Brutalist Impact** | `Anton` / `Clash Display` | `Space Grotesk` | `JetBrains Mono` |

---

## 3. Modular Scales & Fluid Typography (`clamp()`)

### Classical Modular Scale Ratios:
*   **Minor Third ($1.200$):** Compact, subtle scale for data-dense dashboards and mobile-first tools.
*   **Major Third ($1.250$):** Standard balanced scale for general SaaS and web applications.
*   **Perfect Fourth ($1.333$):** Dynamic, clear hierarchy for marketing and documentation.
*   **Golden Ratio ($1.618$):** High-drama, monumental scale for luxury and hero showcases.

### Fluid CSS Typography Formula:
```css
:root {
  /* Fluid Scale calculated from 375px mobile viewport to 1440px desktop */
  --text-xs: clamp(0.75rem, 0.15vw + 0.7rem, 0.875rem);
  --text-sm: clamp(0.875rem, 0.25vw + 0.8rem, 1rem);
  --text-base: clamp(1rem, 0.35vw + 0.9rem, 1.125rem);
  --text-lg: clamp(1.25rem, 0.6vw + 1.1rem, 1.5rem);
  --text-xl: clamp(1.5rem, 1vw + 1.25rem, 2rem);
  --text-2xl: clamp(2rem, 1.8vw + 1.5rem, 3rem);
  --text-display: clamp(2.75rem, 4vw + 1.5rem, 5.5rem);
}
```
