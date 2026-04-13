#!/usr/bin/env python3
"""orchestrator.py - Seed Orchestrator v3.3 for scripted use

Usage:
    from orchestrator import Orchestrator, Registry

    registry = Registry.load("factories-registry.jsonl")
    orch = Orchestrator(registry)
    match = orch.match_factory("portable keyboard research")
    print(f"Match: {match.factory} ({match.confidence:.1%})")

    # Load strategies separately
    strategies = StrategyRegistry.load("seed-prompting-strategies.jsonl")
    allowed = strategies.filter_by_use_case("product research")
"""

import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# Datatypes
# ---------------------------------------------------------------------------


@dataclass
class Signal:
    """Represents one of the 4 matching signals used for factory scoring."""

    name: str
    weight: float
    score: float

    @property
    def weighted(self) -> float:
        return self.score * self.weight


@dataclass
class Match:
    """Represents a factory match result from the 4-signal algorithm."""

    factory: str
    composite: float
    signals: Dict[str, Signal]

    @property
    def confidence(self) -> float:
        return self.composite

    def __repr__(self) -> str:
        return f"Match({self.factory}, {self.confidence:.1%})"


@dataclass
class StrategyEntry:
    """A single strategy from seed-prompting-strategies.jsonl.

    Mirrors the JSONL schema so factories can load, filter, and reference
    strategies dynamically rather than hard-coding them.
    """

    name: str
    version: str
    enabled: bool
    description: str
    implementation: str
    effectiveness: float
    best_for: List[str]
    requires_multiple_runs: bool
    computational_cost: str  # "low" | "medium" | "high"
    model_compatibility: List[str]
    added: str
    updated: str
    research_ref: str
    tags: List[str]

    @classmethod
    def from_dict(cls, d: Dict) -> "StrategyEntry":
        return cls(
            name=d.get("name", ""),
            version=d.get("version", "1.0"),
            enabled=d.get("enabled", True),
            description=d.get("description", ""),
            implementation=d.get("implementation", ""),
            effectiveness=float(d.get("effectiveness", 0.0)),
            best_for=d.get("best_for", []),
            requires_multiple_runs=d.get("requires_multiple_runs", False),
            computational_cost=d.get("computational_cost", "low"),
            model_compatibility=d.get("model_compatibility", []),
            added=d.get("added", ""),
            updated=d.get("updated", ""),
            research_ref=d.get("research_ref", ""),
            tags=d.get("tags", []),
        )

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "version": self.version,
            "enabled": self.enabled,
            "description": self.description,
            "implementation": self.implementation,
            "effectiveness": self.effectiveness,
            "best_for": self.best_for,
            "requires_multiple_runs": self.requires_multiple_runs,
            "computational_cost": self.computational_cost,
            "model_compatibility": self.model_compatibility,
            "added": self.added,
            "updated": self.updated,
            "research_ref": self.research_ref,
            "tags": self.tags,
        }


@dataclass
class FactoryEntry:
    """A single factory entry from factories-registry.jsonl.

    Provides typed access to registry metadata. Orchestrator uses this
    when computing signals and selecting factories.
    """

    name: str
    version: str
    type: str
    description: str
    enabled: bool
    parent: Optional[str] = None
    tasks: List[str] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    rubric: Dict[str, float] = field(default_factory=dict)
    strategies: List[str] = field(default_factory=list)
    recent_scores: List[float] = field(default_factory=list)
    avg_score: float = 8.5
    last_updated: str = ""
    effectiveness: Optional[float] = None
    best_for: List[str] = field(default_factory=list)
    generates: Optional[str] = None
    # Council judging — ordered list of preferred models
    preferred_judge_models: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: Dict) -> "FactoryEntry":
        return cls(
            name=d.get("name", ""),
            version=str(d.get("version", "1.0")),
            type=d.get("type", "factory"),
            description=d.get("description", ""),
            enabled=d.get("enabled", True),
            parent=d.get("parent"),
            tasks=d.get("tasks", []),
            keywords=d.get("keywords", []),
            rubric=d.get("rubric", {}),
            strategies=d.get("strategies", []),
            recent_scores=d.get("recent_scores", []),
            avg_score=float(d.get("avg_score", 8.5)),
            last_updated=d.get("last_updated", ""),
            effectiveness=d.get("effectiveness"),
            best_for=d.get("best_for", []),
            generates=d.get("generates"),
            preferred_judge_models=d.get("preferred_judge_models", []),
        )

    def to_dict(self) -> Dict:
        d: Dict = {
            "name": self.name,
            "version": self.version,
            "type": self.type,
            "description": self.description,
            "enabled": self.enabled,
            "last_updated": self.last_updated,
        }
        if self.parent is not None:
            d["parent"] = self.parent
        if self.tasks:
            d["tasks"] = self.tasks
        if self.keywords:
            d["keywords"] = self.keywords
        if self.rubric:
            d["rubric"] = self.rubric
        if self.strategies:
            d["strategies"] = self.strategies
        if self.recent_scores:
            d["recent_scores"] = self.recent_scores
            d["avg_score"] = self.avg_score
        if self.effectiveness is not None:
            d["effectiveness"] = self.effectiveness
        if self.best_for:
            d["best_for"] = self.best_for
        if self.generates:
            d["generates"] = self.generates
        if self.preferred_judge_models:
            d["preferred_judge_models"] = self.preferred_judge_models
        return d


