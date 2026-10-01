from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

from pathwaymech.source_mapping import CurieMapping, source_mapping_row, unique_source_mappings

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
MAX_EVIDENCE_QUOTE_LENGTH = 400
DB_PREFIXES = {
    "chebi": "CHEBI",
    "go": "GO",
    "gene ontology": "GO",
    "ncbi taxonomy": "NCBITaxon",
    "reactome": "Reactome",
    "uniprot": "UniProtKB",
    "uniprotkb": "UniProtKB",
}


@dataclass(frozen=True)
class NormalizedXref:
    source_id: str
    object_id: str


def load_biopax(path: Path) -> ElementTree.Element:
    return ElementTree.parse(path).getroot()


def biopax_to_pathway_record(
    root: ElementTree.Element,
    fallback_id: str,
) -> dict[str, Any]:
    source_prefix = fallback_id.split(":", 1)[0]
    xref_by_ref = _unification_xrefs(root)
    references, publication_reference_by_ref = _publication_references(root)
    default_reference = next(iter(references.values()), _fallback_reference(fallback_id))
    references.setdefault(default_reference["id"], default_reference)

    pathway_id = _pathway_id(root, xref_by_ref, source_prefix) or fallback_id
    participant_by_ref, source_mappings = _participants(root, xref_by_ref, pathway_id)
    complex_components_by_ref = _complex_components(root)
    reaction_by_ref = {}
    evidence_quote_by_reaction_ref: dict[str, str | None] = {}
    evidence_reference_by_reaction_ref: dict[str, str] = {}
    reactions = []
    edges: list[dict[str, Any]] = []
    for reaction in _elements(root, "BiochemicalReaction"):
        reaction_ref = _element_ref(reaction)
        reaction_id = (
            _source_xref(reaction, xref_by_ref, source_prefix)
            or f"{pathway_id}/{reaction_ref}"
        )
        reaction_by_ref[reaction_ref] = reaction_id
        reactions.append(
            {"id": reaction_id, "label": _text_child(reaction, "displayName") or reaction_ref}
        )

        evidence_quote = _text_child(reaction, "comment")
        evidence_reference = (
            _publication_reference_id(reaction, publication_reference_by_ref)
            or default_reference["id"]
        )
        evidence_quote_by_reaction_ref[reaction_ref] = evidence_quote
        evidence_reference_by_reaction_ref[reaction_ref] = evidence_reference
        for participant_id in _side_participants(reaction, "left", participant_by_ref):
            edges.append(
                _edge(
                    subject=participant_id,
                    predicate="consumes",
                    obj=reaction_id,
                    evidence_reference=evidence_reference,
                    evidence_quote=evidence_quote,
                )
            )
        for participant_id in _side_participants(reaction, "right", participant_by_ref):
            edges.append(
                _edge(
                    subject=reaction_id,
                    predicate="produces",
                    obj=participant_id,
                    evidence_reference=evidence_reference,
                    evidence_quote=evidence_quote,
                )
            )

    for catalysis in _elements(root, "Catalysis"):
        reaction_ref = _resource_child(catalysis, "controlled")
        if reaction_ref not in reaction_by_ref:
            continue
        for participant_id in _controller_participants(
            _resource_child(catalysis, "controller"),
            participant_by_ref,
            complex_components_by_ref,
        ):
            if not participant_id.startswith("UniProtKB:"):
                continue
            edges.append(
                _edge(
                    subject=participant_id,
                    predicate="catalyzes",
                    obj=reaction_by_ref[reaction_ref],
                    evidence_reference=evidence_reference_by_reaction_ref[reaction_ref],
                    evidence_quote=evidence_quote_by_reaction_ref.get(reaction_ref),
                )
            )

    used_participants = {edge["subject"] for edge in edges} | {
        edge["object"] for edge in edges
    }
    source_mappings = [
        mapping for mapping in source_mappings if mapping["object_id"] in used_participants
    ]
    record = {
        "id": pathway_id,
        "label": _pathway_label(root) or pathway_id,
        "description": f"BioPAX pathway {pathway_id}.",
        "pathway_type": "biopax-pathway",
        "taxa": _taxa(root, xref_by_ref),
        "participants": _unique_nodes(
            participant
            for participant in participant_by_ref.values()
            if participant["id"] in used_participants
        ),
        "reactions": reactions,
        "mechanistic_edges": [
            {"id": f"biopax-edge-{index}", **edge}
            for index, edge in enumerate(edges, start=1)
        ],
        "references": list(references.values()),
    }
    if source_mappings:
        record["source_mappings"] = unique_source_mappings(source_mappings)
    return record


