# Evidence-spine rewriting for private conversational SaaS requests

**Owner:** APL-19. **Status:** research complete; architecture proposed for a
separate experiment, not approved for the release engine.

**Reviewed:** 2026-11-12. **Scope:** whether an outline can preserve diagnostic
context while reducing privacy exposure before a request reaches a SaaS model;
whether small-model panels improve that result; and how to test these claims
without making conversational latency unbounded.

## Recommendation

**Test a validated, session-stable evidence ledger with a bounded renderer.
Do not put a multi-stage attack–repair council on every turn by default.**

An outline is useful as a *controlled intermediate representation*, not as a
summary that a model certifies itself. A typical diagnostic spine should carry
explicit source-backed events, pseudonymous actors, actions and objects,
measurements, temporal ordering, evidence, uncertainty, and the downstream
question. Code should check the spine before a SaaS request and check the
rendered request afterward.

The latency requirement changes the architecture:

- Run deterministic secret and direct-identifier detection on every exchange.
- Use **at most one** local semantic extraction/rendering call on the initial
  fast-path candidate. If measurement shows that separate extraction and
  rendering stages are necessary, make that an explicit alternative rather than
  silently adding calls.
- Keep the pseudonym and event ledger stable for the conversation. A cached
  verified prefix or session state must be revalidated before reuse; do not
  re-summarize the entire conversation on every turn.
- Bound input size, generated output, total local calls, and wall-clock time.
  A deadline expires into a **local response or explicit refusal**, never into
  an unverified SaaS request.
- Run adversarial inference, counterfactual fidelity tests, judge calibration,
  and answer-quality comparisons **offline**. They establish confidence in the
  fast path; they do not belong inside every SaaS transaction.

**Do not claim that this proves anonymity or re-identification resistance.**
The fast gate can prove schema validity, absence of known direct identifiers,
preservation of declared evidence, and bounded behavior. It cannot prove that
the remaining event combination is unidentifiable. That is an evaluation target
and a disclosed residual risk, not a release-time guarantee.

### Council verdict

A small-model panel is worth testing for **independent candidate extraction and
adversarial review**, not for majority-vote safety certification and not by
default for whole-document rewrite fusion.

The preferred fusion is deterministic:

- union independently proposed privacy spans and evidence candidates;
- retain provenance and source locations;
- reject unsupported facts and conflicting pseudonyms;
- require agreement on structured **required** facts rather than prose;
- treat any credible high-confidence leak or contradiction as a veto;
- retain unresolved disagreement for offline review instead of averaging it
  into a confidence score.

For interactive use, test a small parallel panel only after a single small
model has a baseline. Compare it with the **same model sampled repeatedly**,
**different model families**, **one larger model**, and **retry/escalation**.
Parallelism may make latency approximately the slowest participating call, but
it does not eliminate additional compute, model-loading, memory, and scheduler
cost. TFLOPS are not an adequate latency measurement for this machine.

For offline use, an independent council can challenge extraction fidelity and
inferential leakage. It must not include the proposing model as an approving
judge of its own output. The repository's existing research procedure already
captures the right posture: dissent is recorded, never averaged away, and the
validator attacks another agent's work rather than its own
([procedure](../../skills/research/references/fusion-council-procedure.md)).
That procedure is useful for research validation; it is not a ready-made
interactive privacy gate.

## What the sources establish

### 1. Outlines help structure and control, not truth by construction

DOC separates detailed outlining from controlled drafting. Its human evaluations
report improvements in long-story coherence and outline relevance, but its
leaf-level relevance analysis still reports only 58.5% faithful short passages
with the detailed controller and notes remaining headroom. More importantly for
this project, fidelity **to a supplied outline** is not fidelity **to the
original evidence** [1]. DOC supports the separation of planning and rendering;
it does not support trusting an extracted outline.

µPLAN makes the intermediate plan an ordered entity sequence and reports better
informativeness and faithfulness for cross-lingual summarization. It evaluates
summary relevance, summary faithfulness, and plan relevance separately, and its
limitations say the resulting systems remain far from perfect [2]. This supports
a structured plan with explicit checks, not a single overall "faithful" label.

