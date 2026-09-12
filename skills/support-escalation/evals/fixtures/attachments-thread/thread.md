# Ticket 44930 — Rowan Health

**2026-08-24 10:15 UTC — customer (lee@rowan-health.example)**
Session replay stopped recording for our web app about three days ago. I've
attached the HAR file from a failing session and our SDK config so you can see
the setup. Org `rowan-health`.

[attachment: rowan-session.har]
[attachment: sentry.client.config.ts]

```ts
// sentry.client.config.ts
Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});
```

**2026-08-24 16:48 UTC — support (me)**
Config looks correct at a glance. I'll check the relay logs for their org and
follow up.

**2026-08-26 09:30 UTC — customer**
Any update? Still not recording.
