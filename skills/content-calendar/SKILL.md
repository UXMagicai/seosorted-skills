---
name: content-calendar
description: Plan and manage the publishing schedule for SEOsorted articles — see what is scheduled and published on the calendar, which destinations are connected and whether deliveries failed, fill gaps with content ideas, and schedule ready articles on a steady cadence. Use when the user asks about their content calendar, publishing schedule, why posts stopped going out, what's publishing next, what to write next, or wants to schedule articles.
---

# Content calendar

Scheduled articles auto-publish to the default destination. If nothing is scheduled, publishing stops — the most common reason "the blogs stopped".

## 1. Read the calendar

1. `get_publishing_calendar` `operation: "calendar"` (default today + 30 days; `from` / `to` as YYYY-MM-DD, at most 120 days) — scheduled and published articles with dates and live URLs.
2. `get_publishing_calendar` `operation: "destinations"` — connected destinations, which are ready, and the default. No ready destination means scheduled posts cannot go out: send the user to Settings → Integrations.
3. If posts "stopped", `get_publishing_calendar` `operation: "deliveries"` — recent publish attempts with their errors. Report the exact error.

All three are free.

## 2. Find what can fill it

1. `manage_articles` `operation: "list"` with `status: "READY"` — written, waiting for a date.
2. Not enough ready? `get_content_ideas` `operation: "ideas"` for saved ideas, or with `generate: true` and `count` to write new ones from the business profile; `operation: "topic_opportunities"` for the keyword opportunities found at onboarding. Free. Ideas become articles through `write-article` or `bulk-content-run`.

## 3. Schedule

1. Propose a cadence. Defaults: 1–2 posts per day for an established site, 3–4 per week for a new one. Spread clusters out rather than publishing one topic in a burst. Quick wins and seasonal topics first.
2. Show the schedule as a table (date, time, title, keyword) and get approval.
3. `publish_articles` `operation: "schedule"` per article with `article_id` and `scheduled_for` (ISO date-time, future). Run it with `dryRun: true` first, then with `confirm: true` once the user has said yes.

## Notes

- Scheduling is a paid feature. If the tool returns an upgrade link, pass it on as is.
- To pull an article off the calendar: `operation: "unschedule"` (also needs `confirm: true`).
