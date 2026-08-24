---
name: spec-driven-development
description: MANDATORY PLANNING GATE for complex features, multi-file refactors, and architectural changes. Creates technical specifications, implementation plans, and verification matrices before coding. MUST ACTIVATE when invoked with /plan, when a task is estimated >15 minutes, touches >3 files, or introduces new APIs/schemas.
---

# Spec-Driven Development (SDD) & Interactive Planning Protocol

## Overview

Write a structured specification before writing any code. The spec is the shared source of truth between you and the human engineer — it defines what we're building, why, and how we'll know it's done. Code without a spec is guessing.

In interactive planning sessions (`/plan`, `/grill-me`, task refinement turns), SDD enforces **strict statefulness**: never perform destructive rewrites that drop discovered facts, and never leave zombie code in active specs.

---

## When to Use

- Starting a new project or feature
- Requirements are ambiguous or incomplete
- The change touches multiple files or modules
- You're about to make an architectural decision
- The task is estimated >15 minutes or explicitly invoked with `/plan`

**When NOT to use:** Single-line fixes, typo corrections, or self-contained single-function changes.

---

## The Gated Workflow

```
SPECIFY ──→ PLAN (Multi-Turn Refinement) ──→ TASKS ──→ IMPLEMENT
   │                       │                    │          │
   ▼                       ▼                    ▼          ▼
 Human                   Human                Human      Human
reviews                 reviews              reviews    reviews
```

---

### Phase 1: Specify

Start with a high-level vision. Ask the human clarifying questions until requirements are concrete.

**Surface assumptions immediately.** Before writing spec content, list what you're assuming:
```
ASSUMPTIONS I'M MAKING:
1. This is a web application (not native mobile)
2. Authentication uses session-based cookies (not JWT)
3. The database is PostgreSQL (based on existing schema)
→ Correct me now or I'll proceed with these.
```

---

### Phase 2: Plan & Multi-Turn Interactive Refinement (`/plan`)

When generating and updating implementation plans in Antigravity (`<Artifact Directory>/<plan_name>.md`) or workspace roots (`tasks/plan.md`), execute the **Planning Lifecycle State Machine**:

```
Draft v1 (Discovery & Baseline Facts Lock) ──► Refinement vN (Iteration Delta & Active SSOT) ──► Execution Lock ("GO")
```

#### Mandatory Plan Artifact Template:

```markdown
# Implementation Plan: [Feature / Task Name]

> [!NOTE]
> **Plan Version:** v[N] (Updated after Turn [N] User Feedback)
> **Iteration Delta:**
> - [ADDED]: [Specific additions in this turn]
> - [MODIFIED]: [Specific changes to previous sections]
> - [PRUNED]: [Specific components removed, logged below]
> - [PRESERVED]: 100% of discovered codebase facts and verification commands from v[N-1].

## 1. User Alignment & Decision Log (Cumulative)
- **[v1 Init - Timestamp]:** Initial baseline plan.
- **[v2 User Decision - Timestamp]:** [User decision / choice] (LOCKED).
- **[v2 Pruned - Timestamp]:** `[PRUNED]`: [Deprecated approach removed per user constraint].

## 2. Discovered Baseline & Codebase Facts (LOCKED)
- **Target Files:** `[Exact absolute paths verified via tools]`
- **Environment:** `[Language, runtime, package manager, OS]`
- **Required Commands:** `[pnpm test, npx tsc --noEmit, etc.]`

## 3. Active Technical Specification (SSOT - 100% Clean)
*Contains ONLY current, approved architecture. Deprecated code is completely excised!*
[Clean architecture diagrams, data models, interfaces, API signatures]

## 4. Proposed Changes (File by File)
### [MODIFY] path/to/file.ts
### [NEW] path/to/new_file.ts

## 5. Verification Plan (Automated & Manual)
- Automated: Exact commands to run (`pnpm test`, `npx tsc --noEmit`)
- Manual: Browser/API verification steps

## 6. Open Questions / Next Steps
[Only genuinely unanswered questions]
```

#### The 4 Invariants of Plan Iteration:
1. **Discovered Facts Lock:** Never delete discovered file paths, line ranges, or test commands across turns.
2. **Active SSOT Cleanliness:** Completely remove deprecated code from Section 3. Keep 1-line tombstones in Section 1.
3. **Top-Level Iteration Delta:** Always summarize what changed in the current version at the very top.
4. **No Duplicate Questioning:** Never re-ask questions that were resolved in previous turns.

---

### Phase 3: Tasks

Break the plan into discrete, implementable tasks in `tasks/todo.md`:

```markdown
- [ ] Task: [Description]
  - Acceptance: [What must be true when done]
  - Verify: [How to confirm — test command, build, manual check]
  - Files: [Which files will be touched]
```

---

### Phase 4: Implement

Execute tasks one at a time. Run tests and linters after each task. Update progress continuously.

---

## Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
| :--- | :--- |
| *"The user gave me 1 feedback sentence so I rewrote the whole plan and forgot the test commands."* | **BLOCKED:** Violates the Discovered Facts Lock. Test commands and file paths must be preserved. |
| *"I left the old PostgreSQL code and the new SQLite code together in Section 3 so nothing is lost."* | **BLOCKED:** Violates Active SSOT. Competing code causes context clash and hallucinations. Clean active spec, record 1-line tombstone in Section 1. |
| *"I'll ask the user again about the database choice."* | **BLOCKED:** The user already answered in Turn 2. Re-asking resolved questions wastes tokens and breaks user trust. |

---

## Verification Gates

Before submitting a plan or proceeding to implementation:
- [ ] Does the plan follow the 6-section template with an `Iteration Delta` box?
- [ ] Are all `Discovered Baseline Facts` from prior turns preserved?
- [ ] Is Section 3 (Active Technical Spec) 100% clean and free of deprecated zombie code?
- [ ] Are all user decisions logged in the cumulative `User Alignment & Decision Log`?
- [ ] Have all verification commands (`test`, `tsc`, `lint`) been validated against project reality?
