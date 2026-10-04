---
name: topic-clusters
description: Plan topic clusters (pillar page plus supporting articles) for topical authority using SEOsorted keyword data. Use when the user asks for a content strategy, content plan, topic clusters, pillar pages, topical authority, a content roadmap, or how to organize many keywords into a site structure with internal links.
---

# Topic clusters

## Steps

1. Start from a keyword shortlist (run `keyword-research` first if there is none) or `research_keywords` `operation: "list"` for saved keywords.
2. Group by **search intent and entity**, not by shared words. A cluster is one topic a reader would explore in one sitting (e.g. "tirzepatide dosing": dosage chart, units conversion, titration schedule, missed dose).
3. Pick each cluster's pillar: the broadest keyword with the highest volume that a comprehensive guide can satisfy. Supporting articles take the narrower intents.
4. Run `cannibalization-check` across the whole plan. Pairs sharing 7+ of Google's top 10 URLs belong in one page — merge them. Pairs sharing 4–6 need clearly different angles.
5. Check `manage_articles` `operation: "list"` so existing pages slot into clusters instead of being rewritten.

## Output

For each cluster:

| Role | Keyword | Volume | KD | Status (new / exists) | Links to |
|---|---|---|---|---|---|

Pillar links to every supporting article; every supporting article links back to the pillar and to 1–2 siblings.

Order clusters by total opportunity (sum of volume of quick-win and high keywords) and by fit with what the business sells.

## Next

Write the pillar first with `write-article` (content type `PILLAR_GUIDE`), then the supporting articles with `bulk-content-run`.
