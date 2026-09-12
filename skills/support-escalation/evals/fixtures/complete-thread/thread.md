# Ticket 44821 — Northwind Labs

**2026-08-24 09:12 UTC — customer (dana@northwind-labs.example)**
Since upgrading `@sentry/node` from 8.31.0 to 8.42.1 on Friday, none of our
unhandled promise rejections show up in Sentry. Handled `captureException`
calls still arrive fine. Org slug is `northwind-labs`, we're on Business.

Example issue that should have caught it:
https://northwind-labs.sentry.io/issues/6612094411/

**2026-08-24 14:40 UTC — support (me)**
Confirmed DSN is valid and quota is not exhausted (14% of monthly volume used).
Reproduced locally on 8.42.1 with a bare Express app — unhandled rejection does
not reach the ingest endpoint. Rolling back to 8.31.0 in the same app restores it.

**2026-08-25 08:03 UTC — customer**
We can't roll back, 8.42.1 has a fix we need for our OTel bridge. This is
blocking our on-call rotation from seeing async failures in production.