Discourse-driven planning likewise motivates separating explanation structure
from generation [3]. These are results in story, Wikipedia/cross-lingual, and
scientific summarization domains; they do not transfer as measurements to
Sentry support captures.

### 2. Privacy must address inference, not only identifiers

TAB annotates spans by whether they need masking, including direct and
quasi-identifiers, rather than treating a fixed named-entity taxonomy as
sufficient. It measures privacy protection and utility separately and explicitly
warns that quasi-identifiers are not a bounded semantic category [4]. Lison et
al. likewise argue for disclosure-risk reasoning and the privacy–utility
trade-off rather than sequence labeling alone [5].

Adversarial anonymization measures whether an independent model can still infer
protected attributes after rewriting. It shows that simple masking can leave
inferential clues intact and that feedback can improve that trade-off [6]. The
same work states the limit: success depends on the adversary's strength and on
available background knowledge; it cannot establish anonymity against arbitrary
adversaries. It also evaluates repeated inference and anonymization rounds, not
a conversational-latency budget. Do not import its scores as evidence for this
machine or this domain.

PAPILLON is closer to the SaaS setting: a trusted local model constructs a
minimal prompt for an untrusted remote model, then combines the answer with the
private query locally [7]. Its optimized pipeline reports quality preservation
for 85.5% of queries and privacy leakage for 7.5%; these are the authors'
measurements, not a privacy guarantee. Its qualitative analysis is especially
relevant: prompt creation can omit critical information or change the requested
task. That is why the proposed experiment must test task intent and required
facts, not just direct identifiers.

EDPB Guidelines 01/2025 treats pseudonymised data as personal data, requires a
defined pseudonymisation domain, and calls for assessing which attributes alone
or in combination permit attribution, including information accessible with
reasonable effort [8]. The guidelines explicitly allow omission and
generalisation of other attributes where needed, not merely replacing direct
identifiers. For a SaaS provider, assume the provider's context and accessible
external information belong to the risk analysis. Never send the local mapping
or raw prefix to the provider.

### 3. Evaluation needs coverage and contradiction checks, not prose similarity

QuestEval generates and answers questions in both directions between source and
summary, separating precision-oriented and recall-oriented signals [9].
QAFactEval finds question generation and answerability handling critical and
reports complementary value from entailment and QA approaches [10]. Use these
as design precedents for asking "which source facts survived?" and "which
generated claims are unsupported?"—not as plug-in proof of diagnostic utility.

LongEval supports fine-grained human judgments rather than one holistic score:
on SQuALITY its reported standard deviation drops from 18.5 for coarse judgments
to 6.8 for fine-grained judgments. Partial annotation reduces workload but
increases variance; source-highlight hints have limited usefulness [11].
For this project, that means small, explicitly labeled evidence and privacy
units, plus human review of difficult cases, rather than hundreds of vague
"looks safe" ratings.

NIST AI 600-1 calls for empirical capability evaluation, independent assessors,
red-teaming for privacy risks, construct-validity/error analysis for metrics,
and continuing feedback after deployment (MEASURE 1.3, 2.3, 2.10, 2.13) [12].
This supports a release/offline/operations split and rejects treating a handful
of successful demos as a general guarantee.

### 4. Judge panels have failure modes as well as benefits

Chen et al. demonstrate measurable misinformation, gender, authority, and
beauty biases in human and LLM judges, and attacks exploiting some of them
[13]. Xu et al. find self-bias in self-refinement and report benefits from
external feedback [14]. FIB finds that LLM evaluators can prefer factually
inconsistent summaries when those inconsistencies occur verbatim in the source
[15]. These results disqualify "the model approved it" as a safety argument,
especially when the same model proposed the rewrite.

Model ensembles can nevertheless help on some tasks:

- Agent Forest reports accuracy improvements from sampling and voting, but
  token usage grows with the number of agents and its tasks are not privacy
  rewriting [16].
- Mixture-of-Agents reports quality gains from heterogeneous proposers and
  aggregation, while explicitly warning that final-layer aggregation delays the
  first token [17]. Its cost analysis uses TFLOPS as a proxy, not measured
  conversational latency on this host.
- LLM-Blender motivates ranking and generative fusion [18], but its instruction
  following results do not show that an aggregator preserves source evidence or
  removes quasi-identifiers.
