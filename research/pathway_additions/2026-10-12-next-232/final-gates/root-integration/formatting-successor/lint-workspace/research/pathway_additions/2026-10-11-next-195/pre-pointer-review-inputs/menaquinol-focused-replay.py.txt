"""Replay citation-only #360 changes over the already replayed complete chemistry."""

import copy
import datetime
import hashlib
import json
from pathlib import Path

import yaml
from lxml import etree as ET

from pathwaymech.kgx import kgx_edges, kgx_nodes, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
DOSSIER = ROOT / "research/pathway_additions/2026-10-11-next-195"
RAW = Path("/private/tmp/pathwaymech-next-195-evidence/menaquinol")
TARGET = ROOT / "data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml"
ARCHIVE = DOSSIER / "intermediate-review-inputs/menaquinol"
START = datetime.datetime.now(datetime.UTC).isoformat()


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


fix = json.loads((DOSSIER / "menaquinol-structure-context-fix.json").read_text())
previous = json.loads((ARCHIVE / "menaquinol-validation.json").read_text())
assert previous["status"] == "passed"
assert digest(ARCHIVE / "menaquinol-validation.json") == fix["full_replay_basis"]["sha256"]
assert previous["target_sha256"] == fix["intermediate_target_sha256"]
assert digest(ARCHIVE / TARGET.name) == previous["target_sha256"]
assert digest(TARGET) == fix["final_target_sha256"]
old = yaml.safe_load((ARCHIVE / TARGET.name).read_text())
new = yaml.safe_load(TARGET.read_text())
expected = copy.deepcopy(old)
edge = next(x for x in expected["mechanistic_edges"] if x["id"] == "menaquinol-edge-059")
for change in fix["narrowed_assembly_evidence"]:
    assert change["before"] in edge["evidence"]
    edge["evidence"][edge["evidence"].index(change["before"])] = change["after"]
edge["evidence"].extend(fix["added_primary_evidence"])
expected["references"].append(fix["added_reference"])
assert expected == new
# The only difference is exact attribution; all chemistry and biological IDs are identical.
record = validate_record(new)
assert strict_errors([TARGET], ROOT) == []
manifest = json.loads((DOSSIER / "menaquinol-source-manifest.json").read_text())
for name in [
    "source-manifest",
    "source-projection",
    "protein-projection",
    "identifiers",
    "authority-delta",
]:
    assert json.loads((DOSSIER / f"menaquinol-{name}.json").read_text())["target_sha256"] == digest(
        TARGET
    )
checks = []
for name, anchors in [
    (
        "PMC6653581.html",
        {
            "P17": ["Wild-type", "E. coli", "analogue", "6NJ0"],
            "P32": ["wild-type", "6NJ0", "R195K", "5C5H"],
        },
    ),
    ("PMC4624480.html", {"P11": ["R195K", "OSB-AMS"], "P23": ["R195K", "OSB-AMS", "5C5H"]}),
]:
    path = RAW / name
    body = next(x for x in manifest["sources"] if x["raw_path"] == str(path))
    assert digest(path) == body["sha256"]
    tree = ET.HTML(path.read_bytes())
    for anchor, words in anchors.items():
        elements = tree.xpath(f'//*[@id="{anchor}"]')
        assert len(elements) == 1
        text = " ".join(" ".join(elements[0].itertext()).split())
        assert all(word in text for word in words), (name, anchor)
        checks.append({"path": str(path), "sha256": body["sha256"], "anchor": anchor})
assert (
    digest(manifest["reference_artifacts"]["PMID:30912442"])
    == fix["added_reference"]["source_sha256"]
)
for pdb in ["6NJ0", "5C5H"]:
    path = RAW / f"rcsb-{pdb}-assembly-1.json"
    data = json.loads(path.read_text())
    assembly = data["pdbx_struct_assembly"]
    assert assembly["oligomeric_count"] == 1
    assert "author" in assembly["details"] and assembly["method_details"] == "PISA"
    reference = next(r for r in new["references"] if r["id"] == f"DOI:10.2210/pdb{pdb}/pdb")
    assert digest(path) == reference["source_sha256"]
    checks.append({"path": str(path), "sha256": digest(path), "assembly": assembly})
# Existing #357 source headings/anchors still resolve after the new evidence addition.
for change in json.loads((DOSSIER / "menaquinol-provenance-fix.json").read_text())["changes"]:
    path = Path(change["raw_path"])
    assert digest(path) == change["raw_sha256"]
    tree = ET.parse(str(path)) if path.suffix == ".xml" else ET.HTML(path.read_bytes())
    e = next(e for e in new["mechanistic_edges"] if e["id"] == change["edge_id"])
    v = next(v for v in e["evidence"] if v["reference_id"] == change["reference_id"])
    assert v["source_locator"] == change["verified_replacement_locator"]
    for anchor in change["native_anchor_checks"]:
        elements = tree.xpath(f'//*[@{anchor["attribute"]}="{anchor["value"]}"]')
        assert elements
        text = " ".join(" ".join(elements[0].itertext()).split())
        if anchor["expected_text"]:
            assert anchor["expected_text"].casefold() in text.casefold()
# Actual exporter proves all final evidence survives, with the graph shape unchanged.
out = RAW / "kgx-final"
write_kgx([record], out)
exported = kgx_edges([record])
assert len(exported) == 85 and len(kgx_nodes([record])) == 56
assert sum(len(e["evidence"]) for e in new["mechanistic_edges"]) == 181
for edge, row in zip(new["mechanistic_edges"], exported, strict=True):
    assert json.loads(row.evidence) == edge["evidence"]
report = {
    "status": "passed",
    "started_at": START,
    "finished_at": datetime.datetime.now(datetime.UTC).isoformat(),
    "target": str(TARGET.relative_to(ROOT)),
    "target_sha256": digest(TARGET),
    "command": (
        "UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 "
        ".venv/bin/python research/pathway_additions/2026-10-11-next-195/"
        "menaquinol-focused-replay.py"
    ),
    "scope": (
        "Focused post-360 author replay, not independent scientific review. "
        "Exact semantic comparison proves only evidence attribution differs "
        "from the fully replayed intermediate record."
    ),
    "complete_chemistry_replay": fix["full_replay_basis"],
    "large_authorities_rehashed_in_this_focused_run": False,
    "preserved_chemistry": {"reactions": 10, "chemical_sides": 43, "atom_charge_balances": 10},
    "native_boundary_complete": previous["native_boundary_complete"],
    "new_context_checks": checks,
    "counts": {
        "participants": 44,
        "reactions": 10,
        "edges": 85,
        "evidence": 181,
        "nodes": 56,
        "references": 68,
    },
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
