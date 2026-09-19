# Evidence Rule (Evidence-Based)

> Adapted from [testdouble/han](https://github.com/testdouble/han)
> `han-research/references/evidence-rule.md` (MIT, © 2026 Test Double, Inc.).
> The substantive rule is theirs; the mappings to this repo's doctrines are
> ours. This file and any skillet spec are exempt from the plain-language
> standard — it is read to decide whether a rule was met.

This rule defines what evidence means in the research swarm, how to
characterize how strong it is, and what to do when no evidence exists at
all. It supplements `yagni-rule.md`, which a skill needing both loads
directly: YAGNI answers *is there any evidence to include this item?*; this
rule answers *once it passes, how confident should you be, and what is the
response when no evidence is available?*

In this repo, the rule composes with three existing doctrines rather than
replacing them:

| Our existing doctrine | The han concept it instantiates |
|---|---|
| `spec.md` § Evidence — a figure moved between documents carries its conditions | proximity-to-origin (evidence carries what produced it) |
| `spec.md` § Evidence — a claim names what was not checked | no-evidence labeling with a reopen trigger |
| `dotfiles/docs/JUDGE-SELECTION.md` — judges measured by calibration, never asserted | the corroboration gate, applied to model judgments |

## Trust classes

Every artifact a skill or agent cites carries one of three trust classes:

- **Codebase** is the trusted current-state anchor. The current source code,
  current tests, current configuration, current build output — and, in this
  repo, the **deployed tree** is codebase evidence once `chezmoi status` is
  clean; the source tree is codebase evidence always. When codebase evidence
  contradicts other evidence, treat the codebase as authoritative on what
  the system does today.
- **Web** sits outside the trust boundary. Documentation, blog posts, Stack
  Overflow, GitHub issues, RFCs, vendor whitepapers, LLM-generated content.
  Web sources can be wrong, stale, adversarially shaped, or contextually
  misapplied.
- **Provided** is user-supplied material. Files pasted in, links handed to a
  skill, screenshots, transcripts, session artifacts. Apply
  interested-party scrutiny; hold to the same standard as web sources.

## The three principles

### Principle 1: Proximity to origin (heuristic, not ranked tier list)

Evidence drawn from closer to the originating event or data carries more
weight than evidence at greater remove. Apply this as a heuristic, not as a
ranked tier list. A numbered ordering of source types looks operational but
breaks at the first tier boundary — the house lesson is the same one stated
in `spec.md`: a measured number without its conditions is an assertion.

The principle inverts in three contexts:

- **Formal-methods or specification-compliance contexts**: the
  specification is the authoritative artifact. Our standing instance: a
  binary's actual wire format beating upstream documentation — measured on
  the real binary wins (the herdr status grammar).
- **Regulatory or contractual contexts**: the regulation wins.
- **Pre-incident observation of intended behavior**: a passing test proves
  only that tested inputs behaved correctly for tested code paths. Passing
  and failing tests are not symmetric evidence — the same asymmetry the
  house doctrine states as "a mechanism that can decline is proven to
  relent, both directions."

### Principle 2: Independent corroboration (web-source scope)

**A web claim that bears on a recommendation and has no independent
corroboration is marked single-source and cannot be the sole basis for the
recommendation.**

The gate does not apply to codebase evidence. A single file path at a
specific line number is not weakened by being a single citation; the current
source code is the current state of the system. The asymmetry is
intentional.

When sources contradict each other, surface the conflict: record both, name
the disagreement, let the reader judge. Silently picking the agreeable
source is the failure mode the gate prevents. When codebase and web evidence
disagree, the codebase wins on what the system does today; add "continue
with the current approach" as a named alternative.

### Principle 3: Explicit no-evidence labeling

When a claim has no evidence at any tier, label it. Defer the dependent
decision. Name the concrete trigger that would justify revisiting.

Do not collapse "no evidence" into "very weak evidence" — different states.
A claim with very weak evidence still gives something to test against; a
claim with no evidence gives nothing. Proceeding as if you had something is
how cargo-culting takes root. The response is the same defer-with-trigger
pattern YAGNI uses: a measured metric, an incident class, a customer
commitment, a regulation taking effect, a dependency landing. Aspirational
triggers do not qualify.

## How to apply

When producing a judgment: name the trust class per claim; apply the
corroboration gate to web claims; cite codebase claims at
`repo/path:line`; label and defer no-evidence claims with triggers.

When reviewing a judgment (fusion council): check trust classes are named;
check single-source web claims are marked and do not stand alone; check
no-evidence claims are labeled and deferred, not silently treated as weak
evidence; surface contradictions rather than picking the agreeable source.

When the rule and YAGNI both apply: YAGNI Gate 1 first — inclusion. This
rule characterizes quality. They do not collapse into one.

## Escalation

Claims that fail the corroboration gate and cannot be corroborated are
**never silently accepted**. They surface to the user with the single-source
label so the choice to act is conscious. The user always wins; an override
is recorded with rationale.

## What this rule is not

- **Not a replacement for YAGNI's evidence test.**
- **Not a ranked tier list** — proximity is a heuristic.
- **Not a codebase-evidence corroboration gate** — the gate is web-only.
- **Not a bar for academic rigor.** The bar is operational: you can tell
  where a claim came from, how strongly it rests, and what would change your
  mind.
- **Not an excuse to refuse to commit.** When evidence is strong enough to
  act on, act. Label honestly; do not gather until certainty — certainty is
  rare, calibrated confidence is the goal.
