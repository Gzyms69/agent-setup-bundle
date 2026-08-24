# Subagent Economy & Swarm Coordination Rules

Token budget is finite. Every subagent costs tokens and introduces coordination overhead.

---

## 1. Model Selection Matrix

| Task Type | Model | Typical Actions |
| :--- | :--- | :--- |
| **I/O & File Reading** | `flash_lite` | Reading SKILL.md, listing directory contents, fast grep parsing |
| **Research & Analysis** | `flash` | Web search, error triage, documentation lookups, simple diff comparison |
| **Complex Reasoning** | `pro` | Deep architectural decisions, multi-file refactors, security threat modeling |
| **Task Delegation** | `inherit` | Delegating an equivalent-complexity subproblem from parent task |

---

## 2. Core Subagent Mandates

1. **Subagent Economy First:** PREFER doing simple work yourself instead of spawning subagents. If a task requires < 3 tool calls: do it yourself inline.
2. **Batching:** Batch related lookups into ONE subagent instead of launching multiple micro-agents.
3. **No Model Waste:** NEVER use `inherit` or `pro` for file reading or web search.
4. **Prompt Termination:** Kill idle subagents promptly after receiving results (`manage_subagents kill`).
5. **Concurrency Limit:** Maximum 3 concurrent subagents unless explicitly justified by an independent parallel DAG branch.
6. **Explicit Model Flag:** Always specify `Model` explicitly in `invoke_subagent` — never rely on defaults.

---

## 3. Swarm Coordination & Context Protection Protocols

### 7. Zero Context Bleed Mandate
* Subagents are **STRICTLY FORBIDDEN** from dumping their raw tool execution history, intermediate file reading steps, or full conversational turns back to the Master Agent.
* Communication back to the parent (via final task completion or `send_message`) MUST follow a strict, structured output format:
  - `Status`: `SUCCESS` | `FAILED` | `BLOCKED`
  - `Findings / Changes`: 3-5 bullet point summary
  - `Artifacts / Modified Files`: Explicit file paths
  - `Blockers / Decisions`: Any unresolved questions

### 8. Workspace Isolation Protocol
* When subagents modify files, they MUST operate in isolated directories or worktrees (`workspace/agents/<agent_id>/` or `Workspace: share` / `Workspace: branch`) to prevent write collisions and dirty tree state.
* Subagents must not modify shared root config files without explicit Master Agent coordination.

### 9. Barrier Synchronization (Task Dependencies)
* Independent tasks (e.g. searching 3 distinct documentation sources) may run concurrently.
* Dependent tasks (e.g. implementing code based on an architectural spec, or running tests after modifications) MUST be gated by a **synchronization barrier** — the parent agent must verify the upstream dependency completed successfully before triggering the downstream subagent.

### 10. Prevention of the "Telephone Game"
* When a subagent produces a final, user-facing artifact or report that is complete, the Master Agent should directly present or link the artifact rather than lossily paraphrasing and distorting critical technical details.
