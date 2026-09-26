from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

WIKIPATHWAYS_ACCESSION = re.compile(r"WP\d+")

DATABASE_PREFIXES = {
    "chebi": "CHEBI",
    "enzyme nomenclature": "EC",
    "geneontology": "GO",
    "sgd": "SGD",
    "uniprot": "UniProtKB",
    "uniprot-trembl": "UniProtKB",
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
    nodes_by_group_graph_id = _group_nodes(root, node_by_graph_id)
    reaction_by_anchor_id = _anchor_reactions(root, pathway_id)
    references = _publication_references(root)
    evidence_reference = next(iter(references.values()), _fallback_reference(pathway_id))
    references.setdefault(evidence_reference["id"], evidence_reference)

    reactions = []
    edges: list[dict[str, Any]] = []
    for interaction in _children(root, "Interaction"):
        graph_id = interaction.get("GraphId")
        if not graph_id:
            continue
        if _contains_anchor_ref(interaction, reaction_by_anchor_id):
            edges.extend(
                _anchor_edges(
                    interaction,
                    node_by_graph_id,
                    nodes_by_group_graph_id,
                    reaction_by_anchor_id,
                    evidence_reference["id"],
                )
            )
            continue

        sources, targets = _interaction_endpoints(
            interaction,
            node_by_graph_id,
            nodes_by_group_graph_id,
        )
        if not sources and not targets:
            continue
        if not _interaction_anchors(interaction) and (not sources or not targets):
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
        "participants": _unique_nodes(node_by_graph_id.values()),
        "reactions": reactions,
        "mechanistic_edges": [
            {"id": f"wikipathways-edge-{index}", **edge}
            for index, edge in enumerate(_unique_edges(edges), start=1)
        ],
        "references": list(references.values()),
    }


def wikipathways_curie_from_text(text: str) -> str | None:
    match = WIKIPATHWAYS_ACCESSION.search(text)
    if not match:
        return None
    return _format_curie("WikiPathways", match.group(0))


def wikipathways_fallback_id(path: Path) -> str:
    return wikipathways_curie_from_text(path.stem) or f"WikiPathways:{path.stem}"


def _pathway_id(root: ElementTree.Element) -> str | None:
    for xref in _children(root, "Xref"):
        database = _attribute(xref, "Database", "dataSource").lower()
        identifier = _attribute(xref, "ID", "identifier")
        if database == "wikipathways" and identifier:
            return _format_curie("WikiPathways", identifier)
    return wikipathways_curie_from_text(root.get("Version") or "")


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


