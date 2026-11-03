# RSS maintenance — 2026-11-03

The existing /index.xml URL is preserved. Hugo's embedded RSS structure is reused with full rendered content in description and content:encoded, absolute body URLs, URL-based GUIDs, and a maximum of 50 nonempty public entries. Missing original publication dates are omitted; no content dates are invented or changed. Draft, private, noindex and future-dated entries are excluded. RSS discovery uses the home feed. Existing sitemap and publishing schedules are preserved.

Validate after a normal Hugo build: `python scripts/check_rss.py <output-directory>`. The check uses only the Python standard library. Feed generation runs on each existing build/deploy. Hugo RSS documentation: https://gohugo.io/templates/rss/ . The template follows Hugo's Apache-2.0 embedded RSS structure.

Rollback: restore the source commit and existing successful Pages deployment recorded in the task's deployment evidence. Do not change hosting, secrets, DNS, or security settings.
Previous source: 20eac64327fe47d18d7f5f5bfcfc02cc4862ba75
Previous successful Pages deployment: 201b1a91-bbee-4dd1-9949-f4b8a713ac01

