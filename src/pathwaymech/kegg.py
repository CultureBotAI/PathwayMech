from __future__ import annotations

from pathlib import Path
from typing import Any
from xml.etree import ElementTree

from pathwaymech.source_mapping import (
    CurieMappings,
    normalized_curie,
    source_mapping_row,
    unique_source_mappings,
)


def load_kgml(path: Path) -> ElementTree.Element:
    return ElementTree.parse(path).getroot()


def kgml_to_pathway_record(
    root: ElementTree.Element,
    compound_mappings: CurieMappings | None = None,
) -> dict[str, Any]:
    pathway_id = _kegg_curie(root.get("name") or "path:unknown")
    compound_mappings = compound_mappings or {}
    participants: dict[str, dict[str, str]] = {}
    reactions = []
    edges = []
    source_mappings = []

    for reaction in root.findall("reaction"):
        reaction_id = _kegg_curie(reaction.get("name") or f"rn:{reaction.get('id')}")
        reactions.append({"id": reaction_id, "label": reaction_id})

        for substrate in reaction.findall("substrate"):
            source_id = _kegg_curie(substrate.get("name"))
            if not source_id:
                continue
            participant_id = normalized_curie(source_id, compound_mappings)
            participants[participant_id] = {"id": participant_id, "label": participant_id}
            source_mappings.extend(
                _source_mapping(
                    source_id,
                    compound_mappings,
                    source_pathway_id=pathway_id,
                    source_element_id=_source_element_id(
                        reaction_id,
                        "substrate",
                        substrate,
                        source_id,
                    ),
                )
            )
            edges.append(
                _edge(
                    subject=participant_id,
                    predicate="consumes",
                    obj=reaction_id,
                    evidence_reference=pathway_id,
                    index=len(edges) + 1,
                )
            )
        for product in reaction.findall("product"):
            source_id = _kegg_curie(product.get("name"))
            if not source_id:
                continue
            participant_id = normalized_curie(source_id, compound_mappings)
            participants[participant_id] = {"id": participant_id, "label": participant_id}
            source_mappings.extend(
                _source_mapping(
                    source_id,
                    compound_mappings,
                    source_pathway_id=pathway_id,
                    source_element_id=_source_element_id(
                        reaction_id,
                        "product",
                        product,
                        source_id,
                    ),
                )
            )
            edges.append(
                _edge(
                    subject=reaction_id,
                    predicate="produces",
                    obj=participant_id,
                    evidence_reference=pathway_id,
                    index=len(edges) + 1,
                )
            )

    record = {
        "id": pathway_id,
        "label": root.get("title") or pathway_id,
        "description": f"KEGG KGML pathway {pathway_id}.",
        "pathway_type": "metabolic",
        "taxa": [],
        "participants": list(participants.values()),
        "reactions": reactions,
        "mechanistic_edges": edges,
        "references": [
            {
                "id": pathway_id,
                "title": f"KEGG source pathway {pathway_id}",
            }
        ],
    }
    if source_mappings:
        record["source_mappings"] = unique_source_mappings(source_mappings)
    return record


def _source_mapping(
    source_id: str,
    compound_mappings: CurieMappings,
    *,
    source_pathway_id: str,
    source_element_id: str,
) -> list[dict[str, str]]:
    target_id = normalized_curie(source_id, compound_mappings)
    mapping = compound_mappings.get(source_id)
    if target_id == source_id or not mapping:
        return []
    return [
        source_mapping_row(
            source_id,
            "",
            mapping,
            source_pathway_id=source_pathway_id,
            source_element_id=source_element_id,
        )
    ]


def _source_element_id(
    reaction_id: str,
    role: str,
    element: ElementTree.Element,
    source_id: str,
) -> str:
    local_id = element.get("id") or source_id
    return f"{reaction_id}/{role}/{local_id}"


def _edge(
    subject: str,
    predicate: str,
    obj: str,
    evidence_reference: str,
    index: int,
) -> dict[str, Any]:
    return {
        "id": f"kegg-edge-{index}",
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "evidence": [
            {
                "reference_id": evidence_reference,
                "quote": f"KEGG KGML reaction participant cites {evidence_reference}.",
            }
        ],
    }


def _kegg_curie(identifier: str | None) -> str | None:
    if not identifier:
        return None
    clean = identifier.split()[-1]
    if ":" in clean:
        _, clean = clean.split(":", 1)
    return f"KEGG:{clean}"
