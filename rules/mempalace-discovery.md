# MemPalace Knowledge Discovery Mandate (First-Port Protocol)

This rule establishes the **absolute priority of MemPalace retrieval** before attempting broad filesystem greps or full-disk searches.

---

## 1. The Core Law of Knowledge Recall
Whenever the user asks about or references:
- Specific past projects (e.g. `katalog`, `busos`, `leadfinder`, `electrode`, `jobhunt`, etc.),
- Historical architectural decisions, benchmarks, or audit reports,
- Previous configurations, prompt sets, or team conventions,
- Personal context, past events, or people:

**I AM ABSOLUTELY FORBIDDEN** from running broad, unconstrained filesystem grep searches (`grep_search` across `/home/gzyms`) or recursive file scans as a primary discovery method.

---

## 2. Mandatory Step-by-Step Retrieval Protocol

1. **Step 1: Check Palace Status & Wings**
   - Call `mempalace_status` to identify relevant wings (e.g. `katalog`, `busos`, `leadfinder`) and rooms.
2. **Step 2: Scoped Search in MemPalace**
   - Call `mempalace_search` with targeted queries and specific `wing` / `room` filters.
   - Or call `mempalace_kg_query` / `mempalace_kg_timeline` for entity relationships and chronological facts.
3. **Step 3: Direct Source File Access**
   - Use the `source_path` returned in the MemPalace drawer results to view the exact, authoritative source file using `view_file`.
4. **Step 4: Fallback to Targeted Directory Grep Only When Needed**
   - Only if MemPalace has no drawer for a brand new, unindexed file, execute a scoped `grep_search` strictly within the identified project directory (e.g. `SearchPath: "/home/gzyms/Dev Projects/Katalog"`), **NEVER** at the root `/home/gzyms`.

---

## 3. Session Closing Mandate
At the conclusion of any session where significant architectural decisions, optimizations, or new features were implemented:
- Call `mempalace_diary_write` to store an AAAK summary of what was completed, learned, and benchmarked.
