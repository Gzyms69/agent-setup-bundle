---
name: skill-graph-analytics
description: Expert guidance for Graph Databases (Neo4j), topology analysis, and Graph Data Science (GDS). Use when Gemini CLI needs to manage Neo4j instances, perform pathfinding/similarity analysis, or handle large-scale knowledge graph ingestion.
---

# Graph Analytics & Topology Skill

This skill provides specialized protocols for high-performance graph database operations.

## 1. The GDS Mandate
*   **Rule:** For any graph algorithm (Similarity, Centrality, Pathfinding), you MUST first check if a `gds.*` procedure exists.
*   **Anti-Reinvention:** Never write multi-hop pathfinding or set-similarity math in raw Cypher if GDS is available.
*   **Verification:** Run `CALL gds.list()` and `CALL apoc.help('keyword')` before coding new logic.

## 2. Memory & Performance
*   **Off-Heap Awareness:** GDS graphs live in **Off-Heap Memory**. Allocating 100% of RAM to the JVM Heap will cause OOM.
*   **Cleanup Mandate:** Any script/test that projects a graph (`gds.graph.project`) MUST explicitly drop it (`gds.graph.drop`) upon completion.
*   **Sampling:** Use topological neighbors sampling to minimize Neo4j memory footprint when resolved entity details are needed.

## 3. Knowledge Graph Architecture
*   **Hybrid Storage:** Store topology (links/QIDs) in Neo4j and heavy metadata (article content/metrics) in SQLite/FTS5 for sub-millisecond retrieval.
*   **JIT Configuration:** Use Just-In-Time (JIT) rules for dynamic schema generation when dealing with multi-language data sources.
*   **Scaling:** Prefer language-isolated Neo4j containers federated through a unified FastAPI bridge.
