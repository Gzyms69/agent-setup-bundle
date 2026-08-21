# Micro-Interactions, Kinetics & Visual Haptics

This reference document provides production code recipes for high-end micro-interactions, magnetic cursor tracking, 3D card tilt physics, and kinetic typography.

---

## 1. Magnetic Cursor Pull Button

Smoothly attracts the button element toward the user's cursor within proximity:

```tsx
"use client";

import { useRef, useState } from "react";
import { motion } from "motion/react";

export function MagneticButton({ children }: { children: React.ReactNode }) {
  const ref = useRef<HTMLButtonElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e: React.MouseEvent<HTMLButtonElement>) => {
    const { clientX, clientY } = e;
    const { left, top, width, height } = ref.current!.getBoundingClientRect();
    const middleX = clientX - (left + width / 2);
    const middleY = clientY - (top + height / 2);
    setPosition({ x: middleX * 0.3, y: middleY * 0.3 });
  };

  const reset = () => setPosition({ x: 0, y: 0 });

  return (
    <motion.button
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseLeave={reset}
      animate={{ x: position.x, y: position.y }}
      transition={{ type: "spring", stiffness: 350, damping: 20, mass: 0.5 }}
      className="relative px-6 py-3 rounded-xl bg-white text-black font-medium shadow-lg hover:shadow-xl transition-shadow"
    >
      {children}
    </motion.button>
  );
}
```

---

## 2. 3D Perspective Tilt Card with Specular Glare

```tsx
"use client";

import { useRef } from "react";
import { motion, useMotionValue, useSpring, useTransform } from "motion/react";

export function PerspectiveTiltCard({ title, desc }: { title: string; desc: string }) {
  const cardRef = useRef<HTMLDivElement>(null);
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  const mouseXSpring = useSpring(x);
  const mouseYSpring = useSpring(y);

  const rotateX = useTransform(mouseYSpring, [-0.5, 0.5], ["12deg", "-12deg"]);
  const rotateY = useTransform(mouseXSpring, [-0.5, 0.5], ["-12deg", "12deg"]);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = cardRef.current!.getBoundingClientRect();
    const width = rect.width;
    const height = rect.height;
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    x.set(mouseX / width - 0.5);
    y.set(mouseY / height - 0.5);
  };

  const handleMouseLeave = () => {
    x.set(0);
    y.set(0);
  };

  return (
    <motion.div
      ref={cardRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      style={{ rotateX, rotateY, transformStyle: "preserve-3d" }}
      className="relative w-80 h-96 rounded-3xl bg-neutral-900 border border-white/10 p-8 flex flex-col justify-between shadow-2xl"
    >
      <div style={{ transform: "translateZ(40px)" }}>
        <h4 className="text-2xl font-bold text-white font-heading">{title}</h4>
        <p className="text-sm text-neutral-400 mt-2">{desc}</p>
      </div>
      <div style={{ transform: "translateZ(20px)" }} className="text-xs font-mono text-neutral-500">
        60 FPS Physical Tilt
      </div>
    </motion.div>
  );
}
```

---

## 3. Kinetic Text Scramble on Hover

```tsx
"use client";

import { useState } from "react";

const CHARS = "ABCDEFGHJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";

export function KineticTextScramble({ text }: { text: string }) {
  const [displayText, setDisplayText] = useState(text);

  const scramble = () => {
    let iteration = 0;
    const interval = setInterval(() => {
      setDisplayText(
        text
          .split("")
          .map((char, index) => {
            if (index < iteration) return text[index];
            return CHARS[Math.floor(Math.random() * CHARS.length)];
          })
          .join("")
      );

      if (iteration >= text.length) clearInterval(interval);
      iteration += 1 / 3;
    }, 30);
  };

  return (
    <span onMouseEnter={scramble} className="font-mono cursor-pointer transition-colors hover:text-emerald-400">
      {displayText}
    </span>
  );
}
```
