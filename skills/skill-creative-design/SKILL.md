---
name: skill-creative-design
description: Master Art Direction, Visual Philosophy, Aesthetics, Grid Systems, Fontjoy Typography Math, OKLCH Color Physics, and Spatial Composition. Use when establishing visual identity, choosing design philosophies (Swiss, Bauhaus, Wabi-Sabi, Industrial Tactical, Brutalism), composing asymmetric grids, calculating fluid typography, or elevating UI aesthetics beyond generic AI templates.
---

# Creative Design & Art Direction Skill (Design Bible)

This skill provides expert visual art direction, design philosophy, spatial composition systems, vector typography math (Fontjoy & Bringhurst), perceptual color theory (OKLCH & Albers), and tactile depth layering for world-class digital experiences.

---

## 1. Grand Philosophies & Art Movements in Digital Design

Before placing a single pixel or selecting a color token, establish the project's **Aesthetic North Star**. Draw from timeless design movements rather than transient AI clichés:

| Design Movement / Philosophy | Core Principles & Masters | Digital UI Characteristics | Ideal Use Cases |
|---|---|---|---|
| **Swiss International Typographic Style** | Josef Müller-Brockmann, Emil Ruder, Armin Hofmann. "Clarity, objectivity, and universal order." | Rigid mathematical modular grids, sans-serif typography, asymmetric compositional tension, active negative space (*white space*), objective visual hierarchy. | High-density developer tools, documentation portals, financial analytics, modern SaaS platforms. |
| **Bauhaus Functionalism** | Walter Gropius, Herbert Bayer, László Moholy-Nagy. "Form follows function." | Reduction to primary geometric primitives (circle, square, triangle), stark visual clarity, elimination of superfluous ornament, structural honesty. | Design tools, structural productivity software, technical utility engines. |
| **Good Design Principles** | Dieter Rams (*Weniger, aber besser* – "Less, but better"). | Unobtrusive, honest, long-lasting, thorough down to the last detail, environmentally and cognitively minimal. | Consumer hardware web apps, quiet software, audio/music software, distraction-free writing tools. |
| **Japanese Negative Space & Tactility** | Kenya Hara (*White* / *Designing Design*), Wabi-Sabi, *Ma* (Pustka). | Sensory receptivity, paper-like matte textures, asymmetric balance, organic imperfections, quiet luxury, intentional breathing room. | Luxury lifestyle, editorial publishing, bespoke portfolio experiences, mindful productivity. |
| **Industrial Tactical / Teenage Engineering** | Dieter Rams (Braun) $\times$ Teenage Engineering. | Mechanical precision, rotary encoders, tactile toggles, high information density, monochromatic base with single fluorescent accent (safety orange, lime). | Audio workstations, hardware configuration dashboards, developer consoles, terminal UIs. |
| **Brutalism & Neo-Brutalism** | Architectural Brutalism $\times$ Web Digital Rebellion. | Exposed layout anatomy, raw HTML aesthetics, bold black borders (2–3px), hard unblurred shadows (`box-shadow: 4px 4px 0px #000`), vibrant clashes. | Creative agencies, indie developer apps, fashion/culture magazines, gaming hubs. |
| **Spatial, Ray-Traced & Ambient Depth** | Modern Optical Physics & Ambient Lighting. | Perceptual depth elevation, 1px inner ambient light reflection highlights, dynamic caustics, multi-layer backdrop refraction, SVG noise/grain overlays. | Dark-mode hero showcases, high-end landing pages, product marketing experiences. |

For complete philosophical breakdowns and historical rules, see [`references/design-philosophies-and-movements.md`](references/design-philosophies-and-movements.md).

---

## 2. Spatial Composition & Grid Systems (Müller-Brockmann Math)

Layout is not a container; it is an organized field of tension, balance, and rhythm.

