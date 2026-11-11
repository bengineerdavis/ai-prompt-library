---
id: APL-17
title: Let pii-redactor load rules, so learned detectors ship without a source edit
status: To Do
created_date: 2026-11-11 03:24
labels:
- pii-redaction
- rules
- adaptability
- cross-repo
priority: medium
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Requirement: the tool must adapt — build rules as vulnerabilities are found, and add patterns from data samples or structures during a session, instead of only shipping hard-coded detectors.

WHAT EXISTS (verified 2026-11-10, ~/code/work/sentry/support):
- src/raise_cli/pii_rule.py — Rule dataclass + build_rule validation. Fields: id, description, category, action, layer, confidence, surrogate, detect{type,pattern,keywords,validator,entropy,exclude}, emitters, examples, counterexamples.
- build_rule already enforces the discipline a learning loop needs: no examples -> refused ("a rule without examples carries no evidence"); no counterexamples -> refused ("a rule without counterexamples cannot be kept precise"); unknown emitter/validator, non-compiling pattern, wrong schema -> refused.
- src/raise_cli/pii_rules.py — LAYERS = ("base","user","project"), later wins by id, "a rule never silently disappears: disabling names a reason." Resolves base, ~/.agents/pii-rules.toml (user), <repo>/pii-rules.toml (project).
- EMITTERS = (in-process, report, betterleaks, redactor, text-redactor); DEFAULT_EMITTERS = (in-process, report), so new rules are OFF for redactor consumers until declared. Staged rollout is already the default.
- redact.py:1136 consumes rules with the "redactor" emitter; har_inventory.py:379 uses the text-redactor/redactor difference to keep free-text-only detectors off HAR profiles.

WHAT IS MISSING:
pii-redactor has NO rule path. Its DETECTORS are hard-coded in home/bin/executable_pii-redactor (chezmoi). So rule authoring exists in raise and rule DELIVERY to this tool does not.

SCOPE:
1. Choose a NEW emitter name for pii-redactor. Do NOT reuse "redactor" — that name already means raise's own HAR redactor, and reusing it would silently widen what raise's redactor does.
2. Compile rules -> the detector list pii-redactor loads. Replace the hard-coded DETECTORS with "built-ins + rule file" so the two cannot drift. A learned rule must not be able to silently shadow a built-in: conflicts are an error, not a winner.
3. Expose a --rules PATH flag so a run can be pointed at a project rule file. Default behaviour without the flag stays exactly as it is today.
4. Staged promotion: learned rules live in the project layer (scoped, uncommitted) and promote to base only once generalized. LAYERS is a fixed tuple today; staged promotion inside "project" needs no schema change, so do not add a "learned" layer unless a real need appears.
5. Give APL-2's detector-bounding work a home: the har_cookie_json and har_auth_json single-line bounding should land as a rule edit with a test pinning it, not a source edit with no rule identity.

This is not a redesign of the rule format. raise's schema is already validated, layered and emitter-scoped; rewriting it would lose all of that. The work is the compiler and the seam.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 pii-redactor can load a rule file and detect via a rule that is not in its built-ins
- [ ] #2 The new emitter name is distinct from raise's 'redactor', and raise's redactor behaviour is unchanged
- [ ] #3 A learned rule conflicting with a built-in is an error, not a silent override
- [ ] #4 Running without --rules produces byte-identical output to today
- [ ] #5 Rules are validated by raise's build_rule before use; an invalid rule file fails loudly
- [ ] #6 A rule reaches the tool from the project layer without being committed
- [ ] #7 The har-cookie/har-auth bounding change lands as a rule edit with a test
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
