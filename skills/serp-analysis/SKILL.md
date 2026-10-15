---
name: serp-analysis
description: Read live Google results for any keyword in any country with SEOsorted — the top 10 organic results, SERP features (AI Overview and its cited sources, featured snippet, People Also Ask, videos, local pack), volume, KD and CPC — and check where any domain ranks across up to 20 keywords. Use when the user asks who ranks for a keyword, what the SERP looks like, whether there is an AI Overview, rank checks, "where do we rank for X", or what it takes to rank.
---

# SERP analysis

`check_google_results` fetches live Google results (cached up to 6 hours). Cost: 1 keyword lookup credit per keyword checked.

## One keyword: what does Google show?

1. `check_google_results` `operation: "results"` with `keyword` (and `country` / `language` for another market).
2. Read it for intent and difficulty:
   - **Who ranks:** brands, publishers, forums, tools? Forums and UGC high up mean a gap for a solid page.
   - **Content type:** guides, listicles, product pages, tools — match the dominant format.
   - **Features:** an AI Overview (and which sources it cites), featured snippet, People Also Ask, videos, local pack. Each one takes clicks and is a target in itself.
   - **Metrics:** volume, KD, CPC.
3. Authority of the top 10: `analyze_any_domain` `operation: "authority"` with their `domains` (1 credit per 10 domains) — if every result is DR 80+, say it is a long-term target.

## Rank check: where does a domain rank?

`check_google_results` `operation: "rank"` with `keywords` (up to 20) and `domain` (subdomains count). Returns position in the top 100, the ranking URL and the current #1 domain. Works for any domain, so run it for a competitor too.

## Output

For results: a short verdict — intent, format to write, features to target, whether the site can compete — and the top 10 table. For rank: keyword, position, URL, #1 domain.

## Next

Worth targeting → `write-article` (or `cannibalization-check` first if the site has related pages). Ranking 8–20 → `content-refresh`. Video results or a video-citing AI Overview → `youtube-citation-strategy`.
