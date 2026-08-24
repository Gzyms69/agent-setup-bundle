# Rule: Interactive Planning Mode & Living Document Integrity

This rule defines the **mandatory operational invariants** for handling interactive planning sessions (`/plan`, `/grill-me`, multi-turn task design), maintaining plan artifacts, and editing living documents, reports, and specifications.

---

## 1. The Planning Mode Invariant (Zero Amnestic Overwrites)

When an AI agent engages in multi-turn planning discussions or refines existing documentation:

**ABSOLUTE MANDATE:**
The agent is **STRICTLY FORBIDDEN** from executing destructive, full-file overwrites that drop previously discovered codebase facts, file paths, test commands, or user decisions.

Planning is a stateful, iterative refinement process, NOT a sequence of disconnected rewrites.

---

## 2. Planning Lifecycle State Machine (For `/plan` and Plan Artifacts)

Every planning session progresses through three deterministic states:

```
┌─────────────────────────┐      User Feedback / Answers      ┌─────────────────────────┐
│     STATE 1: DRAFT      │ ────────────────────────────────► │   STATE 2: REFINEMENT   │
│ (Discovery & Facts Lock)│                                   │ (Delta Updates & Prune) │
└─────────────────────────┘                                   └───────────┬─────────────┘
                                                                          │
                                                                     User "GO"
                                                                          │
                                                                          ▼
                                                              ┌─────────────────────────┐
                                                              │    STATE 3: EXECUTION   │
                                                              │ (Locked SSOT Baseline)  │
                                                              └─────────────────────────┘
```

### State 1: Draft Creation (Turn 1)
* Perform systematic exploration (`skill-codebase-onboarding`, `grep_search`, `view_file`).
* Create the initial plan artifact with:
  - `## 1. User Alignment & Decision Log`
  - `## 2. Discovered Baseline & Codebase Facts (LOCKED)`: exact file paths, line ranges, runtime versions, test/lint commands.
  - `## 3. Active Technical Specification (SSOT)`
  - `## 4. Proposed Changes (File by File)`
  - `## 5. Verification Plan`

### State 2: Iterative Refinement (Turns 2..N)
When receiving user critique, answers to questions, or modified constraints:
1. **Delta Ingestion:** Identify specifically what is being added, modified, or revoked.
2. **Top-Level `Iteration Delta` Alert:** Every revised plan artifact MUST begin with a 3-5 bullet callout documenting:
   - What was added
   - What was modified
   - What was pruned / superseded
   - What was preserved from the previous turn
3. **Discovered Facts Preservation:** The agent is **FORBIDDEN** from deleting verified file paths, versions, or verification commands discovered in Turn 1 unless explicitly requested by the user.
4. **Active SSOT Cleaning (Anti-Context Clash):**
   - If a technology or approach is revoked (e.g. switching from PostgreSQL to SQLite), all deprecated code, schemas, and instructions MUST be **completely removed from the Active Technical Specification** to prevent hallucinated hybrid implementations.
   - Record the change in the decision log as a 1-line atomic tombstone: `[PRUNED Turn N]: <Reason>`.
5. **No Duplicate Questioning:** Answers provided by the user in previous turns are **permanently locked**. Never re-ask questions that have already been resolved.

### State 3: Execution Lock
* Once the user provides an explicit "GO", the plan artifact becomes the immutable baseline for the **Act** phase.
* Deviations during execution require explicit human-in-the-loop notification.

---

## 3. Mandatory Artifact Header Standard for `/plan`

All implementation plans created in Antigravity or workspace planning must incorporate this header structure:

```markdown
# Implementation Plan: [Task / Feature Name]

> [!NOTE]
> **Plan Version:** v[N] (Updated after Turn [N] User Feedback)
> **Iteration Delta:**
> - [ADDED]: ...
> - [MODIFIED]: ...
> - [PRUNED]: ...
> - [PRESERVED]: 100% of discovered codebase facts and test commands from v[N-1].

## 1. User Alignment & Decision Log (Cumulative)
- **[v1 Init - Timestamp]:** Initial baseline proposed.
- **[v2 User Decision - Timestamp]:** User requested [Constraint X] (LOCKED).
- **[v2 Pruned - Timestamp]:** `[PRUNED]`: [Deprecated Option Y] removed per user constraint.

## 2. Discovered Baseline & Codebase Facts (LOCKED)
- Target Files: `[absolute file paths]`
- Environment: `[Language, Runtime, Package Manager]`
- Test Commands: `[pnpm test / pytest / cargo test]`
- Verification Gate: `[npx tsc --noEmit / lint]`

## 3. Active Technical Specification (SSOT - 100% Clean)
[Only current, active architecture - zero deprecated zombie code]
```

---

## 4. Living Documentation & Audit Integrity (Non-Planning Files)

When updating existing documentation, architectural specs, or audit reports:
1. **Surgical Delta Updates:** Prefer `replace_file_content` targeting the specific modified section over blanket `write_to_file` rewrites.
2. **Audit Preservation:** When adding new audit findings to a report, append to the report; NEVER erase previously verified findings.
3. **The `[SUPERSEDED]` Protocol:** If a historical requirement is modified, mark it as `~~[OLD REQUIREMENT]~~ -> [SUPERSEDED: <reason>]` to preserve the architectural decision record (ADR).
4. **Offload Large Dead Ends:** If a revoked exploration exceeds 50 lines, move it to `<appDataDir>/brain/<id>/scratch/archived_<feature>.md` rather than leaving dead text in the main document.

---

## 5. Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
| :--- | :--- |
| *"The user only asked to change the database, so I rewrote the whole plan and omitted the test commands."* | **BLOCKED:** Violates the Discovered Facts Lock. Test commands and file paths must be preserved across turns. |
| *"I kept the old PostgreSQL code and the new SQLite code in the active section so nothing is lost."* | **BLOCKED:** Violates Active SSOT. Deprecated code creates context clash and hallucinations. Clean active spec, log 1-line tombstone in decision log. |
| *"I didn't include an Iteration Delta box because the plan is self-explanatory."* | **BLOCKED:** The user needs immediate visibility of what changed without re-reading the entire file. |

---

## 6. Verification Gates

Before presenting an updated plan artifact or living document:
- [ ] Is there an `Iteration Delta` box at the top summarizing the exact changes?
- [ ] Are all `Discovered Baseline Facts` from prior turns preserved?
- [ ] Has revoked/deprecated code been cleanly excised from the active specification (`Active SSOT`)?
- [ ] Are all user decisions and prunings recorded in the `User Alignment & Decision Log`?
- [ ] Are answered questions marked as resolved without redundant re-asking?
