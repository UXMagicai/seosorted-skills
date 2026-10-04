---
name: seosorted
description: Entry point for SEOsorted.ai, the SEO and AI-search visibility platform. Use when the user mentions SEOsorted, wants to start or plan SEO for their site, asks "what should I do next for SEO", wants a status check of their workspace, or asks which SEOsorted skill to use. Connects the SEOsorted MCP server, reads the workspace, and routes to the right skill in the proper order (audit → plan → write → publish → measure → optimize).
---

# SEOsorted

SEOsorted.ai researches, writes, publishes and measures SEO content for a website, and tracks how often AI engines (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) cite it. This plugin gives the agent that platform through the **SEOsorted MCP server** plus one skill per job.

## 1. Make sure the connection works

Call `get_workspace_overview`. If the tool is missing or returns an auth error:

- Claude Code: run `/mcp`, select **seosorted**, and authenticate. A browser window opens on seosorted.ai; the user signs in and picks **one workspace** (one website). Every tool then works on that workspace.
- No account yet: send the user to https://seosorted.ai to create one. Onboarding (website, business, competitors) is what makes everything downstream good — do not skip it.
- Headless/CI: a workspace API key (`sk_ss_live_…`, created in Settings → API keys) can be sent as `Authorization: Bearer <key>`.

## 2. Read the workspace before recommending anything

From `get_workspace_overview`, note: website and business, connections (CMS for publishing, Google Search Console, GA4), content counts by status, keywords by opportunity bucket, next scheduled posts, last audit, quota left this month, and any active generation run.

Flag gaps plainly: no Search Console = no performance data or striking-distance work; no CMS = articles cannot auto-publish; nothing scheduled = the publishing cadence has stopped.

## 3. Run the loop in this order

| Step | Skill | Why this order |
|---|---|---|
| 1 | `seo-audit` | Fix technical problems before adding pages to a broken site |
| 2 | `keyword-research` → `topic-clusters` | Pick topics by volume vs difficulty, grouped into clusters |
| 3 | `cannibalization-check` | Never write two pages Google treats as one query |
| 4 | `write-article` or `bulk-content-run` | Generate with the workspace's voice, images and internal links |
| 5 | `content-calendar` → `publish-to-cms` | Keep a steady cadence; nothing publishes unscheduled |
| 6 | `seo-report` | Measure with Search Console and GA4 |
| 7 | `content-refresh` | Improve pages on page 2 or decaying — fastest wins |

AI-search work runs alongside: `ai-visibility-tracker`, `ai-citation-outreach`, `ai-crawler-analytics`, `youtube-citation-strategy`.

Authority and positioning: `competitor-analysis`, `comparison-pages`, `backlinks`, `link-building-playbooks`, `statistics-page`.

Planning: `seo-master-plan` (90-day plan), `brand-voice-setup` (do this before bulk writing).

No account needed: `technical-seo-check`, `find-questions`, `llms-txt-generator`.

## 4. Routing rules

- "Write about X" with one keyword → `write-article`. Ten or more keywords → `bulk-content-run`.
- "Why did traffic drop" / "what's working" → `seo-report`, then `content-refresh`.
- "Are we showing up in ChatGPT" → `ai-visibility-tracker`; "get us mentioned" → `ai-citation-outreach`.
- Anything that publishes, schedules, or spends credits: state what will happen and the credits it uses, and get a yes first.

## Ground rules for every skill

- Numbers come from tools, never from memory. If a tool returns nothing, say so — an empty result is a finding.
- Quota is real money for the user. Quote the remaining count the tools return before large runs.
- YMYL topics (health, finance, legal): keep claims attributable to sources, never promise outcomes.
- Work happens in one workspace. If the user means a different site, they must reconnect and pick that workspace.

See `references/tools.md` for the full tool list.
