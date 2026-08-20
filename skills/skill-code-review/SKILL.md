---
name: skill-code-review
description: Systematic 5-axis code review framework for ensuring code quality, security, and performance.
---

# Overview

The 5-Axis Code Review Framework provides a systematic, thorough approach to code reviews. This skill enforces rigorous standards across correctness, readability, architecture, security, and performance to maintain a high-quality codebase. Use this framework before completing any user request, before committing code, or when explicitly asked to perform a code review.

# When to Use
- Pre-commit code reviews
- Pull request reviews
- Code quality audits
- Architecture reviews
- Security audits

# When NOT to Use
- Quick typo fixes in documentation
- Comment-only changes
- Purely automated formatting changes (e.g., Prettier/Black output)

# The 5-Axis Review Framework

When reviewing code, systematically evaluate the changes against these five axes:

## 1. Correctness
- **Logic Validation**: Does the code do what it's supposed to do?
- **Edge Cases**: Are boundary conditions and unusual inputs handled?
- **Error Handling**: Are errors caught and handled gracefully? Are error messages helpful?
- **Business Requirements**: Does the implementation align with the stated requirements?
- **Null/Undefined Handling**: Are null or undefined values checked before access?
- **Off-by-one Errors**: Are loops and boundaries strictly correct?
- **Race Conditions**: Is concurrent state mutation safely managed?

## 2. Readability
- **Code Organization**: Is the code logically structured and easy to follow?
- **Naming Conventions**: Are variables, functions, and classes named descriptively and consistently?
- **Self-Documenting Structure**: Can the code be understood without excessive comments?
- **Cognitive Complexity**: Is the logic too deeply nested? Can it be simplified?
- **Dead Code Elimination**: Has unused code been removed?

## 3. Architecture & SSOT
- **Single Source of Truth (SSOT)**: Does this code duplicate logic, schemas, endpoints, or utilities that already exist elsewhere in the repo?
- **DRY Adherence (Anti-Wheel-Reinvention)**: Are existing shared services, endpoints, and helpers reused rather than re-implemented?
- **In-Place Refactoring**: If an existing component/endpoint was inadequate, was it refactored in-place rather than bypassed with a parallel duplicate?
- **AST-Grep Structural Analysis (`ast-grep` MCP)**: Use `ast-grep` to search for anti-patterns across syntax trees (e.g. unhandled promises, missing React hook dependencies, unclosed connections, hardcoded credentials).
- **Component Boundaries**: Are responsibilities clearly separated?
- **Coupling & Cohesion**: Are related things grouped together? Are unrelated things decoupled?
- **Design Pattern Adherence**: Does the code use established patterns correctly?
- **Dependency Direction**: Do dependencies flow in the right direction (e.g., UI depends on Domain, not vice-versa)?
- **Single Responsibility**: Does each function/class do only one thing?

## 4. Security
- **OWASP Top 10**: Check for common vulnerabilities.
- **Input Sanitization**: Is user input validated and sanitized before use?
- **Secrets Leakage**: Are hardcoded secrets or credentials avoided?
- **SQL Injection**: Are parameterized queries used?
- **XSS & CSRF**: Are cross-site scripting and forgery prevented?
- **Auth/Authz Boundaries**: Are authentication and authorization checks enforced at appropriate boundaries?

## 5. Performance
- **Computational Complexity**: Analyze Big-O time and space complexity. Avoid unintentional O(N^2).
- **Memory Allocation**: Are there memory leaks or excessive object creation?
- **Unnecessary Re-renders**: (Frontend) Is the UI rendering efficiently?
- **N+1 Queries**: (Backend) Are database queries batched or optimized?
- **Async Efficiency**: Are asynchronous operations handled optimally without blocking?
- **Caching Opportunities**: Can results be cached to improve performance?

# Severity Labels for Feedback

When providing review feedback, categorize issues using these severity labels:

- `BLOCKER`: Must fix before merge. Security vulnerabilities, data loss risk, broken functionality.
- `FYI`: Informational observation. No action required.
- `NIT`: Minor style/preference issue. Fix if convenient.
- `OPTIONAL`: Suggested improvement. Author's discretion.

# Atomic Change Enforcement

Keep reviews focused and manageable:
- Target ~100 lines per review unit.
- Large changes must be decomposed into smaller, atomic commits or PRs.
- Reject monolith PRs that mix unrelated changes.

# Review Output Format

Provide your review findings structured by axis, using severity labels:

```markdown
## Code Review Summary

### 1. Correctness
- [BLOCKER] ...
- [NIT] ...

### 2. Readability
- [OPTIONAL] ...

### 3. Architecture
- [FYI] ...

### 4. Security
- [BLOCKER] ...

### 5. Performance
- [NIT] ...
```

# Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
|--------------|------------------|
| "This is a small change, it doesn't need a review" | **BLOCKED:** Small changes cause hidden regressions. All changes require review. |
| "The tests pass so the code is correct" | **BLOCKED:** Tests may not cover edge cases, security, or performance. Manual review is still required. |
| "I wrote this code so I know it's correct" | **BLOCKED:** Self-review is insufficient, apply the 5-axis framework anyway to catch blind spots. |
| "This is just a refactor, no behavior change" | **BLOCKED:** Refactors can introduce subtle behavioral changes, verify with tests and a rigorous review. |
| "The user didn't ask for security review" | **BLOCKED:** Security is a default quality requirement, not an opt-in feature. |
| "Performance optimization is premature here" | **BLOCKED:** Identifying O(n^2) or N+1 queries is not premature optimization, it is basic architectural correctness. |
| "The existing code already does it this way" | **BLOCKED:** Existing patterns may be wrong, don't propagate bad practices. |

# Red Flags
- Ignoring security warnings or skipping input sanitization.
- Merging PRs with `BLOCKER` comments unresolved.
- Reviews that only comment on style (missing correctness/security).
- Missing test coverage for new functionality.

# Verification Gates
- [ ] Have you evaluated the code against all 5 axes?
- [ ] Are all issues tagged with a severity label (`BLOCKER`, `FYI`, `NIT`, `OPTIONAL`)?
- [ ] Are there any unresolved `BLOCKER` issues?
- [ ] Is the change atomic (~100 lines)?
