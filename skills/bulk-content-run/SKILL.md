---
name: bulk-content-run
description: Generate many SEO articles at once (10 to 100+) with SEOsorted, prioritised by search volume and keyword difficulty, deduplicated against existing content and checked for cannibalization. Use when the user asks for a batch of blogs, "write 50 articles", fill a content calendar, scale content, restart publishing that stopped, or produce content to grow impressions.
---

# Bulk content run

This is the playbook used to ship 100 articles for a live client: research wide, filter hard, check overlap with Google's own results, then let SEOsorted generate at a steady pace.

## Steps

1. **State of play.** `get_workspace_overview`: quota left, articles by status, active generation run, next scheduled posts. If a run is already active, report it and do not start a second.
2. **Budget.** Each finished article uses one article credit. If the request exceeds what is left, tell the user the number that fits and how to get more (upgrade or buy articles in Billing). Do not silently generate fewer.
3. **Research wide.** `keyword-research` across 10–30 seeds covering every product line and customer problem. Expect thousands of raw ideas.
4. **Filter.** Relevance to what the business sells, no navigational or competitor-brand terms, no topics the business must not promote, drop `hasArticle` ideas. Prefer quick-win and high buckets; keep a few high-volume long-term targets.
5. **Merge and dedupe.** Collapse variants into one target with secondaries. Compare against `manage_articles` `operation: "list"` titles.
6. **Overlap check.** `check_cannibalization` in chunks of 25 with `compare_existing: true`. Drop or merge every pair at 7+ shared URLs; differentiate 4–6.
7. **Approve.** Show the final list (keyword, volume, KD, type) and total monthly volume. Get a yes — this spends credits.
8. **Generate.** `generate_articles` `operation: "start"` with `keywords` (max 25 per call; call again for the next chunk). SEOsorted dispatches at most a few at a time per workspace, so the rest queue and drain automatically.
9. **Monitor.** `generate_articles` `operation: "status"` with the run id every few minutes. Report progress in tens, and any failures with their error.
10. **QA.** When done, sample-read 5–10 articles with `manage_articles` `operation: "get"`, plus any on YMYL topics. Look for missing images, unsupported claims, and leaked phrasing such as "the supplied sources".

## Hand-off

Finished articles sit as READY. Nothing publishes until it is scheduled — use `content-calendar` (e.g. 2 per day, quick wins first).
