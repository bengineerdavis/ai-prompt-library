#!/usr/bin/env python3
"""
build_bootstrap.py - Seed System Bootstrap Generator v3.3
=========================================================
Reads your local seed-system files and generates ready-to-paste
bootstrap prompts for Perplexity, local models (Ollama/LM Studio),
or any SaaS LLM service.

Usage:
    python3 build_bootstrap.py                          # auto-detect seed-system/ dir
    python3 build_bootstrap.py --dir /path/to/seed-system
    python3 build_bootstrap.py --output bootstrap-out/ # custom output dir
    python3 build_bootstrap.py --target ollama          # ollama-optimised compact format
    python3 build_bootstrap.py --target perplexity      # default: 3-paste format
    python3 build_bootstrap.py --target single          # single-paste for large-context models
    python3 build_bootstrap.py --target api             # JSON structure for API/script use
    python3 build_bootstrap.py --validate               # validate registry + strategies only

Targets:
    perplexity  3 separate paste blocks (registry / orchestrator / strategies)
    ollama      Same 3-paste but with compact whitespace for local models
    single      One combined paste for 128k+ context models (GPT-4o, Claude, Gemini)
    api         JSON file with all components; load programmatically

Output files (in --output dir, default ./bootstrap-out/):
    BOOTSTRAP-PASTE-1-registry.md
    BOOTSTRAP-PASTE-2-orchestrator.md
    BOOTSTRAP-PASTE-3-strategies.md
    BOOTSTRAP-SINGLE.md              (single target only)
    BOOTSTRAP-API.json               (api target only)
    BOOTSTRAP-QUICKSTART.md          (always generated)
    CHANGELOG.md                     (always generated)
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

VERSION = "3.3"
STRAT_VERSION = "1.1"
UPDATED = "2026-03-28"

REGISTRY_FILENAME   = f"factories-registry-v{VERSION}.jsonl"
STRATEGIES_FILENAME = f"seed-prompting-strategies-v{STRAT_VERSION}.jsonl"

INLINE_REGISTRY = [
    {"name":"seed-profile","version":"3","type":"global","description":"Global behavior norms and defaults","enabled":True,"last_updated":"2025-12-05","keywords":["tone","epistemic","criteria","norms"]},
    {"name":"seed-orchestrator-v3.3","version":"3.3","type":"orchestrator","description":"Session entrypoint, 4-signal matching, task expansion confirmation, model council support","enabled":True,"last_updated":"2026-03-28","keywords":["orchestrator","routing","matching","factory-selection","council"]},
    {"name":"shopping-builder","version":"1.0","type":"factory","description":"Product research and buying strategy factory","enabled":True,"last_updated":"2025-12-05","parent":"seed-profile","tasks":["buy","timing","deal_hunting","comparison"],"keywords":["product","shopping","timing","deal","purchase","review"],"rubric":{"value":0.25,"durability":0.20,"fit":0.20,"timing":0.20,"price":0.15},"strategies":["Few-Shot","Meta-Prompting","Self-Critique"],"recent_scores":[9.1,8.7,9.2,8.9,9.0],"avg_score":8.98},
    {"name":"strategy-builder","version":"1.1","type":"factory","description":"Multi-week planning and roadmap strategy factory","enabled":True,"last_updated":"2026-03-28","parent":"seed-profile","tasks":["planning","roadmap","multi-week","decomposition"],"keywords":["strategy","planning","roadmap","timeline","phase"],"rubric":{"clarity":0.25,"completeness":0.25,"feasibility":0.25,"coherence":0.25},"strategies":["Decomposition","Chain-of-Thought","Self-Critique","Mixture-of-Roles"],"recent_scores":[8.8,8.6,8.9,8.7],"avg_score":8.75},
    {"name":"interview-prep","version":"1.0","type":"factory","description":"Interview preparation and mock interview factory","enabled":True,"last_updated":"2025-12-05","parent":"seed-profile","tasks":["interview","mock","prep","feedback"],"keywords":["interview","mock","preparation","practice","1:1","behavioral"],"rubric":{"technical":0.30,"communication":0.25,"problem_solving":0.25,"depth":0.20},"strategies":["Self-Consistency","Self-Critique","Few-Shot"],"recent_scores":[8.5,8.7,8.4,8.6],"avg_score":8.55},
    {"name":"factory-builder-v1","version":"1.1","type":"meta-factory","description":"Generates new factories from domain specifications","enabled":True,"last_updated":"2026-03-28","parent":"seed-profile","tasks":["factory_generation","factory_refactoring","factory_split"],"keywords":["factory","generation","creation","meta"],"strategies":["Meta-Prompting","Decomposition","Model-Council-Generate","Model-Council-Judge","Mixture-of-Roles"],"recent_scores":[8.6,8.7,8.8],"avg_score":8.70,"preferred_judge_models":["claude","qwen","perplexity"]},
    {"name":"wealth-advisor-and-builder","version":"1.1","type":"factory","description":"Wealth planning for mid-career catch-up with employment risk, Boglehead-style","enabled":True,"last_updated":"2026-03-28","parent":"strategy-builder","tasks":["wealth","catchup","swr","runway","boglehead"],"keywords":["wealth","finance","boglehead","swr","runway","late_start","retirement"],"rubric":{"clarity":0.2,"feasibility":0.25,"goal_alignment":0.25,"risk_awareness":0.2,"context_awareness":0.1},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique","Mixture-of-Roles"],"recent_scores":[8.7,8.9,8.6],"avg_score":8.73},
    {"name":"technical-tutor-for-self-learning","version":"1.1","type":"meta-factory","description":"Meta-factory that generates domain-specific technical tutors. All tutors follow Co-Pilot + Failure Review + Study Session pattern.","enabled":True,"last_updated":"2026-03-28","parent":"strategy-builder","tasks":["factory_generation","tutor_deployment","study_plan_design","learner_profiling"],"keywords":["tutor","self-learning","technical","study","co-pilot","failure-review","mastery","mentor","learning"],"rubric":{"domain_coverage":0.25,"job_relevance":0.25,"pedagogical_soundness":0.25,"cognitive_load_management":0.15,"constraint_fit":0.10},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique","Constraint-Based-Reasoning","Model-Council-Generate","Mixture-of-Roles"],"generates":"{domain-slug}-tutor-v1.md","recent_scores":[8.7],"avg_score":8.70,"preferred_judge_models":["claude","qwen","perplexity"]},
    {"name":"sentry-support-tutor","version":"1.1","type":"factory","description":"Co-pilot, failure review, and study guide factory for a Senior Support Engineer accelerating Sentry.io mastery.","enabled":True,"last_updated":"2026-03-28","parent":"technical-tutor-for-self-learning","tasks":["co_pilot","failure_review","study_session","pattern_tracking","question_discipline"],"keywords":["sentry","support","tutor","copilot","study","triage","tickets","SDK","failure-review","breadcrumbs","DSN","tracing","issues","events","escalation"],"rubric":{"clarity":0.2,"feasibility":0.25,"goal_alignment":0.25,"risk_awareness":0.2,"context_awareness":0.1},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique","Mixture-of-Roles"],"recent_scores":[8.8],"avg_score":8.80},
    {"type":"strategy","name":"Few-Shot","description":"Use prior examples to guide solution","enabled":True,"effectiveness":0.88,"best_for":["product_research","career_planning","buying_decisions"]},
    {"type":"strategy","name":"Chain-of-Thought","description":"Explicit reasoning steps","enabled":True,"effectiveness":0.87,"best_for":["planning","analysis","problem_solving"]},
    {"type":"strategy","name":"Meta-Prompting","description":"Reflect on reasoning and biases","enabled":True,"effectiveness":0.82,"best_for":["strategy","research","community_wisdom"]},
    {"type":"strategy","name":"Self-Critique","description":"LLM-as-judge scoring","enabled":True,"effectiveness":0.86,"best_for":["all_tasks"]},
    {"type":"strategy","name":"Decomposition","description":"Break problem into subgoals","enabled":True,"effectiveness":0.84,"best_for":["planning","complex_tasks"]},
    {"type":"strategy","name":"Self-Consistency","description":"Multiple runs, aggregate results","enabled":True,"effectiveness":0.83,"best_for":["interviews","high_stakes"]},
    {"type":"strategy","name":"Model-Council-Generate","description":"Run Phase 1 against 2-3 models independently, collect candidates","enabled":True,"effectiveness":0.88,"best_for":["meta-factory generation","recursive prompts","factory-builder"]},
    {"type":"strategy","name":"Model-Council-Judge","description":"Score candidates across 2-3 judge models, aggregate, flag disagreement","enabled":True,"effectiveness":0.91,"best_for":["factory output validation","meta-factory judging","high-stakes decisions"]},
    {"type":"strategy","name":"Mixture-of-Roles","description":"Simulate council with Skeptic/Expert/Pragmatist role assignments on one model","enabled":True,"effectiveness":0.83,"best_for":["manual mode","budget-constrained","strategy decisions"]},
]

INLINE_STRATEGIES = [
    {"name":"Decomposition","version":"1.0","enabled":True,"description":"Break complex goal into subgoals/phases.","implementation":"Phase 1: Parse goal -> identify sub-phases -> execute each -> synthesize","effectiveness":0.89,"best_for":["multi-week planning","complex research","system design"],"requires_multiple_runs":False,"computational_cost":"low","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Wei et al., Chain-of-Thought Prompting","tags":["reasoning","structuring","optimization"]},
    {"name":"Chain-of-Thought","version":"1.0","enabled":True,"description":"Explicit step-by-step reasoning. Improves accuracy on complex tasks.","implementation":"Phase 1: 'Let's think step by step' -> trace reasoning -> show work -> conclusion","effectiveness":0.87,"best_for":["problem solving","research","technical reasoning"],"requires_multiple_runs":False,"computational_cost":"low","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Wei et al., Chain-of-Thought Prompting","tags":["reasoning","transparency","validation"]},
    {"name":"Meta-Prompting","version":"1.0","enabled":True,"description":"Reflect on the problem. Inject domain wisdom.","implementation":"Phase 1: Ask meta-questions -> research patterns -> synthesize knowledge -> guide solution","effectiveness":0.82,"best_for":["product research","market analysis","domain-specific queries"],"requires_multiple_runs":False,"computational_cost":"medium","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Community patterns + Reddit analysis","tags":["reasoning","context","optimization"]},
    {"name":"Few-Shot","version":"1.0","enabled":True,"description":"Use prior examples as anchors. Learn from continuity baseline.","implementation":"Phase 1: Load continuity_baseline -> extract key features -> compare to new problem -> note improvements","effectiveness":0.88,"best_for":["product upgrades","repeated domains","career decisions"],"requires_multiple_runs":False,"computational_cost":"low","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Brown et al., Few-shot Learning","tags":["learning","comparison","optimization"]},
    {"name":"Self-Consistency","version":"1.0","enabled":True,"description":"Run strategy multiple times, aggregate votes/average for robustness.","implementation":"Phase 1: Execute strategy 3x -> collect results -> vote/average -> select consensus or flag disagreements","effectiveness":0.85,"best_for":["high-uncertainty decisions","benchmark scoring","validation"],"requires_multiple_runs":True,"computational_cost":"high","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Wang et al., Self-Consistency","tags":["validation","robustness","uncertainty"]},
    {"name":"Self-Critique","version":"1.0","enabled":True,"description":"LLM scores own output against rubric. Iterate until satisfied.","implementation":"Phase 2: Score output vs rubric (1-10) -> identify failures -> suggest patches -> optionally re-run Phase 1","effectiveness":0.84,"best_for":["quality assurance","optimization","refinement"],"requires_multiple_runs":False,"computational_cost":"medium","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Self-evaluation patterns","tags":["validation","optimization","feedback"]},
    {"name":"Perspective-Taking","version":"1.0","enabled":True,"description":"Solve from multiple viewpoints: Angel + Devil + Domain expert.","implementation":"Phase 1: Generate 3 independent perspectives -> reason from each -> synthesize -> identify blindspots","effectiveness":0.80,"best_for":["strategy decisions","risk analysis","bias detection"],"requires_multiple_runs":False,"computational_cost":"medium","model_compatibility":["perplexity","qwen","claude"],"added":"2025-12-05","updated":"2025-12-05","research_ref":"Decision theory + cognitive bias research","tags":["reasoning","validation","bias-checking"]},
    {"name":"Community-Wisdom-Injection","version":"1.0","enabled":True,"description":"Research community consensus. Weight by source credibility.","implementation":"Phase 1: Search forums -> aggregate sentiment -> extract patterns -> cite sources -> integrate","effectiveness":0.78,"best_for":["product research","buying decisions","trend analysis"],"requires_multiple_runs":False,"computational_cost":"medium","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Market research + community analysis","tags":["research","social-proof","validation"]},
    {"name":"Constraint-Based-Reasoning","version":"1.0","enabled":True,"description":"Identify hard constraints first. Optimize within feasible region.","implementation":"Phase 1: List constraints -> filter candidates -> score remaining -> rank","effectiveness":0.86,"best_for":["budget decisions","technical choices","vendor selection"],"requires_multiple_runs":False,"computational_cost":"low","model_compatibility":["perplexity","qwen","claude"],"added":"2025-12-05","updated":"2025-12-05","research_ref":"Operations research + constraint satisfaction","tags":["optimization","filtering","decision-making"]},
    {"name":"Rubric-Based-Scoring","version":"1.0","enabled":True,"description":"Define weighted criteria. Score each option. Compute composite scores.","implementation":"Phase 2: Define rubric (criteria + weights) -> score 1-10 -> multiply by weight -> sum -> rank","effectiveness":0.87,"best_for":["product comparison","vendor selection","hiring decisions"],"requires_multiple_runs":False,"computational_cost":"low","model_compatibility":["perplexity","qwen","claude"],"added":"2025-01-01","updated":"2025-12-05","research_ref":"Multi-criteria decision analysis","tags":["evaluation","scoring","comparison"]},
    {"name":"Model-Council-Generate","version":"1.0","enabled":True,"description":"Run Phase 1 against 2-3 models independently. Collect candidates.","implementation":"Phase 1: Submit identical prompt to models [A,B,C] -> collect independent outputs -> tag with source model -> pass to Model-Council-Judge","effectiveness":0.88,"best_for":["meta-factory generation","recursive prompts","factory-builder","high-stakes first draft"],"requires_multiple_runs":True,"computational_cost":"high","model_compatibility":["perplexity","qwen","claude","gpt-4o"],"added":"2026-03-28","updated":"2026-03-28","research_ref":"Ensemble prompting + LLM routing research (2024)","tags":["ensemble","generation","diversity","meta","council"]},
    {"name":"Model-Council-Judge","version":"1.0","enabled":True,"description":"Send candidates to 2-3 judge models. Aggregate scores. Flag std_dev > 1.5 as uncertain.","implementation":"Phase 2: Take candidates -> submit to judge models [A,B,C] with rubric -> collect scores -> mean-aggregate or majority-vote -> flag disagreement (std_dev > 1.5) -> return ranked candidates","effectiveness":0.91,"best_for":["factory output validation","meta-factory judging","high-stakes decisions","prompt quality scoring"],"requires_multiple_runs":True,"computational_cost":"high","model_compatibility":["perplexity","qwen","claude","gpt-4o"],"added":"2026-03-28","updated":"2026-03-28","research_ref":"Constitutional AI + multi-judge eval patterns (Anthropic, 2024)","tags":["judging","validation","bias-reduction","ensemble","council"]},
    {"name":"Mixture-of-Roles","version":"1.0","enabled":True,"description":"Simulate council on one model: Skeptic, Domain Expert, Pragmatist roles.","implementation":"Phase 1: Assign role A (Skeptic) -> get output -> role B (Domain Expert) -> get output -> role C (Pragmatist) -> get output -> synthesize/vote","effectiveness":0.83,"best_for":["manual Perplexity mode","budget-constrained runs","factory-builder","strategy decisions"],"requires_multiple_runs":True,"computational_cost":"medium","model_compatibility":["perplexity","qwen","claude","gpt-4o"],"added":"2026-03-28","updated":"2026-03-28","research_ref":"Role-playing prompting + perspective-taking research (2024)","tags":["ensemble","roles","judging","bias-reduction","budget-friendly","council"]},
]

SEED_PROFILE_TEXT = """You are a meta-system designer, expert senior AI & prompt engineer, and technical coach for a senior IC or technical practitioner.

