---
name: domain-authority-check
description: Check Domain Rating (Ahrefs DR), Domain Rank and referring domains for one domain or up to 50 at once with SEOsorted, plus a full organic and backlink overview of any domain. Use when the user asks for a site's DR or domain authority, wants to vet link prospects, sort a list of sites by authority, or size up any domain's traffic and links.
---

# Domain authority check

`analyze_any_domain` works on any domain on the web, not only the workspace's site. Authority is reported as Domain Rating (Ahrefs DR, 0–100) and Domain Rank (DataForSEO, 0–100).

## Bulk authority (prospect lists, competitor sets)

1. Clean the list to bare domains (`example.com`, no paths), dedupe, cap at 50 per call.
2. `analyze_any_domain` `operation: "authority"` with `domains`. Costs 1 keyword lookup credit per 10 domains — tell the user the total before running a long list.
3. Sort by DR, then referring domains. Flag sites with high DR but few referring domains (often inflated) and anything the tools mark as spammy.

## One domain in depth

`analyze_any_domain` with `domain` (1 keyword lookup credit each):
- `operation: "overview"` — authority, estimated organic traffic and its value, ranking keyword counts, backlink summary (referring domains, dofollow share, spam score) and top keywords.
- `operation: "backlinks"` — monthly new/lost referring domains and the strongest referring domains (`limit` up to 50).
- `operation: "keywords"` / `"pages"` — what it ranks for and its top pages.

`country` and `language` set the Google market; default is the workspace's.

## Output

A table: domain, DR, Domain Rank, referring domains, verdict (strong / usable / skip) with the reason. Traffic figures are modelled estimates for one market; say so.

## Next

Vetted prospects → `backlink-outreach`. Competitor sets → `competitor-analysis`.
