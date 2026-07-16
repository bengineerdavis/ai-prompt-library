#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "PyYAML>=6.0",
# ]
# ///

from __future__ import annotations

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
    return Path(__file__).resolve().parent / "prompts"


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Config {path} must be a YAML mapping at top level.")
    return data


def list_collections(prompts_dir: Path) -> None:
    print(f"Collections in {prompts_dir}:")
    print()
    for coll_dir in sorted(prompts_dir.iterdir()):
        if not coll_dir.is_dir():
            continue
        print(f"{coll_dir.name}/")
        bundle_files = sorted(
            list(coll_dir.glob("bundle.yaml")) +
            list(coll_dir.glob("bundle.*.yaml"))
        )
        for cfg in bundle_files:
            print(f"  {cfg.name}")
        print()


def merge_lists(base: List[str], override: List[str]) -> List[str]:
    seen = set()
    merged: List[str] = []
    for item in base + override:
        if item not in seen:
            seen.add(item)
            merged.append(item)
    return merged


def merge_configs(defaults: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(defaults)
    merged.update(override)

    if "event" in defaults or "event" in override:
        event_base = defaults.get("event", {}) or {}
        event_override = override.get("event", {}) or {}
        event_merged = dict(event_base)
        event_merged.update(event_override)
        merged["event"] = event_merged

    part_base = defaults.get("participants", {}) or {}
    part_override = override.get("participants", {}) or {}
    roles_base = part_base.get("roles") or []
    roles_override = part_override.get("roles") or []
    participants_merged = dict(part_base)
    participants_merged.update(part_override)
    participants_merged["roles"] = merge_lists(roles_base, roles_override)
    merged["participants"] = participants_merged

    skills_base = defaults.get("skills") or []
    skills_override = override.get("skills") or []
    merged["skills"] = merge_lists(skills_base, skills_override)

    include_base = defaults.get("include", {}) or {}
    include_override = override.get("include", {}) or {}
    include_merged = dict(include_base)
    include_merged.update(include_override)
    ctx_base = include_base.get("context") or []
    ctx_override = include_override.get("context") or []
    include_merged["context"] = merge_lists(ctx_base, ctx_override)
    merged["include"] = include_merged

    return merged


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
    if not isinstance(roles, list):
        raise ValueError("participants.roles must be a list.")
    return {"roles": roles}


def get_skills(config: Dict[str, Any]) -> List[str]:
    skills = config.get("skills") or []
    if not isinstance(skills, list):
        raise ValueError("skills must be a list if present.")
    return skills


def get_include(config: Dict[str, Any]) -> Dict[str, Any]:
    include = config.get("include") or {}
    if not isinstance(include, dict):
        raise ValueError("include must be a mapping if present.")

    context = include.get("context") or []
    if not isinstance(context, list):
        raise ValueError("include.context must be a list.")

    templates = include.get("templates", False)
    factories = include.get("factories", False)
    roadmap = include.get("roadmap", False)

    if not isinstance(templates, bool):
        raise ValueError("include.templates must be a boolean.")
    if not isinstance(roadmap, bool):
        raise ValueError("include.roadmap must be a boolean.")
    if not isinstance(factories, (bool, list)):
        raise ValueError("include.factories must be a boolean or a list.")

    if isinstance(factories, list):
        for item in factories:
            if not isinstance(item, str):
                raise ValueError("include.factories list entries must be strings.")

    return {
        "context": context,
        "templates": templates,
        "factories": factories,
        "roadmap": roadmap,
    }


def is_flat_collection(coll_dir: Path) -> bool:
    return not (coll_dir / "events").is_dir() and not (coll_dir / "roles").is_dir()


def dedupe_paths(paths: List[Path]) -> List[Path]:
    seen = set()
    unique: List[Path] = []
    for path in paths:
        key = path.resolve()
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return unique


def find_role_file(coll_dir: Path, role: str) -> Optional[Path]:
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
    path = coll_dir / "skills" / f"{skill}.md"
    return path if path.is_file() else None


def resolve_context_files(coll_dir: Path, event_name: str, include_ctx: List[str]) -> List[Path]:
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
    return dedupe_paths(files)


def resolve_template_files(coll_dir: Path, include_templates: bool) -> List[Path]:
    if not include_templates:
        return []

    templates_dir = coll_dir / "templates"
    if not templates_dir.is_dir():
        sys.stderr.write(f"Warning: templates directory not found: {templates_dir}\n")
        return []

    files = sorted(templates_dir.glob("*.md"))
    if not files:
        sys.stderr.write(f"Warning: no template markdown files found in {templates_dir}\n")
    return files


def resolve_factory_files(coll_dir: Path, include_factories: bool | List[str]) -> List[Path]:
    if not include_factories:
        return []

    candidates: List[Path] = []

    if isinstance(include_factories, bool):
        for dirname in ["factories", "factory", "meta"]:
            d = coll_dir / dirname
            if d.is_dir():
                candidates.extend(sorted(d.glob("*.md")))
    else:
        for item in include_factories:
            path = coll_dir / item
            if path.is_file():
                candidates.append(path)
            elif path.is_dir():
                candidates.extend(sorted(path.glob("*.md")))
            else:
                sys.stderr.write(f"Warning: include.factories target not found: {path}\n")

    if not candidates:
        sys.stderr.write(
            f"Warning: no factory markdown files resolved in collection {coll_dir.name}\n"
        )

    return dedupe_paths(candidates)


def resolve_roadmap_files(coll_dir: Path, include_roadmap: bool) -> List[Path]:
    if not include_roadmap:
        return []

    candidates = [
        coll_dir / "ROADMAP.md",
        coll_dir / "docs" / "ROADMAP.md",
    ]
    files = [p for p in candidates if p.is_file()]
    if not files:
        sys.stderr.write(f"Warning: no ROADMAP.md found for collection {coll_dir.name}\n")
    return dedupe_paths(files)


def assemble_files(
    coll_dir: Path,
    event_conf: Dict[str, Any],
    participants_conf: Dict[str, Any],
    skills_conf: List[str],
    include_conf: Dict[str, Any],
) -> List[Path]:
    event_name = event_conf["name"]
    files: List[Path] = []

    charter = coll_dir / "context" / "charter.md"
    if not charter.is_file():
        charter = coll_dir / "context" / "meetings-charter.md"
    if charter.is_file():
        files.append(charter)
    else:
        sys.stderr.write(f"Warning: charter not found in {coll_dir}/context\n")

    event_file = coll_dir / "events" / event_name / "event.md"
    if event_file.is_file():
        files.append(event_file)
    else:
        sys.stderr.write(f"Warning: event file not found: {event_file}\n")

    prefs = coll_dir / "events" / event_name / "preferences.md"
    if prefs.is_file():
        files.append(prefs)

    files.extend(resolve_context_files(coll_dir, event_name, include_conf["context"]))

    missing_roles = []
    for role in participants_conf["roles"]:
        rf = find_role_file(coll_dir, role)
        if rf:
            files.append(rf)
        else:
            missing_roles.append(role)
    if missing_roles:
        sys.stderr.write(f"Warning: role files not found: {', '.join(missing_roles)}\n")

    missing_skills = []
    for skill in skills_conf:
        sf = find_skill_file(coll_dir, skill)
        if sf:
            files.append(sf)
        else:
            missing_skills.append(skill)
    if missing_skills:
        sys.stderr.write(f"Warning: skill files not found: {', '.join(missing_skills)}\n")

    files.extend(resolve_template_files(coll_dir, include_conf["templates"]))
    files.extend(resolve_factory_files(coll_dir, include_conf["factories"]))
    files.extend(resolve_roadmap_files(coll_dir, include_conf["roadmap"]))

    session = coll_dir / "events" / event_name / "session-prompt.md"
    if not session.is_file():
        session = coll_dir / "templates" / "meeting-session-prompt.md"
    if session.is_file():
        files.append(session)

    return dedupe_paths(files)


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
        coll_dir = Path(args.config).resolve().parent

    if not coll_dir.is_dir():
        sys.stderr.write(f"Error: collection not found: {coll_dir}\n")
        sys.exit(1)

    config_path = Path(args.config).resolve() if args.config else None
    if config_path is None:
        default_cfg = coll_dir / "bundle.yaml"
        if not default_cfg.is_file():
            bundle_candidates = sorted(coll_dir.glob("bundle.*.yaml"))
            default_cfg = bundle_candidates[0] if bundle_candidates else None
        if default_cfg is None:
            sys.stderr.write(f"Error: no bundle config found in {coll_dir}\n")
            sys.exit(1)
        config_path = default_cfg

    config_raw = load_yaml(config_path)

    event_section = config_raw.get("event") or {}
    if not isinstance(event_section, dict):
        raise ValueError("event must be a mapping.")
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
        main_prompt = None
        for candidate in [
            coll_dir / f"{coll_dir.name}.md",
            coll_dir / "main.md",
            *sorted(coll_dir.glob("*.md")),
        ]:
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
        print(f"Copied -> {output_path}")
        return

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

    print(f"Bundled -> {output_path}")


if __name__ == "__main__":
    main()