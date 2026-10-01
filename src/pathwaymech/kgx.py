from __future__ import annotations

import csv
import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from pathwaymech.schema import PathwayRecord

KNOWLEDGE_SOURCE = "infores:pathwaymech"

NODE_COLUMNS = ("id", "name", "category", "provided_by")
EDGE_COLUMNS = (
    "id",
    "subject",
    "predicate",
    "object",
    "category",
    "primary_knowledge_source",
    "knowledge_level",
    "agent_type",
    "source_records",
)

LOCAL_PREDICATE_CURIES = {
    "activates": "pathwaymech:activates",
    "catalyzes": "pathwaymech:catalyzes",
    "consumes": "pathwaymech:consumes",
    "enables": "pathwaymech:enables",
    "inhibits": "pathwaymech:inhibits",
    "precedes": "pathwaymech:precedes",
    "produces": "pathwaymech:produces",
    "regulates": "pathwaymech:regulates",
}

_PREFIX_CATEGORIES = {
    "CAS": "biolink:SmallMolecule",
    "CHEBI": "biolink:SmallMolecule",
    "ChemSpider": "biolink:SmallMolecule",
    "EC": "biolink:MolecularActivity",
    "Ensembl": "biolink:GeneOrGeneProduct",
    "Entrez": "biolink:GeneOrGeneProduct",
    "GO": "biolink:MolecularActivity",
    "HMDB": "biolink:SmallMolecule",
    "KEGG": "biolink:SmallMolecule",
    "LIPIDMAPS": "biolink:SmallMolecule",
    "MetaCyc": "biolink:BiochemicalReaction",
    "ModelSEED": "biolink:SmallMolecule",
    "NCBIProtein": "biolink:GeneOrGeneProduct",
    "NCBITaxon": "biolink:OrganismTaxon",
    "PathBank": "biolink:SmallMolecule",
    "PubChem": "biolink:SmallMolecule",
    "RHEA": "biolink:BiochemicalReaction",
    "Reactome": "biolink:BiochemicalReaction",
    "SGD": "biolink:GeneOrGeneProduct",
    "TubercuList": "biolink:GeneOrGeneProduct",
    "UniProtKB": "biolink:GeneOrGeneProduct",
    "WikiPathways": "biolink:BiochemicalReaction",
    "gomodel": "biolink:BiochemicalReaction",
}
_SPACE = re.compile(r"[\t\r\n]+")
_UNSAFE_EDGE_ID = re.compile(r"[^A-Za-z0-9._-]+")


@dataclass(frozen=True)
class KgxNode:
    id: str
    name: str
    category: str
    provided_by: str = KNOWLEDGE_SOURCE


@dataclass(frozen=True)
class KgxEdge:
    id: str
    subject: str
    predicate: str
    object: str
    category: str = "biolink:Association"
    primary_knowledge_source: str = KNOWLEDGE_SOURCE
    knowledge_level: str = "knowledge_assertion"
    agent_type: str = "manual_validation_of_automated_agent"
    source_records: str = ""


def kgx_nodes(records: list[PathwayRecord]) -> list[KgxNode]:
    """Return one KGX node for every pathway-local node."""

    nodes: dict[str, KgxNode] = {}
    for record in records:
        _add_node(nodes, record.id, record.label, "biolink:Pathway")
        for node in record.taxa:
            _add_node(nodes, node["id"], node["label"], _category(node["id"]))
        for node in record.participants:
            _add_node(nodes, node["id"], node["label"], _category(node["id"]))
        for node in record.reactions:
            _add_node(nodes, node["id"], node["label"], _category(node["id"]))
        for cluster in record.gene_clusters:
            _add_node(nodes, cluster["id"], cluster["label"], "biolink:GenomicEntity")
    return list(nodes.values())


def kgx_edges(records: list[PathwayRecord]) -> list[KgxEdge]:
    """Return KGX edges preserving each curated mechanistic edge."""

    edges = []
    for record in records:
        for edge in record.mechanistic_edges:
            predicate = LOCAL_PREDICATE_CURIES[edge["predicate"]]
            source_records = sorted(
                {
                    evidence["reference_id"]
                    for evidence in edge["evidence"]
                    if evidence.get("reference_id")
                }
            )
            edges.append(
                KgxEdge(
                    id=_edge_id(record.id, edge["id"]),
                    subject=edge["subject"],
                    predicate=predicate,
                    object=edge["object"],
                    source_records="|".join(source_records),
                )
            )
    return edges


def write_kgx(records: list[PathwayRecord], output_dir: Path) -> tuple[Path, Path]:
    """Write the KGX node/edge TSV pair and return their paths."""

    output_dir.mkdir(parents=True, exist_ok=True)
    nodes_path = output_dir / "nodes.tsv"
    edges_path = output_dir / "edges.tsv"
    _write_tsv(nodes_path, NODE_COLUMNS, [asdict(node) for node in kgx_nodes(records)])
    _write_tsv(edges_path, EDGE_COLUMNS, [asdict(edge) for edge in kgx_edges(records)])
    return nodes_path, edges_path


def _add_node(nodes: dict[str, KgxNode], identifier: str, name: str, category: str) -> None:
    if identifier not in nodes:
        nodes[identifier] = KgxNode(id=identifier, name=name, category=category)


def _category(identifier: str) -> str:
    return _PREFIX_CATEGORIES.get(identifier.split(":", 1)[0], "biolink:NamedThing")


def _edge_id(record_id: str, edge_id: str) -> str:
    digest = hashlib.sha256(f"{record_id}\0{edge_id}".encode()).hexdigest()[:12]
    safe = _UNSAFE_EDGE_ID.sub("_", f"{record_id}_{edge_id}").strip("_")
    return f"pathwaymech:{safe}_{digest}"


def _write_tsv(path: Path, columns: tuple[str, ...], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            delimiter="\t",
            fieldnames=columns,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({column: _cell(row.get(column)) for column in columns})


def _cell(value: Any) -> str:
    if value is None:
        return ""
    return _SPACE.sub(" ", str(value)).strip()