@dataclass
class ExecutionLog:
    """A single execution log record written back after a factory run."""

    timestamp: str
    query: str
    factory: str
    match_confidence: float
    execution_score: float
    strategies_used: List[str]
    feedback: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return {
            "timestamp": self.timestamp,
            "query": self.query,
            "factory": self.factory,
            "match_confidence": self.match_confidence,
            "execution_score": self.execution_score,
            "strategies_used": self.strategies_used,
            "feedback": self.feedback,
        }


# ---------------------------------------------------------------------------
# StrategyRegistry
# ---------------------------------------------------------------------------


class StrategyRegistry:
    """Load and query seed-prompting-strategies.jsonl."""

    def __init__(self, entries: List[StrategyEntry]):
        self._entries = entries

    @classmethod
    def load(cls, filepath: str) -> "StrategyRegistry":
        entries: List[StrategyEntry] = []
        with open(filepath) as f:
            for line in f:
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                try:
                    entries.append(StrategyEntry.from_dict(json.loads(stripped)))
                except json.JSONDecodeError:
                    pass
        return cls(entries)

    @classmethod
    def from_text(cls, text: str) -> "StrategyRegistry":
        entries: List[StrategyEntry] = []
        for line in text.strip().split("\n"):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                entries.append(StrategyEntry.from_dict(json.loads(stripped)))
            except json.JSONDecodeError:
                pass
        return cls(entries)

    @property
    def all(self) -> List[StrategyEntry]:
        return self._entries

    @property
    def enabled(self) -> List[StrategyEntry]:
        return [s for s in self._entries if s.enabled]

    def get(self, name: str) -> Optional[StrategyEntry]:
        for s in self._entries:
            if s.name == name:
                return s
        return None

    def filter_by_use_case(self, use_case: str) -> List[StrategyEntry]:
        uc = use_case.lower()
        return [s for s in self.enabled if any(uc in bf.lower() for bf in s.best_for)]

    def filter_by_tag(self, tag: str) -> List[StrategyEntry]:
        return [s for s in self.enabled if tag.lower() in [t.lower() for t in s.tags]]

    def filter_by_cost(self, max_cost: str) -> List[StrategyEntry]:
        order = {"low": 0, "medium": 1, "high": 2}
        ceiling = order.get(max_cost.lower(), 2)
        return [s for s in self.enabled if order.get(s.computational_cost.lower(), 0) <= ceiling]

    def top_by_effectiveness(self, n: int = 5) -> List[StrategyEntry]:
        return sorted(self.enabled, key=lambda s: s.effectiveness, reverse=True)[:n]

    def for_factory(self, allowed: List[str]) -> List[StrategyEntry]:
        return [s for name in allowed for s in [self.get(name)] if s is not None]

    def names(self) -> List[str]:
        return [s.name for s in self.enabled]

    def append(self, strategy: StrategyEntry, filepath: Optional[str] = None) -> None:
        self._entries.append(strategy)
        if filepath:
            with open(filepath, "a") as f:
                f.write(json.dumps(strategy.to_dict()) + "\n")


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


