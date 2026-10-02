from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

VEUPATHDB_SEED_HEADER = (
    "component_site\torganism\tgene_id\tgene_product\tpathway_source\tpathway_id\t"
    "pathway_name\tec_number\texact_match\treaction_count"
)
_SPACE = re.compile(r"[\t\r\n]+")
_EC = re.compile(r"(\d+(?:\.(?:\d+|-)){3})")


@dataclass(frozen=True)
class VeuPathDbPathwayCall:
    component_site: str
    organism: str
    gene_id: str
    gene_product: str
    pathway_source: str
    pathway_id: str
    pathway_name: str
    ec_number: str
    exact_match: str
    reaction_count: str


def load_veupathdb_pathways(path: Path) -> list[VeuPathDbPathwayCall]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return [veupathdb_pathway_call(row) for row in reader]


def veupathdb_pathway_call(row: dict[str, str]) -> VeuPathDbPathwayCall:
    primary_key = _first(row, "primary_key", "Primary Key")
    pathway_source = _first(row, "pathway_source", "Pathway Source")
    return VeuPathDbPathwayCall(
        component_site=_first(row, "component_site", "project_id", "Project ID")
        or _primary_key_part(primary_key, 1),
        organism=_first(row, "organism", "organism_full", "Organism"),
        gene_id=_first(row, "gene_id", "gene_source_id", "source_id", "Gene ID")
        or _primary_key_part(primary_key, 0),
        gene_product=_first(row, "gene_product", "product", "Product"),
        pathway_source=pathway_source,
        pathway_id=_pathway_id(
            _first(row, "pathway_source_id", "pathway_id", "Pathway ID"),
            pathway_source,
        ),
        pathway_name=_first(row, "pathway_name", "Pathway"),
        ec_number=_ec(_first(row, "enzyme", "ec_number", "EC Number Matched in Pathway")),
        exact_match=_first(row, "exact_match", "Exact EC Number Match"),
        reaction_count=_first(row, "reactions", "# Reactions Matching EC Number"),
    )


def veupathdb_seed_rows(calls: list[VeuPathDbPathwayCall]) -> list[str]:
    return [
        VEUPATHDB_SEED_HEADER,
        *[
            "\t".join(
                [
                    _cell(call.component_site),
                    _cell(call.organism),
                    _cell(call.gene_id),
                    _cell(call.gene_product),
                    _cell(call.pathway_source),
                    _cell(call.pathway_id),
                    _cell(call.pathway_name),
                    _cell(call.ec_number),
                    _cell(call.exact_match),
                    _cell(call.reaction_count),
                ]
            )
            for call in calls
        ],
    ]


def _first(row: dict[str, str], *names: str) -> str:
    for name in names:
        if value := (row.get(name) or "").strip():
            return value
    return ""


def _primary_key_part(primary_key: str, index: int) -> str:
    parts = [part.strip() for part in primary_key.split(",")]
    return parts[index] if len(parts) > index else ""


def _pathway_id(pathway_id: str, pathway_source: str) -> str:
    if not pathway_id or ":" in pathway_id:
        return pathway_id

    source = pathway_source.casefold()
    if "metacyc" in source:
        return f"MetaCyc:{pathway_id}"
    if "kegg" in source:
        return f"KEGG:{pathway_id}"
    return pathway_id


def _ec(value: str) -> str:
    if not value:
        return ""
    if match := _EC.search(value):
        return f"EC:{match.group(1)}"
    return f"EC:{value.removeprefix('EC:')}"


def _cell(value: str) -> str:
    return _SPACE.sub(" ", value).strip()
