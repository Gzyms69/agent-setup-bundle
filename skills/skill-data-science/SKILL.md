---
name: skill-data-science
description: Guidance for data science workflows, analysis, and ingestion pipelines. Use when Gemini CLI needs to perform EDA, build data pipelines, manage Jupyter Notebooks, or build stealth web scrapers.
---

# Data Science & Ingestion Skill

This skill manages the end-to-end data lifecycle: from stealth ingestion to analytical reporting, ensuring data quality and reproducibility.

## Overview
Data science requires rigor in exploration, pipelines, and ingestion. This skill mandates structured workflows that prioritize verification, data integrity, and responsible collection over quick, unmaintainable scripts.

## When to Use
- Performing Exploratory Data Analysis (EDA).
- Building automated data pipelines and ETL processes.
- Developing web scrapers and data ingestion tools.
- Unifying datasets and building master databases.

## When NOT to Use
- General software engineering not involving data pipelines.
- UI/UX design.

## 1. Notebook-Driven Workflow
The deliverable for analysis is a well-documented **Jupyter Notebook**.
1.  **Phase 1 (Setup):** Use `uv` for strict environment management. Load data using `pandas` or `polars`. Define all imports and constants at the top.
2.  **Phase 2 (EDA):** Perform systematic checks using `pandas-profiling` or manual `.describe()`, `.info()`, and `.value_counts()`. Use `seaborn` or `matplotlib` for visualizations. Handle missing values and outliers with explicit rationale.
3.  **Phase 3 (Feature Engineering):** Apply normalization, scaling (e.g., StandardScaler), and create interaction terms. Document the mathematical justification for transformations.
4.  **Phase 4 (Hypothesis Testing):** Use `scipy.stats` for rigorous testing (e.g., T-tests, ANOVA). Build baseline models with `scikit-learn` before complex models.
5.  **Phase 5 (Reporting):** Use `plotly` for interactive visualizations. Create a top-level markdown summary of key findings and business impact.

## 2. EDA Checklist
*   [ ] **Distribution Plots:** Visualize continuous variables with histograms/KDEs.
*   [ ] **Null Analysis:** Quantify missingness (MCAR, MAR, MNAR) and visualize with heatmaps.
*   [ ] **Dtype Verification:** Ensure dates are datetime objects, categoricals are category types, etc.
*   [ ] **Correlation Matrix:** Check for multicollinearity using Pearson/Spearman heatmaps.
*   [ ] **Cardinality Checks:** Assess unique values in categorical columns to prevent high-cardinality explosion in one-hot encoding.
*   [ ] **Temporal Patterns:** Plot time-series data to identify seasonality and trends.

## 3. Data Pipeline Quality Gates
*   **Schema Validation:** Enforce schemas at every stage (ingestion, processing, output) using tools like Great Expectations or Pydantic.
*   **Completeness Checks:** Assert that row counts and key metrics fall within expected historical bounds.
*   **Freshness Monitoring:** Ensure timestamps on incoming data indicate it is up-to-date; alert on stale data.

## 4. Stealth Data Ingestion (Scraping)
Operating in adversarial environments requires strict stealth profiles and ethical consideration.
*   **Engine:** Use `curl_cffi` for TLS fingerprint impersonation to match real browsers.
*   **Stealth:** Implement random Gaussian timing (e.g., 3-8s delays), human-like scrolling, and realistic user-agent rotation.
*   **Rate Limiting:** Strictly respect target server capacity. Throttle requests dynamically based on response times and 429 status codes.
*   **Proxy Rotation:** Use residential proxies for distributed scraping, rotating IPs intelligently.
*   **Compliance:** Always check `robots.txt` and Terms of Service. Do not scrape behind authenticated walls unless authorized.
*   **Testing:** ALWAYS test parsing logic on **offline HTML fixtures**. Never hammer live servers for debugging.
*   **Validation:** Use **Pydantic** for schema-first validation of scraped JSON/HTML data to catch silent structural changes.
*   **Persistence:** Use **SQLite** or **GPKG** (for geospatial) for local state tracking of seen items to resume interrupted jobs.

## 5. Data Unification
*   **Relational Stitching:** Use robust relational IDs (e.g., ZIP codes, standardized FIPS codes) to consolidate disparate datasets.
*   **Entity Resolution:** Apply fuzzy matching (e.g., Levenshtein distance) and probabilistic record linkage when unique IDs are missing.
*   **Schema Harmonization:** Map varied incoming column names and formats to a strict, central ontology.
*   **Master Analytical Database:** Aim for a unified `master_analytical.gpkg` or SQL database. Ensure a single source of truth.

## 6. Methodological Verification
*   **Statistical Assumptions:** Explicitly verify assumptions (normality, homoscedasticity, independence) before running tests.
*   **Sample Sizes:** Calculate statistical power and ensure adequate sample sizes for experiments.
*   **Experimental Design:** Validate A/B test setup, control groups, and guard against confounding variables and selection bias.

## 7. Anti-Rationalization Table

| Rationalization | Correction |
| :--- | :--- |
| "The notebook runs end-to-end so it works" | **BLOCKED:** Notebooks hide state bugs. Restart the kernel and run all cells to verify reproducibility. |
| "This dataset is well-known so I don't need EDA" | **BLOCKED:** Even standard datasets can have local corruption, parsing errors, or unexpected formats. EDA is non-negotiable. |
| "Scraping without rate limiting is fine for small jobs" | **BLOCKED:** It is unethical and risks immediate IP bans. Always implement delays. |
| "The data transformations are obvious" | **BLOCKED:** Document every transformation mathematically and logically. What is obvious today is opaque tomorrow. |
| "I'll clean the data later" | **BLOCKED:** Data quality issues compound downstream. Clean data at the point of ingestion or first touch. |

## 8. Red Flags
*   Hardcoded credentials or paths in notebooks.
*   Ignoring warnings from Pandas or Scikit-Learn.
*   Training models on unscaled or un-normalized data without justification.
*   Scraping scripts that crash on the first missing DOM element.
*   Merging dataframes without asserting expected output row counts.

## 9. Verification Gates
1.  **Does the notebook execute flawlessly from a fresh kernel?**
2.  **Are all data pipeline inputs and outputs validated against a schema?**
3.  **Does the scraper use offline fixtures for testing?**
4.  **Are all statistical assumptions verified before drawing conclusions?**
