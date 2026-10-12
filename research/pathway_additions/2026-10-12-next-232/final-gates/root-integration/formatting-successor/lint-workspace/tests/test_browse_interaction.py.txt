"""Execute the shipped browse script under a non-English casing locale."""
import re
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is needed to execute browser logic")
def test_shipped_search_matches_ascii_identifiers_in_any_locale(tmp_path):
    page = (Path(__file__).resolve().parents[1] / "pages/browse.html").read_text()
    scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
    assert len(scripts) == 1
    script = tmp_path / "browse.js"
    script.write_text(scripts[0])
    harness = Path(__file__).with_name("browse_interaction_harness.cjs")
    result = subprocess.run(["node", str(harness), str(script)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "Literal locale-independent search and reset passed" in result.stdout
