---
name: skill-devops-cloud
description: Comprehensive DevOps and cloud infrastructure guidance (Google Cloud). Use when Gemini CLI needs to manage local dev environments, Docker containers, CI/CD pipelines, or production-ready cloud infrastructure.
---

# DevOps & Cloud Infrastructure Skill

This skill manages the transition from local development to production-grade cloud infrastructure on Google Cloud Platform.

## Overview
A strong DevOps culture starts with reproducible local environments and ends with secure, automated, and observable production infrastructure. This skill provides the blueprint for building reliable systems on GCP.

## When to Use
- Setting up a new project's infrastructure.
- Containerizing applications with Docker.
- Designing GCP architecture (Cloud Run, Cloud SQL).
- Creating CI/CD pipelines.

## When NOT to Use
- When writing application business logic.
- When working on local UI/UX design without deployment concerns.

## 1. Local Development Setup
*   **Unified Environment:** Use `docker-compose.yml` to define the entire stack (Frontend, Backend, DB, Cache).
*   **.env Management:** Maintain a `.env.example` file in source control. Never commit `.env`. Provide a script to initialize secrets.
*   **Port Mapping Conventions:** Standardize local ports (e.g., 3000 for frontend, 8000 for API, 5432 for PostgreSQL).
*   **Hot-Reload:** Ensure `npm run dev` (Vite) and `uvicorn --reload` (FastAPI) are used within containers for instant feedback by using volume mounts for source code.

## 2. Docker Best Practices
*   **Multi-Stage Builds:** Always use multi-stage builds to create minimal final images (e.g., build in a Node image, serve with Alpine/Nginx).
*   **.dockerignore:** Exclude `node_modules`, `.git`, `.env`, and test artifacts to minimize build context.
*   **Health Checks:** Embed `HEALTHCHECK` instructions in Dockerfiles to allow orchestrators to restart unhealthy containers.
*   **Security Scanning:** Integrate `trivy` or `grype` in CI to scan images for CVEs before pushing to registries.
*   **Layer Caching:** Order Dockerfile commands from least frequently changed (OS dependencies) to most frequently changed (source code).
*   **Non-Root Users:** Create and switch to a dedicated non-root user (e.g., `USER appuser`) before the `CMD` instruction.

## 3. Google Cloud Architecture (Cloud Run)
*   **Deployment Target:** Deploy Frontend and Backend as independent, stateless Cloud Run services.
*   **Cloud Run Checklist:**
    *   **Region:** Deploy close to users/databases (e.g., `us-central1`).
    *   **CPU/Memory:** Right-size limits based on load testing.
    *   **Concurrency:** Tune concurrent requests per instance (default 80, adjust for I/O vs CPU bound).
    *   **Instances:** Set `--min-instances` to reduce cold starts and `--max-instances` to control costs.
*   **VPC & Private IP:** Use Serverless VPC Access Connectors to route traffic from Cloud Run to private Cloud SQL instances without exposing the DB to the public internet.
*   **Cloud Storage Patterns:** Use signed URLs for client-side uploads/downloads to reduce load on the backend API.

## 4. CI/CD Pipeline (Cloud Build & Deploy)
*   **Source:** Connect GitHub repositories directly to Cloud Build.
*   **Build Triggers:** Trigger tests on PRs, and build/deploy on merges to `main`.
*   **Configuration:** Use `cloudbuild.yaml` to define steps (Lint, Test, Build, Push, Deploy).
*   **Deployment Stages:** Implement isolated environments (`dev`, `staging`, `prod`) using Cloud Deploy.
*   **Rollback Procedures:** Ensure every deployment creates a unique revision tag (e.g., git SHA) to allow instant traffic splitting back to the previous known good revision.

## 5. Secret Management
*   **Google Secret Manager:** Store all production credentials (DB passwords, API keys, certificates) in Secret Manager.
*   **Injection:** Mount secrets directly as environment variables or files into Cloud Run at runtime (never bake them into images).
*   **Rotation:** Implement automated rotation for high-value secrets using Cloud Functions and schedule it periodically.

## 6. Monitoring & Alerting
*   **Cloud Monitoring Setup:** Enable comprehensive monitoring for all GCP services.
*   **Log-Based Alerts:** Create custom metrics from Cloud Logging (e.g., 5xx error rates) and trigger alerts.
*   **Uptime Checks:** Configure public uptime checks for health endpoints from multiple geographic regions.
*   **SLO Definition:** Define Service Level Objectives (e.g., 99.9% availability, P90 latency < 200ms) and alert on burn rates.

## 7. Production Readiness Checklist
*   [ ] **TLS/SSL:** Enforced via Google-managed certificates or Load Balancer.
*   [ ] **CORS:** Strict origin policies configured on the backend API.
*   [ ] **Rate Limiting:** Implemented via Cloud Armor or API Gateway to prevent abuse.
*   [ ] **Graceful Shutdown:** Containers intercept `SIGTERM` to finish processing active requests before exiting.
*   [ ] **Health Endpoints:** Dedicated `/health` and `/ready` endpoints returning deep dependency status.

## 8. Anti-Rationalization Table

| Rationalization | Correction |
| :--- | :--- |
| "I'll add Docker health checks later" | **BLOCKED:** Without health checks, orchestration cannot recover failed states automatically. |
| "Running as root in the container is fine for development" | **BLOCKED:** Dev environments must mirror production to catch permissions errors early. |
| "We don't need staging, just deploy to prod" | **BLOCKED:** Staging is mandatory for verifying configuration and integration before affecting users. |
| "Secrets in environment variables are secure enough" | **BLOCKED:** Unmanaged .env files leak easily. Use Secret Manager for production and local tools like sops. |
| "Monitoring can wait until we have users" | **BLOCKED:** Visibility is required on day 1 to diagnose launch issues. Set up basic logging and alerting now. |

## 9. Red Flags
*   Committing `.env` files or hardcoded credentials.
*   Using `latest` tag for base Docker images.
*   Cloud resources deployed manually via ClickOps instead of Infrastructure as Code (Terraform/gcloud scripts).
*   Containers running as `root`.
*   Lack of CI testing before deployment.

## 10. Verification Gates
1.  **Does the container build and run locally without errors?**
2.  **Are all secrets sourced from Secret Manager in the deployment config?**
3.  **Is there a CI pipeline that runs tests on Pull Requests?**
4.  **Are health checks defined in both the Dockerfile and the deployment config?**
