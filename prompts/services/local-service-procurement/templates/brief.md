---
id: service-procurement-brief-template
version: 0.3.0
status: draft
artifact_type: reusable-template
supersedes: service-procurement-brief-template-v0.2.0
used_by:
  - interaction-questioning@2.3.2
  - local-service-procurement@0.3.0
  - service-provider-due-diligence-advisor@0.3.0
license: MIT
---

# Local Service Discovery & Procurement Brief

> **User starts here:** Describe what you need in your own words. You do not need to know the provider type, technical terms, risks, or questions yet.

## Natural-Language Start

```text
I need help with:

What I hope will be different when this is done:

Anything I already know, am worried about, or want to avoid:
```

## System-Built Discovery Summary

| Field                           | Content             |
| ------------------------------- | ------------------- |
| Initial request                 |                     |
| Inferred underlying outcome     |                     |
| Current session contribution    |                     |
| Confidence                      | low / medium / high |
| Known facts                     |                     |
| Safe defaults                   |                     |
| Material assumptions/open items |                     |
| Next action                     |                     |

## Things the Buyer May Not Know to Ask

| Consideration | Why it could matter | Status                                                   |
| ------------- | ------------------- | -------------------------------------------------------- |
|               |                     | research / safe default / ask next / resolved / deferred |

## Procurement Brief

```yaml
service_brief:
  goal: ""
  location_or_service_area: ""
  desired_completion: ""
  hard_deadline: ""
  scope_items_or_work: []
  known_conditions_or_materials: []
  hard_requirements: []
  preferences: []
  exclusions: []
  budget_ceiling: null
  target_value_band: ""
  one_coordinated_job: true
  communication_preferences: [phone, email]
  acceptance_criteria: []
```

## Advisor Contributions

| Artifact / role                        | Contribution                                                              |
| -------------------------------------- | ------------------------------------------------------------------------- |
| Interaction Questioning                | Goal stack, one high-value question if needed, understanding confirmation |
| Domain specialist                      | Methods, risks, terminology, and conditions buyer may not know            |
| Service Provider Due-Diligence Advisor | Gates, evidence needs, short provider questions, quote/acceptance fields  |
| Deep Researcher                        | Current evidence, candidate research, uncertainty labels                  |
| Pragmatist                             | Removes non-decision-changing questions and requirements                  |
| Systems Thinker                        | Identifies coordination, downstream, and maintenance impacts              |
| Note-Taker                             | Resumable record, decisions, defaults, and learning handoffs              |

## Required Procurement Outputs

- [ ] Candidate ledger with evidence labels
- [ ] Qualification gates
- [ ] Shortlist of 2–4 providers
- [ ] Vendor-specific 3–10 minute call sheets
- [ ] Comparison worksheet mapped to call questions
- [ ] All-in price/value context
- [ ] Booking, completion, and follow-up checklist

## Version History

### v0.3.0 — 2026-09-07

- Refactored around the Questioning v2.3.2 understanding-confirmation handoff.
- Simplified the user-facing start to three natural-language prompts.
- Clarified role boundaries and required outputs.
