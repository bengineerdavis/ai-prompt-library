# Anonymising models that rewrite rather than mask

Research for the question: which models can rewrite text so it becomes
privacy-safe while keeping as much usable context as possible for a downstream
model?

Investigated 2026-11-10. Sources pinned below; revisions recorded per claim.

## Short answer

**A generative rewriter exists, but not as a model you can point at a document.**
The thing that satisfies the question is a *pipeline*, and one is now open and
permissively licensed: **NVIDIA NeMo Anonymizer** (Apache-2.0), whose **Rewrite**
flow is exactly the requested capability — it reasons over the whole text,
covers latent/inferable signals, generates a rewrite, attacks it, and repairs
what leaks.

Two things this research settles that were open assumptions:

1. **Detectors cannot do this.** GLiNER, `openai/privacy-filter`, Presidio, and
   EternisAI's span mode all return offsets and labels. Something else must
   decide the replacement, and placeholder substitution (`[NAME]`) is what
   destroys downstream utility — the failure mode the question is about.
2. **A standalone "context-preserving rewriter model" does not exist as a
   first-class artifact.** The nearest thing is EternisAI's Anonymizer series —
   it is genuinely a rewriter in that it proposes *semantically equivalent
   replacements* rather than tags — but it replaces entities one at a time
   (returning an `original`/`replacement` list) rather than rewriting prose, and
   it is **CC-BY-NC-4.0 (non-commercial)**, which rules it out for work.

So: the capability is real, it ships inside a pipeline, the pipeline is
Apache-2.0, and its default configuration contradicts the local-only constraint
and has to be re-pointed.

## Comparison

| Option | Category | Rewrites prose? | Params / size | License | Local-capable | Deterministic | Verdict |
|---|---|---|---|---|---|---|---|
| **NeMo Anonymizer — Rewrite** | Pipeline: detect → plan → rewrite → attack → repair → judge | **Yes**, end-to-end | Model-agnostic; prompts any provider | **Apache-2.0** | Yes, but default is OpenRouter — must reconfigure | No (LLM sampling; repair loop) | **Recommended.** Only option that addresses latent entities |
| **NeMo Anonymizer — Replace** | Pipeline: detect → span substitute | No, span-level | Model-agnostic | Apache-2.0 | Same caveat | Substitution can be pinned | Useful stepping stone; keeps more utility than placeholders |
| EternisAI Anonymizer 0.6B/1.7B/4B | Rewriter of *entities*, not prose | No (returns replacement list) | 0.6B / 1.7B / ~4B, Qwen3 base | **CC-BY-NC-4.0** | Yes, fully | temperature 0.3 default; pinnable | **Rejected: non-commercial licence** |
| `openai/privacy-filter` | Span detector | No | 1.5B MoE token classifier | Apache-2.0 | Yes | Yes | **Detector only** — layer-2 detection, not a rewriter |
| GLiNER multi-PII (`urchade/gliner_multi_pii-v1`) | Span detector | No | ~0.4B, xlm-roberta | Apache-2.0 | Yes | Yes | **Detector only** — the incumbent span detector |
| Presidio | Framework around detectors | No | N/A (no model) | MIT | Yes | N/A | **Not a model.** Framework; adds recognisers, not semantics |
| Anonymizer-by-construction (arXiv 2603.17217) | Prompted local LLM substitution | Sentence-level rewrite | gpt-oss 20B / DeepSeek-r1 7B | Paper only, no weights | Yes | temperature-dependent | **Pattern, not artifact** — validates prompted rewriting |
| SFAA (arXiv 2601.14683) | Framework: detect/classify/adapt | "Context-aware rewriting" strategy | Phi 3.2 4B / LLaMA 3.2 3B | Paper only | Yes | Partly | **Pattern** — strategy taxonomy worth borrowing |
| On-device PII substitution (arXiv 2605.13538) | Detector + SLM surrogates | No | privacy-filter 1.5B + Bonsai 1.7B | Paper + code | Yes | Seeded | **Honest negative result** — see below |
| Redakto (arXiv 2608.18260) | Tool: redact + pseudonymise | Pseudonymisation, not prose rewrite | Not specified | Fully open source | Yes | N/A | **Tool, not a model**; utility-parity evidence |
| ollamonym | Pipeline: detect + reversible tokens | No (tokens) | Any Ollama model | Not verified | Yes | Yes | Pseudonymisation, not rewriting |

## The finding that changes the design: latent entities

NeMo's argument is the strongest thing in this research, and it reframes the
problem. Anonymisation is not an entity-masking problem; it is a contextual
reasoning problem. Their canonical example: replace "Seattle" with "a generic
city", and the text still mentions the Space Needle, ferries to Bainbridge, a
Mariners game, Puget Sound, and persistent rain. Any one is harmless. Together
they reconstruct Seattle.

This matters directly here, because it says **our existing three-layer
architecture verifies the wrong thing**. `pii-redactor`'s layer 3 re-runs the
*same* detectors over the output and fails if they fire again. That proves no
detectable value survived. It does not prove the text is not re-identifiable —
and for a support capture it is the inference path (repeated escalations, a
regional outage, churn timing) that identifies the account.

The prior-art doc in the support repo (`docs/pii.md`) reaches a version of this
with quasi-identifiers and cardinality tests. NeMo's contribution is making it
the *organising principle* rather than a caveat, and shipping a repair loop
against it.

## Detail per candidate

### NVIDIA NeMo Anonymizer

