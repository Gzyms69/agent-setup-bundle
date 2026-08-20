# MCP Server Master Playbook & Operational Rules

This document defines the **canonical role, execution boundaries, and tool synergies** for all Model Context Protocol (MCP) servers integrated into the Antigravity agentic environment.

---

## 1. Global MCP Execution Directives

1. **Eager vs Lazy Invocation:**
   - Eager MCP tools (e.g. `mempalace_*`) are called directly.
   - Lazy MCP tools are called via `call_mcp_tool(ServerName, ToolName, Arguments)`.
2. **Deterministic Over Bash Shells:**
   - Always prefer specialized MCP tools over spawning interactive bash processes or raw CLI utilities for supported domains (Lighthouse, Chrome DevTools, GitHub API, MemPalace, Postgres/SQLite, Docker, Firecrawl, AST-Grep).
3. **Fallback Grace Period:**
   - If an MCP tool encounters an upstream network/auth error, output an explanation before attempting a standard bash CLI fallback.

---

## 2. MCP Server Roles & Tool Matrix

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       ANTIGRAVITY MCP MATRIX                                           │
└───────────────────────────────────────────────────┬────────────────────────────────────────────────────┘
                                                    │
    ┌──────────────┬────────────────┬───────────────┼───────────────┬────────────────┬─────────────────┐
    ▼              ▼                ▼               ▼               ▼                ▼                 ▼
┌────────┐ ┌───────────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────────┐ ┌───────────┐ ┌─────────────────┐
│ Memory │ │ DevTools/Perf │ │ Lighthouse  │ │ Databases   │ │ Container/OS │ │ Web/Docs  │ │ Code Analysis   │
│ (Mem-  │ │ (Chrome-      │ │ (@daniels-  │ │ (Postgres / │ │ (Docker MCP) │ │ (Fire-    │ │ (AST-Grep,      │
│ palace)│ │  DevTools)    │ │  ogl/mcp)   │ │  SQLite)    │ │              │ │  crawl)   │ │  GitHub)        │
└────────┘ └───────────────┘ └─────────────┘ └─────────────┘ └──────────────┘ └───────────┘ └─────────────────┘
```

### 1. `mempalace` (Long-Term Memory & Knowledge Graph)
- **Role:** Single source of truth for historical code architectures, entity relationships, past audit reports, user preferences, and project facts.
- **Key Tools:** `mempalace_status`, `mempalace_search`, `mempalace_kg_query`, `mempalace_diary_write`, `mempalace_mine`.
- **Mandate:** Always query before declaring facts about past projects or running blind full-disk searches.

### 2. `lighthouse-mcp` (`@danielsogl/lighthouse-mcp`)
- **Role:** End-to-end synthetic web audits, generating 0-100 scores across Performance, Accessibility, Best Practices, and SEO.
- **Key Capabilities:** Mobile & desktop device emulation, network throttling profiles, automated performance budgeting.
- **Mandate:** Use as the primary gatekeeper for benchmarking web applications before and after optimization loops.

### 3. `chrome-devtools` (`chrome-devtools-mcp`)
- **Role:** Deep, runtime browser diagnostics and Chromium performance traces.
- **Key Tools:**
  - `performance_start_trace` / `performance_stop_trace`: Deep flame charts, CPU timelines, Long Tasks detection.
  - `performance_analyze_insight`: Detailed LCP breakdown, layout shift roots, document latency analysis.
  - `take_heapsnapshot`: Memory leak and memory bloat investigations.
  - `list_network_requests`: Waterfall payload and asset blocking inspections.
- **Mandate:** Use whenever a performance audit flags high TBT, Long Tasks, or unexplained LCP delays.

### 4. `postgres` & `sqlite` (`@modelcontextprotocol/server-postgres`, `server-sqlite`)
- **Role:** Direct database inspection, schema analysis, migration testing, and data verification.
- **Key Tools:** Query execution, schema introspection, table structure inspection.
- **Mandate:** Use for verifying database state, foreign keys, index performance, and migration integrity without writing manual bash `psql`/`sqlite3` scripts. Queries modifying production data require explicit approval.

### 5. `docker` (`@modelcontextprotocol/server-docker`)
- **Role:** Container and Docker Compose orchestration and telemetry.
- **Key Tools:** `list_containers`, `get_logs`, `inspect_container`, `list_images`.
- **Mandate:** Use for inspecting backend services (e.g. Postgres, Redis, Microservices), tailing logs without hanging terminal processes, and verifying container port bindings.

### 6. `firecrawl` (`firecrawl-mcp`)
- **Role:** High-fidelity web scraping, dynamic SPA rendering, and clean Markdown extraction.
- **Key Capabilities:** Crawling documentation, bypassing Cloudflare/anti-bot protection for technical research, extracting structured tables.
- **Mandate:** Use as the first-choice tool when extracting documentation or research data from external websites.

### 7. `ast-grep` (`@ast-grep/mcp`)
- **Role:** Structural syntax-tree (AST) search, linting, and multi-file code refactoring.
- **Key Capabilities:** Matching code patterns independent of whitespace/formatting across TypeScript, Python, Rust, Go.
- **Mandate:** Use for systematic code reviews, anti-pattern detection (e.g. missing dependency arrays, uncaught promises, missing cleanups), and architectural refactoring.

### 8. `puppeteer` (`@modelcontextprotocol/server-puppeteer`)
- **Role:** Headless browser automation, complex multi-step user journey simulation, and visual screenshots.
- **Key Tools:** `puppeteer_navigate`, `puppeteer_screenshot`, `puppeteer_click`, `puppeteer_fill`, `puppeteer_evaluate`.
- **Mandate:** Use for interactive verification, end-to-end visual QA, and interaction simulation under throttled conditions.

### 9. `github` (`@modelcontextprotocol/server-github`)
- **Role:** GitHub remote API management.
- **Key Tools:** `create_pull_request`, `list_issues`, `create_issue`, `get_pull_request_status`, `create_pull_request_review`, `search_repositories`.
- **Mandate:** Use for all remote PR/issue/review tasks. Do NOT run interactive `gh` CLI commands in bash. Local file staging and commits must use local `git` CLI.

### 10. `oracle-oci` (`oracle.oci-api-mcp-server`)
- **Role:** Oracle Cloud Infrastructure operations.
- **Mandate:** Prefer over raw OCI CLI commands.

### 11. `StitchMCP` (Google Stitch)
- **Role:** UI screen design generation, screen variants, and design system synchronization.
- **Key Tools:** `create_project`, `generate_screen_from_text`, `edit_screens`, `apply_design_system`.
