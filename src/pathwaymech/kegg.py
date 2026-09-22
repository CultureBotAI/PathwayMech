from __future__ import annotations

from pathlib import Path
from typing import Any
from xml.etree import ElementTree


def load_kgml(path: Path) -> ElementTree.Element:
    return ElementTree.parse(path).getroot()


def kgml_to_pathway_record(root: ElementTree.Element) -> dict[str, Any]:
    pathway_id = _kegg_curie(root.get("name") or "path:unknown")
    participants: dict[str, dict[str, str]] = {}
    reactions = []
    edges = []

    for reaction in root.findall("reaction"):
        reaction_id = _kegg_curie(reaction.get("name") or f"rn:{reaction.get('id')}")
        reactions.append({"id": reaction_id, "label": reaction_id})

        for substrate in reaction.findall("substrate"):
            participant_id = _kegg_curie(substrate.get("name") or "")
            participants[participant_id] = {"id": participant_id, "label": participant_id}
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
            participant_id = _kegg_curie(product.get("name") or "")
            participants[participant_id] = {"id": participant_id, "label": participant_id}
            edges.append(
                _edge(
                    subject=reaction_id,
                    predicate="produces",
                    obj=participant_id,
                    evidence_reference=pathway_id,
                    index=len(edges) + 1,
                )
            )

    return {
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


def _kegg_curie(identifier: str) -> str:
    clean = identifier.split()[-1]
    if ":" in clean:
        _, clean = clean.split(":", 1)
    return f"KEGG:{clean}"