TONE & EPISTEMIC NORMS:
- Use probability language: "[~75% confidence]", "likely", "uncertain"
- Be epistemically honest: always include caveats and "where this might be wrong"
- Prioritize scannability: short sections, bullets, optional tables
- Respect time constraints: design outputs for the time available
- Treat user as a senior IC unless told otherwise
- Avoid walls of text; prioritize actionable outputs
- Technical depth over business buzzwords

EVALUATION CRITERIA (all outputs scored on):
1. Clarity  2. Conciseness  3. Completeness
4. Goal Alignment  5. Context Awareness  6. Expected Output

GLOBAL SWITCHES:
- interaction_mode: "interactive"
- feedback_mode: "on"
"""

ORCHESTRATOR_TEXT = f"""You are the Seed Orchestrator v{VERSION}. When I give you a goal, you:

PHASE 1 - MATCH: Compute 4-signal match against the loaded registry.
  Signal 1: Keyword match (40%) - overlap between query tokens and factory keywords
  Signal 2: Semantic match (30%) - intent alignment between query and factory purpose
  Signal 3: Task coverage (20%) - % of inferred required tasks the factory covers
  Signal 4: Recency/performance (10%) - factory avg_score / 10

  Thresholds:
  >=90% -> AUTO-RUN (state confidence, proceed)
  85-89% -> ASK "Run [factory]?" (default yes)
  75-84% -> Show top 3, ask user to pick
  <75%  -> Suggest creating a new factory with factory-builder-v1

  Show all 4 signals transparently every time.

