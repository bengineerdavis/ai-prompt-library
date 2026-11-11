---
id: APL-18
title: 'Gate rule files for PII: a learned rule must not carry the capture that taught
  it'
status: To Do
created_date: 2026-11-11 03:24
labels:
- pii-redaction
- rules
- privacy-gate
- security
priority: high
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A learning loop that learns from real customer data is a privacy leak with extra steps, and the existing schema has a real hole.

Rules are shareable, exported, versioned artifacts by design (docs/pii.md: policy becomes "a generated, shareable artifact versioned by provenance"). So a rule derived from a real capture can carry that capture with it:
- a pattern embedding a real org slug, hostname, internal path or account id
- a rule id or description derived from a customer name
- THE EXAMPLES FIELD. build_rule requires examples and only requires them to be NON-EMPTY (pii_rule.py:131-132). Inducing a rule from a real capture invites pasting the real value as the example. The schema forces evidence but does not force the evidence to be synthetic.

That is the hole: the field that exists to make rules honest is the field most likely to carry a real customer value out of the building.

Three mitigations, to be evaluated and adopted as a set:
1. Mechanical: a lint over rule files rejecting any example value that also appears in the corpus being redacted. Turns an honor system into a check.
2. Gate at the boundary: run every candidate rule file through the PII gate before write or export, treating the rule file as shareable output like any other artifact.
3. Discipline: induce from STRUCTURE, never values. A rule may only be derived from a stated invariant that makes a match PII by definition — "AKIA + 16 uppercase alphanumerics is an AWS key id", "three dot-separated base64url segments starting eyJ is a JWT". "These 40 strings look alike" is overfitting with a regex, not a rule.

Also decide provenance: a rule learned from a capture should record enough to justify itself (which rule category, which invariant, which date) WITHOUT recording which customer. Cross-reference support's task-74, which owns the raise-side learning loop and is currently a stub with no acceptance criteria.

Standing rule that governs this: fixtures are synthesized, never copied from real captures. A rule's examples are fixtures.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A rule file whose examples contain a value present in the source corpus is rejected, by a check and not by review alone
- [ ] #2 Rule files pass the PII gate before being written or exported
- [ ] #3 Written guidance exists for inducing from structure rather than values, with a worked example and a counterexample of what is not a rule
- [ ] #4 Rule provenance records the invariant and date without recording the customer
- [ ] #5 Signed-off decision recorded on whether the 'examples must be synthetic' rule is enforced mechanically or by review
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
