---
name: page-seo-audit
description: Audit one page of any website with SEOsorted — title, meta description, canonical, headings, word count, images, links, structured data, Open Graph, hreflang, HTTPS, broken links and Core Web Vitals (LCP, CLS, INP) — with a fix for each issue. Free, no credits. Use when the user asks to audit a page or URL, check on-page SEO, why a page doesn't rank, check schema or meta tags, page speed or Core Web Vitals, or broken links on a page.
---

# Page SEO audit

`audit_any_page` checks any public URL live. No credits are used; calls are rate-limited per workspace. Only the HTML is fetched — JavaScript is not executed.

## Steps

1. `audit_any_page` `operation: "audit"` with `url` — title, meta description, canonical, meta robots, lang, viewport, H1s and heading outline, word count, images missing alt or dimensions, link counts, JSON-LD and microdata with parse errors, Open Graph and Twitter tags, hreflang, HTTPS and mixed content, and the site-audit issues for the page, each with a fix.
2. `operation: "speed"` with `url` — PageSpeed mobile score and LCP, CLS, INP (field data when Google has it, otherwise a lab run).
3. `operation: "links"` with `url` — status of up to 50 links on the page; broken ones flagged.
4. If the page should rank for a keyword, `check_google_results` `operation: "results"` with that `keyword` (1 keyword lookup credit) to compare with what ranks.

## Output

- One line: is the page indexable and what is its biggest problem.
- **Fix first:** blocking issues (noindex, wrong canonical, missing title, broken H1 structure, failing Core Web Vitals).
- **Then:** meta length, missing alt text, schema errors, broken links.
- For a JS-rendered page with little HTML text, say the audit sees what crawlers without JavaScript see — that is also what many AI crawlers see.

## Next

If it is a SEOsorted article, fix it with `update-and-republish`. Site-wide problems → `seo-audit`.
