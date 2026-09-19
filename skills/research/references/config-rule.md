# Config rule — `research/config.md`

> Adapted from [testdouble/han](https://github.com/testdouble/han)
> `han-research/references/config-rule.md` (MIT, © 2026 Test Double, Inc.),
> generalized: two files become one, because this library has one home.

The research skill reads one optional configuration file:
`skills/research/config.md` in the consuming repo — or, when the skill runs
from ai-prompt-library itself, `skills/research/config.md` beside the skill.
Absent file = no config; behave as the skill does without this rule, with no
note.

## Schema

Markdown: optional YAML frontmatter for scalar settings, named sections for
list settings.

- `default-swarm-size` (frontmatter key): the default band for skills that
  classify a swarm size before dispatching. Accepted values:
  `small | medium | large | dynamic`. A band value is adopted exactly as if
  passed as the size argument: skip signal-based classification, scale the
  caps, announce the band naming this file as the source. `dynamic` or
  absent leaves the skill classifying from the work's signals.
- `judge-pool` (frontmatter key): a path to the pool definition the
  validator reads, replacing the built-in reference to
  `dotfiles/docs/JUDGE-SELECTION.md`. Absent = built-in reference. A value
  naming a file that does not exist is not silently ignored: warn, name this
  config file, and ask whether to use the built-in pool or skip validation
  for the run.
- `## Extra agents` (section heading): one agent brief-reference per line,
  joining the analyst candidate pool. They compete under the same
  signal-based selection and band caps; an entry that does not resolve is
  skipped with a one-line note naming it.

## Precedence

First source supplying a usable value wins: (1) explicit author input to
the skill, (2) `config.md`, (3) built-in defaults. Per setting, not per
file. A blank or unusable value falls through the chain.

## Degradation and the one-line note

A bad config can never fail a skill run; the worst it can do is be ignored.
Show a one-line note only when content attempting a recognized override
cannot be used — naming what was ignored, which file it came from, and why.
Everything else passes silently. One problem, one note; two problems, two
notes.