PHASE 2 - TASK EXPANSION: If match >=75%, check if query implies tasks not in factory's task list.
  If new tasks detected, ask: "Add [task] to [factory]? [Y/n]"

PHASE 3 - EXECUTE: Tell me which factory .md to paste, or if fully manual, run the factory phases inline.

PHASE 4 - TAIL MODULE: After execution, ask me to rate 1-5 on Clarity / Relevance / Confidence.
  Log result. Suggest next step.

STRATEGY SELECTION (Phase 0 of any factory):
- Default: use strategies listed in the factory's registry entry
- Meta-factories + multi-model available: prepend Model-Council-Generate -> Model-Council-Judge
- Meta-factories + single model (manual mode): prepend Mixture-of-Roles
- Always show selected strategies before executing Phase 1

COUNCIL STRATEGIES:
- Model-Council-Generate: run Phase 1 prompt on 2-3 models independently, collect candidates
- Model-Council-Judge: send candidates to 2-3 judge models with rubric, aggregate scores,
  flag std_dev > 1.5 as uncertain
- Mixture-of-Roles (single-model fallback): run same prompt 3x as Skeptic / Domain Expert /
  Pragmatist, then synthesize

Acknowledge with: "Seed Orchestrator v{VERSION} ready. State your goal."
"""

STRATEGIES_READABLE = """CORE STRATEGIES (v1.0):
- Decomposition (0.89, low): Parse goal -> identify sub-phases -> execute each -> synthesize. Best for: multi-week planning, complex research, system design.
- Chain-of-Thought (0.87, low): 'Let's think step by step' prefix -> trace reasoning -> show work -> conclusion. Best for: problem solving, technical reasoning.
- Few-Shot (0.88, low): Load continuity_baseline -> extract key features -> compare to new problem -> note improvements/tradeoffs. Best for: product upgrades, repeated domains, career decisions.
- Rubric-Based-Scoring (0.87, low): Define rubric (criteria + weights) -> score each option 1-10 -> multiply by weight -> sum -> rank. Best for: product comparison, vendor selection.
- Constraint-Based-Reasoning (0.86, low): List constraints -> filter candidates -> score remaining -> rank. Best for: budget decisions, technical choices.
- Self-Critique (0.84, medium): Score output vs rubric (1-10 per criterion) -> identify failures -> suggest patches -> optionally re-run Phase 1. Best for: quality assurance, refinement.
- Meta-Prompting (0.82, medium): Ask meta-questions -> research community patterns -> synthesize domain knowledge -> guide solution. Best for: product research, domain-specific queries.
- Self-Consistency (0.85, high, requires_multiple_runs): Execute strategy 3x independently -> vote/average -> select consensus or flag disagreements. Best for: high-uncertainty decisions.
- Perspective-Taking (0.80, medium): Generate 3 independent perspectives -> reason from each -> synthesize -> identify blindspots. Best for: strategy decisions, risk analysis.
- Community-Wisdom-Injection (0.78, medium): Search forums -> aggregate sentiment -> extract patterns -> cite sources -> integrate. Best for: product research, buying decisions.

