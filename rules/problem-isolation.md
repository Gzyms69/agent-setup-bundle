# Strict Problem Isolation

If a specific bug is reported in a single file, service, or environment:

1. Solve ONLY that problem.
2. Do NOT change global OS state for a local bug.
3. Do NOT propose rewriting to another technology.
4. Do NOT jump to other threads, side projects, or unrelated issues.
5. Maintain 100% focus on the current, isolated task.
6. Fix at the LOWEST possible level:
   Kernel > Driver > OS Config > Runtime > Framework > Application Code
7. FORBIDDEN from "while we're at it" scope expansion without user consent.
8. If fixing the isolated problem reveals a deeper systemic issue:
   document it, report it, but do NOT fix it without explicit approval.
