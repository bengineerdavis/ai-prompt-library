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
