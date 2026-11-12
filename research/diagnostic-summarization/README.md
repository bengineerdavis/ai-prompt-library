# Summarization for private diagnostic conversations

**Owner:** APL-20. **Status:** research complete; comparison designed, not run.
**Reviewed:** 2026-11-12. **Depends on:** APL-19 (evidence-spine research).

**Scope:** test summarization as both a **competing** and a **complementary**
approach to evidence-ledger rewriting for private, low-latency SaaS requests.

## Recommendation

**Include summarization as a first-class experiment arm, but not as generic
compression. Test task-conditioned, evidence-attributed summarization against
the evidence-ledger baseline and against summary-assisted extraction.**

Three distinct approaches are worth comparing on the same synthesized incidents:

1. **Direct summary (competitor).** A local model summarizes the incident into
   a short task-conditioned brief; deterministic checks gate it; the brief goes
   to the SaaS model.
1. **Evidence ledger (existing baseline).** A validated structured spine is
   rendered into a prompt, as designed in APL-19.
1. **Summary-assisted extraction (complement).** A bounded summary narrows the
   source for subsequent evidence extraction, with provenance retained back to
   the original text. This is only valid if the summary does not become an
   unverifiable intermediate that discards the evidence needed for validation.

**Do not assume summarization helps latency.** A direct summary may cost one
model call like the ledger's single-call candidate. Its benefit is smaller
prompt size and possibly simpler downstream reasoning, not necessarily fewer
local calls. Measure end-to-end latency, not prompt length alone.

**Do not use summarization to hide omissions.** A fluent summary can preserve
the broad issue while dropping the exact version, causal ordering, uncertainty,
or rare configuration that drives both diagnosis and re-identification. Every
arm must pass the same required-evidence and privacy checks.

## What the sources establish

### Summarization quality is task- and domain-specific

DIASUMFACT provides sentence-level factual error annotations for dialogue
summarization across six error classes; evaluated state-of-the-art detectors
reach only about 0.25 macro-F1 [1]. Dialogue summaries have their own error
profile, and detecting those errors is hard. This directly supports
fine-grained, source-backed checks for conversational incidents rather than
assuming a summary is faithful because it reads well.

"Summarization Is Not Dead Yet" finds human references retain advantages in
informativeness and faithfulness while LLM outputs are preferred mainly for
surface coherence and fluency, especially for claims requiring reasoning or
synthesis [2]. Fluency is therefore not evidence of fidelity for this task.

RNSum's extractive-then-abstractive approach to commit-log summarization reports
less noisy release notes at higher coverage than baselines, yet still a
significant gap in essential-information coverage against human references [3].
Technical change logs are close to diagnostic material; coverage of essential
facts is the metric that matters, not summary readability.

### Task conditioning and evidence attribution are the credible variant

SUnsET shows that query-focused summarization with **unstructured evidence
spans** (rather than fixed sentence/paragraph granularity) produces more
relevant and factually consistent evidence and summaries across five LLMs and
four datasets, and that existing systems struggle to copy and cite such spans
("lost-in-the-middle") [4]. This supports requiring provenance from each summary
claim back to the source, and warns that relevant evidence may be scattered.

ReMEMBER formalizes streaming dialogue summarization under a fixed budget and
finds the central challenge is recovering **gap-resolving evidence** the current
window presupposes, not how much history is accessed [5]. For multi-turn SaaS
exchanges, a summary that omits the earlier fact a pronoun or correction depends
on is a correctness failure, not a compression trade-off.

These results motivate a **diagnostic, evidence-attributed** summarization arm,
not a generic "summarize this incident" prompt.

### Summarization is not a privacy mechanism

TAB and the adversarial-anonymization literature (reviewed in APL-19) establish
that privacy depends on direct and quasi-identifying combinations, not just
named entities [6][7]. A summary can remove a name while preserving the exact
timestamp, rare configuration, and event sequence that re-identifies an account.
Summarization must therefore be evaluated for **inferential privacy**, not only
for factual coverage.

PAPILLON's SaaS-shaped pipeline reports that local prompt construction can
preserve response quality while reducing leakage, but its qualitative analysis
shows prompt creation can omit critical information or change the requested
task [8]. That is the exact risk the direct-summary arm must measure.

## Experiment design

### Arms

| Arm                                             | Pipeline                                                                           | Hypothesis                                                               |
| ----------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **A. Direct substitution** (control)            | Entity/secret replacement on the original text                                     | Preserves evidence but leaves the event fingerprint and placeholder soup |
| **B. Direct summary** (competitor)              | One task-conditioned local summary → checks → SaaS                                 | Cheaper, adequate context; risk of omissions and drift                   |
| **C. Evidence ledger** (baseline)               | Validated spine → bounded render → checks → SaaS                                   | Best fidelity/privacy control; more structure to maintain                |
| **D. Summary-assisted extraction** (complement) | Bounded summary → evidence extraction with source provenance → checks → SaaS       | Smaller input for extraction without losing required evidence            |
| **E. Selective summary + ledger** (complement)  | Deterministic spans + task-conditioned summary constrained by the validated ledger | Combines privacy generalization with evidence guarantees                 |

Arm B is the true competitor to C. Arms D and E test whether summarization earns
its place as a stage rather than a replacement. A is the incumbent to beat.