- Language Model Council reports benefits on highly subjective evaluation [19].
  Diagnostic evidence and privacy leakage are not equivalent to that task.
- "Judging with Many Minds" finds debate can amplify several biases, whereas
  meta-judging is more resistant in its setting [20]. Do not equate deliberation
  with independence.

The architectural conclusion is narrower than "more models are better":
**independent candidates may increase coverage; independent attack paths may
find failures; majority consensus cannot establish safety.**

## Proposed architecture

### Synchronous request path

1. **Bound and classify input.** Reject or locally handle inputs outside the
   tested size/type envelope. Never silently truncate evidence.
1. **Run deterministic detection.** Secrets and direct identifiers never reach
   a SaaS request. Existing redaction remains a backstop.
1. **Extract a candidate ledger.** Use structured local processing with a small
   fixed call budget. Every event includes source references, typed actors,
   action/object, measurements, ordering, evidence, and uncertainty. Keep
   temporal sequence separate from causal claims: "failure followed deploy" is
   not "deploy caused failure".
1. **Minimize at the ledger boundary.** Replace identities, generalize exact
   time/place/rare configuration where the downstream task does not need them,
   and omit irrelevant clues. Do not let the renderer decide ad hoc which facts
   matter.
1. **Validate the ledger.** Reject unsupported fields, invalid references,
   conflicting aliases, missing required evidence, and unexpected new numbers.
1. **Render the SaaS prompt.** Use a bounded template or one measured local
   renderer. The prompt asks the downstream question; it need not reproduce
   every sentence of the original incident.
1. **Re-run release checks on the rendered prompt.** Check forbidden direct
   values, required evidence, consistency with the local ledger, and length.
   Only then call the SaaS model.
1. **Handle the response locally.** If the task needs private identifiers for
   presentation, restore them only inside the local process. Never send the
   mapping or raw history to the provider.

### Session behavior

- A turn may add events or corrections; it must not silently replace earlier
  facts or pseudonyms.
- Cache only a **locally validated** prefix and state the assumptions under
  which it remains valid.
- Test at least one three-turn sequence with a correction, a pronoun-only
  follow-up, and a repeated entity.
- Incremental processing must remain within the same deadline and privacy
  checks as the initial request.
- When verification is unavailable, uncertain, or late, respond locally or
  refuse. Do not degrade to raw SaaS forwarding.

### Online versus offline responsibilities

| Concern                        | Synchronous request        | Offline evaluation              | Operational follow-up           |
| ------------------------------ | -------------------------- | ------------------------------- | ------------------------------- |
| Secret/direct-identifier scan  | Required                   | Regression corpus               | New synthesized classes         |
| Evidence/schema/provenance     | Required                   | Mutation/property tests         | Failure review                  |
| Contextual detection           | Bounded, measured          | Compare detectors/councils      | Recalibrate on new classes      |
| Attribute-inference resistance | Not provable               | Independent adversarial attacks | Concrete residual-risk examples |
| Answer/diagnostic utility      | Not judged by the proposer | Blind answer comparison         | Track classes of wrong answers  |
| Latency                        | Hard deadline and call cap | Warm/cold p50/p95 measurements  | Resource and timeout tuning     |

## Testing strategy

### Fixture design

Synthesize cases from the problem class, never from transformed customer
material. Start with six small diagnostic conversations:

1. deployment followed by authorization failures;
1. worker start failure with a version mismatch;
1. retry storm with exact latency and count evidence;
1. public documentation with no private identities;
1. a rare configuration plus regional outage suggesting an account;
1. a three-turn correction/pronoun/follow-up sequence.

Each fixture has independent truth labels for events, evidence, required facts,
direct identifiers, quasi-identifiers, uncertain claims, and expected answer
characteristics. Split development cases from held-out incident shapes and
unseen privacy traps. Include counterexamples where the correct result is
"insufficient evidence" rather than a confident diagnosis.

### Measurement layers

