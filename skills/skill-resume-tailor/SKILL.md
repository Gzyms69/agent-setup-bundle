---
name: skill-resume-tailor
description: Expert AI resume, CV, and cover letter architect following the Google XYZ formula, Harvard Tech standard, ATS semantic keyword mapping, and strict Anti-AI writing guardrails. Use when creating, tailoring, auditing, or optimizing developer CVs, resumes, cover letters, and STAR story banks.
---

# Resume & Cover Letter Tailor Skill (`skill-resume-tailor`)

This skill provides an engineering-grade framework for authoring, auditing, and tailoring resumes, CVs, cover letters, and interview STAR story banks. It synthesizes the **Google XYZ Formula**, **Harvard Tech Resume Standards**, **ATS Semantic Keyword Mapping**, and **Strict Anti-AI Copywriting Rules**.

---

## 1. Core Principles & Non-Negotiable Directives

### 1.1. The Law of Truth Anchoring (Zero Fabrication)
*   **Rule:** *"Keywords get reformulated, never fabricated."*
*   **Total Ban on Hallucination:** You are strictly forbidden from adding technologies, libraries, tools, metrics, or responsibilities that the candidate has not explicitly documented in their Source of Truth (SSOT: `article-digest.md`, `cv.md`, or raw user statements).
*   **Tool-of-Trade Conflation Ban:** The candidate using tool X does not mean they built tool X.
*   **When in doubt:** Re-order, re-frame, and emphasize verifiable facts. If a required technology is missing from the candidate's profile, bridge it honestly through foundational equivalents (e.g. C++ memory management -> Rust; SQLite WAL -> PostgreSQL indexing) without falsely claiming production mastery.

### 1.2. The Google XYZ Bullet Formula
Every single bullet point in the Projects and Experience sections MUST adhere to the Google formula:
$$\textbf{Accomplished [X], as measured by [Y], by doing [Z]}$$

*   **[X] Action & Outcome:** What was built, solved, fixed, or delivered (start with a strong past-tense action verb).
*   **[Y] Measurable Metric:** Quantifiable business impact, performance metric, latency reduction, memory saving, SLA compliance percentage, or user throughput.
*   **[Z] Technical Method:** The exact technical implementation, algorithm, architecture, framework, or tooling used.

```
❌ Bad (Generic Duty):
"Worked on spatial data processing and improved memory performance in Python."

✅ Good (Google XYZ):
"Eliminated Cartesian OOM crashes and reduced memory footprint by 60% across 9,550 transactions by vectorizing spatial coordinates in C-GEOS and replacing groupby with .transform('sum')."
```

### 1.3. Structural Hierarchy Rule (Project-First vs Experience-First)
*   **Project-First Layout:** MANDATORY for self-taught engineers, career switchers, or junior candidates whose independent production projects demonstrate higher technical complexity than their formal non-tech employment history. `Engineering Projects` must appear immediately below the `Professional Summary`, pushing non-tech roles down.
*   **Experience-First Layout:** Standard for candidates with 3+ years of continuous, verified commercial software engineering employment.

---

## 2. Anti-AI Copywriting Guardrails ("No-Slop" Protocol)

AI-generated resumes and cover letters are instantly detected and rejected by experienced recruiters. You MUST strictly enforce these anti-AI rules:

### 2.1. Dead AI Vocabulary (BANNED)
Never use any of the following words or their Polish equivalents:
> `delve`, `realm`, `harness`, `unlock`, `tapestry`, `cutting-edge`, `revolutionize`, `streamline`, `foster`, `testament`, `dynamic`, `robust`, `synergy`, `pivotal`, `groundbreaking`, `elevate`, `seamless`, `empower`, `paradigm`, `versatile`, `innovative`, `game-changer`, `showcase`, `spearhead`, `passionate`.

### 2.2. Dead Clichés & Corporate Filler (BANNED)
*   *"I am a passionate software engineer eager to leverage my skills..."*
*   *"Proven track record of driving impactful results..."*
*   *"Thrives in fast-paced environments..."*
*   *"Results-oriented team player with strong communication skills..."*

### 2.3. Voice & Tone Directives
*   **Voice:** Active, confident, direct, engineering-focused. Use "I built", "I engineered", "I resolved".
*   **Pacing:** Short, punchy sentences. Vary sentence rhythm.
*   **Evidence:** Every claim must point to a concrete system, repository, tool, or metric.

