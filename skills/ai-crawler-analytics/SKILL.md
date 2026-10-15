---
name: ai-crawler-analytics
description: See which AI crawlers and bots (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bingbot and others) visit the user's website, which pages they read, and which missing pages they keep requesting, using SEOsorted's bot tracking. Use when the user asks about AI crawlers, bot traffic, whether ChatGPT can see their site, LLM crawling, robots.txt for AI bots, or 404s hit by bots.
---

# AI crawler analytics

## Steps

1. `get_ai_bot_traffic` `view: "summary"`, `days: 30`. If tracking is not installed, explain it is a one-line setup in SEOsorted (Bot traffic → settings) and stop.
2. Present visits by vendor (OpenAI, Anthropic, Perplexity, Google, Microsoft, others), trend, and share that are AI crawlers vs search crawlers.
3. `view: "vendor_pages"` with the top vendor(s) to see which pages they read most — these are the pages most likely to feed AI answers.
4. `view: "missing_pages"`: URLs bots request that return 404. Each is either a page worth creating (bots expect it — often from old links or hallucinated URLs) or a redirect to add. `track_ai_search_visibility` `operation: "crawler_misses"` splits them into moved pages with a suggested redirect target and expected pages worth creating (free).

## Recommendations to make

- An AI vendor absent entirely → `audit_any_page` `operation: "robots"` with the site `url` shows whether each AI crawler may fetch it (free); then check CDN bot blocking.
- Important pages never visited → strengthen internal links to them, add them to the sitemap, consider an `llms.txt` (`llms-txt-generator`).
- Missing pages with many hits → create or redirect.
