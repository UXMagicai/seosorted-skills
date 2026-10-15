---
name: youtube-citation-strategy
description: Find which YouTube videos AI engines and Google AI Overviews cite for the user's topics, read their transcripts, size the YouTube competition, and plan and script videos the brand can make to be cited instead, with SEOsorted. Use when the user asks about YouTube SEO for AI search, which videos ChatGPT or AI Overviews cite, video content strategy, YouTube topics, or writing YouTube scripts.
---

# YouTube citation strategy

## 1. What gets cited

1. Pick 3–10 search intents the business should own (from `keyword-research` or the AI visibility gap list).
2. `find_youtube_videos_cited_by_ai` with `intents`, `max_videos_per_intent: 3`, `transcript_mode: "summary"` (`"full"` only for a few videos in depth), `country: "auto"`. Free.
3. Per intent note: whether an AI Overview appeared and cited videos, which channels win, length and format, what the transcripts cover that a written article does not.
4. Size each intent: `research_youtube` `operation: "keyword_research"` with `query` (the intent) — Google volume plus a low/medium/high competition reading of the YouTube results (1 keyword lookup credit). For a winning video, `research_youtube` `operation: "video_details"` with `video`, `transcript: true` (free).

## 2. Plan

One row per video to make: intent, angle that beats the cited video, format, target keyword, competition level. Prefer intents where AI cites video and competition is low or medium.

## 3. Topics and scripts (needs a connected YouTube channel)

`plan_youtube_videos`:
- `operation: "strategy"` and `"topics"` for the existing plan; `"starter_topics"` works without a channel.
- `operation: "add_topic"` with `title`, `target_keyword`, `format` and `brief` per planned video (EDITOR); `"suggest_titles"` with `target_keyword` for title options.
- `operation: "write_script"` with `topic_id` — background job (poll `check_job_status`), one YouTube-script credit. Say so before starting.
- `operation: "read_script"` with `script_id` to review: citation-readiness checks, YouTube title, description, tags.
- `operation: "edit_script"` with `script_id` and `instruction` for AI edits (at least 1 AI credit, more if it researches); `"update_script"` with `body`, `seo_title`, `seo_description`, `seo_tags` and `base_version` for your own edits (free).
- `operation: "export_script"` with `export_format: "md"` (or `"txt"` for a teleprompter).
- `delete_script` / `delete_topics` only when the user asks.

## Guardrails

Distinguish the four AI Overview outcomes the tool reports (cited, no AI Overview, uncited, lookup failed). A failed lookup is not a finding — retry. Never claim a video is cited without the tool showing it. YouTube volumes are Google web search volumes; say so.
