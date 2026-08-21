---
name: skill-qa-engineer
description: MANDATORY PHASE 3 QA GATE for test execution, Test-Driven Development (TDD Red-Green), TypeScript compilation checks (npx tsc --noEmit), and dependency management. MUST ACTIVATE when writing tests, modifying code, implementing new features, or fixing bugs.
---

# Quality Assurance & Testing Skill

This skill enforces code reliability, correctness, structural consistency, and testing discipline through ustrukturyzowane workflow and package standards.

---

## 1. Tooling & Code Style Standards

Enforce strict linting and formatting before commits. Do not skip validation checks:

*   **JS/TS:** ESLint + Prettier. Run `npm run lint` and `npm run format` locally.
*   **Python:** **Ruff** (ultra-fast linter and formatter, replacing black/isort/flake8).
*   **Go:** `gofmt` + `golint`.
*   **Configuration Guard:** Validate all local environment configurations (`.env`) via schemas (Zod or Pydantic) on application startup to fail fast on invalid configurations.

---

## 2. Dependency Management & Security

*   **Node.js:** Prefer `npm` or `pnpm`. Always commit `package-lock.json` or `pnpm-lock.yaml` to ensure lockfile synchronization.
*   **Python:** Use **`uv`** with `pyproject.toml` or `requirements.txt` for high-speed package management and compilation.
*   **Security Auditing:** Regularly run `npm audit` or `pip-audit` to detect vulnerabilities. Never commit plain-text credentials, API keys, or JWT secrets.

---

## 3. The Testing Pyramid

Establish clear coverage levels based on business risk:

1.  **Unit Tests (Jest/Vitest/Pytest):** Verify individual logic paths, helper utilities, and edge conditions in complete isolation. High speed, high frequency.
2.  **Integration Tests:** Validate interfaces and operations crossing borders (e.g., API controller querying database tables or calling microservices).
3.  **E2E Tests (Playwright/Cypress):** Test complete user journeys inside real, headless browsers (e.g., navigation, payment checkout flow, hydration validity).

---

## 4. Test-Driven Development (TDD) Protocol

Before writing any implementation code for a new feature or bugfix, write the verification tests. Follow the Red-Green-Refactor loop:

```
 WRITE TEST (RED) ──→ IMPLEMENT CODE (GREEN) ──→ REFACTOR (CLEAN)
        │                       │                       │
        ▼                       ▼                       ▼
 Confirm that test        Write the minimal       Optimize structure,
 fails as expected       code to pass test       clean up redundancy
```

### Phase 1: RED (Write the Test First)
*   Write a unit or integration test asserting the desired behavior.
*   **Run the test to confirm it fails.** A test that passes before implementing code is either testing nothing or relying on incorrect assumptions.

### Phase 2: GREEN (Write Minimal Code)
*   Write the simplest, most direct implementation that makes the test pass.
*   Do not write anticipatory code or add features outside the immediate test contract.

### Phase 3: REFACTOR (Polish and Clean)
*   Clean up the implementation: remove duplication, rename variables for clarity, structure module boundaries, and run formatting tools.
*   **Re-run all tests** to ensure no regressions were introduced.

---

## 5. Web Testing & Browser Diagnostics (DevTools)

When verifying browser behavior or auditing frontend interfaces, follow this diagnostic checklist using DevTools or automated scripts:

### Console & Network Checks
*   **Console Audit:** Open the console and verify that no error messages, missing source maps, or warning notifications are output during page navigation.
*   **Network Payload:** Inspect the Network tab. Verify asset status codes (all structural files must return 200/304). Check bundle weight: confirm heavy dynamic imports are split.

### Render & Layout Shifts (CLS)
*   **Layout Shift Check:** Enable "Layout Shift Regions" in DevTools (Rendering tab). Verify that no layouts shift or jump during hydration or lazy-loading of media placeholders.
*   **Core Web Vitals Triage:**
    *   LCP (Largest Contentful Paint) must be ≤ 2.5s.
    *   INP (Interaction to Next Paint) must be ≤ 200ms.
    *   CLS (Cumulative Layout Shift) must be ≤ 0.1.

### Accessibility (WCAG Verification)
*   **Keyboard Focus Test:** Press `Tab` to navigate through the entire page. Ensure active elements show high-contrast focus rings and that focus does not get trapped.
*   **DOM Headings Check:** Inspect the elements tree. Ensure there is exactly one `h1` element per page and that nesting levels follow order (`h1` -> `h2` -> `h3`).

---

## 6. Verification Mandate

Never assume code is correct because it compiles:
*   **SSOT & DRY Auditing:** Verify that new tests and application code reuse existing test fixtures, mock servers, utility functions, and API endpoints rather than creating duplicate helper modules.
*   **Side Effect Validation:** Check database records, logs, or filesystem states directly after mutations to verify side effects match assertions.
*   **Static Type Checks:** Run `npx tsc --noEmit` after modifying TS/TSX files.
*   **Lint Compliance:** Ensure formatters and linters pass cleanly before flagging a task as complete.
