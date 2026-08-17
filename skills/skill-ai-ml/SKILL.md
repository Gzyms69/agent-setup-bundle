---
name: skill-ai-ml
description: Guidance for AI/ML development, model integration, and agentic frameworks. Use when Gemini CLI needs to work with LLMs (Ollama, Vertex AI, Gemini), integrate vector search (Redis, ChromaDB), or build agentic systems.
---

# AI & Machine Learning Skill

This skill provides patterns for building AI-powered applications, from local prototyping to cloud-scale inference and agentic workflows.

## Overview
AI integration requires balancing capability with cost, latency, and security. This skill defines the standards for leveraging LLMs, vector databases, and agent frameworks responsibly and effectively.

## When to Use
- Integrating Gemini or other LLMs via API.
- Building Retrieval-Augmented Generation (RAG) systems.
- Designing multi-agent systems and tool-use workflows.
- Deploying ML models for inference.

## When NOT to Use
- Traditional statistical modeling (use data-science skill).
- Standard web application backends without AI components.

## 1. Gemini API Cheatsheet
*   **Model Selection:**
    *   *Gemini Flash:* Use for high-volume, low-latency, and cost-sensitive tasks (routing, basic extraction).
    *   *Gemini Pro:* Use for complex reasoning, long-context analysis, and generation tasks.
    *   *Gemini Ultra:* Reserve for the most demanding, highly complex cognitive tasks.
*   **Token Counting:** Always count tokens before sending requests to manage context limits and estimate costs accurately.
*   **Safety Settings:** Configure explicit safety thresholds for harassment, hate speech, and dangerous content based on application context.
*   **System Instructions:** Use robust system prompts to define persona, rules, and output formats.
*   **Function Calling:** Strongly type arguments using OpenAPI schemas to enforce structured outputs.
*   **Grounding:** Use Google Search grounding to reduce hallucinations for factual queries.

## 2. Vertex AI Integration
*   **Model Deployment:** Deploy models to Vertex AI Endpoints for managed, scalable online inference.
*   **Endpoint Management:** Implement traffic splitting for A/B testing new model versions.
*   **Batch Prediction:** Use Vertex AI Batch Prediction for asynchronous, large-scale inference jobs.
*   **Custom Training:** Leverage Vertex AI Custom Jobs for training proprietary models with hyperparameter tuning.

## 3. Local Development
*   **Ollama Setup:** Use Ollama for rapid, cost-free local prototyping with open-weights models (e.g., Llama 3, Mistral).
*   **Model Pulling:** Automate model fetching in setup scripts (`ollama pull <model>`).
*   **API Compatibility Layer:** Expose local models through an OpenAI-compatible API to allow seamless switching between local and cloud providers.

## 4. Vector Search Integration
*   **ChromaDB Setup:** Use Chroma for lightweight, local vector storage during development and prototyping.
*   **Redis Vector Search:** Transition to Redis (or Vertex Vector Search) for low-latency, production-scale similarity search.
*   **Embedding Generation:** Standardize on a robust embedding model (e.g., text-embedding-004) and batch requests for efficiency.
*   **Similarity Search Patterns:** Use Hybrid Search (dense + sparse vectors) and pre-filtering (metadata filtering) to improve relevance.
*   **Index Management:** Monitor index size and rebuild indexes periodically to maintain recall performance.

## 5. Agent Framework Patterns
*   **Tool Definition:** Design tools with singular, specific purposes and comprehensive descriptions for the LLM to understand usage.
*   **Chain-of-Thought / ReAct:** Prompt agents to explicitly reason ("Thought: ... Action: ...") before executing tools to improve reliability.
*   **Multi-Agent Orchestration:** Decompose complex tasks into specialized sub-agents with clear communication protocols.
*   **Memory Management:** Implement bounded memory (sliding window, summarization) to prevent context window exhaustion.

## 6. Performance & Cost
*   **Token Budgeting:** Define strict limits on input and output tokens per user/session.
*   **Caching Strategies:** Implement semantic caching (e.g., Redis) to return pre-computed responses for similar queries.
*   **Batching Requests:** Group multiple small inference requests to maximize throughput and minimize latency.
*   **Model Size Tradeoffs:** Always benchmark the smallest adequate model for the task before scaling up.

## 7. Security
*   **API Key Management:** NEVER hardcode API keys. Use Secret Manager and inject via environment variables. Use Workload Identity where possible.
*   **PII Filtering:** Implement pre-processing pipelines to scrub Personally Identifiable Information before sending data to external APIs.
*   **Prompt Injection Defense:** Sanitize user inputs, use parameterization, and employ explicit instruction delimiters to mitigate injection attacks.
*   **Output Validation:** Treat LLM outputs as untrusted. Validate structure, types, and content before executing downstream actions.

## 8. Anti-Rationalization Table

| Rationalization | Correction |
| :--- | :--- |
| "The largest model will give the best results" | **BLOCKED:** Start with the smallest adequate model to save costs and reduce latency. Only scale up when evaluation metrics demand it. |
| "I don't need to validate LLM output" | **BLOCKED:** LLM outputs require strict validation. Hallucinations and malformed JSON are guaranteed at scale. |
| "Prompt injection isn't a concern for internal tools" | **BLOCKED:** Internal tools process untrusted external data. Injection vulnerabilities apply everywhere. |
| "I'll add rate limiting later" | **BLOCKED:** Unbounded API calls can lead to massive runaway costs in minutes. Implement budgets immediately. |
| "The API key in the code is temporary" | **BLOCKED:** Never commit API keys. Use environment variables and secret managers from day one. |

## 9. Red Flags
*   Trusting LLM-generated code or commands without a sandbox or human-in-the-loop.
*   Failing to handle API rate limits and timeouts gracefully.
*   Sending raw user input directly to the system prompt without sanitization.
*   Lack of observability into token usage and latency.

## 10. Verification Gates
1.  **Is the LLM output validated against a strict schema (e.g., Pydantic) before use?**
2.  **Are API keys securely managed and excluded from source control?**
3.  **Is there a fallback mechanism for when the model API is unavailable or returns an error?**
4.  **Are prompts version-controlled and evaluated against a benchmark dataset?**
