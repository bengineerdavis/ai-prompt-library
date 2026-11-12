---
id: APL-24
title: Report Claude eval preflight failures by their actual error class
status: Done
created_date: 2026-11-12 21:36
labels:
  - eval
  - claude
  - diagnostics
references:
  - scripts/eval-claude
  - scripts/eval-claude-isolated
  - scripts/test_eval_claude.py
  - scripts/README.md
updated_date: 2026-11-12 21:38
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: the original wrapper follow-up, then numbered TASK-234, is absent from the authoritative APL store after its migration. A valid OAuth session produced a tool-schema error through a configured proxy, but scripts/eval-claude incorrectly reported an OAuth-refresh failure.

Ship:

- Error-class-specific, redacted preflight diagnostics and an explicit keyless OAuth interface that preserves --oauth as an alias.
- An opt-in project-settings isolation path covering both preflight and the actual Skillet eval, without changing user/project configuration.
- Regression tests through the public wrapper CLI, plus documentation of the supported path and its boundaries.

Constraints:

- Do not print credentials, private endpoint addresses, credential files, or provider request payloads.
- Do not silently change the configured endpoint or global Claude settings.
- Preserve the built-in Claude harness unless isolation is explicitly selected; preserve low-effort parity.
- Forward Skillet arguments without passing the wrapper's literal -- separator into case selection.
- Use a temporary skill copy and harness config for isolated evals; do not leave .skillet.yaml in the authored skill.

The maintainer chose keyless OAuth with --oauth retained as a compatibility alias 2026-11-11. Recreated under the APL prefix 2026-11-12 because the old TASK-234 record cannot be found.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [x] #1 Tool-schema responses are not labeled OAuth expiry, and the wrapper names the error class and supported retry without exposing sensitive configuration.
- [x] #2 Public-CLI regression tests cover schema errors, actual OAuth expiry, rejected keys, successful preflight, error-class precedence, redaction, and isolated eval wiring.
- [x] #3 python3 scripts/test_eval_claude.py passes.
- [x] #4 A real isolated credential preflight succeeds through scripts/eval-claude --keyless-oauth --project-settings --check, while any default-path provider/configuration blocker is explicitly recorded.

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

Implemented keyless OAuth as the explicit primary flag with --oauth retained as a compatibility alias; API-key and bearer environment credentials are removed for that process only. Error classes distinguish rejected keys, actual authentication expiry, tool-schema failures, timeouts, and other non-authentication failures without printing raw provider diagnostics. --project-settings isolates both preflight and the real Skillet eval through a temporary custom harness, preserves low-effort parity, and removes temporary configuration. Ten public-CLI tests pass on the worktree and current-main integration snapshot. Live keyless project-settings preflight succeeds. The real default path still rejects tool schemas through the configured provider/proxy and is reported as such, not as OAuth expiry. No global Claude settings or authored .skillet.yaml changed.

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

Delivered redacted error-class reporting, explicit keyless OAuth, and an opt-in isolated eval path with public-CLI regression coverage.

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->
