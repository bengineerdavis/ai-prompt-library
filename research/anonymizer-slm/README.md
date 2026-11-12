# Anonymizer SLM: implications for contextual pseudonymization

Status: source comparison and a narrow substitution probe completed 2026-11-11;
general model fitness, detection coverage, and downstream utility remain
unmeasured. This is an experiment record, not a model-adoption or release
decision.

## Requirement

Produce natural, context-faithful replacements for explicitly identified entities
using local models, while code preserves technical evidence and validates every
change. A candidate is disqualified as a work default if its license forbids the
intended commercial use. A passing substitution probe does not establish detection
coverage, anonymity, or fitness for another role.

## Verified sources

- [Anonymizer SLM series blog](https://huggingface.co/blog/pratyushrt/anonymizerslm),
  published 2025-08-27, reviewed 2026-11-11. This is an unversioned community
  article; recheck before changing the experiment contract.
- [Anonymizer-1.7B model card](https://huggingface.co/eternisai/Anonymizer-1.7B/blob/c6545f49718c76dcf03e26844fc5666813ad1583/README.md),
  revision `c6545f49718c76dcf03e26844fc5666813ad1583`, reviewed 2026-11-11.
- [Model repository metadata and file inventory](https://huggingface.co/api/models/eternisai/Anonymizer-1.7B),
  same repository revision, reviewed 2026-11-11.
- [CC BY-NC 4.0 legal code](https://creativecommons.org/licenses/by-nc/4.0/legalcode),
  reviewed 2026-11-11. This is a license constraint to review for the intended
  context, not a legal opinion.

No model was downloaded or run for this comparison. The background research
attempt returned a session log and wrote no report; these findings come from
subsequent direct retrieval of the sources above.

## What the source confirms

The source uses surgical `original`/`replacement` pairs rather than asking the
model to rewrite the whole prompt. That supports the prototype's central boundary:
a model proposes replacements; deterministic code validates and applies them.
The model card returns pairs through a `replace_entities` tool call, with no
`kind` field. Its model both detects and replaces PII. Our first experiment supplies
known fictional identities and measures only replacement generation, not detection.

The card's more detailed replacement policy is the main addition to our prototype:

- Preserve useful cultural, gender, and era context for private people; align
  family surnames; leave globally recognized public figures intact.
- Preserve an organization's industry, size tier, and legal suffix; distinguish
  private organizations from major public companies.
- Replace internal projects and codenames with neutral aliases of similar length.
- Preserve geographic context at a deliberately specified level.
- Shift private dates by small amounts while retaining the year and relative
  timing; leave public historic dates and holidays intact.
- Use format-valid replacements for identifiers, preserving useful domain class.
- Scale private monetary amounts by 0.8–1.25, retaining magnitude; retain public
  list prices and market caps.
- Change only embedded PII tokens inside quotations, not the surrounding text.

The blog's training metrics, GPT-4.1 comparisons, completion times, response
parity, and privacy claims are vendor-reported. They are not measurements on this
machine and do not support a fitness verdict. Its network proxy, traffic mixing,
and query-unlinkability claims are outside this local substitution experiment.

## Prototype changes made

- Return validated pairs from the substitution interface instead of parsing the
  untrusted response a second time in the measurement probe.
- Require full replacement person names and aligned replacement email identities.
- Add deterministic, caller-selected private-amount scaling within 0.8–1.25.
- Add deterministic same-year ISO date shifts with a fixed offset.
- Ask the local model to preserve industry, size tier, legal suffix, and supplied
  cultural context; add a synthesized legal-suffix measurement case.

The unit suite, including the existing redaction tests, must remain green. The
redaction layer and its release gate are unchanged.

Local harness check, 2026-11-11: the installed Ollama endpoint answered a plain
`qwen3.5:9b-mlx` request and requests with `think=False`, temperature `0`, and
seed `42`. It returned `ResponseError: structured output is unavailable (status code: 501)` when `json_object=True`. The probe therefore requests JSON in prose
and still parses it strictly; it does not claim structured-output enforcement.
This local limitation invalidates the earlier twelve invocation failures as
model-fitness evidence.

## Local substitution measurement

Model: `qwen3.5:9b-mlx`, already installed, called through the LLM Ollama plugin
against loopback. Four synthesized incidents, three attempts each, using
`think=False`, temperature `0`, and seed `42`. This is not a statistically
adequate fitness evaluation and uses no customer-derived cases.

- **9/12 attempts passed every strict check.** Three incidents passed all three
  attempts; checkout failed all three on email/person alignment.
- **12/12 preserved the measured technical literals**, including error codes,
  versions, HTTP method/status, timings, counts, cloud-region labels, and the
  public Python reference.
- **12/12 removed the explicitly supplied identities**, retained the required
  name repetition count, and produced a changed private IPv4 address.
- The organization suffix case retained `GmbH` in all three attempts. The model
  chose plausible technology/data organization types in the observed synthetic
  outputs; that observation is not a measured semantic-similarity score.
- The checkout email uses `marv.v` for replacement person `Mara Vance`; `marv`
  is not a prefix of `Mara`. This is a genuine model relationship error, not a
  validator false positive. Follow-up runs reproduced it three of three times,
  and a regression test requires its rejection. Do not weaken this check to turn
  the failed case into a pass.
- The malformed-response fixture was rejected because it omitted supplied
  identities. Validation errors are surfaced by category; invocation exceptions
  do not print raw model output or credentials.

Observed attempt durations across the usable probes were approximately 2–10
seconds. These are individual request wall times under changing local load, not
throughput or the specialized model's claimed latency. Do not compare them to
the blog's 0.65-second report.

At this stopping point, **28 model-free tests pass**, including the existing
redaction suite. No files were committed.

## Remaining measurement gaps

- Industry and cultural similarity require contextual assessment with explicit
  synthetic expectations; a plausible name alone is not evidence of fidelity.
- Public/private classification must be measured separately from replacement
  generation. Supplied fictional identities do not exercise that decision.
- Cross-document mapping consistency and response re-identification need a
  separately designed experiment. A mapping never enters logs or retained output.
- Correlated contextual clues can reveal an identity even after every named
  entity changes. Replacing `Seattle` while retaining a unique combination of
  local landmarks and events illustrates the class; no replacement-only probe
  disproves that risk.
- The current generic local model uses our JSON pair format, not the specialized
  model's required tokenizer chat template, tool schema, and `/no_think` marker.
  Results from the generic driver cannot be transferred to the specialized model.

## Candidate disposition

**Adopt the pair-proposal architecture and explicit semantic policy for the
separate experiment. Do not adopt Anonymizer-1.7B as a work default.** Its model
card declares `cc-by-nc-4.0`; it may be evaluated only where that license permits
the intended use. A permissively licensed alternative or locally measured general
model remains necessary for the eventual engine decision.

Rejected for the first experiment: full-document rewriting, using vendor scores
as local evidence, treating the proposing model as its own privacy judge, and
claiming anonymity from exact-identifier removal.

Review trigger: before selecting a specialized model, changing the substitution
schema, or promoting the experiment into `context-anonymize`. Recheck the model
card and license at that point.
