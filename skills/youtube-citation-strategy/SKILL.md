---
name: youtube-citation-strategy
description: Find which YouTube videos AI engines and Google AI Overviews cite for the user's topics, read their transcripts, and plan videos the brand can make to be cited instead, with SEOsorted. Use when the user asks about YouTube SEO for AI search, which videos ChatGPT or AI Overviews cite, video content strategy, YouTube topics, or writing YouTube scripts.
---

# YouTube citation strategy

## Steps

1. Pick 3–10 search intents the business should own (from `keyword-research` or the AI visibility gap list).
2. `get_cited_youtube_videos` with `intents`, `max_videos_per_intent: 3`, `transcript_mode: "summary"` (use `"full"` only when analysing a few videos in depth), `country: "auto"`.
3. For each intent, note: whether an AI Overview appeared and cited videos, which channels win, video length and format, and what the transcripts cover that a written article does not.
4. Turn this into a plan: one row per video to make — intent, angle that beats the cited video, format, target keyword.
5. If the workspace has a YouTube channel connected, use `plan_youtube_content`:
   - `operation: "strategy"` and `operation: "topics"` for the existing plan.
   - `operation: "add_topic"` for each planned video (EDITOR).
   - `operation: "write_script"` with a topic id to generate a script (uses a YouTube-script credit).

## Guardrails

Distinguish the four AI Overview outcomes the tool reports (present, absent, uncited, unavailable). "Unavailable" is a failed lookup — retry, do not conclude anything. Never claim a video is cited without the tool showing it.
