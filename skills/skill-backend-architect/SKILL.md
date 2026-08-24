---
name: skill-backend-architect
description: Expert backend architecture, database schemas, API design, contract definitions, database indexing, query optimization (EXPLAIN ANALYZE), zero-downtime migrations, and stack selection (Node.js, Python, Go). Use when designing APIs, defining module boundaries, managing database schemas, or validation boundaries.
---

# Backend Architect Skill

This skill provides architectural patterns and best practices for building scalable, maintainable, secure, and type-safe backend services.

---

## 1. Backend Technology Selection

| Stack | Best For | Recommended Frameworks | ORM / DB Access |
| :--- | :--- | :--- | :--- |
| **Node.js** | I/O-heavy, scalable APIs | NestJS, Express.js | **Prisma** (type-safe, schema-first) / **Drizzle** |
| **Python** | Rapid dev, AI/ML, Data Science | FastAPI | **SQLAlchemy** (with Pydantic) / **Alembic** |
| **Go** | Raw performance, microservices | Standard lib, Gin, Echo | Standard lib / sqlx |

### Database Strategy (GCP & Local)
*   **PostgreSQL (via Cloud SQL or Local Docker):** Default choice for structured, transactional, ACID-compliant data.
*   **Firestore / SQLite:** Best for rapid prototyping, real-time sync workloads, and local embedded databases (e.g. Chroma / MemPalace).
*   **BigQuery:** Exclusively for analytical workloads, heavy aggregation, and data warehousing (not transactional).
*   **Bigtable:** Used for massive-scale, high-throughput, flat NoSQL storage.

### Database Verification via MCP (`postgres`, `sqlite`)
Before writing or executing manual database migrations, use the `postgres` and `sqlite` MCP servers:
*   **Schema Introspection:** Directly inspect table structures, primary keys, foreign key constraints, and indices via MCP query tools rather than raw shell commands.
*   **Migration Dry-Runs:** Validate that migration scripts execute cleanly and leave the database in an ACID-consistent state.
*   **Data Integrity Auditing:** Run non-destructive verification queries before and after data transformation tasks.

---

## 2. API Design & Contract-First Development

Define the interface contract in types or schemas *before* writing the API routes. The contract is the specification.

```typescript
// Define the contract first
interface TaskAPI {
  // Creates a task and returns the created task with server-generated fields
  createTask(input: CreateTaskInput): Promise<Task>;

  // Returns paginated tasks matching filters
  listTasks(params: ListTasksParams): Promise<PaginatedResult<Task>>;

  // Returns a single task or throws NotFoundError
  getTask(id: string): Promise<Task>;

  // Partial update — only provided fields change
  updateTask(id: string, input: UpdateTaskInput): Promise<Task>;

  // Idempotent delete — succeeds even if already deleted
  deleteTask(id: string): Promise<void>;
}
```

### Naming Conventions & REST Standard
*   **Resource URLs:** Use plural nouns with no verbs (`GET /api/tasks`, `POST /api/tasks`, not `/api/createTask`).
*   **JSON Field Casing:** Use `camelCase` for JSON request/response payloads (`createdAt`, `taskId`).
*   **Booleans:** Use prefixes such as `is`, `has`, or `can` (`isActive`, `hasPermission`).
*   **Enums:** Use `UPPER_SNAKE` casing (`STATUS_PENDING`, `STATUS_COMPLETED`).

---

## 3. Validation at Boundaries

Never trust external input. Validate input strictly at the system boundaries (controller route handlers, form posts, external webhooks) and trust internal type contracts.

```typescript
// Validate at the API boundary using Zod (Node.js)
app.post('/api/tasks', async (req, res) => {
  const result = CreateTaskSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(422).json({
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Invalid task data',
        details: result.error.flatten(),
      },
    });
  }

  // Internal service code trusts the parsed, typed data
  const task = await taskService.create(result.data);
  return res.status(201).json(task);
});
```
*   **Third-Party API Guard:** Treat third-party API payloads (e.g., webhook payloads, scraped data) as completely untrusted. Parse them through Zod or Pydantic before letting them trigger logic.
*   **Internal Types:** Do not validate types between internal helper functions if they share TypeScript contracts.

---

## 4. Consistent Error Semantics

Maintain a uniform error layout for all API routes. Do not mix throwing patterns, returning nulls, or returning raw text.

```typescript
// Consistent Error Response Shape
interface APIError {
  error: {
    code: string;        // Machine-readable: "VALIDATION_ERROR", "NOT_FOUND"
    message: string;     // Human-readable summary
    details?: unknown;   // Contextual payload (validation details, error arrays)
  };
}
```

### HTTP Status Code Mapping:
*   `400` → Bad Request (malformed JSON syntax).
*   `401` → Unauthorized (missing or invalid credentials).
*   `403` → Forbidden (authenticated, but lacking permission).
*   `404` → Not Found (resource does not exist).
*   `409` → Conflict (duplicate keys, version mismatch, state locks).
*   `422` → Unprocessable Entity (syntactically correct, but failed semantic validation checks).
*   `500` → Internal Server Error (log details internally, never leak database schemas or stack traces to client).

---

