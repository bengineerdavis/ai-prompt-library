# Ticket 44860 — Tamarind Media

**2026-08-20 08:44 UTC — customer (jo@tamarind-media.example)**
Our source maps stopped resolving about a week ago. Every frame in every issue
shows minified output now. Affects all our environments. Org `tamarind-media`.

**2026-08-21 12:10 UTC — customer**
Correction — I went back through our CI logs. It actually started right after
our deploy on 2026-08-19, not a week ago. Sorry for the confusion.

**2026-08-22 15:35 UTC — support (me)**
Internal note: checked three of their recent releases. Minified frames reproduce
in their `staging` project only. Their `production` project resolves source maps
correctly on releases from the same CI pipeline.

**2026-08-23 09:02 UTC — customer**
Attaching our webpack config for reference.

[attachment: webpack.prod.js]
