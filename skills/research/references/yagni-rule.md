# YAGNI Rule (Evidence-Based)

> Adapted from [testdouble/han](https://github.com/testdouble/han)
> `han-research/references/yagni-rule.md` (MIT, © 2026 Test Double, Inc.).
> The substantive rule is theirs; the mappings to this repo's doctrines are
> ours.

YAGNI — "You Aren't Gonna Need It" — keeps specs, plans, code, and
operational machinery from accreting work that is not needed yet. The rule
is evidence-based, not absolute. Items survive when evidence justifies them;
items without evidence get deferred — recorded for later, never silently
dropped.

Every skill section, every abstraction, every config knob, every
observability hook is ongoing maintenance cost and a pattern future agents
will treat as load-bearing and copy. The bar for inclusion is "we need this
now and have evidence to prove it," not "we might want this someday."

The house already runs a sibling doctrine: `dotfiles/docs/TOPIC-RECIPES.md`
carries a YAGNI-flavoured catalogue threshold ("no speculative catalogues"),
and `spec.md` § Work refuses undefined work. This rule generalizes both.

## The two gates

### Gate 1: The evidence test (gate for inclusion)

Any committed item — feature behavior, spec section, code change,
abstraction, configuration option, standard, runbook, hook, alert, test,
plan step — must cite at least one piece of evidence that it is needed now.
Acceptable evidence:

1. **A user-described need** in the source artifact (task line, PRD,
   conversation with the author, stakeholder commitment).
2. **A named direct dependency** — another in-scope item literally cannot
   work without it; the dependent item must itself pass the evidence test.
3. **An existing production code path or contract that will break without
   it** — cite the file/path/function or external consumer.
4. **A regulatory or compliance rule that demonstrably applies today** —
   cite the regulation and how it touches the change. "Compliance might
   require…" is not evidence.
5. **A documented incident, a real alert that has fired, a real customer
   report, or a measured metric** showing the problem exists. Hypotheticals
   do not qualify; alerts that actually fired do.

If no evidence applies, the item is YAGNI — defer it, recorded with the
trigger that would justify reopening.

### Gate 2: The simpler-version test (gate for shape)

When evidence justifies an item, ask: **is there a strictly simpler version
that satisfies the same evidence?** A single function beats a class; a class
beats a hierarchy; a hierarchy beats a framework. One concrete implementation
beats an interface with one implementation. A literal beats a configurable
with a default. One end-to-end test beats one end-to-end test plus twelve
unit tests when it catches every realistic failure mode.

If a simpler version satisfies the same evidence, the simpler version
replaces the larger one. The larger version is YAGNI until the simpler one
demonstrably falls short.

## Named anti-patterns (auto-flag as YAGNI candidates)

- **"We might need…" / "for future flexibility"** — pure speculation.
- **"When we scale" / "for performance"** — scaling work without measured
  pressure.
- **"Best practice says…" / "the standard is…"** — practices that do not
  solve a problem this project actually has.
- **Symmetry/completeness** — "we have create, so we need delete"; tests
  for unreachable enum values.
- **Single-implementation interfaces** — abstractions before three concrete
  uses (Rule of Three).
- **Speculative configuration knobs** — options no caller sets, flags
  wrapping a single code path.
- **Defensive code at trusted internal boundaries** — validate at system
  boundaries; trust internal contracts.
- **Speculative observability** — instrumentation for failure modes that
  have never occurred; runbooks for alerts that have never fired.
- **SLOs for traffic the system does not receive; multi-region for
  workloads that have not proven single-region pressure.**
- **Indexes for queries that do not run; partitioning for data volumes the
  project does not have.**
- **Tests for code paths that do not exist yet.**
- **ADRs about decisions with no forcing function today.**
- **Standards about patterns the project does not actually use yet.**
- **Phases whose only justification is "completeness of the roadmap."**

## Applying it

When producing artifacts: state the evidence per item; move unevidenced
items to the artifact's `## Deferred (YAGNI)` with a reopen trigger; run the
simpler-version test on everything that passes Gate 1.

When reviewing artifacts: run the evidence test per committed item; raise a
YAGNI candidate finding; resolve by citing the missing evidence, replacing
with the simpler version, or moving to deferred.

**Escalation:** YAGNI candidates are never silently dropped. They surface to
the user as deferrals with the reopening trigger named. The user always
wins; a kept-against-the-rule item is recorded with rationale.

## Deferred (YAGNI) section format

```
## Deferred (YAGNI)

### {item name}
**Why deferred:** {which gate failed, with the specific reason}
**Reopen when:** {the concrete trigger — a metric, an incident class, a commitment, a dependency landing, a regulation}
**Source:** {where the item was originally proposed}
```

Omit the section entirely when nothing is deferred — never write empty stub
sections.

## What YAGNI is not

- **Not "never plan ahead."** Plan ahead when planning ahead *is* the
  evidence — a deadline, a commitment, a dependency requiring lead time.
- **Not "skip correctness."** Critical-path correctness passes Gate 1
  trivially; YAGNI applies to speculative hardening, not real exploit paths.
- **Not "never refactor."** Refactor when existing structure demonstrably
  impedes a change — that is evidence. Refactoring for "cleanliness" alone
  is YAGNI.
- **Not an excuse to skip user-described requirements.** If the author said
  they want it, that is evidence. The rule challenges what agents add on top
  of what the author asked for.
