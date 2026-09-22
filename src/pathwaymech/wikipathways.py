from __future__ import annotations

from pathlib import Path
from typing import Any
from xml.etree import ElementTree

DATABASE_PREFIXES = {
    "chebi": "CHEBI",
    "enzyme nomenclature": "EC",
    "geneontology": "GO",
    "uniprot": "UniProtKB",
    "uniprotkb": "UniProtKB",
}

ORGANISM_TAXA = {
    "Bacillus subtilis": "NCBITaxon:1423",
    "Escherichia coli": "NCBITaxon:562",
    "Saccharomyces cerevisiae": "NCBITaxon:4932",
}


def load_gpml_pathway(path: Path) -> ElementTree.Element:
    return ElementTree.parse(path).getroot()


def gpml_to_pathway_record(
    root: ElementTree.Element,
    fallback_id: str,
) -> dict[str, Any]:
    pathway_id = _pathway_id(root) or fallback_id
    node_by_graph_id = _data_nodes(root)
    references = _publication_references(root)
    evidence_reference = next(iter(references.values()), _fallback_reference(pathway_id))
    references.setdefault(evidence_reference["id"], evidence_reference)

    reactions = []
    edges: list[dict[str, Any]] = []
    for interaction in _children(root, "Interaction"):
        graph_id = interaction.get("GraphId")
        if not graph_id:
            continue

        sources, targets = _interaction_endpoints(interaction, node_by_graph_id)
        if not sources or not targets:
            continue

        reaction_id = f"{pathway_id}/{graph_id}"
        reactions.append({"id": reaction_id, "label": f"{pathway_id} interaction {graph_id}"})

        for node_id in sources:
            edges.append(
                _edge(
                    subject=node_id,
                    predicate="consumes",
                    obj=reaction_id,
                    evidence_reference=evidence_reference["id"],
                )
            )
        for node_id in targets:
            edges.append(
                _edge(
                    subject=reaction_id,
                    predicate="produces",
                    obj=node_id,
                    evidence_reference=evidence_reference["id"],
                )
            )

    return {
        "id": pathway_id,
        "label": root.get("Name") or pathway_id,
        "description": f"WikiPathways GPML pathway {pathway_id}.",
        "pathway_type": "pathway-diagram",
        "taxa": _taxa(root),
        "participants": list(node_by_graph_id.values()),
        "reactions": reactions,
        "mechanistic_edges": [
            {"id": f"wikipathways-edge-{index}", **edge}
            for index, edge in enumerate(edges, start=1)
        ],
        "references": list(references.values()),
    }


def _pathway_id(root: ElementTree.Element) -> str | None:
    for xref in _children(root, "Xref"):
        database = _attribute(xref, "Database", "dataSource").lower()
        identifier = _attribute(xref, "ID", "identifier")
        if database == "wikipathways" and identifier:
            return _format_curie("WikiPathways", identifier)
    return None


def _data_nodes(root: ElementTree.Element) -> dict[str, dict[str, str]]:
    data_nodes = {}
    for node in _children(root, "DataNode"):
        graph_id = node.get("GraphId")
        xref = _first_child(node, "Xref")
        if not graph_id or xref is None:
            continue
        identifier = _xref_curie(xref)
        if not identifier:
            continue
        data_nodes[graph_id] = {
            "id": identifier,
            "label": node.get("TextLabel") or identifier,
        }
    return data_nodes


def _xref_curie(xref: ElementTree.Element) -> str | None:
    database = _attribute(xref, "Database", "dataSource").lower()
    identifier = _attribute(xref, "ID", "identifier")
    prefix = DATABASE_PREFIXES.get(database)
    if not prefix or not identifier:
        return None
    return _format_curie(prefix, identifier)


def _interaction_endpoints(
    interaction: ElementTree.Element,
    node_by_graph_id: dict[str, dict[str, str]],
) -> tuple[list[str], list[str]]:
    sources: list[str] = []
    targets: list[str] = []
    graphics = _first_child(interaction, "Graphics")
    points = _children(graphics, "Point") if graphics is not None else []
    for point in points:
        graph_ref = point.get("GraphRef")
        if graph_ref not in node_by_graph_id:
            continue
        node_id = node_by_graph_id[graph_ref]["id"]
        if _is_target(point):
            targets.append(node_id)
        else:
            sources.append(node_id)
    return sources, targets


def _is_target(point: ElementTree.Element) -> bool:
    arrow_head = point.get("ArrowHead")
    return bool(arrow_head and arrow_head.lower() not in {"line", "none"})


def _publication_references(root: ElementTree.Element) -> dict[str, dict[str, str]]:
    references = {}
    for element in root.iter():
        if _local_name(element.tag) != "PublicationXref":
            continue
        pmid = _publication_pmid(element)
        if not pmid:
            continue
        reference_id = f"PMID:{pmid}"
        references[reference_id] = {
            "id": reference_id,
            "title": f"WikiPathways publication {reference_id}",
        }
    return references


def _publication_pmid(element: ElementTree.Element) -> str | None:
    for child in element.iter():
        if _local_name(child.tag) != "ID" or not child.text:
            continue
        text = child.text.strip()
        if text.isdigit():
            return text
    return None


def _fallback_reference(pathway_id: str) -> dict[str, str]:
    return {
        "id": pathway_id,
        "title": f"WikiPathways source pathway {pathway_id}",
    }


def _taxa(root: ElementTree.Element) -> list[dict[str, str]]:
    organism = root.get("Organism")
    if not organism or organism not in ORGANISM_TAXA:
        return []
    return [{"id": ORGANISM_TAXA[organism], "label": organism}]


def _edge(
    subject: str,
    predicate: str,
    obj: str,
    evidence_reference: str,
) -> dict[str, Any]:
    return {
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "evidence": [
            {
                "reference_id": evidence_reference,
                "quote": f"WikiPathways GPML interaction cites {evidence_reference}.",
            }
        ],
    }


def _first_child(
    element: ElementTree.Element,
    name: str,
) -> ElementTree.Element | None:
    return next(iter(_children(element, name)), None)


def _children(
    element: ElementTree.Element,
    name: str,
) -> list[ElementTree.Element]:
    return [child for child in element if _local_name(child.tag) == name]


def _attribute(
    element: ElementTree.Element,
    primary: str,
    fallback: str,
) -> str:
    return element.get(primary) or element.get(fallback) or ""


def _format_curie(prefix: str, identifier: str) -> str:
    if identifier.startswith(f"{prefix}:"):
        return identifier
    return f"{prefix}:{identifier}"


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]
