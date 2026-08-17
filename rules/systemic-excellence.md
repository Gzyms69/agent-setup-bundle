# Systemic Excellence

FORBIDDEN from applying symptomatic patches.

When debugging:
1. Identify the lowest possible level of failure:
   Kernel > Driver > OS Config > Runtime > Framework > Application Code
2. Implement the fix AT THAT LEVEL, not higher.
3. Never change UI code to fix a build error.
4. Never change application logic to fix a configuration error.
5. Never mask errors with try/catch without fixing the underlying cause.
6. Never disable warnings/linting to make errors "go away".
7. Never add defensive code around a bug instead of fixing the bug.

Verification: After applying any fix, re-run the ORIGINAL failing operation
to confirm the root cause is actually resolved -- not just masked.

## Single Source of Truth & Anti-Duplication (SSOT & DRY)
1. Never invent parallel functions, endpoints, or utilities when an implementation exists.
2. Before writing new code, search the codebase (`grep_search`, `list_dir`) for existing abstractions.
3. If an existing utility/endpoint lacks a feature or contains a bug: refactor and extend it IN PLACE with backwards compatibility.
4. Maintain authoritative SSOT files for data contracts, schemas, and diagnostics.
