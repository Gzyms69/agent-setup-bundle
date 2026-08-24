# Rule: Session Handoff & Continuation Protocol

This rule defines the operational protocol for **lossless context transfer (Zero Context Loss)** between consecutive AI pair-programming sessions.

---

## 1. The Lean SSOT Invariant (Anti-Context-Flooding)

* **ABSOLUTE BAN ON CHAT/SESSION DUMPING:** Agents are **STRICTLY FORBIDDEN** from polluting persistent architecture and instruction files (`GEMINI.md`, `CLAUDE.md`, `AGENTS.md`) with daily conversational logs, session narratives, or transcript excerpts.
* **SEPARATION OF CONCERNS:**
  - `AGENTS.md` / `GEMINI.md` / `CLAUDE.md`: Pure, high-signal Source of Truth (SSOT) defining tech stack architecture, executable CLI commands, and inviolable guardrails.
  - `NEXT_SESSION_PLAN.md`: Active, tactical task roadmap for the upcoming session.
  - `DEVLOG.md` (Optional): Chronological devlog if explicitly requested by project conventions.
  - **Handoff Prompt**: Interactive bootstrap prompt generated in the chat response for the user to copy-paste.

---

## 2. Trigger Conditions

This protocol activates automatically whenever:
1. **User Deferral Signal:** The user indicates that work should pause, split, or resume in a new session (e.g. *"to w kolejnej sesji"*, *"kontynuujemy w nowej sesji"*, *"dokończymy następnym razem"*, *"to na inną sesję"*, *"zapisz handoff"*).
2. **Milestone Completion:** A major development milestone or complex multi-phase task is completed, and the next phase should begin with a clean context.

---

## 3. Mandatory Agent Handoff Workflow

Before concluding the session, the agent MUST:
1. **Update the Active Task Plan (`NEXT_SESSION_PLAN.md`):** Document the exact current state, completed items, and a step-by-step roadmap for the next session.
2. **Run Verification Gates:** Execute the repository test suite to confirm a clean, passing baseline.
3. **Emit the Standardized Handoff Prompt:** Present a self-contained markdown code block in the chat response that bootstraps the incoming agent.

---

## 4. Standardized Handoff Prompt Specification

Every generated Handoff Prompt MUST contain:
1. **Planning Mode Directive:** Begins with `/plan`.
2. **Explicit Skill Invocations:** Directs the incoming agent to load relevant domain skills (e.g. `skill-codebase-onboarding`, `skill-qa-engineer`, `spec-driven-development`) before file exploration.
3. **SSOT File Anchors:** Explicit absolute or repository-relative paths to files the new agent must read first (`NEXT_SESSION_PLAN.md`, `portals.yml`, etc.).
4. **Current Baseline State:** 1-2 sentence summary of verified functionality and test results (e.g. `1584/1584 tests passing`).
5. **Codified Action Items:** Numbered, unambiguous task list for the incoming session.
6. **Pre-Flight Verification Command:** The exact test/check command to run before touching code.