### Grid Construction Rules:
*   **The Modular Grid Field:** Divide the canvas into vertical columns (12 or 16), horizontal modules, and baseline grid units (typically 8px or 4px sub-grid).
*   **Harmonic Margins:** Margins must never be arbitrary. Follow the golden section ($\Phi \approx 1.618$) or classical proportions where side margins provide breathing boundaries that focus the eye toward the content center.
*   **Bento Grid Architecture:**
    *   *Anchor Tile (Hero 2x2 or 2x1):* Houses the primary focal point and telemetry/interactive visualization.
    *   *Secondary Modules (1x2 / 1x1):* House supporting features, data pills, and quick micro-actions.
    *   *Visual Weight Distribution:** Distribute dense interactive modules symmetrically across an asymmetric grid to maintain dynamic visual equilibrium.
*   **Gestalt Laws of Visual Perception:**
    *   *Law of Proximity:* Elements belonging together must share tighter spacing than distinct sections.
    *   *Law of Common Region:* Group related data points using distinct, subtle background surfaces rather than loud colored boxes.
    *   *Figure/Ground Segregation:* Maintain a minimum 3-layer depth hierarchy (Canvas Layer 0 $\rightarrow$ Card Layer 1 $\rightarrow$ Interactive Floating Layer 2).

For exhaustive layout formulas (Swiss Grid, Bento, Editorial Split, Full-Bleed Breakout), see [`references/grid-systems-and-composition.md`](references/grid-systems-and-composition.md).

---

## 3. Typography Mastery & Fontjoy Vector Pairing System

Typography is the voice and posture of digital communication. Adhere to the Bringhurst canon and Fontjoy neural pairing geometry.

### The 3-Tier Font Role Architecture:
1.  `--font-heading` (**Display / Primary Voice**): Conveys the identity, brand posture, and emotional weight of the project.
2.  `--font-body` (**Workhorse Text**): Engineered for maximum legibility at small optical sizes ($14\text{px}-18\text{px}$), neutral stroke contrast, and open counters.
3.  `--font-mono` (**Technical & Metadata Anchor**): Monospace typeface for metrics, code, timestamps, status badges, and telemetry numbers.

### Fontjoy Vector Contrast Pairing Formulas:
*   **Formula 1: Editorial High-Contrast (Authority + Modernity):**
    *   *Heading:* High-contrast Renaissance or Transitional Serif (`Newsreader`, `Instrument Serif`, `Playfair`).
    *   *Body:* Neutral Neo-Grotesque Sans (`Geist Sans`, `Inter`, `Helvetica Now`).
    *   *Metadata:* Dense Monospace (`Geist Mono`, `JetBrains Mono`).
*   **Formula 2: Modernist Minimalist (Geometry + Humanism):**
    *   *Heading:* Expressive Geometric Sans (`Space Grotesk`, `Syne`, `Cabinet Grotesk`).
    *   *Body:* Open Humanist Sans (`Plus Jakarta Sans`, `DM Sans`, `Outfit`).
*   **Formula 3: Industrial / Tactical Developer (Precision + Function):**
    *   *Heading & Body:* Clean Neo-Grotesque with tight tracking (`Geist`, `Söhne`, `Inter`).
    *   *Accents & Badges:* High-contrast Monospace with slashed zeros and distinct glyphs.

### Bringhurst Micro-Typographic Commandments:
*   **The Measure (Line Length):** Never allow body text to exceed 45 to 75 characters per line (optimal reading ergonomics: ~66 characters).
*   **Vertical Rhythm & Leading:** Set line-height to $1.4\times - 1.6\times$ for body text; tighten headings to $1.05\times - 1.15\times$ to avoid loose, floating words.
*   **Fluid Typography Scale:** Scale type continuously using mathematical `clamp()` instead of abrupt breakpoint jumps:
    ```css
    --text-display: clamp(2.75rem, 5vw + 1rem, 5.5rem);
    --text-h1: clamp(2rem, 3.5vw + 0.5rem, 3.75rem);
    --text-body: clamp(1rem, 0.5vw + 0.875rem, 1.125rem);
    ```

For full typographic formulas and Google Font pairing tables, see [`references/typography-and-fontjoy-bible.md`](references/typography-and-fontjoy-bible.md).

