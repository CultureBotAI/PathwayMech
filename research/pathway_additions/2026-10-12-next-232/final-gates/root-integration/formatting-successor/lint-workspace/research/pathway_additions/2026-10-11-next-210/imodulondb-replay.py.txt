"""Recheck dated hvKP1 dataset coverage without rewriting historical receipts."""

import argparse
import hashlib
import importlib.util
import json
import sys
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

import yaml


def digest(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "replay.json"
    if output.exists():
        parser.error("Choose a new output directory; existing receipts are preserved.")

    started = datetime.now(UTC).isoformat()
    directory = Path(__file__).resolve().parent
    root = directory.parents[2]
    prior = directory.parent / "2026-10-11-next-209"
    target = root / "data/pathways/aerobactin-biosynthesis.yaml"
    record = yaml.safe_load(target.read_text())
    assert record["id"] == "GO:0019270"
    assert record["taxa"] == [
        {"id": "NCBITaxon:1267897", "label": "Klebsiella pneumoniae hvKP1"}
    ]
    inventory_path = prior / "imodulondb-dataset-inventory.json"
    runner_path = prior / "imodulondb-runner-availability.json"
    assert digest(inventory_path) == (
        "d84677b8bd4bcb4114f4ae918186f28fe5faceba702fc195e62296f259c42fce"
    )
    assert digest(runner_path) == (
        "e478aa48f52e3a7a167361c134f0d13e4cf765eb147ed607bc0052a90956d9c3"
    )
    inventory = json.loads(inventory_path.read_text())
    runner = json.loads(runner_path.read_text())
    module_path = Path(runner["fallback_module"])
    assert digest(module_path) == inventory["module_sha256"]
    assert digest(module_path) == runner["fallback_module_sha256"]
    bodies = {}
    for source in inventory["originals"]:
        path = Path(source["path"])
        assert digest(path) == source["sha256"]
        assert path.stat().st_size == source["bytes"]
        bodies[source["url"]] = json.loads(path.read_bytes())

    spec = importlib.util.spec_from_file_location("retained_imodulondb", module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    requests = []

    def transport(url):
        requests.append(url)
        return bodies[url]

    client = module.ImodulonDBClient(transport=transport)
    rows = json.loads(json.dumps([asdict(row) for row in client.organism_datasets()]))
    assert rows == inventory["datasets"]
    assert len(rows) == 20
    assert sum(len(row["datasets"]) for row in rows) == 28
    raw = bodies["https://imodulondb.org/api/datasets"]
    assert len(raw) == len(rows)
    terms = ["klebsiella", "hvkp1", "1267897", "k_pneumoniae"]
    hits = {term: [row for row in raw if term in json.dumps(row).lower()] for term in terms}
    assert all(not found for found in hits.values())
    ambiguous = [row for row in raw if "pneumoniae" in json.dumps(row).lower()]
    assert len(ambiguous) == 1
    assert ambiguous[0]["name"] == "Streptococcus pneumoniae"
    assert ambiguous[0]["datasets"] == ["precise718"]
    original = directory / "imodulondb-original-replay.py.txt"
    assert digest(original) == (
        "903a14c108b34eb625fd21cd0b5e525814036efaa8c11b0117900562506f2025"
    )
    old_assessment = directory / "imodulondb-applicability.json"
    assert digest(old_assessment) == (
        "21b4bdfda652179a13ad15149232fc5f67ba677247fe197d1ad703ab4b5864fb"
    )
    assessment = json.loads(old_assessment.read_text())
    assert hits == assessment["matching_native_objects_by_term"]
    assert ambiguous == assessment["pneumoniae_name_disambiguation"]["matches"]
    report = {
        "status": "passed",
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "record_sha256": digest(target),
        "script_sha256": digest(Path(__file__)),
        "original_script_sha256": digest(original),
        "assessment_sha256": digest(old_assessment),
        "inventory_observed_at": inventory["checked_at"],
        "network_requests": 0,
        "replayed_urls": requests,
        "organisms": len(rows),
        "datasets": sum(len(row["datasets"]) for row in rows),
        "matching_native_objects_by_term": hits,
        "pneumoniae_disambiguation": ambiguous,
        "inputs": {
            str(path): digest(path) for path in [inventory_path, runner_path, module_path]
        },
        "limits": assessment["limits"],
    }
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))


if __name__ == "__main__":
    main()
