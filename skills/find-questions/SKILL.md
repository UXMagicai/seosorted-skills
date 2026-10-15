---
name: find-questions
description: Find the real questions people ask about a topic — question-form searches with volume and difficulty, Google's People Also Ask, Reddit and Quora threads, and "how/what/why/can" variants — and turn them into FAQ sections and article ideas. Uses SEOsorted's question research when connected, free web search otherwise. Use when the user asks what questions people ask about X, FAQ ideas, People Also Ask, question keywords, or content ideas from real questions.
allowed-tools: WebSearch WebFetch
---

# Find questions

## With SEOsorted connected (preferred)

1. `research_keywords` `operation: "questions"` with `seed` (the topic) and `limit` (up to 100). One keyword lookup credit. It returns question-form searches with volume and KD, Google's People-also-ask questions and the Reddit/Quora threads ranking for the topic.
2. For the strongest question, `check_google_results` `operation: "results"` with `keyword` shows the live People Also Ask box, featured snippet and AI Overview sources (1 keyword lookup credit).
3. Fetch 2–3 of the returned forum threads to capture how people phrase the problem in their own words.

## Without an account (free)

1. Web-search the topic with modifiers: "how to <topic>", "what is <topic>", "why <topic>", "can you <topic>", "<topic> vs", "is <topic> worth it", "<topic> reddit", "<topic> forum".
2. Collect questions from result titles, People-also-ask style snippets and forum thread titles. Fetch 2–3 threads for real phrasing.

## Then

1. Deduplicate and group by intent: definition, how-to, comparison, cost, problems/troubleshooting, safety.
2. For each group, suggest whether it is an FAQ entry on an existing page (`manage_articles` `operation: "list"` with `search` finds it) or a standalone article.

## Output

Grouped question list with volume (when connected) and source links, then 5 article ideas built around the strongest question clusters. Offer `research_keywords` `operation: "save"` for the ones worth targeting. Never estimate volume — without an account, say volume is unknown.
