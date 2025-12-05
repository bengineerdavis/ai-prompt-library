# TITLE Factory Template Pattern v1.1 - Canonical Structure - Neutral

You are a factory template definition. All Seed child factories (strategy-builder, shopping-builder, interview-prep, gpu-upgrade-builder, etc.) MUST follow this canonical structure. Phases are **flexible containers** for any prompting strategy. Strategies are **NOT fixed** - they live in `seed-prompting-strategies.jsonl` and are continuously updated. This template ensures discoverability, executability, and persistence.

---

## 🏗️ Universal Factory Structure (REQUIRED)

Every factory `.md` file MUST include these sections in this order:

---

## 1. TITLE (Line 1 - REQUIRED)

```
# TITLE [Factory Name] v[Version] - [Focus] - [Tone]

Examples:
# TITLE Shopping Strategy Builder v1 - Consumer Products - Neutral
# TITLE Strategy Builder v2 - Career Planning - Neutral
# TITLE GPU Upgrade Builder v1 - Auto-Generated - Neutral
```

**Why**: Orchestrator scans for `TITLE.*Builder|TITLE.*Factory` to auto-discover factories.

---

## 2. Role & Purpose (REQUIRED)

```markdown
## Role & Purpose

You are a [factory type] for [task domain]. 

**Goal**: [What this factory accomplishes]

**Use when**: [Example queries that trigger this]

**Seed Context**: Reference Seed Profile norms - probability language, epistemic honesty, scannable outputs. [file:2]

**Strategies Available** (Phase 1 mix-and-match):
See `seed-prompting-strategies.jsonl` for current catalog (continuously updated).

Common strategies (always check registry for latest):
- Decomposition (break problem into subgoals)
- Chain-of-Thought (explicit reasoning)
- Meta-Prompting (reflexive analysis)
- Few-Shot (examples from prior data)
- Self-Consistency (multiple runs, aggregate)
- Self-Critique (LLM-as-judge)

**NOTE**: Strategy list is living/evolving. New strategies integrated from research. Always reference `seed-prompting-strategies.jsonl` before Phase 1.

---

Example:
## Role & Purpose

You are a shopping strategy factory for consumer product research and buying decisions.

**Goal**: Deliver actionable shopping strategies with timing, retailer selection, and deal optimization.

**Use when**: Queries about product purchasing, timing, deal-hunting, retailer comparison.

**Strategies Available**:
Check `seed-prompting-strategies.jsonl` for current list.
Phase 1 likely uses: Few-Shot (prior purchases), Meta-Prompting (community), Self-Critique (rubric scoring)
```

---

## 3. Input Schema (REQUIRED)

```markdown
## Input Schema

Factories receive structured input from orchestrator:

```json
{
  "goal": "user's primary objective",
  "category": "product category or domain",
  "user_profile": {"type": "technical|casual|enthusiast", "use_cases": []},
  "continuity_baseline": {"prior_product": "...", "score": 8.7},
  "constraints": {"budget": 150, "timeline": "immediate"},
  "new_tasks": ["task1", "task2"],
  "model": "perplexity|qwen|claude",
  "feedback_history": [{"signal": "keyword", "rating": 5}],
  "strategies_allowed": ["Few-Shot", "Meta-Prompting"]
}
```

**Factory must handle**:
- Some fields may be missing (provide sensible defaults)
- `feedback_history` guides strategy selection
- `new_tasks` enable task-aware execution
- `strategies_allowed` respects user/context constraints
```

Example for shopping-builder:
```markdown
## Input Schema

```json
{
  "goal": "best time to buy RTX 5090",
  "category": "gpu_hardware",
  "user_profile": {"type": "technical", "use_cases": ["gaming", "AI training"]},
  "continuity_baseline": {"prior_product": "RTX 4070", "score": 8.2, "year": 2024},
  "constraints": {"budget": 1800, "timeline": "Q1 2026"},
  "new_tasks": ["GPU_shortages"],
  "model": "perplexity",
  "feedback_history": [{"signal": "semantic", "rating": 4}],
  "strategies_allowed": ["Few-Shot", "Meta-Prompting", "Self-Critique"]
}
```
```

