"""Replay the exact three redundant JSON-pointer corrections for issue 361."""

import copy
import datetime
import hashlib
import json
from pathlib import Path

import yaml

from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-195"
RAW = Path("/private/tmp/pathwaymech-next-195-evidence/menaquinol")
TARGET = ROOT / "data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml"
ARCHIVE = DOSSIER / "pre-pointer-review-inputs"
START = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


fix = json.loads((DOSSIER / "menaquinol-pointer-fix.json").read_text())
prior_path = ROOT / fix["prior_validation"]["path"]
assert digest(prior_path) == fix["prior_validation"]["sha256"]
previous = json.loads(prior_path.read_text())
assert previous["status"] == "passed"
assert digest(ARCHIVE / TARGET.name) == fix["initial_target_sha256"]
assert previous["target_sha256"] == fix["initial_target_sha256"]
assert digest(TARGET) == fix["final_target_sha256"]
old = yaml.safe_load((ARCHIVE / TARGET.name).read_text())
new = yaml.safe_load(TARGET.read_text())
expected = copy.deepcopy(old)
assert len(fix["changes"]) == 3
assert {c["edge_id"] for c in fix["changes"]} == {
    "menaquinol-edge-050",
    "menaquinol-edge-051",
    "menaquinol-edge-057",
}
source_checks = []
manifest = json.loads((DOSSIER / "menaquinol-source-manifest.json").read_text())
for change in fix["changes"]:
    edge = next(e for e in expected["mechanistic_edges"] if e["id"] == change["edge_id"])
    evidence = next(v for v in edge["evidence"] if v["reference_id"] == change["reference_id"])
    assert evidence["source_locator"] == change["before"]
    assert change["before"] == "/comments/2/cofactors; /comments/2/note"
    assert change["after"] == "/comments/2/cofactors"
    evidence["source_locator"] = change["after"]
    accession = change["reference_id"].split(":")[1]
    path = RAW / f"uniprot-{accession}.json"
    source = next(s for s in manifest["sources"] if s["raw_path"] == str(path))
    assert digest(path) == source["sha256"]
    data = json.loads(path.read_text())
    assert data["primaryAccession"] == accession
    comment = data["comments"][2]
    assert comment["commentType"] == "COFACTOR" and "note" not in comment
    cofactor = next(
        c for c in comment["cofactors"] if c["cofactorCrossReference"]["id"] == edge["object"]
    )
    expected_evidence = (
        {"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_01659"}
        if accession == "P17109"
        else {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "10978150"}
    )
    assert expected_evidence in cofactor["evidences"]
    source_checks.append(
        {
            "edge_id": edge["id"],
            "raw_path": str(path),
            "sha256": digest(path),
            "verified_cofactor": cofactor,
            "absent_optional_pointer": "/comments/2/note",
        }
    )
assert expected == new
for stem in [
    "source-manifest",
    "source-projection",
    "protein-projection",
    "identifiers",
    "authority-delta",
]:
    assert json.loads((DOSSIER / f"menaquinol-{stem}.json").read_text())["target_sha256"] == digest(
        TARGET
    )
record = validate_record(new)
old_record = validate_record(old)
assert strict_errors([TARGET], ROOT) == []
out = RAW / "kgx-after-361"
write_kgx([record], out)
exported = kgx_edges([record])
old_exported = kgx_edges([old_record])
assert len(exported) == 85 and len(kgx_nodes([record])) == 56
assert kgx_nodes([old_record]) == kgx_nodes([record])
assert sum(len(e["evidence"]) for e in new["mechanistic_edges"]) == 181
for edge, row, old_row in zip(new["mechanistic_edges"], exported, old_exported, strict=True):
    assert json.loads(row.evidence) == edge["evidence"]
    before = vars(old_row).copy()
    after = vars(row).copy()
    before.pop("evidence")
    after.pop("evidence")
    assert before == after
report = {
    "status": "passed",
    "started_at": START,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "command": (
        "UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 "
        ".venv/bin/python research/pathway_additions/2026-10-11-next-195/"
        "menaquinol-pointer-replay.py"
    ),
    "scope": (
        "Author replay of exactly three source-locator removals for #361. "
        "No independent scientific review or repeat full suite claimed."
    ),
    "prior_focused_replay": fix["prior_validation"],
    "complete_chemistry_replay": previous["complete_chemistry_replay"],
    "large_authorities_rehashed_in_this_focused_run": False,
    "preserved_chemistry": previous["preserved_chemistry"],
    "native_boundary_complete": previous["native_boundary_complete"],
    "source_checks": source_checks,
    "parsed_record_delta": fix["changes"],
    "counts": previous["counts"],
    "kgx_non_evidence_fields_and_nodes_unchanged": True,
    "kgx": {p.name: digest(p) for p in out.glob("*.tsv")},
    "helper_sha256": digest(__file__),
}
(DOSSIER / "menaquinol-validation.json").write_text(json.dumps(report, indent=2) + "\n")
print(
    json.dumps(
        {
            "status": report["status"],
            "target_sha256": report["target_sha256"],
            "counts": report["counts"],
        }
    )
)
