"""Exercise shell argument boundaries through the actual just recipes."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.parametrize("recipe", [
    "import-biopax", "import-dbcan-pul", "import-dram", "import-seed-subsystems",
])
def test_local_source_recipe_passes_arguments_literally(tmp_path: Path, recipe: str) -> None:
    just = shutil.which("just")
    if just is None:
        pytest.skip("just is required for executable recipe regression")
    # A fake uv isolates shell forwarding from dependencies and network access.
    uv = tmp_path / "uv"
    uv.write_text(
        f"#!{sys.executable}\nimport json, sys\nprint(json.dumps(sys.argv[1:]))\n"
    )
    uv.chmod(0o755)
    args = ["a directory/source;literal.xlsx", "--sha256", "a" * 64]
    if recipe == "import-biopax":
        args = ["PathBank", *args, "--source-version", "archive; member with spaces.owl"]
    result = subprocess.run(
        [just, "--justfile", str(Path("justfile").resolve()), recipe, *args],
        env={**os.environ, "PATH": str(tmp_path) + os.pathsep + os.environ["PATH"]},
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == ["run", "pathwaymech-" + recipe, *args]
