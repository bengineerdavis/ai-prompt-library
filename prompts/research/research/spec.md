# Research

## Intent

This skill turns an open-ended question into a researched answer whose claims can be checked. It owns how to search, validate, and synthesize; it does not own how clarifying questions are asked, which it delegates to the questioning skill.

It exists because the failure mode of AI research is not ignorance but confident under-sourcing: a well-organized answer that reasons persuasively from thin or non-authoritative sources reads exactly like a well-sourced one. Every rule here targets that gap — separating what was confirmed from what was inferred, insisting the primary source is consulted before commentary about it, and making the reader's verification path explicit rather than implied.

## Triggers

- **SHOULD** apply when the user asks to research, search, compare options, investigate prior art, or gather evidence before a decision.
- **SHOULD** apply when a claim's currency matters — prices, versions, licences, vendor behaviour — because these change faster than model knowledge.
- **SHOULD NOT** apply when the answer is already fully determined by context in the conversation; summarizing what is already known is not research.
- **SHOULD NOT** apply to bug diagnosis, incident triage, or root-cause analysis, which investigate a system rather than a body of knowledge.
- **SHOULD NOT** apply when the user asks for code, editing, or writing with no factual question underneath.

## Behaviors

### Behavior: Delegate clarification to the questioning skill

The agent SHALL check for an active questioning skill or interaction policy before asking anything, and use it for all clarification. When none is available, the agent SHALL ask one question at a time and stop as soon as the goal is actionable. The agent SHALL resolve scope, audience, and success criteria before searching, because research aimed at the wrong question wastes the whole effort.

#### Scenario: Questioning skill is available

- **WHEN** the user asks "research encrypted backup tools for me" and a questioning skill is loaded
- **THEN** the agent uses that skill's one-question-at-a-time protocol to establish threat model and constraints, rather than asking a batch of questions in its own style or assuming defaults

#### Scenario: Non-interactive research agent

- **WHEN** the brief will run unattended, so no clarification is possible
- **THEN** the agent states each assumption it relied on and lists the questions it would have asked, in a dedicated section, rather than silently choosing

### Behavior: Classify scope before researching

The agent SHALL classify the request as narrow, comparative, or broad, and SHALL match research depth and answer length to that classification. The agent SHALL NOT run a broad process on a narrow question unless depth is explicitly requested.

#### Scenario: Narrow factual question

- **WHEN** the user asks "what is the current stable version of restic?"
- **THEN** the agent answers directly with the version and its source, without producing a comparison table or a multi-section report

### Behavior: Label every non-trivial claim twice

The agent SHALL attach both a confidence label — `verified`, `single-source`, or `reasoned` — and a source-authority label — `primary`, `secondary`, or `tertiary` — to each non-trivial claim. Primary means the thing itself: the tool's own documentation, source code, licence text, or API response. These are independent axes: several blogs agreeing is `verified`/`tertiary`, not `verified`/`primary`.

#### Scenario: Multiple blogs agree, vendor docs unread

- **WHEN** three third-party articles state that a tool sends anonymous telemetry, and the agent has not read that tool's own documentation or source
- **THEN** the claim is labelled `verified`/`tertiary`, and the answer names reading the tool's own docs as the step that would raise it to `primary`

### Behavior: Consult the primary source before commentary about it

For any claim about a tool, product, price, licence, or API, the agent SHALL consult that thing's own documentation, source, or API before citing third-party commentary, and SHALL prefer the primary source in the citation. When only third-party sources were consulted, the agent SHALL say so explicitly.

#### Scenario: Pricing question

- **WHEN** asked what a hosted model costs and a provider publishes a models API
- **THEN** the agent reads that API and cites it, rather than citing price-aggregator sites — which have been observed to disagree with the provider's own API by large margins

### Behavior: Give a verification recipe for anything below verified

For each claim not labelled `verified`/`primary`, the agent SHALL state the specific command, file, URL, or observation the reader can use to confirm it. A general instruction to "verify this" does not satisfy the rule; the recipe must be executable as written.

#### Scenario: Uncertain telemetry behaviour

- **WHEN** the agent believes a tool phones home but has not confirmed it
- **THEN** the answer names the exact check — for example the attribute to read in the installed package, or a packet-capture command with the expected and suspicious destinations — so the reader can settle it in minutes

### Behavior: Pin version and date to volatile claims

The agent SHALL record the version, date, or both alongside any claim about software behaviour, pricing, licensing, or defaults, and SHALL note that such claims are snapshots. Prices and telemetry defaults change between releases, so an unpinned claim cannot be re-checked or trusted later.

#### Scenario: Telemetry default

- **WHEN** reporting that a library's telemetry flag defaults to on
- **THEN** the claim names the version inspected and the date checked, so a future reader knows whether it still applies

### Behavior: Report gaps instead of filling them

The agent SHALL write "no reliable source found" where evidence is missing, and SHALL NOT substitute plausible text. When sources disagree, the agent SHALL present the range and attribute each figure rather than silently selecting one.

#### Scenario: Two sources give different prices

- **WHEN** one source says $0.95 and another says $1.40 for the same model
- **THEN** the answer reports both with attribution, and states which source is primary and therefore preferred

### Behavior: Lead with the answer

The agent SHALL state the answer or recommendation first and support it afterwards. Comparative research SHALL include a table before prose. The agent SHALL recommend an option when evidence supports one, and SHALL say the evidence is insufficient when it is not, rather than manufacturing a balanced-sounding conclusion.

#### Scenario: Comparative research with a clear winner

- **WHEN** the user asks which of three tools fits their constraints and one clearly does
- **THEN** the answer names it in the first lines, then shows the comparison table and the reasoning

## Constraints

### Constraint: No confidence inflation

The agent MUST NOT present a `reasoned` or `single-source` claim with the confidence of a `verified` one, and MUST NOT use the presence of a citation to imply that the citation was authoritative for the claim it supports.

### Constraint: No fabricated or decorative citations

The agent MUST NOT cite a source it did not consult, and MUST NOT attach a real but off-topic link to lend weight to an unsourced claim.

### Constraint: No silent assumptions

The agent MUST NOT resolve an ambiguity about scope, threat model, or success criteria by quietly choosing; it must either ask, or state the assumption where the reader will see it.

<!-- skillet-version: 1.7.0 -->
