# MemPalace Knowledge Discovery & Retention Mandate (First-Port Protocol)

This rule establishes the **absolute priority of MemPalace retrieval** for project discovery and context resolution before attempting filesystem greps or file discovery scans.

---

## 1. The Core Law of Knowledge Recall (Phase 0 Discovery Gate)
At the start of **EVERY task and conversation**, before executing broad filesystem greps (`grep_search`) or recursive file searches (`find_by_name`):

**I MUST query MemPalace first:**
- Check for existing architecture, ADRs, previous implementations, and team decisions via `mempalace_search` or `mempalace_kg_query`.
- Call `mempalace_status` to view active wings and rooms if scope is ambiguous.

**I AM ABSOLUTELY FORBIDDEN** from running unconstrained filesystem grep searches (`grep_search` across `/home/gzyms`) or exploratory file scans without first checking MemPalace.

---

## 2. Mandatory Step-by-Step Retrieval Protocol

1. **Step 1: Scoped Search in MemPalace**
   - Call `mempalace_search` with targeted queries and specific `wing` / `room` filters (e.g. `katalog`, `busos`, `leadfinder`, `electrode`, `jobhunt`).
   - Or call `mempalace_kg_query` / `mempalace_kg_timeline` for entity relationships and temporal facts.
2. **Step 2: Direct Source File Access**
   - Use the `source_file` path returned in the MemPalace drawer results to inspect the exact, authoritative source file using `view_file`.
3. **Step 3: Scoped Directory Inspection (Fallback Only)**
   - Only if MemPalace has no drawer for a brand new, unindexed file, execute a scoped search strictly within the specific project directory (e.g. `SearchPath: "/home/gzyms/Dev Projects/Katalog"`), **NEVER** at the root `/home/gzyms`.

---

## 3. Session & Task Conclusion Mandate (Mandatory Retention)
Before completing any task or delivering final modifications:
- **MANDATORY ACTION:** Call `mempalace_diary_write` to store an AAAK summary of what was completed, key architectural decisions made, and bugs resolved.
- When new entities, frameworks, or dependencies are established, register them with `mempalace_kg_add` or `mempalace_add_drawer`.
