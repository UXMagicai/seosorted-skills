---
name: backlinks
description: Analyse a site's backlink profile and find link opportunities with SEOsorted — live backlinks, anchor-text distribution, links gained and lost, Domain Rating, the backlink gap versus competitors and managed backlink package progress. Use when the user asks about backlinks, link building targets, domain authority, who links to competitors, lost links, anchor text, or their backlink package progress.
---

# Backlinks

Link data comes from DataForSEO's backlink index. `build_backlinks` defaults to the workspace's own site; pass `domain` for any other.

## 1. Where the site stands

1. `manage_competitors` `operation: "backlinks"` — stored profile: backlinks, referring domains, spam score, domain rank with 30-day change, and the directory-package progress (live, in review, to do) if the workspace has one. Free.
2. `analyze_any_domain` `operation: "authority"` with `domains: [the site, its competitors]` — Domain Rating, Domain Rank and referring domains side by side (1 keyword lookup credit per 10 domains).
3. `build_backlinks` `operation: "links"` with `dofollow_only: true`, `one_per_domain: true` — the strongest live links (1 keyword lookup credit).
4. `build_backlinks` `operation: "anchors"`, with `keyword` set to the money keyword — anchor distribution; exact match above 10% is flagged as over-optimised (1 credit).
5. `build_backlinks` `operation: "new_lost"` with `days: 30` (or 7 / 90) — links gained and lost with dates (1 credit). Lost links from strong domains are worth a polite follow-up.

## 2. Where the gaps are

1. `manage_competitors` `operation: "list"`; pick the competitor ranking for the user's most valuable keywords.
2. `manage_competitors` `operation: "backlink_gap"` with `url` set to that competitor's domain — domains linking to them but not to the user. Paid plans only; pass on any upgrade link as is.
3. For several competitors at once, `build_backlinks` `operation: "intersect"` with `competitors` (2–5 domains) and `min_competitors: 2` — domains linking to at least two of them but not to the user (1 credit per competitor domain). These are the warmest prospects.
4. Group the gap by type: industry publications, directories and listings, resource pages, blogs and podcasts, partners and integrations. Drop high spam scores.

## 3. Turn it into work

- Dead pages on the site that still have links → `link-reclamation`.
- Intersect and gap domains → `backlink-outreach` (drafts a pitch per prospect).
- Editorial links need a linkable asset → `statistics-page`; other tactics → `link-building-playbooks`.

Quote credits before running several operations: the user's keyword lookup allowance is shared with keyword research.

## Guardrails

No paid links, link farms or PBNs — they put the site at risk. Recommend links a real editor would give. Numbers come from the tools; never estimate DR or link counts.