| Layer                      | Measure                                                                                                        | Evidence it provides                           | Limit / rejection trigger                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------- |
| Deterministic unit tests   | Schema, exact-span provenance, longest-first substitution, placeholders, structured JSON, mapping non-emission | Contract correctness without a model           | Any raw value in logs or SaaS payload blocks             |
| Property/metamorphic tests | Delimiters, escaping, nested JSON, alias stability, ordering, deadline refusal                                 | Robustness beyond handpicked examples          | Any invariant failure becomes a synthesized regression   |
| Extraction fidelity        | Required event/evidence recall; unsupported-field and false-causal-link rates                                  | Whether the spine preserves the source         | Missing load-bearing evidence invalidates a renderer win |
| Reconstruction fidelity    | Required-fact coverage; contradiction rate; event-order and uncertainty preservation                           | Whether rendering follows the validated spine  | Fluency cannot offset changed meaning                    |
| Direct privacy             | Known direct values and secrets absent; no mapping emitted                                                     | Direct-leak checks                             | Any direct leak blocks release                           |
| Inferential privacy        | Protected-attribute inference by independent attackers; named clue combinations                                | Measured residual risk under a stated attacker | No "anonymous" claim; misses feed new cases              |
| Downstream utility         | Answer correctness, evidence use, uncertainty, next-step relevance against labeled outcomes                    | Whether the SaaS request remains useful        | Equal-length/prose similarity is not a substitute        |
| Latency/resources          | p50/p95 end-to-end and per-stage latency, call count, input/output size, resident models, refusals             | Interactive fitness on this host               | Missed budget means simplify or refuse, not forward      |
| Judge validation           | Human-labeled hard-case agreement, false-pass and false-block rates, bias checks                               | Whether a judge is useful at all               | Uncalibrated judges remain advisory                      |

Report each dimension separately. Do not average them into a single safety or
quality score. For small experiments, show counts and exact uncertainty where
useful; do not present three repeated attempts as a stable model-fitness
verdict. Use repeated independent runs for stochastic behavior and record
model, quantization, prompt version, context, temperature, seed, resident
models, cache state, date, and host.

### Mutation and fault injection

Explicitly test that checks can fail:

- remove one required event or reverse event order;
- change correlation to causation;
- substitute a wrong but fluent replacement;
- reintroduce a direct identifier in a later turn;
- leave two individually harmless clues that jointly identify an account;
- inject a fabricated citation or unsupported number;
- make a model return malformed JSON, a tool call, or an empty entity list;
- force a timeout and verify that no SaaS request occurs.

A passing check alone is insufficient; demonstrate the corresponding failing
case as well. Never put secret values into failure messages or retained logs.

### Council ablation

Compare the following on the same synthesized cases, serially and then in a
resource-controlled parallel configuration:

1. one small local model;
1. three samples from that same model;
1. three genuinely different local model families;
1. one larger local model;
1. retry or escalation from the small model.

Measure unique valid detections, false additions, source-backed coverage,
contradictions, residual attribute inference, downstream answer quality,
wall-clock p50/p95, resident-memory pressure, and calls. Use a disjoint
validator for generated proposals. If diversity adds no measurable coverage or
attack recall over the simpler baseline, reject the panel. If parallel calls
miss the deadline, keep the council offline.

### Human evaluation

Use a small blinded hard-case set with source-backed atomic judgments. Ask for
independent labels for "supported", "missing required evidence",
"contradicted", "privacy clue", and "useful next step". Measure agreement and
judge false-pass/false-block rates. Human evaluation should calibrate automatic
checks and settle borderline examples, not bless a pooled quality score.

## Tooling decision

**Recommendation:** keep pytest/Hypothesis and the existing repeatable local
probe as the incumbent baseline. Add **Promptfoo as an optional offline matrix
runner only if its reporting is useful in practice**; do not introduce it into
the request path.

Verified against its installed CLI and documentation on 2026-11-12:

- installed `promptfoo` version **0.125.1** exposes `--repeat`, `--no-cache`,
  `--max-concurrency`, and JSON/JSONL output;
- it supports Ollama, custom Python providers, deterministic/custom assertions,
  latency assertions, and repeated model-graded assertions [21][22][23];
- disable caching for fresh repeated/latency measurements with `--no-cache`;
- disable telemetry with `PROMPTFOO_DISABLE_TELEMETRY=1`, and update notices
  with `PROMPTFOO_DISABLE_UPDATE=1` [24][25].

