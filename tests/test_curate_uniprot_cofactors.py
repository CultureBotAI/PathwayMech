import hashlib
import io
import json
import tarfile
from copy import deepcopy
from pathlib import Path

import pytest

from scripts.curate_uniprot_cofactors import (
    caution_digest,
    curate,
    identifier_index,
    native_identifier_mappings,
)


def fixture():
    record = {
        "id": "gomodel:test",
        "label": "test",
        "description": "test",
        "pathway_type": "test",
        "taxa": [],
        "reactions": [],
        "participants": [{"id": "SGD:S123", "label": "enzyme"}],
        "mechanistic_edges": [],
        "references": [],
    }
    proteins = {
        "P12345": {
            "source": "fixture",
            "index": 0,
            "protein": {
                "primaryAccession": "P12345",
                "entryType": "UniProtKB reviewed (Swiss-Prot)",
                "uniProtKBCrossReferences": [{"database": "SGD", "id": "S123"}],
                "comments": [
                    {
                        "commentType": "COFACTOR",
                        "note": {
                            "texts": [
                                {
                                    "value": (
                                        "Magnesium or manganese; "
                                        "the alternatives are not both required."
                                    ),
                                }
                            ]
                        },
                        "cofactors": [
                            {
                                "name": "Mg(2+)",
                                "cofactorCrossReference": {
                                    "database": "ChEBI",
                                    "id": "CHEBI:18420",
                                },
                                "evidences": [{"evidenceCode": "ECO:0000250"}],
                            }
                        ],
                    }
                ],
            },
        }
    }
    sources = {
        "fixture": {
            "headers": {"X-UniProt-Release": "fixture"},
            "url": "https://rest.uniprot.org/uniprotkb/stream?query=fixture",
            "sha256": "a" * 64,
        }
    }
    return record, proteins, sources


def test_exact_mapping_preserves_cofactor_conditions_and_inferred_evidence():
    record, proteins, sources = fixture()
    index = identifier_index(proteins)
    report = curate(record, proteins, index, {"CHEBI:18420": "magnesium(2+)"}, sources)
    assert len(report["added"]) == 1
    edge = record["mechanistic_edges"][0]
    assert "alternatives are not both required" in edge["description"]
    assert "ECO:0000250" in edge["description"]
    assert edge["evidence"][0]["reference_id"] == "UniProtKB:P12345"
    assert "quote" not in edge["evidence"][0]
    assert record["participants"][1] == {
        "id": "CHEBI:18420",
        "label": "magnesium(2+)",
        "category": "cofactor",
    }
    before = deepcopy(record)
    assert not curate(record, proteins, index, {"CHEBI:18420": "magnesium(2+)"}, sources)["added"]
    assert record == before


def test_similar_gene_id_does_not_inherit_cofactors():
    record, proteins, sources = fixture()
    record["participants"][0]["id"] = "SGD:S1234"
    report = curate(record, proteins, identifier_index(proteins), {}, sources)
    assert report["unmapped"] == ["SGD:S1234"]
    assert not record["mechanistic_edges"]


def test_ambiguous_crossreference_fails_for_selected_protein():
    _, proteins, _ = fixture()
    proteins["P99999"] = deepcopy(proteins["P12345"])
    proteins["P99999"]["protein"]["primaryAccession"] = "P99999"
    with pytest.raises(ValueError, match="ambiguous"):
        identifier_index(proteins, {"SGD:S123"})
    assert identifier_index(proteins, {"UniProtKB:P12345"}) == {"UniProtKB:P12345": "P12345"}


def test_missing_authority_label_stops_without_guessing_from_record():
    record, proteins, sources = fixture()
    before = deepcopy(record)
    with pytest.raises(ValueError, match="missing independent ChEBI label"):
        curate(record, proteins, identifier_index(proteins), {}, sources)
    assert record == before


def test_existing_reviewed_cofactor_decision_preserves_entire_protein():
    record, proteins, sources = fixture()
    index = identifier_index(proteins)
    curate(record, proteins, index, {"CHEBI:18420": "magnesium(2+)"}, sources)
    proteins["P12345"]["protein"]["comments"][0]["cofactors"].append(
        {
            "name": "manganese",
            "cofactorCrossReference": {"database": "ChEBI", "id": "CHEBI:29035"},
        }
    )
    before = deepcopy(record)
    report = curate(record, proteins, index, {}, sources)
    assert report["preserved_existing"] == ["SGD:S123"]
    assert record == before


