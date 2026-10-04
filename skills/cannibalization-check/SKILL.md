---
name: cannibalization-check
description: Detect keyword cannibalization by comparing Google's live top-10 results with SEOsorted, before writing new content or when two pages compete. Use when the user asks about cannibalization, duplicate content, two pages competing for the same keyword, whether to merge articles, or before generating a batch of new articles.
---

# Cannibalization check

Two keywords that look different can be one query to Google ("mounjaro weight loss" vs "zepbound weight loss" are not; "metformin side effects in women" vs "metformin side effects" are). Word overlap cannot tell you which. Google's results can: if two queries return mostly the same pages, Google treats them as the same intent, and two articles targeting them will compete.

## Steps

1. Collect the candidate keywords (up to 25 per call).
2. `check_cannibalization` with `terms` and `compare_existing: true` so every term is also compared with the workspace's existing articles. Each term costs one keyword-lookup credit; say so for large lists.
3. Read the verdicts:
   - **7–10 shared URLs**: same intent. Do not write both. Keep the higher-volume keyword; fold the other in as a secondary keyword or a section.
   - **4–6 shared**: borderline. Both can exist only with clearly different angles (a dosage chart vs a mechanism explainer). Write the angle into the brief.
   - **0–3 shared**: safe.
4. Conflicts with **existing** articles: prefer improving the existing page (`content-refresh`) over writing a new one, unless the existing page targets a different intent.

## Output

Table of conflicts: keyword A, keyword B (or existing article), shared URLs, verdict, action. Then the list of terms that are clear to write.

## Guardrails

Results reflect today's SERP in the workspace's market. If a fetch fails for a term, report it as unchecked rather than safe.
