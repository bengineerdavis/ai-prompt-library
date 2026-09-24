# Research and proposed principles

Save research that may become a project principle under `research/<topic>/` before
turning it into a decision. This directory holds evidence and reasoning, separate
from the research workflow skill under `skills/research/`.

## Active records

| Topic                                                        | Status                                                                                                    |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| [Escalation writing](escalation-writing/README.md)           | Public evidence and design decisions for a new spec-only skill; private voice-policy integration pending. |
| [GitHub CLI read permissions](gh-read-permissions/README.md) | Global configuration proposal only; no permissions applied.                                               |

## Preserve the reasoning

A small topic can use one README. Split sources, cases, or decisions into separate
files only when their size makes that useful. Record:

- The question, requirement, owner, and status.
- The proposed principle and the evidence supporting or challenging it.
- Source URLs, the exact version consulted where available, and the access date.
- What was verified, what was inferred, and what remains unknown.
- Alternatives considered and why they were rejected.
- The decision, approval status, and links to the resulting specification or rule.
- The last source review, its result, and the next review trigger.

On promotion, keep the evidence and link it to the decision. A rejected proposal
still records something useful. Add new findings and explain supersession rather
than silently replacing the evidence behind an earlier choice.

Keep confidential source content, derived private summaries, and private locators
outside this public repository. Public accessibility is not blanket permission to
redistribute a source. Paraphrase findings with attribution; verify rights before
including substantial excerpts or snapshots.

## Check upstream deliberately

Keep a canonical URL for finding updates and a pinned revision for the material
used as evidence. Mark unversioned pages explicitly. A revision identifies content;
it does not guarantee future availability or establish that its guidance is current.

Recheck affected sources before adopting or revising a principle, after relevant
tool or policy changes, or when contrary evidence appears. Record "checked,
unchanged" as well as changes. Separate finding an update from reviewing whether
it changes the decision. A quarterly manual review of active, important sources
is the initial recommendation, not an installed schedule or a measured optimum.

## Choose how to retain a source

| Mechanism                                       | Use when                                                                                                                                        |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Canonical and pinned links with review metadata | Research needs traceable evidence; this is the default.                                                                                         |
| A small licensed snapshot                       | Specific material must work offline or remain available at runtime. Preserve applicable attribution, license, and modification notices.         |
| A Git submodule                                 | A substantial upstream repository is an actual local dependency, and its checkout/update overhead is justified. Importance alone is not enough. |

A submodule records a commit in the parent repository. Normal initialization and
update check out that recorded commit; `update --remote` selects an upstream
revision instead. Adopting a new revision still requires review and a changed
gitlink in the parent. Ordinary clones do not automatically populate submodules.
A working checkout may also contain local edits, so copying it is not proof that
the pinned content is pristine.

For portable skills, include necessary public runtime material inside the skill.
Do not rely on links into this directory or assume the distributor initializes
submodules. Do not place a private submodule inside a directory that will be copied.

## Sources for source maintenance

Reviewed in the 2026-09-23–24 research session. These are unversioned documentation
pages; recheck them before adopting a new retention mechanism.

- [Git submodule model](https://git-scm.com/docs/gitsubmodules).
- [Git submodule commands](https://git-scm.com/docs/git-submodule).
- [Git checkout behavior](https://git-scm.com/docs/git-checkout).
- [GitHub file permalinks](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files).
- [GitHub licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
