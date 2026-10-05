from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

from pathwaymech.source_mapping import CurieMapping, source_mapping_row, unique_source_mappings

RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
DB_PREFIXES = {
    "chebi": "CHEBI",
    "go": "GO",
    "gene ontology": "GO",
    "ncbi taxonomy": "NCBITaxon",
    "panther": "PANTHER",
    "panther pathway": "PANTHER",
    "pantherdb": "PANTHER",
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
    """Preserve native conversion direction and physical catalytic assemblies.

    Source comments and publication links do not establish a verbatim quotation
    from the linked publication. Evidence therefore cites the BioPAX objects.
    """
    source_prefix = fallback_id.split(":", 1)[0]
    xrefs = _unification_xrefs(root)
    pathway_id = _pathway_id(root, xrefs, source_prefix) or fallback_id
    references, _ = _publication_references(root)
    references[pathway_id] = _fallback_reference(pathway_id)
    participants, mappings = _participants(root, xrefs, pathway_id)
    physical_types = {
        "SmallMolecule": "small_molecule",
        "Protein": "protein",
        "Complex": "complex",
        "Dna": "dna",
        "DnaRegion": "dna",
        "Rna": "rna",
        "RnaRegion": "rna",
        "PhysicalEntity": None,
    }
    elements = {_element_ref(e): e for e in root if _local_name(e.tag) in physical_types}
    side_refs = {
        _resource(e)
        for reaction in _elements(root, "BiochemicalReaction")
        for side in ("left", "right")
        for e in _children(reaction, side)
    }
    # A protein entityReference identifies a sequence, not its modification state.
    # Distinct source physical objects must not collapse across a conversion or
    # across cellular compartments merely because they share a database xref.
    contexts: dict[str, set[tuple[str | None, tuple[str, ...]]]] = {}
    for native, node in participants.items():
        e = elements[native]
        context = (
            _resource_child(e, "cellularLocation"),
            tuple(sorted(_resource(f) for f in _children(e, "feature"))),
        )
        contexts.setdefault(node["id"], set()).add(context)
    for native, e in elements.items():
        kind = _local_name(e.tag)
        previous = participants.get(native)
        needs_native = (
            previous is None
            or kind == "Complex"
            or (kind in {"Protein", "Dna", "DnaRegion", "Rna", "RnaRegion"} and native in side_refs)
            or len(contexts.get(previous["id"], set())) > 1
        )
        if needs_native:
            identifier = _source_xref(e, xrefs, source_prefix) or f"{pathway_id}/{native}"
            participants[native] = {
                "id": identifier,
                "label": _text_child(e, "displayName") or _text_child(e, "standardName") or native,
            }
            if physical_types[kind]:
                participants[native]["category"] = physical_types[kind]
    locations = {}
    for loc in _elements(root, "CellularLocationVocabulary"):
        identifier = _curie_with_prefix(loc, xrefs, "GO")
        if identifier:
            locations[_element_ref(loc)] = {
                "id": identifier,
                "label": _text_child(loc, "term") or identifier,
                "category": "cellular_component",
            }
    edges = []
    reactions = []
    reaction_by_ref = {}
    used_refs: set[str] = set()
    for reaction in _elements(root, "BiochemicalReaction"):
        native = _element_ref(reaction)
        rid = _source_xref(reaction, xrefs, source_prefix) or f"{pathway_id}/{native}"
        direction, orientation, direction_locator = _conversion_direction(root, reaction)
        reaction_by_ref[native] = rid
        reactions.append(
            {
                "id": rid,
                "label": _text_child(reaction, "displayName") or native,
                "direction": direction.lower().replace("-", "_"),
            }
        )
        local_locations = []
        for side in ("left", "right"):
            for participant in _children(reaction, side):
                pref = _resource(participant)
                if pref not in participants:
                    raise ValueError(
                        f"BioPAX {native}/{side} has unresolved physical entity {pref}"
                    )
                used_refs.add(pref)
                node = participants[pref]
                consumed = (side == "left") != (orientation == "RIGHT-TO-LEFT")
                s, p, o = (
                    (node["id"], "consumes", rid) if consumed else (rid, "produces", node["id"])
                )
                edges.append(
                    _edge(
                        s,
                        p,
                        o,
                        pathway_id,
                        (
                            f"BioPAX {native} places physical entity {pref} on its {side} side; "
                            f"conversion direction is {direction}; "
                            f"displayed orientation is {orientation}."
                        ),
                        f"#{native}/bp:{side}/#{pref}; {direction_locator}",
                    )
                )
                local_locations.append(_resource_child(elements[pref], "cellularLocation"))
        if local_locations and None not in local_locations and len(set(local_locations)) == 1:
            location = locations.get(local_locations[0])
            if location:
                edges.append(
                    _edge(
                        rid,
                        "occurs_in",
                        location["id"],
                        pathway_id,
                        (
                            f"All physical entities on both sides of BioPAX {native} "
                            "have the same cellular location."
                        ),
                        (
                            f"#{native}/bp:left|bp:right; "
                            f"physicalEntity/bp:cellularLocation/#{local_locations[0]}"
                        ),
                    )
                )
    for catalysis in _elements(root, "Catalysis"):
        controlled = _resource_child(catalysis, "controlled")
        if controlled not in reaction_by_ref:
            continue
        controller = _resource_child(catalysis, "controller")
        if controller not in participants:
            raise ValueError(f"BioPAX catalysis has unresolved controller {controller}")
        if _local_name(elements[controller].tag) not in {"Protein", "Complex"}:
            raise ValueError(
                f"BioPAX catalysis controller {controller} is not a protein or complex"
            )
        used_refs.add(controller)
        edges.append(
            _edge(
                participants[controller]["id"],
                "catalyzes",
                reaction_by_ref[controlled],
                pathway_id,
                f"BioPAX {_element_ref(catalysis)} names {controller} as its catalytic controller.",
                (
                    f"#{_element_ref(catalysis)}/bp:controller/#{controller}; "
                    f"bp:controlled/#{controlled}"
                ),
            )
        )
    pending = list(used_refs)
    visited = set()
    while pending:
        native = pending.pop()
        if native in visited:
            continue
        visited.add(native)
        e = elements[native]
        for component in _children(e, "component"):
            cref = _resource(component)
            if cref not in participants:
                raise ValueError(f"BioPAX complex {native} has unresolved component {cref}")
            used_refs.add(cref)
            pending.append(cref)
            edges.append(
                _edge(
                    participants[native]["id"],
                    "has_part",
                    participants[cref]["id"],
                    pathway_id,
                    f"BioPAX complex {native} explicitly includes physical entity {cref}.",
                    f"#{native}/bp:component/#{cref}",
                )
            )
        locref = _resource_child(e, "cellularLocation")
        if locref in locations:
            edges.append(
                _edge(
                    participants[native]["id"],
                    "located_in",
                    locations[locref]["id"],
                    pathway_id,
                    f"BioPAX physical entity {native} is assigned to cellular location {locref}.",
                    f"#{native}/bp:cellularLocation/#{locref}",
                )
            )
    used_ids = {e[k] for e in edges for k in ("subject", "object")}
    record = {
        "id": pathway_id,
        "label": _pathway_label(root) or pathway_id,
        "description": f"BioPAX pathway {pathway_id}.",
        "pathway_type": "biopax-pathway",
        "taxa": _taxa(root, xrefs),
        "participants": _unique_nodes(
            [
                *(participants[n] for n in participants if n in used_refs),
                *(n for n in locations.values() if n["id"] in used_ids),
            ]
        ),
        "reactions": reactions,
        "mechanistic_edges": [{"id": f"biopax-edge-{i}", **e} for i, e in enumerate(edges, 1)],
        "references": list(references.values()),
    }
    mappings = [m for m in mappings if m["object_id"] in used_ids]
    if mappings:
        record["source_mappings"] = unique_source_mappings(mappings)
    return record


def _conversion_direction(
    root: ElementTree.Element, reaction: ElementTree.Element
) -> tuple[str, str, str]:
    """BioPAX left/right are sides, not implicit reactant/product assignments."""
    native = _element_ref(reaction)
    conversion = _text_child(reaction, "conversionDirection")
    controls = {
        _element_ref(c): _text_child(c, "catalysisDirection")
        for c in _elements(root, "Catalysis")
        if _resource_child(c, "controlled") == native and _text_child(c, "catalysisDirection")
    }
    steps = {
        _element_ref(step): _text_child(step, "stepDirection")
        for step in _elements(root, "BiochemicalPathwayStep")
        if _resource_child(step, "stepConversion") == native and _text_child(step, "stepDirection")
    }
    directed = {"LEFT-TO-RIGHT", "RIGHT-TO-LEFT"}
    if conversion is not None and conversion not in directed | {"REVERSIBLE"}:
        raise ValueError(f"BioPAX {native} has invalid conversion direction {conversion}")
    contextual = set(controls.values()) | set(steps.values())
    if not contextual <= directed:
        raise ValueError(f"BioPAX {native} has invalid contextual direction")
    if conversion in directed and contextual - {conversion}:
        raise ValueError(f"BioPAX {native} has contradictory direction assertions")
    if len(set(steps.values())) > 1:
        raise ValueError(f"BioPAX {native} has conflicting pathway-step directions")
    if steps:
        orientation = next(iter(steps.values()))
        locator = "; ".join(f"#{step}/bp:stepDirection" for step in steps)
        return conversion or orientation, orientation, locator
    if conversion is not None:
        orientation = "LEFT-TO-RIGHT" if conversion == "REVERSIBLE" else conversion
        return conversion, orientation, f"#{native}/bp:conversionDirection"
    if len(set(controls.values())) == 1:
        direction = next(iter(controls.values()))
        locator = "; ".join(f"#{control}/bp:catalysisDirection" for control in controls)
        return direction, direction, locator
    raise ValueError(f"BioPAX {native} needs an explicit conversion direction")


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
            "title": _text_child(publication, "title") or f"BioPAX publication {reference_id}",
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
    source_assertion: str,
    source_locator: str,
) -> dict[str, Any]:
    return {
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "evidence": [
            {
                "reference_id": evidence_reference,
                "source_assertion": source_assertion,
                "source_locator": source_locator,
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


def _source_prefix(database: str, object_prefix: str) -> str:
    if database.lower() == "uniprot":
        return "UniProt"
    return object_prefix


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]
