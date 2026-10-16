"""Build-time pathway diagrams of declared nodes and asserted edges only.

The SVG and evidence links work without JavaScript or network dependencies.
Coordinates are presentation choices, never evidence for ordering or causation.
"""

from __future__ import annotations

import hashlib
import html
import json
import textwrap
from bisect import insort
from collections import defaultdict, deque

from pathwaymech.site_display import plain_label

_CONTEXT = {"part_of", "has_part", "occurs_in", "located_in", "has_cofactor"}
_CHEMICAL = {"chemical_entity", "small_molecule", "lipid", "polymer", "cofactor"}
_CONTEXT_NODES = {"cellular_component", "biological_process"}
_WIDTH = 236
_GAP = 212
_MARGIN = 74
_LABEL_ABOVE = 14
_LABEL_BELOW = 6
_LABEL_SPACING = _LABEL_ABOVE + _LABEL_BELOW + 4


def _escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def _declared_nodes(record: object, labels: dict[str, str]) -> dict[str, dict]:
    endpoints = {edge[key] for edge in record.mechanistic_edges for key in ("subject", "object")}
    nodes = {}
    for field in ("participants", "reactions", "taxa"):
        for item in getattr(record, field, []):
            identifier = item["id"]
            if (field == "participants"
                    and identifier in getattr(record, "detail_only_participant_ids", [])):
                continue
            if field == "taxa" and identifier not in endpoints:
                continue
            category = item.get("category")
            kind = "participant"
            if category == "pathway":
                kind = "pathway"
            elif field == "reactions":
                kind = "reaction"
            elif field == "taxa":
                kind = "taxon"
            elif category in _CHEMICAL:
                kind = "chemical"
            elif category in {"protein", "complex"}:
                kind = "protein"
            elif category in _CONTEXT_NODES:
                kind = "context"
            label = plain_label(labels.get(identifier) or item.get("label") or identifier)
            details = [f"{label}; {identifier}"]
            details.append("Declared type: " + (category or {
                "participants": "participant (type not recorded)",
                "reactions": "reaction/activity", "taxa": "taxon",
            }[field]))
            if item.get("direction"):
                details.append("Source reaction direction: " + item["direction"])
            node = {
                "label": label, "kind": kind,
                "type_label": (category or {
                    "participants": "participant · type not recorded",
                    "reactions": "reaction / activity", "taxa": "taxon",
                }[field]).replace("_", " "),
                "detail": "; ".join(details),
            }
            if identifier in nodes:
                previous = nodes[identifier]
                node["detail"] = previous["detail"] + "; Also declared: " + node["detail"]
                if previous["kind"] != node["kind"]:
                    node["kind"] = "participant"
                    node["type_label"] = "multiple declared roles"
            nodes[identifier] = node
    if record.id in endpoints:
        label = plain_label(labels.get(record.id) or record.label)
        nodes[record.id] = {
            "label": label, "kind": "pathway", "type_label": "pathway",
            "detail": f"{label}; {record.id}; Declared type: pathway",
        }
    unknown = endpoints - nodes.keys()
    if unknown:
        raise ValueError("Graph endpoints are not declared in this record: "
                         + ", ".join(sorted(unknown)))
    return nodes


def _levels(nodes: dict, edges: list[dict]) -> dict[str, int]:
    """Place related nodes in deterministic breadth-first columns, including cycles."""
    children = defaultdict(list)
    indegree = dict.fromkeys(nodes, 0)
    # Molecular mechanism edges take precedence in layout, without removing
    # contextual edges from the diagram or changing their direction.
    ordered = sorted(edges, key=lambda edge: edge["predicate"] in _CONTEXT)
    for edge in ordered:
        children[edge["subject"]].append(edge["object"])
        indegree[edge["object"]] += 1
    levels = {}
    roots = [node for node in nodes if not indegree[node]]
    for root in roots + list(nodes):
        if root in levels:
            continue
        levels[root] = 0
        queue = deque([root])
        while queue:
            source = queue.popleft()
            for target in children[source]:
                if target not in levels:
                    levels[target] = levels[source] + 1
                    queue.append(target)
    return levels


