---
name: skill-emulator-wasm
description: WebAssembly emulation engineering, Emscripten runtime bridging, retro hardware simulation (CPU/RSP/RDP/APU), ROM header parsing, save state serialization, WebGL rendering, and Web Audio synchronization. Use when developing, analyzing, or debugging WebAssembly emulators, ROM managers, and retro gaming web platforms.
---

# WebAssembly & Retro Emulation Engineering Skill

This skill provides architectural patterns, performance optimization, and operational guidelines for browser-based emulation, WebAssembly bridging, and ROM manipulation.

---

## 1. Emulator Architecture & Emscripten Bridge

Browser-based emulators (like N64Wasm, RetroArch WASM cores, Mupen64Plus-WASM) bridge compiled C/C++ core engines with browser subsystem APIs:

```
[ JavaScript / Web Frontend ]
   ├── Input Controller (Gamepad API, Keyboard, Touch/NippleJS)
   ├── Display Manager (WebGL / Canvas context binding)
   ├── Audio Subsystem (Web Audio API / ScriptProcessor / AudioWorklet)
   └── Persistence Layer (IndexedDB / LocalStorage / Cloud Saves)
             │
      Emscripten C-Bridge (`ccall`, `cwrap`, `Module._*`, `FS`)
             │
[ WebAssembly Core Engine (Compiled C/C++) ]
   ├── CPU Interpreter / Dynarec Recompiler
   ├── Reality Co-Processor (RSP / RDP Graphics Engine)
   ├── Memory-Mapped I/O & Memory Controller
   └── Save System (SRAM / FlashRAM / EEPROM 4k/16k / Save States)
```

---

## 2. ROM Header Parsing & Identification (Nintendo 64 Standard)

The first 64 bytes (`0x00 - 0x3F`) of any N64 ROM contain critical metadata:

| Byte Offset | Size (Bytes) | Field Name | Description |
|-------------|--------------|------------|-------------|
| `0x00` | 4 | Magic Number | `0x80371240` (Big Endian `.z64`), `0x37804012` (Byte Swapped `.v64`), `0x40123780` (Little Endian `.n64`) |
| `0x04` | 4 | Clock Rate | Clock rate seed |
| `0x08` | 4 | Program Counter | Boot entry address (default `0x80000400`) |
| `0x0C` | 4 | Release Address | Library version |
| `0x10` | 4 | CRC1 | Checksum 1 (boot verification) |
| `0x14` | 4 | CRC2 | Checksum 2 (boot verification) |
| `0x18` | 8 | Reserved | Unused |
| `0x20` | 20 | Internal Name | ASCII title padded with spaces |
| `0x34` | 4 | Reserved | Unused |
| `0x38` | 4 | Media Format | Cartridge format code |
| `0x3C` | 2 | Cartridge ID | Game ID (e.g. `SM` for Super Mario, `ZL` for Zelda) |
| `0x3E` | 1 | Country Code | `E` (USA), `P` (Europe), `J` (Japan), `U` (Australia), `D` (Germany), `F` (France) |
| `0x3F` | 1 | Version | ROM revision version |

---

## 3. Audio Synchronization & Rate Matching

Emulated retro consoles produce audio at non-standard sample rates (e.g., 32000Hz, 44100Hz, 48000Hz) tied to CPU cycles.
Browser `AudioContext` typically operates at the hardware host rate (usually 44100Hz or 48000Hz).

* **Buffer Starvation / Underrun:** Causes audio clicks, pops, and stutter.
* **Buffer Overflow / High Latency:** Causes sound delay and video desync.
* **Dynamic Resampling:** Monitor the audio ring buffer fill level. If the buffer is depleting, slightly slow down playback or duplicate samples; if overflowing, skip or interpolate samples to keep latency < 50ms.
* **Audio-to-Video Timing:** Emulation frame loops (`requestAnimationFrame`) should be throttled by the audio buffer consumption to prevent video tearing or erratic speedups.

---

## 4. Input Polling & Virtual Controller

1. **HTML5 Gamepad API:** Must be polled inside `requestAnimationFrame` using `navigator.getGamepads()`. Do not rely on event listeners for stick axes.
2. **Deadzone Filtering:** Apply radial or axial deadzones (typically 0.15 - 0.20) to analog sticks to prevent stick drift.
3. **Touch Controls:** Use multi-touch virtual joysticks (e.g. NippleJS) with decoupled canvas rendering to prevent blocking touch event processing.

---

## 5. Save Data Management & Integrity

* **EEPROM (512B or 2KB):** 4Kbit or 16Kbit serial EEPROM used for lightweight saves.
* **SRAM (32KB):** Battery-backed Static RAM (`.sra`).
* **FlashRAM (128KB):** High-capacity flash memory (`.fla`).
* **Save States (`.state`):** Full serialized snapshot of CPU registers, RDRAM, RSP/RDP status, and timer interrupts.
* **IndexedDB over LocalStorage:** For ROM caching and save states (>5MB), always prefer `IndexedDB` over `localStorage` due to synchronous 5MB quota limitations.