class Registry:
    """Load and query factories-registry.jsonl."""

    def __init__(self, entries: List[Dict]):
        self._raw = entries
        self.factory_entries: List[FactoryEntry] = [
            FactoryEntry.from_dict(e)
            for e in entries
            if e.get("type")
            in (
                "factory",
                "meta-factory",
                "template",
                "global",
                "orchestrator",
                "optimizer",
                "specializer",
            )
        ]
        self.inline_strategies: List[Dict] = [e for e in entries if e.get("type") == "strategy"]

    @property
    def factories(self) -> List[FactoryEntry]:
        return [e for e in self.factory_entries if e.type in ("factory", "meta-factory")]

    @property
    def enabled_factories(self) -> List[FactoryEntry]:
        return [f for f in self.factories if f.enabled]

    @classmethod
    def load(cls, filepath: str) -> "Registry":
        entries: List[Dict] = []
        with open(filepath) as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    try:
                        entries.append(json.loads(stripped))
                    except json.JSONDecodeError:
                        pass
        return cls(entries)

    @classmethod
    def from_text(cls, text: str) -> "Registry":
        entries: List[Dict] = []
        for line in text.strip().split("\n"):
            stripped = line.strip()
            if stripped:
                try:
                    entries.append(json.loads(stripped))
                except json.JSONDecodeError:
                    pass
        return cls(entries)

    def get_factory(self, name: str) -> Optional[FactoryEntry]:
        for f in self.factory_entries:
            if f.name == name:
                return f
        return None

    def list_factories(self) -> List[str]:
        return [f.name for f in self.enabled_factories]

    def list_strategies(self) -> List[str]:
        return [s.get("name", "") for s in self.inline_strategies]

    def update_scores(
        self, factory_name: str, new_score: float, filepath: Optional[str] = None
    ) -> None:
        entry = self.get_factory(factory_name)
        if entry is None:
            return
        entry.recent_scores.append(new_score)
        if len(entry.recent_scores) > 10:
            entry.recent_scores = entry.recent_scores[-10:]
        entry.avg_score = round(sum(entry.recent_scores) / len(entry.recent_scores), 2)
        if filepath:
            self._write(filepath)

    def _write(self, filepath: str) -> None:
        with open(filepath, "w") as f:
            for entry in self.factory_entries:
                f.write(json.dumps(entry.to_dict()) + "\n")
            for s in self.inline_strategies:
                f.write(json.dumps(s) + "\n")


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