def _qualifier_detail(qualifier: dict) -> str:
    detail = qualifier["kind"].replace("_", " ") + ": " + qualifier["description"]
    for evidence in qualifier["evidence"]:
        detail += "; Evidence " + evidence["reference_id"] + ": "
        detail += evidence.get("quote", evidence.get("source_assertion", ""))
        if evidence.get("source_locator"):
            detail += " (" + evidence["source_locator"] + ")"
    return detail


def _qualified_endpoints(nodes: dict, edges: list[dict]) -> list[dict]:
    """Add per-edge display instances; biological IDs and input edges stay intact."""
    displayed = []
    for number, edge in enumerate(edges, 1):
        view = dict(edge)
        for qualifier in edge.get("endpoint_qualifiers", []):
            role = qualifier["endpoint"]
            identifier = edge[role]
            base = nodes[identifier]
            key = f"qualified-endpoint-{number}-{role}"
            while key in nodes:
                key += "-display"
            kind = qualifier["kind"].replace("_", " ")
            label = base["label"] + " [" + kind + ": " + textwrap.shorten(
                qualifier["description"], width=100, placeholder="…",
            ) + "]"
            nodes[key] = {
                **base, "label": label, "type_label": kind, "identifier": identifier,
                "detail": base["detail"] + "; " + _qualifier_detail(qualifier),
                "anchor": edge.get("anchor", f"mechanism-edge-{number}") + f"-qualifier-{role}",
            }
            view[role] = key
            view["_native_" + role] = identifier
        displayed.append(view)
    return displayed


def _shape(kind: str, x: float, y: float, width: float, height: float) -> str:
    attrs = 'class="graph-node-shape" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"'
    if kind == "chemical":
        return (f'<rect {attrs} x="{x}" y="{y}" width="{width}" height="{height}" '
                f'rx="{min(height / 2, 36)}"/>')
    if kind == "protein":
        inset = min(15, width / 5)
        points = ((x + inset, y), (x + width - inset, y), (x + width, y + height / 2),
                  (x + width - inset, y + height), (x + inset, y + height), (x, y + height / 2))
        return f'<polygon {attrs} points="' + " ".join(f"{a},{b}" for a, b in points) + '"/>'
    if kind in {"context", "taxon", "pathway"}:
        return (f'<rect {attrs} x="{x}" y="{y}" width="{width}" height="{height}" '
                'rx="3" stroke-dasharray="5 3"/>')
    radius = 8 if kind in {"reaction", "step"} else 0
    return (f'<rect {attrs} x="{x}" y="{y}" width="{width}" height="{height}" '
            f'rx="{radius}"/>')


def _route_lanes(edges: list[dict], levels: dict[str, int]) -> dict[int, int]:
    """Reuse disjoint horizontal spans, with bounded space for a dense network.

    Once eight lanes are occupied, reuse the least-overlapping lane. Crossings
    are acceptable presentation limits: each original edge retains its own path,
    title and evidence link. Dense networks must not acquire a huge empty header.
    """
    occupied: list[list[tuple[int, int]]] = []
    lanes = {}
    for index, edge in enumerate(edges):
        source, target = levels[edge["subject"]], levels[edge["object"]]
        if target == source + 1:
            continue
        low, high = min(source, target), max(source, target)
        overlaps = [sum(not (high < start or low > stop) for start, stop in spans)
                    for spans in occupied]
        if 0 in overlaps:
            lane = overlaps.index(0)
        elif len(occupied) < 8:
            lane = len(occupied)
            occupied.append([])
        else:
            lane = min(range(len(occupied)), key=lambda i: (overlaps[i], len(occupied[i]), i))
        occupied[lane].append((low, high))
        lanes[index] = 28 + lane * 18
    return lanes