- Repo: <https://github.com/NVIDIA-NeMo/Anonymizer>, pinned `7605c13cd7945197daadb09692bd69d3b8570b6f` (main, read 2026-11-10).
- Docs: <https://nvidia-nemo.github.io/Anonymizer/latest/>; Rewrite concept at `/concepts/rewrite/`; intro devnote dated 2026-05-19.
- License: Apache-2.0 (repo LICENSE; README "License" section). Python 3.11+.
- Install: `pip install nemo-anonymizer`. Ships an Agent Skill at `skills/anonymizer/SKILL.md`.
- Two flows, both after a shared hybrid detection step:
  - **Replace** — four strategies over detected spans: `Substitute` (LLM-generated realistic alternative), `Redact`, `Annotate`, `Hash`. Substitute's stated requirement matches what we want: each replacement realistic on its own AND the set internally consistent (names match email local-parts, cities match cultural cues).
  - **Rewrite** — 10-step pipeline: detect → plan consistent replacements → find latent clues → decide what to protect → identify what must survive → build privacy + quality checks → generate → **attack the rewrite** → repair what failed → final judge.
- Rewrite configuration that matters: `privacy_goal` (`protect` / `preserve` free text), `risk_tolerance` (`minimal`/`low`/`moderate`/`high` — default `low`), `max_repair_iterations` (default 3), `strict_entity_protection` (default False — some low-risk quasi-identifiers are deliberately left as-is).
- Protection methods per entity: `replace`, `generalize`, `suppress_inference` (rewrite surrounding text to remove inferable cues), `remove`, `leave_as_is`. The middle three are the ones placeholders cannot express.
- Output columns are directly usable as gates: `utility_score`, `leakage_mass`, `weighted_leakage_rate`, `any_high_leaked`, `needs_human_review`. Leakage mass is a sensitivity-weighted sum (high 1.0 / medium 0.6 / low 0.3), so "one high-sensitivity entity leaked at full confidence" ≈ 1.0.
- Seven LLM roles: `domain_classifier`, `disposition_analyzer`, `meaning_extractor`, `qa_generator`, `rewriter`, `evaluator`, `repairer`. Defaults are `gpt-oss-120b` and `nemotron-30b-thinking`.

**Two disqualifying defaults for our use, both configurable:**

1. **Default LLM provider is OpenRouter** (`OPENROUTER_API_KEY`), with `build.nvidia.com` as the other documented endpoint. This conflicts head-on with the local-only constraint. It must be re-pointed at a local endpoint via a providers YAML (`Anonymizer(model_providers="path/to/model_providers.yaml")`) before it touches anything real.
2. **Telemetry is on by default** — one event per `run()`/`preview()`. The docs state it carries only technical metadata (strategy, models, hosts, record counts, duration, failure attribution; explicitly no record contents, prompts, or outputs). Opt out with `--no-emit-telemetry`, `emit_telemetry=False`, or `NEMO_TELEMETRY_ENABLED=false`. In a PII pipeline I would disable it unconditionally rather than trust the field list.

Also: default detection expects a **local GLiNER2 endpoint** (the tutorials can start one), so "local by default" is true for detection and false for the LLM stages. That asymmetry is easy to misread as fully local.

Cost note: Rewrite runs up to 7 LLM roles plus up to 3 repair rounds per record, with adversarial attack calls inside. This is not a per-document call — plan for tens of calls per record. At our scale (154-entry HAR = 154 records) that is thousands of calls, so this is a "run overnight on a sample" tool, not an interactive one.

### EternisAI Anonymizer (0.6B / 1.7B / 4B)

- HF: `eternisai/Anonymizer-0.6B` `e0d63404f50c`, `Anonymizer-1.7B` `c6545f49718c`, `Anonymizer-4B` `4a1c1f58ca14` (read 2026-11-10).
- **License: CC-BY-NC-4.0 on all three — non-commercial. This disqualifies them for work use** and it is the reason this row is rejected rather than ranked.
- Base: Qwen3. Trained SFT → GRPO with a GPT-4.1 judge, ~30k samples. Vendor-reported score 9.20/10 vs GPT-4.1's 9.77/10 — their measurement, not independently reproduced.
- Output shape: a **tool call** `<|tool_call|>{"name": "replace_entities", "arguments": {"replacements": [{"original": ..., "replacement": ...}]}}</|tool_call|>`. It proposes replacement *pairs*; the caller applies them. That is the same engine-owns-substitution contract as `raise_cli`'s `text_redact`, which is architecturally convenient — but it is entity substitution, not prose rewriting.
- Its instruction is the single most useful thing to borrow regardless of licence. It is a compact, well-reasoned substitution policy: pick same culture + gender + era for names and keep surnames aligned across a family; invent a same-industry, same-size-tier org and keep the legal suffix; keep major public companies (anonymity set ≥ 1,000,000) and globally recognised public figures; shift dates by small amounts but **keep the year** to preserve temporal context; keep big cities (≥ 1M) and iconic landmarks; scale monetary values by 0.8–1.25 to keep order of magnitude; swap only embedded tokens inside quotes. This is a directly reusable specification for a surrogate layer, independent of the model.
- Hardware: 0.6B runs CPU-only at ~400 MB–1 GB quantised, <200 ms TTFT. 1.7B is <1 s full completion quantised.
- A GGUF quantisation exists (`eternisai/Anonymizer-0.6B-gguf`) for llama.cpp/Ollama.
- Deployments: powers the Enchanted app. Downloads are low (46–50/month), so there is little third-party validation.
- Limits the authors state: 0.6B is worse on nuanced cases; rare identifiers and subtle contextual PII may be missed; quantisation slightly reduces accuracy.

