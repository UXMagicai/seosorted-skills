---
name: competitor-analysis
description: Analyze SEO competitors with SEOsorted — side-by-side Domain Rating, traffic, ranking keywords and links, keyword gaps, who ranks for the money keywords on Google today, audit benchmarks, backlink gaps and AI share of voice — and turn them into a plan. Use when the user asks who their SEO competitors are, how they compare, why competitors outrank them, competitor traffic or keywords, or a competitive SEO analysis.
---

# Competitor analysis

## Steps

1. **Who.** `manage_competitors` `operation: "list"` for tracked competitors. To find who really competes in search, `check_google_results` `operation: "results"` with `keyword` for 2–3 money keywords (1 keyword lookup credit each) — the domains in the top 10 are the search competitors, not only business rivals. Add missing ones with `manage_competitors` `operation: "add"` and `url` (EDITOR); unmeasured ones with `operation: "score"`, then poll `check_job_status`.
2. **Side by side.** `analyze_any_domain` `operation: "compare"` with `domains: [the site, up to 4 competitors]` — authority, traffic, keywords and links (1 keyword lookup credit per domain).
3. **Keyword gap.** `analyze_any_domain` `operation: "keyword_gap"` with `domain` (the site), `competitor` and `mode: "missing"` — keywords they rank for and the site does not (1 credit). `mode: "shared"` shows both positions where they compete head-on.
4. **Their best pages.** `analyze_any_domain` `operation: "pages"` with the competitor's `domain` (1 credit) — the topics driving their traffic.
5. **Where each ranks.** `check_google_results` `operation: "rank"` with `keywords` (up to 20) and `domain` — run it for the site and the main competitor (1 credit per keyword).
6. **Benchmarks.** `audit_my_site` `operation: "report"` for audit scores against competitors, if benchmarked.
7. **Links.** `manage_competitors` `operation: "backlink_gap"` with `url` set to the strongest competitor (paid plans; pass on any upgrade link).
8. **AI search.** `track_ai_search_visibility` `operation: "summary"` for share of voice against the same competitors.

Tell the user the credit total before steps 2–5; they share the keyword lookup allowance.

## Output

- Table: competitor, Domain Rating, estimated traffic, ranking keywords, AI share of voice, where they are ahead.
- Top 3 reasons they outrank the user, each backed by a number from the tools.
- Actions: keyword gaps (→ `keyword-research`, save with `research_keywords` `operation: "save"`), comparison pages (→ `comparison-pages`), link gaps (→ `backlinks`, `backlink-outreach`), technical gaps (→ `seo-audit`).

Traffic and keyword figures are modelled estimates for one Google market; say so.
