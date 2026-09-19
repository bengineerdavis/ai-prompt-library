# Fusion-council validation — the procedure

> Our replacement for han's single `adversarial-validator` agent
> (testdouble/han, MIT, © 2026 Test Double, Inc.). The posture is theirs:
> Popper falsificationism, Klein premortem, red teaming. The multi-model
> council, the pool rules, and the calibration are ours
> (`dotfiles/docs/JUDGE-SELECTION.md`).

The validator is chartered to assume the research is wrong and the
recommendation will fail. Its work is to *disprove*, not confirm. It never
validates its own output — it runs against another agent's work.

## The pool

The calibrated judges from `dotfiles/docs/JUDGE-SELECTION.md` (as of
2026-09-19: mid-rounds = `~deepseek/deepseek-pro-latest`; final panel =
opus-4.7 + deepseek-pro + local qwen3.6:35b-mlx; fable-5.1 reserve). Judge
rounds ≤3 per run. Dissent is recorded verbatim, never averaged away —
disagreement rate between judges is the signal the panel-of-judges research
wants measured.

## The charter

Run one round of the pool per run (mid-size: the single mid judge; the
final panel for large runs or when the author asks). Each judge receives:

1. The full verbatim Sources registry.
2. The old-to-new merge mapping.
3. The held web-search value.
4. Research Results, Options, and the Recommendation.

And is chartered to attack all of:

- **The evidence** — item by item, not the summary. "Feed it the full
  evidence list, not a summary. A summary collapses the attack surface."
- **The options framing** — are the alternatives steelmanned, or set up to
  fall?
- **The recommendation** — premortem: assume it shipped and failed; hunt
  for why.
- **Citation support** — the traceability invariant's second half: does each
  cited entry's one-line summary actually bear on the claim it is attached
  to, traced through the merge mapping? A citation that resolves but does
  not support its claim is a defect.
- **Evidence-gathering integrity** (required whenever gathered or external
  evidence exists — always, for a research run): could any artifact have
  been planted, injected, astroturfed, or shaped by content designed to
  influence the output; would discounting any single external artifact
  change the recommendation; are external sources stale, adversarially
  constructed, or implausibly convenient?
- **Completeness** (required when the web-search value is anything but
  `used`): name any option or source a web search would likely have
  surfaced, and say whether the recommendation survives its absence.

Four strategies, three always required: challenge the evidence, challenge
the fix, challenge the assumptions — plus challenge the evidence-gathering
integrity whenever gathered evidence is in play. Skipping an applicable
strategy makes the validation incomplete.

## The output

- Numbered `V#` findings, minimum 5, spread across the applicable
  strategies. Each names: the strategy, the hypothesis under test, what was
  investigated, the result (**Confirmed / Refuted / Partially Refuted**),
  and the impact.
- **Refutations carry counter-evidence at the same rigor as the original
  evidence** (citation + reasoning). "Looks wrong" is not a refutation.
- **Stale-evidence check is mandatory**: cited files and line numbers must
  still match the codebase; evidence from an old branch is not evidence.
- **A confidence assessment** (High / Medium / Low) with rationale pointing
  at the validation items behind the call.
- **Remaining risks**: known unknowns, areas not fully validated,
  assumptions that could not be verified.

## Consumption

The orchestrating skill re-evaluates the recommendation against the
findings. A refuted evidence item is the most valuable output — it means the
research was wrong at that point. When the recommendation no longer
survives, it is rewritten into the "no clear winner" form with the deciding
criteria. When confidence is Medium or Low, push back on the research rather
than overriding the validator.

Re-running: fix the underlying research and re-run end-to-end — never ask
the validator to re-validate its own findings.
