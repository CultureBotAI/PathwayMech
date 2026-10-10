"""Build-time pathway diagrams of declared nodes and asserted edges only.

The SVG and evidence links work without JavaScript or network dependencies.
Coordinates are presentation choices, never evidence for ordering or causation.
"""

from __future__ import annotations

import hashlib
import html
import json
import textwrap
from collections import defaultdict, deque

from pathwaymech.site_display import plain_label

_CONTEXT = {"part_of", "has_part", "occurs_in", "located_in", "has_cofactor"}
_CHEMICAL = {"small_molecule", "lipid", "cofactor"}
_CONTEXT_NODES = {"cellular_component", "biological_process"}
_WIDTH = 236
_GAP = 212
_MARGIN = 74


def _escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def _declared_nodes(record: object, labels: dict[str, str]) -> dict[str, dict]:
    endpoints = {edge[key] for edge in record.mechanistic_edges for key in ("subject", "object")}
    nodes = {}
    for field in ("participants", "reactions", "taxa"):
        for item in getattr(record, field, []):
            identifier = item["id"]
            if field == "taxa" and identifier not in endpoints:
                continue
            category = item.get("category")
            kind = "participant"
            if field == "reactions":
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
    radius = 8 if kind == "reaction" else 0
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


def graph_html(record: object, labels: dict[str, str], component_anchors: dict[str, str]) -> str:
    """Render the complete asserted graph without collapsing labels or inventing edges."""
    start = ('<section id="pathway-network" class="pathway-network" '
             'aria-labelledby="pathway-network-title"><h2 id="pathway-network-title">'
             'Pathway network</h2>')
    edges = record.mechanistic_edges
    if not edges:
        return (start + '<p>No supported network is recorded: this record has no curated '
                'mechanistic edges. Component or cluster membership alone does not establish '
                'a mechanistic connection.</p></section>')
    nodes = _declared_nodes(record, labels)
    levels = _levels(nodes, edges)
    uid = "pathway-graph-" + hashlib.sha256(json.dumps(
        [record.id, nodes, edges], sort_keys=True, default=str,
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
           '<label for="graph-node-picker">Find a node</label>'
           '<select id="graph-node-picker"><option value="">Find a node…</option>']
    for key, node in nodes.items():
        out.append(f'<option value="{_escape(key)}">{_escape(node["label"])} '
                   f'— {_escape(key)}</option>')
    out += ['</select></div><ul class="graph-legend" aria-label="Network legend">']
    legend = {"reaction": "Reaction / activity", "chemical": "Chemical / cofactor",
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
            '<input type="checkbox" class="graph-native-size" id="graph-native-size"/>'
            '<label for="graph-native-size">Show at full size (scroll to explore)</label>',
            '<div class="graph-viewport" id="graph-viewport" tabindex="0" role="region" '
            'aria-label="Scrollable pathway network">',
            f'<svg xmlns="http://www.w3.org/2000/svg" class="pathway-network-svg" '
            f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
            f'role="group" aria-labelledby="{uid}-title {uid}-description">',
            f'<title id="{uid}-title">Pathway network: '
            f'{_escape(plain_label(record.label))}</title>',
            f'<desc id="{uid}-description">{count}. Every arrow links to its evidence table row; '
            'nodes link to their component details. '
            'Isolated declared components are retained.</desc>',
            f'<defs><marker id="{uid}-arrow" markerWidth="10" markerHeight="8" '
            'refX="9" refY="4" orient="auto" markerUnits="userSpaceOnUse">'
            '<path d="M0,0 L10,4 L0,8 Z" fill="#64748b"/></marker></defs>']
    pairs = defaultdict(int)
    for edge in edges:
        pairs[(edge["subject"], edge["object"])] += 1
    seen = defaultdict(int)
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
        else:
            lane = lanes[index]
            # Vertical trunks stay in gutters; long horizontal runs remain
            # above every node. Self loops enter the same node from its left.
            right, left = sx + 74 + fraction * 34, tx - 24 - fraction * 30
            path = f"M{sx},{sy} H{right} V{lane} H{left} V{ty} H{tx}"
            lx, ly = sx + _GAP / 2, sy - 6
        predicate = edge["predicate"]
        kind = "context" if predicate in _CONTEXT else "mechanism"
        detail = f'{subject} — {predicate} → {obj}'
        if edge.get("description"):
            detail += "; " + plain_label(edge["description"])
        evidence = [item["reference_id"] for item in edge.get("evidence", [])]
        if evidence:
            detail += "; Evidence: " + ", ".join(evidence)
        dashed = ' stroke-dasharray="6 4"' if kind == "context" else ""
        out.append(
            f'<a class="graph-edge graph-edge-{kind}" data-subject="{_escape(subject)}" '
            f'data-object="{_escape(obj)}" data-predicate="{_escape(predicate)}" '
            f'href="#mechanism-edge-{index + 1}" tabindex="0" aria-label="{_escape(detail)}">'
            f'<title>{_escape(detail)}</title><path class="graph-edge-line" d="{path}" '
            f'fill="none" stroke="#64748b" stroke-width="1.5"{dashed} '
            f'marker-end="url(#{uid}-arrow)"/>'
            f'<text class="graph-edge-label" x="{lx}" y="{ly}" text-anchor="middle" '
            f'font-size="11" fill="#475569">{_escape(predicate.replace("_", " "))}</text></a>'
        )
    for number, (key, node) in enumerate(nodes.items(), 1):
        x, y = positions[key]
        title_id = f"{uid}-node-{number}"
        anchor = component_anchors.get(key) or title_id
        out.append(f'<a class="graph-node" data-node-id="{_escape(key)}" '
                   f'data-node-label="{_escape(node["label"])}" data-kind="{node["kind"]}" '
                   f'href="#{_escape(anchor)}" tabindex="0" aria-label="{_escape(node["detail"])}">'
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
