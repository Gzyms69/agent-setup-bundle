---
name: wasm-emscripten
description: Compiles C/C++ code to WebAssembly using Emscripten, configures runtime flags, bridges JavaScript and WASM, manages virtual filesystems (FS/IDBFS), and handles direct HEAP memory views. Use when compiling, debugging, or interfacing C/C++ WebAssembly modules with browser APIs, WebGL, Web Audio, or Node.js.
license: MIT
metadata:
  triggers: WebAssembly, WASM, Emscripten, emcc, ccall, cwrap, HEAPU8, HEAP16, Module.FS, IDBFS, MEMFS, wasm memory growth, EMSCRIPTEN_KEEPALIVE
  role: specialist
  scope: implementation
---

# WebAssembly & Emscripten Engineering Skill

Specialist in WebAssembly compilation pipelines, Emscripten toolchains (`emcc`), runtime bindings, direct memory inspection, and browser I/O interfacing.

---

## 1. Emscripten Compilation & Optimization Flags

When building high-performance C/C++ projects (e.g. emulators, game engines, audio processors) to WebAssembly:

```bash
emcc source.c -O3 \
  -s WASM=1 \
  -s ALLOW_MEMORY_GROWTH=1 \
  -s EXPORTED_FUNCTIONS="['_main', '_malloc', '_free', '_init_core', '_run_frame']" \
  -s EXPORTED_RUNTIME_METHODS="['ccall', 'cwrap', 'FS', 'getValue', 'setValue', 'UTF8ToString']" \
  -s USE_WEBGL2=1 \
  -s FULL_ES3=1 \
  -o emulator.js
```

### Essential Debugging Flags
* `-s ASSERTIONS=1` / `-s ASSERTIONS=2`: Enables runtime assertions and checks for stack overflows.
* `-s SAFE_HEAP=1`: Detects unaligned memory accesses, NULL pointer dereferences, and out-of-bounds reads/writes.
* `-s STACK_OVERFLOW_CHECK=2`: Injects guards to catch call-stack exhaustion.
* `-g3 --source-map-base http://localhost:8000/`: Generates DWARF/WASM sourcemaps for browser DevTools debugging.

---

## 2. JavaScript <-> WASM Interfacing

### C-Level Exports (`EMSCRIPTEN_KEEPALIVE`)
```c
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
void run_frame(void) {
    // Process one video/audio emulation step
}

EMSCRIPTEN_KEEPALIVE
uint8_t* get_framebuffer_ptr(void) {
    return g_framebuffer;
}
```

### JS-Level Invocation (`cwrap` vs Direct Calls)
```javascript
// Function wrapper with type safety
const runFrame = Module.cwrap('run_frame', null, []);
const getFramebufferPtr = Module.cwrap('get_framebuffer_ptr', 'number', []);

// Direct fast C-pointer call
const ptr = Module._get_framebuffer_ptr();
```

---

## 3. Direct HEAP Memory Views & The Growth Invalidation Rule

Emscripten exposes WASM linear memory as typed array views:
* `Module.HEAPU8`: `Uint8Array` (8-bit unsigned bytes)
* `Module.HEAP16`: `Int16Array` (16-bit signed PCM audio samples)
* `Module.HEAP32`: `Int32Array` (32-bit signed integers/pointers)
* `Module.HEAPF32`: `Float32Array` (32-bit IEEE-754 floats)

### CRITICAL MEMORY INVALIDATION RULE
Whenever WebAssembly memory grows (`ALLOW_MEMORY_GROWTH=1` or `Module._malloc`), the underlying `ArrayBuffer` is detached and reallocated.
**Never cache `HEAP` typed arrays across asynchronous boundaries or frame loops:**

```javascript
// BAD: Storing reference across frames (will throw "Cannot perform construct on detached ArrayBuffer" on memory grow)
class AudioRenderer {
  constructor() {
    this.buffer = new Int16Array(Module.HEAP16.buffer, Module._getAudioPtr(), 4096);
  }
}

// GOOD: Fresh view instantiation or validation helper
function getAudioView(ptr, size) {
  return new Int16Array(Module.HEAP16.buffer, ptr, size);
}
```

---

## 4. Virtual File System (FS & IDBFS)

Emscripten provides an in-memory POSIX filesystem (`MEMFS`) and an IndexedDB persistent layer (`IDBFS`):

```javascript
// Writing ROM directly to Virtual FS
FS.writeFile('/rom.v64', romUint8Array);

// Reading output or save data
const saveStateBytes = FS.readFile('/savestate.gz');

// Mounting persistent storage in IndexedDB
FS.mkdir('/saves');
FS.mount(IDBFS, {}, '/saves');
FS.syncfs(true, function (err) {
    // populated from IndexedDB to Virtual FS
});
```
