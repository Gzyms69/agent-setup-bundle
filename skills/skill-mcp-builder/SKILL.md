---
name: skill-mcp-builder
description: Architecture, development, debugging, and testing of Model Context Protocol (MCP) servers using FastMCP (Python) and the TypeScript MCP SDK. MUST ACTIVATE when creating, modifying, extending, or troubleshooting custom MCP servers, stdio/SSE transports, tool schemas, or resource providers.
---

# Model Context Protocol (MCP) Builder Skill

This skill provides architectural patterns, implementation standards, and debugging workflows for building high-performance, secure, and developer-friendly **Model Context Protocol (MCP)** servers.

The quality of an MCP server is measured by how seamlessly and reliably LLMs can discover, call, and recover from tool errors.

---

## When to Activate

Activate this skill when:
- Creating a new custom MCP server to connect the agent to external APIs, databases, or local tools.
- Refactoring, extending, or optimizing existing MCP servers.
- Debugging MCP connection failures, serialization issues, or schema validation errors.
- Designing tool signatures, resource templates, or prompt definitions.

---

## 1. Stack Selection & Architecture

### Recommended Frameworks:
* **TypeScript SDK (`@modelcontextprotocol/sdk`):** Recommended for web services, Node.js tooling, and frontend integrations. Offers native type safety with Zod schemas.
* **Python FastMCP (`fastmcp` / `mcp`):** Recommended for data science, AI workflows, systems automation, and rapid prototyping with Pydantic models.

### Transport Protocols:
| Transport | Best For | Characteristics |
| :--- | :--- | :--- |
| **`stdio`** | Local CLI tools & desktop agents | Simple, process-bound, lowest latency, zero network exposure. |
| **Streamable HTTP / SSE** | Distributed / remote microservices | Stateless JSON requests, horizontally scalable, multi-client support. |

---

## 2. Tool Design & Schema Engineering

### Tool Naming & Discoverability
* **Action-Oriented Prefixes:** Prefix tool names consistently with their domain (e.g., `postgres_query`, `github_create_issue`, `docker_list_containers`).
* **Concise, Precise Descriptions:** Explain both *what* the tool does and *under what exact conditions* the model should call it.

### Typed Schemas with Strict Boundaries
Always validate arguments at the server boundary using **Zod** (TypeScript) or **Pydantic** (Python):

```typescript
// TypeScript MCP Tool Definition (Zod)
server.tool(
  'deploy_service',
  'Deploys a containerized service to the target environment.',
  {
    serviceName: z.string().min(1).describe('Unique name of the microservice'),
    environment: z.enum(['staging', 'production']).describe('Target deployment environment'),
    replicas: z.number().int().min(1).max(10).default(1).describe('Number of container replicas'),
  },
  async ({ serviceName, environment, replicas }) => {
    // Implementation logic
    return {
      content: [{ type: 'text', text: `Successfully deployed ${serviceName} (${replicas} replicas) to ${environment}` }]
    };
  }
);
```

```python
# Python FastMCP Tool Definition (Pydantic)
from fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("ServiceDeployer")

@mcp.tool(description="Deploys a containerized service to the target environment.")
def deploy_service(
    service_name: str = Field(description="Unique name of the microservice"),
    environment: str = Field(description="Target deployment environment (staging/production)"),
    replicas: int = Field(default=1, ge=1, le=10, description="Number of container replicas")
) -> str:
    return f"Successfully deployed {service_name} ({replicas} replicas) to {environment}"
```

---

## 3. Actionable Error Messages (Self-Correction Protocol)

When a tool fails, NEVER return opaque stack traces or generic "Internal Error" messages. Provide **Actionable Error Messages** that guide the LLM toward self-correction:

```json
// BAD Error Response:
{ "error": "Invalid argument" }

// GOOD Actionable Error Response:
{
  "isError": true,
  "content": [
    {
      "type": "text",
      "text": "Error: Table 'usr' not found. Did you mean 'users'? Available tables in current schema: ['users', 'orders', 'transactions']."
    }
  ]
}
```

---

## 4. MCP Server Security & Error Boundaries

1. **Input Sanitization:** Sanitize all file paths and SQL strings to prevent directory traversal and injection.
2. **Timeout Boundaries:** Wrap all external network calls in explicit timeouts (e.g. 10-30s) to prevent hanging the client.
3. **Secret Isolation:** Never expose raw API tokens or credentials in tool parameters or log streams; load them securely from environment variables.

---

## 5. Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
| :--- | :--- |
| *"I'll use untyped `any` for MCP tool parameters to make it flexible."* | **BLOCKED:** Untyped schemas cause malformed tool calls and hallucinated arguments. Enforce Zod/Pydantic schemas. |
| *"I'll return the raw 2MB JSON dump from the API."* | **BLOCKED:** Bloats the client context window. Paginate and filter down to essential fields. |
| *"A simple error string like '500 Failed' is enough."* | **BLOCKED:** Violates Actionable Error Semantics. Include the failed parameter and valid suggestions. |

---

## 6. Verification Gates

- [ ] Are all tool parameters strictly typed and validated via Zod or Pydantic?
- [ ] Do tool descriptions clearly explain the triggers and usage context?
- [ ] Are error responses actionable with concrete suggestions for recovery?
- [ ] Are sensitive tokens isolated from tool schemas and logs?