COUNCIL STRATEGIES (v1.1 - added 2026-03-28):
- Model-Council-Generate (0.88, high, requires_multiple_runs): Submit identical prompt to models [A,B,C] -> collect independent outputs -> tag with source model -> pass to Model-Council-Judge. Best for: meta-factory generation, recursive prompts.
- Model-Council-Judge (0.91, high, requires_multiple_runs): Submit candidates to judge models [A,B,C] with rubric -> collect scores -> mean-aggregate or majority-vote -> flag std_dev > 1.5 as uncertain -> return ranked candidates. Best for: factory output validation, high-stakes decisions.
- Mixture-of-Roles (0.83, medium, requires_multiple_runs): Assign role A (Skeptic) -> get output -> role B (Domain Expert) -> get output -> role C (Pragmatist) -> get output -> synthesize/vote. Best for: manual Perplexity mode, budget-constrained runs.
"""

CHANGELOG_TEXT = f"""# Seed System Changelog
System: Seed Orchestrator + Factory Registry
Maintained by: Ben Davis
Last updated: {UPDATED}

---

## v3.3 - 2026-03-28 (current)

### orchestrator-v3.3.py
- Breaking changes: None - fully backwards compatible with v3.2 registries
- New: FactoryEntry datatype with preferred_judge_models field
- New: ExecutionLog as proper @dataclass with to_dict()
- New: StrategyEntry datatype - typed mirror of seed-prompting-strategies.jsonl schema
- New: StrategyRegistry class - filter_by_use_case(), filter_by_tag(), filter_by_cost(),
       top_by_effectiveness(), for_factory(), append()
