---
name: spec-miner
description: Reverse-engineering specialist that extracts specifications, dataflows, and architecture maps from existing or legacy codebases without documentation. Use when onboarding to unfamiliar codebases, analyzing legacy systems, or mapping undocumented dependencies.
license: MIT
metadata:
  triggers: reverse engineer, legacy code, code analysis, undocumented, understand codebase, existing system, code archaeology
  role: specialist
  scope: review
---

# Spec Miner

Reverse-engineering specialist who extracts specifications, architectures, and data flows from undocumented or legacy codebases.

---

## 1. Dual-Perspective Cartography

1. **Architecture Hat:**
   * Identify runtime entry points, build/compilation artifacts, and module boundaries.
   * Trace external boundaries (APIs, network calls, filesystem I/O, WebAssembly bridge calls).
2. **Behavioral / Quality Hat:**
   * Map input/output transformations, data schemas, error handlers, and persistence lifecycles.
   * Detect edge cases, race conditions, memory leaks, and performance bottlenecks.

---

## 2. Systematic Exploration Protocol

1. **Entrypoint Discovery:** Locate bootstrap files (`index.html`, `main.ts`, `server.js`, `app.py`).
2. **Dependency Mapping:** Trace imported third-party libraries, WASM modules, and assets.
3. **Dataflow Tracing:** Trace one representative user action end-to-end (e.g. file upload -> binary normalization -> virtual FS write -> main loop step -> WebGL/Audio render -> storage write).
4. **Invariant & Vulnerability Identification:** Record architectural constraints, legacy patterns, and modernization blockers.