Promptfoo does not supply the domain-specific truth model, establish judge
validity, or make its latency number a SaaS end-to-end measurement. A Python
provider may measure the full pipeline, but must return the internal call count
and resource conditions explicitly. Run one tiny synthetic offline comparison
before adopting it; if it adds configuration without improving comparison or
reporting, retain the current probe.

DeepEval and Ragas were reviewed as alternatives. DeepEval integrates with
pytest and multi-turn evaluation, while Ragas offers experiment and metric
libraries [26][27]. Neither supplies a demonstrated advantage here over custom
Python contracts plus the small matrix runner. Their hosted/LLM-judge features
are not needed for the deterministic core and must not receive private
fixtures.

## Alternatives rejected for the proposed path

| Alternative                                      | Reason                                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------------- |
| Free-form whole-document rewriting on every turn | Unbounded semantic drift, difficult provenance, and added model latency         |
| Deterministic-only outline                       | Cheap but cannot establish contextual coverage or inference resistance          |
| A large attack–repair pipeline per request       | Conflicts with the conversational/transactional requirement; keep it offline    |
| Majority-vote "safe" certification               | Shared blind spots and judge biases can outvote a real leak                     |
| Complete-rewrite fusion by another model         | Adds a synthesis stage and can merge unsupported details; no fidelity guarantee |
| Same-model council only                          | Does not establish independent perspectives or coverage diversity               |
| One aggregate confidence score                   | Can hide a credential, causal error, or latency failure behind good averages    |
| Public benchmark scores as adoption evidence     | Different domain, conditions, and threat model; local measurement is required   |
| A hosted eval platform in the privacy path       | Adds an unnecessary data boundary and does not validate the domain contract     |

## Relationship to existing work

- **APL-13** owns re-identification resistance and the disclosure-risk gate.
  APL-19 borrows its threat model and supplies candidate cases; it does not
  declare that gate solved.
- The current redaction/span-substitution engine remains unchanged. This
  research proposes a separate experiment and cannot weaken its fail-closed
  layers.
- The earlier substitution probe establishes only that model-proposed pairs
  plus deterministic substitution can preserve selected technical evidence.
  It does not establish outline fidelity, conversation stability, anonymity,
  or interactive fitness.

## What remains unmeasured

No local model or panel was run for this research. The following are therefore
proposals, not findings:

- whether one small model can extract a sufficiently complete ledger within a
  conversational deadline;
- whether an independent council improves valid coverage enough to justify its
  resource cost;
- whether rendering adds useful fluency over a validated structured prompt;
- whether the SaaS model produces equivalent diagnostic answers;
- how much inferential risk remains after minimization.

The first experiment should be the smallest matrix that can answer these
questions and expose its own failures. Do not integrate the approach into the
release engine before that evidence exists.

## Sources

Accessed 2026-11-12. Publication identifiers are stable source locators;
unversioned documentation pages are marked for re-review before adoption.
All performance claims above are author-reported unless explicitly identified
as an installed-tool check.

