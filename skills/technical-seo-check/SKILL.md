---
name: technical-seo-check
description: Free technical SEO check for any website, no account needed — robots.txt rules (including AI crawlers like GPTBot and ClaudeBot), XML sitemap health, indexability, canonical tags, meta robots, titles, meta descriptions, headings, structured data and broken links on key pages. Use when the user asks for a quick technical SEO check, robots.txt review, sitemap check, "can Google index my site", or "is my site blocking AI bots".
allowed-tools: WebFetch Bash(curl *)
---

# Technical SEO check (free)

Runs entirely with the agent's own fetch tools. For a full crawl with tracked issues and fix steps, use `seo-audit` with an SEOsorted account.

## Steps

1. **robots.txt:** fetch `https://<domain>/robots.txt`. Report any `Disallow: /`, blocked CSS/JS, and rules for AI crawlers: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot. Note whether a `Sitemap:` line exists.
2. **Sitemap:** fetch the sitemap (from robots.txt, else `/sitemap.xml`, `/sitemap_index.xml`). Count URLs, check `lastmod` freshness, and spot-check 5 URLs for status 200 (`curl -s -o /dev/null -w "%{http_code}" -L`).
3. **Key pages** (home plus 3–5 important pages): with `curl -sL` check the status code, redirect chain, `<title>` (≤60 chars), meta description (≤160), exactly one `<h1>`, `rel=canonical` (self-referencing, not pointing at a redirect), `meta robots` noindex, `hreflang` if multilingual, JSON-LD types, and image `alt` coverage.
4. **Links:** collect internal links from the home page and check them for 4xx/5xx.
5. **HTTPS and www:** http → https and www/non-www should resolve to one version with a single 301.

## Output

A pass / warn / fail table per check, then the top 5 fixes in priority order. Mention what this check cannot see (rendering, Core Web Vitals, index coverage — those need Search Console or a full audit).