def _unification_xrefs(root: ElementTree.Element) -> dict[str, NormalizedXref]:
    xrefs = {}
    for xref in _elements(root, "UnificationXref"):
        database = _text_child(xref, "db") or ""
        normalized_database = database.lower()
        identifier = _text_child(xref, "id")
        prefix = DB_PREFIXES.get(normalized_database)
        if prefix and identifier:
            xrefs[_element_ref(xref)] = NormalizedXref(
                source_id=_format_curie(_source_prefix(database, prefix), identifier),
                object_id=_format_curie(prefix, identifier),
            )
    return xrefs


def _participants(
    root: ElementTree.Element,
    xref_by_ref: dict[str, NormalizedXref],
    pathway_id: str,
) -> tuple[dict[str, dict[str, str]], list[dict[str, str]]]:
    reference_by_ref = _entity_references(root, xref_by_ref)
    participants = {}
    source_mappings = []
    for element_name in ["SmallMolecule", "Protein"]:
        for element in _elements(root, element_name):
            reference = _resource_child(element, "entityReference")
            if not reference or reference not in reference_by_ref:
                continue
            xref = reference_by_ref[reference]
            identifier = xref.object_id
            label = _text_child(element, "displayName") or identifier
            participants[_element_ref(element)] = {
                "id": identifier,
                "label": label,
            }
            if xref.source_id != xref.object_id:
                source_mappings.append(
                    source_mapping_row(
                        xref.source_id,
                        label,
                        CurieMapping(
                            subject_id=xref.source_id,
                            subject_label=label,
                            object_id=xref.object_id,
                            object_label=label,
                        ),
                        source_pathway_id=pathway_id,
                        source_element_id=_element_ref(element),
                    )
                )
    return participants, source_mappings


def _complex_components(root: ElementTree.Element) -> dict[str, list[str]]:
    components = {}
    for complex_element in _elements(root, "Complex"):
        components[_element_ref(complex_element)] = [
            _resource(component) for component in _children(complex_element, "component")
        ]
    return components


