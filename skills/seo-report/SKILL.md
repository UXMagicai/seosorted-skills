---
name: seo-report
description: Produce an SEO performance report from SEOsorted's Google Search Console and GA4 data — clicks, impressions, CTR, position, top pages and queries, content attribution, winners and losers — for a weekly review or a client. Use when the user asks how their SEO is doing, for an SEO report, traffic report, Search Console summary, which articles drive traffic, or why traffic changed.
---

# SEO report

## Steps

1. `get_search_performance` `view: "overview"` for the period (default `days: 28`; use 90 for quarterly) — totals and change against the previous period.
2. `view: "top_pages"` for the pages driving clicks and impressions.
3. `view: "opportunities"` and `view: "decaying"` for what to do next.
4. Optional depth: `view: "page"` with `page_url` for a page that moved a lot.
5. `track_ai_visibility` `operation: "summary"` and `get_ai_crawler_traffic` `view: "summary"` for the AI-search side.

## Report structure

1. **Headline:** clicks, impressions, CTR, average position, each with % change.
2. **What drove it:** top 5 pages and top queries, new pages gaining impressions.
3. **What slipped:** decaying pages with the likely reason.
4. **AI search:** share of voice and crawler activity trend.
5. **Next 3 actions**, each tied to a skill (`content-refresh`, `bulk-content-run`, `ai-citation-outreach`…).

## Guardrails

Search Console data lags 2–3 days; say which date the data runs to. New pages take weeks to collect impressions — do not call a 10-day-old page a failure. If Search Console is not connected, say so; do not estimate traffic.
