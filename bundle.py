#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "PyYAML>=6.0",
# ]
# ///

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "Error: PyYAML is required to run bundle.py.\n"
        "Install with:\n\n"
        "  python3 -m pip install PyYAML\n\n"
    )
    raise


def resolve_prompts_dir() -> Path:
    """Return the root prompts/ directory (library root / prompts)."""
    return Path(__file__).resolve().parent / "prompts"


def list_collections(prompts_dir: Path) -> None:
    """List collections and their bundle configs."""
    print(f"Collections in {prompts_dir}:")
    print()
    for coll_dir in sorted(prompts_dir.iterdir()):
        if not coll_dir.is_dir():
            continue
        print(f" {coll_dir.name}/")
        bundle_files = sorted(
            list(coll_dir.glob("bundle.yaml")) +
            list(coll_dir.glob("bundle.*.yaml"))
        )
        for cfg in bundle_files:
            print(f"   {cfg.name}")


def load_yaml(path: Path) -> Dict[str, Any]:
    """Load a YAML file and ensure the top level is a mapping."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Config {path} must be a YAML mapping at top level.")
    return data


def get_event(config: Dict[str, Any]) -> Dict[str, Any]:
    event = config.get("event") or {}
    if not isinstance(event, dict):
        raise ValueError("event must be a mapping.")
    name = event.get("name")
    if not name:
        raise ValueError("event.name is required.")
    return event


def get_participants(config: Dict[str, Any]) -> Dict[str, Any]:
    participants = config.get("participants") or {}
    if not isinstance(participants, dict):
        raise ValueError("participants must be a mapping if present.")
    roles = participants.get("roles") or []
    if roles is None:
        roles = []
    if not isinstance(roles, list):
        raise ValueError("participants.roles must be a list.")
    return {
        "roles": roles,
    }


def get_skills(config: Dict[str, Any]) -> List[str]:
    skills = config.get("skills") or []
    if skills is None:
        skills = []
    if not isinstance(skills, list):
        raise ValueError("skills must be a list if present.")
    return skills


def get_include(config: Dict[str, Any]) -> Dict[str, Any]:
    include = config.get("include") or {}
    if not isinstance(include, dict):
        raise ValueError("include must be a mapping if present.")
    context = include.get("context") or []
    if context is None:
        context = []
    if not isinstance(context, list):
        raise ValueError("include.context must be a list.")
    templates = bool(include.get("templates", False))
    factories = include.get("factories", False)
    roadmap = bool(include.get("roadmap", False))
    return {
        "context": context,
        "templates": templates,
        "factories": factories,
        "roadmap": roadmap,
    }


def merge_lists(base: List[str], override: List[str]) -> List[str]:
    """Merge two lists with deduplication, preserving order."""
    seen = set()
    merged: List[str] = []
    for item in base + override:
        if item not in seen:
            seen.add(item)
            merged.append(item)
    return merged


def merge_configs(defaults: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge defaults and override configs with special handling for:
    - event (mapping)
    - participants.roles (list merged)
    - skills (list merged)
    - include.context (list merged)
    """
    merged: Dict[str, Any] = dict(defaults)
    merged.update(override)  # shallow override, then fix nested sections

    # event
    if "event" in defaults or "event" in override:
        event_base = defaults.get("event", {}) or {}
        event_override = override.get("event", {}) or {}
        event_merged = dict(event_base)
        event_merged.update(event_override)
        merged["event"] = event_merged

    # participants.roles
    part_base = defaults.get("participants", {}) or {}
    part_override = override.get("participants", {}) or {}
    roles_base = part_base.get("roles") or []
    roles_override = part_override.get("roles") or []
    merged_participants = dict(part_base)
    merged_participants.update(part_override)
    merged_participants["roles"] = merge_lists(roles_base, roles_override)
    merged["participants"] = merged_participants

    # skills
    skills_base = defaults.get("skills") or []
    skills_override = override.get("skills") or []
    merged["skills"] = merge_lists(skills_base, skills_override)

    # include.context
    include_base = defaults.get("include") or {}
    include_override = override.get("include") or {}
    include_merged = dict(include_base)
    include_merged.update(include_override)
    ctx_base = include_base.get("context") or []
    ctx_override = include_override.get("context") or []
    include_merged["context"] = merge_lists(ctx_base, ctx_override)
    merged["include"] = include_merged

    return merged


