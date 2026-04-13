#!/usr/bin/env python3
"""Build Seed bootstrap paste files from the live repo."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from textwrap import dedent

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REGISTRIES_SUBDIR = "registries"
FACTORY_REGISTRY = "factories-registry-v3.3.jsonl"
STRATEGY_REGISTRY = "seed-prompting-strategies-v1.1.jsonl"
PROFILE_PATH = "seed/profile/profile.md"
ORCHESTRATOR_PATH = "seed/orchestrator/orchestrator.md"
CHANGELOG_PATH = "CHANGELOG.md"
IMPROMPTU_FACTORIES = "prompts/impromptu/factories"

# Patterns for parsing factory .md files
_METADATA_RE = re.compile(
    r"##\s+Metadata\s+```json\s*(\{.*?\})\s*```",
    re.DOTALL | re.IGNORECASE,
)
_TITLE_RE = re.compile(r"^#\s+(?:TITLE\s+)?(.+)", re.MULTILINE)

QUICKSTART = dedent("""\
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


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSONL {path}:{n}: {e}")
    return rows


def to_jsonl(rows: list[dict]) -> str:
    return "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows)


# ---------------------------------------------------------------------------
# Factory discovery
# ---------------------------------------------------------------------------


class FactoryDiscoveryError(Exception):
    """Raised when .md files are found that don't follow the <dir>/<dir>.md
    naming convention and are not README.md or inside versions/.

    Attributes:
    ----------
    unmatched  : files that failed the convention check
    candidates : the expected correct path for each unmatched file
    valid      : files that did pass (caller may still use these)
    """

    def __init__(
        self,
        unmatched: list[Path],
        candidates: list[Path],
        valid: list[Path],
    ) -> None:
        self.unmatched = unmatched
        self.candidates = candidates
        self.valid = valid
        lines = "\n".join(
            f"  found:    {u}\n  expected: {c}" for u, c in zip(unmatched, candidates)
        )
        super().__init__(
            f"{len(unmatched)} .md file(s) don't follow the <dir>/<dir>.md "
            f"naming convention:\n{lines}"
        )


def discover_factories(scan_dir: Path) -> list[Path]:
    """Recursively find factory .md files under scan_dir.

    Convention
    ----------
    A factory file must be named after its immediate parent directory:
        factories/sentry-support-tutor/sentry-support-tutor.md  ← valid
        factories/sentry-support-tutor/something-else.md        ← invalid
        factories/sentry-support-tutor/README.md                ← silently ignored
        factories/versions/factory-template-v1.1.md             ← silently ignored

    Raises FactoryDiscoveryError if any non-ignored .md files don't satisfy
    the convention, carrying both the offending paths and the expected filenames
    so the caller can surface a helpful error message.
    """
    if not scan_dir.is_dir():
        return []

    valid: list[Path] = []
    unmatched: list[Path] = []

    for path in sorted(scan_dir.rglob("*.md")):
        rel_parts = path.relative_to(scan_dir).parts

        if "versions" in rel_parts:  # archived / template dirs
            continue
        if path.name.lower() == "readme.md":  # maintainer docs
            continue

        # Convention: stem must match the immediate parent directory name
        if path.stem == path.parent.name:
            valid.append(path)
        else:
            unmatched.append(path)

    if unmatched:
        candidates = [p.parent / f"{p.parent.name}.md" for p in unmatched]
        raise FactoryDiscoveryError(unmatched, candidates, valid)

    return valid


def parse_factory_entry(path: Path, source_label: str) -> dict:
    """Build a registry-compatible dict from a factory .md file.

    Strategy:
      1. Parse the ## Metadata JSON block — present in all well-formed factories.
      2. Fall back to the first heading + filename for bare/draft files.

    Always stamps 'source' and 'path' so the LLM can see the provenance.
    """
    text = path.read_text(encoding="utf-8")

    m = _METADATA_RE.search(text)
    if m:
        try:
            entry = json.loads(m.group(1))
            entry.setdefault("source", source_label)
            entry.setdefault("path", str(path))
            return entry
        except json.JSONDecodeError:
            pass  # fall through to heading-based fallback

    title_m = _TITLE_RE.search(text)
    title = title_m.group(1).strip() if title_m else path.stem
    return {
        "name": path.stem,
        "title": title,
        "description": f"Auto-discovered factory: {title}",
        "source": source_label,
        "path": str(path),
        "autogenerated": True,
    }


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------


