---
name: doubt-driven-development
description: ADVERSARIAL VERIFICATION GATE. Subjects architectural decisions, migrations, and code changes to a fresh-context adversarial review to challenge false confidence. MUST ACTIVATE when correctness matters more than speed, when stakes are high (security, irreversible ops, core refactors), or before asserting non-obvious technical facts.
---

# Doubt-Driven Development

## Overview

A confident answer is not a correct one. Long sessions accumulate context that quietly turns assumptions into "facts." Doubt-driven development is the discipline of materializing a fresh-context reviewer — biased to **disprove**, not approve — before any non-trivial output stands.

This is an in-flight posture: non-trivial decisions get cross-examined while course-correction is still cheap.

## When to Use

A decision is **non-trivial** when at least one of these is true:
- It introduces or modifies branching logic.
- It crosses a module or service boundary.
- It asserts a property the compiler cannot verify (idempotence, ordering, invariants).
- Its blast radius is high (production deploy, DB migration, public API change).
- Working in code you don't fully understand.

**When NOT to use:**
- Mechanical operations (renaming, formatting, file moves).
- Following a clear, unambiguous user instruction.
- Pure tooling operations (running tests, listing files).

---

## The Process

Copy this checklist when applying the skill:

```
Doubt cycle:
- [ ] Step 1: CLAIM — write the claim + why-it-matters
- [ ] Step 2: EXTRACT — isolate artifact + contract, strip reasoning
- [ ] Step 3: DOUBT — invoke fresh-context reviewer with adversarial prompt
- [ ] Step 4: RECONCILE — classify every finding against the artifact text
- [ ] Step 5: STOP — stop when findings are trivial, or after 3 loops
```

### Step 1: CLAIM — Surface what stands

Name the decision in two or three lines:
```
CLAIM: "The new database transaction guarantees no orphaned order items."
WHY THIS MATTERS: Orphans cause billing bugs that are hard to correct later.
```

### Step 2: EXTRACT — Smallest reviewable unit
A reviewer needs the **artifact** (the code snippet or diff) and the **contract** (what it must do), NOT your journey or reasoning. Strip explanations to prevent confirmation bias.

### Step 3: DOUBT — Adversarial Review
Invoke a fresh-context check. The review prompt **must be adversarial**:

```
Adversarial review. Find what is wrong with this artifact.
Assume the author is overconfident. Look for:
- Unstated assumptions
- Edge cases not handled
- Hidden coupling or shared state
- Ways the contract could be violated
- Failure modes under unexpected input

Do NOT validate. Do NOT summarize. Find issues, or state
explicitly that you cannot find any after thorough examination.

ARTIFACT: <paste artifact>
CONTRACT: <paste contract>
```
*Note: Do not pass the CLAIM to the reviewer, only the ARTIFACT and CONTRACT.*

#### Cross-Model Escalation (Interactive Sessions)
A single model shares blind spots. In interactive sessions, after completing the single-model review, explicitly ask the user:
> *"Single-model review complete. Want a cross-model second opinion? Options: Gemini CLI, Codex CLI, manual external review, or skip."*
If the user approves, write the prompt to a temp file and pipe it to the target CLI to prevent shell injections.

### Step 4: RECONCILE — Fold findings back
Read the artifact text against each finding. Classify in this order:
1. **Contract misread:** The reviewer flagged something because the CONTRACT was unclear. Fix the contract and re-loop.
2. **Valid + Actionable:** A real issue. Correct the artifact and re-loop.
3. **Valid trade-off:** A real issue, but fixing it costs more than accepting it. Document the trade-off.
4. **Noise:** The reviewer flagged something correct that they misread.

### Step 5: STOP — Bounded loop
Stop when:
- Iterations return only trivial or already-considered findings.
- 3 cycles are completed (if issues persist, escalate to the user, do not grind further).
- User explicitly overrides and says "ship it".

---

## Red Flags

- Spawning reviews for trivial edits (renames, lints).
- Accepting reviewer output as authoritative without verifying the artifact.
- Looping >3 cycles without escalating to the user.
- Prompting with "is this good?" instead of "find issues".
- Passing the CLAIM or your reasoning to the reviewer.
- Accepting "this change is simple/small" as a reason to skip the doubt process. Simple changes in critical paths still need adversarial review.
- Using the reviewer to validate rather than challenge — framing the review as "confirm this is correct" instead of "find what's wrong." Validation bias defeats the purpose of the doubt cycle.
- Skipping the doubt process for "obvious" fixes. Obvious is a confidence signal, not a correctness signal. The fixes that cause the most damage are the ones that looked obvious.

---

## Verification

Before finishing the doubt cycle, confirm:
- [ ] The claim and its impact were explicitly documented.
- [ ] Reviewer received ARTIFACT + CONTRACT without prior explanations.
- [ ] Adversarial prompt was used.
- [ ] Findings were reconciled and classified.
- [ ] Stop condition was met within 3 cycles.

### Verification Gates

These gates are mandatory. A doubt cycle is not complete until all are satisfied.

1. **Doubt process log preservation**: The full doubt cycle (CLAIM, EXTRACT, DOUBT, RECONCILE, STOP) must be preserved in the conversation or session log. If the log is lost, the doubt cycle must be re-run. No "I already checked this" claims without a traceable record.
2. **Issue resolution tracking**: All issues identified by the reviewer must be either (a) fixed in the artifact, or (b) explicitly accepted as a known trade-off with documented rationale. No silent dismissals. Every finding gets a disposition: fixed, accepted-with-rationale, or classified-as-noise-because.
3. **Cross-model escalation for high stakes**: For decisions meeting the high-stakes threshold (production deploy, DB migration, public API change, security-sensitive logic), cross-model review must be attempted — not just offered. If the user declines cross-model review, document that the escalation was offered and declined.
