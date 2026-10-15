---
name: write-article
description: Write and generate one SEO article with SEOsorted's pipeline — SERP research, competitor analysis, grounded research with citations, outline, draft, humanizing, internal links, images in the workspace's preset style, and meta tags. Use when the user asks to write a blog post, article, guide or how-to for a keyword, or to create content for their site.
---

# Write one article

SEOsorted writes in the workspace's own brand voice, image preset and research settings. The agent's job is choosing the right target, giving a sharp brief, and checking the result.

## Steps

1. **Target.** Confirm the primary keyword. If it came from a list, it has volume and KD; if the user typed it, get metrics with `research_keywords` `operation: "metrics"`.
2. **Overlap.** `check_keyword_overlap` with the keyword and `compare_existing: true`. If an existing page already owns the intent, recommend `content-refresh` instead.
3. **Draft.** `manage_articles` `operation: "create_draft"` with `primary_keyword`, optional `title`, `content_type` (BLOG_POST, PILLAR_GUIDE, HOWTO, LISTICLE — comparison pages use `write_comparison_page`), `secondary_keywords`, and a `brief` when there is a specific angle, audience or must-cover point. If the response carries an overlap warning, read it before continuing.
4. **Generate.** Tell the user it uses one article credit (charged when it finishes), then `write_articles` `operation: "start"` with the `article_ids`. Poll `check_job_status` (`wait_seconds: 45`) — generation usually takes 4–7 minutes.
5. **Review.** `manage_articles` `operation: "get"`. Check: the H1 matches the intent, facts carry sources, nothing promises outcomes on YMYL topics, internal links point at real pages, no meta-commentary about "the sources provided". Report issues honestly with the exact passage.

## Output

Title, word count, URL slug, meta title/description, image count, and anything that needs a human edit. Then offer `content-calendar` to schedule it or `publish-to-cms` to publish now.

## Guardrails

Never paste a "generated" article you wrote yourself into the workspace as if SEOsorted produced it. If the user wants their own copy, create the draft with their text as the brief and say so.
