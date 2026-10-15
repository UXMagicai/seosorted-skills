---
name: update-and-republish
description: Edit an existing SEOsorted article and push the update live — score it, rewrite passages, humanise, fix the title, meta description and slug, add internal links, regenerate the featured image or add section images, then republish to the CMS with the user's confirmation. Use when the user asks to edit, update, improve, fix or rewrite an article, change its images, or push changes to a published post.
---

# Update and republish

None of these edits use article credits. Every body edit keeps the previous version as a revision.

## 1. Find and score

1. `manage_articles` `operation: "list"` with `search` (title) to get the `article_id`; `operation: "get"` for the body, meta and live URL.
2. `improve_article` `operation: "health"` — content score with each check, readability, keyword density and, if published, 30-day Search Console clicks and queries. `operation: "recommendations"` — prioritised fixes.

## 2. Edit

Pick what the user asked for (or what the recommendations call for):
- **Meta:** `improve_article` `operation: "suggest_meta"`; show it, then again with `apply: true` to write it.
- **A passage:** `improve_article` `operation: "rewrite"` with `selection` (quoted exactly from the body) and `instruction` or `preset` (`concise`, `data`, `hook`, `humanise`, `formal`, `casual`). It replaces the passage unless `apply: false` — use `apply: false` to preview first.
- **Whole body reads machine-written:** `operation: "humanise"`.
- **Internal links:** `operation: "suggest_links"` returns anchors already in the body with targets; apply the ones the user accepts via a body update.
- **Missing keywords:** `operation: "suggest_keywords"`.
- **First-hand experience:** `operation: "questions"` returns author-interview questions; pass `answers` to save the user's replies.
- **Direct edits:** `manage_articles` `operation: "update"` with any of `title`, `meta_title`, `meta_description`, `slug`, `focus_keyword`, `secondary_keywords`, `brief`, or `body`. `body` replaces everything — read with `get` first and send the whole edited text. Changing the slug of a live post changes its URL; warn the user and recommend a redirect.

## 3. Images

`manage_article_images` with `article_id` (no article credits; 10–40 seconds each):
- `operation: "list"` — current images and the style in effect.
- `operation: "regenerate_featured"` — new featured image, `source: "AI"` (optional `prompt`) or `"UNSPLASH"` (optional `query`), with `alt`.
- `operation: "generate_inline"` with `heading` (exact H2–H4 text) to illustrate that section, or only `prompt` to get an image URL and markdown without placing it.

## 4. Push live

A published article keeps showing the old text and images until it is republished.

1. Re-run `improve_article` `operation: "health"` and summarise what changed.
2. `publish_articles` `operation: "republish"` with `article_id` and `dryRun: true`; show what will happen.
3. Only after the user says yes, run it with `confirm: true`. It is refused when nothing changed since the last publish. Failures → `get_publishing_calendar` `operation: "deliveries"` with `article_id`.

Deleting an article is a separate, permanent step (`delete_article`, needs `confirm: true`) — only when the user explicitly asks.
