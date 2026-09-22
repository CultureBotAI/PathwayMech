from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ALLOWED_RO_PREDICATES = {
    "RO:0002211": "regulates",
    "RO:0002212": "inhibits",
    "RO:0002213": "activates",
    "RO:0002411": "regulates",
    "RO:0002413": "precedes",
}


def load_gocam_model(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a GO-CAM JSON object")
    return value


def gocam_to_pathway_record(model: dict[str, Any]) -> dict[str, Any]:
    model_id = _required_string(model, "id")
    label_by_id = _object_labels(model)
    participants: dict[str, dict[str, str]] = {}
    reactions: dict[str, dict[str, str]] = {}
    references: dict[str, dict[str, str]] = {}
    edges: list[dict[str, Any]] = []

    def add_participant(identifier: str) -> None:
        participants.setdefault(
            identifier,
            {"id": identifier, "label": label_by_id.get(identifier, identifier)},
        )

    def add_reference(identifier: str) -> None:
        references.setdefault(
            identifier,
            {
                "id": identifier,
                "title": f"GO-CAM evidence reference {identifier}",
            },
        )

    def make_evidence(raw_evidence: list[dict[str, Any]]) -> list[dict[str, str]]:
        evidence = []
        for item in raw_evidence:
            reference_id = item.get("reference")
            evidence_code = item.get("term")
            if not isinstance(reference_id, str) or not isinstance(evidence_code, str):
                continue
            add_reference(reference_id)
            evidence.append(
                {
                    "reference_id": reference_id,
                    "quote": f"GO-CAM evidence {evidence_code} cites {reference_id}.",
                }
            )
        return evidence

    for activity in _activities(model):
        activity_id = _required_string(activity, "id")
        reaction_label = activity_id
        molecular_function = activity.get("molecular_function")
        if isinstance(molecular_function, dict):
            term = molecular_function.get("term")
            if isinstance(term, str):
                reaction_label = label_by_id.get(term, term)
        reactions.setdefault(activity_id, {"id": activity_id, "label": reaction_label})

    for activity in _activities(model):
        activity_id = _required_string(activity, "id")

        enabled_by = activity.get("enabled_by")
        if isinstance(enabled_by, dict):
            enabler_id = enabled_by.get("term")
            evidence = make_evidence(_evidence(enabled_by))
            if isinstance(enabler_id, str) and evidence:
                add_participant(enabler_id)
                edges.append(
                    _edge(
                        subject=enabler_id,
                        predicate="enables",
                        obj=activity_id,
                        evidence=evidence,
                    )
                )

        for association in _molecule_associations(activity, "has_input"):
            term = association.get("term")
            evidence = make_evidence(_evidence(association))
            if isinstance(term, str) and evidence:
                add_participant(term)
                edges.append(
                    _edge(
                        subject=term,
                        predicate="consumes",
                        obj=activity_id,
                        evidence=evidence,
                    )
                )

        for association in _molecule_associations(activity, "has_output"):
            term = association.get("term")
            evidence = make_evidence(_evidence(association))
            if isinstance(term, str) and evidence:
                add_participant(term)
                edges.append(
                    _edge(
                        subject=activity_id,
                        predicate="produces",
                        obj=term,
                        evidence=evidence,
                    )
                )

        for association in _causal_associations(activity):
            downstream_activity = association.get("downstream_activity")
            predicate = ALLOWED_RO_PREDICATES.get(str(association.get("predicate")))
            evidence = make_evidence(_evidence(association))
            if isinstance(downstream_activity, str) and predicate and evidence:
                reactions.setdefault(
                    downstream_activity,
                    {
                        "id": downstream_activity,
                        "label": label_by_id.get(
                            downstream_activity,
                            downstream_activity,
                        ),
                    },
                )
                edges.append(
                    _edge(
                        subject=activity_id,
                        predicate=predicate,
                        obj=downstream_activity,
                        evidence=evidence,
                    )
                )

    taxon = _required_string(model, "taxon")
    title = _required_string(model, "title")
    return {
        "id": model_id,
        "label": title,
        "description": f"GO-CAM causal activity model {model_id}.",
        "pathway_type": "causal-activity-model",
        "taxa": [{"id": taxon, "label": model.get("taxon_label") or taxon}],
        "participants": list(participants.values()),
        "reactions": list(reactions.values()),
        "mechanistic_edges": [
            {"id": f"gocam-edge-{index}", **edge}
            for index, edge in enumerate(edges, start=1)
        ],
        "references": list(references.values()),
    }


def _activities(model: dict[str, Any]) -> list[dict[str, Any]]:
    return [item for item in model.get("activities") or [] if isinstance(item, dict)]


def _object_labels(model: dict[str, Any]) -> dict[str, str]:
    labels = {}
    for item in model.get("objects") or []:
        if not isinstance(item, dict):
            continue
        identifier = item.get("id")
        label = item.get("label")
        if isinstance(identifier, str) and isinstance(label, str):
            labels[identifier] = label
    return labels


def _molecule_associations(
    activity: dict[str, Any],
    field: str,
) -> list[dict[str, Any]]:
    value = activity.get(field)
    if isinstance(value, dict):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    return []


def _causal_associations(activity: dict[str, Any]) -> list[dict[str, Any]]:
    value = activity.get("causal_associations")
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _evidence(association: dict[str, Any]) -> list[dict[str, Any]]:
    value = association.get("evidence")
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _edge(
    subject: str,
    predicate: str,
    obj: str,
    evidence: list[dict[str, str]],
) -> dict[str, Any]:
    return {
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "evidence": evidence,
    }


def _required_string(model: dict[str, Any], field: str) -> str:
    value = model.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"GO-CAM model missing string field: {field}")
    return value
