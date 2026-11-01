# Skill-building with the ask-matt flow

How the ask-matt skill system (`~/.config/opencode/skills/ask-matt`) composes
with skillet-based skill authoring, so an agent can be used across every stage
of building a skill — from the foggy idea through the shipped, eval-covered
artifact.

This doc is the integration layer. It names which skill drives which stage and
where the hand-offs are. It does not restate each skill's internals: read the
named skill's `SKILL.md` before the stage that references it.

## The two sides

- **ask-matt** is the *idea→ship* flow for software: grill → spec → tickets →
  implement → retro, with on-ramps (triage, diagnosing-bugs, wayfinder) and a
  vocabulary layer (domain-modeling, codebase-design) underneath.
- **skillet** (via `skillify` and `skillet-authoring`) is the *authoring
  machine* for skills: `spec.md` → rendered `SKILL.md` → optional eval cases →
  `validate`, landing in the library behind the dotagents distribution gate.

A skill is a small software artifact. Building one is therefore a legitimate
ask-matt flow whose "product" happens to be a skill rather than an app; skillet
is the compiler the flow drives.

## Stage mapping

| ask-matt stage | Skill-building action                                                       | Skill to invoke                                                                          |
| -------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Idea (foggy)   | Decide whether the skill is one well-scoped artifact or a multi-part family | `/grill-with-docs` (working dir) or `/grill-me` (no repo)                                |
| Sharpen        | Pin name, triggers, must-never-do, scope boundary — the spec's inputs       | `/grilling` primitive inside `/grill-with-docs`; `/domain-modeling` for overloaded terms |
| Spec           | Write `spec.md` (Intent / Triggers / Behaviors / Constraints)               | `skillify` (spec-writing stage) or `skillet-authoring`                                   |
| Author         | Render `SKILL.md` from the validated spec                                   | `skillet-authoring` (`instructions skill` + `validate`)                                  |
| Eval (opt-in)  | Write `evals/cases/*.yaml` for high-value scenarios                         | `skillet-authoring` eval branch, or `tdd` for the eval's verification command            |
| Ship/retro     | Commit, push, `dotagents install` behind the review gate; then reflect      | `/retro` (environment changes, not code)                                                 |

## Which authoring skill when

Two skills already cover skillet authoring; do not add a third.

- **`skillify`** — the *product-level* flow: a new skill end-to-end, interactive
  spec questions, land in the library, stop at the dotagents gate. Reach for it
  when the ask is "make me a skill for X."
- **`skillet-authoring`** — the *mechanic-level* flow: create/improve/migrate
  with the Skillet CLI, diagnose failing evals, migrate legacy `SKILL.md` /
  `SPEC.md` / `spec.yaml`. Reach for it when the ask is a specific authoring or
  eval operation on an existing skill, not a fresh product.

`skillify` is the user-invoked entry point; `skillet-authoring` is the reusable
discipline both `skillify` and an implementing agent reach for mid-stage. (A
`skill-creator` name has appeared in available-skill indexes but is not present
in `~/.agents/skills`; treat references to it as stale until it exists.)

## Stage-by-stage notes

**Idea → sharpen.** Use `/grill-with-docs` because it is stateful: it leaves the
interview in `GLOSSARY.md` and ADRs, which is exactly the paper trail a
`spec.md` needs to be written against next. Run it in the skill's working
directory (the library repo), not a scratch dir. The grilling discipline's
rule — "facts are the agent's job, decisions are yours" — means the spec's
*behaviors* are agent-synthesized but the *scope* and *must-never-do* are
human decisions, so confirm those before writing `spec.md`.

**Spec.** A skill spec's behaviors must be WHEN/THEN-observable; anything that
cannot be phrased so is not a behavior and belongs in Intent or is dropped.
This is the same seam discipline as `/tdd`'s "one red slice at a time" but on a
contract, not a test. `domain-modeling` earns its keep when a spec has an
overloaded term (e.g. "manage" doing install, update, and port at once) —
resolve the word before rendering the skill.

**Author.** The contract is `spec.md`; `SKILL.md` is derived. Every Skillet
command runs through `npx -y @sentry/skillet@latest`, never a bare `skillet`
binary. `validate` gates every step; the skill is not done while `validate`
reports errors.

**Eval.** Optional; add cases only when the user asks for them. eval is where a
skill's behavior becomes a mechanical check — this is the same "deterministic
checks graduate fastest" trust-funneling the repo's retro loop favors.

**Ship.** The distribution gate is a human review point, not a self-service
step: the author stops at `git add`/`commit`/`push` + `dotagents install` and
prints the commands. Do not conflate "authored and valid" with "installed and
live" — they are separated by the gate.

**Retro.** After shipping, `/retro` (in the session that did the work) asks
what would have made the *environment* better — a missing eval case, a thinner
spec, a steering note — so the next skill builds from a better setup. This is
the close of the loop, not a second authoring pass.

## Composition rule that governs all of the above

A user-invoked skill (a flow like `/grill-with-docs`) may invoke model-invoked
skills (disciplines like `skillet-authoring`, `/research`, `/tdd`, `/pr`), but
never another user-invoked flow. Sharpened: **flows don't nest; disciplines
do.** When a stage looks like it wants to nest a flow, demote the nested thing
to the discipline beneath it or inline it rather than spawning a second
orchestrator.