def _edge_routes(edges: list[dict], positions: dict, heights: dict,
                 lanes: dict[int, int]) -> list[tuple[str, float, float, float, float]]:
    """Keep arrow geometry separate from movable labels and their attachment points."""
    pairs = defaultdict(int)
    for edge in edges:
        pairs[(edge["subject"], edge["object"])] += 1
    seen = defaultdict(int)
    routes = []
    for index, edge in enumerate(edges):
        subject, obj = edge["subject"], edge["object"]
        x1, y1 = positions[subject]
        x2, y2 = positions[obj]
        pair = (subject, obj)
        number = seen[pair]
        seen[pair] += 1
        # Separate parallel endpoints inside each box; no fixed offset can push
        # a large set of parallel edges outside the recorded node bounds.
        fraction = (number + 1) / (pairs[pair] + 1)
        sy = y1 + 22 + fraction * (heights[subject] - 38)
        ty = y2 + 22 + fraction * (heights[obj] - 38)
        sx, tx = x1 + _WIDTH, x2
        if index not in lanes:
            bend = (sx + tx) / 2
            path = f"M{sx},{sy} C{bend},{sy} {bend},{ty} {tx},{ty}"
            lx, ly = bend, (sy + ty) / 2 - 6
            # Attach callouts near the source, outside every predicate text box.
            # These are points on the same cubic Bezier, evaluated at t = .01.
            t = .01
            ax = sx + 3 * t * (1 - t) * (bend - sx) + t ** 3 * (tx - sx)
            ay = sy + (3 * t ** 2 - 2 * t ** 3) * (ty - sy)
        else:
            lane = lanes[index]
            # Vertical trunks stay in gutters; long horizontal runs remain
            # above every node. Self loops enter the same node from its left.
            right, left = sx + 74 + fraction * 34, tx - 24 - fraction * 30
            path = f"M{sx},{sy} H{right} V{lane} H{left} V{ty} H{tx}"
            lx, ly = sx + _GAP / 2, sy - 6
            ax, ay = sx + 3, sy
        routes.append((path, lx, ly, ax, ay))
    return routes


def _edge_label_positions(
    routes: list[tuple], line_counts: list[int] | None = None,
) -> list[tuple[float, float]]:
    """Reserve nonoverlapping text boxes in each gutter, nearest the original label.

    All supported predicate labels fit inside the 212 px gutter. Reserve its full
    width and 20 px vertically, including the text halo, plus 4 px between labels.
    Search free intervals in stable edge order; ties prefer the upper position.
    Dense gutters can grow below the nodes, without increasing the top header.
    """
    occupied = defaultdict(list)
    positions = []
    for index, (_, x, preferred, _, _) in enumerate(routes):
        below = _LABEL_BELOW + _LABEL_SPACING * ((line_counts[index] if line_counts else 1) - 1)
        lower = _LABEL_ABOVE + 12
        candidates = []
        for start, end in occupied[x]:
            upper = start - 4 - below
            if lower <= upper:
                candidates.append(max(lower, min(preferred, upper)))
            lower = end + 4 + _LABEL_ABOVE
        candidates.append(max(lower, preferred))
        y = min(candidates, key=lambda candidate: (abs(candidate - preferred), candidate))
        insort(occupied[x], (y - _LABEL_ABOVE, y + below))
        positions.append((x, y))
    return positions


def graph_html(record: object, labels: dict[str, str], component_anchors: dict[str, str]) -> str:
    """Render source assertions, excluding only explicitly detail-only declarations."""
    if not record.mechanistic_edges and not getattr(record, "reaction_mechanisms", []):
        return display_graph_html({}, [], title="Pathway network", identity="")
    alternatives = {m["source_reaction_id"] for m in getattr(record, "reaction_mechanisms", [])
                    if m["relation_to_source"] == "alternative_interpretation"}
    edges = [{**edge, **({"source_reported": True} if
              edge["subject"] in alternatives or edge["object"] in alternatives else {})}
             for edge in record.mechanistic_edges]
    title = ("Source pathway representation" if getattr(record, "reaction_mechanisms", [])
             else "Pathway network")
    description = ("Source-reported assertions are preserved. Alternative interpretations "
                   "and their evidence appear below." if alternatives else "")
    return display_graph_html(
        _declared_nodes(record, labels), edges, title=title, identity=record.id,
        component_anchors=component_anchors, description=description,
        render_isolated=bool(getattr(record, "reaction_mechanisms", [])),
    )


