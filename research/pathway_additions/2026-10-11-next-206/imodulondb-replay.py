"""Replay this cohort's dataset inventory from its retained original responses."""

import hashlib
import importlib.util
import json
import sys
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


directory = Path(__file__).resolve().parent
inventory_path = directory / "imodulondb-dataset-inventory.json"
applicability_path = directory / "imodulondb-applicability.json"
availability_path = directory / "imodulondb-runner-availability.json"
inventory = json.loads(inventory_path.read_text())
applicability = json.loads(applicability_path.read_text())
availability = json.loads(availability_path.read_text())
module_path = Path(availability["fallback_module"])
assert sha256(module_path) == inventory["module_sha256"]
assert sha256(module_path) == availability["fallback_module_sha256"]
assert sha256(inventory_path) == applicability["inventory_sha256"]

bodies = {}
for original in inventory["originals"]:
    path = Path(original["path"])
    assert sha256(path) == original["sha256"]
    assert path.stat().st_size == original["bytes"]
    bodies[original["url"]] = json.loads(path.read_bytes())

spec = importlib.util.spec_from_file_location("native_imodulondb", module_path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
client = module.ImodulonDBClient(transport=lambda url: bodies[url])
rows = json.loads(json.dumps([asdict(row) for row in client.organism_datasets()]))
assert rows == inventory["datasets"]
assert len(rows) == applicability["organisms_returned"]
assert sum(len(row["datasets"]) for row in rows) == applicability["datasets_returned"]
names = {row["name"].lower() for row in rows}
assert all("metallosphaera" not in name and "chloroflexus" not in name for name in names)
assert "sulfolobus acidocaldarius" in names

report = {
    "status": "passed",
    "checked_at": datetime.now(UTC).isoformat(),
    "script_sha256": sha256(Path(__file__)),
    "module_sha256": sha256(module_path),
    "inputs": {
        path.name: sha256(path)
        for path in [inventory_path, applicability_path, availability_path]
    },
    "method": (
        "The unchanged source client re-parses hash-verified original response bodies. "
        "The replay transport accepts only retained URLs and performs no network calls. "
        "Inventory equality and exact organism coverage are checked."
    ),
    "limits": (
        "Verifies dataset projection and the stated coverage assessment. "
        "It does not establish biological absence or gene/pathway membership. "
        "Reassess if the experimental organism scope changes."
    ),
}
(directory / "imodulondb-offline-replay.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report))