def render_paste1(factory_rows: list[dict], impromptu_rows: list[dict] | None = None) -> str:
    out = (
        "SEED SYSTEM BOOTSTRAP — PASTE 1 of 3: REGISTRY\n"
        'Paste this first. Do not respond yet. Acknowledge with "Registry loaded ✓"\n\n'
        f"--- {FACTORY_REGISTRY} ---\n"
        f"{to_jsonl(factory_rows)}\n"
        "--- END REGISTRY ---\n"
    )
    if impromptu_rows:
        out += (
            "\n--- IMPROMPTU FACTORIES (discovered; not registry-verified) ---\n"
            + to_jsonl(impromptu_rows)
            + "\n--- END IMPROMPTU FACTORIES ---\n"
        )
    return out


def render_paste2(profile: str, orchestrator: str, changelog: str | None = None) -> str:
    out = (
        "SEED SYSTEM BOOTSTRAP — PASTE 2 of 3: SEED PROFILE + ORCHESTRATOR\n"
        'Paste after registry. Do not respond yet. Acknowledge with "Orchestrator loaded ✓"\n\n'
        f"--- {PROFILE_PATH} ---\n{profile}\n--- END SEED PROFILE ---\n\n"
        f"--- {ORCHESTRATOR_PATH} ---\n{orchestrator}\n--- END ORCHESTRATOR ---\n"
    )
    if changelog:
        out += f"\n--- {CHANGELOG_PATH} ---\n{changelog}\n--- END CHANGELOG ---\n"
    return out