def display_graph_html(
    declared_nodes: dict[str, dict], declared_edges: list[dict], *, title: str,
    identity: str, namespace: str = "", component_anchors: dict[str, str] | None = None,
    description: str = "", render_isolated: bool = False,
) -> str:
    """Render an explicit display graph; local claim keys are never biological IDs.

    The caller supplies already validated endpoints and explicit evidence anchors.
    No input node, edge or record is mutated. Namespace is a safe navigation token.
    """
    def anchor(suffix: str) -> str:
        return f"{namespace}-{suffix}" if namespace else suffix

    component_anchors = component_anchors or {}
    section_id, title_id = anchor("pathway-network"), anchor("pathway-network-title")
    start = (f'<section id="{_escape(section_id)}" class="pathway-network" '
             f'aria-labelledby="{_escape(title_id)}"><h2 id="{_escape(title_id)}">'
             f'{_escape(title)}</h2>')
    if description:
        start += f'<p class="graph-scope">{_escape(description)}</p>'
    if not declared_edges and not (render_isolated and declared_nodes):
        return (start + '<p>No supported network is recorded: this record has no curated '
                'mechanistic edges. Component or cluster membership alone does not establish '
                'a mechanistic connection.</p></section>')
    nodes = {key: dict(value) for key, value in declared_nodes.items()}
    edges = _qualified_endpoints(nodes, declared_edges)
    if any(edge[role] not in nodes for edge in edges for role in ("subject", "object")):
        raise ValueError("Display graph endpoints must resolve to explicit display nodes")
    levels = _levels(nodes, edges)
    uid = "pathway-graph-" + hashlib.sha256(json.dumps(
        [identity, nodes, edges], sort_keys=True, default=str,
    ).encode()).hexdigest()[:16]
    wrapped = {key: textwrap.wrap(node["label"], 28) or [key] for key, node in nodes.items()}
    heights = {key: max(78, 43 + len(lines) * 17) for key, lines in wrapped.items()}
    # Forward edges fit inside a column gutter; feedback/long edges use compact
    # reserved top lanes. Their labels sit beside the source, not above the graph.
    lanes = _route_lanes(edges, levels)
    top = max(lanes.values(), default=0) + 76
    column_bottom = defaultdict(lambda: top)
    positions = {}
    for key in nodes:
        column = levels[key]
        positions[key] = (_MARGIN + column * (_WIDTH + _GAP), column_bottom[column])
        column_bottom[column] += heights[key] + 66
    width = int(max(x for x, _ in positions.values()) + _WIDTH + _GAP)
    height = int(max(y + heights[key] for key, (_, y) in positions.items()) + _MARGIN)
    routes = _edge_routes(edges, positions, heights, lanes)
    edge_labels = []
    for edge in edges:
        label = edge["predicate"].replace("_", " ")
        if "coefficient" in edge:
            label += f" × {edge['coefficient']}"
        lines = (textwrap.wrap(label, 20) if "coefficient" in edge else [label])
        if edge.get("assertion_status"):
            lines.append(edge["assertion_status"])
        if edge.get("source_reported"):
            lines.append("source-reported")
        edge_labels.append(lines)
    label_positions = _edge_label_positions(routes, [len(lines) for lines in edge_labels])
    if label_positions:
        height = max(height, int(max(
            y + _LABEL_SPACING * (len(lines) - 1)
            for (_, y), lines in zip(label_positions, edge_labels, strict=True)
        ) + _LABEL_BELOW + _MARGIN))
    count = (f'{len(nodes)} node{"" if len(nodes) == 1 else "s"} · '
             f'{len(edges)} asserted directed edge{"" if len(edges) == 1 else "s"}')
    out = [start, f'<p class="graph-status" role="status" aria-live="polite">{count}</p>',
           '<p class="graph-help">Arrows show recorded subject → object relationships, '
           'not necessarily metabolic flow. Select a node for details or an arrow for evidence. '
           'Scroll, zoom or find a node to explore.</p>',
           '<div class="graph-tools" hidden><button type="button" '
           'data-graph-action="zoom-in" aria-label="Zoom in on pathway network">Zoom in</button>'
           '<button type="button" data-graph-action="zoom-out" '
           'aria-label="Zoom out of pathway network">Zoom out</button>'
           '<button type="button" data-graph-action="fit">Fit width</button>'
           f'<label for="{_escape(anchor("graph-node-picker"))}">Find a node</label>'
           f'<select class="graph-node-picker" id="{_escape(anchor("graph-node-picker"))}">'
           '<option value="">Find a node…</option>']
    for key, node in nodes.items():
        identifier = node.get("display_identifier", node.get("identifier", key))
        out.append(f'<option value="{_escape(key)}">{_escape(node["label"])} '
                   f'— {_escape(identifier)}</option>')
    out += ['</select></div><ul class="graph-legend" aria-label="Network legend">']
    legend = {"reaction": "Reaction / activity", "step": "Record-local mechanistic claim",
              "chemical": "Chemical / cofactor",
              "protein": "Protein / complex", "participant": "Other participant",
              "context": "Cell / process context", "taxon": "Taxon", "pathway": "Pathway"}
    present = {node["kind"] for node in nodes.values()}
    for kind, description in legend.items():
        if kind in present:
            out.append(f'<li><svg width="30" height="18" '
                       f'viewBox="0 0 30 18" aria-hidden="true">'
                       f'<g class="graph-node" data-kind="{kind}">'
                       f'{_shape(kind, 1, 1, 28, 16)}</g>'
                       f'</svg> {_escape(description)}</li>')
    out += ['<li>Solid arrow: mechanistic relation</li><li>Dashed arrow: membership, location '
            'or cofactor relation</li></ul>',
            '<input type="checkbox" class="graph-native-size" '
            f'id="{_escape(anchor("graph-native-size"))}"/>'
            f'<label for="{_escape(anchor("graph-native-size"))}">'
            'Show at full size (scroll to explore)</label>',
            f'<div class="graph-viewport" id="{_escape(anchor("graph-viewport"))}" '
            'tabindex="0" role="region" '
            'aria-label="Scrollable pathway network">',
            f'<svg xmlns="http://www.w3.org/2000/svg" class="pathway-network-svg" '
            f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'role="group" aria-labelledby="{uid}-title {uid}-description">',
            f'<title id="{uid}-title">{_escape(title)}</title>',
            f'<desc id="{uid}-description">{count}. Every arrow links to its evidence table row; '
            'nodes link to their component details. '
            'Isolated declared components are retained.</desc>',
            f'<defs><marker id="{uid}-arrow" markerWidth="10" markerHeight="8" '
            'refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse">'
            '<path d="M0,0 L10,4 L0,8 Z" fill="#64748b"/></marker></defs>']
    for index, edge in enumerate(edges):
        subject, obj = edge["subject"], edge["object"]
        path, _, original_y, ax, ay = routes[index]
        lx, ly = label_positions[index]
        leader = ""
        if abs(ly - original_y) >= _LABEL_ABOVE + _LABEL_BELOW:
            # Conservatively allow 10 px per lowercase glyph at 11 px font size,
            # 4 px per space and 8 px for the text halo. A side rail keeps long
            # callouts away from all labels, including the stationary collision.
            text_width = 8 + max(sum(4 if char == " " else 10 for char in line)
                                 for line in edge_labels[index])
            left = lx - text_width / 2
            rail = lx - _GAP / 2 + 2
            leader = (f'<path class="graph-label-leader" '
                      f'd="M{left},{ly - 4} H{rail} V{ay} H{ax}" '
                      'fill="none" stroke="#64748b" stroke-width="1" '
                      'stroke-dasharray="2 3" aria-hidden="true"/>')
        predicate = edge["predicate"]
        predicate_label = " · ".join(edge_labels[index])
        kind = "context" if predicate in _CONTEXT else "mechanism"
        native_subject = edge.get("_native_subject", subject)
        native_object = edge.get("_native_object", obj)
        detail = f'{nodes[subject]["label"]} — {predicate_label} → {nodes[obj]["label"]}'
        for qualifier in edge.get("endpoint_qualifiers", []):
            detail += "; " + qualifier["endpoint"] + " " + _qualifier_detail(qualifier)
        if edge.get("description"):
            detail += "; " + plain_label(edge["description"])
        evidence = [item["reference_id"] for item in edge.get("evidence", [])]
        if evidence:
            detail += "; Evidence: " + ", ".join(evidence)
        dashed = ' stroke-dasharray="6 4"' if kind == "context" else ""
        native_attrs = (
            f' data-subject-id="{_escape(native_subject)}" '
            f'data-object-id="{_escape(native_object)}"'
            if edge.get("endpoint_qualifiers") else ""
        )
        label_svg = "".join(
            f'<text class="graph-edge-label" x="{lx}" y="{ly + line * _LABEL_SPACING}" '
            f'text-anchor="middle" font-size="11" fill="#475569">{_escape(text)}</text>'
            for line, text in enumerate(edge_labels[index])
        )
        out.append(
            f'<a class="graph-edge graph-edge-{kind}" data-subject="{_escape(subject)}" '
            f'data-object="{_escape(obj)}" data-predicate="{_escape(predicate)}"{native_attrs} '
            f'href="#{_escape(edge.get("anchor", f"mechanism-edge-{index + 1}"))}" '
            f'tabindex="0" aria-label="{_escape(detail)}">'
            f'<title>{_escape(detail)}</title><path class="graph-edge-line" d="{path}" '
            f'fill="none" stroke="#64748b" stroke-width="1.5"{dashed} '
            f'marker-end="url(#{uid}-arrow)"/>{leader}{label_svg}</a>'
        )
    for number, (key, node) in enumerate(nodes.items(), 1):
        x, y = positions[key]
        title_id = f"{uid}-node-{number}"
        target = node.get("anchor") or component_anchors.get(key) or title_id
        native_attrs = (
            f' data-base-node-id="{_escape(node["identifier"])}" data-qualified="true"'
            if "identifier" in node else ""
        )
        out.append(f'<a class="graph-node" data-node-id="{_escape(key)}" '
                   f'data-node-label="{_escape(node["label"])}" '
                   f'data-kind="{node["kind"]}"{native_attrs} '
                   f'href="#{_escape(target)}" tabindex="0" aria-label="{_escape(node["detail"])}">'
                   f'<title id="{title_id}">{_escape(node["detail"])}</title>'
                   + _shape(node["kind"], x, y, _WIDTH, heights[key]))
        out.append(f'<text class="graph-node-type" x="{x + _WIDTH / 2}" y="{y + 19}" '
                   'text-anchor="middle" font-size="10" fill="#475569">'
                   f'{_escape(node["type_label"])}</text>')
        for line, text in enumerate(wrapped[key]):
            out.append(f'<text class="graph-node-label" x="{x + _WIDTH / 2}" '
                       f'y="{y + 41 + line * 17}" text-anchor="middle" '
                       f'font-size="13" fill="#172033">{_escape(text)}</text>')
        out.append("</a>")
    out.append("</svg></div></section>")
    return "\n".join(out)
