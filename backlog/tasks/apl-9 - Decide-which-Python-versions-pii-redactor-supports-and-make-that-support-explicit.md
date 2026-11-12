---
id: APL-9
title: Decide which Python versions pii-redactor supports, and make that support explicit
status: To Do
created_date: 2026-11-10 23:19
labels:
  - pii
  - python
  - compatibility
  - research
  - deferred
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: the script claims Python 3.9 compatibility (`from __future__ import annotations` keeps `X | None` annotations working), but nothing enforces or tests that claim, and streaming adds features whose availability varies by version. The author wants multi-Python support explored rather than assumed.

The concrete conflict already found (2026-11-10): `tomllib` arrived in 3.11, and /usr/bin/python3 on this Mac is 3.9.6 with no tomllib at all. So on an unprovisioned box there is NO stdlib TOML parser at any size. Streaming makes this visible: TOML structural handling would silently behave differently by interpreter version, which is worse than refusing.

Version-dependent surface to settle:

- `tomllib` — 3.11+. Absent on 3.9/3.10.
- `from __future__ import annotations` — keeps PEP 604 (`X | None`) annotations parseable on 3.9. Already in use.
- Free-threaded builds (`python3.15t`) — 3.13+, a different interpreter build entirely; see APL-8.
- `multiprocessing` start methods — macOS default spawn, Linux default forkserver in 3.14, fork unavailable on Windows. `--concurrency` must not depend on a method that is missing.
- `json.JSONDecoder.raw_decode` — available across the supported range (verified on 3.9 and 3.14); `scan_once` is NOT a class attribute on either, so incremental JSON must use raw_decode.

Interpreter inventory on this machine (2026-11-10): mise python 3.14.10 (GIL enabled), Homebrew python3.14, /usr/bin/python3 3.9.6. mise registry offers 3.11.14, 3.12.13, 3.13.13, 3.14.x.

The decision needed: a floor (3.9? 3.11?), whether the floor is enforced or merely documented, and whether CI runs more than one version. Note the tension with the mise-managed-tools preference: the floor that matters most is the interpreter a fresh clone happens to have, which on macOS is the system 3.9.

Related: APL-4 (TOML/binary/stdin limits), APL-8 (free-threaded build).

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 A stated minimum Python version, with the reasoning recorded and the rejected alternatives named
- [ ] #2 The version-dependent surface is enumerated (tomllib, annotations, multiprocessing start methods, JSON decoding) with the chosen behaviour at and below the floor
- [ ] #3 Behaviour is identical across supported versions, or the run refuses with an explicit message naming the version requirement
- [ ] #4 Either the floor is enforced by a runtime check, or the docs state plainly that it is not — no unenforced compatibility claim
- [ ] #5 If CI or tests can run more than one version, they do; otherwise the single version tested is named

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->
