# SEOsorted Skills

**SEO and AI-search visibility for your AI agent.** 26 agent skills plus the hosted [SEOsorted](https://seosorted.ai) MCP server: audit a site, research keywords by volume and difficulty, check cannibalization against Google's live results, generate and publish articles in your brand's voice, read Search Console, and track how often ChatGPT, Claude, Perplexity, Gemini and Google AI Overviews cite you.

Works with Claude Code, Claude Desktop and any agent that supports Agent Skills and remote MCP servers.

## Install

**Claude Code (plugin, recommended)**

```
/plugin marketplace add UXMagicai/seosorted-skills
/plugin install seosorted@seosorted
```

Then run `/mcp`, choose **seosorted**, and sign in. A browser opens on seosorted.ai; pick the workspace (website) the agent should work on. No API key to paste.

**Skills only (any agent)**

```
npx skills add UXMagicai/seosorted-skills
```

and add the MCP server yourself: `https://seosorted.ai/api/mcp` (streamable HTTP, OAuth 2.1). For headless use, send a workspace API key from Settings → API keys as `Authorization: Bearer sk_ss_live_…`.

**No account?** The three free skills below work without one. Everything else needs a [SEOsorted](https://seosorted.ai) workspace.

## Skills

### Core SEO loop
| Skill | What it does |
|---|---|
| `seosorted` | Start here. Connects, reads the workspace, routes to the right skill in the right order |
| `seo-audit` | Technical and on-page audit with a prioritized fix list |
| `keyword-research` | Ideas with volume, difficulty, CPC and intent, ranked quick win → long term |
| `topic-clusters` | Pillar pages and supporting articles for topical authority |
| `cannibalization-check` | Compares Google's live top 10 so you never write two pages for one query |
| `write-article` | One article: research, citations, internal links, preset-style images, meta |
| `bulk-content-run` | 10–100+ articles, prioritized, deduplicated, overlap-checked, paced |
| `content-calendar` | Schedule ready articles on a steady cadence |
| `publish-to-cms` | Publish or republish to WordPress, Webflow, Shopify, Strapi or a webhook |
| `content-refresh` | Lift page-2 and decaying pages using Search Console queries |

### AI search (GEO / AEO)
| Skill | What it does |
|---|---|
| `ai-visibility-tracker` | Share of voice in ChatGPT, Claude, Perplexity, Gemini and AI Overviews |
| `ai-citation-outreach` | The sites AI engines cite for your buyer questions, with contacts to pitch |
| `ai-crawler-analytics` | Which AI bots crawl you, what they read, which missing pages they request |
| `youtube-citation-strategy` | Videos AI engines cite for your topics, with transcripts, and a plan to beat them |
| `youtube-creator-outreach` | Creators worth partnering with, chosen by AI citations |

### Authority, competitors and planning
| Skill | What it does |
|---|---|
| `competitor-analysis` | Traffic, authority, audit benchmarks and AI share of voice vs competitors |
| `comparison-pages` | Honest "you vs competitor" pages that convert |
| `backlinks` | Backlink gap vs competitors and managed backlink packages |
| `link-building-playbooks` | Broken links, unlinked mentions, outdated stats, resource pages, AI listicles |
| `statistics-page` | A sourced statistics page that earns links and AI citations |
| `seo-report` | Search Console and GA4 report: what moved, why, what next |
| `seo-master-plan` | A 90-day plan from live data, or the $49 done-for-you SEO Master Plan |
| `brand-voice-setup` | Voice, audience and rules so every article sounds like you |

### Free, no account
| Skill | What it does |
|---|---|
| `technical-seo-check` | robots.txt (incl. AI crawlers), sitemap, canonicals, titles, broken links |
| `find-questions` | Real questions people ask, grouped into FAQs and article ideas |
| `llms-txt-generator` | A ready-to-upload `llms.txt` for your site |

## Try it

- "Audit my site and tell me what to fix first."
- "Find 50 low-difficulty keywords we don't cover yet and check them for cannibalization."
- "Write and schedule 20 articles for next month, two a day."
- "Are we showing up in ChatGPT for 'best CRM for small business'? Who should we pitch?"
- "Which AI crawlers visited us this month and what 404s are they hitting?"

## How it works

The skills hold the playbooks; the [SEOsorted MCP server](https://seosorted.ai/api/mcp) does the work against your workspace. Writing uses SEOsorted's own pipeline — your brand voice, image style presets, research with citations and internal links — so your agent spends its effort on choosing the right targets and checking the results.

| MCP tool | Used for |
|---|---|
| `get_workspace_overview` | Site, connections, content state, quota |
| `research_keywords` | Ideas, metrics, save, list |
| `check_cannibalization` | SERP-overlap test |
| `run_site_audit` | Start an audit, read the report |
| `manage_articles` | List, read, draft, suggest titles |
| `generate_articles` | Generate one or many, track runs |
| `schedule_and_publish` | Schedule, publish, republish (asks for confirmation) |
| `check_job` | Poll long-running work |
| `get_search_performance` | Search Console overview, opportunities, decaying pages, page queries |
| `track_ai_visibility` | Prompts, scans, share of voice |
| `get_ai_crawler_traffic` | AI bot visits and missing pages |
| `analyze_competitors` | Competitors, scores, backlink gap |
| `create_comparison_page` | Comparison pages |
| `plan_youtube_content` | YouTube strategy, topics, creator targets, scripts |
| `find_citation_prospects` | AI-cited sites and their contacts |
| `get_cited_youtube_videos` | AI-cited videos and transcripts |

Credits follow your SEOsorted plan; tools report what is left before you spend it. Anything that publishes asks for confirmation first.

## Contributing

Each skill is `skills/<name>/SKILL.md` (kept under ~5k tokens) with optional `references/`. Run `node scripts/validate.mjs` before opening a PR.

## License

MIT — see [LICENSE](LICENSE).
