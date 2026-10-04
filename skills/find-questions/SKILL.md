---
name: find-questions
description: Free tool to find the real questions people ask about a topic — People Also Ask style questions, forum and Reddit threads, and "how/what/why/can" variants — and turn them into FAQ sections and article ideas, no account needed. Use when the user asks what questions people ask about X, FAQ ideas, People Also Ask, question keywords, or content ideas from real questions.
allowed-tools: WebSearch WebFetch
---

# Find questions (free)

## Steps

1. Run web searches for the topic with question modifiers: "how to <topic>", "what is <topic>", "why <topic>", "can you <topic>", "<topic> vs", "is <topic> worth it", "<topic> reddit", "<topic> forum".
2. Collect questions from result titles, "People also ask"-style snippets, and forum thread titles. Fetch 2–3 forum threads to capture how people phrase the problem in their own words.
3. Deduplicate and group by intent: definition, how-to, comparison, cost, problems/troubleshooting, safety.
4. For each group, suggest whether it is an FAQ entry on an existing page or a standalone article.

## Output

Grouped question list with source links, then 5 article ideas built around the strongest question clusters.

With an SEOsorted account, check real search volume for the best questions with `research_keywords` `operation: "metrics"` before committing to articles.