- Changed: Orchestrator.select_strategies() - new multi_model_available param
- Changed: Registry returns typed List[FactoryEntry] instead of raw dicts
- Changed: Signal 2 (semantic) - domain-rule boost system replaces static mock values
- Changed: Signal 3 (task) - expanded task_inference map with sentry/SDK triggers
- Changed: CLI accepts optional third arg [strategies.jsonl]
- Fixed: match_factory/match_all unclosed dict literals (syntax error in original)
- Fixed: Council guard now uses name-set check instead of object identity

### factories-registry-v3.3.jsonl
- seed-orchestrator-v3.2 -> v3.3: renamed, added council keyword
- factory-builder-v1: v1.0 -> v1.1: council strategies + preferred_judge_models
- technical-tutor-for-self-learning: v1.0 -> v1.1: council strategies + preferred_judge_models
- sentry-support-tutor: v1.0 -> v1.1: Mixture-of-Roles added
- wealth-advisor-and-builder: v1.0 -> v1.1: Mixture-of-Roles added
- strategy-builder: v1.0 -> v1.1: Mixture-of-Roles added
- New inline strategy entries: Model-Council-Generate, Model-Council-Judge, Mixture-of-Roles
- Total entries: 21 (was 17)

### seed-prompting-strategies-v1.1.jsonl
- New: Model-Council-Judge (effectiveness 0.91, high cost)
- New: Model-Council-Generate (effectiveness 0.88, high cost)
- New: Mixture-of-Roles (effectiveness 0.83, medium cost)
- New: companion seed-prompting-strategies-v1.1.md - docs split from .jsonl
- Total strategies: 13 (was 10)

