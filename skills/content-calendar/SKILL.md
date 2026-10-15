---
name: content-calendar
description: Plan and manage the publishing schedule for SEOsorted articles — see what is drafted, ready, scheduled and published, and schedule ready articles on a steady cadence. Use when the user asks about their content calendar, publishing schedule, why posts stopped going out, what's publishing next, or wants to schedule articles.
---

# Content calendar

Scheduled articles auto-publish to the connected CMS. If nothing is scheduled, publishing stops — the most common reason "the blogs stopped".

## Steps

1. `get_site_overview`: next scheduled posts, counts by status, the default publishing integration.
2. `manage_articles` `operation: "list"` with `status: "READY"` for articles waiting to be scheduled.
3. Propose a cadence. Defaults: 1–2 posts per day for an established site, 3–4 per week for a new one. Spread clusters out rather than publishing one topic in a burst. Order by opportunity (quick wins first) and seasonality.
4. Show the proposed schedule as a table (date, time, title, keyword). Get approval.
5. `publish_articles` `operation: "schedule"` per article with `scheduled_for` (ISO date-time, future) and `confirm: true`. Use `dryRun: true` first if the user wants to preview.

## Notes

- Scheduling is a paid feature. If the tool returns an upgrade link, pass it on as is.
- No CMS connected: scheduled posts cannot publish. Send the user to Settings → Integrations (WordPress, Webflow, Shopify, Strapi or a webhook).
- To pull an article off the calendar: `operation: "unschedule"`.