1. Yang et al., [DOC: Improving Long Story Coherence With Detailed Outline
   Control](https://aclanthology.org/2023.acl-long.190/), ACL 2023, especially
   Table 6 and Discussion.
1. Huot et al., [µPLAN: Summarizing using a Content Plan as Cross-Lingual
   Bridge](https://aclanthology.org/2024.eacl-long.131/), EACL 2024, §5 and
   Limitations.
1. Liu et al., [Explanatory Summarization with Discourse-Driven
   Planning](https://aclanthology.org/2025.tacl-1.53/), TACL 2025.
1. Pilán et al., [The Text Anonymization Benchmark
   (TAB)](https://aclanthology.org/2022.cl-4.19/), Computational Linguistics
   48(4), 2022, annotation model and §6.
1. Lison et al., [Anonymisation Models for Text
   Data](https://aclanthology.org/2021.acl-long.323/), ACL-IJCNLP 2021.
1. Staab et al., [Language Models are Advanced
   Anonymizers](https://arxiv.org/abs/2402.13846v2), ICLR 2025, §§3–6 and
   Appendix A.6.
1. Siyan et al., [PAPILLON: PrivAcy Preservation from Internet-based and Local
   Language MOdel ENsembles](https://arxiv.org/abs/2410.17127v1), NAACL 2025,
   §§5–6.
1. EDPB, [Guidelines 01/2025 on
   Pseudonymisation](https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf),
   adopted 16 January 2025, public-consultation version, especially ¶¶60–61,
   76, 84, 131.
1. Scialom et al., [QuestEval: Summarization Asks for Fact-based
   Evaluation](https://aclanthology.org/2021.emnlp-main.529/), EMNLP 2021.
1. Fabbri et al., [QAFactEval: Improved QA-Based Factual Consistency
   Evaluation for Summarization](https://aclanthology.org/2022.naacl-main.187/),
   NAACL 2022.
1. Krishna et al., [LongEval: Guidelines for Human Evaluation of Faithfulness
   in Long-form Summarization](https://aclanthology.org/2023.eacl-main.121/),
   EACL 2023.
1. NIST, [Artificial Intelligence Risk Management Framework: Generative
   Artificial Intelligence Profile, NIST AI
   600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), July 2024,
   MEASURE 1.3, 2.3, 2.10, 2.13 and Appendix A.1.4.
1. Chen et al., [Humans or LLMs as the Judge? A Study on Judgement
   Bias](https://aclanthology.org/2024.emnlp-main.474/), EMNLP 2024.
1. Xu et al., [Pride and Prejudice: LLM Amplifies Self-Bias in
   Self-Refinement](https://aclanthology.org/2024.acl-long.826/), ACL 2024.
1. Tam et al., [Evaluating the Factual Consistency of Large Language Models
   Through News Summarization](https://aclanthology.org/2023.findings-acl.322/),
   Findings of ACL 2023 (FIB).
1. Li et al., [More Agents Is All You
   Need](https://arxiv.org/abs/2402.05120v2), 2024, §5.5 and Conclusions.
1. Wang et al., [Mixture-of-Agents Enhances Large Language Model
   Capabilities](https://arxiv.org/abs/2406.04692v1), 2024, §§3.3–5.
1. Jiang et al., [LLM-Blender: Ensembling Large Language Models with Pairwise
   Ranking and Generative Fusion](https://aclanthology.org/2023.acl-long.792/),
   ACL 2023.
1. Zhao et al., [Language Model Council: Democratically Benchmarking
   Foundation Models on Highly Subjective
   Tasks](https://aclanthology.org/2025.naacl-long.617/), NAACL 2025.
1. Ma et al., [Judging with Many Minds: Do More Perspectives Mean Less
   Prejudice?](https://aclanthology.org/2025.findings-emnlp.941/), Findings of
   EMNLP 2025.
1. Promptfoo, [Ollama provider](https://www.promptfoo.dev/docs/providers/ollama/)
   and [Python provider](https://www.promptfoo.dev/docs/providers/python/),
   unversioned documentation checked 2026-11-12; installed CLI 0.125.1 checked
   with `npx -y promptfoo@latest --version` and `eval --help`.
1. Promptfoo, [Deterministic
   assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/),
   unversioned documentation checked 2026-11-12.
1. Promptfoo, [Caching](https://www.promptfoo.dev/docs/configuration/caching/),
   unversioned documentation checked 2026-11-12; use `--no-cache` and
   `--repeat` together for fresh repeated calls.
1. Promptfoo, [Telemetry](https://www.promptfoo.dev/docs/configuration/telemetry/),
   unversioned documentation checked 2026-11-12.
1. Hypothesis, [property-based testing
   documentation](https://hypothesis.readthedocs.io/en/latest/), unversioned
   documentation checked 2026-11-12.
1. Confident AI, [DeepEval quickstart](https://deepeval.com/docs/getting-started),
   unversioned documentation checked 2026-11-12.
1. Ragas, [documentation](https://docs.ragas.io/en/stable/), unversioned
   documentation checked 2026-11-12.

### Review triggers

Revisit before implementation if the target threat model, SaaS provider,
latency budget, model/driver capabilities, or applicable privacy guidance
changes. Recheck unversioned tool documentation before installing any new eval
dependency. Treat measured false passes, cross-turn alias drift, direct leaks,
and unsupported causal links as reasons to stop the experiment and revise the
architecture rather than tune a composite score.
