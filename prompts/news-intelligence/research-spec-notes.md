# Research Specification Notes

This is a living design record for research-capable skills. Runtime rules belong in `SKILL.md`; stable shared policy belongs in `references/`; observable outcomes belong in `spec.md`. Add a runtime rule only when a user need, dependency, failure, or measured result shows it is needed now. Prefer the simpler rule that addresses the same evidence.

## Outcome shape

Avoid standalone claims that a result provides “value,” is “helpful,” or is “good.” Name the property instead. For news intelligence, a successful result is:

- **Responsive:** answers the user's actual question.
- **Sufficient:** completes enough due diligence for the cost of error.
- **Traceable:** shows the basis of important conclusions.
- **Calibrated:** separates established facts, incomplete evidence, contradiction, no evidence, and assessment.
- **Proportionate:** does not recommend more action than evidence and exposure justify.
- **Accountable:** can explain evidence choices, alternatives, stopping point, limits, and reopening trigger.
- **Readable:** uses the smallest clear form without removing decision-relevant facts.

## Adopted lessons

### R-001 — Introduced counterpoints

- **Observation:** An inferred counterpoint formatted as a quote looked like a user claim.
- **Decision:** Introduce it as a counterpoint or implication; quote only exact user or verified source text.
- **Test:** `preserve-provenance-and-traceability.yaml`.

### R-002 — Fetch failure changes state

- **Observation:** A failed full-source fetch was silently replaced by search snippets.
- **Decision:** Snippets are leads. Attach the gap to the affected claim and obtain approval before a materially weaker fallback.
- **Test:** `check-runtime-and-handle-failure.yaml`.

### R-003 — Capability checks need runtime placement

- **Observation:** Front matter can declare needs but cannot make a host run checks.
- **Decision:** Put the preflight as the first relevant runtime step; use semantic rather than vendor-specific capability names.
- **Test:** `check-runtime-and-handle-failure.yaml`.

### R-004 — Separate task stages

- **Observation:** Digest, interpretation, verification, practical assessment, and validation have different outcomes and evidence needs.
- **Decision:** Keep one user-facing skill, but route internally to the smallest needed stage.
- **Test:** `match-the-task.yaml` and `validate-the-outcome.yaml`.

### R-005 — Credibility differs from evidence fit

- **Observation:** A credible source may prove an announcement but not effect, scope, causation, or personal relevance.
- **Decision:** Judge source credibility and whether its evidence is sufficient for this claim and decision separately.
- **Test:** `perform-due-diligence.yaml`.

### R-006 — No evidence is not weak evidence

- **Observation:** Missing access and contrary findings were both being called uncertain.
- **Decision:** Keep established, partial, contradicted, and no-evidence states distinct.
- **Test:** `perform-due-diligence.yaml`.

### R-007 — Sensitivity reveals dependency

- **Observation:** Source counts can hide that one item carries the conclusion.
- **Decision:** Remove the strongest external source; if the result changes, label the conclusion single-source-dependent and limit action.
- **Test:** `perform-due-diligence.yaml`.

### R-008 — Blind spots travel with findings

- **Observation:** A general limitations section can be separated from the claim it qualifies.
- **Decision:** Attach a material limitation to the affected finding; a general summary may repeat it.
- **Test:** `check-runtime-and-handle-failure.yaml`.

### R-009 — Media bias is a scrutiny signal

- **Observation:** Political orientation and motivations affect selection and framing but do not decide truth.
- **Decision:** Check orientation, ownership, sponsorship, audience, access, corrections, framing, and corroboration at claim level.
- **Test:** `examine-media-and-framing.yaml`.

### R-010 — Traceability scales

- **Observation:** Full registries burden short answers, while no cross-references obscure decision-bearing work.
- **Decision:** Use ordinary citations by default; use `S#`, `C#`, and `A#` for multi-claim or durable work and always include a legend.
- **Test:** `preserve-provenance-and-traceability.yaml`.

### R-011 — Due diligence needs a stopping account

- **Observation:** “Do no more research than needed” can stop too early.
- **Decision:** Stop only when the evidence threshold is met and another check is unlikely to change the answer enough to justify its cost or delay. Be able to explain why.
- **Test:** `validate-the-outcome.yaml`.

### R-012 — Validation must challenge itself

- **Observation:** A review can repeat the original reasoning and call it validation.
- **Decision:** Test counterevidence, framing, practical conclusions, evidence provenance, source laundering, and sensitivity to removing a source. Repair or disclose material failures.
- **Test:** `validate-the-outcome.yaml`.

## Deferred (YAGNI)

### Mandatory multi-agent validation on every request

- **Why deferred:** A single-agent final check satisfies current evidence; mandatory orchestration would burden simple summaries.
- **Reopen when:** Repeated evals show the same agent cannot detect its own material errors, or high-stakes deployment requires independent review.
- **Source:** Han adversarial-validator pattern and project discussion.

### Full source registry on every answer

- **Why deferred:** Lightweight citations and optional IDs satisfy current traceability needs with less output.
- **Reopen when:** Results are routinely saved, shared, audited, or consumed by machines that require stable claim-source mappings.
- **Source:** Han research report resolvability pattern and project discussion.

### Numeric media-bias scoring

- **Why deferred:** Practice and incentive checks address the current need; a score risks false precision and outsourced judgment.
- **Reopen when:** A validated scoring method improves claim-level accuracy in evals beyond the compact source screen.
- **Source:** Project discussion of NewsGuard, Ad Fontes, and AllSides.

### Vendor-specific dependency front matter

- **Why deferred:** Tool names are host-specific, while the runtime preflight already tests the needed capability.
- **Reopen when:** A target orchestrator supports and enforces a stable dependency schema.
- **Source:** Project runtime-capability discussion.

## External design sources

- Han evidence rule: https://github.com/testdouble/han/blob/main/han-research/references/evidence-rule.md
- Han YAGNI rule: https://github.com/testdouble/han/blob/main/han-research/references/yagni-rule.md
- Han adversarial validator: https://github.com/testdouble/han/blob/main/han-core/agents/adversarial-validator.md
- Han collaborative stop rule: https://github.com/testdouble/han/blob/main/han-core/references/collaborative-stop-rule.md
