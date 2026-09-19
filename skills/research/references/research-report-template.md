# Research report template

> Adapted from [testdouble/han](https://github.com/testdouble/han)
> (MIT, © 2026 Test Double, Inc.). One fixed structure, depth scaled to the
> band: every section heading is present on every run; what scales is the
> depth of each entry, never the set of sections. The `A#`/`V#`/`O#`
> citation identifiers survive any edit unchanged.

```markdown
# {Question, restated as the report's title}

## Summary

{The answer in brief. Plain language, no jargon, no artifact IDs — a reader
who stops here still has the answer. One phrase on how solid it is.}

**Confidence:** High | Medium | Low
**Web search:** used | not available | not reported

## Research Results

{The relevant findings, minimal technical detail. Every claim cites the
artifact IDs it rests on, e.g. "(A1)". Claims without independent
corroboration are marked inline `[single-source]`; reasoning, in
exploratory mode only, `[reasoning]`. Contradictions between sources are
surfaced, not resolved silently.}

## Options to Consider

{Present only when the question implies discrete alternatives; omitted
entirely for "how does X work" questions.}

- **O1. {Option name}** — steelmanned, in its strongest form. Trade-offs.
  Rests on: A1, A3. Evidence status.
- **O2. …**

## Recommendation

{The recommended option (referencing its O#) with its explicit evidence
basis: which parts rest on corroborated evidence, which on a single source,
which (exploratory only) on reasoning.

When the evidence does not support a single answer, this section reads
instead: **No clear winner** — the deciding criteria, named, and the
evidence that would settle it.}

## Validation

- **V1.** {strategy | hypothesis under test | what was investigated |
  Confirmed / Refuted / Partially Refuted | impact}
- **V2. …**

{Adjustments made in response: a recommendation that no longer survives is
rewritten above, not annotated. Then:}

**Confidence assessment:** {High / Medium / Low, with the rationale pointing
at the validation items behind the call}
**Remaining risks:** {known unknowns; areas not fully validated; assumptions
that could not be verified}

## Sources

| ID | Title / source | Link or location | Retrieved | Trust class | Summary (one line) | Evidence status |
|----|----------------|------------------|-----------|-------------|--------------------|-----------------|
| A1 | …              | …                | 2026-09-19| web         | …                  | corroborated by A2 |
| A2 | …              | repo/path:line   | —         | codebase    | …                  | — |

{A full prose summary is reserved for the sources the recommendation rests
on, below the table. The registry is always present, even on a minimal run.}
```
