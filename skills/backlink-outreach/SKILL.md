---
name: backlink-outreach
description: Build a backlink outreach campaign with SEOsorted — prospects from competitor link intersect, the backlink gap and the sites AI answers cite, vetted by Domain Rating, with a personalised pitch email drafted for each. Drafts only; the user sends. Use when the user asks for outreach targets, link prospects, sites that link to competitors but not to us, guest post or resource link pitches, or to write outreach emails.
---

# Backlink outreach

## 1. Prospects

Pick one or more sources:
- **Link intersect:** `build_backlinks` `operation: "intersect"` with `competitors` (2–5 domains) and `min_competitors: 2` — sites linking to several competitors but not the user (1 keyword lookup credit per competitor domain). Warmest list.
- **Backlink gap:** `manage_competitors` `operation: "backlink_gap"` with `url` set to one competitor's domain (paid plans).
- **AI-cited sites:** `find_backlink_prospects` with buyer `prompts` (or none to have them written), `surfaces`, `max_prospects` — sites AI answers cite, with contacts from public pages.

## 2. Vet

1. `analyze_any_domain` `operation: "authority"` with the prospect `domains` (up to 50; 1 credit per 10 domains).
2. Drop high spam scores, irrelevant niches, link farms and anything selling links. Keep 10–25.
3. For each, find the exact page to pitch (a resource list, an article citing an outdated source, a roundup).

Quote the credit total to the user before steps 1–2.

## 3. Draft

Per prospect, `build_backlinks` `operation: "draft_pitch"` with:
- `prospect` — the page URL (or domain for the homepage)
- `pitch_type` — `resource`, `guest_post`, `broken_link`, `citation_update` or `unlinked_mention`
- `our_page_url` — the page to pitch (default homepage; a specific page converts better)
- `contact_name` if known, `notes` for specifics (the broken link, the outdated figure)

Free. It returns subject, body and a follow-up, personalised from the page and the workspace's brand voice. Read each one and tighten it: under 120 words, one clear ask.

## Output

A table (prospect, DR, page, pitch type, contact) and the drafts.

## Guardrails

The tool only drafts. Never send outreach or say an email was sent; the user sends from their own inbox. Contacts come from public pages — never guess email addresses. No paid links.
