"""Execute the shipped graph controls and verify observable state transitions."""
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is needed to execute browser logic")
@pytest.mark.parametrize("scenario", [
    "zoom_and_fit",
    "zoom_limits",
    "directed_selection_preserves_graph",
    "clear_and_escape",
    "absent_or_invalid_graph",
])
def test_shipped_graph_interactions(scenario):
    root = Path(__file__).resolve().parents[1]
    script = root / "src/pathwaymech/assets/pathway-network.js"
    harness = Path(__file__).with_name("graph_interaction_harness.cjs")
    result = subprocess.run(
        ["node", str(harness), str(script), scenario],
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"Graph interaction passed: {scenario}" in result.stdout
