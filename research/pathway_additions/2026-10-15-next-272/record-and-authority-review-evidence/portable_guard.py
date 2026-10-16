"""Run a retained verifier while denying reads from unrelated temporary owners."""

import argparse
import os
import runpy
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("directory", type=Path)
parser.add_argument("mode", choices=["retain", "manifests"])
args = parser.parse_args()
base = args.directory.resolve()
allowed = [str(base), sys.prefix]


def audit(event, values):
    if event not in {"open", "os.listdir", "os.scandir"} or not values:
        return
    value = values[0]
    if not isinstance(value, (str, bytes, os.PathLike)):
        return
    path = os.path.abspath(os.fsdecode(value))
    if not path.startswith("/private/tmp/pathwaymech-"):
        return
    if any(path == prefix or path.startswith(prefix + os.sep) for prefix in allowed):
        return
    raise RuntimeError(f"Portable verification attempted an external temporary-owner read: {path}")


sys.addaudithook(audit)
if args.mode == "retain":
    script = base / "retain.py"
    sys.argv = [str(script), "verify", "--output", str(base)]
else:
    script = base / "check_archived_manifests.py"
    sys.argv = [str(script), str(base)]
runpy.run_path(str(script), run_name="__main__")
