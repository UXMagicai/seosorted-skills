---
name: brand-voice-setup
description: Define a website's brand voice, tone, audience and writing rules so every SEOsorted-generated article sounds like the brand, by analysing the site's best existing pages, and save it to the workspace. Use when the user asks to set up brand voice, writing style, tone of voice, content guidelines, or says generated articles don't sound like them — and before any bulk content run.
---

# Brand voice setup

## Steps

1. `manage_site_settings` `operation: "get"` — current business profile, brand voice, voice preset, tone, perspective and global article instructions.
2. Pick 3–5 of the site's best pages (the user's picks, or top pages from `get_search_traffic` `view: "top_pages"`).
3. `manage_site_settings` `operation: "analyze_brand_voice"` with `urls` (up to 5) and/or `text_samples` (pasted copy), `save` omitted — it derives a voice guide with an AI model and returns it without storing it.
4. Shape it into a profile:
   - **Audience:** who reads, what they already know, what they worry about.
   - **Tone:** 3 adjectives, each with "this, not that" (e.g. "direct, not blunt").
   - **Style rules:** sentence length, person (we/you), jargon policy, reading level.
   - **Hard constraints:** claims that need sources, words never to use, legal or medical limits, how to handle prices.
   - **Two short samples:** one intro paragraph and one product mention written in the voice.
5. Show it to the user and refine.
6. Once approved, save with `manage_site_settings` `operation: "update"` (ADMIN) and `settings`:
   - `brandVoice` — the profile text.
   - `targetPersona` — the audience line.
   - `defaultTone`, `defaultPerspective`, `defaultVoicePreset` — the closest presets (values are listed in the tool schema).
   - `globalArticleInstructions` — the hard constraints (max 5,000 characters).
   Omitted keys stay as they are.

## Why it matters

Brand voice, persona and presets are applied to every new draft automatically. Setting them once before a bulk run costs minutes and saves editing every article. Image style and other defaults → `site-settings`.
