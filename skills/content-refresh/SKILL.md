---
name: content-refresh
description: Find and improve existing pages that are close to ranking (page 2, positions 8–20), losing clicks, or getting impressions without clicks, using SEOsorted's Search Console data. Use when the user asks to optimize existing content, refresh old posts, fix declining traffic, improve CTR, find quick SEO wins, or update articles that dropped.
---

# Content refresh

Pages that already rank on page 2 have authority. Moving them up is usually faster than ranking a new page.

## Steps

1. `get_search_performance` `view: "opportunities"` (striking distance and CTR issues) and `view: "decaying"` (losing clicks/impressions), `days: 90`. If there is no Search Console data, stop and explain how to connect it.
2. Pick 3–10 pages with the most impressions at risk or within reach.
3. Per page, `get_search_performance` `view: "page"` with `page_url` for the queries it ranks for. `manage_articles` `operation: "get"` for its content if it is a SEOsorted article.
4. Diagnose with evidence:
   - Ranks for queries the page barely covers → add a section answering them.
   - High impressions, low CTR at a good position → rewrite title and meta description around the top query.
   - Decaying → outdated facts, prices or dates; competitors added depth.
   - Two pages splitting the same queries → `cannibalization-check`, then merge.
5. Write a concrete edit plan per page: new title/meta (within 60 / 160 characters), sections to add with the query each one targets, facts to update with sources.

## Applying changes

Edits are made in the SEOsorted article editor (or the CMS for non-SEOsorted pages); then `publish-to-cms` with `operation: "republish"`. Re-check the page in `get_search_performance` after 2–4 weeks.
