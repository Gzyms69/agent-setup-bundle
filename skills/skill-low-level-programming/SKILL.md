---
name: skill-low-level-programming
description: Low-level systems programming, C/C++, Rust, Assembly, byte manipulation, memory layout, pointers, bitwise arithmetic, and endianness handling. Use when analyzing or developing low-level systems, WASM memory layouts, binary protocols, memory-mapped I/O, or performance-critical byte buffers.
---

# Low-Level Systems Programming Skill

This skill provides expert patterns for memory-safe, high-performance systems programming, binary data parsing, and low-level computing across C/C++, Rust, WebAssembly, and native system boundaries.

---

## 1. Endianness & Binary Format Parsing

Always account for byte endianness when reading or transforming binary payloads, ROMs, or raw buffers:

* **Big-Endian (BE, Network Byte Order):** Most significant byte stored first (`0x80371240` -> `80 37 12 40`). Standard for N64 `.z64`, Motorola 68k, MIPS BE.
* **Byte-Swapped (Middle-Endian / BADC):** 16-bit word byte swap (`0x37804012` -> `37 80 40 12`). Standard for `.v64` / Doctor V64 format.
* **Little-Endian (LE):** Least significant byte stored first (`0x40123780` -> `40 12 37 80`). Standard for `.n64` / Z64 copier, x86/x64, ARM (default), WASM memory.

### Fast In-Place Byte-Swap Routine (JavaScript / TypedArrays)
```typescript
/**
 * Fast 16-bit byte-swapping for .v64 to .z64 normalization
 */
function swap16InPlace(u8: Uint8Array): void {
  const len = u8.length - (u8.length % 2);
  for (let i = 0; i < len; i += 2) {
    const tmp = u8[i];
    u8[i] = u8[i + 1];
    u8[i + 1] = tmp;
  }
}

/**
 * Fast 32-bit word-swapping for .n64 to .z64 normalization
 */
function swap32InPlace(u8: Uint8Array): void {
  const len = u8.length - (u8.length % 4);
  const u32 = new Uint32Array(u8.buffer, u8.byteOffset, len >> 2);
  for (let i = 0; i < u32.length; i++) {
    const v = u32[i];
    u32[i] = ((v & 0xff) << 24) |
             ((v & 0xff00) << 8) |
             ((v >> 8) & 0xff00) |
             ((v >> 24) & 0xff);
  }
}
```

---

## 2. WebAssembly Memory & Direct Heap Access

When interfacing JavaScript/TypeScript with C/C++ Emscripten or Rust WASM modules:

* **Zero-Copy Transfers:** Use views directly over `Module.HEAPU8.buffer` (`new Uint8Array(Module.HEAPU8.buffer, ptr, size)`).
* **Buffer Invalidation Rule:** ANY call to `Module._malloc`, `Module._realloc`, or WASM functions that grow memory (`memory.grow`) **invalidates** all previous `ArrayBuffer` views. Always re-instantiate typed arrays after allocations or memory growth.
* **Alignment Guarantees:** Ensure pointers passed to 32-bit/64-bit typed arrays (`HEAP32`, `HEAPF32`, `HEAP64`) are properly aligned to 4 or 8 bytes (`ptr % 4 === 0`).
* **Memory Lifecycle (Manual RAII):** Every `Module._malloc(size)` MUST have a guaranteed matching `Module._free(ptr)` in a `finally` block to prevent catastrophic heap leaks.

---

## 3. Bitwise Manipulation & Flag Bitmasks

* **Bit Extraction:** `(value >> bitPosition) & 1`
* **Bitmask Verification:** `(flags & MASK) === MASK`
* **Bit Clearing:** `flags &= ~MASK`
* **Bit Setting:** `flags |= MASK`
* **Bit Toggling:** `flags ^= MASK`
* **Sign Extension (e.g. 16-bit to 32-bit integer):** `(val << 16) >> 16`
* **Clamp to Byte:** `val & 0xFF`

---

## 4. Performance & Memory Safety Invariants

1. **Preallocate Buffers:** Never allocate small `ArrayBuffers` or typed arrays inside hot rendering, audio sampling, or frame-emulation loops. Allocate static circular buffers and reuse them.
2. **Bounds Checking:** Always validate buffer length and slice ranges before reading offsets to prevent `RangeError: offset is out of bounds`.
3. **DataView for Mixed Heterogeneous Structs:** Use `DataView` with explicit endianness flags (`view.getUint32(offset, false /* bigEndian */)`) when parsing structured headers, rather than relying on host architecture endianness.