---

## 3. Workflows & Execution Modes

### 3.1. Workflow A: Bullet Transformation (Google XYZ Engine)

When auditing or rewriting bullets:
1.  **Extract:** Identify the raw technical fact from the source text.
2.  **Quantify:** Find the metric (RAM reduction, RPS, Lighthouse score, SLA %, latency ms, line count, user count). If no exact number exists, identify the systemic constraint (e.g. "zero-downtime", "O(1) lookup", "deterministic DOM extraction").
3.  **Specify:** Name the exact tools, data structures, and algorithms (e.g. `mwparserfromhell AST`, `C-GEOS`, `Neo4j GDS Louvain`, `image2pipe Node streams`).
4.  **Format:** Assemble into: `[Strong Verb] + [System/Outcome X] + [Metric Y] + [Implementation Z]`.

### 3.2. Workflow B: ATS Job Description Tailoring
1.  **JD Deconstruction:** Extract the 5-8 primary hard requirements (languages, databases, protocols, domain concepts).
2.  **SSOT Proof Mapping:** Match extracted JD tokens against the candidate's `article-digest.md` and `cv.md`.
3.  **Re-Ranking:**
    *   Place the top 2-3 most relevant projects at the top of the `Projects` section.
    *   Highlight relevant competencies in the `Professional Summary` (first 3 lines).
    *   Ensure exact keyword matching for ATS indexing (e.g., `FastAPI`, `Docker Compose`, `Linux CLI`, `PostgreSQL`).
4.  **Preserve Core Truth:** Never invent a skill to match a JD token. If unmatched, re-rank matching adjacent skills higher.

### 3.3. Workflow C: High-Conversion Cover Letter (3-Paragraph Architecture)

Cover letters must never exceed 250 words and must follow this 3-paragraph structure:

*   **Paragraph 1 (The Hook & Direct Technical Fit):**
    *   State the exact target role.
    *   Immediately declare the primary technical/operational stack match without pleasantries.
    *   *Example:* "I am applying for the Technical Support Engineer role at [Company]. With production experience debugging Python/Next.js systems, managing Docker/Linux environments, and operating under 98% SLA compliance in corporate logistics at FedEx Express, I can immediately take ownership of your L2 incident queue."
*   **Paragraph 2 (The Deep Technical Proof Point):**
    *   Dive deep into ONE specific, impressive engineering challenge that mirrors the company's pain point.
    *   *Example:* "In my spatial analytics engine BusOS, I resolved severe memory exhaustion (Cartesian OOM) during multi-gigabyte dataset joins by vectorizing geometry calculations in C-GEOS and streaming data pipelines, reducing RAM footprint by 60%."
*   **Paragraph 3 (Operational Rigor & Call to Action):**
    *   Highlight discipline, compliance, English fluency (C1/C2 CAE), and immediate availability.
    *   Direct invitation for a technical interview.

### 3.4. Workflow D: STAR+R Interview Story Banking

Format every behavioral and technical story according to STAR+R:
*   **S (Situation):** Concise context, scale, and constraints (1-2 sentences).
*   **T (Task):** The specific technical problem or bottleneck that had to be solved.
*   **A (Action):** Exact engineering decisions, architectural choices, and debugging steps taken by the candidate.
*   **R (Result):** Quantified outcome, performance improvement, or SLA adherence.
*   **R (Reflection):** What this taught the candidate about system design, maintainability, or team communication.

---

## 4. Technical Resume Formatting & LaTeX Standards

When generating or auditing LaTeX CV templates (`.tex`):
1.  **Single Column Standard:** Use 1-column layout for 100% ATS parser extractability.
2.  **Typography & Diacritics:**
    *   `\usepackage[utf8]{inputenc}` and `\usepackage[T1]{fontenc}` for flawless Polish/European diacritic rendering.
    *   `\input{glyphtounicode}` and `\pdfgentounicode=1` to ensure text is selectable and machine-readable.
3.  **Layout Safety:**
    *   Include `\nopagebreak[4]` before major section titles to prevent orphan headings.
    *   Set strict margin and text-height boundaries to ensure clean 1-page or 2-page cutoffs with zero awkward overflow lines.
