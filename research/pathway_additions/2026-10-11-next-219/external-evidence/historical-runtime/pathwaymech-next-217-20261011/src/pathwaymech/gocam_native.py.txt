"""Faithful projection of native Noctua individuals and facts.

The source model remains the evidence, including its limitations. Native facts
are not paper quotations, an input is not necessarily consumed, and a causal
upstream relation is not necessarily regulation. Generic physical individuals
retain their source IDs so redox states and unspecified proteins do not merge.
"""

from __future__ import annotations

import html
import re
from collections.abc import Callable
from typing import Any

NATIVE_PREDICATES = {
    "RO:0002333": "enables",  # Inverse of enabled_by.
    "RO:0002233": "has_input",
    "RO:0002234": "has_output",
    "RO:0002411": "causally_upstream_of",
    "RO:0002413": "provides_input_for",
    "RO:0002211": "regulates",
    "RO:0002212": "inhibits",
    "RO:0002213": "activates",
    "BFO:0000066": "occurs_in",
    "RO:0001025": "located_in",
    "BFO:0000050": "part_of",
    "BFO:0000051": "has_part",
}
GENERIC_CLASSES = {
    "CHEBI:24431", "CHEBI:33695", "CHEBI:36080", "PR:000000001",
}
ACTIVITY_ROOTS = {"GO:0003674", "obo:go/extensions/reacto.owl#molecular_event"}


def annotation_values(node: dict[str, Any], key: str) -> list[str]:
    return [a["value"] for a in node.get("annotations", [])
            if a.get("key") == key and isinstance(a.get("value"), str)]


def plain_label(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def activity_ids(model: dict[str, Any]) -> set[str]:
    return {n["id"] for n in model["individuals"]
            if ACTIVITY_ROOTS.intersection(t["id"] for t in n.get("root-type", []))}


def project_native_model(
    model: dict[str, Any],
    *,
    source_member: str,
    included_activities: set[str] | None = None,
    known_labels: dict[str, str] | None = None,
    chemical_category: Callable[[str], str | None] | None = None,
) -> dict[str, Any]:
    """Return nodes, edges and a disposition for *every* native source fact.

    ``included_activities`` is a scientifically reviewed scope, not an evidence
    filter. Excluded native facts are reported explicitly. Unknown predicates,
    dangling endpoints and ambiguous multiple classes fail rather than vanish.
    The caller supplies labels from an independent ontology or existing display
    curation; these never create new identifiers or source assertions.
    """
    individuals = {n["id"]: n for n in model["individuals"]}
    if len(individuals) != len(model["individuals"]):
        raise ValueError("duplicate native individual IDs")
    indexes = {n["id"]: i for i, n in enumerate(model["individuals"])}
    activities = activity_ids(model)
    included = activities if included_activities is None else included_activities
    if not included <= activities:
        raise ValueError(f"requested activities absent from model: {included - activities}")
    labels = known_labels or {}
    nodes: dict[str, dict[str, str]] = {}
    projections: dict[str, str] = {}

    def add_node(native_id: str) -> str:
        if native_id in projections:
            return projections[native_id]
        if native_id not in individuals:
            raise ValueError(f"dangling native endpoint {native_id}")
        individual = individuals[native_id]
        types = individual.get("type", [])
        if len(types) > 1:
            raise ValueError(f"ambiguous native types for {native_id}")
        term = types[0] if types else {}
        type_id = term.get("id", "")
        roots = {t["id"] for t in individual.get("root-type", [])}
        native_labels = annotation_values(individual, "rdfs:label")
        category = None
        if native_id in activities:
            identifier = native_id
            category = "molecular_activity"
            label = term.get("label") if type_id.startswith("GO:") else None
            label = label or (native_labels[0] if native_labels else term.get("label", native_id))
        else:
            # Unsupported external prefixes retain independently existing native
            # instances; their external type is still in the exact locator.
            identifier = (type_id if type_id and type_id not in GENERIC_CLASSES
                          and type_id.split(":", 1)[0] in {"GO", "CHEBI", "SGD", "UniProtKB"}
                          else native_id)
            label = (term.get("label") if identifier == type_id else None)
            label = label or (native_labels[0] if native_labels else term.get("label", native_id))
            if "GO:0032991" in roots:
                category = "complex"
            elif "GO:0005575" in roots:
                category = "cellular_component"
            elif "GO:0008150" in roots:
                category = "biological_process"
            elif type_id.startswith(("SGD:", "UniProtKB:", "EcoCyc:", "PR:")):
                category = "protein"
            elif any(x.endswith(".Protein") for x in annotation_values(individual, "skos:note")):
                category = "protein"
            elif chemical_category and type_id.startswith("CHEBI:"):
                category = chemical_category(type_id)
            elif "CHEBI:36080" in roots:
                category = "protein"
        node = {"id": identifier, "label": labels.get(identifier, plain_label(label or native_id))}
        if category:
            node["category"] = category
        if identifier in nodes and nodes[identifier].get("category") != node.get("category"):
            raise ValueError(f"inconsistent category for {identifier}")
        nodes.setdefault(identifier, node)
        projections[native_id] = identifier
        return identifier

    for identifier in sorted(included):
        add_node(identifier)
    edges: dict[tuple[str, str, str], dict[str, Any]] = {}
    dispositions = []
    for index, fact in enumerate(model["facts"]):
        source, target, relation = fact["subject"], fact["object"], fact["property"]
        if relation not in NATIVE_PREDICATES:
            raise ValueError(f"unsupported source predicate {relation}")
        if source not in individuals or target not in individuals:
            raise ValueError(f"dangling native fact {index}")
        disposition: dict[str, Any] = {"fact_index": index, "subject": source,
                                       "predicate": relation, "object": target}
        excluded = {source, target}.intersection(activities - included)
        if excluded:
            disposition.update(status="excluded_activity_scope", activities=sorted(excluded))
            dispositions.append(disposition)
            continue
        subject, obj = add_node(source), add_node(target)
        predicate = NATIVE_PREDICATES[relation]
        if relation == "RO:0002333":
            subject, obj = obj, subject
        key = subject, predicate, obj
        if key not in edges:
            edges[key] = {"id": f"edge-{len(edges) + 1:03d}", "subject": subject,
                          "predicate": predicate, "object": obj, "evidence": []}
        assertion = f"The model asserts {source} {relation} {target}."
        if len(assertion) > 400:
            assertion = f"The native {relation} assertion projects to {subject} {predicate} {obj}."
        if len(assertion) > 400:
            raise ValueError(f"source assertion too long at fact {index}")
        locator = (f"{source_member}#/facts/{index}; endpoint types: "
                   f"/individuals/{indexes[source]}/type; /individuals/{indexes[target]}/type")
        evidence = {"reference_id": model["id"], "source_assertion": assertion,
                    "source_locator": locator}
        edges[key]["evidence"].append(evidence)
        disposition.update(status="represented", edge_id=edges[key]["id"])
        dispositions.append(disposition)
    return {
        "participants": [n for n in nodes.values() if n["id"] not in included],
        "reactions": [n for n in nodes.values() if n["id"] in included],
        "mechanistic_edges": list(edges.values()),
        "facts": dispositions,
        "individual_projections": projections,
    }