## 5. Architectural Principles (Hyrum's Law & Versioning)

### Hyrum's Law & API Obsolescence
> With a sufficient number of users of an API, all observable behaviors of your system will be depended on by somebody, regardless of what you promise in the contract.
*   **Intentional Exposure:** Keep API surface areas as small as possible. Undocumented query parameters, response headers, and exact database error strings become permanent contracts once clients rely on them.
*   **Idempotency:** Designing operations to be idempotent (e.g., `DELETE` requests returning 200/204 even if the resource was already deleted) prevents client retry loops from corrupting state.

### The One-Version Rule
*   Avoid maintaining multiple forks or branches of APIs side-by-side. Extend existing endpoints by adding **optional** fields rather than modifying existing formats.
*   **Backward Compatibility:** Prefer addition over modification. Adding an optional property is backward-compatible; changing a property type or removing it breaks existing clients.

---

## 6. Database Performance, Indexing & Zero-Downtime Migrations

### Query Execution Plan Analysis (`EXPLAIN ANALYZE`)
* **Sequential Scan Detection:** Whenever queries take >50ms or scan large tables, run `EXPLAIN (ANALYZE, BUFFERS)` via MCP or CLI. Check for `Seq Scan on large_table` and high `Buffers: shared read`.
* **Index Types:**
  - **B-Tree:** Default for high-cardinality equality (`=`) and range (`<`, `>`, `BETWEEN`) queries.
  - **GIN (Generalized Inverted Index):** Mandatory for PostgreSQL `jsonb` containment (`@>`), full-text search (`tsvector`), and array columns (`&&`).
  - **Partial Indexes:** Create indexes with a `WHERE` clause for filtered subsets (e.g. `CREATE INDEX idx_active_tasks ON tasks(due_date) WHERE status != 'COMPLETED'`) to minimize index size and write overhead.
  - **Composite Indexes (Left-to-Right Rule):** Place equality columns first, range columns last (e.g. `(tenant_id, status, created_at)`).

### Zero-Downtime Migration Pattern (Expand / Contract)
Never perform breaking schema changes (renaming columns, dropping columns, changing types) in a single step on production databases. Use the **Expand/Contract** pattern:
1. **Expand (Phase 1):** Add the new column/table as nullable or with defaults. Write dual-write application code (write to both old and new, read from old).
2. **Backfill (Phase 2):** Run an asynchronous batch migration to copy and transform historical data from old to new column.
3. **Switch (Phase 3):** Update application to read and write exclusively to the new column.
4. **Contract (Phase 4):** Drop the deprecated old column/table in a subsequent release once stability is proven.

---

## 7. Data Querying & Formatting Patterns

### List Pagination (REST)
Always paginate list endpoints. Never return raw arrays without paging guards:
```typescript
// Paginated JSON list response
{
  "data": [...],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 142,
    "totalPages": 8
  }
}
```

### Discriminator Unions (TypeScript)
Use discriminated unions to model distinct state structures instead of using optional properties:
```typescript
type TaskStatus =
  | { type: 'pending' }
  | { type: 'in_progress'; assigneeId: string; startedAt: Date }
  | { type: 'completed'; completedAt: Date; completedBy: string };
```

---

## 8. Operational Guidelines

*   **Statelessness:** Keep API containers stateless. Store sessions in Redis or DB tables, and file uploads in Cloud Storage to allow horizontal autoscaling.
*   **Asynchronous I/O:** Leverage non-blocking async handlers to ensure event loops do not get blocked.
*   **Structured Logging:** Write logs in structured JSON format (`timestamp`, `severity`, `message`, `context`). This enables immediate indexing and querying in Cloud Logging.

---

## 9. Single Source of Truth (SSOT) & Anti-Duplication Protocol

*   **Pre-Implementation Audit:** Before creating any new API endpoint, database helper, service class, or diagnostic route, grep the codebase (`grep_search`, `list_dir`) to check for existing endpoints and contracts.
*   **Reuse Existing Services:** Reuse existing repositories, database clients, and service handlers instead of instantiating parallel clients.
*   **In-Place Extension:** If an existing endpoint lacks query parameters or needs expanded response fields, extend the existing endpoint in-place with backward compatibility. Never build competing `/api/v2/...` or duplicate `/api/alt-...` endpoints without architectural sign-off.
*   **Centralized Configuration:** All environment variables and settings must flow through a single configuration schema (e.g., `config.ts`, `settings.py`, or `profile.yml`).

---

## 10. Verification Checklist

After designing/updating backend endpoints, verify:
- [ ] Codebase audited for existing endpoints and utilities (SSOT enforced, zero duplicate routes).
- [ ] Input schemas are defined using Zod/Pydantic, and validation runs at API boundaries.
- [ ] Error payloads consistently return the `{ error: { code, message } }` schema.
- [ ] Database queries audited with `EXPLAIN (ANALYZE, BUFFERS)` to verify proper index usage.
- [ ] Breaking database changes follow the Expand/Contract zero-downtime migration strategy.
- [ ] JSON logging outputs valid JSON syntax with appropriate severity levels.
- [ ] Paginated parameters are implemented for list routes.
- [ ] API contract changes are backward-compatible.
