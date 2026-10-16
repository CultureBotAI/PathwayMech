"""Record-local mechanistic statements beneath an externally identified reaction.

Step keys are claim coordinates, never biological identifiers. The public nodes
are declarations already checked by the record's identifier authority gate.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Callable, Iterator
from typing import Any

_KEY = re.compile(r"[a-z][a-z0-9_-]{0,63}")
_CHEMICAL = {"chemical_entity", "small_molecule", "lipid", "polymer", "cofactor"}
_STATUS = {"supported", "inferred", "proposed"}
_PREDICATES = {
    "consumes",
    "produces",
    "catalyzes",
    "enables",
    "provides_input_for",
    "precedes",
    "occurs_in",
}


def iter_mechanism_evidence(value: Any) -> Iterator[dict]:
    """Include mechanism-, step-, edge-, qualifier-, hypothesis- and conflict-only evidence."""
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "evidence":
                yield from child
            else:
                yield from iter_mechanism_evidence(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_mechanism_evidence(child)


def mechanism_equation(mechanism: dict) -> dict[str, list[dict]]:
    """Exact signed material sum for a validated, single-location detail graph."""
    net: Counter = Counter()
    for edge in mechanism["edges"]:
        if edge["predicate"] == "consumes":
            net[edge["subject"]["node_id"]] -= edge["coefficient"]
        elif edge["predicate"] == "produces":
            net[edge["object"]["node_id"]] += edge["coefficient"]
    return {
        side: [
            {"participant_id": node, "coefficient": abs(quantity)}
            for node, quantity in sorted(net.items())
            if quantity * sign > 0
        ]
        for side, sign in (("inputs", -1), ("outputs", 1))
    }


def validate_reaction_mechanisms(
    value: Any,
    record: dict,
    reference_ids: set[str],
    errors: list[str],
    *,
    validate_evidence: Callable,
    validate_qualifiers: Callable,
) -> list[dict]:
    """Validate the closed nested contract without creating an authority namespace."""

    def closed(item: Any, fields: set[str], path: str) -> bool:
        if not isinstance(item, dict):
            errors.append(f"{path} must be a mapping")
            return False
        if set(item) - fields:
            errors.append(f"{path} has unsupported fields: {sorted(map(str, set(item) - fields))}")
        if any(v is None for v in item.values()):
            errors.append(f"{path} cannot contain null values")
        return True

    def text(item: dict, field: str, path: str) -> None:
        v = item.get(field)
        if not isinstance(v, str) or not v.strip():
            errors.append(f"{path}.{field} must be a non-empty string")

    def choice(item: dict, field: str, allowed: set[str], path: str) -> None:
        v = item.get(field)
        if not isinstance(v, str) or v not in allowed:
            errors.append(f"{path}.{field} is not supported: {v!r}")

    def coefficient(item: dict, path: str) -> bool:
        v = item.get("coefficient")
        if type(v) is not int or v < 1:
            errors.append(f"{path}.coefficient must be a positive integer")
            return False
        return True

    def evidence(item: dict, path: str) -> None:
        v = item.get("evidence")
        validate_evidence(v, reference_ids, f"{path}.evidence", errors)
        if isinstance(v, list):
            for i, e in enumerate(v):
                closed(
                    e,
                    {"reference_id", "quote", "source_assertion", "source_locator"},
                    f"{path}.evidence[{i}]",
                )

    def entries(v: Any, path: str, *, nonempty: bool = True) -> list:
        if not isinstance(v, list) or (nonempty and not v):
            errors.append(f"{path} must be a {'non-empty ' if nonempty else ''}list")
            return []
        return v

    def key(item: dict, seen: set[str], path: str) -> str | None:
        v = item.get("key")
        if not isinstance(v, str) or not _KEY.fullmatch(v):
            errors.append(f"{path}.key must be a local ASCII claim key, not a CURIE")
            return None
        if v in seen:
            errors.append(f"{path}.key is duplicated: {v}")
        seen.add(v)
        return v

    declarations: dict[str, list[tuple[str, dict]]] = {}
    for field in ("taxa", "participants", "reactions"):
        for node in record.get(field, []) if isinstance(record.get(field), list) else []:
            if isinstance(node, dict) and isinstance(node.get("id"), str):
                declarations.setdefault(node["id"], []).append((field, node))

    def kind(identifier: Any, field: str) -> str | None:
        if not isinstance(identifier, str) or identifier == record.get("id"):
            return None
        matches = declarations.get(identifier, [])
        if len(matches) != 1 or matches[0][0] != field:
            return None
        category = matches[0][1].get("category")
        return category if isinstance(category, str) else None

    proteins = {n for n in declarations if kind(n, "participants") in {"protein", "complex"}}
    mechanisms = entries(value, "reaction_mechanisms", nonempty=False)
    mechanism_keys: set[str] = set()
    for mi, mechanism in enumerate(mechanisms):
        path = f"reaction_mechanisms[{mi}]"
        if not closed(
            mechanism,
            {
                "version",
                "key",
                "source_reaction_id",
                "relation_to_source",
                "description",
                "evidence",
                "source_equation",
                "steps",
                "edges",
                "source_conflicts",
            },
            path,
        ):
            continue
        key(mechanism, mechanism_keys, path)
        if type(mechanism.get("version")) is not int or mechanism["version"] != 1:
            errors.append(f"{path}.version must be 1")
        if kind(mechanism.get("source_reaction_id"), "reactions") != "molecular_activity":
            errors.append(f"{path}.source_reaction_id must be one declared molecular_activity")
        choice(
            mechanism, "relation_to_source", {"decomposition", "alternative_interpretation"}, path
        )
        text(mechanism, "description", path)
        evidence(mechanism, path)

        equation = mechanism.get("source_equation")
        source: dict[str, dict[str, int]] = {"inputs": {}, "outputs": {}}
        if closed(equation, {"orientation", "inputs", "outputs"}, f"{path}.source_equation"):
            choice(equation, "orientation", {"as_reported", "reversed"}, f"{path}.source_equation")
            for side in source:
                p = f"{path}.source_equation.{side}"
                for ti, term in enumerate(entries(equation.get(side), p)):
                    tp = f"{p}[{ti}]"
                    if not closed(term, {"participant_id", "coefficient"}, tp):
                        continue
                    identifier = term.get("participant_id")
                    if kind(identifier, "participants") not in _CHEMICAL:
                        errors.append(
                            f"{tp}.participant_id must be one declared chemical participant"
                        )
                    if coefficient(term, tp) and isinstance(identifier, str):
                        if identifier in source[side]:
                            errors.append(f"{tp} duplicates a source equation term")
                        source[side][identifier] = term["coefficient"]
            if source["inputs"].keys() & source["outputs"].keys():
                errors.append(f"{path}.source_equation must be a net equation without shared terms")
            if equation.get("orientation") == "reversed":
                source = {"inputs": source["outputs"], "outputs": source["inputs"]}

        step_keys: set[str] = set()
        for si, step in enumerate(entries(mechanism.get("steps"), f"{path}.steps")):
            sp = f"{path}.steps[{si}]"
            if not closed(
                step,
                {"key", "label", "description", "assertion_status", "evidence", "hypotheses"},
                sp,
            ):
                continue
            key(step, step_keys, sp)
            text(step, "label", sp)
            text(step, "description", sp)
            choice(step, "assertion_status", _STATUS, sp)
            evidence(step, sp)
            if "hypotheses" in step:
                for hi, hypothesis in enumerate(entries(step["hypotheses"], f"{sp}.hypotheses")):
                    hp = f"{sp}.hypotheses[{hi}]"
                    if closed(hypothesis, {"description", "status", "evidence"}, hp):
                        text(hypothesis, "description", hp)
                        choice(hypothesis, "status", {"proposed"}, hp)
                        evidence(hypothesis, hp)

        def endpoint(v: Any, ep: str, local_steps=step_keys) -> tuple[str, str] | None:
            if not closed(v, {"node_id", "step_key"}, ep):
                return None
            if len(v) != 1:
                errors.append(f"{ep} must contain exactly one node_id or step_key")
                return None
            field, identifier = next(iter(v.items()))
            if not isinstance(identifier, str):
                errors.append(f"{ep} must reference a string identifier")
                return None
            if field == "step_key" and identifier in local_steps:
                return (field, identifier)
            if field == "node_id" and kind(identifier, "participants") is not None:
                return (field, identifier)
            errors.append(f"{ep} does not resolve to a typed participant or this mechanism's step")
            return None

        edge_keys: set[str] = set()
        materials: set[tuple[str, str, str]] = set()
        locations: dict[str, list[str]] = {s: [] for s in step_keys}
        nested_net: Counter = Counter()
        for ei, edge in enumerate(entries(mechanism.get("edges"), f"{path}.edges")):
            ep = f"{path}.edges[{ei}]"
            if not closed(
                edge,
                {
                    "key",
                    "subject",
                    "object",
                    "predicate",
                    "description",
                    "assertion_status",
                    "evidence",
                    "coefficient",
                    "endpoint_qualifiers",
                },
                ep,
            ):
                continue
            key(edge, edge_keys, ep)
            choice(edge, "predicate", _PREDICATES, ep)
            choice(edge, "assertion_status", _STATUS, ep)
            if "description" in edge:
                text(edge, "description", ep)
            evidence(edge, ep)
            subject = endpoint(edge.get("subject"), f"{ep}.subject")
            obj = endpoint(edge.get("object"), f"{ep}.object")
            if "endpoint_qualifiers" in edge:
                proxy = {
                    "subject": subject[1] if subject and subject[0] == "node_id" else None,
                    "object": obj[1] if obj and obj[0] == "node_id" else None,
                    "endpoint_qualifiers": edge["endpoint_qualifiers"],
                }
                validate_qualifiers(proxy, proteins, reference_ids, ep, errors)
                if isinstance(edge["endpoint_qualifiers"], list):
                    for qi, qualifier in enumerate(edge["endpoint_qualifiers"]):
                        if isinstance(qualifier, dict):
                            evidence(qualifier, f"{ep}.endpoint_qualifiers[{qi}]")
            predicate = edge.get("predicate")
            if not isinstance(predicate, str):
                continue
            if predicate not in {"consumes", "produces"} and "coefficient" in edge:
                errors.append(f"{ep}.coefficient is only permitted on material edges")
            if not subject or not obj:
                continue
            valid = False
            if predicate in {"consumes", "produces"}:
                material, step = (subject, obj) if predicate == "consumes" else (obj, subject)
                valid = (
                    material[0] == "node_id"
                    and step[0] == "step_key"
                    and kind(material[1], "participants") in _CHEMICAL
                )
                if coefficient(edge, ep) and valid:
                    term_key = (step[1], material[1], predicate)
                    if term_key in materials:
                        errors.append(f"{ep} duplicates a step/material/side term")
                    materials.add(term_key)
                    nested_net[material[1]] += edge["coefficient"] * (
                        -1 if predicate == "consumes" else 1
                    )
            elif predicate in {"catalyzes", "enables"}:
                valid = subject[0] == "node_id" and subject[1] in proteins and obj[0] == "step_key"
            elif predicate in {"provides_input_for", "precedes"}:
                valid = subject[0] == obj[0] == "step_key" and subject != obj
            elif predicate == "occurs_in":
                valid = (
                    subject[0] == "step_key"
                    and obj[0] == "node_id"
                    and kind(obj[1], "participants") == "cellular_component"
                )
                if valid:
                    locations[subject[1]].append(obj[1])
            if not valid:
                errors.append(f"{ep} has invalid endpoint kinds for {predicate!r}")

        for step in step_keys:
            for predicate in ("consumes", "produces"):
                if not any(s == step and p == predicate for s, _, p in materials):
                    errors.append(f"{path}.steps[{step}] needs explicit inputs and outputs")
        if any(locations.values()) and (
            any(len(v) != 1 for v in locations.values())
            or len({v[0] for v in locations.values() if v}) != 1
        ):
            errors.append(
                f"{path} requires one identical explicit location for every step, "
                "or no locations; transport cannot be inferred"
            )

        interpreted = {
            side: {n: abs(c) for n, c in nested_net.items() if c * sign > 0}
            for side, sign in (("inputs", -1), ("outputs", 1))
        }
        if not all(interpreted.values()):
            errors.append(f"{path} must have a nonempty net input and output")
        if mechanism.get("relation_to_source") == "decomposition":
            if "source_conflicts" in mechanism:
                errors.append(f"{path} decomposition cannot have source_conflicts")
            if source != interpreted:
                errors.append(f"{path} decomposition does not match the exact source equation")
        elif mechanism.get("relation_to_source") == "alternative_interpretation":
            _validate_conflicts(
                mechanism,
                path,
                source,
                interpreted,
                errors,
                closed,
                entries,
                choice,
                coefficient,
                text,
                evidence,
            )
    detail_only = record.get("detail_only_participant_ids", [])
    if not isinstance(detail_only, list):
        errors.append("detail_only_participant_ids must be a list")
        return mechanisms
    seen_detail: set[str] = set()
    detail_endpoints: set[str] = set()
    source_nodes: set[str] = set()
    top_edges = record.get("mechanistic_edges")
    for edge in top_edges if isinstance(top_edges, list) else []:
        if isinstance(edge, dict):
            for role in ("subject", "object"):
                if isinstance(edge.get(role), str):
                    source_nodes.add(edge[role])
    for mechanism in mechanisms:
        if not isinstance(mechanism, dict):
            continue
        for edge in mechanism.get("edges", []) if isinstance(mechanism.get("edges"), list) else []:
            if isinstance(edge, dict):
                for role in ("subject", "object"):
                    endpoint_value = edge.get(role)
                    if isinstance(endpoint_value, dict) and isinstance(
                        endpoint_value.get("node_id"), str
                    ):
                        detail_endpoints.add(endpoint_value["node_id"])
        equation = mechanism.get("source_equation")
        if isinstance(equation, dict):
            for side in ("inputs", "outputs"):
                for term in equation.get(side, []) if isinstance(equation.get(side), list) else []:
                    if isinstance(term, dict) and isinstance(term.get("participant_id"), str):
                        source_nodes.add(term["participant_id"])
        conflicts = mechanism.get("source_conflicts", [])
        if isinstance(conflicts, list):
            for conflict in conflicts:
                if isinstance(conflict, dict) and isinstance(
                    conflict.get("source_participant_id"), str
                ):
                    source_nodes.add(conflict["source_participant_id"])
    for identifier in detail_only:
        if not isinstance(identifier, str) or kind(identifier, "participants") is None:
            errors.append(
                "detail_only_participant_ids must identify uniquely declared participants"
            )
            continue
        if identifier in seen_detail:
            errors.append("detail_only_participant_ids contains a duplicate")
        seen_detail.add(identifier)
        if identifier not in detail_endpoints or identifier in source_nodes:
            errors.append(
                f"detail-only participant {identifier} must be used in detail and absent "
                "from top-level edges and source equations/conflict terms"
            )
    return mechanisms


def _validate_conflicts(
    mechanism,
    path,
    source,
    interpreted,
    errors,
    closed,
    entries,
    choice,
    coefficient,
    text,
    evidence,
):
    """Only whole-term, same-side, equal-quantity substitutions are supported."""
    expected = {
        side: {
            "source": {n: c for n, c in source[side].items() if n not in interpreted[side]},
            "interpreted": {n: c for n, c in interpreted[side].items() if n not in source[side]},
        }
        for side in source
    }
    for side in source:
        for node in source[side].keys() & interpreted[side].keys():
            if source[side][node] != interpreted[side][node]:
                errors.append(
                    f"{path} cannot disguise a shared term's coefficient change "
                    "as a source substitution"
                )
    covered = {side: {"source": {}, "interpreted": {}} for side in source}
    conflicts = entries(mechanism.get("source_conflicts"), f"{path}.source_conflicts")
    for ci, conflict in enumerate(conflicts):
        cp = f"{path}.source_conflicts[{ci}]"
        if not closed(
            conflict,
            {
                "source_participant_id",
                "interpreted_participant_id",
                "side",
                "coefficient",
                "kind",
                "status",
                "rationale",
                "evidence",
            },
            cp,
        ):
            continue
        choice(conflict, "side", {"inputs", "outputs"}, cp)
        choice(conflict, "kind", {"stereo", "constitution", "microstate"}, cp)
        choice(conflict, "status", {"unresolved", "proposed_revision", "supported_revision"}, cp)
        text(conflict, "rationale", cp)
        evidence(conflict, cp)
        valid_quantity = coefficient(conflict, cp)
        side = conflict.get("side")
        if not isinstance(side, str) or side not in expected:
            continue
        for role, field in (
            ("source", "source_participant_id"),
            ("interpreted", "interpreted_participant_id"),
        ):
            identifier = conflict.get(field)
            if not isinstance(identifier, str) or identifier not in expected[side][role]:
                errors.append(f"{cp}.{field} must identify an unmatched {side} term")
                continue
            if identifier in covered[side][role]:
                errors.append(f"{cp} repeats a source conflict term")
            if valid_quantity:
                covered[side][role][identifier] = conflict["coefficient"]
    if covered != expected or not any(v for side in expected.values() for v in side.values()):
        errors.append(
            f"{path}.source_conflicts must cover every boundary difference exactly "
            "once with equal coefficients on the same side"
        )
