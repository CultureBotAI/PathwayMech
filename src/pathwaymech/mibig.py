from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

MIBIG_SEED_HEADER = "mibig_id\tproducts\tgenes\tloci\treferences"


@dataclass(frozen=True)
class MibigLocus:
    accession: str
    start: int | None = None
    end: int | None = None


@dataclass(frozen=True)
class MibigCluster:
    id: str
    products: tuple[str, ...]
    genes: tuple[str, ...]
    loci: tuple[MibigLocus, ...]
    references: tuple[str, ...]
    biosynthetic_classes: tuple[str, ...]
    organism: str | None = None
    taxon_id: str | None = None


def load_mibig_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a MIBiG JSON object")
    return value


def mibig_cluster(record: dict[str, Any]) -> MibigCluster:
    accession = _cluster_accession(record)
    if not accession:
        raise ValueError("MIBiG JSON missing mibig_accession")

    return MibigCluster(
        id=f"MIBiG:{accession.removeprefix('MIBiG:')}",
        products=tuple(sorted(_compound_names(record))),
        genes=tuple(sorted(_gene_ids(record))),
        loci=tuple(sorted(_loci(record), key=_locus_sort_key)),
        references=tuple(sorted(_pubmed_references(record))),
        biosynthetic_classes=tuple(sorted(_biosynthetic_classes(record))),
        organism=_organism_name(record),
        taxon_id=_taxon_id(record),
    )


def mibig_pathway_record(cluster: MibigCluster) -> dict[str, Any]:
    cluster_label = _cluster_label(cluster)
    gene_cluster: dict[str, Any] = {
        "id": cluster.id,
        "label": cluster_label,
    }
    if cluster.products:
        gene_cluster["products"] = list(cluster.products)
    if cluster.biosynthetic_classes:
        gene_cluster["biosynthetic_classes"] = list(cluster.biosynthetic_classes)
    if cluster.genes:
        gene_cluster["genes"] = [{"id": gene} for gene in cluster.genes]
    if cluster.loci:
        gene_cluster["loci"] = [
            {
                key: value
                for key, value in {
                    "accession": locus.accession,
                    "start": locus.start,
                    "end": locus.end,
                }.items()
                if value is not None
            }
            for locus in cluster.loci
        ]

    record: dict[str, Any] = {
        "id": cluster.id,
        "label": cluster_label,
        "description": f"Experimentally characterized MIBiG {cluster.id} gene cluster.",
        "pathway_type": "biosynthetic-gene-cluster",
        "taxa": [],
        "participants": [],
        "reactions": [],
        "mechanistic_edges": [],
        "gene_clusters": [gene_cluster],
        "references": [
            {
                "id": cluster.id,
                "title": f"MIBiG record {cluster.id.removeprefix('MIBiG:')}",
            },
            *[
                {
                    "id": reference,
                    "title": f"MIBiG literature reference {reference}",
                }
                for reference in cluster.references
            ],
        ],
    }
    if cluster.taxon_id:
        record["taxa"] = [
            {
                "id": f"NCBITaxon:{cluster.taxon_id.removeprefix('NCBITaxon:')}",
                "label": cluster.organism or f"NCBITaxon:{cluster.taxon_id}",
            }
        ]
    return record


def mibig_seed_rows(clusters: list[MibigCluster]) -> list[str]:
    rows = [MIBIG_SEED_HEADER]
    for cluster in clusters:
        rows.append(
            "\t".join(
                [
                    cluster.id,
                    ";".join(cluster.products),
                    ";".join(cluster.genes),
                    ";".join(locus.accession for locus in cluster.loci),
                    ";".join(cluster.references),
                ]
            )
        )
    return rows


def _cluster_label(cluster: MibigCluster) -> str:
    if not cluster.products:
        return f"{cluster.id} biosynthetic gene cluster"
    if len(cluster.products) == 1:
        return f"{cluster.products[0]} biosynthetic gene cluster"
    return f"{cluster.products[0]} and related metabolites biosynthetic gene cluster"


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