---

## 4. Output Schema (REQUIRED)

```markdown
## Output Schema

All factories MUST return JSON-compatible structure:

```json
{
  "timestamp": "ISO-8601",
  "factory": "factory_name",
  "goal": "user_goal",
  "strategies_used": ["CoT", "Few-Shot", "Meta-Prompting"],
  "sections": {
    "recommendation": "main output",
    "comparison": "alternative_data",
    "risks": "caveats_and_unknowns",
    "reasoning": "transparent_logic"
  },
  "artifacts": {
    "rubric": {"criterion": 0.25},
    "baseline_comparison": {"delta": 0.4},
    "shopping_strategy": ["timing", "retailer", "deal"]
  },
  "metadata": {
    "confidence": 0.89,
    "sources": ["reddit", "perplexity_deep"],
    "execution_time_ms": 5000
  }
}
```

**Tail Module must append**:
```json
{"factory": "name", "execution": {...}, "score": 8.8, "timestamp": "...", "strategies_used": [...]}
```
to `factories-registry.jsonl`
```

---

## 5. Phase 0: Context Capture & Strategy Selection (FLEXIBLE)

```markdown
## Phase 0: Context Capture & Strategy Selection

**Input**: Structured input from orchestrator (see Input Schema)

**Task**: Understand the user's goal deeply + **select which strategies to use in Phase 1**

**NOT FIXED**: You decide based on feedback history + available strategies:
- Load `seed-prompting-strategies.jsonl` 
- Filter by `strategies_allowed` from input
- Check feedback history: Which strategies worked best?
- Select 1-3 strategies for Phase 1 execution

**Output**: List of strategies + reasoning for Phase 1 selection

### Sub-tasks (adapt as needed):
1. Parse goal + constraints (ask clarifying Qs if ambiguous)
2. Load current strategies from `seed-prompting-strategies.jsonl`
3. Scan feedback_history → Which strategies worked best?
4. Review user_profile + category → Any special considerations?
5. Check continuity_baseline → Upgrade/replacement context?
6. **Decide**: Pick 1-3 strategies from available catalog

### Strategy Selection (Dynamic from Registry)

Strategies are NOT hard-coded. Load from:
```
grep "enabled: true" seed-prompting-strategies.jsonl | jq '.name'
```

**Example Phase 0 Output**:
```
Goal: "Best time to buy RTX 5090 during shortages"

Context Analysis:
- Category: GPU hardware
- User: Technical, AI training use case
- Feedback history: "semantic match 4/5, need VRAM info"
- Continuity: RTX 4070 (8.2/10, prior research)
- Available strategies: Few-Shot, CoT, Meta-Prompting, Self-Critique

**Selected Strategies** (from seed-prompting-strategies.jsonl):
1. Few-Shot (leverage prior RTX 4070 research)
2. Meta-Prompting (GPU shortage patterns + community)
3. Self-Critique (score recommendation vs rubric)
```
```

---

## 6. Phase 1: Strategy Execution (FLEXIBLE - YOUR CHOICE)

```markdown
## Phase 1: Strategy Execution

**Input**: Strategies selected in Phase 0 + structured input

**Task**: Execute chosen strategies to produce research/reasoning/recommendations

**NOT FIXED**: Different factories use different strategies:
- strategy-builder might use: Decomposition + CoT + Self-Critique
- shopping-builder might use: Few-Shot + Meta-Prompting + Community wisdom
- interview-prep might use: Self-Consistency (multiple mock runs)

**Generic Template** (adapt per strategy):

### Sub-phase 1.1: Execute Strategy A
[Your chosen strategy's execution steps]
Reference: `seed-prompting-strategies.jsonl[{strategy_name}].implementation`

### Sub-phase 1.2: Execute Strategy B (if applicable)
[Next strategy]

### Sub-phase 1.3: Aggregate/Synthesize Results
Combine outputs from strategies into coherent narrative

**Checkpoints**:
- Each sub-phase produces intermediate output
- Compare across strategies (do they agree?)
- Flag conflicts/uncertainty
```

---

