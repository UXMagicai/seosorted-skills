---
name: youtube-keyword-research
description: Find YouTube video keywords and questions with search volume and a competition reading of the YouTube results (views, channel size, video age, Shorts share), plus the top videos and title ideas for a topic, using SEOsorted. Use when the user asks for YouTube keyword research, video topic ideas, how competitive a YouTube topic is, what to title a video, or which videos rank on YouTube for a search.
---

# YouTube keyword research

`research_youtube` reads live YouTube data. Volumes are Google web search volumes — YouTube's own search volume is not available; say so.

## Steps

1. **Ideas and competition:** `research_youtube` `operation: "keyword_research"` with `query` (the seed), `limit` (up to 50 ideas) and `competition_for` (how many top keywords get a competition reading; default 3). 1 keyword lookup credit. Competition is low/medium/high: high means median channel ≥1M subscribers or average views ≥1M; low means both under 50K.
2. **What ranks:** for the 2–3 best keywords, `operation: "search_videos"` with `query` — top results with views, channel subscribers, views per subscriber, age and length (1 credit each). Small channels with high views per subscriber mean the topic is winnable.
3. **Titles:** `operation: "title_ideas"` with `query` and `limit` — new titles written against those ranking now (1 keyword lookup).
4. `country` sets the market (default the workspace's).

Tell the user the credit total before running several seeds.

## Output

A table: keyword, volume, competition level, median views, median channel size, Shorts share, suggested format and title. Rank by volume against competition; flag ideas where AI Overviews cite videos (check with `find_youtube_videos_cited_by_ai`).

## Next

Save chosen videos as topics and script them: `plan_youtube_videos` `operation: "add_topic"` with `title` and `target_keyword`, then `"write_script"` (see `youtube-citation-strategy`). Spot breakout formats → `youtube-outliers`.
