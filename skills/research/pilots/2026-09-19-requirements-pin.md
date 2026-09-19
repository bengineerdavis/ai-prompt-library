# Pilot — should `dotfiles/requirements.yml` pin its ansible collections?

Research-swarm pilot, 2026-09-19. Process: `skills/research/SKILL.md`
(adapted from testdouble/han). Size: **medium** (2 domains, 4 options,
codebase+web reach). Roster (4): analyst A (ansible pinning practice),
analyst B (supply-chain/reproducibility + engineered sub-angle), codebase
lane, fusion-council validation (medium band → 1 judge, deepseek-pro).
Evidence mode: **strict**. Machine-note: the web-isolation contract was not
mechanically enforced by the dispatch tool (see V3/V4) — recorded, not
hidden.

## Summary

**Pin, yes — the exact shape is unsettled.** The evidence strongly supports
pinning the two collections over leaving them unpinned (official docs,
practitioner consensus, and general IaC/supply-chain guidance all converge),
and this repo's own queued task already carries the reproducibility
rationale. But the validation refuted the initial recommendation (exact pin
with manual bump-on-regrade): without update automation it contradicts the
pinning guidance's own caveat, and a bounded range trades grade-linkage for
staleness-safety. **No clear winner** between the surviving shapes; the
deciding criteria are named below. The engineered sub-angle came back as
designed: a demonstrated supply-chain *attack* risk to this repo has **no
evidence**, and that path (defer-with-trigger) was exercised for real.

**Confidence:** Medium
**Web search:** used

## Research Results

- `requirements.yml` `version:` accepts exact pins and bounded ranges
  (`>=X,<Y`); absent `version:` means latest-at-install with no lockfile —
  every install is a silent re-roll (A1, corroborated A2, A5) (C1: both
  entries are unpinned).
- Practitioner consensus converges on pinning for prod/CI; unpinned is
  "quick testing only" (A5, corroborated A6). Official docs give the
  reproducibility rationale (A1). No ansible-lint enforcement rule exists
  [no-evidence].
- General supply-chain guidance names pinning as the mitigation for
  compromised/vulnerable dependency pulls, with the explicit caveat that
  pinning inhibits security updates **unless paired with update tooling**
  (A7, corroborated A8, A9, A10).
- Update tooling: Renovate has a dedicated ansible-galaxy manager (A3);
  Dependabot does not support Ansible (A4). This repo has neither wired up.
- Ansible-specific incidents: Galaxy availability outages (A11); one
  single-source, unverified client-side CVE claim (A12); **no documented
  malicious-collection compromise found** [no-evidence] — absence of a hit,
  not proof of absence.
- This repo's collections are load-bearing: dozens of topic tasks invoke
  `community.general.*` (C3); installed today: community.general 13.0.1,
  community.docker 5.2.1 (C4, captured with a clean `chezmoi status` and a
  verified in-sync deploy).

## Options to Consider

- **O1. Pin exact** (`community.general: 13.0.1`, `community.docker:
  5.2.1`), bumps deliberate ("bump-on-regrade"). Rests on: A1, A5–A8, C2,
  C4. Weakened by: the update-tooling caveat (A7/A8) — no automation exists
  here, so bumps likely never fire (V1, V5, V8 of the council).
- **O2. Pin bounded** (`>=13.0.0,<14.0.0`). Installs still receive
  minor/patch updates without new tooling. Rests on: A1, A3, A9. Weakened
  by: a bounded range can still install 13.x ≠ the graded 13.0.1, so the
  grade-linkage concern in C2 persists.
- **O3. Stay unpinned.** Contradicted by A1/A5–A8 and by C2's own queued
  rationale; every install re-rolls.
- **O4. Pin exact + adopt Renovate** for bump PRs. Rests on: A3, A7/A8's
  update-tooling mitigation. Requires adopting a new automation surface —
  a scope decision this question cannot make for the author.

## Recommendation

**No clear winner** among O1, O2, and O4 — the validation refuted O1 as
initially framed (confidence in it: Low) and the deciding criteria are the
author's to weigh:

1. **Automation appetite** — adopt Renovate (→ O4) or keep updates
   deliberate (→ O1 with a named re-grade cadence, or O2).
2. **Grade-linkage tightness** — the support-grade record is versioned
   against 13.0.1 (C2, C4); exact pins preserve that linkage (O1/O4), a
   bounded range loosens it (O2).
3. **Staleness tolerance** — O1 without automation means collections freeze
   until a break; O2 keeps minor/patch flowing; O4 automates bumps.

What the evidence *does* settle: **O3 (unpinned) is refuted** — the
reproducibility rationale (A1, A5–A8) and the repo's own queued task (C2)
both point against it.

## Validation

- **V1. Challenge the fix | O1-without-automation contradicts the
  dossier's own caveat** — A7/A8 say pinning inhibits security updates
  unless paired with update tooling; O1 pairs it with nothing.
  **Confirmed.** Impact: high — the recommendation as first framed would
  freeze collections indefinitely.
- **V2. Challenge the evidence | "demonstrated" overstatement** — the
  reproducibility risk is structural (fresh installs can diverge from the
  graded version, C2+C4) but no divergence or breakage has actually
  occurred here. **Partially Refuted** as worded; reworded above.
  Impact: medium.
- **V3. Evidence-gathering integrity | the web-isolation contract was not
  mechanically enforced** — analyst B's brief forbade codebase access, but
  the dispatch machinery (a subagent running inside the repo with file
  tools) allowed local reads; B returned local evidence (L1–L3),
  reclassified as codebase-class C1–C3. **Confirmed** as a process
  violation. Impact: medium — the file facts are independently checkable,
  but the isolation control needs a dispatch mechanism without repo file
  access (or a cwd outside the repo).
- **V4. Same strategy | deployed-tree gate held** — `chezmoi status` was
  clean and the deployed copy verified in sync before the codebase evidence
  was captured. **Confirmed** (the gate worked). Impact: positive.
- **V5. Options framing | O4 dismissed without sufficient justification** —
  A3 supports pin+Renovate; the initial recommendation gave no strong
  reason to reject it. **Confirmed.** Impact: high — drove the rewrite to
  no-clear-winner.
- **V6. Citation support | production/CI consensus over-applied to a
  personal non-CI repo** — A5/A7/A8 are organizational-grade guidance.
  **Partially Refuted** as context transfer. Impact: medium —
  reproducibility still matters at this scale, but the production-grade
  framing is weaker here.
- **V7. Citation quality | A6's "multiple independent guides" is
  unauditable; A12 is single-source** — both weaken the incident-basis
  claims, not the core reproducibility argument. **Confirmed.** Impact:
  low-medium. A live-fetch audit of A6 and a second source for A12 remain
  open.

**Confidence assessment:** Medium — pinning-over-unpinned is corroborated
across independent sources; the recommendation *shape* is genuinely
unsettled, which is why this report ends at no-clear-winner rather than a
forced pick.

**Remaining risks:** manual bump processes may never fire; transitive
collection dependencies stay unpinned either way; the A12 CVE claim is
unverified; A6's consensus may include content-farm sources; the isolation
breach means codebase evidence should be independently rechecked (they were
captured this run with the gate, mitigating this).

## No evidence yet

### Unpinned collections pose a demonstrated supply-chain attack risk to this repo
**Why no evidence:** the five YAGNI categories were applied —
user-described need, direct dependency, and code-path-divergence are met
(those establish *reproducibility* risk, not attack risk); no regulation
applies to a personal two-machine repo; no incident has fired, no metric
exists, no monitoring exists to fire one. Searches found no
malicious-collection compromise comparable to npm-class incidents.
**Reopen when:** the ansible-galaxy client CVE (A12) is confirmed by a
second independent source; a documented malicious-collection incident on
Galaxy is published; or a measured breakage occurs on this repo.
**Source:** the pilot's engineered sub-angle (this run, analyst B).

---

*Pilot of the research swarm (`skills/research/SKILL.md`), first run
2026-09-19. Process deviations and fixes feed back into the skill: the
isolation enforcement gap (V3) is a dispatch-machinery fix, queued with the
skill.*
