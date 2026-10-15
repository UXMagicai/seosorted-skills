---
name: technical-seo-check
description: Free technical SEO check for any website — robots.txt rules (including AI crawlers like GPTBot and ClaudeBot), XML sitemap health, indexability, canonical tags, meta robots, titles, meta descriptions, headings, structured data, Core Web Vitals and broken links on key pages. Uses SEOsorted's free page checks when connected, the agent's own fetch tools otherwise. Use when the user asks for a quick technical SEO check, robots.txt review, sitemap check, "can Google index my site", or "is my site blocking AI bots".
allowed-tools: WebFetch Bash(curl *)
---

# Technical SEO check (free)

Site-wide quick check. For one page in depth use `page-seo-audit`; for a full crawl with tracked issues and fix steps, `seo-audit`.

## With SEOsorted connected (preferred)

`audit_any_page` works on any public URL and uses no credits (rate-limited per workspace).

1. **robots.txt:** `operation: "robots"` with `url: "https://<domain>/"` — user agents, sitemaps, crawl-delay, and whether Googlebot, Bingbot and each AI crawler (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended, CCBot…) may fetch the path.
2. **Sitemap:** `operation: "sitemap"` with the site URL (or the sitemap URL) — URL count, child sitemaps, latest `lastmod`, off-host URLs.
3. **Key pages** (home plus 3–5 important pages): `operation: "audit"` per `url` — title, meta description, canonical, meta robots, H1s, JSON-LD, hreflang, HTTPS and mixed content, alt text, with a fix per issue.
4. **Links:** `operation: "links"` with the home page `url` — HTTP status of up to 50 links, broken ones flagged.
5. **Speed:** `operation: "speed"` on the home page — PageSpeed mobile score and LCP, CLS, INP.

Only HTML is fetched; JavaScript is not executed, so say so for JS-rendered sites.

## Without an account

1. **robots.txt:** fetch `https://<domain>/robots.txt`. Report any `Disallow: /`, blocked CSS/JS, rules for the AI crawlers above, and whether a `Sitemap:` line exists.
2. **Sitemap:** fetch it (from robots.txt, else `/sitemap.xml`, `/sitemap_index.xml`). Count URLs, check `lastmod`, spot-check 5 URLs with `curl -s -o /dev/null -w "%{http_code}" -L`.
3. **Key pages:** with `curl -sL` check status, redirect chain, `<title>` (≤60 chars), meta description (≤160), one `<h1>`, self-referencing `rel=canonical`, `meta robots` noindex, `hreflang`, JSON-LD types, image `alt`.
4. **Links:** check internal links from the home page for 4xx/5xx.

## Both routes

**HTTPS and www:** http → https and www/non-www should resolve to one version with a single 301.

## Output

A pass / warn / fail table per check, then the top 5 fixes in priority order. Mention what this check cannot see (rendering, index coverage — those need Search Console or `seo-audit`).
