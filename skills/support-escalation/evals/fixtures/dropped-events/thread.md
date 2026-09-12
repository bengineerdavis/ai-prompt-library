# Ticket 44944 — Acme Co

**2026-08-21 16:30 UTC — customer (chris@acme-co.example)**
We're missing errors. Our app logged 4,100 exceptions to our own logging
pipeline yesterday afternoon and Sentry only shows 380 for the same window.
Org slug `acme-co`, window was roughly 14:00 to 16:00 UTC on 2026-08-21.

**2026-08-22 10:12 UTC — support (me)**
Checked their quota — not exhausted, and no rate limit events on the account.
Checked their DSN — valid, single project. Their SDK is `@sentry/python` 2.14.0,
unchanged for six weeks. No client-side `before_send` filter in their config.

**2026-08-22 11:05 UTC — support (me)**
Internal note: could be SDK-side sampling or server-side ingestion. Nothing in
what we have separates the two — we'd need to know whether the events reached
our edge at all.
