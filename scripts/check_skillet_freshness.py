#!/usr/bin/env python3
"""Turn Skillet's stale-render status into a failing check.

Skillet status deliberately exits 0 when the next authoring action is needed;
pre-commit needs a failure for that state. Skillet remains the sole owner of
hash calculation and staleness semantics.
"""

import json
import subprocess
import sys


def main() -> int:
    skill_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    result = subprocess.run(
        [
            "npx",
            "-y",
            "@sentry/skillet@latest",
            "status",
            skill_dir,
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        sys.stderr.write(result.stderr or result.stdout)
        return result.returncode
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        sys.stderr.write("Skillet status did not return valid JSON.\n")
        return 1
    if report["skill"]["stale"]:
        print(report["next"], file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
