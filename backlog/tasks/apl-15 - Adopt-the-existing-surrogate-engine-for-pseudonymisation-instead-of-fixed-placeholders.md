---
id: APL-15
title: Adopt the existing surrogate engine for pseudonymisation instead of fixed placeholders
status: To Do
created_date: 2026-11-11 03:15
labels:
- pii-redaction
- pseudonymisation
- design-reversal
- packaging
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
REVERSES an earlier decision in this session and supersedes part of APL-1..4.

Context: the requirement was clarified as pseudonymisation at EU quality (EDPB Guidelines 01/2025), preserving enough context for a model to reason over. Earlier the scope was fenced to placeholders only ([NAME], [EMAIL]), explicitly excluding a surrogate engine, a pii-map, and pseudonymisation. That fence does not meet the stated requirement: a fixed tag collapses every person into one referent, destroying the context the requirement exists to preserve. It was drawn before the requirement was clear.

What exists already, in ~/code/work/sentry/support:
- src/raise_cli/surrogates.py (196 lines) — Engine(ticket_id) maps (category, value) -> surrogate, consistent via a _seen dict, typed via 17 per-category generators, per-ticket salted (salt = sha256(ticket_id)[:8]), deterministic counters so re-runs reproduce. IPs land in RFC 5737 documentation ranges, hosts in RFC 2606 reserved TLDs, cards Luhn-valid. Pure stdlib + hashlib, no filesystem access.
- src/raise_cli/pii_map.py (83 lines) — persistence, schema 1, salt stored, append-only entries.
- Its docstring cites docs/pii.md "Surrogates must be consistent and typed" as the contract. That is the EDPB-relevant property set.

pii-redactor today has no pseudonymisation mechanism at all: fixed bracketed placeholders, no per-value consistency (verified: no surrogate or pseudonym logic in the 874-line script).

Scope of this task:
1. Decide and record HOW pii-redactor reaches the engine — shared package, vendored copy, or import from raise_cli. This is a packaging decision, driven by the APL-10 question of where the script lives. Do not duplicate the engine.
2. Wire layer 2's substitution step to emit stable typed pseudonyms rather than fixed tags, as an explicit MODE (see APL-16), never an implicit default.
3. Keep the ledger constraint (APL-3) intact: if the model proposes values, the engine owns substitution, so identities never ride in the model's text.
4. Do NOT port the map to disk inside pii-redactor unless a persistence requirement appears. The engine is in-memory by design; on-disk persistence is raise's concern and has its own retention story.

Do not grow a second surrogate scheme. If a generator is missing (e.g. realistic human names), that is a gap to fill in the shared engine or to source from NeMo Substitute (APL-14), not a reason to fork.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The packaging decision is recorded with its reasoning, and no second surrogate implementation exists in pii-redactor
- [ ] #2 A redacted run can emit stable typed pseudonyms, with the same value mapping to the same pseudonym across the whole run
- [ ] #3 Two different people in one document remain distinguishable in the output
- [ ] #4 Pseudonym mode is explicit; the placeholder behaviour is unchanged when it is not selected
- [ ] #5 The engine's type-preservation is exercised by a test (an email stays email-shaped, an IP stays in a documentation range)
- [ ] #6 The model never receives a real value in either mode
- [ ] #7 research/anonymization-models/README.md addendum (3) is linked from the decision
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