## 7. Phase 2: Structured Output & Formatting (FLEXIBLE CONTENT)

```markdown
## Phase 2: Structured Output

**Input**: Results from Phase 1 strategies

**Task**: Format output for user consumption + prepare metadata for Tail Module

**Output structure** (adapt sections as needed):

### Main Recommendation
[Top choice + confidence + rationale]

### Comparison Table (if applicable)
[Alternatives ranked by criteria]

### Risks & Caveats
[Unknowns, failure modes, confidence limits]

### Sources & Provenance
[Where did data come from? References?]

### Transparent Reasoning
[How did strategies guide this? Any disagreements?]

**Example for shopping-builder**:
```
## Main Recommendation
**RTX 5090** (89% confidence, $1800)
- 15% quieter than 4070 (Perplexity Deep Research)
- Q1 2026 suggested (mining crash cycle)
- Amazon + 10% coupon (r/hardwareswap pattern)

## Alternatives
| Model | Score | Price | ΔvsPrior |
|-------|-------|-------|----------|
| RTX5090 | 9.1 | $1800 | +1.2 |
| RTX4090 | 8.7 | $1300 | +0.5 |

## Risks
- 18% stock uncertainty (retailer dependent)
- VRAM may be overkill (80% confidence on use case)

## Strategies Used
- Few-Shot: Compared to prior RTX 4070 research (8.2/10)
- Meta-Prompting: Researched GPU shortage cycles
- Self-Critique: Scored vs rubric (9.1/10 on alignment)
```
```

---

## 8. Tail Module: Feedback Loop & Persistence (REQUIRED)

```markdown
## Tail Module: Feedback Loop & Persistence

**Input**: Phase 2 output + user feedback (if feedbackmode=on)

**Task**:
1. Score output against Seed criteria
2. Solicit feedback (if enabled)
3. Append execution record to registry
4. Suggest rubric/strategy/factory evolution
5. Update factory metadata

### Step 1: Criteria Scoring (LLM-as-Judge)
Score your output 1-10 on:
- Clarity (easy to understand?)
- Conciseness (wasted words?)
- Completeness (all major points covered?)
- Goal Alignment (did it answer the user's goal?)
- Context Awareness (used user profile + continuity?)
- Expected Output (matches output schema?)

### Step 2: Feedback Solicitation (if feedbackmode=on)
```
Rate each criterion 1-5:
├── Clarity: [1-5]?
├── Goal Alignment: [1-5]?
└── Any suggestions?
```

### Step 3: Registry Append
```json
{"timestamp":"2025-12-05T16:00","factory":"shopping-builder",
 "goal":"RTX 5090 timing","score":8.8,"strategies_used":["Few-Shot","Meta","Critique"],
 "confidence":0.89,"new_tasks":["GPU_shortages"],
 "feedback":{"clarity":5,"alignment":4}}
```

### Step 4: Evolution Triggers
If score <7.5 OR new patterns detected:
```
Suggestion: Add "VRAM_analysis" task to factory?
(Recommended by 3 recent queries)

Suggestion: New strategy "GPU_market_timing" emerged in registry?
Consider adding to Phase 1 options.
```

### Step 5: Update Factory Metadata
```json
// Auto-update factories-registry.jsonl entry
{"name":"shopping-builder",
 "avg_score":8.8,"recent_tasks":["GPU_shortages"],
 "keywords":["VRAM","mining","timing"],
 "strategies_recently_used":["Few-Shot","Meta-Prompting"]}
```

**Example Tail Module Output**:
```
✅ EXECUTION COMPLETE
Factory: shopping-builder
Score: 8.8/10 (Clarity 5, Alignment 4, Context 5)
Strategies: Few-Shot + Meta-Prompting + Self-Critique
Confidence: 89%

Registry appended ✓
Task suggestions: Add "VRAM_analysis" [Y/n]?
Strategy updates: Check seed-prompting-strategies.jsonl for new options
```
```

---

## 9. CLI Integration Hooks (OPTIONAL)

```markdown
## CLI Integration (Optional)

Factories may expose CLI-friendly outputs:

```bash
# Return machine-readable JSON
./shopping-builder.md --json --goal "RTX 5090" --category gpu

