# Ticket 44877 — Alder Systems

**2026-08-25 13:07 UTC — customer (marco@alder-systems.example)**
Our Next.js app crashes on boot after adding the Sentry SDK. We're using
`@sentry/node`. Stack trace below.

```
TypeError: cannot read property 'dsn' of undefined
    at initSentry (/srv/app/instrumentation.js:14:22)
    at Object.<anonymous> (/srv/app/server.js:3:1)
```

Org slug is `alder-systems`.

**2026-08-25 18:22 UTC — support (me)**
Asked for the SDK version and the contents of instrumentation.js. No reply yet.
