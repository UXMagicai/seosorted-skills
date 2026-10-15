---
name: ai-citation-outreach
description: Find the websites that AI answer engines (Google AI Overviews, ChatGPT, Claude, Perplexity, Gemini) cite for the user's buyer questions, and build an outreach list with contacts to earn a mention there. Use when the user asks how to get mentioned by ChatGPT or AI Overviews, wants listicle or PR outreach targets, link-building prospects from AI citations, or "who should we pitch".
---

# AI citation outreach

AI engines answer buyer questions by quoting a small set of trusted pages. Getting the brand onto those pages is the most direct way to appear in AI answers.

## Steps

1. Choose up to 10 buyer prompts. Use the gap list from `ai-visibility-tracker` if available; otherwise let the tool write them from the workspace's business context (omit `prompts`).
2. `find_backlink_prospects` with `prompts`, `surfaces` (start with `["google_ai_overview"]`; add `chat_gpt`, `perplexity`, `claude`, `gemini` to compare), `country: "auto"`, `max_prospects: 10–25`.
3. Read the result: sites ranked by how many prompts cite them (topical authority), the exact passage each engine quoted, and contacts.
4. For the top 5–10 sites draft one specific pitch each:
   - Reference the exact cited page and what it is trusted for (the quoted passage).
   - Offer something the page lacks: fresher data, a missing option, an expert quote, a correction.
   - One short email; no mass templates.

## Output

The prospect table (site, prompts, cited page, quote, contact), then the drafted pitches. Platforms nobody can pitch (Reddit, YouTube, review sites) are a format signal: engines want a thread, a video or a listing there — say which.

## Guardrails

Contacts come from public pages. Do not guess email addresses. Draft emails for the user to send; never send outreach on their behalf without explicit instruction.
