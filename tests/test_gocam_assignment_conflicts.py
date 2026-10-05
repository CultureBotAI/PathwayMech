"""Independent regressions for the root enzyme-assignment corrections."""

import importlib
import sys
from copy import deepcopy
from pathlib import Path

from pathwaymech.schema import validate_record

SCRIPT_DIR = str(Path(__file__).parents[1] / "scripts")
sys.path.insert(0, SCRIPT_DIR)
try:
    MODULE = importlib.import_module("review_gocam_assignment_conflicts")
finally:
    sys.path.remove(SCRIPT_DIR)


def record(rid, proteins, activities, pairs):
    return {
        "id": rid,
        "label": "Test pathway",
        "description": "Test curated assignments.",
        "pathway_type": "test",
        "taxa": [{"id": "NCBITaxon:559292", "label": "Saccharomyces cerevisiae S288C"}],
        "participants": [{"id": p, "label": p, "category": "protein"} for p in proteins],
        "reactions": [{"id": r, "label": r, "category": "molecular_activity"} for r in activities],
        "references": [{"id": rid, "title": "Native evidence fixture"}],
        "mechanistic_edges": [
            {
                "id": f"edge-{i}",
                "subject": s,
                "predicate": "enables",
                "object": o,
                "evidence": [{"reference_id": rid, "quote": "Inspected native assertion."}],
            }
            for i, (s, o) in enumerate(pairs)
        ],
    }


def test_assignment_reconciliation_retains_supported_routes_and_is_idempotent():
    bna3 = "SGD:S000003596"
    bna7 = "SGD:S000002836"
    lys4 = "SGD:S000002642"
    dehydration = "gomodel:RXN3O-1983"
    hydration = "gomodel:HOMOACONITATE-HYDRATION"
    str2 = "SGD:S000003891"
    records = {
        "l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde": record(
            "gomodel:YeastPathways_PWY-5651",
            [bna3, bna7],
            ["gomodel:ARYLFORMAMIDASE-RXN", "gomodel:BNA7-RXN"],
            [(bna3, "gomodel:ARYLFORMAMIDASE-RXN"), (bna7, "gomodel:BNA7-RXN")],
        ),
        "l-lysine-biosynthesis-iv": record(
            "gomodel:lysine",
            [lys4],
            [dehydration, hydration],
            [(lys4, dehydration), (lys4, hydration)],
        ),
        "homocysteine-and-cysteine-interconversion": record(
            "gomodel:interconversion",
            [str2],
            ["gomodel:RXN-721"],
            [(str2, "gomodel:RXN-721")],
        ),
    }
    identities = [("Q04066", "S000002836"), ("P39533", "S000003736"), ("P19414", "S000004295")]
    batch = {
        "results": [
            {
                "primaryAccession": acc,
                "uniProtKBCrossReferences": [{"database": "SGD", "id": sgd}],
            }
            for acc, sgd in identities
        ]
    }
    locations = {
        "results": [
            {
                "primaryAccession": acc,
                "comments": [
                    {"commentType": "FUNCTION"},
                    {
                        "commentType": "SUBCELLULAR LOCATION",
                        "subcellularLocations": [
                            {"location": {"id": "SL-0173", "value": "Mitochondrion"}}
                        ],
                    },
                ],
            }
            for acc, _ in identities[1:]
        ]
    }
    meta = {"url": "https://rest.uniprot.org/uniprotkb/stream?query=fixture"}
    primary = {
        "STR2.html": {
            "url": "https://pathway.yeastgenome.org/gene?id=YJR130C&orgid=YEAST",
            "sha256": MODULE.PRIMARY_SHA["STR2.html"],
        }
    }
    ledger = MODULE.curate(records, batch, meta, primary, locations, meta)
    bna = records["l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde"]
    assert not any(n["id"] == bna3 for n in bna["participants"])
    assert not any(n["id"] == "gomodel:ARYLFORMAMIDASE-RXN" for n in bna["reactions"])
    assert any(
        e["subject"] == bna7 and e["predicate"] == "enables" for e in bna["mechanistic_edges"]
    )
    lys = records["l-lysine-biosynthesis-iv"]
    assert {
        e["object"]
        for e in lys["mechanistic_edges"]
        if e["subject"] == lys4 and e["predicate"] == "enables"
    } == {hydration}
    assert {
        e["subject"]
        for e in lys["mechanistic_edges"]
        if e["object"] == dehydration and e["predicate"] == "enables"
    } == {"SGD:S000003736", "SGD:S000004295"}
    assert any(
        e["subject"] == "SGD:S000003736"
        and e["predicate"] == "located_in"
        and e["object"] == "GO:0005739"
        for e in lys["mechanistic_edges"]
    )
    assert not any(
        e["subject"] == dehydration and e["predicate"] == "occurs_in"
        for e in lys["mechanistic_edges"]
    )
    retained = records["homocysteine-and-cysteine-interconversion"]["mechanistic_edges"][0]
    assert retained["object"] == "gomodel:RXN-721"
    assert any(
        e["reference_id"] == str2 and "Reactions table" in e["source_locator"]
        for e in retained["evidence"]
    )
    assert len(ledger["superseded_edges"]) == 2
    for rec in records.values():
        validate_record(rec)
    first = deepcopy(records)
    MODULE.curate(records, batch, meta, primary, locations, meta)
    assert first == records
