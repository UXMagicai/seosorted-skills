---
name: youtube-creator-outreach
description: Build and manage a list of YouTube creators to partner with or pitch in the user's niche — channels AI engines cite, found and vetted with live channel stats and SEOsorted's YouTube targets. Use when the user asks for YouTube influencer outreach, creator partnerships, sponsored video targets, or which YouTubers to work with.
---

# YouTube creator outreach

## Steps

1. **Find creators that matter for AI search:** `find_youtube_videos_cited_by_ai` with the business's key `intents` (free). Channels cited across several intents carry the most weight.
2. **Widen the pool:** `research_youtube` `operation: "channel_search"` with `query` (free, 20 per hour) and `operation: "search_videos"` with `query` (1 keyword lookup credit) for channels ranking on YouTube itself.
3. **Vet each candidate:** `research_youtube` `operation: "channel_stats"` with `channel` (URL, @handle or UC… id; free) — subscribers, median views, engagement rate, uploads in the last 30/90 days. For a deeper read, `analyze_any_youtube_channel` with `channel` (metadata audit free; `profile: true` adds content mix and tone for 1 keyword lookup).
4. **Read the existing list:** `plan_youtube_videos` `operation: "targets"`.
5. **Shortlist up to 10** (the target list holds 10): topical fit, cited for buyer intents (not just entertainment), active recently, engagement over raw subscribers. Note the video that made each one relevant.
6. **Save:** `plan_youtube_videos` `operation: "set_targets"` with `targets` (channel URLs or @handles; EDITOR). This replaces the list — include the ones you keep. Confirm with the user first.
7. **Draft a pitch per creator** referencing their cited video and offering something specific: data, a product to review, an expert interview.

## Guardrails

Numbers come from the tools — never invent subscriber counts or contact details. Draft messages for the user to send; never claim anything was sent.
