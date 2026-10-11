"""Focused author replay of six supplemental row-attribution corrections.

Full chemistry was unchanged and is covered by the immutable v1 author replay.
This replay reopens primary bodies and tests each historical misattribution,
then independently exports the unchanged current record for exact KGX parity.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import yaml
from lxml import html

from pathwaymech.kgx import LOCAL_PREDICATE_CURIES, write_kgx
from pathwaymech.schema import validate_record
from pathwaymech.strict import strict_errors

ROOT = Path.cwd()
D = ROOT / "research/pathway_additions/2026-10-11-next-209"
RAW = Path("/private/tmp/pathwaymech-next-209-evidence/dchb")
TARGET = ROOT / "data/pathways/dicarboxylate-hydroxybutyrate-cycle.yaml"
ROWS = [(0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (1, 9)]
TARGET_HASH = "bf5316958e94eae4e2e09a864dca8e45d8997b041d7e26c991c9633f24449209"
V1_HASH = "8d3640f46bd1d8d6882b6ee8b9d1523a84368ab9f31d6af2f79a9ab5af178b5f"


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def scoped_assertions(projection):
    for a, b in ROWS:
        row = projection["primary_assertions"][a]["rows"][b]
        statement = row["assertion"].lower()
        if a == 0:
            assert "extract" in statement
            assert not any(term in statement for term in ["tneu_", "table 1", "locus", "subunit"])
        else:
            assert "domain" in statement and "similarity" in statement and "candidate" in statement
            assert all(locus in statement for locus in ["msed_0399", "tneu_0541", "igni_1058"])
            assert not any(term in statement for term in ["purified", "recombinant", "tested"])
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--projection", type=Path, default=D / "dchb-source-projection-successor-v2.json"
    )
    ap.add_argument("--output", type=Path, default=RAW / "replay-result-successor-v2.json")
    args = ap.parse_args()
    started = datetime.now(UTC).isoformat()
    v1_path = D / "dchb-source-projection-successor.json"
    assert digest(v1_path) == V1_HASH
    assert digest(TARGET) == TARGET_HASH
    old = read(v1_path)
    new = read(args.projection)
    reset = copy.deepcopy(new)
    deltas = []
    for a, b in ROWS:
        before = old["primary_assertions"][a]["rows"][b]["assertion"]
        after = new["primary_assertions"][a]["rows"][b]["assertion"]
        assert before != after
        reset["primary_assertions"][a]["rows"][b]["assertion"] = before
        deltas.append(
            {
                "pointer": f"/primary_assertions/{a}/rows/{b}/assertion",
                "before": before,
                "after": after,
            }
        )
    assert reset == old
    assert new["target_sha256"] == TARGET_HASH
    assert scoped_assertions(new)
    rejected = []
    for a, b in ROWS:
        trial = copy.deepcopy(new)
        trial["primary_assertions"][a]["rows"][b]["assertion"] = old["primary_assertions"][a][
            "rows"
        ][b]["assertion"]
        try:
            scoped_assertions(trial)
        except AssertionError:
            rejected.append([a, b])
        else:
            raise AssertionError("Historical assertion not rejected")
    doc = yaml.safe_load(TARGET.read_text())
    refs = {r["id"]: r for r in doc["references"]}
    spans = 0
    primary_inputs = []
    for source in new["primary_assertions"]:
        path = Path(new["reference_original_paths"][source["reference"]])
        assert digest(path) == refs[source["reference"]]["source_sha256"]
        primary_inputs.append({"path": str(path), "sha256": digest(path)})
        tree = html.fromstring(path.read_bytes())
        for row in source["rows"]:
            found = tree.xpath(row["xpath"])
            assert len(found) == 1
            text = " ".join(" ".join(found[0].itertext()).split())
            assert hashlib.sha256(text.encode()).hexdigest() == row["text_sha256"]
            spans += 1
    record = validate_record(doc)
    assert not strict_errors([TARGET], ROOT)
    exported = RAW / "kgx-replay-successor-v2"
    exported.mkdir(exist_ok=True)
    write_kgx([record], exported)
    nodes = list(csv.DictReader((exported / "nodes.tsv").open(), delimiter="\t"))
    edges = list(csv.DictReader((exported / "edges.tsv").open(), delimiter="\t"))
    assert len(nodes) == 66 and len(edges) == 116
    assert sum(len(e["evidence"]) for e in doc["mechanistic_edges"]) == 234
    for source, output in zip(doc["mechanistic_edges"], edges, strict=True):
        assert (
            source["subject"],
            LOCAL_PREDICATE_CURIES[source["predicate"]],
            source["object"],
        ) == (output["subject"], output["predicate"], output["object"])
        assert json.loads(output["evidence"]) == source["evidence"]
    kgx = {}
    for name in ["nodes.tsv", "edges.tsv"]:
        assert digest(exported / name) == digest(RAW / "kgx-replay-successor" / name)
        kgx[name] = digest(exported / name)
    assert digest(TARGET) == TARGET_HASH and digest(v1_path) == V1_HASH
    result = {
        "status": "passed",
        "scope": (
            "Focused author supplemental-attribution replay; "
            "not independent review or a repeated full chemistry replay"
        ),
        "started_at": started,
        "finished_at": datetime.now(UTC).isoformat(),
        "target_sha256": TARGET_HASH,
        "projection_sha256": digest(args.projection),
        "v1_projection_preserved": V1_HASH,
        "prior_complete_chemistry_replay": {
            "path": str(D / "dchb-validation-successor.json"),
            "sha256": digest(D / "dchb-validation-successor.json"),
        },
        "exact_six_assertion_deltas": deltas,
        "historical_rows_individually_rejected": rejected,
        "all_primary_spans_reopened": spans,
        "primary_originals_rehashed": primary_inputs,
        "schema_and_strict": "passed",
        "actual_kgx": {"nodes": 66, "edges": 116, "evidence": 234, "unchanged_hashes": kgx},
        "helper_sha256": digest(Path(__file__)),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps({k: v for k, v in result.items() if k != "exact_six_assertion_deltas"}, indent=2)
    )


if __name__ == "__main__":
    main()
