---
name: spec-driven-development
description: Creates technical specifications before coding. Use when starting a new project, feature, or significant change, and no specification exists yet. Use when requirements are unclear, ambiguous, or when a change touches multiple modules.
---

# Spec-Driven Development

## Overview

Write a structured specification before writing any code. The spec is the shared source of truth between you and the human engineer — it defines what we're building, why, and how we'll know it's done. Code without a spec is guessing.

## When to Use

- Starting a new project or feature
- Requirements are ambiguous or incomplete
- The change touches multiple files or modules
- You're about to make an architectural decision
- The task would take more than 15 minutes to implement

**When NOT to use:** Single-line fixes, typo corrections, or changes where requirements are unambiguous and self-contained.

## The Gated Workflow

Spec-driven development has four phases. Do not advance to the next phase until the current one is validated by the user.

```
SPECIFY ──→ PLAN ──→ TASKS ──→ IMPLEMENT
   │          │        │          │
   ▼          ▼        ▼          ▼
 Human      Human    Human      Human
 reviews    reviews  reviews    reviews
```

### Phase 1: Specify

Start with a high-level vision. Ask the human clarifying questions until requirements are concrete.

**Surface assumptions immediately.** Before writing any spec content, list what you're assuming:

```
ASSUMPTIONS I'M MAKING:
1. This is a web application (not native mobile)
2. Authentication uses session-based cookies (not JWT)
3. The database is PostgreSQL (based on existing schema)
4. We're targeting modern browsers only (no legacy support)
→ Correct me now or I'll proceed with these.
```

Don't silently fill in ambiguous requirements. The spec's entire purpose is to surface misunderstandings *before* code gets written — assumptions are the most dangerous form of misunderstanding.

**Write a spec document covering these six core areas:**

1. **Objective** — What are we building and why? Who is the user? What does success look like?
2. **Commands** — Full executable commands with flags, not just tool names.
   ```
   Build: npm run build
   Test: npm test
   Lint: npm run lint --fix
   Dev: npm run dev
   ```
3. **Project Structure** — Where source code lives, where tests go, where docs belong.
4. **Code Style** — A concise code snippet showing naming conventions, imports, and style.
5. **Testing Strategy** — Testing framework, location of test suites, coverage expectations.
6. **Boundaries** — Three-tier system:
   - **Always do:** Run tests/linters before commits, validate external inputs.
   - **Ask first:** Modify database schemas, add npm/pip dependencies, change CI/CD configuration.
   - **Never do:** Commit plain secrets, edit vendor directories, remove failing tests without approval.
7. **SSOT & Architecture Cartography** — Audit existing codebase (`grep_search`, `list_dir`) and document:
   - Existing endpoints/modules/utilities to REUSE.
   - Existing modules to EXTEND in-place (no parallel duplicates).

**Spec template:**

```markdown
# Spec: [Project/Feature Name]

## Objective
[What we're building and why. User stories or acceptance criteria.]

## Tech Stack
[Framework, language, key dependencies with versions]

## Commands
[Build, test, lint, dev — full commands]

## Project Structure
[Directory layout with descriptions]

## Code Style
[Example snippet + key conventions]

## Testing Strategy
[Framework, test locations, coverage requirements]

## Boundaries
- Always: [...]
- Ask first: [...]
- Never: [...]

## Success Criteria
[How we'll know this is done — specific, testable conditions]

## Open Questions
[Anything unresolved that needs human input]
```

**Reframe instructions as success criteria.** When receiving vague requirements, translate them into concrete conditions:

```
REQUIREMENT: "Make the dashboard faster"

REFRAMED SUCCESS CRITERIA:
- Dashboard LCP < 2.5s on 4G connection
- Initial data load completes in < 500ms
- No layout shift during load (CLS < 0.1)
→ Are these the right targets?
```

### Phase 2: Plan

With the validated spec, generate a technical implementation plan:

1. Identify the major components and their dependencies.
2. Determine the implementation order (what must be built first).
3. Note risks and mitigation strategies.
4. Define verification checkpoints between phases.

Save the plan to `tasks/plan.md`. The plan should be reviewable so the user can easily approve the technical path.

### Phase 3: Tasks

Break the plan into discrete, implementable tasks:

- Each task should be completable in a single focused session.
- Each task has explicit acceptance criteria.
- Each task includes a verification step (test command, build, manual check).
- Tasks are ordered by dependency.
- Save the task list to `tasks/todo.md`.

**Task template:**
```markdown
- [ ] Task: [Description]
  - Acceptance: [What must be true when done]
  - Verify: [How to confirm — test command, build, manual check]
  - Files: [Which files will be touched]
```

### Phase 4: Implement

Execute tasks one at a time. Run tests and linters after each task. Update the `tasks/todo.md` progress continuously.

---

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| \"This is simple, I don't need a spec\" | Simple tasks don't need *long* specs, but they still need acceptance criteria. A two-line spec is fine. |
| \"I'll write the spec after I code it\" | That's documentation, not specification. The spec's value is in forcing clarity *before* code. |
| \"The spec will slow us down\" | A 15-minute spec prevents hours of rework. Designing in 15 minutes beats debugging in 15 hours. |
| \"The error handling can be simplified because this exception rarely happens\" | BLOCKED: Unhandled rare exceptions cause production outages. All error boundaries must be explicitly handled. |
| \"I tested the happy path and it works\" | BLOCKED: Happy path testing is insufficient. Boundary conditions, null inputs, and network failure modes must be verified. |
| \"The user didn't explicitly request error handling\" | BLOCKED: Error handling is a default quality requirement, not an optional feature. |

---

## Red Flags

- Starting to write code without any written requirements.
- Asking "should I just start building?" before clarifying what "done" means.
- Implementing features not mentioned in the spec or task list.
- Skipping the spec because "it's obvious what to build."

---

## Verification Gates

These gates are mandatory checkpoints. No phase may be skipped or reordered.

1. **Spec gate**: A spec document must exist and be approved before any implementation code is written. No exceptions for "simple" tasks — a two-line spec is fine, but it must exist.
2. **Plan-spec linkage**: The implementation plan must reference specific spec sections. Every plan item must trace back to a spec requirement. Orphaned plan items indicate scope creep.
3. **Task-plan mapping**: Tasks must map 1:1 to plan items. A task without a corresponding plan item is unauthorized work. A plan item without a corresponding task is unfinished planning.
4. **Test verification**: Implementation must pass all tests defined in tasks. No task is complete until its verification step (test command, build, manual check) has been executed and passed.

---

## Verification

Before proceeding to implementation, confirm:
- [ ] The spec covers all core areas.
- [ ] The human has reviewed and approved the spec.
- [ ] Success criteria are specific and testable.
- [ ] Boundaries (Always/Ask First/Never) are defined.
- [ ] The spec and plan are saved in the workspace.
