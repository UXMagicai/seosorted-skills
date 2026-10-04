# SEOsorted MCP tools

All tools act on the workspace chosen at sign-in. Long operations return a `jobId`; poll with `check_job`.

| Tool | Operations | Credits |
|---|---|---|
| `get_workspace_overview` | — | none |
| `research_keywords` | ideas, metrics, save, list | keyword lookups |
| `check_cannibalization` | — | keyword lookups (one per SERP fetched) |
| `run_site_audit` | start, report | audits |
| `manage_articles` | list, get, create_draft, suggest_titles | none |
| `generate_articles` | start, status | articles (charged on completion) |
| `schedule_and_publish` | schedule, unschedule, publish, republish | needs `confirm: true` |
| `check_job` | — | none |
| `get_search_performance` | overview, opportunities, decaying, top_pages, page | none |
| `track_ai_visibility` | summary, prompts, add_prompts, remove_prompt, scan | AI visibility scans |
| `get_ai_crawler_traffic` | summary, missing_pages, vendor_pages | none |
| `analyze_competitors` | list, add, score, backlink_gap | backlink gap: paid plans |
| `create_comparison_page` | list, generate | articles |
| `plan_youtube_content` | strategy, topics, generate_topics, add_topic, targets, set_targets, write_script | YouTube scripts |
| `find_citation_prospects` | — | none |
| `get_cited_youtube_videos` | — | none |
