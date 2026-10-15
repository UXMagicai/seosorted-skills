---
name: comparison-pages
description: Create "Brand vs Competitor" and alternative comparison pages with SEOsorted, built from the workspace's real competitor data, with comparison tables, an honest "where they offer more" section, FAQ and CTA. Use when the user asks for comparison pages, "X vs Y" articles, competitor alternative pages, or bottom-of-funnel content that converts.
---

# Comparison pages

Comparison searches ("brand vs competitor", "competitor alternatives") come from buyers close to deciding. These pages convert well if they are credible, which means stating where the competitor is genuinely better.

## Steps

1. `manage_competitors` `operation: "list"`. If a key competitor is missing, add it: `operation: "add"` with its URL (EDITOR).
2. `write_comparison_page` `operation: "list"` to see which comparisons exist and their status.
3. Prioritise: competitors the user loses deals to, and competitors with the highest search interest. Check volume for "<competitor> alternative" and "<brand> vs <competitor>" with `research_keywords` `operation: "metrics"`.
4. Confirm credits (one article credit each), then `write_comparison_page` `operation: "generate"` with `competitor_id` and an optional `brief` (positioning points, pricing facts with their source, what the user wants emphasised). Poll `check_job_status`.
5. Review with `manage_articles` `operation: "get"`: every competitor claim must be sourced and current, and the "where they offer more" section must be real.

## Guardrails

Never disparage a competitor or state unverifiable claims about them — they will read the page. Prices must carry a source and date.
