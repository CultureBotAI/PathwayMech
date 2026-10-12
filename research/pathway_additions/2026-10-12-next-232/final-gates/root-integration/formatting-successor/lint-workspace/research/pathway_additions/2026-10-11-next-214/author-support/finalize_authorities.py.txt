"""Complete external canonical namespace coverage after narrow original extraction."""

import hashlib
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

from pathwaymech.identifiers import identifier_errors

B = Path(__file__).resolve().parent
D = B / "draft"
S = B / "authority-sandbox"
R = Path("/private/tmp/pathwaymech-next-211-20261011")
F = Path("/private/tmp/pathwaymech-staphyloferrin-a-followup-20261011")


def sha(p):
    with Path(p).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


reports = []
for name in ["ontology", "sources"]:
    p = S / "data/identifier_authorities" / (name + ".json")
    fresh = json.loads(p.read_text())
    old = json.loads((R / "data/identifier_authorities" / (name + ".json")).read_text())
    old["sources"].update(fresh["sources"])
    old["terms"].update(fresh["terms"])
    p.write_text(json.dumps(old, indent=2) + "\n")
    if name == "ontology":
        for key, metadata in fresh["sources"].items():
            if key.startswith("staphyloferrin-a-"):
                prefix = key.removeprefix("staphyloferrin-a-").removesuffix("-original")
                file = {"CHEBI": "chebi", "RHEA": "rhea", "NCBITaxon": "ncbitaxon"}[prefix]
                reports.append(
                    {
                        "prefix": prefix,
                        "path": "/private/tmp/pathwaymech-curation-authorities/" + file + ".db",
                        "sha256": metadata["sha256"],
                        "source_metadata": metadata,
                        "selected_ids": sorted(
                            cid for cid, t in fresh["terms"].items() if t["source"] == key
                        ),
                        "canonical_original_extractor": True,
                    }
                )
shutil.copyfile(
    D / "staphyloferrin-a-biosynthesis.yaml",
    S / ("data/pathways/staphyloferrin-a-biosynthesis.yaml"),
)
errors = identifier_errors(S)
assert not errors, errors
entries = json.loads((S / "source-manifest.json").read_text())
originals = json.loads((F / "authority-inputs.json").read_text())["inputs"]
for e, x in zip(entries, originals, strict=True):
    e["raw_path"] = x["path"]
    e["native_terms"] = x["terms"]
selected = json.loads((D / "staphyloferrin-a-identifiers.json").read_text())
ids = [selected["record"]] + selected["participants"] + selected["taxa"] + selected["reactions"]
receipt = {
    "created_at": datetime.now(UTC).isoformat(),
    "status": "passed",
    "scope": (
        "Actual canonical original source/ontology extraction; unchange"
        "d full namespace policy checked on final exact external draft."
        " Baseline namespace authorities retained in sandbox; maintaine"
        "d files untouched."
    ),
    "target_sha256": sha(D / "staphyloferrin-a-biosynthesis.yaml"),
    "source_manifest_additions": entries,
    "ontology_inputs": reports,
    "named_ids": sorted(ids),
    "sandbox": str(S),
    "identifier_errors": errors,
    "reference_code_head": "5cf4d2578da6b61a49f8c0f9886229b8c1369c91",
    "policy_sha256": sha(R / "conf/identifier_policy.yaml"),
    "initial_attempt": (
        "Original extraction succeeded; the first one-record-only names"
        "pace snapshot failed because unchanged global policy requires "
        "every configured namespace. Existing independent baseline name"
        "space entries were retained; no exception or waiver."
    ),
    "root_integration_pending": True,
}
(D / "staphyloferrin-a-authority-proposal.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(
    json.dumps(
        {
            "status": "passed",
            "named_ids": len(ids),
            "fresh_original_ontology_groups": len(reports),
            "target_sha256": receipt["target_sha256"],
        },
        indent=2,
    )
)