def test_reviewed_caution_is_content_pinned_and_new_caution_is_deferred():
    record, proteins, sources = fixture()
    caution = {"commentType": "CAUTION", "texts": [{"value": "Former functional name was wrong."}]}
    proteins["P12345"]["protein"]["comments"].append(caution)
    index = identifier_index(proteins)
    assert curate(record, proteins, index, {}, sources)["needs_caution_review"]
    assert not record["mechanistic_edges"]
    decisions = {
        "decisions": {
            "P12345": {
                "caution_sha256": caution_digest([caution]),
                "rationale": "Historical name does not contradict the cofactor annotation.",
            }
        }
    }
    assert curate(record, proteins, index, {"CHEBI:18420": "magnesium(2+)"}, sources, decisions)[
        "added"
    ]
    record["mechanistic_edges"] = []
    caution["texts"][0]["value"] = "New caution disputes magnesium binding."
    assert curate(record, proteins, index, {}, sources, decisions)["needs_caution_review"]


def test_covalent_pyruvoyl_projection_does_not_assert_free_pyruvate():
    record, proteins, sources = fixture()
    comment = proteins["P12345"]["protein"]["comments"][0]
    comment["cofactors"][0]["cofactorCrossReference"]["id"] = "CHEBI:15361"
    comment["note"]["texts"][0]["value"] = "Binds 1 pyruvoyl group covalently per subunit."
    decisions = {
        "projection_authority": {
            "url": "https://example.org/chebi.obo",
            "source_version": "255",
            "source_sha256": "b" * 64,
        },
        "decisions": {
            "P12345": {
                "cofactor_projection": {"CHEBI:15361": "CHEBI:45360"},
                "required_note_terms": ["pyruvoyl group", "covalently"],
                "projection_label": "pyruvoyl group",
                "rationale": "Covalent prosthetic group.",
            }
        },
    }
    report = curate(
        record,
        proteins,
        identifier_index(proteins),
        {"CHEBI:45360": "pyruvoyl group"},
        sources,
        decisions,
    )
    assert report["semantic_decisions"][0]["action"] == "project_covalent_group"
    edge = record["mechanistic_edges"][0]
    assert (edge["predicate"], edge["object"]) == ("has_cofactor", "CHEBI:45360")
    assert "CHEBI:15361" not in {node["id"] for node in record["participants"]}
    assert any("CHEBI:15361" in ev["source_assertion"] for ev in edge["evidence"])
    assert any(ev["reference_id"] == "CHEBI:45360" for ev in edge["evidence"])


def test_tentative_crystal_ion_is_reported_without_positive_edge():
    record, proteins, sources = fixture()
    decisions = {
        "decisions": {
            "P12345": {
                "excluded_cofactors": ["CHEBI:18420"],
                "rationale": "Tentative structural observation.",
            }
        }
    }
    report = curate(record, proteins, identifier_index(proteins), {}, sources, decisions)
    assert not record["mechanistic_edges"]
    assert report["semantic_decisions"][0]["action"] == "excluded_tentative"


def test_arg82_crystal_calcium_is_excluded_without_a_uniprot_caution():
    record, proteins, sources = fixture()
    item = proteins.pop("P12345")
    proteins["P07250"] = item
    protein = item["protein"]
    protein["primaryAccession"] = "P07250"
    protein["comments"] = [
        {
            "commentType": "COFACTOR",
            "cofactors": [
                {
                    "name": "Ca(2+)",
                    "evidences": [
                        {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "17050532"}
                    ],
                    "cofactorCrossReference": {"database": "ChEBI", "id": "CHEBI:29108"},
                }
            ],
        }
    ]
    decisions = json.loads(
        (Path(__file__).parents[1] / "reports/causal_graph_review/uniprot-cofactor-decisions.json")
        .read_text()
    )
    report = curate(record, proteins, identifier_index(proteins), {}, sources, decisions)
    assert not record["mechanistic_edges"]
    assert report["semantic_decisions"][0]["action"] == "excluded_crystal_contact"
    assert not report["needs_caution_review"]

    # This reviewed exclusion must not silently apply to changed source evidence.
    protein["comments"][0]["cofactors"][0]["evidences"][0]["id"] = "99999999"
    with pytest.raises(ValueError, match="Unreviewed cofactor annotation"):
        curate(record, proteins, identifier_index(proteins), {}, sources, decisions)


