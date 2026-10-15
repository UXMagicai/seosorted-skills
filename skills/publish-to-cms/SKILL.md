---
name: publish-to-cms
description: Publish or republish SEOsorted articles to the connected CMS (WordPress, Webflow, Shopify, Strapi or a custom webhook). Use when the user asks to publish an article now, push changes live, republish an updated post, or check which publishing integrations are connected.
---

# Publish to CMS

## Steps

1. `get_publishing_calendar` `operation: "destinations"` — connected destinations (WordPress, Webflow, Shopify, Strapi, Ghost, HubSpot, Notion, Headless API, webhook), whether each is ready, and the default. If none is ready, stop and explain how to connect one in Settings → Integrations.
2. Confirm the article: `manage_articles` `operation: "get"`. It must be READY (generated) and reviewed.
3. `publish_articles` `operation: "publish"` with `article_id`, `integration_id` if not the default, and `dryRun: true` — say exactly what will happen ("Publish 'X' to WordPress at example.com/blog") and get a yes.
4. Run it again with `confirm: true`. Poll `check_job_status` if a job id comes back, and return the live URL.
5. For an already-published article that was edited: `operation: "republish"` (same dry run, then `confirm: true`). It is refused when nothing changed since the last publish.
6. If a publish failed, `get_publishing_calendar` `operation: "deliveries"` with `article_id` shows the attempt and its error.

## Guardrails

Publishing is public and outward-facing. Never publish without an explicit yes for that article. Do not bulk-publish; schedule instead (`content-calendar`).
