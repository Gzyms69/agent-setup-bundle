# Subagent Economy Rules

Token budget is finite. Every subagent costs tokens.

## Model Selection Matrix

| Task type | Model | Examples |
|-----------|-------|---------|
| Read files, list directories | flash_lite | Reading SKILL.md, listing dir contents |
| Web search, docs lookup | flash | Searching for error codes, reading URLs |
| Simple analysis, summarization | flash | Comparing two files, extracting patterns |
| Complex reasoning, planning | pro | Architecture decisions, multi-file refactors |
| Same complexity as parent task | inherit | Delegating part of current complex task |

## Rules

1. PREFER doing simple work yourself instead of spawning subagents.
2. If task requires < 3 tool calls: do it yourself.
3. Batch related lookups into ONE subagent instead of many.
4. NEVER use inherit/pro for file reading or web search.
5. Kill idle subagents promptly after receiving results.
6. When spawning multiple subagents: maximum 3 concurrent unless justified.
7. Always specify Model explicitly -- never rely on defaults for subagents.