def test_note_only_experimental_evidence_is_preserved_without_upgrading_cofactor_row():
    record, proteins, sources = fixture()
    comment = proteins["P12345"]["protein"]["comments"][0]
    comment["cofactors"][0]["evidences"] = []
    comment["note"]["texts"][0]["evidences"] = [
        {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "2266128"}
    ]
    curate(record, proteins, identifier_index(proteins), {"CHEBI:18420": "magnesium(2+)"}, sources)
    edge = record["mechanistic_edges"][0]
    assert "UniProt evidence: not specified" in edge["description"]
    assert "UniProt note evidence: ECO:0000269 (PubMed:2266128)" in edge["description"]
    assert "/results/0/comments/0/note" in edge["evidence"][0]["source_locator"]


def test_existing_full_entry_reference_does_not_redirect_reduced_batch_pointer():
    record, proteins, sources = fixture()
    reference = {
        "id": "UniProtKB:P12345",
        "title": "Previously inspected complete entry",
        "url": "https://rest.uniprot.org/uniprotkb/P12345.json",
        "source_sha256": "b" * 64,
    }
    record["references"].append(deepcopy(reference))
    curate(record, proteins, identifier_index(proteins), {"CHEBI:18420": "magnesium(2+)"}, sources)
    assert record["references"][0] == reference
    locator = record["mechanistic_edges"][0]["evidence"][0]["source_locator"]
    assert sources["fixture"]["url"] in locator
    assert "a" * 64 in locator
    assert "#/results/0/comments/0/cofactors/0" in locator


def test_native_biocyc_join_has_two_independent_mapping_assertions(tmp_path):
    record, proteins, sources = fixture()
    native_id, native_type = "gomodel:test/lpx", "EcoCyc:LPX-MONOMER"
    record["participants"] = [{"id": native_id, "label": "Lpx", "category": "protein"}]
    protein = proteins["P12345"]["protein"]
    protein["organism"] = {"taxonId": 83333}
    protein["uniProtKBCrossReferences"] = [{"database": "BioCyc", "id": native_type}]
    model = {
        "id": "gomodel:test",
        "individuals": [{"id": native_id, "type": [{"id": native_type}]}],
        "annotations": [
            {"key": "https://w3id.org/biolink/vocab/in_taxon", "value": "NCBITaxon:83333"}
        ],
    }
    archive_path = tmp_path / "models.tgz"
    with tarfile.open(archive_path, "w:gz") as archive:
        raw = json.dumps(model).encode()
        member = tarfile.TarInfo("./test.json")
        member.size = len(raw)
        archive.addfile(member, io.BytesIO(raw))
    sha = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    mapping = native_identifier_mappings(proteins, archive_path, {native_id}, {"gomodel:test"}, sha)
    assert mapping[native_id]["accession"] == "P12345"
    curate(record, proteins, {}, {"CHEBI:18420": "magnesium(2+)"}, sources, native_mappings=mapping)
    evidence = record["mechanistic_edges"][0]["evidence"]
    assert len(evidence) == 3
    assert evidence[1]["reference_id"] == "gomodel:test"
    assert "has type EcoCyc:LPX-MONOMER" in evidence[1]["source_assertion"]
    assert "exact BioCyc cross-reference EcoCyc:LPX-MONOMER" in evidence[2]["source_assertion"]
    assert "gomodel:" not in evidence[2]["source_assertion"]
    with pytest.raises(ValueError, match="digest mismatch"):
        native_identifier_mappings(proteins, archive_path, {native_id}, {"gomodel:test"}, "0" * 64)
    proteins["P12345"]["protein"]["entryType"] = "UniProtKB unreviewed (TrEMBL)"
    with pytest.raises(ValueError, match="requires reviewed Swiss-Prot"):
        native_identifier_mappings(proteins, archive_path, {native_id}, {"gomodel:test"}, sha)
