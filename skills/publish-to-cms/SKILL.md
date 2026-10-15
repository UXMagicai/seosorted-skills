---
name: publish-to-cms
description: Publish or republish SEOsorted articles to the connected CMS (WordPress, Webflow, Shopify, Strapi or a custom webhook). Use when the user asks to publish an article now, push changes live, republish an updated post, or check which publishing integrations are connected.
---

# Publish to CMS

## Steps

1. `get_site_overview` → connections. Find a usable publishing integration (WordPress, Webflow, Shopify, Strapi, webhook). If there is none, stop and explain how to connect one in Settings → Integrations.
2. Confirm the article: `manage_articles` `operation: "get"`. It must be READY (generated) and reviewed.
3. Say exactly what will happen ("Publish 'X' to WordPress at example.com/blog") and get a yes.
4. `publish_articles` `operation: "publish"` with `article_id`, `integration_id` if there is more than one, and `confirm: true`. Poll `check_job_status` until done and return the live URL.
5. For an already-published article that was edited: `operation: "republish"`. SEOsorted only pushes when the content actually changed since the last publish.

## Guardrails

Publishing is public and outward-facing. Never publish without an explicit yes for that article. Do not bulk-publish; schedule instead (`content-calendar`).
