# SEOsorted MCP tools

All tools act on the workspace chosen at sign-in. Long operations return a `jobId`; poll with `check_job_status`.

| Tool | Operations | Credits |
|---|---|---|
| `get_site_overview` | — | none |
| `research_keywords` | ideas, metrics, save, list | keyword lookups |
| `check_keyword_overlap` | — | keyword lookups (one per SERP fetched) |
| `audit_my_site` | start, report | audits |
| `manage_articles` | list, get, create_draft, suggest_titles | none |
| `write_articles` | start, status | articles (charged on completion) |
| `publish_articles` | schedule, unschedule, publish, republish | needs `confirm: true` |
| `check_job_status` | — | none |
| `get_search_traffic` | overview, opportunities, decaying, top_pages, page | none |
| `track_ai_search_visibility` | summary, prompts, add_prompts, remove_prompt, scan | AI visibility scans |
| `get_ai_bot_traffic` | summary, missing_pages, vendor_pages | none |
| `manage_competitors` | list, add, score, backlink_gap | backlink gap: paid plans |
| `write_comparison_page` | list, generate | articles |
| `plan_youtube_videos` | strategy, topics, generate_topics, add_topic, targets, set_targets, write_script | YouTube scripts |
| `find_backlink_prospects` | — | none |
| `find_youtube_videos_cited_by_ai` | — | none |