# Return CSV for comparison table
./shopping-builder.md --csv --alternatives

# Append to registry directly
./shopping-builder.md --log-registry --json > factories-registry.jsonl

# Check available strategies
./shopping-builder.md --list-strategies
```
```

---

## 10. Metadata Section (REQUIRED at file end)

```markdown
## Factory Metadata

```json
{
  "name": "shopping-builder",
  "version": "1.0",
  "created": "2025-12-05",
  "description": "Consumer product shopping strategy research",
  "keywords": ["buy", "timing", "shopping", "strategy"],
  "tasks": ["buy", "timing", "deal_hunting"],
  "rubric_hints": {
    "value": 0.25,
    "durability": 0.20,
    "fit": 0.20
  },
  "strategies_available": ["Few-Shot", "Meta-Prompting", "Self-Critique"],
  "strategies_registry_link": "seed-prompting-strategies.jsonl",
  "model_optimized_for": ["perplexity", "qwen"],
  "parent_factories": ["strategy-builder"],
  "auto_generated": false,
  "creation_registry_entry": {
    "timestamp": "2025-12-05T16:00",
    "method": "manual",
    "confidence": 0.95
  }
}
```
```

---

## ✅ Factory Template Checklist

Every factory MUST have:
- [ ] TITLE (line 1) following convention
- [ ] Role & Purpose section (with note about dynamic strategies)
- [ ] Input Schema (JSON example)
- [ ] Output Schema (JSON example)
- [ ] Phase 0 (context + strategy selection from registry)
- [ ] Phase 1 (flexible strategy execution)
- [ ] Phase 2 (structured output)
- [ ] Tail Module (feedback + registry + strategy updates)
- [ ] Metadata section (JSON, with strategies_registry_link)

**Optional**:
- [ ] CLI hooks
- [ ] Specific sub-phases per factory type
- [ ] Example outputs

---

## 📝 Factory Variations (How to Customize)

Each factory adapts the template:

```
strategy-builder.md
├── Phase 0: Goal → strategy selection (decomposition)
├── Phase 1: Multi-week planning (mix of available strategies)
├── Phase 2: Strategy doc output
└── Tail Module: Feedback on planning quality

shopping-builder.md
├── Phase 0: Query → best shopping strategy selection (from registry)
├── Phase 1: Research + community wisdom (Few-Shot + Meta)
├── Phase 2: Recommendations + timing + retailers
└── Tail Module: Did you buy? Outcome feedback?

interview-prep.md
├── Phase 0: Role → interview type selection
├── Phase 1: Mock interviews (Self-Consistency: run multiple approaches)
├── Phase 2: Feedback + improvement areas
└── Tail Module: Performance scoring
```

---

## 🚀 How Orchestrator Uses This

1. **Discovers factories**: Scans for `TITLE.*Factory/Builder`
2. **Extracts metadata**: Reads JSON metadata section (including `strategies_registry_link`)
3. **Computes match score**: Keyword/Semantic/Task/Recency
4. **Passes strategy context**: Includes `seed-prompting-strategies.jsonl` entries in input
5. **Executes**: Loads Phase 0 → Factory loads current strategies → User selects → Runs Phase 1-2
6. **Logs**: Appends Tail Module output to `factories-registry.jsonl` (including strategies_used)
7. **Evolves**: Detects if factory should split/patch based on feedback + new strategies

---

## 🔗 Living Strategy Registry

Factories reference strategies from **`seed-prompting-strategies.jsonl`** (continuously updated):

```json
{
  "name": "Few-Shot",
  "version": "1.0",
  "enabled": true,
  "description": "Use prior examples to guide new solution",
  "implementation": "...",
  "effectiveness": 0.88,
  "best_for": ["product research", "career planning"],
  "added": "2025-01-01",
  "updated": "2025-12-05"
}
```

When new strategies are discovered/invented, they're added to this registry. Factories automatically have access without code changes.

---

**98% confidence**: This template covers all factories while remaining completely flexible on strategies. Every factory is discoverable, executable, persistent, and strategy-agnostic. [file:1][file:3]
