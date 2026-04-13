# Orchestrator

The orchestrator is the session entrypoint for Seed. It reads `factories-registry.jsonl`, matches your query to the right factory using multi-signal scoring, and tells you what to run or paste next.

There are three files here with distinct roles:

| File | What it is | When to use it |
| ---------------------------------- | ---------------------------- | -------------------------------------------------------- |
| `seed-orchestrator-v3.2-hybrid.md` | LLM prompt | Paste into Perplexity or any chat LLM to start a session |
| `orchestrator.py` | Python implementation (v3.3) | Scripts, automation, batch matching, CI |
| `orchestrator-match.sh` | Bash one-liner | Quick terminal match checks; pipe into other scripts |

______________________________________________________________________

## Which file to run

**Starting a Perplexity session:**

```text
Paste 1: factories-registry.jsonl
Paste 2: seed-orchestrator-v3.2-hybrid.md
Paste 3: seed-profile.md
Type:    "Goal: [your goal]"
```

**Matching from the terminal:**

```bash
./orchestrator-match.sh "your query" factories-registry.jsonl
```

**Matching from Python:**

```python
from orchestrator import Orchestrator, Registry

registry = Registry.load("factories-registry.jsonl")
match = Orchestrator(registry).match_factory("your query")
```

______________________________________________________________________

## Inputs and outputs

### `seed-orchestrator-v3.2-hybrid.md`

| | |
| ------------ | ----------------------------------------------------------------------------------------------- |
| **Requires** | `factories-registry.jsonl` (pasted or loaded), `seed-profile.md` |
| **Input** | Natural language goal or query |
| **Output** | Top factory match with confidence score and signal breakdown; instruction on what to paste next |
| **Writes** | Nothing directly — tail module appends to `execution-log.jsonl` after factory runs |

### `orchestrator.py`

| | |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Requires** | `factories-registry.jsonl`, optionally `seed-prompting-strategies.jsonl` |
| **Key classes** | `Registry` (load/query registry), `Orchestrator` (match factory, select strategies), `StrategyRegistry` (filter strategies by use case or cost) |
| **Input** | Query string |
| **Output** | `Match` object with `.factory`, `.confidence`, `.signals` |
| **Writes** | `execution-log.jsonl` via `log_execution()` |

### `orchestrator-match.sh`

| | |
| ------------ | ------------------------------------------------ |
| **Requires** | `factories-registry.jsonl`, `jq` |
| **Input** | Query string, optional registry path |
| **Output** | JSON: `{query, matches[], top_match, timestamp}` |
| **Writes** | Nothing |

______________________________________________________________________

## Mode selection (hybrid prompt only)

When you paste `seed-orchestrator-v3.2-hybrid.md` into an LLM, it auto-detects its context and asks you to confirm:

| Mode | When it applies | What changes |
| ------------ | ------------------------------------------- | -------------------------------------------------------------- |
| **Manual** | Perplexity chat, no file access | Orchestrator tells you what to paste next |
| **Scripted** | Registry loaded from file | Orchestrator references registry directly, returns JSON |
| **Hybrid** | Registry pasted as text + manual selections | Uses registry for matching, prompts for factory paste on match |

______________________________________________________________________

## Match confidence thresholds

| Score | Behavior |
| ------ | ------------------------------- |
| ≥ 90% | Auto-runs factory |
| 85–89% | Asks to confirm (default yes) |
| 75–84% | Shows top 3, asks you to pick |
| < 75% | Suggests creating a new factory |

These thresholds are part of the orchestrator’s matching logic and are separate from the Impromptu scoring and thresholds used inside individual factory runs.

______________________________________________________________________

## Troubleshooting

| Problem | Fix |
| ----------------------- | ---------------------------------------------------------------------------------- |
| No match above 75% | Rephrase with more domain-specific keywords |
| `.sh` permission denied | `chmod +x orchestrator-match.sh` |
| `jq` not found | Install via `brew install jq` or `apt install jq` |
| Python `ImportError` | Confirm `orchestrator.py` and `factories-registry.jsonl` are in the same directory |

______________________________________________________________________

**Orchestrator version**: v3.2 (hybrid prompt) / v3.3 (Python)