def _unique_nodes(nodes: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    unique: dict[str, dict[str, str]] = {}
    for node in nodes:
        unique.setdefault(node["id"], node)
    return list(unique.values())


def _unique_edges(edges: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    unique = {}
    for edge in edges:
        unique.setdefault((edge["subject"], edge["predicate"], edge["object"]), edge)
    return list(unique.values())


def _group_nodes(
    root: ElementTree.Element,
    node_by_graph_id: dict[str, dict[str, str]],
) -> dict[str, list[str]]:
    nodes_by_group_id: dict[str, list[str]] = {}
    for node in _children(root, "DataNode"):
        graph_id = node.get("GraphId")
        group_id = node.get("GroupRef")
        if not group_id or graph_id not in node_by_graph_id:
            continue
        nodes_by_group_id.setdefault(group_id, []).append(node_by_graph_id[graph_id]["id"])

    nodes_by_group_graph_id = {}
    for group in _children(root, "Group"):
        graph_id = group.get("GraphId")
        group_id = group.get("GroupId")
        if graph_id and group_id:
            nodes_by_group_graph_id[graph_id] = nodes_by_group_id.get(group_id, [])
    return nodes_by_group_graph_id


def _anchor_reactions(
    root: ElementTree.Element,
    pathway_id: str,
) -> dict[str, str]:
    reactions = {}
    for interaction in _children(root, "Interaction"):
        graph_id = interaction.get("GraphId")
        if not graph_id:
            continue
        for anchor in _interaction_anchors(interaction):
            anchor_id = anchor.get("GraphId")
            if anchor_id:
                reactions[anchor_id] = f"{pathway_id}/{graph_id}"
    return reactions


def _interaction_endpoints(
    interaction: ElementTree.Element,
    node_by_graph_id: dict[str, dict[str, str]],
    nodes_by_group_graph_id: dict[str, list[str]],
) -> tuple[list[str], list[str]]:
    sources: list[str] = []
    targets: list[str] = []
    for point in _interaction_points(interaction):
        graph_ref = point.get("GraphRef")
        node_ids = _nodes_for_graph_ref(
            graph_ref,
            node_by_graph_id,
            nodes_by_group_graph_id,
        )
        if _is_target(point):
            targets.extend(node_ids)
        else:
            sources.extend(node_ids)
    return sources, targets


def _anchor_edges(
    interaction: ElementTree.Element,
    node_by_graph_id: dict[str, dict[str, str]],
    nodes_by_group_graph_id: dict[str, list[str]],
    reaction_by_anchor_id: dict[str, str],
    evidence_reference: str,
) -> list[dict[str, Any]]:
    points = _interaction_points(interaction)
    anchor_points = [
        point
        for point in points
        if point.get("GraphRef") and point.get("GraphRef") in reaction_by_anchor_id
    ]
    if len(anchor_points) != 1:
        return []

    anchor_point = anchor_points[0]
    anchor_id = anchor_point.get("GraphRef", "")
    reaction_id = reaction_by_anchor_id[anchor_id]
    edges = []
    for point in points:
        if point is anchor_point:
            continue

        node_ids = _nodes_for_graph_ref(
            point.get("GraphRef"),
            node_by_graph_id,
            nodes_by_group_graph_id,
        )
        for node_id in node_ids:
            if _is_catalysis(anchor_point):
                edges.append(
                    _edge(
                        subject=node_id,
                        predicate="catalyzes",
                        obj=reaction_id,
                        evidence_reference=evidence_reference,
                    )
                )
            elif _is_target(anchor_point):
                edges.append(
                    _edge(
                        subject=node_id,
                        predicate="consumes",
                        obj=reaction_id,
                        evidence_reference=evidence_reference,
                    )
                )
            elif _is_target(point):
                edges.append(
                    _edge(
                        subject=reaction_id,
                        predicate="produces",
                        obj=node_id,
                        evidence_reference=evidence_reference,
                    )
                )
    return edges


def _nodes_for_graph_ref(
    graph_ref: str | None,
    node_by_graph_id: dict[str, dict[str, str]],
    nodes_by_group_graph_id: dict[str, list[str]],
) -> list[str]:
    if not graph_ref:
        return []
    if graph_ref in node_by_graph_id:
        return [node_by_graph_id[graph_ref]["id"]]
    return nodes_by_group_graph_id.get(graph_ref, [])


def _contains_anchor_ref(
    interaction: ElementTree.Element,
    reaction_by_anchor_id: dict[str, str],
) -> bool:
    return any(
        point.get("GraphRef") in reaction_by_anchor_id
        for point in _interaction_points(interaction)
    )


def _interaction_anchors(interaction: ElementTree.Element) -> list[ElementTree.Element]:
    graphics = _first_child(interaction, "Graphics")
    return _children(graphics, "Anchor") if graphics is not None else []


def _interaction_points(interaction: ElementTree.Element) -> list[ElementTree.Element]:
    graphics = _first_child(interaction, "Graphics")
    return _children(graphics, "Point") if graphics is not None else []


def _is_target(point: ElementTree.Element) -> bool:
    arrow_head = point.get("ArrowHead")
    return bool(arrow_head and arrow_head.lower() not in {"line", "none"})


def _is_catalysis(point: ElementTree.Element) -> bool:
    return "catalysis" in (point.get("ArrowHead") or "").lower()


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
