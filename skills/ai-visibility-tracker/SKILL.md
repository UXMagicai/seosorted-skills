---
name: ai-visibility-tracker
description: Track how often ChatGPT, Claude, Perplexity, Gemini and Google AI Overviews mention or cite the user's brand versus competitors, using SEOsorted's tracked buyer prompts and scans. Use when the user asks about AI visibility, GEO, AEO, LLM visibility, share of voice in AI answers, whether ChatGPT recommends them, or "are we showing up in AI search".
---

# AI visibility tracker

## Steps

1. `track_ai_search_visibility` `operation: "summary"`. If there is no data yet, go to step 3.
2. `operation: "prompts"` to see which buyer questions are tracked. Good prompts are what a buyer actually types: "best X for Y", "X vs Y", "how do I solve Z". Propose additions for gaps (each product line, each competitor comparison, the main problem) and add with `operation: "add_prompts"` (EDITOR) — each prompt is `{text, topic}`, up to 25 per call. The plan sets how many prompts can be tracked; respect the limit the tool reports.
3. `operation: "scan"` to run a fresh scan (one AI-visibility scan credit). Poll `check_job_status`.
4. Present:
   - Visibility score and share of voice against each competitor.
   - Per engine: mentioned / cited / absent.
   - Prompts where competitors appear and the brand does not — the gap list.
   - Pages of the site that engines already cite (defend these).

## Next

- Gap prompts → `ai-citation-outreach` to find the pages engines cite for them and get mentioned there.
- Engines cite video for a topic → `youtube-citation-strategy`.
- Few AI crawler visits → `ai-crawler-analytics`.

## Guardrails

AI answers vary run to run. Talk in trends across scans, not single answers. Report "not mentioned" as a finding, never as an error.