---

## v3.2 - 2025-12-05 (original baseline)

### orchestrator-v3.2-hybrid.md
- Initial hybrid manual/scripted orchestrator
- 4-signal matching algorithm: keyword (40%), semantic (30%), task (20%), recency (10%)
- Three modes: MANUAL_MODE, SCRIPTED_MODE, HYBRID_MODE
- Confidence thresholds: >=90% auto-run, 85-89% ask, 75-84% top 3, <75% new factory
- Task expansion confirmation (Phase 2)
- Feedback loop + execution logging (Phase 4)

### factories-registry.jsonl (original)
- Initial entries: seed-profile, seed-orchestrator-v3.2, shopping-builder, strategy-builder,
  interview-prep, factory-template-v1.1, factory-builder-v1, seed-optimizer, role-specializer,
  6 inline strategy entries, wealth-advisor-and-builder, technical-tutor-for-self-learning,
  sentry-support-tutor (deduplicated)

### seed-prompting-strategies.jsonl (v1.0)
- 10 strategies: Decomposition, Chain-of-Thought, Meta-Prompting, Few-Shot, Self-Consistency,
  Self-Critique, Perspective-Taking, Community-Wisdom-Injection, Constraint-Based-Reasoning,
  Rubric-Based-Scoring

### orchestrator-match.sh
- Bash CLI: ./orchestrator-match.sh "query" registry.jsonl -> JSON with top match + 4 signals
"""


def find_seed_dir(override: Optional[str] = None) -> Optional[Path]:
    if override:
        p = Path(override)
        return p if p.exists() else None
    candidates = [
        Path("seed-system"),
        Path("../seed-system"),
        Path.home() / "seed-system",
        Path.cwd(),
    ]
    for c in candidates:
        if (c / REGISTRY_FILENAME).exists() or (c / "factories-registry.jsonl").exists():
            return c
    return None


def load_jsonl(path: Path) -> list:
    entries = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"  WARNING: Invalid JSON in {path.name}: {e}", file=sys.stderr)
    return entries


def registry_to_jsonl_block(entries: list) -> str:
    return "\n".join(json.dumps(e, separators=(",", ":")) for e in entries)


def validate_registry(entries: list) -> bool:
    ok = True
    names = set()
    for e in entries:
        name = e.get("name", "<unnamed>")
        if name in names:
            print(f"  WARNING: Duplicate entry: {name}", file=sys.stderr)
            ok = False
        names.add(name)
        if e.get("type") in ("factory", "meta-factory"):
            for field in ("tasks", "keywords", "strategies", "avg_score"):
                if field not in e:
                    print(f"  WARNING: Factory '{name}' missing field: {field}", file=sys.stderr)
                    ok = False
    return ok


def validate_strategies(entries: list) -> bool:
    ok = True
    for e in entries:
        for field in ("name", "effectiveness", "computational_cost"):
            if field not in e:
                print(f"  WARNING: Strategy missing field: {field}", file=sys.stderr)
                ok = False
    return ok


def build_paste_1(registry_entries: list, compact: bool = False) -> str:
    block = registry_to_jsonl_block(registry_entries)
    return f"""SEED SYSTEM BOOTSTRAP - PASTE 1 of 3: REGISTRY
Paste this first. Do not respond yet. Acknowledge with "Registry loaded ✓"

--- factories-registry-v{VERSION}.jsonl ---
{block}
--- END REGISTRY ---
"""


def build_paste_2(compact: bool = False) -> str:
    orch = ORCHESTRATOR_TEXT.strip()
    profile = SEED_PROFILE_TEXT.strip()
    if compact:
        orch = " ".join(orch.split())
        profile = " ".join(profile.split())
    return f"""SEED SYSTEM BOOTSTRAP - PASTE 2 of 3: SEED PROFILE + ORCHESTRATOR
Paste after registry. Do not respond yet. Acknowledge with "Orchestrator loaded ✓"

--- seed-profile-v3 ---
{profile}
--- END SEED PROFILE ---

