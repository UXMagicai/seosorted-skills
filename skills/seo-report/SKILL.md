---
name: seo-report
description: Produce an SEO performance report from SEOsorted's Google Search Console and GA4 data — clicks, impressions, CTR, position, sessions, conversions, revenue by channel, AI-assistant referrals, top pages and queries, content attribution, winners and losers — for a weekly review or a client. Use when the user asks how their SEO is doing, for an SEO report, traffic report, Search Console or GA4 summary, which articles drive traffic or conversions, or why traffic changed.
---

# SEO report

Every `get_search_traffic` view is free and reads synced data up to yesterday. `days` sets the window (default 28; 90 for quarterly); the previous window of the same length is the comparison.

## Steps

1. `get_search_traffic` `view: "kpis"` — the headline cards: traffic, AI mention rate, AI-crawler visits, backlinks and authority, each with change.
2. `view: "what_changed"` — notable gains and drops (pages, queries, AI mentions), each with a suggested action.
3. Search Console: `view: "overview"` (clicks, impressions, CTR, position) and `view: "top_pages"`.
4. GA4 (if connected):
   - `view: "traffic"` — sessions, users, engagement, key events and revenue by channel, source, country and device, plus AI-assistant referrers.
   - `view: "content_performance"` — sessions and key events per article, articles down 30%+, articles AI assistants send visitors to.
   - `view: "attribution"` — which sources bring key events and revenue.
5. Next steps: `view: "opportunities"` and `view: "decaying"`.
6. Optional depth: `view: "page"` with `page_url` for a page that moved a lot; `traffic` / `attribution` also accept `page_url`.
7. AI-search side: `track_ai_search_visibility` `operation: "summary"` and `get_ai_bot_traffic` `view: "summary"`.

## Report structure

1. **Headline:** clicks, impressions, CTR, average position; sessions and key events from GA4 — each with % change.
2. **What drove it:** top 5 pages and queries, the channels and sources behind conversions.
3. **What slipped:** decaying pages with the likely reason.
4. **AI search:** share of voice, AI-referred sessions and crawler activity.
5. **Next 3 actions**, each tied to a skill (`content-refresh`, `bulk-content-run`, `ai-citation-outreach`…).

## Guardrails

Search Console data lags 2–3 days; say which date the data runs to. New pages take weeks to collect impressions — do not call a 10-day-old page a failure. If Search Console or GA4 is not connected, say which; do not estimate traffic.