def is_flat_collection(coll_dir: Path) -> bool:
    """Return True if collection has no events/ and no roles/."""
    return not (coll_dir / "events").is_dir() and not (coll_dir / "roles").is_dir()


def find_role_file(coll_dir: Path, role: str) -> Optional[Path]:
    """Find a role file in roles/, roles/judges/, or roles/specialists/."""
    candidates = [
        coll_dir / "roles" / f"{role}.md",
        coll_dir / "roles" / "judges" / f"{role}.md",
        coll_dir / "roles" / "specialists" / f"{role}.md",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def find_skill_file(coll_dir: Path, skill: str) -> Optional[Path]:
    """Find a skill file in skills/."""
    path = coll_dir / "skills" / f"{skill}.md"
    return path if path.is_file() else None


def resolve_context_files(coll_dir: Path, event_name: str, include_ctx: List[str]) -> List[Path]:
    """Resolve include.context entries to actual files, with handoff-context alias support."""
    files: List[Path] = []
    for item in include_ctx:
        if item == "handoff-context":
            event_local = coll_dir / "events" / event_name / "handoff-context.md"
            root = coll_dir / "handoff-context.md"
            if event_local.is_file():
                files.append(event_local)
            elif root.is_file():
                files.append(root)
            else:
                sys.stderr.write(f"Warning: no handoff-context found for {event_name}\n")
        else:
            path = coll_dir / item
            if path.is_file():
                files.append(path)
            else:
                sys.stderr.write(f"Warning: include.context target not found: {path}\n")
    # dedupe, preserving order
    seen = set()
    unique_files: List[Path] = []
    for f in files:
        key = f.resolve()
        if key not in seen:
            seen.add(key)
            unique_files.append(f)
    return unique_files


def assemble_files(
    coll_dir: Path,
    event_conf: Dict[str, Any],
    participants_conf: Dict[str, Any],
    skills_conf: List[str],
    include_conf: Dict[str, Any],
) -> List[Path]:
    """Assemble the ordered list of files to bundle for a structured collection."""
    event_name = event_conf["name"]

    files: List[Path] = []

    # 1. charter — prefer charter.md, fall back to meetings-charter.md
    charter = coll_dir / "context" / "charter.md"
    if not charter.is_file():
        charter = coll_dir / "context" / "meetings-charter.md"
    if charter.is_file():
        files.append(charter)
    else:
        sys.stderr.write(f"Warning: charter not found in {coll_dir}/context\n")

    # 2. event definition
    event_file = coll_dir / "events" / event_name / "event.md"
    if event_file.is_file():
        files.append(event_file)
    else:
        sys.stderr.write(f"Warning: event file not found: {event_file}\n")

    # 3. event preferences (optional)
    prefs = coll_dir / "events" / event_name / "preferences.md"
    if prefs.is_file():
        files.append(prefs)

    # 4. include.context
    ctx_files = resolve_context_files(coll_dir, event_name, include_conf["context"])
    files.extend(ctx_files)

    # 5. roles
    missing_roles: List[str] = []
    for role in participants_conf["roles"]:
        rf = find_role_file(coll_dir, role)
        if rf:
            files.append(rf)
        else:
            missing_roles.append(role)
    if missing_roles:
        sys.stderr.write(f"Warning: role files not found: {', '.join(missing_roles)}\n")

    # 6. skills
    missing_skills: List[str] = []
    for skill in skills_conf:
        sf = find_skill_file(coll_dir, skill)
        if sf:
            files.append(sf)
        else:
            missing_skills.append(skill)
    if missing_skills:
        sys.stderr.write(f"Warning: skill files not found: {', '.join(missing_skills)}\n")

    # 7. session prompt — prefer event-local, fall back to templates/
    session = coll_dir / "events" / event_name / "session-prompt.md"
    if not session.is_file():
        session = coll_dir / "templates" / "meeting-session-prompt.md"
    if session.is_file():
        files.append(session)

    # dedupe by resolved path
    seen = set()
    unique_files: List[Path] = []
    for f in files:
        key = f.resolve()
        if key not in seen:
            seen.add(key)
            unique_files.append(f)

    return unique_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="bundle.py",
        description="Assemble a paste-ready session prompt from a collection in the ai-prompt-library.",
    )
    parser.add_argument(
        "-p", "--collection",
        help="Collection name under prompts/ (e.g. panel-of-judges)",
    )
    parser.add_argument(
        "-c", "--config",
        help="Path to a bundle config YAML (relative or absolute)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (defaults to <collection>/generated/session.txt)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would be included without writing output",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List collections and their bundle configs",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompts_dir = resolve_prompts_dir()

    if args.list:
        list_collections(prompts_dir)
        return

    if not args.collection and not args.config:
        sys.stderr.write("Error: no collection specified. Use -p or -c.\n")
        sys.exit(1)

    if args.collection:
        coll_dir = prompts_dir / args.collection
    else:
        # derive collection from config parent
        cfg_path = Path(args.config).resolve()
        coll_dir = cfg_path.parent

    if not coll_dir.is_dir():
        sys.stderr.write(f"Error: collection not found: {coll_dir}\n")
        sys.exit(1)

    # Default config discovery if none provided
    config_path = Path(args.config) if args.config else None
    if config_path is None:
        default_cfg = coll_dir / "bundle.yaml"
        if not default_cfg.is_file():
            bundle_candidates = sorted(coll_dir.glob("bundle.*.yaml"))
            default_cfg = bundle_candidates[0] if bundle_candidates else None
        if default_cfg is None:
            sys.stderr.write(f"Error: no bundle config found in {coll_dir}\n")
            sys.exit(1)
        config_path = default_cfg

    # Load and merge configs
    config_raw = load_yaml(config_path)
    event_section = config_raw.get("event") or {}
    defaults_ref = event_section.get("defaults")
    if defaults_ref:
        defaults_path = (coll_dir / defaults_ref).resolve()
        if not defaults_path.is_file():
            raise FileNotFoundError(f"Defaults config not found: {defaults_path}")
        defaults_raw = load_yaml(defaults_path)
        config_merged = merge_configs(defaults_raw, config_raw)
    else:
        config_merged = config_raw

    if is_flat_collection(coll_dir):
        # Flat collection: copy main .md to generated/session.txt
        main_prompt: Optional[Path] = None
        for candidate in [
            coll_dir / f"{coll_dir.name}.md",
            coll_dir / "main.md",
        ] + list(coll_dir.glob("*.md")):
            if candidate.is_file():
                main_prompt = candidate
                break
        if main_prompt is None:
            sys.stderr.write(f"Error: no prompt file found in flat collection: {coll_dir}\n")
            sys.exit(1)
        out_dir = coll_dir / "generated"
        out_dir.mkdir(parents=True, exist_ok=True)
        output_path = Path(args.output) if args.output else out_dir / "session.txt"
        if args.dry_run:
            print("Dry run (flat collection):")
            print(f"  {main_prompt}")
            print(f"Output: {output_path}")
            return
        output_path.write_text(main_prompt.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Copied → {output_path}")
        return

    # Structured collection
    event_conf = get_event(config_merged)
    participants_conf = get_participants(config_merged)
    skills_conf = get_skills(config_merged)
    include_conf = get_include(config_merged)

    files = assemble_files(coll_dir, event_conf, participants_conf, skills_conf, include_conf)

    out_dir = coll_dir / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = Path(args.output) if args.output else out_dir / "session.txt"

    if args.dry_run:
        print(f"Dry run — {coll_dir.name} / {event_conf['name']}")
        print()
        for f in files:
            print(f"  {f.relative_to(Path(__file__).resolve().parent)}")
        print()
        print(f"Output: {output_path}")
        return

    with output_path.open("w", encoding="utf-8") as out:
        for f in files:
            out.write(f.read_text(encoding="utf-8"))
            out.write("\n\n")

    print(f"Bundled → {output_path}")


if __name__ == "__main__":
    main()