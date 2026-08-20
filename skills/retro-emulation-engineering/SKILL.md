---
name: retro-emulation-engineering
description: Retro console emulator architecture, hardware coprocessor simulation (CPU/RSP/RDP/APU), frame timing, audio dynamic resampling, ROM format validation, and cartridge save persistence. Use when developing, optimizing, or debugging browser-based or native video game emulators.
license: MIT
metadata:
  triggers: emulator, emulation, N64, Mupen64, RetroArch, RSP, RDP, Dynarec, ROM, .z64, .v64, .n64, save states, SRAM, FlashRAM, EEPROM
  role: specialist
  scope: implementation
---

# Retro Emulation Engineering Skill

Specialist in console hardware simulation, CPU interpretation and dynamic recompilation (Dynarec), coprocessor command buffers (RSP/RDP), audio ring buffer synchronization, and ROM format manipulation.

---

## 1. Emulation Core Subsystems Topology

An emulator simulates hardware components communicating over virtual buses:

```
[ MIPS R4300i CPU ] <─── System Bus ───> [ RDRAM (4MB / 8MB Expansion) ]
       │                                            │
       ▼                                            ▼
[ Reality Co-Processor (RCP) ]              [ Serial Interface (SI) ]
   ├── RSP (Vector DSP / Geometry)             └── Controllers & Memory Paks
   ├── RDP (Rasterizer & Blending)          [ Audio Interface (AI) ]
   ├── Video Interface (VI / WebGL)            └── PCM Audio Buffer / DMA
   └── Audio Interface (AI / Web Audio)     [ Peripheral Interface (PI) ]
                                               └── Cartridge ROM & Save Media
```

---

## 2. ROM Header Validation & Auto-Detection Table

Nintendo 64 ROMs exist in three physical endian formats. The first 4 bytes indicate format:

| Format | Magic Bytes (Hex) | Description | Normalization Action |
|--------|-------------------|-------------|----------------------|
| **`.z64`** | `80 37 12 40` | Big-Endian (Native N64 bus order) | Native format; no swap needed. |
| **`.v64`** | `37 80 40 12` | Byte-Swapped (Doctor V64 copier) | Swap every 2 adjacent bytes (`swap16`). |
| **`.n64`** | `40 12 37 80` | Little-Endian (Z64 copier / PC) | Swap every 4 bytes (`swap32`). |

### In-Place ROM Normalizer (JavaScript / TypeScript)
```typescript
export function normalizeN64Rom(data: Uint8Array): Uint8Array {
    if (data.length < 4) return data;
    const b0 = data[0], b1 = data[1], b2 = data[2], b3 = data[3];

    // Already Big-Endian .z64
    if (b0 === 0x80 && b1 === 0x37 && b2 === 0x12 && b3 === 0x40) {
        return data;
    }
    // Byte-swapped .v64 -> swap 16-bit words
    if (b0 === 0x37 && b1 === 0x80 && b2 === 0x40 && b3 === 0x12) {
        const len = data.length - (data.length % 2);
        for (let i = 0; i < len; i += 2) {
            const tmp = data[i];
            data[i] = data[i + 1];
            data[i + 1] = tmp;
        }
        return data;
    }
    // Little-endian .n64 -> swap 32-bit dwords
    if (b0 === 0x40 && b1 === 0x12 && b2 === 0x37 && b3 === 0x80) {
        const len = data.length - (data.length % 4);
        for (let i = 0; i < len; i += 4) {
            const t0 = data[i], t1 = data[i + 1], t2 = data[i + 2], t3 = data[i + 3];
            data[i] = t3;
            data[i + 1] = t2;
            data[i + 2] = t1;
            data[i + 3] = t0;
        }
        return data;
    }
    return data;
}
```

---

## 3. Audio Rate Matching & Frame Pacing

* **Sample Pacing Problem:** Emulators generate audio at non-integer rates relative to the 60Hz display refresh cycle.
* **Audio-Throttled Main Loop:** Use the audio output buffer capacity to throttle emulation steps instead of `setInterval` or unbounded `requestAnimationFrame`:
  - If buffer fill level < 20%: run extra emulation tick to prevent underflow (crackling).
  - If buffer fill level > 80%: pause emulation tick to prevent overflow and latency buildup.