--- orchestrator-v{VERSION} ---
{orch}
--- END ORCHESTRATOR ---
"""


def build_paste_3(compact: bool = False) -> str:
    strats = STRATEGIES_READABLE.strip()
    if compact:
        strats = "\n".join(" ".join(line.split()) for line in strats.splitlines())
    return f"""SEED SYSTEM BOOTSTRAP - PASTE 3 of 3: STRATEGY REGISTRY
Paste last. Respond with "Strategy registry loaded ✓ - all 3 components active. State your goal."

--- seed-prompting-strategies-v{STRAT_VERSION} ---
{strats}
--- END STRATEGIES ---
"""


def build_single_paste(registry_entries: list) -> str:
    reg_block = registry_to_jsonl_block(registry_entries)
    return f"""SEED SYSTEM BOOTSTRAP - SINGLE PASTE (large context 128k+)
Load all components in one message. Respond with "Seed System v{VERSION} ready. State your goal."

=== COMPONENT 1: REGISTRY (factories-registry-v{VERSION}.jsonl) ===
{reg_block}

=== COMPONENT 2: SEED PROFILE ===
{SEED_PROFILE_TEXT.strip()}

=== COMPONENT 3: ORCHESTRATOR v{VERSION} ===
{ORCHESTRATOR_TEXT.strip()}

=== COMPONENT 4: STRATEGIES (seed-prompting-strategies-v{STRAT_VERSION}) ===
{STRATEGIES_READABLE.strip()}

=== END BOOTSTRAP ===
"""


def build_api_json(registry_entries: list, strategy_entries: list) -> dict:
    return {
        "seed_system_version": VERSION,
        "strategy_registry_version": STRAT_VERSION,
        "generated": UPDATED,
        "components": {
            "registry": registry_entries,
            "seed_profile": SEED_PROFILE_TEXT.strip(),
            "orchestrator": ORCHESTRATOR_TEXT.strip(),
            "strategies_readable": STRATEGIES_READABLE.strip(),
            "strategies_jsonl": strategy_entries,
        },
        "paste_order": [
            "registry",
            "seed_profile + orchestrator",
            "strategies_readable",
        ],
        "quick_start_examples": [
            "Goal: I want to study Sentry tracing and breadcrumbs for my support role",
            "Goal: Create a 6-week DevOps learning roadmap",
            "Goal: Help me prep for a staff engineer behavioral interview",
            "Goal: Build a new factory for Kubernetes troubleshooting",
            "Goal: Best mechanical keyboard to buy under $150",
        ],
    }


def build_quickstart(target: str) -> str:
    paste_note = {
        "perplexity": "Paste all 3 blocks **in order** into a new Perplexity conversation.",
        "ollama":     "Paste all 3 blocks **in order** into your Ollama/LM Studio chat UI.",
        "single":     "Paste the **single combined block** into any 128k+ context model.",
        "api":        "Load `BOOTSTRAP-API.json` in your script. See `components` keys.",
    }.get(target, "Paste all 3 blocks in order.")

    return f"""# Seed System v{VERSION} - Bootstrap Quick Start
Generated: {UPDATED} | Target: {target}

## How to Use

{paste_note}

## After Bootstrap - Just Type Your Goal

```
Goal: [your goal here]
```

### Example Goals

```
Goal: I want to study Sentry tracing and breadcrumbs for my support role
Goal: Create a 6-week DevOps learning roadmap
Goal: Help me prep for a staff engineer behavioral interview
Goal: Build a new factory for Kubernetes troubleshooting
Goal: Best mechanical keyboard to buy under $150
Goal: Build a wealth plan for mid-career retirement catch-up
```

## What Happens

1. Orchestrator scores your goal against all factories using 4 signals
2. If confidence >=90%: auto-runs the best factory
3. If 75-89%: shows top match(es) and asks to confirm
4. Factory executes phases, then asks you to rate output 1-5
5. Score logged and fed back into factory avg_score over time

## Factories Available

| Factory | Type | Best For |
|---|---|---|
| shopping-builder | factory | Product research, buying decisions |
| strategy-builder | factory | Multi-week plans, roadmaps |
| interview-prep | factory | Mock interviews, prep, feedback |
| wealth-advisor-and-builder | factory | Boglehead wealth planning |
| sentry-support-tutor | factory | Sentry SDK/support study |
| technical-tutor-for-self-learning | meta-factory | Generate domain-specific tutors |
| factory-builder-v1 | meta-factory | Generate new factories |

## File Map