class Orchestrator:
    """Main orchestrator: 4-signal factory matching and execution logging."""

    WEIGHTS = {
        "keyword": 0.40,
        "semantic": 0.30,
        "task": 0.20,
        "recency": 0.10,
    }

    AUTO_RUN = 0.90
    ASK_USER = 0.85
    SHOW_THREE = 0.75

    def __init__(self, registry: Registry, strategy_registry: Optional[StrategyRegistry] = None):
        self.registry = registry
        self.strategy_registry = strategy_registry
        self.execution_log: List[ExecutionLog] = []

    def tokenize_query(self, query: str) -> List[str]:
        return re.findall(r"\w+", query.lower())

    def signal_1_keyword_match(self, query_tokens: List[str], factory: FactoryEntry) -> float:
        factory_keywords = set(factory.keywords)
        query_set = set(query_tokens)
        if not query_set:
            return 0.0
        overlap = len(query_set & factory_keywords)
        return overlap / len(query_set)

    def signal_2_semantic_match(self, query: str, factory: FactoryEntry) -> float:
        description_tokens = set(re.findall(r"\w+", factory.description.lower()))
        keyword_tokens = {k.lower() for k in factory.keywords}
        task_tokens = {t.lower() for t in factory.tasks}
        combined = description_tokens | keyword_tokens | task_tokens
        query_tokens = set(re.findall(r"\w+", query.lower()))

        overlap = len(combined & query_tokens)
        max_possible = max(len(combined), len(query_tokens), 1)
        base = min(0.60, overlap / max_possible + 0.30)

        domain_rules = [
            (
                [
                    "buy",
                    "purchase",
                    "keyboard",
                    "headphone",
                    "monitor",
                    "laptop",
                    "product",
                    "deal",
                ],
                ["buy", "timing", "deal_hunting", "comparison"],
                0.50,
            ),
            (
                ["interview", "mock", "behavioral", "leet", "prep", "practice"],
                ["interview", "mock", "prep", "feedback"],
                0.55,
            ),
            (
                ["plan", "roadmap", "strategy", "phase", "timeline", "week"],
                ["planning", "roadmap", "multi-week", "decomposition"],
                0.45,
            ),
            (
                ["sentry", "sdk", "dsn", "tracing", "breadcrumb", "issue", "event", "escalat"],
                ["co_pilot", "failure_review", "study_session", "triage"],
                0.60,
            ),
            (
                ["wealth", "retire", "boglehead", "swr", "runway", "invest", "saving"],
                ["wealth", "catchup", "swr", "runway", "boglehead"],
                0.55,
            ),
            (
                ["factory", "generate", "create", "meta", "new factory"],
                ["factory_generation", "factory_refactoring"],
                0.50,
            ),
            (
                ["tutor", "learn", "study", "mastery", "mentor", "self-learning"],
                ["tutor_deployment", "study_plan_design", "learner_profiling"],
                0.50,
            ),
        ]

        q = query.lower()
        factory_task_set = set(factory.tasks)
        for query_triggers, factory_task_signals, boost in domain_rules:
            if any(t in q for t in query_triggers) and bool(
                factory_task_set & set(factory_task_signals)
            ):
                return min(1.0, base + boost)

        return base

    def signal_3_task_coverage(self, query: str, factory: FactoryEntry) -> float:
        factory_tasks = set(factory.tasks)
        query_lower = query.lower()
        required: set = set()

        task_inference = {
            "buy": ["buy", "purchase", "get", "acquire"],
            "timing": ["when", "time", "soon", "month", "year"],
            "comparison": ["compare", "vs", "versus", "which", "best", "difference"],
            "planning": ["plan", "roadmap", "phase", "week", "timeline"],
            "interview": ["interview", "mock", "prep", "behavioral", "technical"],
            "study": ["study", "learn", "understand", "practice", "tutor"],
            "study_session": ["study", "learn", "session", "understand", "practice"],
            "co_pilot": [
                "help",
                "debug",
                "triage",
                "ticket",
                "escalate",
                "tracing",
                "breadcrumb",
                "dsn",
                "sdk",
                "sentry",
            ],
            "failure_review": ["failure", "review", "incident", "postmortem", "rca"],
            "pattern_tracking": ["pattern", "track", "recurring", "log", "trend"],
            "wealth": ["wealth", "retire", "invest", "savings", "boglehead"],
            "factory_generation": ["factory", "create", "generate", "new factory"],
        }

        for task, triggers in task_inference.items():
            if any(t in query_lower for t in triggers):
                required.add(task)

        if not required:
            required.add("general")

        covered = len(factory_tasks & required)
        return covered / len(required)

    def signal_4_recency(self, factory: FactoryEntry) -> float:
        return factory.avg_score / 10.0

    def _compute_match(self, query: str, query_tokens: List[str], factory: FactoryEntry) -> Match:
        s1 = self.signal_1_keyword_match(query_tokens, factory)
        s2 = self.signal_2_semantic_match(query, factory)
        s3 = self.signal_3_task_coverage(query, factory)
        s4 = self.signal_4_recency(factory)
        signals = {
            "keyword": Signal("keyword", self.WEIGHTS["keyword"], s1),
            "semantic": Signal("semantic", self.WEIGHTS["semantic"], s2),
            "task": Signal("task", self.WEIGHTS["task"], s3),
            "recency": Signal("recency", self.WEIGHTS["recency"], s4),
        }
        composite = sum(s.weighted for s in signals.values())
        return Match(factory=factory.name, composite=composite, signals=signals)

    def match_factory(self, query: str) -> Optional[Match]:
        query_tokens = self.tokenize_query(query)
        results = [
            self._compute_match(query, query_tokens, f) for f in self.registry.enabled_factories
        ]
        return max(results, key=lambda m: m.composite) if results else None

    def match_all(self, query: str) -> List[Match]:
        query_tokens = self.tokenize_query(query)
        results = [
            self._compute_match(query, query_tokens, f) for f in self.registry.enabled_factories
        ]
        return sorted(results, key=lambda m: m.composite, reverse=True)

    def decide(self, match: Match) -> str:
        c = match.confidence
        if c >= self.AUTO_RUN:
            return "AUTO-RUN ✓"
        if c >= self.ASK_USER:
            return "ASK USER? (default: yes)"
        if c >= self.SHOW_THREE:
            return "SHOW TOP 3 — ask user to pick"
        return "LOW CONFIDENCE — suggest new factory"

    def select_strategies(
        self,
        factory: FactoryEntry,
        allowed: Optional[List[str]] = None,
        feedback_history: Optional[List[Dict]] = None,
        max_cost: str = "high",
        multi_model_available: bool = False,
    ) -> List[StrategyEntry]:
        """Phase 0 helper: return ordered StrategyEntry list for a factory.

        Priority:
        1. Respect `allowed` list from orchestrator input (if provided)
        2. Fall back to factory.strategies from registry
        3. Filter by computational cost
        4. Inject council strategies for meta/recursive factories
        5. Boost strategies with high feedback ratings
        """
        if self.strategy_registry is None:
            return []

        candidate_names = allowed if allowed else factory.strategies
        candidates = self.strategy_registry.for_factory(candidate_names)

        order = {"low": 0, "medium": 1, "high": 2}
        ceiling = order.get(max_cost.lower(), 2)
        candidates = [
            s for s in candidates if order.get(s.computational_cost.lower(), 0) <= ceiling
        ]

        # Council injection for meta/recursive factories
        is_meta = factory.type in ("meta-factory",) or "factory_generation" in factory.tasks
        existing_names = {c.name for c in candidates}
        if is_meta:
            if multi_model_available:
                for cname in ("Model-Council-Generate", "Model-Council-Judge"):
                    s = self.strategy_registry.get(cname)
                    if s and s.name not in existing_names:
                        candidates.insert(0, s)
                        existing_names.add(s.name)
            else:
                more = self.strategy_registry.get("Mixture-of-Roles")
                if more and more.name not in existing_names:
                    candidates.insert(0, more)

        if feedback_history:
            high_rated = {
                item["strategy"]
                for item in feedback_history
                if item.get("rating", 0) >= 4 and "strategy" in item
            }
            candidates.sort(key=lambda s: (s.name in high_rated, s.effectiveness), reverse=True)

        return candidates

    def format_match_report(self, match: Match, query: str = "") -> str:
        sigs = match.signals
        lines = [
            f"🏭 FACTORY MATCH: {match.factory}",
            "─" * 52,
            f"Query: {query}" if query else "",
            "",
            "SIGNALS:",
            f"├── Keyword:  {sigs['keyword'].score:.1%}  [×{sigs['keyword'].weight:.0%} = {sigs['keyword'].weighted:.1%}]",
            f"├── Semantic: {sigs['semantic'].score:.1%}  [×{sigs['semantic'].weight:.0%} = {sigs['semantic'].weighted:.1%}]",
            f"├── Task:     {sigs['task'].score:.1%}  [×{sigs['task'].weight:.0%} = {sigs['task'].weighted:.1%}]",
            f"└── Recency:  {sigs['recency'].score:.1%}  [×{sigs['recency'].weight:.0%} = {sigs['recency'].weighted:.1%}]",
            "",
            f"TOTAL CONFIDENCE: {match.confidence:.1%}",
            f"ACTION: {self.decide(match)}",
        ]
        return "\n".join(line for line in lines if line is not None)

    def log_execution(
        self,
        factory_name: str,
        query: str,
        match: Match,
        score: float,
        strategies: List[str],
        feedback: Optional[Dict] = None,
    ) -> ExecutionLog:
        log = ExecutionLog(
            timestamp=datetime.utcnow().isoformat(),
            query=query,
            factory=factory_name,
            match_confidence=match.confidence,
            execution_score=score,
            strategies_used=strategies,
            feedback=feedback or {},
        )
        self.execution_log.append(log)
        return log

    def dump_log(self, filepath: str) -> None:
        with open(filepath, "a") as f:
            for log in self.execution_log:
                f.write(json.dumps(log.to_dict()) + "\n")
        self.execution_log.clear()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py '<query>' [registry.jsonl] [strategies.jsonl]")
        sys.exit(1)

    query = sys.argv[1]
    registry_file = sys.argv[2] if len(sys.argv) > 2 else "factories-registry.jsonl"
    strategies_file = sys.argv[3] if len(sys.argv) > 3 else "seed-prompting-strategies.jsonl"

    registry = Registry.load(registry_file)

    strategy_registry: Optional[StrategyRegistry] = None
    if Path(strategies_file).exists():
        strategy_registry = StrategyRegistry.load(strategies_file)

    orch = Orchestrator(registry, strategy_registry)
    match = orch.match_factory(query)
    if match is None:
        print("No factories found in registry.")
        sys.exit(1)

    print(orch.format_match_report(match, query))

    print("\n📊 TOP 3 CANDIDATES:\n")
    for i, alt in enumerate(orch.match_all(query)[:3], 1):
        print(f"  {i}. {alt.factory} — {alt.confidence:.1%}")

    if strategy_registry:
        factory_entry = registry.get_factory(match.factory)
        if factory_entry:
            selected = orch.select_strategies(factory_entry)
            if selected:
                print("\n🧠 SUGGESTED STRATEGIES (Phase 0):\n")
                for s in selected:
                    print(
                        f"  • {s.name} (effectiveness={s.effectiveness:.0%}, cost={s.computational_cost})"
                    )
