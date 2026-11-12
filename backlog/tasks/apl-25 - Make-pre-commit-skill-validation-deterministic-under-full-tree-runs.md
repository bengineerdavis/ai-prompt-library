---
id: APL-25
title: Make pre-commit skill validation deterministic under full-tree runs
status: To Do
created_date: 2026-11-12 21:47
labels:
  - alint
  - skillet
  - pre-commit
  - diagnostics
references:
  - ../.alint.yml
  - ../scripts/check_skillet_freshness.py
  - ../.pre-commit-config.yaml
updated_date: 2026-11-12 21:47
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: while verifying APL-23 and APL-24 on a disposable current-main integration checkout, pre-commit run --all-files intermittently failed unrelated skill freshness checks and reported support-partner-deep-research fixtures missing. The referenced files were present before and after the failing run, direct Skillet validation passed, and direct alint full/changed checks passed on unchanged sources. Some subsequent full-hook runs passed without source changes; the failure therefore remains an execution-environment or concurrency discrepancy, not evidence that the fixtures are absent.

Ship:

- A tight red-capable reproduction of the first/full pre-commit failure that captures the failing child process, its working directory, relevant tool versions, and source hashes without exposing credentials or private configuration.
- A fix at the owning seam, or an explicitly documented upstream blocker, so the all-files gate reports the same skill validity and freshness as direct validation.

Constraints:

- Do not bypass alint, Skillet, or pre-commit, and do not silence the failing rules.
- Do not re-render unrelated skills merely to make the discrepancy disappear.
- Preserve synthetic fixtures and concurrent user work.
- Distinguish tool initialization races, working-directory problems, version skew, and formatter-induced hash rotation by measurement rather than assumption.

Surfaced during APL-23/APL-24 integration verification 2026-11-12; implementation is not authorized by those follow-ups.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 A repeatable or statistically characterized pre-commit reproduction captures the exact failing child and differentiates it from the passing direct invocation.
- [ ] #2 pre-commit run --all-files and direct alint/Skillet validation agree on unchanged inputs across repeated runs, or the upstream blocker is recorded with its evidence.
- [ ] #3 The original support fixture references and unrelated rendered skills are not changed merely to suppress the discrepancy.

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
