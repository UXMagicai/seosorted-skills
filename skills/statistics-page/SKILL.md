---
name: statistics-page
description: Research and produce a sourced statistics page ("<topic> statistics 2026") that journalists, bloggers and AI engines cite and link to, using web research and SEOsorted generation. Use when the user wants a linkable asset, a statistics or data roundup page, PR-friendly content, or content that earns backlinks.
---

# Statistics page

## Steps

1. Check demand: `research_keywords` `operation: "metrics"` for "<topic> statistics", "<topic> stats", "<topic> facts". Run `check_cannibalization` with `compare_existing: true`.
2. Research 30–60 statistics with the agent's own web tools. Each one needs: the figure, what it measures, the year, the publisher, and the original source URL (not a blog quoting it). Prefer government, academic and industry-body sources. Drop anything you cannot trace to an original.
3. Group into 5–8 sections (market size, adoption, outcomes, demographics, trends, costs).
4. `manage_articles` `operation: "create_draft"` with `primary_keyword: "<topic> statistics"`, `content_type: "LISTICLE"`, and a `brief` containing the full sourced list grouped by section, with the instruction that every statistic keeps its source link and year.
5. Generate with `generate_articles` `operation: "start"`, then review with `manage_articles` `operation: "get"`: every number must still match its source.

## Promote it

Run `link-building-playbooks` (outdated statistics) and `ai-citation-outreach` to put the page in front of people already writing about the topic.
