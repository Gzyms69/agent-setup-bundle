# UNIVERSAL CODING CONVENTIONS FOR SUB-WORKERS (AIDER & CHINESE LLMs)

1. **NO LAZY CODING OR PLACEHOLDERS:**
   - NEVER output comments like `// ... existing code ...`, `/* TODO */`, or `# rest of file unchanged`.
   - Provide complete, fully-formed code blocks within diff replacements.

2. **SINGLE SOURCE OF TRUTH (SSOT) & PRESERVATION:**
   - Preserve all existing imports, docstrings, type annotations, and comments unless explicitly instructed to refactor them.
   - Never remove existing functionality to fix a compiler error.

3. **TYPE SAFETY & STRICT COMPLIANCE:**
   - For TypeScript: Ensure strict null checks and full interface coverage. Do not use `any` when specific types exist.
   - For Python: Use type hints (`from typing import ...` or Python 3.10+ union types) and Pydantic models where applicable.

4. **TDD & TESTING INTEGRITY:**
   - When generating unit tests, test edge cases, exception handling, and boundary values.
   - Mock external network I/O, database connections, and disk mutations.

5. **CLEAN DIFF FORMAT:**
   - Emit valid SEARCH/REPLACE diff blocks strictly conforming to Aider's diff grammar.
   - Match indentation and line endings precisely.
