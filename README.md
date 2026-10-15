# SEOsorted Skills

**SEO and AI-search visibility for your AI agent.** 36 agent skills plus the hosted [SEOsorted](https://seosorted.ai) MCP server: audit a site or any page, research keywords by volume and difficulty, read live Google results, check any domain's DR and backlinks, check cannibalization against Google's live results, generate and publish articles in your brand's voice, read Search Console, and track how often ChatGPT, Claude, Perplexity, Gemini and Google AI Overviews cite you.

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

**No account?** The three free checks below work without one (and do more with one). Everything else needs a [SEOsorted](https://seosorted.ai) workspace.

## Skills

### Core SEO loop
| Skill | What it does |
|---|---|
| `seosorted` | Start here. Connects, reads the workspace, routes to the right skill in the right order |
| `seo-audit` | Technical and on-page audit with a prioritized fix list and fix tracking |
| `keyword-research` | Ideas with volume, difficulty, CPC and intent, ranked quick win → long term |
| `topic-clusters` | Pillar pages and supporting articles for topical authority |
| `cannibalization-check` | Compares Google's live top 10 so you never write two pages for one query |
| `write-article` | One article: research, citations, internal links, preset-style images, meta |
| `bulk-content-run` | 10–100+ articles, prioritized, deduplicated, overlap-checked, paced |
| `content-calendar` | Calendar, destinations, failed deliveries, content ideas and scheduling |
| `publish-to-cms` | Publish or republish to WordPress, Webflow, Shopify, Strapi, Ghost, HubSpot, Notion or a webhook |
| `content-refresh` | Lift page-2 and decaying pages using Search Console and GA4 |
| `update-and-republish` | Edit an article's text, meta, links and images, then republish |

### AI search (GEO / AEO)
| Skill | What it does |
|---|---|
| `ai-visibility-tracker` | Share of voice in ChatGPT, Claude, Perplexity, Gemini and AI Overviews, plus AI readiness |
| `ai-citation-outreach` | The sites AI engines cite for your buyer questions, with contacts to pitch |
| `ai-crawler-analytics` | Which AI bots crawl you, what they read, which missing pages they request |
| `youtube-citation-strategy` | Videos AI engines cite for your topics, a plan to beat them, and scripts |
| `youtube-creator-outreach` | Creators worth partnering with, chosen by AI citations and vetted with live stats |

### Competitors, links and authority
| Skill | What it does |
|---|---|
| `competitor-analysis` | Side-by-side DR, traffic and keywords, keyword gap, live rankings, AI share of voice |
| `domain-authority-check` | DR and referring domains for up to 50 domains at once, or a full domain overview |
| `serp-analysis` | Live Google top 10, SERP features and AI Overview sources; rank checks for any domain |
| `comparison-pages` | Honest "you vs competitor" pages that convert |
| `backlinks` | Backlink profile, anchors, new and lost links, gap vs competitors |
| `link-reclamation` | Dead pages that still have backlinks, with a 301 redirect map |
| `backlink-outreach` | Link-intersect and AI-cited prospects, vetted by DR, with drafted pitches |
| `link-building-playbooks` | Broken links, unlinked mentions, outdated stats, resource pages, AI listicles |
| `statistics-page` | A sourced statistics page that earns links and AI citations |

### YouTube
| Skill | What it does |
|---|---|
| `youtube-keyword-research` | Video keywords with volume and a YouTube competition reading, plus title ideas |
| `youtube-outliers` | Videos far above their channel's median views, trending charts, and why they worked |
| `youtube-channel-audit` | Metadata audit and stats for any public channel or video |

### Reporting, planning and setup
| Skill | What it does |
|---|---|
| `seo-report` | Search Console and GA4 report: what moved, why, what next |
| `seo-master-plan` | A 90-day plan from live data, or the $49 done-for-you SEO Master Plan |
| `brand-voice-setup` | Voice, audience and rules so every article sounds like you |
| `site-settings` | Article defaults, image styles, brand color, auto-publish and destinations |
| `page-seo-audit` | On-page SEO, schema, broken links and Core Web Vitals for any URL (no credits) |

### Free checks (no account needed)
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
- "Which sites link to two of our competitors but not to us? Draft a pitch for the top ten."
- "Find outlier videos in our niche and turn the best three into scripts."

## How it works

The skills hold the playbooks; the [SEOsorted MCP server](https://seosorted.ai/api/mcp) does the work against your workspace. Writing uses SEOsorted's own pipeline — your brand voice, image style presets, research with citations and internal links — so your agent spends its effort on choosing the right targets and checking the results.

| MCP tool | Used for |
|---|---|
| `get_site_overview` | Site, connections, content state, credits |
| `manage_site_settings` | Brand voice, article defaults, image styles, publishing defaults |
| `get_content_ideas` | Content ideas, onboarding topic opportunities, briefs |
| `research_keywords` | Ideas, metrics, questions, save, list |
| `check_keyword_overlap` | SERP-overlap test |
| `check_google_results` | Live Google results and rank checks for any keyword and domain |
| `analyze_any_domain` | DR, traffic, keywords, pages, backlinks, compare and keyword gap for any domain |
| `audit_my_site` | Start an audit, read the report, track fixes |
| `audit_any_page` | On-page audit, links, robots.txt, sitemap and speed for any URL |
| `manage_articles` | List, read, draft, suggest titles, edit |
| `write_articles` | Generate one or many, track or cancel runs |
| `improve_article` | Health score, recommendations, meta, links, rewrites |
| `manage_article_images` | Regenerate featured images, add section images |
| `delete_article` | Permanent deletion (asks for confirmation) |
| `publish_articles` | Schedule, publish, republish (asks for confirmation) |
| `get_publishing_calendar` | Calendar, destinations, delivery attempts |
| `check_job_status` | Poll long-running work |
| `get_search_traffic` | Search Console and GA4 views, what changed, KPIs |
| `track_ai_search_visibility` | Prompts, scans, share of voice, AI readiness, citations |
| `get_ai_bot_traffic` | AI bot visits and missing pages |
| `manage_competitors` | Competitors, backlink profile, backlink gap |
| `write_comparison_page` | Comparison pages |
| `build_backlinks` | Backlinks, anchors, new/lost, reclaim, link intersect, pitch drafts |
| `find_backlink_prospects` | AI-cited sites and their contacts |
| `research_youtube` | YouTube keywords, outliers, trending, channels, video details, titles |
| `analyze_any_youtube_channel` | YouTube SEO audit of any channel or video |
| `manage_my_youtube_channel` | The connected channel's analysis and videos |
| `plan_youtube_videos` | YouTube strategy, topics, creator targets, scripts |
| `find_youtube_videos_cited_by_ai` | AI-cited videos and transcripts |

Credits follow your SEOsorted plan; tools report what is left before you spend it. Anything that publishes, deletes or changes something outside SEOsorted asks for confirmation first; outreach is drafted, never sent.

## Contributing

Each skill is `skills/<name>/SKILL.md` (kept under ~5k tokens) with optional `references/`. Run `node scripts/validate.mjs` before opening a PR.

## License

MIT — see [LICENSE](LICENSE).
