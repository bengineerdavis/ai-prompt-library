from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent

# Filenames within registries/
FACTORY_REGISTRY  = "factories-registry-v3.3.jsonl"
STRATEGY_REGISTRY = "seed-prompting-strategies-v1.1.jsonl"
REGISTRIES_SUBDIR = "registries"

# Paths relative to repo root
PROFILE_PATH      = "seed/profile/profile.md"
ORCHESTRATOR_PATH = "seed/orchestrator/orchestrator.md"


# ---------------------------------------------------------------------------
# Readers
# ---------------------------------------------------------------------------

def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            s = line.strip()
            if not s:
                continue
            try:
                rows.append(json.loads(s))
            except json.JSONDecodeError as e:
                raise SystemExit(f"Invalid JSONL in {path} line {n}: {e}")
    return rows


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def to_jsonl_text(rows: list[dict]) -> str:
    return "\n".join(
        json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows
    )


def render_paste1(factory_rows: list[dict]) -> str:
    return dedent(f"""\
SEED SYSTEM BOOTSTRAP — PASTE 1 of 3: REGISTRY
Paste this first. Do not respond yet. Acknowledge with "Registry loaded ✓"

--- {FACTORY_REGISTRY} ---
{to_jsonl_text(factory_rows)}
--- END REGISTRY ---
""")


def render_paste2(profile_text: str, orchestrator_text: str) -> str:
    return dedent(f"""\
SEED SYSTEM BOOTSTRAP — PASTE 2 of 3: SEED PROFILE + ORCHESTRATOR
Paste after registry. Do not respond yet. Acknowledge with "Orchestrator loaded ✓"

--- {PROFILE_PATH} ---
{profile_text}
--- END SEED PROFILE ---

--- {ORCHESTRATOR_PATH} ---
{orchestrator_text}
--- END ORCHESTRATOR ---
""")


def render_paste3(strategy_rows: list[dict]) -> str:
    core, council = [], []
    for s in strategy_rows:
        effectiveness = s.get("effectiveness", "?")
        cost = s.get("computational_cost", "?")
        line = f"- {s['name']} ({effectiveness}, {cost})"
        if s.get("requires_multiple_runs"):
            line = line.rstrip(")") + ", requires_multiple_runs)"
        impl = s.get("implementation", s.get("description", ""))
        best = ", ".join(s.get("best_for", []))
        line += f": {impl}. Best for: {best}."
        if "council" in s.get("tags", []):
            council.append(line)
        else:
            core.append(line)

    core_block    = "\n".join(core)    if core    else "(none)"
    council_block = "\n".join(council) if council else "(none)"

    return dedent(f"""\
SEED SYSTEM BOOTSTRAP — PASTE 3 of 3: STRATEGY REGISTRY
Paste last. Respond with "Strategy registry loaded ✓ — all 3 components active. State your goal."

--- {STRATEGY_REGISTRY} ---
CORE STRATEGIES:
{core_block}

COUNCIL STRATEGIES:
{council_block}
--- END STRATEGIES ---
""")


def write_bootstrap_quickstart(outdir: Path) -> None:
    text = dedent("""\
# Bootstrap Quickstart

1. Paste `PASTE-1-registry.md`
2. Paste `PASTE-2-orchestrator.md`
3. Paste `PASTE-3-strategies.md`
4. Then send your goal:

    Goal: [your goal here]

Example goals:
- Goal: I want to study Sentry tracing and breadcrumbs for my support role
- Goal: Create a 6-week DevOps learning roadmap
- Goal: Help me prep for a staff engineer behavioral interview
- Goal: Build a new factory for Kubernetes troubleshooting
- Goal: Best mechanical keyboard to buy under $150

For full usage instructions see QUICKSTART.md in the repo root.
For registry setup and factory registration see docs/setup.md.
""")
    (outdir / "BOOTSTRAP-QUICKSTART.md").write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Path resolution + validation
# ---------------------------------------------------------------------------

def resolve_paths(root: Path, registries_dir: str) -> dict[str, Path]:
    registries = root / registries_dir
    return {
        "registries_dir": registries,
        "factory":        registries / FACTORY_REGISTRY,
        "strategy":       registries / STRATEGY_REGISTRY,
        "profile":        root / PROFILE_PATH,
        "orchestrator":   root / ORCHESTRATOR_PATH,
    }


def validate_paths(paths: dict[str, Path]) -> bool:
    ok = True

    reg_dir = paths["registries_dir"]
    if not reg_dir.is_dir():
        print(f"  MISSING DIR   {reg_dir}")
        ok = False
    else:
        print(f"  OK  (dir)     {reg_dir}")

    labels = {
        "factory":     FACTORY_REGISTRY,
        "strategy":    STRATEGY_REGISTRY,
        "profile":     PROFILE_PATH,
        "orchestrator": ORCHESTRATOR_PATH,
    }
    for key, label in labels.items():
        path = paths[key]
        if not path.exists():
            print(f"  MISSING       {label}")
            ok = False
        else:
            size = path.stat().st_size
            print(f"  OK  ({size:>7,} B)  {label}")

    return ok


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build Seed bootstrap paste files from the live repo.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--root", default=".",
        help="Repo root directory (default: current directory)"
    )
    parser.add_argument(
        "--registries-dir", default=REGISTRIES_SUBDIR, dest="registries_dir",
        help=f"Registries subdirectory relative to --root (default: '{REGISTRIES_SUBDIR}')"
    )
    parser.add_argument(
        "--output", default="bootstrap-out",
        help="Output directory for paste files (default: bootstrap-out)"
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Validate source files only; do not write output"
    )
    args = parser.parse_args()

    root   = Path(args.root).expanduser().resolve()
    outdir = Path(args.output).expanduser().resolve()
    paths  = resolve_paths(root, args.registries_dir)

    print(f"Root:          {root}")
    print(f"Registries:    {paths['registries_dir']}")
    print()

    all_ok = validate_paths(paths)
    if not all_ok:
        raise SystemExit("\nValidation failed — fix missing files above before building.")

    if args.validate:
        factory_rows  = read_jsonl(paths["factory"])
        strategy_rows = read_jsonl(paths["strategy"])
        print()
        print(f"Factories : {len(factory_rows)}")
        print(f"Strategies: {len(strategy_rows)}")
        print("\nValidation passed.")
        return

    # Read all source files
    factory_rows  = read_jsonl(paths["factory"])
    strategy_rows = read_jsonl(paths["strategy"])
    profile_text  = read_text(paths["profile"])
    orch_text     = read_text(paths["orchestrator"])

    # Write output
    outdir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "PASTE-1-registry.md":     render_paste1(factory_rows),
        "PASTE-2-orchestrator.md": render_paste2(profile_text, orch_text),
        "PASTE-3-strategies.md":   render_paste3(strategy_rows),
    }

    print()
    for name, content in outputs.items():
        dest = outdir / name
        dest.write_text(content, encoding="utf-8")
        print(f"Wrote: {dest}")

    write_bootstrap_quickstart(outdir)
    print(f"Wrote: {outdir / 'BOOTSTRAP-QUICKSTART.md'}")
    print(f"\nDone — {len(outputs) + 1} files in {outdir}")


if __name__ == "__main__":
    main()