from __future__ import annotations

from pathlib import Path
from typing import Any
from xml.etree import ElementTree

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
DB_PREFIXES = {
    "chebi": "CHEBI",
    "go": "GO",
    "uniprot": "UniProtKB",
    "uniprotkb": "UniProtKB",
}


def load_biopax(path: Path) -> ElementTree.Element:
    return ElementTree.parse(path).getroot()


def biopax_to_pathway_record(
    root: ElementTree.Element,
    fallback_id: str,
) -> dict[str, Any]:
    xref_by_ref = _unification_xrefs(root)
    participant_by_ref = _participants(root, xref_by_ref)
    references = _publication_references(root)
    evidence_reference = next(iter(references.values()), _fallback_reference(fallback_id))
    references.setdefault(evidence_reference["id"], evidence_reference)

    reactions = []
    edges: list[dict[str, Any]] = []
    for reaction in _elements(root, "BiochemicalReaction"):
        reaction_ref = _element_ref(reaction)
        reaction_id = f"{fallback_id}/{reaction_ref}"
        reactions.append(
            {"id": reaction_id, "label": _text_child(reaction, "displayName") or reaction_ref}
        )

        for participant_id in _side_participants(reaction, "left", participant_by_ref):
            edges.append(
                _edge(
                    subject=participant_id,
                    predicate="consumes",
                    obj=reaction_id,
                    evidence_reference=evidence_reference["id"],
                )
            )
        for participant_id in _side_participants(reaction, "right", participant_by_ref):
            edges.append(
                _edge(
                    subject=reaction_id,
                    predicate="produces",
                    obj=participant_id,
                    evidence_reference=evidence_reference["id"],
                )
            )

    return {
        "id": fallback_id,
        "label": _pathway_label(root) or fallback_id,
        "description": f"BioPAX pathway {fallback_id}.",
        "pathway_type": "biopax-pathway",
        "taxa": [],
        "participants": list(participant_by_ref.values()),
        "reactions": reactions,
        "mechanistic_edges": [
            {"id": f"biopax-edge-{index}", **edge}
            for index, edge in enumerate(edges, start=1)
        ],
        "references": list(references.values()),
    }


def _unification_xrefs(root: ElementTree.Element) -> dict[str, str]:
    xrefs = {}
    for xref in _elements(root, "UnificationXref"):
        database = (_text_child(xref, "db") or "").lower()
        identifier = _text_child(xref, "id")
        prefix = DB_PREFIXES.get(database)
        if prefix and identifier:
            xrefs[_element_ref(xref)] = _format_curie(prefix, identifier)
    return xrefs


def _participants(
    root: ElementTree.Element,
    xref_by_ref: dict[str, str],
) -> dict[str, dict[str, str]]:
    reference_by_ref = _entity_references(root, xref_by_ref)
    participants = {}
    for element_name in ["SmallMolecule", "Protein"]:
        for element in _elements(root, element_name):
            reference = _resource_child(element, "entityReference")
            if not reference or reference not in reference_by_ref:
                continue
            identifier = reference_by_ref[reference]
            participants[_element_ref(element)] = {
                "id": identifier,
                "label": _text_child(element, "displayName") or identifier,
            }
    return participants


def _entity_references(
    root: ElementTree.Element,
    xref_by_ref: dict[str, str],
) -> dict[str, str]:
    references = {}
    for element_name in ["SmallMoleculeReference", "ProteinReference"]:
        for element in _elements(root, element_name):
            xref = _resource_child(element, "xref")
            if xref in xref_by_ref:
                references[_element_ref(element)] = xref_by_ref[xref]
    return references


def _side_participants(
    reaction: ElementTree.Element,
    side: str,
    participant_by_ref: dict[str, dict[str, str]],
) -> list[str]:
    participants = []
    for element in _children(reaction, side):
        resource = _resource(element)
        if resource in participant_by_ref:
            participants.append(participant_by_ref[resource]["id"])
    return participants


def _publication_references(root: ElementTree.Element) -> dict[str, dict[str, str]]:
    references = {}
    for publication in _elements(root, "PublicationXref"):
        pmid = _text_child(publication, "id")
        if not pmid or not pmid.isdigit():
            continue
        reference_id = f"PMID:{pmid}"
        references[reference_id] = {
            "id": reference_id,
            "title": f"BioPAX publication {reference_id}",
        }
    return references


def _fallback_reference(pathway_id: str) -> dict[str, str]:
    return {
        "id": pathway_id,
        "title": f"BioPAX source pathway {pathway_id}",
    }


def _pathway_label(root: ElementTree.Element) -> str | None:
    pathway = next(iter(_elements(root, "Pathway")), None)
    if pathway is None:
        return None
    return _text_child(pathway, "displayName")


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
                "quote": f"BioPAX reaction cites {evidence_reference}.",
            }
        ],
    }


def _elements(root: ElementTree.Element, name: str) -> list[ElementTree.Element]:
    return [element for element in root.iter() if _local_name(element.tag) == name]


def _children(element: ElementTree.Element, name: str) -> list[ElementTree.Element]:
    return [child for child in element if _local_name(child.tag) == name]


def _text_child(element: ElementTree.Element, name: str) -> str | None:
    for child in _children(element, name):
        if child.text:
            return child.text.strip()
    return None


def _resource_child(element: ElementTree.Element, name: str) -> str | None:
    for child in _children(element, name):
        return _resource(child)
    return None


def _resource(element: ElementTree.Element) -> str:
    return (element.get(f"{RDF}resource") or "").removeprefix("#")


def _element_ref(element: ElementTree.Element) -> str:
    return (
        element.get(f"{RDF}ID")
        or element.get(f"{RDF}about", "").removeprefix("#")
        or element.get("ID")
        or element.get("id")
        or _local_name(element.tag)
    )


def _format_curie(prefix: str, identifier: str) -> str:
    if identifier.startswith(f"{prefix}:"):
        return identifier
    return f"{prefix}:{identifier}"


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]
