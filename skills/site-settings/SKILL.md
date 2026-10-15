---
name: site-settings
description: Read and change how SEOsorted writes, illustrates and publishes for a site — business profile, article defaults (length, tone, perspective, model, research depth, internal links, table of contents, CTAs), image styles and presets, brand color, YouTube embeds, the default publishing destination and auto-publish. Use when the user asks to change article settings, default article length, image style, featured images, brand color, auto-publish, the blog path, or wants to see the workspace's current settings.
---

# Site settings

All through `manage_site_settings`. Reading is free; changes apply to new drafts, not to articles already written.

## Read

- `operation: "get"` — business profile, brand voice, article defaults, media settings, publishing defaults and connected integrations.
- `operation: "image_presets"` — built-in image styles and the workspace's custom presets, with the defaults marked.

## Change article and publishing defaults (ADMIN)

`operation: "update"` with `settings` containing only the keys to change (null clears a value). Common ones:
- Writing: `defaultLength` (auto, short, medium, long, comprehensive), `defaultTone`, `defaultPerspective`, `defaultVoicePreset`, `defaultAiModel`, `defaultResearchDepth`, `defaultInternalLinksPerArticle`, `tocEnabled`, `ctaEnabled`, `globalArticleInstructions`.
- Media: `defaultGenerateFeaturedImage`, `defaultGenerateInArticleImages`, `titleBasedFeaturedImage`, `brandColor`, `defaultEmbedYoutubeVideos`, `youtubeMode`, `youtubeChannelUrl`.
- Publishing: `defaultPublishIntegrationId` (id from `get`), `blogPathPrefix`, `autoPublishEnabled` (paid plans).

Show the before and after and get a yes. Turning on `autoPublishEnabled` means every finished article goes live without review — confirm that explicitly.

## Image styles

- `operation: "preview_image_preset"` with `prompt` — renders one sample (EDITOR, paid plan; no article credit).
- `operation: "create_image_preset"` with `name`, `prompt`, `kind` (`REGULAR` or `FEATURED`) and optional reference `samples`; `"update_image_preset"` with `preset_id`.
- `operation: "set_default_image_preset"` with `preset_id` (custom id or SKETCH, WATERCOLOR, REALISTIC, ILLUSTRATION, BRAND_TEXT) and `target` (`article` or `featured`) (ADMIN).
- `operation: "delete_image_preset"` needs `confirm: true` — only after the user agrees; anything using it falls back to the default.

## Other

- `operation: "detect_brand_color"` reads the color from the website; `save: true` stores it.
- `operation: "reanalyze_profile"` re-crawls the site and rewrites the business profile (background job; poll `check_job_status`).
- Brand voice → `brand-voice-setup`.
