---
id: APL-12
title: 'Support commit gate is unpassable: pytest hook loses BETTERLEAKS_CONFIG'
status: To Do
created_date: 2026-11-11 02:54
labels:
  - support
  - gates
  - test-infra
  - bug
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Found 2026-11-10 while committing a redact.py fix. The `pytest` pre-commit hook in support/prek.toml runs `uv run pytest -q` with no environment, so `BETTERLEAKS_CONFIG` is unset. 22 tests then fail because they isolate `RAISE_DATA_HOME` into a tmp dir (tests/conftest.py:223), so `generated_rules_path()` points at a file that isn't there, and egress/robo-rev raise "no betterleaks config ... run `mise run leaks-config`".

Consistent with a repo comment at mise.toml:31 — "The pre-commit hook does not depend on this variable: it resolves the config through the repo's machine symlink (see prek.toml), so non-mise shells scan correctly too." The symlink exists (`.betterleaks.generated.toml -> ~/.local/share/raise/betterleaks.generated.toml`) and prek.toml passes `-c .betterleaks.generated.toml` to betterleaks. That covers the SCANNER. It does not cover the Python code paths: `raise_cli.egress._scan_config()` and `robo_rev.default_config()` read the env var, then fall back to the data home, and never look at the checkout symlink.

Reproduce (no change to the tree needed):
env -u BETTERLEAKS_CONFIG uv run pytest tests/test_egress.py -q
-> 5 failed, 29 passed
With the variable set: 34 passed. Full suite: 22 failed / 1563 passed unset, 1585 passed set.

So the documented invariant is false for the Python callers: the symlink makes the path resolvable for betterleaks, not for the code that decides whether it is configured. Effect: every commit in this repo fails its own gate unless the committer happens to have the variable exported, and the failure names a remediation ("mise run leaks-config") that does not fix it.

Options, in order of preference:

1. Make `egress._scan_config()` and `robo_rev.default_config()` resolve the checkout symlink too — one resolution order, matching what mise.toml already claims. Cheapest fix that makes the comment true.
1. Have the pytest hook run through `mise exec`, so hooks see mise.toml's env. Wider blast radius: every hook gains mise semantics.
1. Set `BETTERLEAKS_CONFIG` in the hook's env block. Narrow, but re-encodes a path in a second place and still leaves the documented claim wrong.

Recommendation: option 1. It is the only one that makes the stated invariant true rather than routing around it, and it fixes non-mise agent/IDE commits generally.

Check first whether this is intended to be caught by `leaks-config-current` — that hook does pass, it only checks staleness.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 A commit in support passes its own gate in a shell with no BETTERLEAKS_CONFIG exported
- [ ] #2 egress and robo-rev resolve the config the same way mise.toml documents, or the documented claim is corrected
- [ ] #3 A test pins the resolution order so the symlink path cannot silently regress
- [ ] #4 The full suite passes without any pre-exported environment variable

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
