# Rule: Context Engineering & Attention Budget Preservation

This rule defines the **mandatory operational invariants** for managing the model's attention budget, preventing context degradation, and offloading bulky data across all sessions.

---

## 1. The Context Economy Invariant (Signal-to-Noise Ratio)

Context windows are constrained not merely by token limits, but by **attention mechanics**.
As context accumulates, models suffer from the **Attention U-Curve** (diminished recall in the middle of long contexts) and **attention competition** from noisy tool outputs.

Every token in the context window MUST be high-signal.

---

## 2. Mandatory Context Invariants

### 1. Filesystem Scratchpad Offloading Mandate (The 100-Line / 5KB Rule)
* **Trigger:** Any tool output, log dump, test output, or intermediate parsing result exceeding **100 lines** or **5 KB**.
* **Mandatory Action:**
  1. Offload the raw content to a file in `<appDataDir>/brain/<conversation_id>/scratch/` or `./scratch/` (e.g. `scratch/test_output_20260825.log`).
  2. In the active conversation context, output ONLY:
     - The absolute file path to the saved output.
     - A concise, high-signal summary (max 3-5 bullet points / <200 words).
  3. Retrieve specific details later via targeted tools (`grep_search`, `view_file` with `StartLine`/`EndLine` ranges) instead of re-dumping the file.

### 2. Attention Anchoring & U-Curve Defense (Lost-in-the-Middle Mitigation)
* Information placed in the middle of long prompts (>4K tokens) suffers a 10-40% reduction in recall accuracy.
* **Placement Protocol:**
  - **Top (Preamble):** Inviolable system rules, core personas, and input constraints.
  - **Bottom (Recency Anchor):** The exact active objective, acceptance criteria, active plan status, and immediate next action.
  - **Middle:** Compressed references, file links, and tool summaries.

### 3. Context Poisoning Circuit Breaker (Zero Error Compounding)
* Once a hallucinated fact, invalid tool assumption, or false hypothesis enters context, it compounds through self-reference.
* **Quarantine Protocol:**
  - When an assumption or hypothesis is proven wrong, the agent is **STRICTLY FORBIDDEN** from layering multiple conversational corrections on top of poisoned history.
  - The agent MUST explicitly flag the claim as `[INVALIDATED: <reason>]` and re-orient reasoning strictly from verified ground truth (`rules/zero-speculation.md`).

### 4. Semantic Drift & Task Isolation
* When switching between distinct tasks or subsystems within the same session:
  - Do NOT blend constraints from previous tasks into current reasoning.
  - Use explicit Markdown headings (`### Subtask: [Name]`) to establish clear cognitive boundaries.
  - If a task diverges completely, execute `rules/session-handoff.md` to initiate a clean session.

---

## 3. Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
| :--- | :--- |
| *"I'll just paste the entire 500-line test output into the chat response so the user can see it."* | **BLOCKED:** Violates the Scratchpad Offloading Mandate. Save to `scratch/` and provide a 3-bullet summary with path. |
| *"The context window is 1M tokens, so I don't need to worry about token bloat."* | **BLOCKED:** Attention degradation happens long before hard token limits. Noisy context weakens reasoning quality. |
| *"I made a mistake in the previous turn, so I'll write a 4-paragraph apology and explanation."* | **BLOCKED:** Apology filler pollutes the attention budget. State the invalidation cleanly: `[INVALIDATED: ...]`, state the verified fact, and proceed. |

---

## 4. Verification Checkpoint

Before generating a response with large payloads:
- [ ] Is raw tool output >100 lines offloaded to `scratch/`?
- [ ] Are active success criteria anchored at the end of the reasoning block?
- [ ] Are any previous incorrect assumptions quarantined with `[INVALIDATED]`?