### Conditions and measurements

Use the six synthesized conversations specified in APL-19 (deployment/authorization
failure, worker version mismatch, retry storm, public documentation, rare
configuration + regional outage, three-turn correction/pronoun/follow-up).
Each fixture independently labels events, required facts, uncertainties, direct
identifiers, quasi-identifiers, and expected answer characteristics.

Measure **separately**, never as an aggregate score:

- **Factual coverage:** required event/evidence recall; unsupported-claim and
  false-causal-link rates.
- **Temporal/causal fidelity:** ordering preserved; correlation not turned into
  causation; corrections and pronoun references resolved.
- **Privacy:** direct values/secrets absent; mapping never emitted; independent
  adversarial attribute inference and named clue combinations.
- **Utility:** diagnostic answer correctness, evidence use, calibrated
  uncertainty, next-step relevance against labeled outcomes.
- **Latency/resources:** p50/p95 end-to-end and per-stage latency, local call
  count, prompt/output sizes, resident models, refusals and timeouts.
- **Compression:** output length relative to source, reported separately from
  latency so a smaller prompt is not mistaken for a faster pipeline.

Record model, quantization, prompt version, temperature, seed, cache state,
resident models, date, and host for every run. Use repeated independent runs for
stochastic behavior; three attempts are a smoke signal, not a fitness verdict.

### Fault injection

Prove the checks can fail on each arm:

- delete one load-bearing event from the summary;
- reverse deploy/failure order or assert causation;
- reintroduce a direct identifier in a later turn;
- leave two harmless clues that jointly identify the account;
- drop the earlier fact a pronoun depends on;
- force malformed output, an empty entity list, or a timeout.

Any direct leak, missing required evidence, or unverified SaaS forwarding is a
blocking failure for that arm.

## Decision criteria

- **Choose B (direct summary)** only if it matches C on required-evidence
  recall, temporal/causal fidelity, and privacy while being measurably faster or
  simpler. If it wins on fluency but loses any load-bearing fact, reject it.
- **Choose C (evidence ledger)** when provenance and validation matter more
  than brevity; it remains the reference for privacy-critical releases.
- **Adopt D or E** only if summary-assisted extraction preserves required
  evidence with source provenance and reduces measured latency or model calls
  versus C. If the summary becomes an unverifiable bottleneck, drop the stage.
- **Keep A** wherever any restructuring would change technical meaning.

No arm is adopted from published scores. Every judgment above is a hypothesis
until measured locally on synthesized incidents.

## Relationship to APL-19 and APL-13

- **APL-19** remains the completed evidence-ledger and council study; this task
  adds summarization as a sibling comparison without altering its conclusions.
- **APL-13** owns re-identification resistance. Summarization supplies candidate
  cases (summary-omitted identifiers, preserved clue combinations) but does not
  claim to solve inference resistance.
- The release engine is unchanged. All arms are separate experiments.

## Sources

Accessed 2026-11-12. Performance claims are author-reported on the authors'
corpora, not local measurements.

1. Zhu, Qi & Lau, [Annotating and Detecting Fine-grained Factual Errors for
   Dialogue Summarization](https://aclanthology.org/2023.acl-long.377/), ACL
   2023 (DIASUMFACT; six error classes, ~0.25 macro-F1 detectors).
1. Liu et al., [Summarization Is Not Dead
   Yet](https://aclanthology.org/2026.emnlp-main.402/), EMNLP 2026 (human
   references stronger on informativeness/faithfulness; LLMs on fluency).
1. Kamezawa et al., [RNSum: A Large-Scale Dataset for Automatic Release Note
   Generation via Commit Logs Summarization](https://aclanthology.org/2022.acl-long.597/),
   ACL 2022 (extractive-then-abstractive; essential-information coverage gap).
1. Wright et al., [Unstructured Evidence Attribution for Long Context Query
   Focused Summarization](https://aclanthology.org/2025.emnlp-main.95/), EMNLP
   2025 (SUnsET; evidence spans improve relevance/consistency; lost-in-middle).
1. Min & Song, [Don't Scroll Back: Missing-Evidence Memory for Streaming
   Dialogue Summarization](https://aclanthology.org/2026.findings-emnlp.1075/),
   Findings of EMNLP 2026 (ReMEMBER; gap-resolving evidence under fixed budget).
1. Pilán et al., [The Text Anonymization Benchmark
   (TAB)](https://aclanthology.org/2022.cl-4.19/), Computational Linguistics
   48(4), 2022 (direct/quasi-identifiers; privacy vs utility).
1. Staab et al., [Language Models are Advanced
   Anonymizers](https://arxiv.org/abs/2402.13846v2), ICLR 2025 (adversarial
   inference; attacker-dependent limits).
1. Siyan et al., [PAPILLON: PrivAcy Preservation from Internet-based and Local
   Language MOdel ENsembles](https://arxiv.org/abs/2410.17127v1), NAACL 2025
   (quality/leakage trade-off; prompt creation can omit or distort the task).

### Review triggers

Revisit if the target latency budget, SaaS threat model, or a measured
summarization failure class changes. Add new synthesized cases for omissions,
causal drift, and cross-turn evidence gaps before adopting any summary stage.
