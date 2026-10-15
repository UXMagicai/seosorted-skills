---
name: youtube-creator-outreach
description: Build and manage a list of YouTube creators to partner with or pitch in the user's niche, using the channels AI engines cite and SEOsorted's YouTube targets. Use when the user asks for YouTube influencer outreach, creator partnerships, sponsored video targets, or which YouTubers to work with.
---

# YouTube creator outreach

## Steps

1. Find creators that matter for AI search: `find_youtube_videos_cited_by_ai` for the business's key intents. Channels cited across several intents carry the most weight.
2. Read the existing target list: `plan_youtube_videos` `operation: "targets"`.
3. Shortlist up to 10 channels (the target list holds 10): topical fit, cited for buyer intents (not just entertainment), recent activity. Note the specific video that made each one relevant.
4. Save the list: `plan_youtube_videos` `operation: "set_targets"` with channel names or URLs (EDITOR). This replaces the list, so include the existing ones you are keeping.
5. Draft a short pitch per creator that references their cited video and offers something specific: data, a product to review, an expert interview.

## Guardrails

Do not invent subscriber counts or contact details. Draft messages for the user to send.
