---
name: technical-audit-report
description: Full technical SEO audit of any website delivered as a client-ready Excel workbook — crawls every page, checks every link and image, redirects (www/apex, http→https, 301 vs 307), canonicals, sitemap and robots.txt, titles and meta, headings, Open Graph, JSON-LD, security headers, llms.txt, soft-404s and access for Googlebot, Bingbot and AI crawlers (GPTBot, ClaudeBot, PerplexityBot), plus Lighthouse performance, accessibility, best-practices and SEO for every page on mobile and desktop. Runs locally with Python and Chrome; no API keys. Use when the user asks for a technical audit report, an SEO audit spreadsheet or Excel file, or a full audit to hand to a client.
allowed-tools: Bash(python3 *) Bash(pip3 *) Bash(npm *)
---

# Technical audit report (Excel)

Produces one `.xlsx` with these tabs: Summary, Issues (prioritised, each with the fix, effort and impact), Pages, Performance, Lighthouse opportunities, Links, Images, Redirects, Crawlability & AI, Security headers, and Structured data.

For a tracked, in-app audit with fix steps, use `seo-audit`. For a quick check without a file, use `technical-seo-check`.

## Requirements

- Python 3.9+ with `requests`, `beautifulsoup4` and `openpyxl` (`pip3 install requests beautifulsoup4 openpyxl`).
- Google Chrome or Chromium, plus Node.js/npm. Lighthouse installs itself into the working folder on first run.

## Inputs

- **Domain** (required), e.g. `example.com`.
- **Display name** for the report title (optional; defaults to the domain).
- **Page cap** (optional, default 300).

Ask only if the domain is missing.

## Steps

The scripts live in this skill's [scripts](scripts/) folder; call them by absolute path. Use a fresh, empty working folder (`$WORK`) outside the skill.

1. **Crawl** ([crawl.py](scripts/crawl.py)), which takes 1–3 minutes on small sites:
   ```bash
   python3 -I <skill>/scripts/crawl.py <domain> $WORK/crawl.json [max_pages]
   ```
   It detects which of apex and `www` actually serves the site, follows internal links and the sitemap, and checks every link and image. It also tests redirect chains, robots.txt, sitemap, llms.txt and security.txt, and runs a soft-404 test. Finally it fetches the homepage as Googlebot, Bingbot, GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended and CCBot.

2. **Lighthouse** ([lighthouse.py](scripts/lighthouse.py)), which takes about 1.5 minutes per page:
   ```bash
   python3 -I <skill>/scripts/lighthouse.py $WORK [max_pages]
   ```
   Tests run **one at a time**, and the mobile score is the **median of 3 runs** (set with `MOBILE_RUNS`). Runs that fail to load are excluded. Never run tests in parallel: CPU contention drags mobile scores 20–40 points too low. A single mobile run can also swing 20 points, which is why the median is used.

3. **Build the workbook** ([build_report.py](scripts/build_report.py)):
   ```bash
   python3 -I <skill>/scripts/build_report.py $WORK "$HOME/Desktop/<Name> - Technical SEO Audit - <YYYY-MM-DD>.xlsx" "<Name>"
   ```

4. **Sanity-check before handing over.** Go through the Issues tab and confirm each finding is real:
   - LinkedIn returns **999** to bots, and the builder already ignores it. Treat other 403/429 responses from big platforms the same way, as bot blocking rather than broken links.
   - Duplicates across *different paths* are real issues. The same path reached via `www` and apex is not; it's the canonical/redirect issue.
   - If a score looks implausible, re-run that URL on its own.

5. **Report back** with the file path, the issue counts by priority, the top 3–5 fixes in plain language, and anything you couldn't test.

## What it checks

- **Canonicals and redirects:** canonicals compared with the host that actually serves the site; www/apex and http→https redirects, including permanent (301/308) vs temporary (302/307).
- **Sitemap and robots.txt:** sitemap entries that redirect or are missing, and robots.txt directives.
- **On-page:** titles and meta descriptions (missing, duplicate, length), H1s, thin content, `lang`, viewport.
- **Sharing and schema:** Open Graph and Twitter cards; JSON-LD (Organization, BreadcrumbList, invalid JSON).
- **Links and images:** broken internal and outbound links, internal links that go through a redirect, image alt text and dimensions.
- **Security and crawl access:** security headers, mixed content, llms.txt, AI-crawler access, soft-404, security.txt.
- **Lighthouse for every page:** performance, accessibility, best practices and SEO, with Core Web Vitals and the failing audits.

## With SEOsorted connected

Add search context from `get_search_traffic` (Search Console clicks and queries) to the summary when you present the report. Offer `seo-audit` to track the fixes.