```
seed-system/
├── orchestrator-v3.3.py                 <- Python impl + all datatypes
├── factories-registry-v3.3.jsonl        <- registry (21 entries)
├── seed-prompting-strategies-v1.1.jsonl <- strategy data (13 entries)
├── seed-prompting-strategies-v1.1.md    <- strategy docs
├── orchestrator-v3.2-hybrid.md          <- manual Perplexity prompt (legacy)
├── orchestrator-match.sh                <- bash CLI
├── factory-builder-v1.md
├── factory-template-v1.1.md
├── seed-profile.md
├── seed-optimizer.md
└── role-specializer.md
```
"""


def main():
    parser = argparse.ArgumentParser(
        description=f"Seed System Bootstrap Generator v{VERSION}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--dir",    help="Path to seed-system directory (auto-detected if omitted)")
    parser.add_argument("--output", default="bootstrap-out", help="Output directory (default: bootstrap-out/)")
    parser.add_argument("--target", choices=["perplexity","ollama","single","api"], default="perplexity",
                        help="Bootstrap target format (default: perplexity)")
    parser.add_argument("--validate", action="store_true", help="Validate only, no files written")
    args = parser.parse_args()

    print(f"\n  Seed System Bootstrap Generator v{VERSION}")
    print(f"  Target: {args.target} | Output: {args.output}/\n")

    seed_dir = find_seed_dir(args.dir)
    registry_entries  = INLINE_REGISTRY
    strategy_entries  = INLINE_STRATEGIES

    if seed_dir:
        print(f"  Seed dir: {seed_dir}")
        reg_path = seed_dir / REGISTRY_FILENAME
        if not reg_path.exists():
            reg_path = seed_dir / "factories-registry.jsonl"
        if reg_path.exists():
            registry_entries = load_jsonl(reg_path)
            print(f"  Loaded registry: {reg_path.name} ({len(registry_entries)} entries)")
        else:
            print("  Registry file not found - using inline defaults")

        strat_path = seed_dir / STRATEGIES_FILENAME
        if not strat_path.exists():
            strat_path = seed_dir / "seed-prompting-strategies.jsonl"
        if strat_path.exists():
            strategy_entries = load_jsonl(strat_path)
            print(f"  Loaded strategies: {strat_path.name} ({len(strategy_entries)} entries)")
        else:
            print("  Strategies file not found - using inline defaults")
    else:
        print("  seed-system/ dir not found - using inline defaults")

    print("\n  Validating...")
    reg_ok = validate_registry(registry_entries)
    str_ok = validate_strategies([e for e in strategy_entries if "effectiveness" in e])
    print(f"  Registry: {'OK' if reg_ok else 'ISSUES FOUND'}")
    print(f"  Strategies: {'OK' if str_ok else 'ISSUES FOUND'}")

    if args.validate:
        print("\n  --validate only mode, no files written.\n")
        return

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    compact = args.target == "ollama"
    written = []

    if args.target in ("perplexity", "ollama"):
        for fname, content in {
            "BOOTSTRAP-PASTE-1-registry.md":    build_paste_1(registry_entries, compact),
            "BOOTSTRAP-PASTE-2-orchestrator.md": build_paste_2(compact),
            "BOOTSTRAP-PASTE-3-strategies.md":   build_paste_3(compact),
        }.items():
            p = out_dir / fname
            p.write_text(content)
            written.append(str(p))

    elif args.target == "single":
        p = out_dir / "BOOTSTRAP-SINGLE.md"
        p.write_text(build_single_paste(registry_entries))
        written.append(str(p))

    elif args.target == "api":
        p = out_dir / "BOOTSTRAP-API.json"
        p.write_text(json.dumps(build_api_json(registry_entries, strategy_entries), indent=2))
        written.append(str(p))

    for fname, content in {
        "BOOTSTRAP-QUICKSTART.md": build_quickstart(args.target),
        "CHANGELOG.md":            CHANGELOG_TEXT,
    }.items():
        p = out_dir / fname
        p.write_text(content)
        written.append(str(p))

    print(f"\n  Written {len(written)} files to {out_dir}/")
    for w in written:
        print(f"    {w}")

    steps = {
        "perplexity": "1. Paste PASTE-1 -> wait 'Registry loaded'\n  2. Paste PASTE-2 -> wait 'Orchestrator loaded'\n  3. Paste PASTE-3 -> wait 'Strategy registry loaded'\n  4. Type: Goal: [your goal]",
        "ollama":     "1. Paste PASTE-1 -> wait 'Registry loaded'\n  2. Paste PASTE-2 -> wait 'Orchestrator loaded'\n  3. Paste PASTE-3 -> wait 'Strategy registry loaded'\n  4. Type: Goal: [your goal]",
        "single":     "1. Paste BOOTSTRAP-SINGLE.md into 128k+ context model\n  2. Wait for 'Seed System v3.3 ready'\n  3. Type: Goal: [your goal]",
        "api":        "1. Load BOOTSTRAP-API.json\n  2. POST components['seed_profile'] + components['orchestrator'] as system message\n  3. POST components['registry'] as first user message\n  4. POST components['strategies_readable'] as second user message\n  5. Send Goal: messages",
    }
    print(f"\n  Next steps ({args.target}):\n  {steps.get(args.target, '')}\n")


if __name__ == "__main__":
    main()
