---
name: keyword-research
description: Find SEO keywords with real search volume, keyword difficulty, CPC and intent using SEOsorted, and rank them by opportunity (quick win, high, long-term). Use when the user asks for keyword research, keyword ideas, what to write about, search volume, keyword difficulty, low-competition keywords, or wants to grow impressions/traffic with new content.
---

# Keyword research

## Steps

1. `get_site_overview` for the business, market and what already exists (saved keywords by bucket, articles).
2. Pick 3–8 seeds from the business: core product terms, problems the customer has, the categories competitors rank for. Ask the user for seeds only if the business is unclear.
3. `research_keywords` `operation: "ideas"` per seed (each call uses one keyword-lookup credit). Collect results.
4. Filter hard:
   - Drop navigational terms (brand names of others, "login", "near me" for non-local businesses), off-topic matches and anything the business cannot credibly write about.
   - Drop ideas flagged `hasArticle` — the site already targets them.
   - For regulated topics, drop terms the business must not promote (e.g. controlled substances for a pharmacy).
5. Rank by opportunity: `quick-win` (volume ≥ 250 and KD ≤ 29) first, then `high`, then `medium`. Use volume ÷ (KD + 5)^1.3 as a tiebreaker inside a bucket.
6. Merge near-duplicates ("ozempic side effects" / "side effects of ozempic") into one target with secondaries.

## Output

A table: keyword, volume, KD, bucket, intent, suggested content type (guide, how-to, comparison, listicle), secondary keywords. Then total monthly volume of the shortlist.

## Then

- Offer to save the shortlist: `research_keywords` `operation: "save"` (EDITOR role).
- Before writing anything, run `cannibalization-check` on the shortlist — keyword similarity is not the same as Google treating two queries as one.
- Group into clusters with `topic-clusters` when there are more than ~15 targets.

## Guardrails

Volume and KD come from the tool. Never estimate them. If the provider returns nothing for a seed, say so and try a broader seed.