def _cluster_accession(value: dict[str, Any]) -> str | None:
    for field in ["mibig_accession", "accession"]:
        accession = value.get(field)
        if isinstance(accession, str) and accession:
            return accession
    cluster = value.get("cluster")
    if isinstance(cluster, dict):
        return _cluster_accession(cluster)
    return None


def _locus_sort_key(locus: MibigLocus) -> tuple[str, int, int]:
    return (locus.accession, locus.start or 0, locus.end or 0)


def _gene_ids(value: Any) -> set[str]:
    genes = set()
    for gene in _walk_list_members(value, "genes"):
        if isinstance(gene, str) and gene:
            genes.add(gene)
            continue
        if isinstance(gene, dict):
            for field in ["id", "gene", "accession"]:
                gene_id = gene.get(field)
                if isinstance(gene_id, str) and gene_id:
                    genes.add(gene_id)
                    break
    for gene in _walk_string_values(value, "gene"):
        genes.add(gene)
    return genes


def _loci(value: Any) -> set[MibigLocus]:
    loci = set()
    for locus in _walk_list_members(value, "loci"):
        parsed = _parse_locus(locus)
        if parsed:
            loci.add(parsed)
    return loci


def _parse_locus(value: Any) -> MibigLocus | None:
    if not isinstance(value, dict):
        return None
    accession = value.get("accession")
    if not isinstance(accession, str) or not accession:
        return None
    location = value.get("location") if isinstance(value.get("location"), dict) else {}
    start = _positive_int(location.get("from") or value.get("start"))
    end = _positive_int(location.get("to") or value.get("end"))
    return MibigLocus(accession=accession, start=start, end=end)


def _biosynthetic_classes(value: Any) -> set[str]:
    classes = set()
    for item in _walk_list_members(value, "biosyn_class"):
        if isinstance(item, str) and item:
            classes.add(item)
    for item in _walk_list_members(value, "classes"):
        if isinstance(item, str) and item:
            classes.add(item)
            continue
        if not isinstance(item, dict):
            continue
        class_name = item.get("class")
        subclass = item.get("subclass")
        if isinstance(class_name, str) and class_name:
            if isinstance(subclass, str) and subclass:
                classes.add(f"{class_name}:{subclass}")
            else:
                classes.add(class_name)
    return classes


def _pubmed_references(value: Any) -> set[str]:
    references = set()
    for field in ["pmid", "pubmed", "pubmed_id"]:
        for pmid in _walk_string_values(value, field):
            if reference := _pmid_reference(pmid):
                references.add(reference)
    for field in ["legacy_references", "publications"]:
        for reference in _walk_list_members(value, field):
            if not isinstance(reference, str):
                continue
            if pmid := _pmid_reference(reference):
                references.add(pmid)
    return references


def _organism_name(value: Any) -> str | None:
    if name := _first_string(value, "organism_name"):
        return name
    taxonomy = value.get("taxonomy") if isinstance(value, dict) else None
    if isinstance(taxonomy, dict):
        name = taxonomy.get("name")
        if isinstance(name, str) and name:
            return name
    return None


def _taxon_id(value: Any) -> str | None:
    return _first_string(value, "ncbi_tax_id", "ncbiTaxId")


def _pmid_reference(value: str) -> str | None:
    lowered = value.lower()
    if lowered.startswith("pubmed:"):
        value = value.split(":", 1)[1]
    return f"PMID:{value}" if value.isdigit() else None


def _first_string(value: Any, *fields: str) -> str | None:
    for field in fields:
        for item in _walk_string_values(value, field):
            return item
    return None


def _walk_list_members(value: Any, field: str) -> list[Any]:
    members = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == field:
                if isinstance(child, list):
                    members.extend(child)
                else:
                    members.append(child)
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
            if key == field:
                if isinstance(child, str) and child:
                    strings.append(child)
                elif type(child) is int:
                    strings.append(str(child))
                continue
            else:
                strings.extend(_walk_string_values(child, field))
    elif isinstance(value, list):
        for item in value:
            strings.extend(_walk_string_values(item, field))
    return strings


def _positive_int(value: Any) -> int | None:
    return value if type(value) is int and value > 0 else None
