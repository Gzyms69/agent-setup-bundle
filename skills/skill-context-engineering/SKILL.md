---
name: skill-context-engineering
description: Production context engineering, attention budget curation, Anchored Iterative Summarization, Artifact Trail Tracking, tokens-per-task optimization, and MemPalace context compaction. MUST ACTIVATE for long-running sessions, multi-step refactors, high token load, or when diagnosing attention degradation (lost-in-the-middle, context poisoning).
---

# Context Engineering Skill

Context engineering is the science of curating the language model's attention window. As conversational trajectories grow, models exhibit predictable degradation patterns: the **Attention U-Curve** (diminished recall for mid-context tokens), **attention scarcity**, and **context poisoning**.

This skill provides deterministic protocols for compressing context, preserving artifact integrity, and maximizing the signal-to-noise ratio in long-horizon coding sessions.

---

## When to Activate

Activate this skill when:
- Sessions extend beyond 10+ turns or involve massive codebase exploration.
- Agent begins "forgetting" files it previously modified or decisions made earlier.
- Diagnosing attention failures, hallucinations, or context poisoning.
- Designing compaction and handoff summaries for multi-phase tasks.
- Integrating ephemeral scratchpad outputs with persistent semantic memory (MemPalace).

Do NOT activate for:
- Simple, single-turn query answering or typo fixes.
- Low-level database indexing (use `skill-backend-architect`).

---

## 1. The Attention U-Curve & Placement Strategy

Models attend strongly to the beginning (system instructions, initial prompt) and the end (recent turns, immediate directives) of their context window. Information placed in the middle experiences a 10% to 40% reduction in retrieval fidelity.

```
High Attention │ █                                         █
               │ ██                                       ██
               │ ███                                     ███
               │ ████                                   ████
Low Attention  │ ███████████████████████████████████████████
               └─────────────────────────────────────────────►
                 Beginning            Middle              End
               (Rules/Persona)   (References/Logs)     (Active Task)
```

### Placement Protocol:
1. **Top (System Prompt / Static Rules):** Core invariants, safety guardrails, tool schemas.
2. **Middle (Dynamic Overflow):** Reference file contents, search findings, and scratchpad pointers.
3. **Bottom (Active Anchor):** Active task goal, acceptance criteria, current step checklist, and explicit next command.

---

## 2. Anchored Iterative Summarization (Compression Schema)

When compressing long conversation histories, avoid freeform summaries that silently discard critical identifiers. Maintain an **Anchored Structured Summary** populated using this mandatory schema:

```markdown
# Session State Summary

## 1. Active Intent & Scope
- Objective: [Clear 1-sentence goal]
- Acceptance Criteria: [Testable conditions of completion]

## 2. Artifact Trail (Strict File Tracking)
- Created Files:
  - `path/to/new_file.ts` (Exports: `UserService`, `AuthMiddleware`)
- Modified Files:
  - `path/to/existing.py` (Functions changed: `validate_token`, `refresh_session`)
- Inspected / Read-Only Files:
  - `path/to/config.yml` (Verified schema version 2.4)

## 3. Decisions & Invariant Contracts
- [DECISION] Using Redis connection pool (max 20 connections) instead of per-request clients.
- [INVALIDATED] Removed initial hypothesis about memory leak in worker thread; root cause was unclosed HTTP client.

## 4. Current State & Verification Baseline
- Tests: 42 passed, 0 failed.
- Build: Clean TypeScript compilation (`npx tsc --noEmit` passed).

## 5. Next Immediate Actions
1. Implement integration test for refresh endpoint.
2. Trigger 5-axis review before commit.
```

---

## 3. Optimizing Tokens-Per-Task (Anti-Re-Fetching)

Measure efficiency by **Tokens-Per-Task** (total tokens needed to complete the overall objective), NOT tokens-per-turn.
* Overly aggressive compression that strips full file paths or specific function names causes the model to re-read files repeatedly, multiplying token costs.
* **Preserve Specific Identifiers:** Always preserve exact file paths, exported symbol names, error codes, and line numbers across compression cycles.

---

## 4. Context Poisoning Circuit Breaker

When an invalid assumption or tool hallucination enters context, it compounds through self-reference.
1. **Quarantine:** Immediately label the invalid assumption with `[INVALIDATED: Reason]`.
2. **Re-anchoring:** Do NOT stack multiple conversational retries. Re-read the source of truth file (`view_file`) and restart the reasoning step from verified baseline data.

---

## 5. Persistent Memory Sync (MemPalace Protocol)

For knowledge that must survive across separate sessions and project restarts:
1. Extract architectural decisions, learned conventions, and domain facts.
2. File memories into MemPalace using `mempalace_kg_add` or `mempalace_diary_write`.
3. Invalidate superseded facts with `mempalace_kg_invalidate` to prevent knowledge graph clash.

---

## 6. Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
| :--- | :--- |
| *"I'll just write a vague 2-line summary like 'we worked on auth'."* | **BLOCKED:** Omission of the Artifact Trail causes expensive re-exploration loops. Follow the 5-section schema. |
| *"I don't need to track which files were read."* | **BLOCKED:** Untracked files cause duplicate reading operations and wasted tool calls. |
| *"The model has a massive context window so compaction is unnecessary."* | **BLOCKED:** Performance degrades smoothly along the Attention U-Curve. Compact context keeps reasoning sharp. |

---

## 7. Verification Gates

- [ ] Does the context summary include the full Artifact Trail (created, modified, read files)?
- [ ] Are active acceptance criteria positioned at the bottom of the prompt/reasoning anchor?
- [ ] Have all discarded hypotheses been marked as `[INVALIDATED]`?
- [ ] Are cross-session learnings synchronized to MemPalace?