def render_paste3(strategy_rows: list[dict]) -> str:
    core, council = [], []
    for s in strategy_rows:
        line = (
            f"- {s['name']} ({s.get('effectiveness', '?')}, {s.get('computational_cost', '?')}"
            + (", requires_multiple_runs" if s.get("requires_multiple_runs") else "")
            + f"): {s.get('implementation', s.get('description', ''))}."
            + f" Best for: {', '.join(s.get('best_for', []))}."
        )
        (council if "council" in s.get("tags", []) else core).append(line)

    return (
        "SEED SYSTEM BOOTSTRAP — PASTE 3 of 3: STRATEGY REGISTRY\n"
        'Paste last. Respond with "Strategy registry loaded ✓ — all 3 components active. State your goal."\n\n'
        f"--- {STRATEGY_REGISTRY} ---\n"
        f"CORE STRATEGIES:\n{chr(10).join(core) or '(none)'}\n\n"
        f"COUNCIL STRATEGIES:\n{chr(10).join(council) or '(none)'}\n"
        "--- END STRATEGIES ---\n"
    )


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_paths(root: Path, reg: Path, impromptu_dir: Path | None = None) -> bool:
    ok = True
    checks: list[tuple[Path, str, bool]] = [
        (reg, f"[dir] {reg}", True),
        (reg / FACTORY_REGISTRY, FACTORY_REGISTRY, True),
        (reg / STRATEGY_REGISTRY, STRATEGY_REGISTRY, True),
        (root / PROFILE_PATH, PROFILE_PATH, True),
        (root / ORCHESTRATOR_PATH, ORCHESTRATOR_PATH, True),
        (root / CHANGELOG_PATH, CHANGELOG_PATH, False),  # optional
    ]
    if impromptu_dir is not None:
        checks.append((impromptu_dir, f"[dir] {impromptu_dir}", True))

    dir_paths = {p for p in (reg, impromptu_dir) if p is not None}
    for path, label, required in checks:
        exists = path.is_dir() if path in dir_paths else path.exists()
        if not exists:
            prefix = "  MISSING  " if required else "  OPTIONAL "
            if required:
                ok = False
            print(f"{prefix}{label}")
        else:
            size = "" if path.is_dir() else f"({path.stat().st_size:>7,} B)  "
            print(f"  OK  {size}{label}")
    return ok


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repo root (default: .)")
    parser.add_argument("--registries-dir", default=REGISTRIES_SUBDIR, dest="registries_dir")
    parser.add_argument("--output", default="bootstrap-out", help="Output directory")
    parser.add_argument("--validate", action="store_true", help="Validate only; no output written")
    parser.add_argument(
        "--include-impromptu",
        action="store_true",
        dest="include_impromptu",
        help=(
            "Discover and append factory .md files from the impromptu factories dir "
            "to PASTE-1 as a labelled block (opt-in; omit to preserve existing behaviour)"
        ),
    )
    parser.add_argument(
        "--impromptu-dir",
        default=IMPROMPTU_FACTORIES,
        dest="impromptu_dir",
        help=f"Impromptu factories path relative to --root (default: '{IMPROMPTU_FACTORIES}')",
    )
    parser.add_argument(
        "--no-changelog",
        action="store_true",
        dest="no_changelog",
        help="Suppress CHANGELOG.md injection into PASTE-2 (included by default when found)",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    reg = root / args.registries_dir
    impromptu_dir = (root / args.impromptu_dir) if args.include_impromptu else None

    print(f"Root:       {root}\nRegistries: {reg}")
    if impromptu_dir:
        print(f"Impromptu:  {impromptu_dir}")
    print()

    if not validate_paths(root, reg, impromptu_dir):
        raise SystemExit("\nValidation failed — fix missing files above before building.")

    factory_rows = read_jsonl(reg / FACTORY_REGISTRY)
    strategy_rows = read_jsonl(reg / STRATEGY_REGISTRY)

    # Load CHANGELOG if present and not suppressed
    changelog_path = root / CHANGELOG_PATH
    changelog: str | None = None
    if not args.no_changelog:
        if changelog_path.exists():
            changelog = changelog_path.read_text(encoding="utf-8").strip()
            print(f"Changelog:  {changelog_path}  ({changelog_path.stat().st_size:,} B)")
        else:
            print(f"Changelog:  (not found at {CHANGELOG_PATH} — skipping)")
        print()

    # Discover impromptu factories if requested
    impromptu_rows: list[dict] | None = None
    if args.include_impromptu and impromptu_dir:
        try:
            found = discover_factories(impromptu_dir)
        except FactoryDiscoveryError as exc:
            print(f"  WARNING: naming convention violation in {impromptu_dir.relative_to(root)}:")
            print(f"  {exc}")
            print("\n  Possible valid filenames (rename to fix):")
            for c in exc.candidates:
                print(f"    {c.relative_to(impromptu_dir)}")
            print()
            found = exc.valid  # continue with files that did pass

        if found:
            impromptu_rows = [parse_factory_entry(p, source_label="impromptu") for p in found]
            print(f"Discovered {len(impromptu_rows)} impromptu factory file(s):")
            for p in found:
                print(f"  {p.relative_to(root)}")
        else:
            print(f"  (no factory .md files found in {impromptu_dir.relative_to(root)})")
        print()

    if args.validate:
        print(f"Factories  (registry):  {len(factory_rows)}")
        if impromptu_rows is not None:
            print(f"Factories  (impromptu): {len(impromptu_rows)}")
        print(f"Strategies:             {len(strategy_rows)}")
        if changelog is not None:
            print(f"Changelog:              yes ({len(changelog.splitlines())} lines)")
        print("\nValidation passed.")
        return

    profile = (root / PROFILE_PATH).read_text(encoding="utf-8").strip()
    orch = (root / ORCHESTRATOR_PATH).read_text(encoding="utf-8").strip()

    outdir = Path(args.output).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "PASTE-1-registry.md": render_paste1(factory_rows, impromptu_rows),
        "PASTE-2-orchestrator.md": render_paste2(profile, orch, changelog),
        "PASTE-3-strategies.md": render_paste3(strategy_rows),
        "BOOTSTRAP-QUICKSTART.md": QUICKSTART,
    }

    print()
    for name, content in outputs.items():
        dest = outdir / name
        dest.write_text(content, encoding="utf-8")
        print(f"Wrote: {dest}")

    print(f"\nDone — {len(outputs)} files in {outdir}")


if __name__ == "__main__":
    main()
