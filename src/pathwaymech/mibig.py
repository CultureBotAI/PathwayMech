from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

MIBIG_SEED_HEADER = "mibig_id\tproducts\tgenes\tloci\treferences"


@dataclass(frozen=True)
class MibigCluster:
    id: str
    products: tuple[str, ...]
    genes: tuple[str, ...]
    loci: tuple[str, ...]
    references: tuple[str, ...]


def load_mibig_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a MIBiG JSON object")
    return value


def mibig_cluster(record: dict[str, Any]) -> MibigCluster:
    accession = _first_string(record, "mibig_accession")
    if not accession:
        raise ValueError("MIBiG JSON missing mibig_accession")

    return MibigCluster(
        id=f"MIBiG:{accession.removeprefix('MIBiG:')}",
        products=tuple(sorted(_compound_names(record))),
        genes=tuple(sorted(_gene_ids(record))),
        loci=tuple(sorted(_locus_accessions(record))),
        references=tuple(sorted(_pubmed_references(record))),
    )


def mibig_seed_rows(clusters: list[MibigCluster]) -> list[str]:
    rows = [MIBIG_SEED_HEADER]
    for cluster in clusters:
        rows.append(
            "\t".join(
                [
                    cluster.id,
                    ";".join(cluster.products),
                    ";".join(cluster.genes),
                    ";".join(cluster.loci),
                    ";".join(cluster.references),
                ]
            )
        )
    return rows


def _compound_names(value: Any) -> set[str]:
    names = set()
    for compound in _walk_list_members(value, "compounds"):
        if not isinstance(compound, dict):
            continue
        for field in ["compound", "compound_name", "name"]:
            name = compound.get(field)
            if isinstance(name, str) and name:
                names.add(name)
    return names


def _gene_ids(value: Any) -> set[str]:
    genes = set()
    for gene in _walk_list_members(value, "genes"):
        if not isinstance(gene, dict):
            continue
        gene_id = gene.get("id")
        if isinstance(gene_id, str) and gene_id:
            genes.add(gene_id)
    return genes


def _locus_accessions(value: Any) -> set[str]:
    loci = set()
    for locus in _walk_list_members(value, "loci"):
        if not isinstance(locus, dict):
            continue
        accession = locus.get("accession")
        if isinstance(accession, str) and accession:
            loci.add(accession)
    return loci


def _pubmed_references(value: Any) -> set[str]:
    references = set()
    for field in ["pmid", "pubmed", "pubmed_id"]:
        for pmid in _walk_string_values(value, field):
            if pmid.isdigit():
                references.add(f"PMID:{pmid}")
    return references


def _first_string(value: Any, field: str) -> str | None:
    for item in _walk_string_values(value, field):
        return item
    return None


def _walk_list_members(value: Any, field: str) -> list[Any]:
    members = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == field and isinstance(child, list):
                members.extend(child)
            else:
                members.extend(_walk_list_members(child, field))
    elif isinstance(value, list):
        for item in value:
            members.extend(_walk_list_members(item, field))
    return members


def _walk_string_values(value: Any, field: str) -> list[str]:
    strings = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == field and isinstance(child, str) and child:
                strings.append(child)
            else:
                strings.extend(_walk_string_values(child, field))
    elif isinstance(value, list):
        for item in value:
            strings.extend(_walk_string_values(item, field))
    return strings
