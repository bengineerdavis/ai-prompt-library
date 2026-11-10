#!/usr/bin/env python3
"""Exercise the shipped Skillet freshness adapter through its public CLI."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "scripts" / "check_skillet_freshness.py"


def run_adapter(skill_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ADAPTER), str(skill_dir)],
        capture_output=True,
        text=True,
        check=False,
    )


class FreshnessAdapterTest(unittest.TestCase):
    def test_valid_skill_passes(self) -> None:
        result = run_adapter(ROOT / "skills" / "research")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_stale_skill_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            skill = Path(temporary)
            (skill / "spec.md").write_text(
                "# Stale Fixture\n\n"
                "## Intent\n\n"
                "Exercise a stale render.\n\n"
                "## Triggers\n\n"
                "- **SHOULD** trigger for this fixture.\n\n"
                "## Behaviors\n\n"
                "### Behavior: Detect a stale render\n\n"
                "The agent SHALL detect the stale render.\n\n"
                "#### Scenario: A stale render\n\n"
                "- **WHEN** the fixture is checked\n"
                "- **THEN** the adapter reports the stale render.\n"
            )
            (skill / "SKILL.md").write_text(
                "---\n"
                "name: stale\n"
                "description: Deliberately stale fixture.\n"
                'spec_hash: "000000000000"\n'
                "---\n"
            )
            result = run_adapter(skill)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("re-render", result.stdout + result.stderr)

    def test_missing_skill_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = run_adapter(Path(temporary))
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
