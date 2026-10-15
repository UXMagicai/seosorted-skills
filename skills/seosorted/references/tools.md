# SEOsorted MCP tools

All tools act on the workspace chosen at sign-in. Long operations return a job id; poll with `check_job_status`. Tools that change things outside SEOsorted, or delete, need `confirm: true` (most also take `dryRun: true`).

## Workspace and content

| Tool | Operations | Credits |
|---|---|---|
| `get_site_overview` | — | none |
| `manage_site_settings` | get, update, image_presets, create/update/delete_image_preset, set_default_image_preset, preview_image_preset, analyze_brand_voice, detect_brand_color, reanalyze_profile | none (delete needs `confirm`) |
| `get_content_ideas` | ideas, topic_opportunities, brief | none |
| `manage_articles` | list, get, create_draft, suggest_titles, update | none |
| `write_articles` | start, status, cancel | 1 article per finished article |
| `improve_article` | health, recommendations, suggest_meta, suggest_links, suggest_keywords, rewrite, humanise, questions | none |
| `manage_article_images` | list, regenerate_featured, generate_inline | none |
| `delete_article` | — | none; needs `confirm` |
| `publish_articles` | schedule, unschedule, publish, republish | none; needs `confirm` |
| `get_publishing_calendar` | calendar, destinations, deliveries | none |
| `check_job_status` | — | none |
| `write_comparison_page` | list, generate | 1 article |

## Research and audits

| Tool | Operations | Credits |
|---|---|---|
| `research_keywords` | ideas, metrics, questions, save, list, update, delete | 1 keyword lookup for ideas, metrics, questions, save |
| `check_keyword_overlap` | — | 1 keyword lookup per results page fetched |
| `check_google_results` | results, rank | 1 keyword lookup per keyword |
| `analyze_any_domain` | overview, keywords, pages, backlinks, authority, compare, keyword_gap | 1 keyword lookup per call; compare 1 per domain; authority 1 per 10 domains |
| `audit_my_site` | start, report, issues, update_issue, history | 1 audit for start |
| `audit_any_page` | audit, links, robots, sitemap, speed | none |
| `manage_competitors` | list, add, update, remove, score, backlink_gap, backlinks | none; backlink_gap is paid plans |

## Performance and AI search

| Tool | Operations | Credits |
|---|---|---|
| `get_search_traffic` | overview, opportunities, decaying, top_pages, page, traffic, content_performance, attribution, what_changed, kpis | none |
| `track_ai_search_visibility` | summary, prompts, add_prompts, remove_prompt, regions, scan, readiness, citations, crawler_misses | 1 AI-visibility scan for scan |
| `get_ai_bot_traffic` | summary, missing_pages, vendor_pages | none |

## Links and outreach

| Tool | Operations | Credits |
|---|---|---|
| `build_backlinks` | links, anchors, new_lost, reclaim, intersect, draft_pitch | 1 keyword lookup each; intersect 1 per competitor; draft_pitch 1 AI credit (drafts only) |
| `find_backlink_prospects` | — | none |

## YouTube

| Tool | Operations | Credits |
|---|---|---|
| `research_youtube` | keyword_research, search_videos, outliers, trending, channel_search, channel_stats, video_details, title_ideas | 1 keyword lookup for keyword_research, search_videos, query outliers; title_ideas adds 1 AI credit; the rest free |
| `analyze_any_youtube_channel` | — | none; `profile: true` 1 AI credit |
| `manage_my_youtube_channel` | analysis, run_analysis, published, update_video | none |
| `plan_youtube_videos` | strategy, topics, starter_topics, generate_topics, add_topic, update_topic, delete_topics, suggest_titles, targets, set_targets, write_script, list_scripts, read_script, export_script, update_script, edit_script, duplicate_script, delete_script | 1 YouTube script for write_script; edit_script 1+ AI credit |
| `find_youtube_videos_cited_by_ai` | — | none |
