---
title: Local Service Procurement Kit
version: 0.3.0
status: draft
artifact_type: README
license: MIT
---

# Local Service Procurement Kit

A reusable kit for helping a buyer choose and use a local professional service provider when they may not yet know what matters, what questions to ask, or how to compare quotes fairly.

## What This Kit Does

Start with a natural-language need, such as:

> “I need someone to help with a problem in my house.”

The kit helps discover the real outcome, research and validate providers, create short calls, compare complete quotes, and plan booking/completion—without requiring the buyer to know the right vocabulary or fill out a long form.

## Artifact Map

| Artifact                                                                             | Role                           | Use it when                                                                                     |
| ------------------------------------------------------------------------------------ | ------------------------------ | ----------------------------------------------------------------------------------------------- |
| `interaction-questioning/SKILL.md` v2.3.2                                            | Discovery controller           | Always start here; it decides whether to ask, research, explain, default, calibrate, or proceed |
| `services/local-service-procurement/SKILL.md` v0.3.0                                 | Procurement workflow           | Use after questioning has reached a good-enough understanding                                   |
| `panel-of-judges/roles/specialists/service-provider-due-diligence-advisor.md` v0.3.0 | Provider-evaluation specialist | Add when vendors, quotes, process claims, or acceptance need scrutiny                           |
| `services/local-service-procurement/templates/brief.md` v0.3.0                       | Discovery/procurement record   | Store the evolving understanding, assumptions, outputs, and next action                         |

## How They Fit Together

```text
User speaks naturally
        |
        v
Interaction Questioning
- discovers goal, outcome, gaps, stakes
- asks one question only if useful
- confirms shared understanding
        |
        v
Local Service Procurement
- researches candidates
- applies qualification gates
- creates vendor calls and quote sheet
- recommends a booking/acceptance plan
        |
        +-------------------------------+
        |                               |
        v                               v
Provider Due-Diligence Advisor      Domain Specialist
- provider process/evidence         - category method/risk/material expertise
- gates/calls/quotes                - added only when needed
        |
        v
Note-Taker
- preserves decisions, assumptions, and reusable learning handoffs
```

### Role boundaries

- **Questioning** owns discovery discipline and the user-facing question, if any.
- **Local Service Procurement** owns the practical buying workflow once discovery is good enough.
- **Provider Due-Diligence Advisor** contributes provider-specific gates, evidence checks, call design, and quote normalization.
- **Domain Specialist** contributes category expertise only when it materially improves the decision.
- **Note-Taker** makes the session resumable and turns repeated discoveries into reusable improvement candidates.

This separation prevents duplicate questioning, long generic checklists, and unclear ownership.

## Quick Start

Use this as the opening request:

```text
Use local-service-procurement.

I need help with: [describe the service need naturally].

What I hope will be different when this is done: [desired result, if known].

Anything I already know, am worried about, or want to avoid: [optional].
```

You do **not** need to know:

- the exact provider category;
- technical methods or terms;
- which credentials matter;
- what a fair price is;
- every risk or failure mode; or
- the questions a vendor should answer.

The system should discover those things proportionately.

## Default Session Flow

1. Questioning reads the request and builds a goal stack: request, session task, underlying outcome, and session contribution.
1. It orients to the domain and identifies unknown unknowns.
1. It asks one question only if the answer materially changes the next action.
1. It gives a plain-English understanding confirmation once discovery is good enough.
1. Procurement research builds candidate ledger and gates.
1. Advisor/domain roles add only material expertise.
1. The system delivers shortlist, short calls, comparison sheet, price context, and booking/acceptance plan.
1. Note-Taker records reusable learning handoffs.

## When to Add a Domain Specialist

Add a domain specialist when a provider’s method, the asset/material, safety, regulations, or a technical condition could change the appropriate service or acceptance criteria.

Examples:

| Need                                  | Useful domain specialist                                               |
| ------------------------------------- | ---------------------------------------------------------------------- |
| Rug/furniture cleaning or restoration | Textile, rug, furniture-restoration professional                       |
| HVAC/plumbing/electrical              | Trade-aware technical specialist; regulatory/safety research as needed |
| Moving/storage                        | Moving logistics and valuation/coverage specialist                     |
| Auto repair                           | Vehicle diagnostic/repair specialist                                   |
| Home accessibility                    | Accessibility and occupational-use specialist                          |

Do not add a specialist merely to make the session look thorough.

## Output Expectations

The buyer should leave with:

- a plain-English problem/outcome summary;
- known facts, safe defaults, and material assumptions;
- an evidence-labeled candidate shortlist;
- pass/fail gates before score/rank;
- short provider-specific call sheets;
- one comparison sheet whose rows match call questions;
- a realistic all-in price/value view;
- a booking, completion, and follow-up plan; and
- a single next action.

## Installation Layout

Recommended repository placement:

```text
prompts/
  questioning/
    SKILL.md
    spec.md

  services/
    local-service-procurement/
      SKILL.md
      README.md
      templates/
        brief.md

  panel-of-judges/
    roles/
      specialists/
        service-provider-due-diligence-advisor.md
```

If the panel bundler supports optional roles/skills, add a `service-procurement` advisory-meeting variant that includes:

```yaml
participants:
  roles:
    - chair
    - facilitator
    - note-taker
    - pragmatist
    - systems-thinker
    - service-provider-due-diligence-advisor
skills:
  - interaction-questioning
  - local-service-procurement
  - deep-research
```

Add a domain specialist only for sessions that need one.

## Maintenance

- Keep the Questioning skill general and reusable across domains.
- Keep procurement workflow generic; do not hard-code rug cleaning, home repair, or one buyer’s preferences into it.
- Put stable category expertise in optional domain references or specialist roles.
- Use semantic versioning.
- Capture repeated question/outcome patterns as Note-Taker learning handoffs, then promote proven patterns into skills, roles, templates, or safe defaults.

## Version History

### v0.3.0 — 2026-09-07

- Initial README for the refactored kit.
- Documents boundaries, flow, artifact placement, quick start, role selection, outputs, and maintenance rules.
