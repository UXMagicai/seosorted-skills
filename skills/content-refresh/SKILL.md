---
name: content-refresh
description: Find and improve existing pages that are close to ranking (page 2, positions 8–20), losing clicks, or getting impressions without clicks, using SEOsorted's Search Console and GA4 data, then edit and republish them. Use when the user asks to optimize existing content, refresh old posts, fix declining traffic, improve CTR, find quick SEO wins, or update articles that dropped.
---

# Content refresh

Pages that already rank on page 2 have authority. Moving them up is usually faster than ranking a new page.

## 1. Pick the pages

1. `get_search_traffic` with `days: 90` and each of:
   - `view: "opportunities"` — query/page pairs ranking 8–20, ranked by clicks a top position would add.
   - `view: "decaying"` — articles whose average position fell 3+ places.
   - `view: "top_pages"` — page-one queries whose CTR is well below the benchmark (title and description worth rewriting).
   - `view: "content_performance"` (needs GA4) — articles whose sessions fell 30%+.
   If there is no Search Console data, stop and explain how to connect it. All views are free.
2. Pick 3–10 pages with the most impressions at risk or within reach.

## 2. Diagnose each page

1. `get_search_traffic` `view: "page"` with `page_url` — its queries and position changes.
2. Find the SEOsorted article: `manage_articles` `operation: "list"` with `search`, then `operation: "get"` with `article_id`.
3. `improve_article` `operation: "health"` (score, failing checks, 30-day clicks and queries) and `operation: "recommendations"` (prioritised fixes). Free.
4. `check_google_results` `operation: "results"` with the top query (1 keyword lookup credit) — what now ranks above it and which SERP features (AI Overview, People Also Ask) it competes with.
5. Diagnose with evidence:
   - Ranks for queries the page barely covers → add a section answering them.
   - High impressions, low CTR at a good position → new title and meta description around the top query.
   - Decaying → outdated facts, prices or dates; competitors added depth.
   - Two pages splitting the same queries → `cannibalization-check`, then merge.

## 3. Edit plan, then apply

Write a concrete plan per page: new title/meta (within 60 / 160 characters), sections to add with the query each targets, facts to update with sources. Show it and get a yes.

Apply with `update-and-republish`: `improve_article` (`suggest_meta` with `apply: true`, `rewrite`, `suggest_links`), `manage_articles` `operation: "update"` for title, body or meta, then `publish_articles` `operation: "republish"` with `confirm: true` — only after the user approves pushing it live. None of the edits use article credits.

Non-SEOsorted pages are edited in the user's CMS; hand over the plan.

Re-check with `get_search_traffic` `view: "page"` after 2–4 weeks.
