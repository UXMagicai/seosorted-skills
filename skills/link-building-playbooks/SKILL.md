---
name: link-building-playbooks
description: Run white-hat link-building playbooks end to end — broken link replacement, link reclamation, unlinked brand mentions, outdated statistics, resource pages, competitor link intersect and AI-citation listicle outreach — from prospecting with SEOsorted's backlink data to ready-to-send drafts. Use when the user asks for link building strategies, how to get backlinks, outreach campaigns, broken link building, or unlinked mentions.
---

# Link-building playbooks

Pick one playbook per campaign. Each ends with a short prospect list and a drafted email per prospect, written with `build_backlinks` `operation: "draft_pitch"` (free; it only drafts, nothing is sent).

## 1. Link reclamation (start here)
`build_backlinks` `operation: "reclaim"` — links already pointing at dead pages on the user's site, with a suggested live page to redirect to. Fixing these needs no outreach. See `link-reclamation`.

## 2. Broken link replacement
Find a niche resource page, then `audit_any_page` `operation: "links"` with its `url` to flag broken outbound links (free). Where a dead link covers a topic the user has a page for, draft with `pitch_type: "broken_link"` and put the dead URL in `notes`.

## 3. Unlinked mentions
Search the web for the brand name excluding the user's own domain; `track_ai_search_visibility` `operation: "citations"` also lists cited pages that name the brand and whether they link. For pages that mention without linking, draft with `pitch_type: "unlinked_mention"`. Highest reply rate of any playbook.

## 4. Outdated statistics
Find well-linked articles quoting old numbers in the niche. Create or point to a page with current, sourced figures (`statistics-page`) and draft with `pitch_type: "citation_update"`.

## 5. Resource pages
Search `"<topic>" inurl:resources` and `"<topic>" "helpful links"`. Pitch the single best page for that list (`our_page_url`), not the homepage, with `pitch_type: "resource"`.

## 6. Competitor link intersect
`build_backlinks` `operation: "intersect"` with 2–5 `competitors` — sites linking to several competitors but not the user. See `backlink-outreach`.

## 7. AI-citation listicles
`find_backlink_prospects` (see `ai-citation-outreach`) — pages AI engines cite are the most valuable links to earn now.

## For every playbook

- Check prospect strength with `analyze_any_domain` `operation: "authority"` (`domains`, up to 50; 1 keyword lookup credit per 10 domains) and drop weak or spammy sites.
- Prospect table: page, Domain Rating, why it fits, contact (from public pages only).
- One specific email per prospect: `draft_pitch` with `prospect`, `pitch_type`, `contact_name` if known, `our_page_url` and `notes`. Edit it so it references the exact page and fix. Under 120 words.
- The user sends the emails. Never send outreach or claim it was sent.
