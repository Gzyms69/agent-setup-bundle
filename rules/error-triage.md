# Error Triage Protocol

Upon encountering any failed command or error:

1. FIRST: Check project documentation (README.md, CONTRIBUTING.md, docs/)
   for known issues and prescribed solutions.
2. SECOND: Search the web for the EXACT error message or error code.
3. THIRD: If not found in steps 1-2, begin systematic diagnostic debugging.
4. NEVER skip steps 1-2 and jump straight to speculative fixes.

## Trace and Verify Protocol

When the user asks how the codebase works:

1. Physically trace code paths -- do not guess from memory.
2. Follow imports, function calls, and data flow through actual files.
3. Verify every claim by reading the actual source code.
4. Show file:line references for every assertion about the codebase.
5. If you cannot trace the path: say so explicitly, do not fabricate.
