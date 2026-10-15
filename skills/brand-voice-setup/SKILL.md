---
name: brand-voice-setup
description: Define a website's brand voice, tone, audience and writing rules so every SEOsorted-generated article sounds like the brand, by analysing the site's best existing pages. Use when the user asks to set up brand voice, writing style, tone of voice, content guidelines, or says generated articles don't sound like them — and before any bulk content run.
---

# Brand voice setup

## Steps

1. `get_site_overview` for the current brand voice, voice preset, persona and image presets.
2. Read 3–5 of the site's best pages (the user's picks, or the top pages from `get_search_traffic` `view: "top_pages"`) with the agent's own web fetch.
3. Write a voice profile:
   - **Audience:** who reads, what they already know, what they worry about.
   - **Tone:** 3 adjectives, each with "this, not that" (e.g. "direct, not blunt").
   - **Style rules:** sentence length, person (we/you), jargon policy, reading level.
   - **Hard constraints:** claims that need sources, words never to use, legal or medical limits, how to handle prices.
   - **Two short samples:** one intro paragraph and one product mention written in the voice.
4. Show it to the user and refine.
5. Save it in SEOsorted: Settings → Brand voice (paste the profile). Image style presets live in Settings → Images (paid feature).

## Why it matters

Brand voice, persona and image preset are applied to every new draft automatically. Setting them once before a bulk run costs minutes and saves editing every article.
