---
name: skill-data-analysis
description: Statistical analysis, hypothesis testing, anomaly detection, and dataset evaluation. MUST ACTIVATE when analyzing datasets, calculating statistical metrics, running regressions, evaluating scientific data, or detecting statistical anomalies.
---

# Overview

Skill for analyzing datasets, evaluating statistical claims, and detecting bias. Use when working with data files, CSVs, databases, statistical reports, or when evaluating claims made with data. This skill enforces rigorous statistical protocols, prevents jumping to conclusions, and ensures all claims are empirically grounded.

# When to Use

- Analyzing datasets (structured or semi-structured).
- Evaluating statistical claims made in reports or articles.
- Reviewing research data for soundness.
- Performing Exploratory Data Analysis (EDA).
- Checking for data quality issues, anomalies, or corruption.
- Bias detection in methodologies or datasets.

# When NOT to Use

- System diagnostics or performance profiling (use `skill-system-diagnostics`).
- Pure code review or software architecture analysis (use `skill-code-review`).

# Data Quality Assessment Protocol

1. **Schema evaluation**: Rigorously analyze column types, constraints, and relationships. Ensure data models match reality.
2. **Distribution analysis**: Create histograms, check for skewness and kurtosis. Never assume normality without testing.
3. **Missing value analysis**: Identify Missing Completely At Random (MCAR), Missing At Random (MAR), and Missing Not At Random (MNAR) patterns. The mechanism of missingness dictates the imputation strategy.
4. **Data type validation and coercion rules**: Check for mixed types in columns (e.g., strings in numerical columns) and define strict coercion rules.
5. **Duplicate detection methodology**: Identify exact duplicates and fuzzy duplicates. Determine if duplicates are valid records or data entry errors.

# Statistical Analysis Methodology

1. **Descriptive statistics first**: Always compute the mean, median, mode, standard deviation, and quartiles. Look at the raw numbers before applying any complex models.
2. **Correlation analysis**: Use Pearson for linear relationships, Spearman for rank/monotonic relationships, and point-biserial for categorical-continuous relationships.
3. **Trend identification**: Identify linear, seasonal, and cyclical trends. Differentiate between noise and signal.
4. **Outlier detection**: Use Interquartile Range (IQR), Z-scores, or DBSCAN to detect anomalies. Do not discard outliers without a documented reason.
5. **Statistical significance testing**: Calculate p-values, confidence intervals, and effect sizes. Always correct for multiple comparisons (e.g., Bonferroni correction) to avoid false discovery.

# Claim Verification Framework

1. **Extract discrete verifiable claims**: Break down complex, narrative assertions into individual, testable hypotheses.
2. **Evaluate claims against empirical evidence**: Cross-reference the extracted claims with available raw data or aggregate statistics.
3. **Identify logical fallacies**: Actively scan for ad hominem, strawman, false dichotomy, survivorship bias, and cherry-picking (especially highlighting only supportive data points).
4. **Assess overall credibility**: Assign a confidence score based on the robustness of evidence, sample size, and methodology.

# Bias Detection Checklist

- **Selection bias**: Is the sample truly representative of the target population?
- **Confirmation bias**: Is the analysis explicitly looking for evidence that contradicts the hypothesis, or only evidence that supports it?
- **Survivorship bias**: Are we evaluating only the data that 'survived' a filtering process (e.g., successful startups, retaining customers)?
- **Simpson's paradox awareness**: Do the observed trends reverse or disappear when the data is aggregated or disaggregated into subgroups?
- **Confounding variable identification**: What hidden, unmeasured variables might explain the observed relationship between the independent and dependent variables?
- **Sample size adequacy**: Is the dataset large enough to draw statistically significant conclusions, or is the statistical power too low?

# Output Format

Use the following format when presenting data analysis results:

DATASET SUMMARY:
[High-level overview of the data, size, and quality]

KEY TRENDS:
[Observed patterns and descriptive statistics]

OUTLIERS & ANOMALIES:
[Details of any data points that deviate significantly from the norm]

CLAIM VERIFICATION:
[Assessment of specific claims against the data]

STRATEGIC TAKEAWAYS:
[Actionable insights derived from the analysis]

# Anti-Rationalization Table

| Agent Rationalization | BLOCKED Rebuttal |
|-----------------------|------------------|
| "The data looks clean enough." | BLOCKED: Always verify distributions, check for nulls, validate dtypes. Never assume cleanliness. |
| "The sample size is large so it's representative." | BLOCKED: Large samples can still be biased. Sample quality and selection mechanism matter more than sheer quantity. |
| "Correlation implies this relationship." | BLOCKED: Correlation != causation. Explicitly check for confounders and underlying mechanisms. |
| "One source confirms this claim." | BLOCKED: Cross-reference with independent sources. Single sources can be flawed or biased. |
| "The p-value is significant." | BLOCKED: Check effect size, multiple testing correction, and sample size. Statistical significance does not equal practical significance. |
| "I can remove these outliers." | BLOCKED: Document removal justification, report results with and without outliers. Outliers often contain the most important information. |

# Red Flags

- Skipping Exploratory Data Analysis (EDA) and jumping straight to machine learning or complex statistical models.
- Failing to explicitly document data cleaning steps and imputation choices.
- Presenting correlation as causation in the final takeaways.
- Ignoring missing data mechanisms and blindly applying mean-imputation or assuming MCAR.
- Dropping outliers without thorough investigation and documentation.

# Verification Gates

1. **Data Quality Gate**: Has the dataset been rigorously checked for missing values, mixed types, and anomalies?
2. **Statistical Validity Gate**: Are the chosen statistical tests mathematically appropriate for the given data types and distributions?
3. **Bias Check Gate**: Have potential confounding variables and selection biases been considered and documented?
4. **Claim Verification Gate**: Have all empirical claims been traced back to specific, verifiable data points in the dataset?
