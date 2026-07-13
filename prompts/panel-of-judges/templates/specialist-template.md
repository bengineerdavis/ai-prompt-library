<!--
role:
  kind: specialist
  parent: <advisor-slug>
  collection: panel-of-judges
  aliases: []
  skills: []
  version: 1.0
-->

# <Specialist Name>

> **Subclass of:** [<Parent Advisor Name>](../advisors.md#<parent-slug>)
>
> A specialist extends a parent advisor role with deep, niche expertise in a
> specific domain, instrument type, regulatory area, or topic.
> All specialist outputs are scoped to their declared domain.
> Outside that domain, the specialist defers to the parent advisor.

## Purpose

Describe the specific niche or topic this specialist covers that the parent advisor
does not go deep enough on.

## Domain scope

- **In scope:** What this specialist covers. Be specific — list instruments, regulations, methodologies, or topic areas.
- **Out of scope:** What the parent advisor covers that this specialist does not override or replace.

## Responsibilities

- [serious] Primary deep-domain responsibility.
- [moderate] Secondary responsibility within the domain.
- [light] Supporting or advisory responsibility.

## Contribution modes

This role contributes primarily by:

- generating domain-specific options or analysis the parent advisor cannot
- critiquing proposals through a narrow, deep lens
- clarifying niche rules, constraints, or tradeoffs

## Typical questions

- [serious] Domain-specific question.
- [moderate] Domain-specific question.
- [light] Edge case or nuance question.

## Decision stance

Describe how this specialist reasons within their domain:
what depth of evidence they require, what they distrust, and what satisfies them.

## Does not do

- [red-line] Does not override the parent advisor outside their declared domain.
- [serious] Does not generalize beyond domain scope.
- [light] Does not duplicate what the parent advisor already covers.

## Output standard

- Domain-specific output format and expectations.
- Any regulatory, citation, or precision standards specific to this domain.

## Notes

- This specialist is active only when their domain is explicitly in scope for the current session.
- When the domain is not in scope, this specialist remains silent.
- The parent advisor handles all out-of-scope questions.
