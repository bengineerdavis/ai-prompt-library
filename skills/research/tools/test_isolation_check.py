"""Tests for skills/research/tools/isolation_check.py — the post-hoc
provenance gate for web-briefed analysts (both directions per spec.md:
declines when it must, proceeds when it may). Run:

    uv run --with pytest pytest skills/research/tools/test_isolation_check.py -q
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

TOOL = Path(__file__).with_name("isolation_check.py")
spec = importlib.util.spec_from_file_location("isolation_check", TOOL)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def run_cli(text: str, repo_root: str | None = None) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(TOOL), "-", *( ["--repo-root", repo_root] if repo_root else [] )],
        input=text, capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout + proc.stderr


def test_clean_web_output_proceeds():
    """The relent direction: URL-embedded repo-ish strings are not hits."""
    # mutation: removing the URL-stripping would make this fail — the gate
    # must proceed on legitimate web citations.
    clean = (
        "**Web search:** used\n"
        "A1 https://github.com/testdouble/han/blob/main/han-research/references/evidence-rule.md\n"
        "The docs state the corroboration gate (A1). Renovate docs: A2.\n"
    )
    rc, out = run_cli(clean)
    assert rc == 0, out
    assert "clean" in out


def test_absolute_repo_root_path_is_caught():
    dirty = "the topic lives at /Users/someone/.local/share/chezmoi/dotfiles/apps/herdr/tasks/install.yaml and it says X"
    rc, out = run_cli(dirty, repo_root="/Users/someone/.local/share/chezmoi")
    assert rc == 1
    assert "repo-root path" in out


def test_home_relative_path_is_caught():
    rc, out = run_cli("config at ~/.config/opencode/plugins/herdr-agent-state.js exists")
    assert rc == 1
    assert "home-relative path" in out


def test_repo_relative_file_path_with_line_is_caught():
    """The real 2026-09-19 breach shape: TASKS.md:741, tasks/*.yaml cites."""
    dirty = (
        "Per TASKS.md:741 the pin task is queued, and "
        "dotfiles/apps/herdr/tasks/install.yaml:252 handles it."
    )
    rc, out = run_cli(dirty)
    assert rc == 1
    assert out.count("repo-relative file path") == 2, out


def test_prose_and_versions_do_not_trip():
    rc, _ = run_cli(
        "Version 13.0.1 beats 5.2.1; the arc has four moves; see A1 and A2."
    )
    assert rc == 0


def test_module_entry_point_matches_cli():
    assert mod.find_local_citations("see TASKS.md:741 for it", None) != []
    assert mod.find_local_citations("no paths here at all", None) == []


def test_live_pilot_breach_is_detected():
    """The real breach the pilot disclosed (analyst B, 2026-09-19): a
    web-briefed analyst returned local evidence. The gate must catch the
    same shape."""
    breach = (
        "L1 `dotfiles/requirements.yml` (local) — declares community.general "
        "with no version key.\n"
        "L2 `TASKS.md` § Planned:741-747 (local) — queued task to pin both "
        "collections.\n"
        "L3 Topic tree (local) — dozens of tasks/*.yaml invoke "
        "community.general.homebrew.\n"
    )
    rc, out = run_cli(breach)
    assert rc == 1, out
    assert out.count("repo-relative file path") >= 2