---

## 4. Perceptual Color Physics (OKLCH) & Tactile Depth Systems

Modern digital design must replace muddy RGB/HSL interpolation with perceptually uniform color spaces and physical light interaction.

### OKLCH Chromatic Architecture:
*   **Lightness ($L$):** Perceived brightness ($0\%$ to $100\%$) remains uniform across all hues, guaranteeing consistent WCAG/APCA contrast ratios.
*   **Chroma ($C$):** Saturation/Purity ($0$ to $\sim 0.37$). Keep background neutrals at $C < 0.015$ for deep, rich dark tones without muddy brown/gray tinting.
*   **Hue ($H$):** Angle ($0^{\circ}$ to $360^{\circ}$). Generate complementary and triadic accents mathematically:
    ```css
    :root {
      --brand-base: oklch(0.65 0.22 260); /* Electric Indigo */
      --brand-accent: oklch(0.75 0.18 55); /* Warm Amber Accent (Complementary) */
      --surface-dark: oklch(0.12 0.008 260); /* Rich Polar Dark */
    }
    ```

### Tactile Depth & Ambient Light Layering:
1.  **1px Inset Light Reflection (Physical Edge Highlight):**
    Give dark-mode cards physical presence with a 1px top highlight simulating an overhead light source:
    ```css
    box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.12),
                0 4px 20px -2px rgba(0, 0, 0, 0.5);
    ```
2.  **Procedural SVG Noise / Grain Overlay:**
    Eliminate cold, flat digital plastic surfaces by layering subtle SVG turbulence ($2-4\%$ opacity) with `mix-blend-mode: overlay` to give backgrounds tactile paper/aluminum texture.
3.  **Color-Bled Dynamic Shadows:**
    Never use pure black shadows on colored backgrounds. Mix 10–20% of the brand hue into the shadow spread.

For complete color palettes and CSS depth recipes, see [`references/color-and-depth-systems.md`](references/color-and-depth-systems.md).

---

## 5. Eradicating the "AI Aesthetic" (Zero-Tolerance Guardrails)

| Cliché AI Default | Why It Destroys Quality | Master Art Direction Solution |
|---|---|---|
| Fake pulsing green dots (`animate-pulse`) | Shouts "cheap automated template". Creates artificial status noise. | **TOTAL BAN** on fake status dots. Use clean typography or honest telemetry. |
| Purple/Indigo gradient background soup | Makes every tech website look identical. | Use custom OKLCH brand palettes, raw monochromatic bases, or rich ambient lighting. |
| Unconstrained rounding (`rounded-3xl` everywhere) | Childish, unrefined visual scale. | Match corner radius to the component scale in the design system (`rounded-md` / `rounded-xl`). |
| Centered floating hero cards with zero narrative | Disconnects the user from real product value. | Editorial split view, asymmetric hero typography, or interactive sandbox viewports. |
| Cliché buzzwords ("Unleash", "Elevate", "Seamlessly") | Generic marketing filler. | Precise, factual, and direct technical value propositions. |

---

## 6. Verification & Art Direction Review Checklist

Before approving any UI design concept, verify:
- [ ] **Design North Star:** Distinct design philosophy explicitly chosen (Swiss, Bauhaus, Rams, Wabi-Sabi, Tactical, Brutalist, Ambient Depth).
- [ ] **Anti-AI Guardrail:** Clean of fake pulsing dots, purple clichés, and generic floating cards.
- [ ] **Typographic Rhythm:** Font hierarchy respects the 3-tier architecture with Bringhurst measure ($45-75$ chars) and fluid `clamp()` scale.
- [ ] **Grid Math:** Modular grid or Bento layout anchored by a clear primary focal point.
- [ ] **Perceptual Contrast:** Colors defined in OKLCH or validated against APCA / WCAG 2.1/2.2 AA.
- [ ] **Tactile Depth:** 1px inner edge highlights, subtle grain/noise, and purposeful layer hierarchy applied.
