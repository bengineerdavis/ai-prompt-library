# Seed Orchestrator v3.2+ - Quick Reference Card

## Download These 5 Files

```
✓ factories-registry.jsonl        (JSONL registry - 3KB)
✓ orchestrator-v3.2-hybrid.md     (Perplexity prompt - 380 lines)
✓ orchestrator.py                 (Python impl - 400 lines)
✓ orchestrator-match.sh           (Bash script - 80 lines)
✓ SETUP_GUIDE.md                  (Documentation)
```

---

## Three Ways to Use

### 1️⃣ Perplexity Chat (No Coding)

```
Paste 1: factories-registry.jsonl
Paste 2: orchestrator-v3.2-hybrid.md
Type:    "Goal: Find best portable keyboard"
Result:  Orchestrator suggests factory → Paste that factory → Get output
```

### 2️⃣ Python Script

```python
from orchestrator import Orchestrator, Registry

registry = Registry.load("factories-registry.jsonl")
orch = Orchestrator(registry)
match = orch.match_factory("portable keyboard")
print(f"Match: {match.factory} ({match.confidence:.1%})")
```

### 3️⃣ Bash Command

```bash
./orchestrator-match.sh "portable keyboard" factories-registry.jsonl
# Returns JSON with match details
```

---

## Registry Format (Each Line is JSON)

```json
{
  "name": "shopping-builder",
  "type": "factory",
  "description": "Product research",
  "tasks": ["buy", "timing"],
  "keywords": ["product", "shopping"],
  "strategies": ["Few-Shot", "Meta-Prompting"],
  "avg_score": 8.98
}
```

---

## 4-Signal Matching Algorithm

```
Composite Score = (Keyword×0.40) + (Semantic×0.30) + (Task×0.20) + (Recency×0.10)

Signal 1: Keyword Match (40%)
  → Word overlap between query and factory keywords

Signal 2: Semantic Match (30%)
  → Conceptual alignment (product research, planning, etc.)

Signal 3: Task Coverage (20%)
  → What % of required tasks factory can handle

Signal 4: Recency Score (10%)
  → Recent performance (avg of last 5 scores)

Decision Threshold:
  ≥90% → AUTO-RUN (confident)
  85-89% → Ask user (default yes)
  75-84% → Show top 3, pick one
  <75% → Suggest new factory
```

---

## Common Commands

### Python

```python
# Load registry
from orchestrator import Registry
registry = Registry.load("factories-registry.jsonl")

# Create orchestrator
from orchestrator import Orchestrator
orch = Orchestrator(registry)

# Match query
match = orch.match_factory("your query")

# Get alternatives
for alt in orch.match_all("query")[:3]:
    print(f"{alt.factory}: {alt.confidence:.1%}")

# Format report
print(orch.format_match_report(match, "your query"))

# Log execution
orch.log_execution("factory-name", "query", match, 8.8, ["Few-Shot"])
```

### Bash

```bash
# Quick match
./orchestrator-match.sh "query" factories-registry.jsonl

# Get top factory
./orchestrator-match.sh "query" factories-registry.jsonl \
  | jq -r '.top_match.factory'

# Get confidence
./orchestrator-match.sh "query" factories-registry.jsonl \
  | jq '.top_match.composite'

# List all factories
jq 'select(.type == "factory") | .name' factories-registry.jsonl

# Query registry
jq 'select(.name == "shopping-builder")' factories-registry.jsonl
```

---

## File Dependencies

```
For Perplexity:
  └─ factories-registry.jsonl
  └─ orchestrator-v3.2-hybrid.md

For Python:
  ├─ orchestrator.py (import)
  └─ factories-registry.jsonl (load)

For Bash:
  ├─ orchestrator-match.sh (run)
  └─ factories-registry.jsonl (reference)
```

---

## Adding New Factories

```bash
# Append to registry
echo '{"name":"your-factory","type":"factory","description":"...","tasks":["task1"],"keywords":["word"],"strategies":["Few-Shot"],"avg_score":8.5}' >> factories-registry.jsonl
```

---

## Workflow Examples

### Example 1: Find Best Keyboard

**In Perplexity:**
```
Paste: factories-registry.jsonl + orchestrator-v3.2-hybrid.md

Goal: Best portable keyboard under 1.5 lbs for travel
Baseline: Keychron Q2 Max with tactile switches
Constraint: Lightweight but good typing feel

Orchestrator Output:
  🏭 TOP MATCH: shopping-builder (87%)
  
  Signals:
  ├── Keyword: 35% (buy, comparison, travel)
  ├── Semantic: 92% (product selection research)
  ├── Task: 67% (2/3 match)
  └── Recency: 89% (8.98/10 recent scores)
  
  Paste shopping-builder.md to proceed?
```

### Example 2: Batch Process Queries

**Python script:**
```python
from orchestrator import Orchestrator, Registry

registry = Registry.load("factories-registry.jsonl")
orch = Orchestrator(registry)

queries = [
    "best portable keyboard",
    "30-week career plan",
    "interview prep",
]

for q in queries:
    match = orch.match_factory(q)
    print(f"{q:30} → {match.factory:20} ({match.confidence:.1%})")
```

**Output:**
```
best portable keyboard         → shopping-builder         (87%)
30-week career plan           → strategy-builder         (91%)
interview prep                → interview-prep           (88%)
```

### Example 3: Check Registry Health

```bash
# Count factories
jq 'select(.type == "factory")' factories-registry.jsonl | wc -l

# Find low-performing factories
jq 'select(.type == "factory" and .avg_score < 8.0)' factories-registry.jsonl

# List all strategies
jq 'select(.type == "strategy") | .name' factories-registry.jsonl
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Python ImportError | Check both .py and .jsonl in same dir |
| Registry not found | `ls factories-registry.jsonl` |
| Invalid JSON error | `python3 -m json.tool < factories-registry.jsonl` |
| Bash permission denied | `chmod +x orchestrator-match.sh` |
| Perplexity paste error | Paste registry FIRST, then orchestrator |

---

## Testing

```bash
# Python test
python3 -c "from orchestrator import Orchestrator, Registry; r = Registry.load('factories-registry.jsonl'); o = Orchestrator(r); print(o.match_factory('keyboard'))"

# Bash test
./orchestrator-match.sh "keyboard" factories-registry.jsonl | jq '.top_match'

# Registry test
jq '.' factories-registry.jsonl > /dev/null && echo "✓ Valid registry"
```

---

## Summary

**What changed**: Orchestrator now uses lightweight JSONL registry instead of embedding all metadata

**Key benefit**: Works in 3 contexts (Perplexity, Python, Bash) with single registry file

**Total files**: 5 (registry + orchestrator + implementations + docs)

**Time to setup**: 2 minutes

**Learning curve**: Minimal (paste into Perplexity, read suggestions, or use Python/Bash scripts)

---

**Version**: 3.2+  
**Updated**: 2025-12-05  
**Status**: ✓ Production-ready
