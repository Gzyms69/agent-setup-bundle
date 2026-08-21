# 21st.dev Component Ecosystem Integration Guide

This reference document provides concrete code patterns and setup recipes for top-tier creative component libraries indexed on [21st.dev](https://21st.dev/) and compatible with shadcn/ui.

---

## 1. BKLit UI ([ui.bklit.com](https://ui.bklit.com/)) – Composable Charts & Data Viz

BKLit UI provides composable data visualization components designed for the shadcn ecosystem.

### Installation via CLI:
```bash
npx shadcn@latest add @bklit/area-chart
# or
npx shadcn@latest add @bklit/bar-chart
```

### Production Recipe:
```tsx
import { AreaChart, Grid, XAxis, ChartTooltip } from "@/components/ui/chart";

const TELEMETRY_DATA = [
  { timestamp: "10:00", throughput: 420 },
  { timestamp: "11:00", throughput: 580 },
  { timestamp: "12:00", throughput: 890 },
  { timestamp: "13:00", throughput: 760 },
];

export function LiveThroughputChart() {
  return (
    <div className="w-full h-56 p-4 rounded-2xl bg-neutral-950 border border-white/10">
      <AreaChart data={TELEMETRY_DATA} categories={["throughput"]} index="timestamp">
        <Grid strokeDasharray="3 3" className="stroke-white/10" />
        <XAxis dataKey="timestamp" className="text-xs fill-neutral-400" />
        <ChartTooltip />
      </AreaChart>
    </div>
  );
}
```

---

## 2. Kokonut UI ([kokonutui.com](https://kokonutui.com/)) – Creative & AI UI

100+ creative components, interactive buttons, and AI prompt inputs.

### Production Recipe (AI Prompt Input):
```tsx
"use client";

import { useState } from "react";
import { motion } from "motion/react";
import { Sparkles, ArrowUp } from "lucide-react";

export function KokonutPromptInput({ onSubmit }: { onSubmit: (prompt: string) => void }) {
  const [prompt, setPrompt] = useState("");

  return (
    <div className="relative flex items-center w-full p-2 bg-neutral-900 border border-white/15 rounded-2xl shadow-xl focus-within:border-white/30 transition-colors">
      <Sparkles className="w-5 h-5 ml-3 text-neutral-400" />
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Ask anything or generate UI..."
        className="w-full px-4 py-2 bg-transparent text-white placeholder:text-neutral-500 focus:outline-none text-sm"
        onKeyDown={(e) => e.key === "Enter" && onSubmit(prompt)}
      />
      <motion.button
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        onClick={() => onSubmit(prompt)}
        className="p-2.5 bg-white text-black rounded-xl hover:bg-neutral-200 transition-colors"
      >
        <ArrowUp className="w-4 h-4" />
      </motion.button>
    </div>
  );
}
```

---

## 3. Origin UI ([originui.com](https://originui.com/)) – Production-Grade Controls

500+ accessible form controls, sliders, multi-selects, and tables expanding the basic shadcn library.

### Strategy:
1. Browse the exact component pattern on [originui.com](https://originui.com/).
2. Copy the TSX code directly into `@/components/ui/` with full TypeScript typing.
3. Ensure `@radix-ui/react-*` dependencies and `clsx` / `tailwind-merge` are configured.

---

## 4. Cult UI ([cult-ui.com](https://cult-ui.com/)), Animata ([animate-ui.com](https://animate-ui.com/)) & Fancy Components ([fancycomponents.dev](https://fancycomponents.dev/))

*   **Cult UI:** Heavy use of Motion physics and gradient lighting for interactive cards.
*   **Animata:** Lightweight hover effects, expandables, and micro-motion.
*   **Fancy Components:** Kinetic typography, stacked physics cards, and text scramblers.
