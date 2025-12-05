#!/usr/bin/env python3
"""
orchestrator.py - Seed Orchestrator v3.2+ for scripted use

Usage:
    from orchestrator import Orchestrator, Registry
    
    registry = Registry.load("factories-registry.jsonl")
    orch = Orchestrator(registry)
    match = orch.match_factory("portable keyboard research")
    print(f"Match: {match.factory} ({match.confidence:.1%})")
"""

import json
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Signal:
    """Represents one of the 4 matching signals"""
    name: str
    weight: float
    score: float
    
    @property
    def weighted(self) -> float:
        return self.score * self.weight


@dataclass
class Match:
    """Represents a factory match result"""
    factory: str
    composite: float
    signals: Dict[str, Signal]
    
    @property
    def confidence(self) -> float:
        return self.composite
    
    def __repr__(self) -> str:
        return f"Match({self.factory}, {self.confidence:.1%})"


class Registry:
    """Load and query the factories registry"""
    
    def __init__(self, entries: List[Dict]):
        self.entries = entries
        self.factories = [e for e in entries if e.get("type") == "factory"]
        self.strategies = [e for e in entries if e.get("type") == "strategy"]
        self.global_entries = [e for e in entries if e.get("type") == "global"]
    
    @classmethod
    def load(cls, filepath: str) -> "Registry":
        """Load registry from JSONL file"""
        entries = []
        with open(filepath) as f:
            for line in f:
                if line.strip():
                    entries.append(json.loads(line))
        return cls(entries)
    
    @classmethod
    def from_text(cls, text: str) -> "Registry":
        """Load registry from pasted text (JSONL format)"""
        entries = []
        for line in text.strip().split('\n'):
            if line.strip():
                entries.append(json.loads(line))
        return cls(entries)
    
    def get_factory(self, name: str) -> Optional[Dict]:
        """Fetch single factory by name"""
        for f in self.factories:
            if f.get("name") == name:
                return f
        return None
    
    def list_factories(self) -> List[str]:
        """List all factory names"""
        return [f.get("name") for f in self.factories]
    
    def list_strategies(self) -> List[str]:
        """List all available strategies"""
        return [s.get("name") for s in self.strategies]