def _unique_nodes(nodes: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    unique: dict[str, dict[str, str]] = {}
    for node in nodes:
        unique.setdefault(node["id"], node)
    return list(unique.values())


def _entity_references(
    root: ElementTree.Element,
    xref_by_ref: dict[str, NormalizedXref],
) -> dict[str, NormalizedXref]:
    references = {}
    for element_name in ["SmallMoleculeReference", "ProteinReference"]:
        for element in _elements(root, element_name):
            xref = _resource_child(element, "xref")
            if xref in xref_by_ref:
                references[_element_ref(element)] = xref_by_ref[xref]
    return references


def _taxa(
    root: ElementTree.Element,
    xref_by_ref: dict[str, NormalizedXref],
) -> list[dict[str, str]]:
    taxa_by_ref = {}
    for source in _elements(root, "BioSource"):
        taxon_id = _curie_with_prefix(source, xref_by_ref, "NCBITaxon")
        if not taxon_id:
            continue
        taxa_by_ref[_element_ref(source)] = {
            "id": taxon_id,
            "label": _text_child(source, "name") or taxon_id,
        }

    taxa = []
    for pathway in _elements(root, "Pathway"):
        organism = _resource_child(pathway, "organism")
        if organism and organism in taxa_by_ref:
            taxa.append(taxa_by_ref[organism])
    return _unique_nodes(taxa)


def _pathway_id(
    root: ElementTree.Element,
    xref_by_ref: dict[str, NormalizedXref],
    source_prefix: str,
) -> str | None:
    pathway = next(iter(_elements(root, "Pathway")), None)
    if pathway is None:
        return None
    return _source_xref(pathway, xref_by_ref, source_prefix)


def _source_xref(
    element: ElementTree.Element,
    xref_by_ref: dict[str, NormalizedXref],
    source_prefix: str,
) -> str | None:
    return _curie_with_prefix(element, xref_by_ref, source_prefix)


def _curie_with_prefix(
    element: ElementTree.Element,
    xref_by_ref: dict[str, NormalizedXref],
    prefix: str,
) -> str | None:
    for xref in _children(element, "xref"):
        normalized_xref = xref_by_ref.get(_resource(xref))
        if normalized_xref and normalized_xref.object_id.startswith(f"{prefix}:"):
            return normalized_xref.object_id
    return None


def _side_participants(
    reaction: ElementTree.Element,
    side: str,
    participant_by_ref: dict[str, dict[str, str]],
) -> list[str]:
    participants = []
    for element in _children(reaction, side):
        resource = _resource(element)
        if resource not in participant_by_ref:
            continue
        participant_id = participant_by_ref[resource]["id"]
        if participant_id.startswith("CHEBI:"):
            participants.append(participant_id)
    return participants


def _controller_participants(
    controller_ref: str | None,
    participant_by_ref: dict[str, dict[str, str]],
    complex_components_by_ref: dict[str, list[str]],
    seen: set[str] | None = None,
) -> list[str]:
    if not controller_ref:
        return []
    if controller_ref in participant_by_ref:
        return [participant_by_ref[controller_ref]["id"]]

    seen = seen or set()
    if controller_ref in seen:
        return []
    seen.add(controller_ref)

    participants = []
    for component_ref in complex_components_by_ref.get(controller_ref, []):
        participants.extend(
            _controller_participants(
                component_ref,
                participant_by_ref,
                complex_components_by_ref,
                seen,
            )
        )
    return participants


def _publication_references(
    root: ElementTree.Element,
) -> tuple[dict[str, dict[str, str]], dict[str, str]]:
    references = {}
    publication_reference_by_ref = {}
    for publication in _elements(root, "PublicationXref"):
        pmid = _text_child(publication, "id")
        if not pmid or not pmid.isdigit():
            continue
        reference_id = f"PMID:{pmid}"
        publication_reference_by_ref[_element_ref(publication)] = reference_id
        references[reference_id] = {
            "id": reference_id,
            "title": _text_child(publication, "title")
            or f"BioPAX publication {reference_id}",
        }
    return references, publication_reference_by_ref


def _publication_reference_id(
    element: ElementTree.Element,
    publication_reference_by_ref: dict[str, str],
) -> str | None:
    for xref in _children(element, "xref"):
        reference_id = publication_reference_by_ref.get(_resource(xref))
        if reference_id:
            return reference_id
    return None


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
    evidence_quote: str | None = None,
) -> dict[str, Any]:
    return {
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "evidence": [
            {
                "reference_id": evidence_reference,
                "quote": _short_evidence_quote(evidence_quote)
                or f"BioPAX reaction cites {evidence_reference}.",
            }
        ],
    }


def _short_evidence_quote(evidence_quote: str | None) -> str | None:
    if not evidence_quote:
        return None
    return evidence_quote[:MAX_EVIDENCE_QUOTE_LENGTH]


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


def _source_prefix(database: str, object_prefix: str) -> str:
    if database.lower() == "uniprot":
        return "UniProt"
    return object_prefix


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]
