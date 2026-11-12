---
id: APL-16
title: Make redaction vs pseudonymisation an explicit mode with honest output labelling
status: To Do
created_date: 2026-11-11 03:15
labels:
  - pii-redaction
  - spec
  - legal-framing
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Under EU law the two produce artifacts with different legal status, so the tool must not blur them.

EDPB Guidelines 01/2025 (pseudonymisation, adopted 16 Jan 2025): pseudonymised data is STILL personal data; attribution is prevented only without the additional information, and GDPR applies in full to it. Its executive summary states plainly that "prevention of attribution does not imply anonymity of the data."

EDPB Guidelines 02/2026 (anonymisation, v1.0 adopted 7 Jul 2026, consultation to 30 Oct 2026): anonymous data is outside GDPR, and requires three criteria — No Record Isolation, No Linkage, No Inference. The No Inference criterion accounts for external information AND the context the data was produced in ("no specific and meaningful inference can be drawn"). A ticket-shaped support capture essentially never clears that bar, because the escalation history is itself the identifying signal.

Consequence: a support-capture redaction tool that prints "anonymised" is making a false compliance claim, which is worse than claiming nothing. Under the older A29WP Opinion 05/2014 Table 6, pseudonymisation scores "yes" on all three criteria (singling out, linkability, inference) — that is the definitional point, not a defect.

Scope:

1. Two explicit modes: REDACT (placeholders, nothing linkable survives — today's behaviour) and PSEUDONYMIZE (stable typed surrogates, linkability is the product). No third implicit state.
1. Output labels the mode honestly. Never the word "anonymised" for a pseudonymised artifact.
1. The tool states what its gate proves: that no detected value survives (redact) or that values were consistently substituted (pseudonymise). It does NOT claim re-identification resistance — that is APL-13.
1. Where the surrogate mapping lives is a retention decision; if it persists, destroying it is what upgrades the artifact's status later (raise's pii erase, support task-52 as prior art).

Cite the guidelines by number and date in the spec. Do not paraphrase them into stronger claims than they make, and note that 02/2026 is still in consultation and may change.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 Mode is explicit in the CLI surface and cannot be inferred or defaulted silently
- [ ] #2 Output text and exit messaging state the mode and never label a pseudonymised artifact anonymised
- [ ] #3 The spec cites EDPB 01/2025 for pseudonymisation and EDPB 02/2026 for anonymisation, with adoption dates
- [ ] #4 The spec does not claim anonymity or re-identification resistance for either mode
- [ ] #5 A test pins that each mode's labelling appears in its output
- [ ] #6 Retention of any mapping is either explicitly out of scope or explicitly specified

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
