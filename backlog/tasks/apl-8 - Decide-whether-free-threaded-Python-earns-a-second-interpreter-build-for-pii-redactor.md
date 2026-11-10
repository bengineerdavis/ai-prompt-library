---
id: APL-8
title: Decide whether free-threaded Python earns a second interpreter build for pii-redactor
status: To Do
created_date: 2026-11-10 23:08
labels:
- pii
- performance
- deferred
- research
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: the author wants first-class support for free-threaded Python and its concurrency. Measured on 2026-11-10 before committing to it: the answer is that it buys nothing measurable here, and the measurement should be preserved so this is not relitigated from intuition.

Environment facts (2026-11-10):
- mise python3 3.14.10 has the GIL enabled: sys._is_gil_enabled() True, Py_GIL_DISABLED 0.
- Homebrew python3.14 also has the GIL enabled.
- mise's python registry has NO free-threaded variant (1124 versions, no 't' tag).
- Homebrew python-freethreading exists (3.15.2, installs as python3.15t). uv can also fetch cpython-3.14.0+freethreaded.
- So free-threaded means a SECOND interpreter build, which conflicts with the mise-managed-tools preference since mise cannot install it.
- One point in its favour: pii-redactor imports only stdlib (os, re, shlex, shutil, subprocess, sys, tempfile, collections, pathlib), so no C extension can silently re-enable the GIL.

Measurement (14-core Apple silicon, synthetic support-thread text, all detectors firing, deterministic pass only):
- Serial: 8.7 MB/s (4 MB in 0.46 s; 40 MB in 4.62 s).
- multiprocessing 8 workers: 40 MB in 0.71 s = 56 MB/s = 6.49x speedup, match counts identical to serial (1,109,406).
- 4 workers spawn: 3.61x. 2 workers: 1.90x.

Conclusion: multiprocessing captures the available win on the ordinary GIL-enabled interpreter. Free-threading optimizes a stage that is ~1% of wall clock on the motivating 2 GB case (228 s of regex against ~5.7 h of model calls at 1 s per 100 KB chunk). Ordinary threads already overlap the model pass because subprocess.run releases the GIL while waiting.

Open question the measurement does NOT answer: whether _sre matching actually runs concurrently under a free-threaded build. CPython's re does not release the GIL on the GIL-enabled build, and this was not benchmarked on a 't' build.

Revisit when: mise grows a free-threaded variant, or opt-in parallel model calls exist and make layer 1 a larger share of wall clock (with 8-way model concurrency layer 1's 228 s becomes ~8% of a 43-minute run rather than ~1%).

Relevant prior art: raise docs/conventions.md C52 (never truncate; chunk to budget).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The recorded measurement is reproduced or contradicted on a free-threaded build, with conditions stated
- [ ] #2 Whether _sre matching runs concurrently under free threading is answered by measurement, not by assumption
- [ ] #3 A recommendation on adopting a second interpreter build, with the mise-preference conflict and the ~1-8% single-threaded overhead (per CPython's HOWTO) both weighed
- [ ] #4 If deferred, the trigger conditions for revisiting are stated as concrete signals, not dates
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
