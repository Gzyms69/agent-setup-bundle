# Color Theory (OKLCH & Albers) & Tactile Depth Systems

This reference document provides mathematical rules for constructing chromatic palettes using the OKLCH color model, enforcing APCA contrast standards, and engineering physical tactile depth in digital interfaces.

---

## 1. OKLCH Color Space & Chromatic Harmony

### Why OKLCH Replaces HSL & RGB:
*   **Perceptual Uniformity:** In HSL, pure blue (`hsl(240, 100%, 50%)`) appears far darker to human eyes than pure yellow (`hsl(60, 100%, 50%)`), despite having the same 50% lightness value. OKLCH fixes this: $L = 0.70$ has the EXACT same perceived brightness across every hue.
*   **No Muddy RGB Interpolation:** Transitions between colors across the color wheel avoid the desaturated gray dead zones typical of sRGB.

### OKLCH Coordinate Definition:
$$\text{oklch}(L \quad C \quad H)$$
*   **$L$ (Perceived Lightness):** $0.0$ (pitch black) to $1.0$ (pure white).
*   **$C$ (Chroma / Saturation):** $0.0$ (grayscale neutral) to $\sim 0.37$ (maximum vivid display-P3 color).
*   **$H$ (Hue Angle):** $0^{\circ}$ to $360^{\circ}$ (Color wheel angle: $0^{\circ}$ Pink/Red, $90^{\circ}$ Yellow, $145^{\circ}$ Green, $250^{\circ}$ Blue, $300^{\circ}$ Purple).

### Chromatic Harmony Formulas:
```css
:root {
  /* Dark Surface Foundation */
  --surface-base: oklch(0.12 0.008 260); /* Polar Abyss Dark */
  --surface-card: oklch(0.16 0.012 260); /* Elevated Dark Surface */
  --surface-border: oklch(0.25 0.015 260); /* Subtle Border Contrast */

  /* Text Levels */
  --text-primary: oklch(0.96 0.005 260); /* Crisp High-Contrast White */
  --text-muted: oklch(0.70 0.015 260); /* Legible Secondary Gray */

  /* Brand Accents (Calculated by Hue Shifting with Constant Lightness) */
  --brand-primary: oklch(0.65 0.22 260); /* Electric Sapphire */
  --brand-complementary: oklch(0.70 0.18 80); /* Warm Golden Amber */
  --brand-success: oklch(0.72 0.19 145); /* Emerald Signal */
  --brand-danger: oklch(0.65 0.24 25); /* Crimson Alert */
}
```

---

## 2. Tactile Depth, Ambient Light & Surface Physics

Eliminate flat, sterile digital planes by applying physical optics:

### 1. 1px Inset Light Reflection (Physical Edge Bevel):
Simulate an overhead light bouncing off the chamfered edge of a physical glass/aluminum card:
```css
.card-tactile {
  background: var(--surface-card);
  border: 1px solid var(--surface-border);
  box-shadow:
    inset 0 1px 0 0 rgba(255, 255, 255, 0.12),
    0 10px 30px -10px rgba(0, 0, 0, 0.6);
}
```

### 2. Procedural SVG Noise / Grain Overlay:
Adds microscopic tactile texture that removes color banding on OLED screens:
```html
<!-- Inline SVG Filter -->
<svg class="pointer-events-none fixed inset-0 z-50 h-full w-full opacity-[0.025] mix-blend-overlay">
  <filter id="noiseFilter">
    <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch" />
  </filter>
  <rect width="100%" height="100%" filter="url(#noiseFilter)" />
</svg>
```

### 3. Ambient Glow & Border Beam Tracing:
```css
/* Animated Ambient Border Beam */
@property --beam-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.border-beam {
  --beam-angle: 0deg;
  border: 1px solid transparent;
  background:
    linear-gradient(var(--surface-card), var(--surface-card)) padding-box,
    conic-gradient(from var(--beam-angle), transparent 70%, var(--brand-primary) 95%, transparent 100%) border-box;
  animation: rotateBeam 4s linear infinite;
}

@keyframes rotateBeam {
  to {
    --beam-angle: 360deg;
  }
}
```
