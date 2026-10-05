from __future__ import annotations

import csv
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from pathwaymech.schema import PathwayRecord

KNOWLEDGE_SOURCE = "infores:pathwaymech"

NODE_COLUMNS = (
    "id", "name", "category", "provided_by", "source_category", "direction", "source_contexts",
)
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
    "description",
    "evidence",
    "reference_metadata",
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
    "causally_upstream_of": "RO:0002411",
    "provides_input_for": "RO:0002413",
    "has_input": "RO:0002233",
    "has_output": "RO:0002234",
    "occurs_in": "BFO:0000066",
    "located_in": "RO:0001025",
    "part_of": "BFO:0000050",
    "has_part": "BFO:0000051",
    "has_cofactor": "pathwaymech:has_cofactor",
}

EXPLICIT_CATEGORIES = {
    "small_molecule": "biolink:SmallMolecule",
    "lipid": "biolink:ChemicalEntity",
    "cofactor": "biolink:ChemicalEntity",
    "protein": "biolink:Protein",
    "gene": "biolink:Gene",
    "dna": "biolink:NucleicAcidEntity",
    "rna": "biolink:RNAProduct",
    "complex": "biolink:MacromolecularComplex",
    "cellular_component": "biolink:CellularComponent",
    "molecular_activity": "biolink:MolecularActivity",
    "biological_process": "biolink:BiologicalProcess",
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
    "PANTHER": "biolink:BiochemicalReaction",
    "PathBank": "biolink:SmallMolecule",
    "PMN": "biolink:BiochemicalReaction",
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
    source_category: str = ""
    direction: str = ""
    source_contexts: str = ""


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
    description: str = ""
    evidence: str = ""
    reference_metadata: str = ""


def kgx_nodes(records: list[PathwayRecord]) -> list[KgxNode]:
    """Return one KGX node for every pathway-local node."""

    nodes: dict[str, KgxNode] = {}
    for record in records:
        _add_node(nodes, record.id, record.label, "biolink:Pathway",
                  context={"record_id": record.id, "collection": "pathway", "label": record.label})
        for node in record.taxa:
            _add_node(nodes, node["id"], node["label"], _category(node["id"]),
                      context={"record_id": record.id, "collection": "taxa", **node})
        for node in record.participants:
            category = _category(node["id"])
            # Native graph namespaces contain physical instances as well as
            # reactions. An unresolved participant must not acquire a process
            # identity merely from its namespace.
            if category == "biolink:BiochemicalReaction":
                category = "biolink:NamedThing"
            _add_node(nodes, node["id"], node["label"],
                      EXPLICIT_CATEGORIES.get(node.get("category"), category),
                      source_category=node.get("category", ""),
                      context={"record_id": record.id, "collection": "participants", **node})
        for node in record.reactions:
            _add_node(nodes, node["id"], node["label"],
                      EXPLICIT_CATEGORIES.get(node.get("category"), _category(node["id"])),
                      source_category=node.get("category", ""),
                      direction=node.get("direction", ""),
                      context={"record_id": record.id, "collection": "reactions", **node})
        for cluster in record.gene_clusters:
            _add_node(nodes, cluster["id"], cluster["label"], "biolink:GenomicEntity",
                      context={"record_id": record.id, "collection": "gene_clusters", **cluster})
    return list(nodes.values())


def kgx_edges(records: list[PathwayRecord]) -> list[KgxEdge]:
    """Return KGX edges preserving each curated mechanistic edge."""

    edges = []
    for record in records:
        references = {reference["id"]: reference for reference in record.references}
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
                    description=edge.get("description", ""),
                    evidence=json.dumps(edge["evidence"], ensure_ascii=False, sort_keys=True),
                    reference_metadata=json.dumps(
                        [references[identifier] for identifier in source_records],
                        ensure_ascii=False, sort_keys=True,
                    ),
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


def _add_node(
    nodes: dict[str, KgxNode], identifier: str, name: str, category: str,
    *, source_category: str = "", direction: str = "",
    context: dict[str, Any] | None = None,
) -> None:
    existing = nodes.get(identifier)
    if existing is None:
        nodes[identifier] = KgxNode(
            id=identifier, name=name, category=category,
            source_category=source_category, direction=direction,
            source_contexts=json.dumps([context] if context else [],
                                       ensure_ascii=False, sort_keys=True),
        )
        return

    def merge_values(first: str, second: str) -> str:
        return "|".join(sorted((set(first.split("|")) | set(second.split("|"))) - {""}))

    # Explicit source kinds take precedence over a prefix guess, regardless of
    # input order. Multiple supported roles (e.g. metabolite/cofactor) survive.
    if source_category and not existing.source_category:
        merged_category = category
    elif existing.source_category and not source_category:
        merged_category = existing.category
    else:
        merged_category = merge_values(existing.category, category)
    contexts = json.loads(existing.source_contexts)
    if context and context not in contexts:
        contexts.append(context)
    contexts.sort(key=lambda value: json.dumps(value, sort_keys=True))
    source_directions = {value["direction"] for value in contexts if value.get("direction")}
    # A shared identifier does not acquire one record's direction globally when
    # another record supplies a different orientation. Both survive in context.
    merged_direction = next(iter(source_directions)) if len(source_directions) == 1 else ""
    nodes[identifier] = KgxNode(
        id=identifier, name=existing.name, category=merged_category,
        source_category=merge_values(existing.source_category, source_category),
        direction=merged_direction,
        source_contexts=json.dumps(contexts, ensure_ascii=False, sort_keys=True),
    )


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
