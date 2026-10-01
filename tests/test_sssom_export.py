from __future__ import annotations

import csv
from pathlib import Path

import pytest
import yaml
from sssom.parsers import parse_sssom_table

from pathwaymech.schema import PathwayRecord
from pathwaymech.sssom import SSSOM_COLUMNS, SssomRow, sssom_rows, write_sssom
from pathwaymech.yaml_io import load_pathway_records


def record(source_mappings: list[dict[str, str]] | None = None) -> PathwayRecord:
    return PathwayRecord(
        id="Reactome:R-TEST-12345",
        label="test pathway",
        description="A compact test pathway.",
        pathway_type="test",
        taxa=[],
        participants=[{"id": "UniProtKB:P12345", "label": "Mini enzyme"}],
        reactions=[],
        mechanistic_edges=[],
        references=[],
        source_mappings=source_mappings
        if source_mappings is not None
        else [
            {
                "subject_id": "UniProt:P12345",
                "subject_label": "Mini enzyme",
                "predicate_id": "skos:exactMatch",
                "object_id": "UniProtKB:P12345",
                "object_label": "Mini enzyme",
                "mapping_justification": "semapv:UnspecifiedMatching",
                "confidence": "1.0",
                "source_pathway_id": "Reactome:R-TEST-12345",
                "source_element_id": "mini_enzyme",
            }
        ],
    )


def test_sssom_rows_keep_source_context_in_deterministic_rows() -> None:
    assert sssom_rows([record()]) == [
        SssomRow(
            subject_id="UniProt:P12345",
            subject_label="Mini enzyme",
            predicate_id="skos:exactMatch",
            object_id="UniProtKB:P12345",
            object_label="Mini enzyme",
            mapping_justification="semapv:UnspecifiedMatching",
            confidence="1.0",
            comment=(
                "source_pathway_id=Reactome:R-TEST-12345; "
                "source_element_id=mini_enzyme"
            ),
        )
    ]


def test_write_sssom_uses_lf_tsv_with_stable_headers(tmp_path: Path) -> None:
    path = write_sssom([record()], tmp_path / "source_mappings.sssom.tsv")

    assert path.read_bytes().count(b"\r") == 0
    lines = path.read_text(encoding="utf-8").splitlines()
    assert "# curie_map:" in lines
    assert '#   CHEBI: "http://purl.obolibrary.org/obo/CHEBI_"' in lines
    assert '#   HMDB: "https://identifiers.org/hmdb:"' in lines
    assert '#   UniProt: "https://identifiers.org/uniprot:"' in lines
    assert '#   UniProtKB: "http://purl.uniprot.org/uniprot/"' in lines
    assert next(line for line in lines if not line.startswith("#")) == "\t".join(
        SSSOM_COLUMNS
    )
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t", fieldnames=SSSOM_COLUMNS))

    assert rows[-1]["subject_id"] == "UniProt:P12345"
    assert rows[-1]["object_id"] == "UniProtKB:P12345"


def test_write_sssom_uses_yaml_safe_curie_map_for_all_source_prefixes(
    tmp_path: Path,
) -> None:
    path = write_sssom(
        [
            record(
                [
                    dict(
                        record().source_mappings[0],
                        subject_id=f"{prefix}:{local_id}",
                        subject_label=prefix,
                        object_id=f"CHEBI:{index}",
                        object_label=f"ChEBI {index}",
                        source_element_id=prefix,
                    )
                    for index, (prefix, local_id) in enumerate(
                        [
                            ("CAS", "98-92-0"),
                            ("ChemSpider", "555"),
                            ("HMDB", "HMDB0000223"),
                            ("KEGG", "C00197"),
                            ("PubChem", "647"),
                            ("UniProt", "P12345"),
                        ],
                        start=1,
                    )
                ]
            )
        ],
        tmp_path / "source_mappings.sssom.tsv",
    )

    lines = path.read_text(encoding="utf-8").splitlines()
    preamble = "\n".join(
        line.removeprefix("# ") for line in lines if line.startswith("#")
    )

    assert yaml.safe_load(preamble)["curie_map"] == {
        "CAS": "https://identifiers.org/cas:",
        "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
        "ChemSpider": "https://identifiers.org/chemspider:",
        "HMDB": "https://identifiers.org/hmdb:",
        "infores": "https://w3id.org/biolink/vocab/",
        "KEGG": "https://identifiers.org/kegg.compound:",
        "PubChem": "https://identifiers.org/pubchem.compound:",
        "semapv": "https://w3id.org/semapv/vocab/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "UniProt": "https://identifiers.org/uniprot:",
        "UniProtKB": "http://purl.uniprot.org/uniprot/",
    }


def test_write_sssom_emits_standard_sssom_parseable_metadata(tmp_path: Path) -> None:
    path = write_sssom([record()], tmp_path / "source_mappings.sssom.tsv")

    assert len(parse_sssom_table(path).df) == 1


def test_committed_sssom_output_is_current(tmp_path: Path) -> None:
    expected = write_sssom(
        load_pathway_records(Path("data/pathways")),
        tmp_path / "source_mappings.sssom.tsv",
    )

    assert Path("output/sssom/source_mappings.sssom.tsv").read_text(
        encoding="utf-8"
    ) == expected.read_text(encoding="utf-8")


def test_sssom_rejects_label_only_subjects() -> None:
    bad_mapping = dict(record().source_mappings[0], subject_id="Mini enzyme")

    with pytest.raises(ValueError, match="subject_id must be a CURIE"):
        sssom_rows([record([bad_mapping])])


def test_sssom_rejects_empty_curie_prefixes() -> None:
    bad_mapping = dict(record().source_mappings[0], subject_id=":P12345")

    with pytest.raises(ValueError, match="subject_id must be a CURIE"):
        sssom_rows([record([bad_mapping])])


def test_sssom_rejects_final_curie_only_pseudo_mappings() -> None:
    bad_mapping = dict(record().source_mappings[0], subject_id="UniProtKB:P12345")

    with pytest.raises(ValueError, match="source mapping subject_id must differ"):
        sssom_rows([record([bad_mapping])])
