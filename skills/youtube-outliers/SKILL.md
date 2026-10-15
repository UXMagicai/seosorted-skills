---
name: youtube-outliers
description: Find outlier YouTube videos — videos with views several times their channel's median — for a topic or within one channel, plus the trending chart for a country, and read what made them work from their details, comments and transcript. Use when the user asks for outlier videos, viral video ideas, what's working on YouTube in their niche, breakout formats, trending videos, or a competitor channel's best videos.
---

# YouTube outliers

An outlier beat its own channel's normal by a wide margin, so the topic, title or format did the work, not the audience size. Those are the ideas worth copying.

## Steps

1. **Outliers for a topic:** `research_youtube` `operation: "outliers"` with `query`, `multiplier` (default 3; 5–10 for stricter) and `limit` (up to 50). 1 keyword lookup credit.
2. **Outliers within a channel:** same operation with `channel` (URL, @handle or UC… id) instead of `query`. Free.
3. **Trending:** `operation: "trending"` with `country` and optional `category_id` (e.g. 26 Howto & Style, 27 Education, 28 Science & Technology). Free.
4. **Why it worked:** for the top 3–5, `operation: "video_details"` with `video`, `comments: 10–20` and `transcript: true` (free). Note the title pattern, thumbnail promise, hook in the first 30 seconds, length, and what commenters ask for.

Free operations are capped at 300 YouTube lookups per workspace per hour.

## Output

A table: video, channel, views, multiple of channel median, age, length, title pattern. Then 3–5 patterns that repeat, and video ideas for the user's channel that apply them to their own expertise — not copies.

## Next

Turn ideas into topics and scripts with `plan_youtube_videos` (see `youtube-citation-strategy`); size their search demand with `youtube-keyword-research`.