### `openai/privacy-filter`

- HF `openai/privacy-filter`, `7ffa9a043d54`, Apache-2.0, ~103k downloads, pipeline `token-classification`.
- A 1.5B mixture-of-experts token classifier (per arXiv 2605.13538, which uses it as the detector stage). Named entity labels, no rewriting.
- Relevant as a **better span detector** for layer 2 than the current model pass, because it is deterministic and local. It does not answer this question.

### GLiNER multi-PII

- `urchade/gliner_multi_pii-v1` `1fcf13e85f4e`, Apache-2.0, ~100k downloads; xlm-roberta base, ~0.4B. Zero-shot label-driven detection.
- `knowledgator/gliner-multitask-large-v0.5` `7a95e168036d`, Apache-2.0.
- Detector only. This is the same family as the bardsai model already filed as APL-7 — the layer-2 detection seam.

### Where the papers land

- **Anonymizer-by-construction** (arXiv <https://arxiv.org/abs/2603.17217>, 2026-03-17): on-premise prompted substitution with gpt-oss 20B and DeepSeek-r1 7B; one instruction enforces span detection by type, type-preserving replacement, and faithful structure reproduction; issued utterance-by-utterance. Evidence that a *prompt* gets most of this, without a bespoke model. No weights released.
- **SFAA** (arXiv <https://arxiv.org/abs/2601.14683>): three steps (detection, classification into direct/strong-indirect/weak-indirect, adaptive anonymisation) with four strategies (rule-based substitution, context-aware rewriting, generalisation, suppression). Phi 3.2 4B: 91.3% recall / 96.6% precision on case study 1, 93.5% / 95.1% on case study 2, and 94.8% sentiment preservation. Useful taxonomy: suppression for identifiers that "could not be rewritten safely" is a legitimate outcome, not a failure.
- **On-device PII substitution** (arXiv <https://arxiv.org/abs/2605.13538>): the honest negative result to keep in view. With naive fixed few-shot demos, a 1-bit SLM regurgitates the demo outputs verbatim; fixable with locale-conditioned rotating demos (482/482 calls clean). But the downstream numbers are the point: on NER, redact F1 = 0.000, faker 0.656, original 0.960 — and on a matched subset **faker (0.506) beats the SLM hybrid (0.346) at p < 0.001**. SLM surrogates read more naturally but vary less, and downstream tasks benefit more from variety than naturalness. Conclusion: for patterned fields, a rule-based generator beats an SLM.
- **Redakto** (arXiv <https://arxiv.org/abs/2608.18260>, WIPE-OUT 2026 workshop): open-source tool, local, REST + MCP; reports utility scores on par with original text across redaction strategies on legal and medical data. Tool-level evidence that utility loss is not inevitable.

## What does not exist

- **No standalone, permissively licensed, general-purpose "context-preserving rewriter" model.** The closest artifact (EternisAI) is non-commercial and does entity pairs, not prose.
- **No model here proves re-identification resistance.** None of the candidates ship an attack suite except NeMo's Rewrite, and even that is a loop with thresholds, not a guarantee. TAB, NAP², SynthPAI, RAT-Bench are named as the benchmarks to evaluate against; NeMo lists them as future work.
- **No multilingual evidence.** NeMo: "Multilingual quality has not yet been evaluated systematically"; tested mostly on English. EternisAI's instruction is culture-aware but unmeasured.
- **No measured numbers for our actual task.** Every accuracy figure above is the authors' own benchmark, on their own corpus. None of it transfers to Sentry support captures.

## Recommendation for this pipeline

**Do not adopt NeMo Anonymizer wholesale now. Adopt its architecture and its vocabulary, and evaluate its Replace flow first.**

Reasoning, in order:

1. **It reframes the verification layer correctly.** Our layer 3 answers "did any detector fire again", which is necessary and insufficient. The right target is "can the account still be inferred from what survived". That is a different gate, and it is the finding that outlives whichever tool we use. It also matches the user's standing requirement that residual-risk warnings name a concrete re-identification example.
2. **Replace before Rewrite.** Replace's `Substitute` strategy (realistic, internally consistent values) gets most of the utility win over `[NAME]` placeholders for a fraction of the cost, and its output is verifiable by our existing detectors. Rewrite is 7 LLM roles plus repair rounds per record — thousands of calls on a 154-entry HAR. Prove the utility gain on a sample with Replace, measure it, then decide whether Rewrite's latent-entity handling earns its cost.
3. **It cannot be the shipped path yet**: default provider is OpenRouter and telemetry is on. Both must be re-pointed and disabled, and the local endpoint measured, before any real capture goes near it.
4. **Borrow the substitution policy text** from EternisAI's instruction regardless of its licence — the *policy* (same culture/gender/era, keep the year, scale money by 0.8–1.25, keep public figures) is the reusable asset. Do not copy the model weights; the licence forbids the deployment, and the policy is expressed as instructions we can write ourselves.
5. **Use `faker`-style rules for patterned fields and reserve SLMs for names/addresses/dates.** The negative result above is direct evidence: rules beat SLMs on variety for structured fields.
6. **Keep the mapping local.** NeMo's Replace/Substitute decides replacements in-process; nothing in the recommended path requires sending a real→fake map anywhere. That preserves the hard constraint.

### Rejected options, with reasons

| Rejected | Why |
|---|---|
| EternisAI Anonymizer as the engine | CC-BY-NC-4.0 — non-commercial, unusable for work |
| `openai/privacy-filter` or GLiNER as "the anonymiser" | Detectors return spans; something must still choose the replacement. Correct as layer-2 detection (APL-7), wrong as the answer |
| Presidio as a candidate | A framework wrapping detectors; no context reasoning, no rewriting |
| Prompted local LLM only (arXiv 2603.17217 pattern) | No released weights, no verification harness; the *pattern* is adopted, not the artifact |
| Rewrite flow on day one | Tens of LLM calls per record, unmeasured utility gain, two disqualifying defaults to fix first |
| SLM surrogates for every field | Measured worse than faker for downstream NER (0.346 vs 0.506) |

### Follow-ups this creates

- A gate that tests re-identification resistance rather than detector recurrence — the actual gap. Needs a definition of "inferable" we can defend.
- An evaluation of NeMo Replace against our existing `pii-redactor` output on the same capture, measuring downstream utility (does a model answer the same questions correctly from both?). That is a model-fitness question and belongs in a measured run, not this note.
- The local provider YAML plus telemetry-off configuration, if Replace proves its value.

## Sources register

| Source | URL | Revision / date | Licence | Review trigger |
|---|---|---|---|---|
| NeMo Anonymizer repo | <https://github.com/NVIDIA-NeMo/Anonymizer> | `7605c13cd7945197daadb09692bd69d3b8570b6f` (2026-11-10) | Apache-2.0 | New release; Rewrite leaves "future work" for TAB/RAT-Bench |
| NeMo Rewrite concept | <https://nvidia-nemo.github.io/Anonymizer/latest/concepts/rewrite/> | latest, 2026-11-10 | Apache-2.0 (docs) | Threshold defaults change |
| NeMo intro devnote | <https://nvidia-nemo.github.io/Anonymizer/latest/devnotes/introducing-nemo-anonymizer-text-anonymization-for-the-reasoning-era/> | 2026-05-19 | Apache-2.0 (docs) | Multilingual coverage announced |
| EternisAI Anonymizer-1.7B | <https://huggingface.co/eternisai/Anonymizer-1.7B> | `c6545f49718c` (2026-11-10) | **CC-BY-NC-4.0** | A commercial licence appears |
| EternisAI Anonymizer-0.6B | <https://huggingface.co/eternisai/Anonymizer-0.6B> | `e0d63404f50c` | CC-BY-NC-4.0 | As above |
| EternisAI Anonymizer-4B | <https://huggingface.co/eternisai/Anonymizer-4B> | `4a1c1f58ca14` | CC-BY-NC-4.0 | As above |
| openai/privacy-filter | <https://huggingface.co/openai/privacy-filter> | `7ffa9a043d54` | Apache-2.0 | New checkpoint |
| GLiNER multi-PII | <https://huggingface.co/urchade/gliner_multi_pii-v1> | `1fcf13e85f4e` | Apache-2.0 | Superseded by GLiNER2 |
| Anonymizer-by-construction | <https://arxiv.org/abs/2603.17217> | 2026-03-17 | paper (CC) | Weights released |
| SFAA | <https://arxiv.org/abs/2601.14683> | 2026 | paper | Weights released |
| On-device PII substitution | <https://arxiv.org/abs/2605.13538> | 2026-05-13 | paper (CC-BY-4.0) | A positive NER result supersedes the negative one |
| Redakto | <https://arxiv.org/abs/2608.18260> | 2026-08-18 | paper (CC-BY-SA-4.0) | MCP surface stabilises |

## Limitations of this research

- Every performance number is vendor- or author-reported on their own corpus. None reproduced here.
- No candidate was installed or run. Claims about behaviour come from documentation and source README, not execution — the NeMo default-provider and telemetry facts were read, not observed.
- EternisAI's 4B model card was not read in full; its metadata (licence, revision, size) was.
- `ollamonym`'s licence was not verified; it is listed for completeness and not recommended.
- Cost estimates for Rewrite are arithmetic from the documented role count, not measured.

## Addendum 2026-11-10: the EU-compliance axis

Prompted by a question about "anonymizer models for EU standards". Two things
worth separating: **what a model can do** and **what makes a deployment
compliant**. No model in this note is a compliance program, and the one card that
says so explicitly is bardsai's: "This is a detection model, not a compliance
program. Use it to support a redaction workflow with review where the stakes
require it."

### bardsai EU PII detector — verified, and it is the APL-7 model

- `bardsai/eu-pii-anonimization-multilang-v3`, `091984b5fbce`, **Apache-2.0**,
  24 EU languages, 37 BIO labels, ModernBERT-base (`jhu-clsp/mmBERT-base`),
  307M params, **8192-token context**. v1 `62ca57123687`, v2 `07a9a69b0d75`.
- **Art. 9 classes are real labels, not a claim**: `HEALTH_DATA`,
  `BIOMETRIC_DATA`, `ETHNIC_ORIGIN`, `POLITICAL_OPINION`, `RELIGION_OR_BELIEF`,
  `SEXUAL_ORIENTATION`, `TRADE_UNION_MEMBERSHIP`, `CRIMINAL_OFFENCE_DATA`.
- v3 adds `DATE_TIME` and `URL`; `det.anonymize(text, labels={...})` filters which
  types get masked, so generic dates and URLs can be left alone.
- Reported PIIMB average F2 **0.927** (v2 0.773); real-text strict F1 0.980.
  Author-reported, on their test sets.
- **ONNX INT8 is 0.3 GB and scores the same as FP32** (0.980), runs on CPU. The
  browser demo runs it client-side, so PII never leaves the device.
- Ships a **word-level decoder** (`pii_detector.py`) — the card warns a plain
  per-token argmax emits sub-word fragments. Use their decoder, not the raw
  pipeline, or spans come out cut.
- 512-token windows with 128 overlap internally, so it chunks itself; 8192 is
  the ceiling, not the working window.

**This supersedes the pin in APL-7**, which was written against a *preview*
checkpoint. v3 is the stable release to pin. Same conclusion as before: detector
only — it returns spans, and the engine still owns substitution. It breaks
stdlib-only (needs `transformers` + `onnxruntime`), which is the APL-7 tradeoff
and should be decided there, not assumed here.

### Disabling NeMo telemetry — verified, three ways

The README documents all three; use them all if this ever ships:

- Per invocation: `--no-emit-telemetry`
- In the SDK: `AnonymizerConfig(..., emit_telemetry=False)`
- Per shell: `NEMO_TELEMETRY_ENABLED=false`

The README lists exactly what is collected (strategy, models, model hosts, record
counts, duration, failure attribution by pipeline step) and states no record
contents, prompts or outputs. Disable it anyway rather than trust the field list —
the cost is one flag.

### Pointing NeMo fully local — the trick, and the trap

Ollama on this machine already serves an OpenAI-compatible API at
`http://localhost:11434/v1` (verified: `/v1/models` returns the 40 installed
models). So NeMo can be made fully local.

**Trap:** the bundled model configs hardcode `provider: openrouter`, and
`Anonymizer` validates that every config's provider name resolves. Dropping
`openrouter` from your provider list fails validation. Two ways through:

1. Keep the name, repoint the URL — `name: openrouter`,
   `endpoint: http://localhost:11434/v1`. Cheapest, no model-config override.
2. Pass `model_configs=` that name your own provider. Explicit, and the only
   route if you also want to change which role gets which model.

Validation is `anonymizer validate` / `anonymizer.validate_config(config)` —
run it after any provider change.

Also note the bundled detector is `fastino/gliner2-privacy-filter-PII-multi` at a
**loopback** endpoint, so detection is local by default while the LLM roles are
not. That asymmetry is the thing to check when claiming "local".

### Can a general Qwen serve as NeMo's rewriter?

Separate question from whether it is PII-tuned. NeMo drives plain chat LLMs
through OpenAI-compatible endpoints, so yes mechanically — any installed Qwen
reaches it via the `/v1` endpoint. But role fit is a measurement, not an
assumption, and NeMo's own guidance is to split by role:

- Strongest model for `latent_detector`, `disposition_analyzer`, `rewriter`,
  `repairer`
- Mid-tier for `entity_augmenter`, `meaning_extractor`, `replacement_generator`
- Small/fast for `entity_validator`, `domain_classifier`, `qa_generator`,
  `evaluator`

So a local Qwen belongs in the rewriter role only after it is measured there.
What does **not** work: Qwen-based *PII-tuned* models. EternisAI's Anonymizer
series is Qwen3-based and is the one Qwen-tuned family found — but it is
CC-BY-NC-4.0, so it is out on licence, not on capability.

### Corrections to circulating summaries

Two claims that appeared in an AI-generated summary and do not hold up:

- **VaultGemma is not an anonymizer.** It is a Google research LLM trained with
  differential privacy — that is privacy of *training data*, not masking PII in a
  prompt. Grouping it with "open-source LLM anonymizers" misreads what it does.
- **"MAPA" could not be verified at the repo location given.** `pangeanic/MAPA`
  returns 404 via the GitHub API. MAPA does appear in this ecosystem as the
  `mapa-eur-lex` dataset, which bardsai uses for training and evaluation (21
  languages, and their weakest benchmark at 0.633 F2). Treat MAPA as a
  dataset/benchmark until the tool itself is located and read.

Unverified in that summary and not repeated here: the "three years" human-review
retention window for consumer Gemini, and vendor compliance claims for VEIL.AI,
Gallio PRO and vAnonymize. None were checked; none should be relied on.

Also: differential privacy (`diffprivlib`, Google DP) protects aggregate releases
and model training, not free text. It is not an alternative to redaction.

## Addendum 2026-11-10 (2): "EU as a heuristic" names pseudonymisation, not anonymisation

The requirement was clarified as: pseudonymisation of high enough quality to
maintain privacy while preserving model instructions and context, using the EU
regime as the yardstick. That is a sharper target than the first addendum
assumed, and the EU has a specific standard for it. **It is not the
anonymisation standard.**

### The two EDPB instruments are different tools

| | Guidelines 01/2025 — Pseudonymisation | Guidelines 02/2026 — Anonymisation |
| --- | --- | --- |
| Adopted | 16 Jan 2025 | 7 Jul 2026 (public consultation to 30 Oct 2026) |
| Target | Art. 4(5): data that can no longer be attributed to a person *without additional information* | Art. 4(1): data that does not relate to an identifiable person *at all* |
| Legal status of output | **Still personal data.** GDPR applies in full | Outside GDPR |
| Test | Attribution prevented without the additional information | No Record Isolation, No Linkage, No Inference |
| Achievable for a support capture | **Yes, with discipline** | In practice no |

EDPB 01/2025 is explicit that the two are not the same: "Prevention of
attribution does not imply anonymity of the data."

And the older Opinion 05/2014 (Table 6) scores pseudonymisation against all
three anonymisation criteria — singling out **yes**, linkability **yes**,
inference **yes**. So a pseudonymised capture remains personal data by
definition. That is the *point* of it: you get a document a model can reason
over without shipping real identities, and you keep the legal obligations rather
than pretending they vanished.

**Why this is the right target here:** for a support capture, the anonymisation
standard is unreachable. EDPB 02/2026's No Inference criterion requires that no
specific and meaningful inference can be drawn, including from external
information and the context the data was produced in. A ticket-shaped document
survives that test almost never — the escalation history is the identifying
signal. Chasing it produces either refusal or a false claim of compliance.

### What this changes in the design

1. **The gate must test attribution, not detector recurrence — and must not
   claim anonymity.** This is the same conclusion as APL-13 but with a correct
   legal frame: name the output as pseudonymised, keep it in scope, and say so.
   A tool that prints "anonymised" for a document it pseudonymised is making a
   false compliance claim, which is worse than making none.
2. **The "collapse placeholders" default is wrong for this goal.** Collapsing
   `[NAME]` for every person destroys the ability to tell two people apart —
   and the people in a support capture are exactly the referents whose distinct
   relationships are the meaning being preserved. Consistency is the whole
   mechanism by which pseudonymisation keeps utility. The right default is a
   *stable* pseudonym per value, within the run at minimum (raise's
   `pii-map.toml` is the mature form: salted per-ticket, `{slug}-{salt}-{NNN}`).
   This directly contradicts the Q8 scope fence taken earlier in this session,
   which chose placeholders-only, no surrogate engine, no map. **That fence was
   drawn before this requirement was clear and should be revisited rather than
   defended.**
3. **`raise pii`'s existing design is the reference implementation**, not a
   separate concern. docs/pii.md already argues surrogates must be consistent
   and typed, and `pii-map.toml` already implements per-ticket salt and
   one-way-lifed mappings. The earlier framing ("surrogates are a separate
   decision") split off exactly what this requirement needs.
4. **EDPB 01/2025 makes the additional information the security boundary.** The
   mapping is the "additional information" — so it must be protected at least as
   strongly as the original data, and its destruction is what upgrades the
   artifact's status later. That matches raise's `pii erase` (task-52) design and
   means the ledger in APL-3 must never touch disk, which it already does not.

### Revised recommendation

Adopt the pseudonymisation frame explicitly and treat the placeholder path as
the degenerate case of it (placeholder = a pseudonym with no information
content). Concretely, the layer-2 backend should be able to emit **stable typed
pseudonyms** rather than fixed tags, and the spec should say which of the two
modes a run used. The EU yardstick to cite is EDPB 01/2025; the anonymisation
guidelines are the ceiling we are deliberately not claiming.

This does not change the simple-grandiose advice from the first addendum: NeMo
Replace/Substitute is the off-the-shelf way to get consistent, realistic
pseudonyms, and it is the thing worth measuring (APL-14). It changes *what we
call the output* and *what the gate must prove*.

### Sources added

| Source | URL | Revision / date |
| --- | --- | --- |
| EDPB Guidelines 01/2025 — Pseudonymisation | <https://www.edpb.europa.eu/system/files/2025-01/edpb_guidelines_202501_pseudonymisation_en.pdf> | adopted 16 Jan 2025 |
| EDPB Guidelines 02/2026 — Anonymisation | <https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202602_anonymisation_v1_en_0.pdf> | v1.0 adopted 7 Jul 2026 |
| A29WP Opinion 05/2014 — Anonymisation Techniques | <https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf> | 10 Apr 2014 |
| ICO — motivated intruder test | <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/how-do-we-ensure-anonymisation-is-effective/> | read 2026-11-10 |

Caveats: 02/2026 is in public consultation until 30 Oct 2026 and may change;
01/2025 was read via search extract, not the PDF end to end. Nothing here is
legal advice, and the compliance decision belongs to whoever owns the data.

## Addendum 2026-11-10 (3): the incumbent already implements the requirement

Applying review-best-practices to this problem rather than continuing to
research models exposed how much was already built and not consulted.

**Requirement, stated before searching:** produce a pseudonymised support
capture whose substitutions preserve enough context for a model to reason over
it, against the EDPB 01/2025 pseudonymisation standard. Disqualifying
capabilities: (a) destroys referent identity — fixed `[NAME]` tags collapse two
people into one; (b) requires sending real values to a non-local model.

| Capability required | `raise_cli` (in-tree, `surrogates.py` + `pii_map.py`) | `pii-redactor` (chezmoi) | NeMo Anonymizer Replace | EternisAI |
| --- | --- | --- | --- | --- |
| Consistent per value | **Yes** — `_seen` dict keys on `(category, value)` | No — fixed `[NAME]` | Yes (coordinated map) | Yes |
| Typed / shape-preserving | **Yes** — 17 generators, IPs in RFC 5737 ranges, hosts RFC 2606, cards Luhn-valid | Placeholders only | Yes | Yes |
| Scoped per ticket | **Yes** — salt = `sha256(ticket_id)[:8]` | n/a (single file) | n/a | n/a |
| Re-run reproducible | **Yes** — deterministic counters | No | No (seeded LLM) | Partly |
| Local-only | **Yes** — pure stdlib transform | Yes | Only after repointing | Yes |
| Mature | 196 + 83 lines, tested | 874 lines, tested | Apache-2.0, new | CC-BY-NC-4.0 |
| Extra dependency | **None** (stdlib + hashlib) | None | torch/transformers chain | torch |

`surrogates.py`'s own module docstring names the contract it implements:
*consistent*, *type-preserving*, *per-ticket salted*, *reserved ranges only*.
It cites `docs/pii.md § Surrogates must be consistent and typed`. Its stated
exclusions are deliberate: persistence is a separate module (`pii_map.py`), and
the engine is "a pure value transform with no filesystem access."

**This is the answer that was being searched for.** The requirement asked for a
pseudonymisation engine of high quality; one exists in this workspace, is
stdlib-only, is already EU-shaped (consistent + typed + scoped), and costs
nothing to adopt. NeMo remains interesting for *contextual detection* (finding
names an NER model would miss) and for its latent-entity reasoning, but it is
not the pseudonymisation mechanism. EternisAI is out on licence regardless.

### The correction this forces, stated where it was claimed

Earlier in this session I recorded a scope fence ("Q8"): placeholders only, no
surrogate engine, no `pii-map`, no pseudonymisation, on the reasoning that
raise's surrogates were a separate decision. **That framing was wrong** and the
requirement clarification is what exposed it. A pseudonymisation requirement
cannot be met by a mechanism that deliberately discards referent identity, and
splitting the surrogate engine off as "separate" removed exactly the capability
being asked for.

What survives from that fence: the *binding* stays off. `pii-redactor` should
not grow its own map file, salt scheme, or surrogate generators — it should
consume the engine, which is now a library-shaped module. Whether that means a
shared package, a vendored copy, or importing from `raise_cli` is the open
question, and it is a packaging question, not a design one.

### Second correction: the "collapse placeholders" default

The default approved earlier this session — collapse `[NAME]` rather than
`[NAME-1]` — is correct for *redaction* (nothing linkable survives) and wrong for
*pseudonymisation* (linkability is the product). Both defaults are now on record
and they are not interchangeable. Which applies should be an explicit mode of the
run, never an implicit default, because the two produce artifacts with different
legal status.

### Revised ranking against the requirement

1. **`raise_cli.surrogates.Engine`** — meets the requirement, already written, no
   new dependency. Adopt. The only work is packaging (how `pii-redactor` reaches
   it) and wiring it into the layer-2 substitution step.
2. **NeMo Anonymizer Replace** — a second option for *detection* and for realistic
   name generation (`Substitute` produces plausible human names where the
   in-tree engine produces `Person-1`). Worth measuring (APL-14) specifically on
   whether realistic names improve downstream answer quality over typed tokens.
   Not a replacement for the engine.
3. **Plain placeholders** — retained as the redaction mode, not the
   pseudonymisation mode.
4. **EternisAI** — rejected on licence.

The honest summary: the search was worth running because it produced the
disqualifying facts (EternisAI non-commercial, NeMo OpenRouter default + telemetry,
no standalone permissive rewriter). But the build-versus-adopt answer was
**adopt what is here**, and the earlier framing was sending work toward building
something the workspace already had.

## Addendum 2026-11-10 (4): how NeMo works, and how well — evidence tiers

### How it works

Every input goes through **hybrid entity detection** first, then one of two flows.

**Detection** (shared by both): `fastino/gliner2-privacy-filter-PII-multi` at a
loopback endpoint does the first pass, then LLM roles *validate* candidates and
*augment* the set with what the NER model missed. Validation is chunked
(`validation_max_entities_per_call`) with excerpts around each candidate — this
is why detection is the expensive stage.

**Replace** — operates on detected spans, four strategies applied uniformly to
every entity in the run: `Substitute` (LLM generates a realistic replacement),
`Redact` (tag/mask), `Annotate` (`<value|label>`), `Hash`. One
replacement-map generation per record after the final entity set is known.

**Rewrite** — ten stages, not one prompt:

1. detect (as above, plus **latent entity** detection for inferable facts)
2. plan consistent replacements
3. find latent clues
4. decide what to protect (goal-aware; depends on `privacy_goal`)
5. identify what must survive (**meaning units**: events, relationships,
   chronology, conclusions)
6. build privacy + quality checks (two QA harnesses from steps 4 and 5)
7. generate the first rewrite
8. **attack** the rewrite (adversarial questions)
9. repair what failed — the failure ships with an explanation naming which clues
   still leak, so repair is targeted, not "try again"
10. final judge (holistic; fluency, coherence, obvious leaks)

Per-entity protection methods in Rewrite: `replace`, `generalize` (exact date →
quarter), `suppress_inference` (rewrite surrounding text to kill inference
cues), `remove`, `leave_as_is`.

### How well it works — three tiers of evidence, only two of which exist

**Tier 1 — measured operational throughput. Trustworthy.** Vendor-measured but
it is timing and token counts, which are hard to fake:

| Run | Records | Wall | Throughput | Failed | Cost |
| --- | --- | --- | --- | --- | --- |
| Compact 100 | 100/100 | 2.54 min | 39.33 rec/min | 0 | $0.40 |
| Compact 250 | 250/250 | 8.86 min | 28.23 rec/min | 0 | $1.40 |

One B300, Qwen3.6-35B-A3B (NVFP4) on vLLM + GLiNER, everything on localhost.
Stage split: detection 413.7 s vs substitute-map 117.5 s on the 250 slice —
**detection dominates**. Tokens: 8,820,515 total for 250 records
(7.46 M in / 1.36 M out) ≈ **35 k tokens per record**. Mean 46.3 entities/record.

That token figure is the number to budget with. For a 154-entry HAR this is
roughly 5.4 M tokens — feasible locally, but not free, and it is *Replace*, not
Rewrite. Rewrite multiplies this by its seven-role pipeline plus repair rounds.

**Tier 2 — vendor self-evaluation. Real mechanism, unverified numbers.**
`utility_score` and `leakage_mass` are computed *during* `run()`, and rows over
threshold enter the repair loop while `evaluate()` adds independent LLM judges
afterward. The mechanism is genuinely better than most tools ship. But:

- `leakage_mass = Σ(sensitivity_weight × leak_confidence)` where the confidence
  comes from an LLM judge. It is a model's opinion, not a measurement.
- `utility_score` is a weighted mean over questions *generated from the original
  record*. A meaning no generated question captured scores as preserved.
- The authors say so themselves, in a section titled "What the Scores Do Not
  Prove": utility "can miss meaning that no question captured", leakage metrics
  "do not model every possible attacker or external dataset", entity coverage "is
  not ground truth". They do not certify anonymity.
- Judge scores are configurable — `gpt-oss-120b` vs `nemotron-super` on the same
  result — so a score is partly a property of the judge you chose.

**Tier 3 — independent evaluation. Does not exist.** RAT-Bench
(arXiv 2602.12806, Feb 2026, de Montjoye group) is the right benchmark: it
measures *re-identification risk* rather than recall, grounded in US Census
PUMS demographics, with an LLM attacker, across 12 tools. **NeMo Anonymizer is
not among them** — it postdates the benchmark. So there is no third-party
measurement of NeMo's privacy effectiveness. Every quality claim about it
originates with NVIDIA.

### What RAT-Bench says about the category (this is the sobering part)

Re-identification success rate, lower is better (θ = 0.2, k=5):

| Tool | Easy | Hard | Explicit avg | Implicit |
| --- | --- | --- | --- | --- |
| **No anonymization** | 100% | 98% | 99% | **32%** |
| Azure (NER) | 22% | 33% | 28% | 21% |
| Presidio (NER) | 41% | 77% | 59% | 30% |
| GLiNER (NER) | 67% | 71% | 69% | 28% |
| Textwash | 39% | 55% | 47% | 32% |
| **Anthropic PII purifier + GPT-4.1** | 26% | 58% | **42%** | 19% |
| Gemini 2.5 Flash | 48% | 64% | 56% | 33% |
| Llama 3.1-8B | 37% | 72% | 55% | 21% |
| ITERATIVE anonymizer (Staab 2025) | best overall | — | — | — |
| *Average across tools* | 44% | 69% | 57% | 28% |

Four findings that bear on this project directly:

1. **Even the best tool leaves ~42% average re-identification risk** on explicit
   identifiers, and Azure's better number (28%) comes with heavy over-redaction
   (low BLEU) — it buys privacy by destroying utility.
2. **Implicit identifiers barely move.** No anonymization: 32%. Most tools: 21–33%.
   A tool that reduces risk to 21% on implicit identifiers has achieved
   approximately nothing on the hard half of the problem. This is exactly the
   latent-entity gap, measured.
3. **Representation format matters more than tool choice.** Risk climbs from 44%
   (easy) to 69% (hard) — non-standard formatting defeats detection far more than
   a better model helps. For our captures this is the "names written oddly" case.
4. **The iterative anonymizer wins, but conditionally.** It reduces risk
   drastically *when the exact attribute set is known*, and degrades with a noisy
   or generic attribute list. NeMo's Rewrite is this architecture.

### Conclusion for our decision

NeMo's **architecture** is the best-justified in the literature; its **measured
quality is unknown** to anyone but NVIDIA. That combination argues for exactly
what was already recommended: adopt the in-tree surrogate engine for the
mechanism (APL-15), keep NeMo as the evaluated second opinion (APL-14), and use
RAT-Bench itself as the evaluation harness rather than NeMo's own judge — it is
open (HuggingFace `imperial-cpg/rat-bench`, GitHub `imperial-aisp/rat-bench`,
leaderboard space) and it measures risk rather than recall.

And the category numbers make the EDPB framing unavoidable: if the best
independent evidence says ~42% of records are still re-identifiable after the
best explicit-identifier tool, then no run of any of these tools supports an
"anonymised" label. Pseudonymised, with the gate we have, and honest labelling
(APL-16) is the defensible claim.

### Sources added

| Source | URL | Revision / date |
| --- | --- | --- |
| NeMo — evaluating Replace | devnotes/after-anonymization--part-i-evaluating-replace-mode/ | 2026-07-28 |
| NeMo — evaluating Rewrite | devnotes/after-anonymization--part-ii-evaluating-rewrite-mode/ | 2026-08-07 |
| NeMo — self-hosted on one B300 | devnotes/running-nemo-anonymizer-fully-self-hosted-on-one-b300/ | 2026-07-07 |
| RAT-Bench | <https://arxiv.org/abs/2602.12806> | v1, 2026-02-13 |

Caveat: the B300 figures are vendor-measured on rented hardware that does not
resemble this machine (a 36 GB M4 Max). Throughput here will be far worse; the
token-per-record ratio is the transferable figure.
