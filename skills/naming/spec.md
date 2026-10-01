# Naming

## Intent

Make the agent name a project, tool, package, or repository the way this house names things: by asking the questions that decide the namespaces first, checking availability mechanically, and only then choosing a legible, ownable word. The skill exists so a name is a ten-minute decision with evidence, not a multi-day search, and so the search is never run blind twice. It is for setting up a coding project and its package-registry namespacing — the names the thing will be built under and shared under.

The skill pairs with the `interaction-questioning` skill: when a gating fact about the target is not stated, the agent questions the human one question at a time instead of assuming, then proceeds on the answers.

## Triggers

- **SHOULD** trigger when the user asks to name a project, tool, package, CLI, repository, or the package-registry namespace(s) a coding project will ship under.
- **SHOULD** trigger when an existing name must be checked or cleared against one or more package registries before use.
- **SHOULD NOT** trigger for naming local variables, functions, parameters, or other in-code identifiers, where the criteria and registry checks do not apply.
- **SHOULD NOT** trigger when the user is only asking a factual question about a name or registry, not opening a naming decision.

## Behaviors

### Behavior: Clarify the target before searching

The agent SHALL establish the gating facts about the thing being named before considering any candidate word, and SHALL default to asking the human (via `interaction-questioning`, one question at a time) rather than assuming any of them.

#### Scenario: A tool with a planned port

- **GIVEN** a user asks the agent to name a new repo-management tool
- **WHEN** the user has not stated the language or any planned ports
- **THEN** the agent asks, one question at a time, how the thing is used, which language it is built in, whether a port (e.g. Rust or Go) is planned, which OSes and ecosystems it targets, how it will be distributed, and how public the ship is — and does not begin choosing words until these are answered.

#### Scenario: Facts already stated

- **GIVEN** the user has already stated the language, targets, and distribution channel
- **WHEN** the skill is active
- **THEN** it proceeds without re-asking those facts.

### Behavior: Establish the gating namespaces from language and distribution

The agent SHALL derive the set of namespaces a candidate must clear, from the primary language, any planned ports, and the distribution channel, and SHALL check every one of them — not only today's.

#### Scenario: Python now, Rust later

- **GIVEN** a tool is written in Python with a planned Rust port
- **WHEN** the agent checks a candidate name
- **THEN** it checks PyPI and crates.io (and any Homebrew or GitHub-org channel named), and a candidate is only available if it clears all of them.

#### Scenario: The mapping is configurable per session

- **GIVEN** a registry the mapping does not yet cover
- **WHEN** the agent needs to check a namespace for an unlisted registry
- **THEN** it supplies a per-session registry mapping via `check-name` arguments or a config file, without requiring the skill itself to be re-edited.

### Behavior: Evaluate candidates against the naming criteria

The agent SHALL judge every candidate on the same fixed axes — legibility (strict or loose), metaphor-integrity, ownability, constellation-distinctness, and ergonomics — and SHALL mark a candidate unacceptable when it fails the verb surface of the tool.

#### Scenario: A name that strains lock and pin

- **GIVEN** a repo manager whose verbs are `update`, `upgrade`, `lock`, `pin`, `sync`, `status`
- **WHEN** a candidate direction-word such as `downstream` is proposed
- **THEN** the agent flags it: `downstream pin` strains (you pin a point, not a flow), and the name is not acceptable as-is.

#### Scenario: Two legibility standards

- **GIVEN** the user has allowed both strict and loose legibility
- **WHEN** the agent reports candidates
- **THEN** it separates names a stranger can read as "manages repos" (strict) from names that only avoid misleading and carry meaning via etymology (loose).

### Behavior: Check availability mechanically

The agent SHALL run `scripts/check-name` over the surviving candidates rather than recalling availability from memory, and SHALL treat its machine-readable classification (`free`, `taken`, `collision`, `541-claimable`) as the availability evidence.

#### Scenario: A literature-name candidate

- **GIVEN** a candidate word that is plausibly taken in a package registry
- **WHEN** the agent runs `scripts/check-name` on it
- **THEN** the script reports the registry status with the package summary, last upload, and release count for any taken PyPI name, plus the top GitHub hits and watchlist flags, and the agent relays that verdict instead of guessing.

### Behavior: Resolve collisions before conceding or excluding

The agent SHALL apply, in order, the registry-name-vs-binary-name split, the `-cli`-style compound, and PEP 541 name transfer before reporting a loved name as lost.

#### Scenario: The bare name is taken but the binary is not

- **GIVEN** `redge` is taken on PyPI but `redge-cli` is free and the binary may remain `redge`
- **WHEN** the user wants the name `redge`
- **THEN** the agent recommends `redge-cli` as the registry namespace with `redge` as the binary, and does not report `redge` as available.

#### Scenario: A dead package on PyPI

- **GIVEN** the desired name is taken on PyPI by a package with no releases in years and non-responsive ownership
- **WHEN** the agent assesses whether the name can be reclaimed
- **THEN** it reports it as `541-claimable`, and reports a small-but-live package as `taken`, not `541-claimable`.

### Behavior: Scale the process to the stakes

The agent SHALL use a light path (criteria plus `check-name`, no model council) for low-stakes names and a full path (advisor and researcher panels) for public or high-stakes names, and SHALL ask the human to confirm the path when the stakes are unclear.

#### Scenario: An internal script name

- **GIVEN** the user wants a name for a throwaway `~/bin` script
- **WHEN** the skill is active
- **THEN** the agent runs the criteria and `check-name` only, and does not convene a council.

#### Scenario: A public tool name

- **GIVEN** a tool that will ship publicly to strangers
- **WHEN** the skill is active
- **THEN** the agent may convene advisor and researcher panels before narrowing the shortlist, and confirms the path with the human when uncertain.

### Behavior: Converge and record the decision

The agent SHALL stop generating when families repeat without a clear winner rather than continuing indefinitely, SHALL leave the final pick to the human, and SHALL record the decision and any new collision data for reuse.

#### Scenario: Repeated dead ends

- **WHEN** the search has covered several metaphor families and every surviving candidate is from an earlier shortlist
- **THEN** the agent presents the final shortlist, states its recommendation, and asks the human to choose or delegate the choice, instead of generating more names.

## Constraints

### Constraint: Never call a name available without checking every gating namespace

The agent MUST NOT state that a name is available, or recommend it, unless `scripts/check-name` has cleared it against every namespace derived from the language, the planned ports, and the distribution channel.

### Constraint: Never treat a live package as PEP 541 reclaimable

The agent MUST NOT report a PyPI name as `541-claimable` when the package shows recent activity or is merely small; PEP 541 applies to abandoned, non-responsive ownership, not to names the agent simply wants.

### Constraint: Never hand-edit a registry mapping into the skill

The agent MUST NOT hardcode a new registry's namespace into the skill or script such that covering it requires rebuilding the skill; namespace coverage is extended per session through `check-name` arguments or configuration.

### Constraint: Never conflate sibling tools' nouns

The agent MUST NOT recommend a name whose metaphor or noun overlaps the domain of a sibling tool on the same machine (for example, a repo manager must not read as config/state management when `topical` already owns that noun).

<!-- skillet-version: 1.8.0 -->
