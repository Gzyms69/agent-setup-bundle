---
name: seo-optimization-and-audit
description: Audits, reviews, and optimizes web pages for search engine ranking (SEO) and user experience. Use when designing, modifying, or auditing public-facing web pages, writing metadata, checking head tags, or solving Core Web Vitals issues.
---

# SEO Optimization & Audit Skill

This skill provides expert guidelines for technical SEO, on-page optimization, metadata standards, and search engine compliance.

---

## 1. Technical SEO & Indexability

Ensure search engines can crawl, parse, and index pages without errors:
*   **Indexation Check:** Verify pages do not contain `<meta name="robots" content="noindex">` unless they are explicitly private (admin pages, drafts, success pages).
*   **Canonical URLs:** Every page must specify a canonical URL to prevent duplicate content indexing:
    ```html
    <link rel="canonical" href="https://example.com/target-path">
    ```
*   **Sitemap & Robots.txt:** Ensure all structural pages are listed in `/sitemap.xml` and crawl rules are configured in `/robots.txt`.

---

## 2. On-Page SEO Checklist

Every public-facing page template must pass this structural layout checklist:

### Meta Header Tags
*   **Title Tag:** Keep titles between 50-60 characters. Must contain the primary keyword near the beginning. Do not exceed 60 characters (titles will get truncated in SERPs).
*   **Meta Description:** Keep between 110-150 characters. Write a clear, benefit-oriented CTA encouraging users to click.
*   **Open Graph (OG):** Provide OG titles, descriptions, and dynamic image URLs (`og:image`, `og:title`, `og:description`) to ensure premium display when shared on social media.

### Heading Hierarchy
*   **One H1 Mandate:** Exactly one `h1` element per page. The `h1` must contain the primary keyword and represent the page's main topic.
*   **Hierarchy Flow:** Use heading tags in sequential order (`h1` -> `h2` -> `h3` -> `h4`). Never use header tags purely for sizing or visual styling (use CSS classes instead).

### Content & Media
*   **Keyword Placement:** Include the target keyword in the `h1`, the first 100 words of body copy, and at least one `h2` header.
*   **Image Alt Texts:** Every `<img>` tag must have a descriptive, keyword-conscious `alt` attribute. If an image is purely decorative, use `alt=""` so screen readers ignore it.
*   **Semantic HTML:** Use HTML5 semantic elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`) to give crawl bots clear context.

---

## 3. Core Web Vitals Targets

Technical page speed directly impacts rankings. Target these 75th percentile thresholds:

| Metric | Good | Needs Improvement | Poor |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s - 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms - 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |

### Speed Optimization Checklist:
- Compilations use modern next-gen image formats (`WebP`, `AVIF`) with defined width and height attributes.
- Critical styles are inlined in the initial HTML document payload.
- Non-critical scripts (e.g., analytics, speed insights) are deferred.

---

## 4. Structured Data (Schema.org)

Help crawl engines parse specific content types. Inject JSON-LD schema scripts:
*   **Organization Schema:** For the homepage, listing company name, logo, social profiles, and contact details.
*   **Product Schema:** For product pages, specifying price, currency, availability, and review ratings.
*   **Article Schema:** For blog posts and documentation, listing publish dates, authors, and publisher context.
*   **FAQ Schema:** For frequently asked question sections to enable rich snippets.

---

## 5. Audit Report Output Standard

When delivering an SEO audit, organize the findings using this layout:

### Executive Summary
- **Overall Health Score (0-100)** based on criteria met.
- **Top 3 Critical Issues** blocking indexation or rankings.
- **Quick Wins** requiring low effort but providing immediate SEO benefits.

### Findings Breakdown
For each issue, specify:
*   **Issue:** What is wrong.
*   **Impact:** SEO severity (High / Medium / Low).
*   **Evidence:** File paths, line numbers, or URL paths containing the issue.
*   **Fix:** Specific, actionable code or configuration changes.
*   **Priority:** Implementation order (1-5).

### Action Plan
1.  **Critical Fixes:** Broken canonicals, indexation blocks, invalid heading structures.
2.  **On-Page Tweaks:** Missing alt attributes, meta tag optimizations, keyword spacing.
3.  **Performance Fixes:** Next-gen images, layout shifts (CLS fixes), code splitting.
4.  **Schema Markup:** Structured data injections.
