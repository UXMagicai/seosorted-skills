---
name: competitor-analysis
description: Analyze SEO competitors with SEOsorted — traffic estimates, authority scores, audit benchmarks and backlink gaps — and turn them into a plan. Use when the user asks who their SEO competitors are, how they compare, why competitors outrank them, competitor traffic, or a competitive SEO analysis.
---

# Competitor analysis

## Steps

1. `manage_competitors` `operation: "list"` for tracked competitors with their measurements. If any show as unmeasured, run `operation: "score"` and poll `check_job_status`.
2. Add missing competitors with `operation: "add"` (EDITOR; up to the workspace limit). Use the domains that actually outrank the user for their main keywords, not only business rivals.
3. `audit_my_site` `operation: "report"` for audit benchmarks against competitors, if present.
4. `manage_competitors` `operation: "backlink_gap"` for the strongest competitor: domains linking to them but not to the user (paid plans; pass on the upgrade link if returned).
5. `track_ai_search_visibility` `operation: "summary"` for share of voice against the same competitors in AI answers.

## Output

- Table: competitor, estimated traffic, authority score, AI share of voice, where they are ahead.
- Top 3 reasons they outrank the user, each backed by a number from the tools.
- Actions: content gaps (→ `keyword-research`), comparison pages (→ `comparison-pages`), link gaps (→ `backlinks`), technical gaps (→ `seo-audit`).
