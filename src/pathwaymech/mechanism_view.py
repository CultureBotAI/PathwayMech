"""Readable, evidence-complete views of record-local mechanistic claims.

The renderer consumes validated objects. Local navigation and graph keys never
become external reaction identifiers or alter the source graph's assertions.
"""
from __future__ import annotations

import html
import json
from collections.abc import Callable

from pathwaymech.graph_view import display_graph_html
from pathwaymech.reaction_mechanisms import mechanism_equation
from pathwaymech.site_display import autolink_html, label_html, plain_label


def mechanism_anchor(record_id: str, mechanism_key: str, kind: str, key: str = "") -> str:
    """An injective navigation token, including the type of local claim."""
    value = json.dumps([record_id, mechanism_key, kind, key], ensure_ascii=False,
                       separators=(",", ":"))
    return "mechanism-" + value.encode("utf-8").hex()


def _badge(status: str) -> str:
    return f'<span class="mechanism-status">{html.escape(status.replace("_", " "))}</span>'


def mechanism_views(
    record: object, labels: dict[str, str], component_anchors: dict[str, str],
    citations_html: Callable[[list[dict]], str],
) -> str:
    """Render every nested claim and evidence item, including non-edge evidence."""
    if not getattr(record, "reaction_mechanisms", []):
        return ""
    sections = []
    participants = {node["id"]: node for node in record.participants}
    detail_only = set(getattr(record, "detail_only_participant_ids", []))

    def chemical(identifier: str) -> str:
        label = label_html(labels.get(identifier, identifier))
        code = f'<code>{html.escape(identifier)}</code>'
        target = component_anchors[identifier]
        return f'<a href="#{html.escape(target)}">{label}</a> ({code})'

    def evidence(items: list[dict]) -> str:
        return '<ul class="mechanism-evidence">' + citations_html(items) + '</ul>'

    def equation(value: dict) -> str:
        def side(terms: list[dict]) -> str:
            return " + ".join(f'{term["coefficient"]} {chemical(term["participant_id"])}'
                              for term in terms) or "∅"
        return (side(value["inputs"]) + ' <span aria-label="yields">→</span> '
                + side(value["outputs"]))

    for number, mechanism in enumerate(getattr(record, "reaction_mechanisms", []), 1):
        def anchor(kind: str, key: str = "", mechanism_key: str = mechanism["key"]) -> str:
            return mechanism_anchor(record.id, mechanism_key, kind, key)

        steps = {step["key"]: step for step in mechanism["steps"]}
        owner = mechanism["source_reaction_id"]
        heading = f'Mechanistic detail {number}: {plain_label(labels.get(owner, owner))}'
        relation = mechanism["relation_to_source"].replace("_", " ")
        pieces = [
            f'<section class="reaction-mechanism" id="{anchor("section")}" '
            f'aria-labelledby="{anchor("heading")}">',
            f'<h2 id="{anchor("heading")}">{html.escape(heading)}</h2>',
            f'<p><strong>Relation to source:</strong> {html.escape(relation)}. '
            f'<strong>Parent reaction:</strong> {chemical(owner)}.</p>',
            f'<p>{autolink_html(mechanism["description"])}</p>',
            '<p>Steps below are evidence-bearing claims within this record. '
            'They do not assert new external reaction identities.</p>',
            '<h3>Association evidence</h3>', evidence(mechanism["evidence"]),
            '<h3>Source and detailed equations</h3>',
            '<p><strong>Source equation as reported:</strong> '
            + equation(mechanism["source_equation"]) + '</p>',
        ]
        if mechanism["source_equation"]["orientation"] == "reversed":
            pieces.append('<p>The inverse of this source equation is selected for comparison. '
                          'The source reaction’s reported direction is retained.</p>')
        pieces.append('<p><strong>Net of the detailed material steps:</strong> '
                      + equation(mechanism_equation(mechanism)) + '</p>')
        pieces.append('<p>Equation reconciliation does not by itself establish physiological '
                      'flux, chemical identity, or an exhaustive set of elementary steps.</p>')
        if mechanism.get("source_conflicts"):
            pieces.append('<h3>Differences from the source</h3><p>The compared identities remain '
                          'distinct. These dispositions do not declare them equivalent.</p>')
            for index, conflict in enumerate(mechanism["source_conflicts"], 1):
                pieces += [
                    f'<article class="mechanism-conflict" id="{anchor("conflict", str(index))}">',
                    f'<h4>{html.escape(conflict["kind"].replace("_", " "))} difference '
                    f'{_badge(conflict["status"])}</h4>',
                    f'<p>Selected equation side: {html.escape(conflict["side"])}; '
                    f'coefficient: {conflict["coefficient"]}.</p>',
                    '<p><strong>Source identity:</strong> '
                    + chemical(conflict["source_participant_id"]) + '<br>'
                    '<strong>Interpreted identity:</strong> '
                    + chemical(conflict["interpreted_participant_id"]) + '</p>',
                    f'<p>{autolink_html(conflict["rationale"])}</p>',
                    evidence(conflict["evidence"]), '</article>',
                ]
        locations = [edge for edge in mechanism["edges"] if edge["predicate"] == "occurs_in"]
        if not locations:
            pieces.append('<p><strong>Location:</strong> unspecified. No transport or '
                          'co-location is inferred.</p>')
        else:
            pieces.append('<p><strong>Recorded step location:</strong> '
                          + chemical(locations[0]["object"]["node_id"]) + '</p>')

        def step_key(key: str) -> str:
            return json.dumps(["step", key], separators=(",", ":"))

        def endpoint_key(endpoint: dict) -> str:
            return endpoint["node_id"] if "node_id" in endpoint else step_key(endpoint["step_key"])

        def endpoint(endpoint_value: dict, edge: dict, role: str, steps: dict = steps) -> str:
            if "node_id" in endpoint_value:
                content = chemical(endpoint_value["node_id"])
            else:
                key = endpoint_value["step_key"]
                content = (f'<a href="#{anchor("step", key)}">'
                           f'{label_html(steps[key]["label"])}</a> (mechanistic step)')
            for qualifier in edge.get("endpoint_qualifiers", []):
                if qualifier["endpoint"] == role:
                    target = anchor("edge", edge["key"]) + f'-qualifier-{role}'
                    kind_label = html.escape(qualifier["kind"].replace("_", " "))
                    content += (f'<div class="endpoint-qualifier" id="{target}">'
                                f'<p><strong>{kind_label}:</strong> '
                                f'{autolink_html(qualifier["description"])}</p>'
                                + evidence(qualifier["evidence"]) + '</div>')
            return content

        display_nodes = {}
        for claim_number, step in enumerate(mechanism["steps"], 1):
            display_nodes[step_key(step["key"])] = {
                "label": plain_label(step["label"]), "kind": "step",
                "type_label": "Mechanistic step · " + step["assertion_status"],
                "display_identifier": f"record-local mechanistic claim {claim_number}",
                "detail": plain_label(step["label"]) + "; " + step["assertion_status"]
                          + "; " + step["description"],
                "anchor": anchor("step", step["key"]),
            }
        display_edges = []
        for edge in mechanism["edges"]:
            for role in ("subject", "object"):
                if "node_id" not in edge[role]:
                    continue
                identifier = edge[role]["node_id"]
                node = participants[identifier]
                category = node.get("category", "participant")
                kind = ("protein" if category in {"protein", "complex"} else
                        "context" if category == "cellular_component" else "chemical")
                scope = "; detail only" if identifier in detail_only else ""
                display_nodes[identifier] = {
                    "label": plain_label(labels.get(identifier, node["label"])), "kind": kind,
                    "type_label": category.replace("_", " ") + scope,
                    "detail": plain_label(node["label"]) + "; " + identifier + scope,
                    "anchor": component_anchors[identifier],
                }
            display_edges.append({**edge, "subject": endpoint_key(edge["subject"]),
                                  "object": endpoint_key(edge["object"]),
                                  "anchor": anchor("edge", edge["key"])})
        pieces.append(display_graph_html(
            display_nodes, display_edges, title=f"Detailed mechanism graph {number}",
            identity=json.dumps([record.id, mechanism["key"]]), namespace=anchor("graph"),
            description=("Statuses describe each claim’s evidence. "
                         "Local steps are not issued reaction IDs."),
        ))
        pieces.append('<h3>Step claims and hypotheses</h3>')
        for step in mechanism["steps"]:
            pieces += [f'<article class="mechanism-step" id="{anchor("step", step["key"])}">',
                       f'<h4>{label_html(step["label"])} {_badge(step["assertion_status"])}</h4>',
                       f'<p>{autolink_html(step["description"])}</p>', evidence(step["evidence"])]
            for index, hypothesis in enumerate(step.get("hypotheses", []), 1):
                target = anchor("hypothesis", json.dumps([step["key"], index]))
                pieces += [f'<aside class="mechanism-hypothesis" id="{target}">',
                           '<h5>Mechanistic hypothesis ' + _badge(hypothesis["status"]) + '</h5>',
                           f'<p>{autolink_html(hypothesis["description"])}</p>',
                           evidence(hypothesis["evidence"]), '</aside>']
            pieces.append('</article>')
        pieces.append('<h3>Detailed relationships and evidence</h3>'
                      '<div class="table-scroll" role="region" tabindex="0" '
                      'aria-label="Detailed mechanism relationships and evidence"><table>'
                      '<caption>Every detailed relationship and its evidence</caption><thead><tr>'
                      '<th scope="col">Subject</th><th scope="col">Claim</th>'
                      '<th scope="col">Object</th><th scope="col">Evidence</th>'
                      '</tr></thead><tbody>')
        for edge in mechanism["edges"]:
            claim = html.escape(edge["predicate"].replace("_", " "))
            if "coefficient" in edge:
                claim += f' × {edge["coefficient"]}'
            pieces.append(f'<tr id="{anchor("edge", edge["key"])}">'
                          f'<td>{endpoint(edge["subject"], edge, "subject")}</td>'
                          f'<td>{claim} {_badge(edge["assertion_status"])}'
                          f'<p>{autolink_html(edge.get("description", ""))}</p></td>'
                          f'<td>{endpoint(edge["object"], edge, "object")}</td>'
                          f'<td>{evidence(edge["evidence"])}</td></tr>')
        pieces.append('</tbody></table></div></section>')
        sections.append("\n".join(pieces))
    return "\n".join(sections)
