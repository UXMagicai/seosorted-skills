---
name: link-reclamation
description: Recover backlinks pointing at dead or moved pages on the user's site with SEOsorted — finds the dead URLs that still have links, re-checks them live, matches each to the closest live page, and produces a 301 redirect map. Use when the user asks to reclaim lost links, fix broken backlinks, find 404 pages with backlinks, redirect old URLs after a migration, or for quick link-building wins.
---

# Link reclamation

The fastest links to win are ones the site already earned. A redirect from a dead URL to the right live page recovers them without outreach.

## Steps

1. `build_backlinks` `operation: "reclaim"` (defaults to the workspace's site; `domain` for another). 1 keyword lookup credit. Returns up to 25 dead URLs grouped with link counts and the strongest linking domains; each is re-checked live and matched against the sitemap for a similar live page.
2. Add AI-crawler 404s: `track_ai_search_visibility` `operation: "crawler_misses"` lists moved pages with a suggested redirect target (free).
3. Check every suggested target is right: same topic and intent, not just similar words. Verify with `audit_any_page` `operation: "audit"` on the target `url` (free) when unsure. No good match → redirect to the closest category page, or recommend recreating the page if it had many strong links.
4. Prioritise by referring-domain strength and link count.

## Output

A redirect map the user can hand to their developer or CMS:

| Dead URL | Links | Strongest linking domains | Redirect to (301) | Why |
|---|---|---|---|---|

Plus one line per URL to recreate instead of redirect.

## Guardrails

SEOsorted does not change redirects on the site; the user applies them. Never redirect everything to the homepage — Google treats that as a soft 404. Where a linking page links to a wrong URL on the user's site, `backlink-outreach` can draft a correction request (`pitch_type: "broken_link"`).
