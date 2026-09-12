# Ticket 44988 — Copperline Bank

**2026-08-26 14:05 UTC — customer (rae@copperline-bank.example)**
Cron monitor check-ins are being marked missed even though our jobs run on
schedule. We've confirmed the jobs complete via our own logging. This started
Monday. Org `copperline-bank`.

**2026-08-26 19:20 UTC — support (me)**
Which environment is this in? And can you share a monitor slug?

**2026-08-27 08:15 UTC — customer**
Monitor slug is `nightly-recon`. It runs in both our environments and we see
missed check-ins in the dashboard. Our SRE says the deploy that changed the cron
schedule went out to staging first.
