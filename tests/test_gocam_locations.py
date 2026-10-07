"""Source-role acceptance checks for the bounded yeast compartment review."""

from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location(
    "review_gocam_locations", SCRIPTS / "review_gocam_locations.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def protein(accession="PTEST", location="Mitochondrion", location_id="SL-0173"):
    return {
        "primaryAccession": accession,
        "organism": {"taxonId": 559292},
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "uniProtKBCrossReferences": [{"database": "SGD", "id": "S000000001"}],
        "comments": [
            {
                "commentType": "SUBCELLULAR LOCATION",
                "subcellularLocations": [
                    {
                        "location": {
                            "value": location,
                            "id": location_id,
                            "evidences": [{"evidenceCode": "ECO:0000250"}],
                        }
                    }
                ],
                "note": {"texts": [{"value": "Location inferred by similarity."}]},
            }
        ],
    }


def record():
    return {
        "id": "gomodel:test",
        "label": "test",
        "description": "Test pathway.",
        "pathway_type": "biosynthesis",
        "taxa": [{"id": "NCBITaxon:559292", "label": "yeast"}],
        "participants": [
            {"id": "SGD:S000000001", "label": "enzyme", "category": "protein"},
            {"id": "GO:0005829", "label": "cytosol", "category": "cellular_component"},
        ],
        "reactions": [{"id": "gomodel:r", "label": "activity"}],
        "references": [{"id": "gomodel:test", "title": "Native model"}],
        "mechanistic_edges": [
            {
                "id": "enable",
                "subject": "SGD:S000000001",
                "predicate": "enables",
                "object": "gomodel:r",
                "evidence": [
                    {
                        "reference_id": "gomodel:test",
                        "source_assertion": "The protein enables the activity.",
                        "source_locator": "/facts/0",
                    }
                ],
            },
            {
                "id": "location",
                "subject": "gomodel:r",
                "predicate": "occurs_in",
                "object": "GO:0005829",
                "evidence": [
                    {
                        "reference_id": "gomodel:test",
                        "source_assertion": "The source places the activity in cytosol.",
                        "source_locator": "/facts/1",
                    }
                ],
            },
        ],
    }


PROVENANCE = {"url": "https://example.org/pinned-locations.json", "sha256": "a" * 64}
LABELS = {"GO:0005739": "mitochondrion", "GO:0005737": "cytoplasm", "GO:0005829": "cytosol"}


def test_physical_location_does_not_automatically_become_activity_location():
    value = record()
    proteins, _ = MODULE.protein_index({"results": [protein()]})
    report = MODULE.curate(value, proteins, PROVENANCE, LABELS, {})
    triples = {(e["subject"], e["predicate"], e["object"]) for e in value["mechanistic_edges"]}
    assert ("SGD:S000000001", "located_in", "GO:0005739") in triples
    assert not any(e["predicate"] == "occurs_in" for e in value["mechanistic_edges"])
    assert report["excluded_source_edges"][0]["edge"]["id"] == "location"
    physical = next(e for e in value["mechanistic_edges"] if e["predicate"] == "located_in")
    assert "ECO:0000250" in physical["description"]
    assert "inferred by similarity" in physical["description"]
    assert "sha256=" in physical["evidence"][0]["source_locator"]


def test_cytoplasmic_isoenzyme_preserves_native_cytosolic_activity():
    value = record()
    p1 = protein()
    p2 = protein("POTHER", "Cytoplasm", "SL-0086")
    p2["uniProtKBCrossReferences"][0]["id"] = "S000000002"
    value["participants"].append(
        {"id": "SGD:S000000002", "label": "alternative", "category": "protein"}
    )
    enable = copy.deepcopy(value["mechanistic_edges"][0])
    enable.update(id="enable2", subject="SGD:S000000002")
    value["mechanistic_edges"].append(enable)
    proteins, _ = MODULE.protein_index({"results": [p1, p2]})
    report = MODULE.curate(value, proteins, PROVENANCE, LABELS, {})
    assert not report["excluded_source_edges"]
    edge = next(e for e in value["mechanistic_edges"] if e["predicate"] == "occurs_in")
    assert "does not place every isoenzyme" in edge["description"]


def test_explicit_function_places_activity_and_keeps_distinct_reference_representation():
    value = record()
    p = protein("P36013")
    p["comments"].append(
        {
            "commentType": "FUNCTION",
            "texts": [
                {
                    "value": "NAD-dependent mitochondrial malic enzyme "
                    "that converts malate to pyruvate."
                }
            ],
        }
    )
    value["references"].append(
        {
            "id": "UniProtKB:P36013",
            "title": "Older cofactor representation",
            "url": "https://example.org/cofactors",
            "source_sha256": "b" * 64,
        }
    )
    proteins, _ = MODULE.protein_index({"results": [p]})
    MODULE.curate(value, proteins, PROVENANCE, LABELS, {})
    edge = next(e for e in value["mechanistic_edges"] if e["predicate"] == "occurs_in")
    assert edge["object"] == "GO:0005739"
    assert "/comments/1/texts/0" in edge["evidence"][0]["source_locator"]
    assert PROVENANCE["url"] in edge["evidence"][0]["source_locator"]
    assert (
        next(r for r in value["references"] if r["id"] == "UniProtKB:P36013")["source_sha256"]
        == "b" * 64
    )


def test_ambiguous_identity_is_not_joined_by_label():
    p1, p2 = protein(), protein("POTHER")
    proteins, ambiguous = MODULE.protein_index({"results": [p1, p2]})
    assert "SGD:S000000001" in ambiguous
    assert "SGD:S000000001" not in proteins
    value = record()
    report = MODULE.curate(value, proteins, PROVENANCE, LABELS, {})
    assert not report["excluded_source_edges"]
    assert not any(e["predicate"] == "located_in" for e in value["mechanistic_edges"])


def test_cytoplasmic_actin_patch_is_not_a_conflicting_organelle():
    value = record()
    p = protein(location="Cytoplasm, cytoskeleton, actin patch", location_id="SL-0008")
    proteins, _ = MODULE.protein_index({"results": [p]})
    report = MODULE.curate(
        value, proteins, PROVENANCE, {**LABELS, "GO:0030479": "actin cortical patch"}, {}
    )
    assert not report["excluded_source_edges"]
    assert any(
        e["predicate"] == "occurs_in" and e["object"] == "GO:0005829"
        for e in value["mechanistic_edges"]
    )
