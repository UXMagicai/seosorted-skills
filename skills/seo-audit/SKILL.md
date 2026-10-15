---
name: seo-audit
description: Run and explain a technical and on-page SEO audit of the user's website with SEOsorted. Use when the user asks for an SEO audit, site health check, "what's wrong with my site", technical SEO issues, broken pages, crawl errors, or wants a prioritized fix list. Starts an audit, waits for it, and turns the issues into a ranked action plan with step-by-step fixes.
---

# SEO audit

Audit before writing anything new. Adding pages to a site with indexing, speed or on-page problems wastes the content.

## Steps

1. `audit_my_site` with `operation: "report"` (no `audit_id`) to see whether a recent audit exists. If it is under 14 days old and the user has not changed the site since, use it.
2. Otherwise tell the user an audit uses one audit credit, then `audit_my_site` with `operation: "start"`. Poll `check_job_status` with `wait_seconds: 45` until it completes (audits usually take a few minutes; keep the user posted).
3. `audit_my_site` with `operation: "report"` for the finished audit.

## How to present it

- One line: overall score and how it compares with the previous audit, if there is one.
- **Fix first** table: critical issues, ordered by pages affected. Columns: issue, pages affected, why it matters (one plain sentence), fix steps.
- **Then** table: warnings worth doing this month.
- **Ignore for now**: low-impact notices, grouped in one line.
- Competitor benchmarks, if returned: where the site is clearly behind.

Translate jargon. "Canonical points to a redirect" becomes "these pages tell Google the 'real' version is a page that redirects, so Google may index neither."

## Guardrails

- Report what the audit found. Do not invent issues it did not flag; if you spot something extra by fetching a page yourself, label it as your own observation.
- If the audit fails or times out, say so and offer to retry; do not present a partial report as complete.

## Next

Technical issues fixed → `keyword-research`. Many thin or duplicate pages → `cannibalization-check`. No Search Console connected → point the user to Settings → Integrations; performance work needs it.
