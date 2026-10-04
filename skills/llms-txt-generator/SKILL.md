---
name: llms-txt-generator
description: Free tool to generate an llms.txt file for a website — a curated, markdown map of the site's most important pages that helps AI assistants and LLM crawlers understand and cite it — no account needed. Use when the user asks for llms.txt, an AI-readable site summary, how to help ChatGPT or Claude understand their site, or GEO/AEO quick wins.
allowed-tools: WebFetch Bash(curl *)
---

# llms.txt generator (free)

`llms.txt` sits at `https://<domain>/llms.txt` and gives language models a short, curated index of the site in markdown (proposed standard: https://llmstxt.org).

## Steps

1. Fetch the home page, `/sitemap.xml` (or the sitemap from robots.txt), and the main navigation.
2. Pick the pages that matter most: product/service pages, pricing, docs or guides, about, contact, and the 10–20 best articles. Skip tag pages, pagination, legal boilerplate (except a privacy/terms link in "Optional").
3. Fetch each chosen page's title and write a one-line description of what it answers, in plain language.
4. Write the file in this format:

```markdown
# <Site name>

> <One or two sentences: what the business does and for whom.>

<Optional short paragraph with key facts: locations, audience, what it does not do.>

## Products
- [Page title](https://example.com/page): What this page answers.

## Guides
- [Article title](https://example.com/blog/post): What this article answers.

## Optional
- [Privacy policy](https://example.com/privacy)
```

5. Return the file and tell the user to upload it to the site root, then link it from nowhere in particular — crawlers look for it by path.

With an SEOsorted account, `ai-crawler-analytics` shows which AI bots then fetch it.
