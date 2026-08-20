---
name: c-cpp-systems
description: Writes, analyzes, optimizes, and debugs low-level C and C++ systems code, memory safety, pointers, manual RAII, struct alignment, bitwise arithmetic, and sanitizers (ASan/UBSan). Use when inspecting C/C++ source code, emulator cores, compiler flags, memory corruption, or native bindings.
license: MIT
metadata:
  triggers: C, C++, C++20, pointers, memory allocation, struct packing, bitfields, endianness, malloc, free, RAII, AddressSanitizer, ASan, valgrind
  role: specialist
  scope: implementation
---

# C & C++ Systems Programming Skill

Specialist in high-performance C and C++ systems engineering, memory safety, zero-overhead abstractions, binary representation, and low-level debugging.

---

## 1. Memory Management & Pointer Arithmetic

1. **Manual RAII & Ownership Rules:**
   * Every dynamically allocated pointer (`malloc`, `calloc`, `new`) must have an unambiguous single owner responsible for its deallocation (`free`, `delete`, `unique_ptr`).
   * Never dereference a pointer after freeing (`use-after-free`). Explicitly set freed pointers to `NULL`/`nullptr` in non-RAII code.
2. **Alignment & Padding:**
   * Align data types according to machine natural boundary (4 bytes for 32-bit, 8 bytes for 64-bit).
   * For binary headers (ROMs, network packets), use explicit packing to prevent compiler padding:
     ```c
     #pragma pack(push, 1)
     typedef struct {
         uint32_t magic;
         uint32_t clock_rate;
         uint32_t pc;
         uint32_t release;
         uint32_t crc1;
         uint32_t crc2;
     } RomHeader;
     #pragma pack(pop)
     ```

---

## 2. Bitwise Manipulation & Endianness Handling

* **Byte Extraction:** `uint8_t byte = (val >> (shift * 8)) & 0xFF;`
* **Bitmask Assertion:** `if ((status_reg & STATUS_READY) != 0)`
* **Big-Endian to Little-Endian (32-bit swap):**
  ```c
  static inline uint32_t swap32(uint32_t val) {
      return ((val & 0x000000FF) << 24) |
             ((val & 0x0000FF00) << 8)  |
             ((val & 0x00FF0000) >> 8)  |
             ((val & 0xFF000000) >> 24);
  }
  ```
* **Byte-Swapped (16-bit Middle-Endian swap for .v64):**
  ```c
  static inline uint16_t swap16(uint16_t val) {
      return (val << 8) | (val >> 8);
  }
  ```

---

## 3. Sanitizers & Diagnostic Verification

When compiling native cores or diagnostic builds:
* **AddressSanitizer (ASan):** `-fsanitize=address -fno-omit-frame-pointer` — Catches out-of-bounds access, stack overflows, and use-after-free.
* **UndefinedBehaviorSanitizer (UBSan):** `-fsanitize=undefined` — Catches integer overflows, invalid bit shifts, and misaligned pointer dereferences.
* **MemorySanitizer (MSan):** `-fsanitize=memory` — Detects uninitialized memory reads.
* **Valgrind Memcheck:** `valgrind --leak-check=full --track-origins=yes ./binary`
