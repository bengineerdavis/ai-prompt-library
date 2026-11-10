---
id: APL-2
title: 'Prove chunk boundaries safe: carry window, edge rule, and bound the two unbounded
  detectors'
status: To Do
created_date: 2026-11-10 21:50
labels:
- pii
- streaming
- security
dependencies:
- APL-1
updated_date: 2026-11-10 21:50
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: chunking introduces a leak the current tool cannot have. jane.smith@example.com cut across a boundary matches no pattern in either chunk, is never seen whole by the model, and verifies clean in both halves.

Ship: a carry window read before each chunk, and an edge rule that turns an unproven boundary into a visible failure.

Also documents a deliberate behaviour change: har_cookie_json (r'("cookies"\s*:\s*\[)([^\]]*)("?\])') and har_auth_json's ([^"]*) match across newlines with no length bound, so no fixed carry can ever be proven sufficient against them. They become single-line (add \n to the negated classes) and rely on the structural path, where a whole top-level value is one atom and a multi-line cookies array still matches.

Prior art: raise docs/conventions.md C52 (chunk on a structural boundary, never truncate) and raise text_redact's determinism-owned substitution.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A detector match spanning two adjacent lines is redacted, not passed through because neither chunk held it whole
- [ ] #2 A match touching either edge of the carry+chunk window widens the carry and rescans; past the bound the run fails rather than emits
- [ ] #3 har_cookie_json and har_auth_json are bounded to a single line, with a test pinning the change and the spec recording it
- [ ] #4 Pretty-printed JSON containing a multi-line cookies array is still fully covered via the structural path
- [ ] #5 No rendered output can be produced whose boundary was never proven safe
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