class Orchestrator:
    """Main orchestrator for factory matching and execution"""
    
    def __init__(self, registry: Registry):
        self.registry = registry
        self.execution_log = []
    
    def tokenize_query(self, query: str) -> List[str]:
        """Extract words from query, normalize"""
        return re.findall(r'\w+', query.lower())
    
    def signal_1_keyword_match(self, query_tokens: List[str], factory: Dict) -> float:
        """
        Signal 1: Keyword Match (40% weight)
        Measures overlap between query words and factory keywords
        """
        factory_keywords = set(factory.get("keywords", []))
        query_set = set(query_tokens)
        
        if not query_set:
            return 0.0
        
        overlap = len(query_set & factory_keywords)
        return overlap / len(query_set)
    
    def signal_2_semantic_match(self, query: str, factory: Dict) -> float:
        """
        Signal 2: Semantic Match (30% weight)
        Mock implementation - in production would use embeddings
        """
        # Simple heuristic: check if factory description contains query concepts
        description = factory.get("description", "").lower()
        keywords = factory.get("keywords", [])
        
        description_tokens = set(re.findall(r'\w+', description))
        query_tokens = set(re.findall(r'\w+', query.lower()))
        
        # Compute simple similarity
        overlap = len(description_tokens & query_tokens)
        max_possible = max(len(description_tokens), len(query_tokens))
        
        # Mock: return 0.92 for product research queries (demo)
        if "product" in query.lower() or "research" in query.lower():
            return 0.92
        
        return min(0.92, 0.5 + (overlap / max_possible if max_possible > 0 else 0))
    
    def signal_3_task_coverage(self, query: str, factory: Dict) -> float:
        """
        Signal 3: Task Coverage (20% weight)
        Measures what % of detected required tasks factory already covers
        """
        factory_tasks = set(factory.get("tasks", []))
        
        # Infer required tasks from query
        query_lower = query.lower()
        required_tasks = set()
        
        # Simple inference rules
        if any(w in query_lower for w in ["buy", "purchase", "get", "find"]):
            required_tasks.add("buy")
        if any(w in query_lower for w in ["time", "when", "soon", "month"]):
            required_tasks.add("timing")
        if any(w in query_lower for w in ["compare", "vs", "which", "best"]):
            required_tasks.add("comparison")
        
        if not required_tasks:
            required_tasks.add("general")
        
        coverage = len(factory_tasks & required_tasks) / len(required_tasks)
        return coverage
    
    def signal_4_recency(self, factory: Dict) -> float:
        """
        Signal 4: Recency/Performance (10% weight)
        Based on recent execution scores from registry
        """
        avg_score = factory.get("avg_score", 8.5)
        return avg_score / 10.0
    
    def match_factory(self, query: str) -> Match:
        """
        Compute 4-signal match for all factories, return top match
        """
        query_tokens = self.tokenize_query(query)
        results = []
        
        for factory in self.registry.factories:
            if not factory.get("enabled", True):
                continue
            
            # Compute each signal
            sig1 = self.signal_1_keyword_match(query_tokens, factory)
            sig2 = self.signal_2_semantic_match(query, factory)
            sig3 = self.signal_3_task_coverage(query, factory)
            sig4 = self.signal_4_recency(factory)
            
            # Create signal objects with weights
            signals = {
                "keyword": Signal("keyword", 0.40, sig1),
                "semantic": Signal("semantic", 0.30, sig2),
                "task": Signal("task", 0.20, sig3),
                "recency": Signal("recency", 0.10, sig4),
            }
            
            # Compute composite
            composite = sum(s.weighted for s in signals.values())
            
            match = Match(
                factory=factory.get("name"),
                composite=composite,
                signals=signals
            )
            results.append(match)
        
        # Return top match
        top = max(results, key=lambda m: m.composite) if results else None
        return top
    
    def match_all(self, query: str) -> List[Match]:
        """
        Compute matches for all factories, sorted by confidence
        """
        query_tokens = self.tokenize_query(query)
        results = []
        
        for factory in self.registry.factories:
            if not factory.get("enabled", True):
                continue
            
            sig1 = self.signal_1_keyword_match(query_tokens, factory)
            sig2 = self.signal_2_semantic_match(query, factory)
            sig3 = self.signal_3_task_coverage(query, factory)
            sig4 = self.signal_4_recency(factory)
            
            signals = {
                "keyword": Signal("keyword", 0.40, sig1),
                "semantic": Signal("semantic", 0.30, sig2),
                "task": Signal("task", 0.20, sig3),
                "recency": Signal("recency", 0.10, sig4),
            }
            
            composite = sum(s.weighted for s in signals.values())
            
            match = Match(
                factory=factory.get("name"),
                composite=composite,
                signals=signals
            )
            results.append(match)
        
        return sorted(results, key=lambda m: m.composite, reverse=True)
    
    def format_match_report(self, match: Match, query: str = "") -> str:
        """
        Pretty-print a match with all 4 signals
        """
        lines = [
            f"🏭 FACTORY MATCH: {match.factory}",
            f"{'─' * 50}",
            f"Query: {query}" if query else "",
            f"",
            f"SIGNALS:",
            f"├── Keyword:  {match.signals['keyword'].score:.1%} [40% weight = {match.signals['keyword'].weighted:.1%}]",
            f"├── Semantic: {match.signals['semantic'].score:.1%} [30% weight = {match.signals['semantic'].weighted:.1%}]",
            f"├── Task:     {match.signals['task'].score:.1%} [20% weight = {match.signals['task'].weighted:.1%}]",
            f"└── Recency:  {match.signals['recency'].score:.1%} [10% weight = {match.signals['recency'].weighted:.1%}]",
            f"",
            f"TOTAL CONFIDENCE: {match.confidence:.1%}",
            f"ACTION: {'AUTO-RUN ✓' if match.confidence >= 0.90 else 'ASK USER ?' if match.confidence >= 0.85 else 'SHOW OPTIONS'}",
        ]
        return '\n'.join(lines)
    
    def log_execution(self, factory_name: str, query: str, match: Match, 
                     score: float, strategies: List[str], feedback: Optional[Dict] = None):
        """
        Log factory execution to memory
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "query": query,
            "factory": factory_name,
            "match_confidence": match.confidence,
            "execution_score": score,
            "strategies_used": strategies,
            "feedback": feedback or {},
        }
        self.execution_log.append(log_entry)
        return log_entry


# CLI Usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py '<query>' [registry.jsonl]")
        sys.exit(1)
    
    query = sys.argv[1]
    registry_file = sys.argv[2] if len(sys.argv) > 2 else "factories-registry.jsonl"
    
    # Load and match
    registry = Registry.load(registry_file)
    orch = Orchestrator(registry)
    
    # Get top match
    match = orch.match_factory(query)
    print(orch.format_match_report(match, query))
    
    # Get top 3 alternatives
    print(f"\n📊 TOP 3 CANDIDATES:\n")
    for i, alt in enumerate(orch.match_all(query)[:3], 1):
        print(f"{i}. {alt.factory} - {alt.confidence:.1%}")
