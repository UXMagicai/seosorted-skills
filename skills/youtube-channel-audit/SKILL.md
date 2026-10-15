---
name: youtube-channel-audit
description: Audit the YouTube SEO of any public channel or video with SEOsorted — channel stats, upload cadence, engagement, top videos, and a per-video metadata audit (title, description, tags, chapters, captions, keyword placement) with pass rates — or review the workspace's own connected channel. Use when the user asks to audit a YouTube channel, review video SEO or metadata, benchmark a competitor channel, or check why videos don't get found.
---

# YouTube channel audit

## Any public channel or video

1. `analyze_any_youtube_channel` with `channel` (URL, @handle or UC… id) and `sample` (5–50 recent uploads, default 30). Returns subscribers, median and average views, engagement, upload cadence, Shorts share, the five most-viewed videos, a per-video metadata audit and channel-wide pass rates. Free.
2. Add `target_keyword` for keyword checks in title, description opening and tags.
3. `profile: true` adds an AI read of content mix, tone and recurring topics — 1 AI credit; ask first.
4. Individual videos: `videos` (up to 10 URLs or ids) instead of `channel`; with 5 or fewer, captions are read to check whether the keyword is spoken in the opening (`transcripts: false` skips that).
5. Fuller stats: `research_youtube` `operation: "channel_stats"` with `channel` (free) — uploads in the last 30/90 days and recent videos.

Checks cover title length, description length, whether the first 150 characters restate the title, tag count, chapters on videos over 3 minutes.

## The workspace's own channel

`manage_my_youtube_channel` `operation: "analysis"` (stored analysis) and `"published"` (videos with views, AI-answer citation counts and 30-day change). `"run_analysis"` refreshes it in the background (no metered credits). `"update_video"` only changes SEOsorted's records, never YouTube.

## Output

Scorecard: stats, cadence, pass rate per check. Then the 5 highest-impact fixes with the videos they apply to, and for a competitor, what they do better.

Compare with `find_youtube_videos_cited_by_ai` to see which videos AI answers cite instead.
