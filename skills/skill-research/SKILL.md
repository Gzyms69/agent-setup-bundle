---
name: skill-research
description: Skill for rigorous technical and academic research. Enforces multi-source verification and systematic paper analysis.
---

# Overview

Skill for rigorous technical and academic research. Enforces multi-source verification, systematic paper analysis, and wisdom extraction from long-form content. This skill ensures that information provided is accurate, up-to-date, and free from single-source bias or misinterpretation of complex texts.

# When to Use

- Evaluating technical papers or academic journals.
- Researching unfamiliar technologies, frameworks, or concepts.
- Fact-checking claims and debugging deep-seated assumptions.
- Synthesizing knowledge from multiple disparate sources.
- Analyzing long-form content (podcasts, talks, long-form essays, documentation).

# When NOT to Use

- Quick API doc lookups (just use `search_web`).
- Data analysis or statistical evaluation of raw datasets (use `skill-data-analysis`).

# Multi-Source Verification Protocol

- **MINIMUM 3 independent sources** for any factual claim or definitive statement.
- **Source hierarchy**:
  1. Official documentation and primary specifications.
  2. Peer-reviewed papers and academic journals.
  3. Reputable tech blogs and established industry publications.
  4. Community forums (StackOverflow, Reddit) - use only as a last resort or for anecdotal context.
- **Cross-reference dates** to ensure currency. Outdated information in technology is often worse than no information.
- **Identify consensus vs minority positions**. Clearly delineate what is universally agreed upon versus what is heavily debated.
- **Flag when sources contradict each other**. Do not synthesize away contradictions; expose them to the user for evaluation.

# Paper Analysis Methodology

1. **Extract core research questions**: Identify the hypotheses and central claims the authors are attempting to prove.
2. **Assess methodology**: Evaluate the experimental design, sample size, control groups, and statistical controls used.
3. **Evaluate conclusions**: Determine if the conclusions stated in the abstract and discussion are actually supported by the results. Do not take the abstract at face value.
4. **Identify limitations**: Note biases, open questions, and the authors' own stated limitations.
5. **Check citations**: Watch for circular referencing. Ensure foundational claims are actually supported by independent prior work, not just self-citations.

# Wisdom Extraction Process

1. **Filter out fluff**: Remove preambles, conversational filler, rhetorical repetition, and marketing speak. Focus purely on high signal density.
2. **Extract surprising or high-value insights**: Look for counterintuitive findings or paradigm-shifting ideas.
3. **Capture exact memorable quotes**: Preserve the original phrasing for profound insights, as rewording may lose nuance.
4. **Identify actionable habits/recommendations**: What can the user actually do with this information? Translate theory into practice.
5. **Extract specific verifiable facts**: Separate objective reality from the author's subjective opinion or conjecture.

# Credibility Assessment Framework

- **Author credentials and institutional affiliation**: Do they have recognized domain expertise?
- **Publication venue reputation**: Is it a predatory journal, a personal blog, or a top-tier conference?
- **Funding sources and potential conflicts of interest**: Who paid for the research or sponsored the content?
- **Reproducibility of results**: Is the methodology clear enough to be replicated? Is source code or raw data provided?
- **Community reception and citation count**: How has the broader community reacted? Is the work widely cited or largely ignored?

# Output Format

Use the following format when presenting research findings:

SUMMARY:
[Concise synthesis of the research topic]

METHODOLOGY ASSESSMENT:
[Evaluation of how the sources derived their information]

KEY FINDINGS:
[The most important, verified facts and insights]

LIMITATIONS:
[Gaps in the research, potential biases, or contradictory evidence]

CREDIBILITY RATING (1-5 scale):
[Overall score based on source quality and verification robustness]

# Anti-Rationalization Table

| Agent Rationalization | BLOCKED Rebuttal |
|-----------------------|------------------|
| "One source is enough for this fact." | BLOCKED: Minimum 3 independent sources required to establish a verified fact. |
| "This is common knowledge." | BLOCKED: Common knowledge errors are the most dangerous. Verify anyway. |
| "The paper is from a top venue so it must be correct." | BLOCKED: Venue prestige does not guarantee validity. Always evaluate the methodology independently. |
| "I found a blog post confirming this." | BLOCKED: Blog posts are lowest tier. Find the primary sources they cite. |
| "The Wikipedia article says..." | BLOCKED: Use Wikipedia citations as starting points, not endpoints. Read the cited sources. |
| "This information is recent enough." | BLOCKED: Check the exact publication date and verify currency. Tech moves fast. |

# Red Flags

- Relying entirely on secondary sources, summaries, or AI overviews.
- Failing to mention conflicts of interest in funded or sponsored research.
- Presenting a heavily debated topic as a settled consensus.
- Ignoring the methodology section and only reading abstracts or conclusions.
- Failing to notice when multiple 'independent' sources are all just citing the same flawed primary source.

# Verification Gates

1. **Source Diversity Gate**: Are there at least three truly independent primary sources?
2. **Currency Gate**: Have the dates of all sources been explicitly verified against the current state of the art?
3. **Methodology Gate**: Has the experimental design/methodology been evaluated independently of the authors' conclusions?
4. **Bias Gate**: Have funding sources, affiliations, and potential conflicts of interest been investigated?
