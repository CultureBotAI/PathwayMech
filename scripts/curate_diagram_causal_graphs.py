#!/usr/bin/env python3
"""Replay the bounded 2026-10 causal review of GPML, Reactome and MIBiG records.

Requires the independently downloaded conf/identifier_sources.json source cache,
SGD_features.tab, and an OAK ChEBI SQLite database. This is a curated migration,
not a general-purpose importer: reviewed scope and source corrections are explicit.
"""

# Long scientific assertions and explicit source equations are kept intact.
# ruff: noqa: E501
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import subprocess
from functools import cache
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml

from pathwaymech import biopax as bp
from pathwaymech.curation import CAUSAL_REVIEW_BASELINE, guard_baseline, publish_curation, require
from pathwaymech.wikipathways import DATABASE_PREFIXES

WP = [
    "WP171",
    "WP178",
    "WP266",
    "WP287",
    "WP296",
    "WP392",
    "WP478",
    "WP5019",
    "WP5060",
    "WP556",
    "WP5587",
    "WP71",
]
REACTOME = ["R-MTU-868688", "R-MTU-879299", "R-MTU-879325"]
CHEMICAL_CORRECTIONS = {
    # Native source names, reaction context and ChEBI identity checked together;
    # these are deliberate corrections, not equivalent-xref assertions.
    ("WP478", "c69"): "CHEBI:4170",
    ("WP5587", "c3273"): "CHEBI:18005",
    ("WP171", "f6f"): "CHEBI:30616",
    ("WP171", "dba6f"): "CHEBI:30616",
    ("WP171", "d8269"): "CHEBI:30616",
    ("WP5060", "eb5c4"): "CHEBI:16488",
    ("WP5060", "a68a3"): "CHEBI:15570",
    ("WP5060", "a6683"): "CHEBI:16932",
    ("WP5060", "b5141"): "CHEBI:61543",
    ("WP5060", "b0b99"): "CHEBI:15784",
    ("WP5060", "a0d71"): "CHEBI:47965",
    ("WP5060", "ed65e"): "CHEBI:61564",
    ("WP5060", "de8b0"): "WikiPathways:WP5060/de8b0",
    ("WP5060", "e9564"): "WikiPathways:WP5060/e9564",
    ("WP5060", "c345c"): "WikiPathways:WP5060/e9564",
    ("WP5060", "a45c7"): "WikiPathways:WP5060/a45c7",
}
EXACT_NAMED = {
    "ATP": "CHEBI:30616",
    "ADP": "CHEBI:456216",
    "Coenzyme A": "CHEBI:15346",
    "COENZYME A": "CHEBI:15346",
    "H⁺": "CHEBI:15378",
    "CO₂": "CHEBI:16526",
    "pyrophosphate": "CHEBI:33019",
    "phosphate": "CHEBI:43474",
    "maltodextrin": "CHEBI:25140",
    "NADP": "CHEBI:58349",
    "ubiquinone": "CHEBI:52971",
    "ubiqionol": "CHEBI:52970",
}
NOTES = {
    "WP171": "Restored nicotinamide, ATP/ADP/PPi and peptide substrates. Corrected ATP xrefs (source CAS1927-31-7 identifies dATP). Histone acetyllysine is represented as a protein residue, not free acetyllysine. Unmapped external pathway connectors are excluded.",
    "WP178": "Restored catalysts and cosubstrates. Excluded THI3 catalytic assignment: individual enzyme assays in DOI10.1128/AEM.01675-12 found no activity. No subcellular location inferred from isozyme identity alone.",
    "WP266": "Restored acyl-CoA/CoA, water/phosphate, PC/lysoPC and enzymes; LRO1 and DGA1 remain distinct routes to TAG.",
    "WP287": "Restored COQ catalysts, SAM/SAH, oxygen, reducing equivalents and carbon dioxide; retained the source generic electron acceptor classes. Source complex membrane attachment is tentative, so no certain compartment edge is inferred.",
    "WP296": "Restored supported anchor cofactors and enzyme components; multisubunit groups enable the reaction instead of each subunit being independently catalytic. Q6 replaces the native Q9 cross-reference; source ATP and CoA CAS crossrefs incorrectly identify dATP and F420 and are corrected by reaction context and named chemical identity. Anaplerotic pyruvate branch is outside the retained TCA-cycle scope.",
    "WP392": "Restored GSH conjugate and redox cosubstrates. Removed the ungrounded glutaredoxin diagram branch whose controller and redox partner are not identified. GPX assignments remain diagram-level evidence, not an exclusive physiological electron-donor claim.",
    "WP478": "Retained the explicitly scoped GPH1/PGM branch, including prior glucose-6-phosphate correction; restored shortened glucan product and phosphate. Ambiguous GDB1 debranching and SGA1 peripheral branches are not reinterpreted as complete reactions.",
    "WP5019": "Restored explicit enzymes and directed cofactors. Corrinoid methyl carrier is not a free methyl radical: the two native carrier-transfer/assembly reactions are represented as an aggregate, without a free methyl-radical intermediate. Undirected connectors and energy-complex drawings are not reaction arrows.",
    "WP5060": "Restored missing cosubstrates where exact identity is available; reversed-arrow racemases and phosphoglucosamine mutase marked reversible. MurJ is transport support rather than an enzyme that polymerizes peptidoglycan. Cytoplasmic source is explicitly incomplete for membrane/periplasm steps; no omitted DNA/RNA nodes inferred.",
    "WP556": "Restored GAD1, UGA1, UGA2, proton/CO2, 2-oxoglutarate/glutamate, water and NAD(P) redox pair from native anchors.",
    "WP5587": "Grounded missing G6P, prephenate, phenylpyruvate and phenylacetaldehyde; restored the connected Ehrlich route. Merged duplicate DAHP condensation lines and preserved reversible transamination. Collapsed glycolysis/shikimate branches have component enables relationships, not single-enzyme catalysis claims.",
    "WP71": "Retained the explicitly scoped SPO14 phospholipase D branch. Excluded ISC1 phosphatidylcholine claim contradicted by the source comment; PLC1 branch is outside this record scope.",
}


def local(e):
    return e.tag.rsplit("}", 1)[-1]


def children(e, t):
    return [c for c in e if local(c) == t]


def first(e, t):
    return next(iter(children(e, t)), None)


def points(e):
    return [p for p in e.iter() if local(p) == "Point" and p.get("GraphRef")]


def arrow(p):
    return (p.get("ArrowHead") or "line").lower()


def directed(p):
    return arrow(p) in {"arrow", "mim-conversion"}


def assertion(ref, text, locator):
    require(len(text) <= 400, text)
    return {"reference_id": ref, "source_assertion": text, "source_locator": locator}


def edge(s, p, o, ref, text, locator, description=None):
    d = {"subject": s, "predicate": p, "object": o, "evidence": [assertion(ref, text, locator)]}
    if description:
        d["description"] = description
    return d


def source_reference(key, ref, manifest, cache):
    m = manifest[key]
    require(
        hashlib.sha256((cache / m["path"]).read_bytes()).hexdigest() == m["sha256"],
        'Migration precondition failed: hashlib.sha256((cache / m["path"]).read_bytes()).hexdigest() == m["sha256"]',
    )
    return {
        "id": ref,
        "title": f"{key} native structured pathway source",
        "url": m["url"],
        "source_version": m["version"],
        "source_sha256": m["sha256"],
    }


def add_reference(r, ref):
    r["references"] = [x for x in r["references"] if x["id"] != ref["id"]] + [ref]


def finish(r, participants, reactions, edges):
    uniq = {}
    for e in edges:
        key = (e["subject"], e["predicate"], e["object"])
        if key in uniq:
            for ev in e["evidence"]:
                if ev not in uniq[key]["evidence"]:
                    uniq[key]["evidence"].append(ev)
        else:
            uniq[key] = e
    r["mechanistic_edges"] = [
        {"id": f"causal-review-{i}", **e} for i, e in enumerate(uniq.values(), 1)
    ]
    used = {e[k] for e in uniq.values() for k in ["subject", "object"]}
    r["participants"] = list({n["id"]: n for n in participants if n["id"] in used}.values())
    r["reactions"] = reactions
    if "source_mappings" in r:
        r["source_mappings"] = [m for m in r["source_mappings"] if m["object_id"] in used]
        if not r["source_mappings"]:
            del r["source_mappings"]


@cache
def chemical_category(conn, identifier):
    """Use ChEBI is_a ancestry, never a name substring, for lipid identity."""
    row = conn.execute(
        "WITH RECURSIVE ancestors(term) AS (SELECT ? UNION "
        "SELECT s.object FROM ancestors CROSS JOIN statements s ON s.subject=ancestors.term "
        "WHERE s.predicate='rdfs:subClassOf' AND s.object LIKE 'CHEBI:%') "
        "SELECT 1 FROM ancestors WHERE term='CHEBI:18059' LIMIT 1",
        (identifier,),
    ).fetchone()
    return "lipid" if row else "small_molecule"


def gpml(r, cache, manifest, conn, sgd, xrefs):
    acc = r["id"].split(":")[1]
    x = ET.parse(cache / (acc + ".gpml")).getroot()
    ref = r["id"]
    prior = {n["id"]: n for n in r["participants"]}
    prior_map = {m["subject_id"]: m["object_id"] for m in r.get("source_mappings", [])}
    nodes = {}
    unresolved = []
    corrections = []
    for n in children(x, "DataNode"):
        gid = n.get("GraphId")
        label = (n.get("TextLabel") or "").strip()
        xx = first(n, "Xref")
        a = xx.attrib if xx is not None else {}
        prefix = DATABASE_PREFIXES.get(a.get("Database", "").lower())
        raw = a.get("ID", "")
        ident = f"{prefix}:{raw.removeprefix(str(prefix) + ':')}" if prefix and raw else None
        native = ident
        ident = prior_map.get(ident, ident)
        if prefix == "Ensembl" and raw in sgd:
            ident = sgd[raw]
        if prefix not in {"CHEBI", "SGD", "UniProtKB", "Ensembl"}:
            xp = {
                "HMDB": "hmdb",
                "CAS": "cas",
                "KEGG": "kegg.compound",
                "PubChem": "pubchem.compound",
            }.get(prefix)
            keys = [xp + ":" + raw] if xp else []
            if prefix == "HMDB":
                keys.append("hmdb:HMDB" + raw.removeprefix("HMDB").zfill(7))
            cand = {q for key in keys for q in xrefs.get(key, [])}
            ident = next(iter(cand)) if len(cand) == 1 else None
        if label in EXACT_NAMED:
            ident = EXACT_NAMED[label]
        if (acc, gid) in CHEMICAL_CORRECTIONS:
            ident = CHEMICAL_CORRECTIONS[(acc, gid)]
        if acc == "WP178" and label == "L-glutamate":
            ident = "CHEBI:29985"
        if acc == "WP171" and gid == "a42ba":
            ident = "CHEBI:61930"
        if acc == "WP171" and gid == "fbed5":
            ident = "CHEBI:29967"  # L-lysine residue, not free lysine
        if not ident or ident.startswith("Ensembl:"):
            unresolved.append({"graph_id": gid, "label": label, "xref": native})
            continue
        if ident.startswith("CHEBI:"):
            row = conn.execute(
                "select value from statements where subject=? and predicate='rdfs:label'", (ident,)
            ).fetchone()
            if not row:
                raise ValueError(ident)
            label = row[0]
            category = chemical_category(conn, ident)
        else:
            category = "small_molecule" if ident.startswith("WikiPathways:") else "protein"
        nodes[gid] = {
            "id": ident,
            "label": prior.get(ident, {}).get("label", label),
            "category": category,
        }
        if native != ident:
            corrections.append({"graph_id": gid, "source_xref": native, "id": ident})
    groups = {
        g.get("GraphId"): [
            n.get("GraphId")
            for n in children(x, "DataNode")
            if n.get("GroupRef") == g.get("GroupId")
        ]
        for g in children(x, "Group")
    }
    ints = {i.get("GraphId"): i for i in children(x, "Interaction")}
    anchors = {
        a.get("GraphId"): gid for gid, i in ints.items() for a in i.iter() if local(a) == "Anchor"
    }
    selected = {n["id"].split("/")[-1] for n in r["reactions"]}
    if acc == "WP5587":
        selected |= {"id42570815", "id9510c196"}
        selected.discard("id88645eca")
    if acc == "WP392":
        selected.discard("id8fe92484")
    if acc == "WP5019":
        selected.discard("id8e976caf")
    oldr = {n["id"]: n for n in r["reactions"]}
    reactions = []
    edges = []

    def resolved(refid):
        return [nodes[g] for g in groups.get(refid, [refid]) if g in nodes]

    def emit(n, p, rid, gid, nodegid, desc=None):
        s, o = (rid, n["id"]) if p == "produces" else (n["id"], rid)
        txt = (
            f"GPML {gid} connects normalized {n['id']} as "
            + {
                "produces": "an output",
                "consumes": "an input",
                "catalyzes": "a catalyst",
                "enables": "an enabling enzyme component",
            }[p]
            + f" of interaction {rid.split('/')[-1]}."
        )
        native_nodes = [
            g for g in groups.get(nodegid, [nodegid]) if g in nodes and nodes[g]["id"] == n["id"]
        ]
        loc = f"/Pathway/Interaction[@GraphId='{gid}']/Graphics; " + "; ".join(
            f"/Pathway/DataNode[@GraphId='{g}']" for g in native_nodes
        )
        edges.append(edge(s, p, o, ref, txt, loc, desc))

    for gid in sorted(selected):
        i = ints[gid]
        ps = points(i)
        rid = ref + "/" + gid
        if len(ps) < 2:
            continue
        nsets = [resolved(p.get("GraphRef")) for p in ps]
        if not all(nsets):
            # A record may retain a source reaction with one ungrounded endpoint;
            # do not continue emitting a chemically one-sided step.
            unresolved.append({"interaction": gid, "reason": "unresolved main endpoint"})
            continue
        rev = all(directed(p) for p in ps)
        targets = [directed(p) for p in ps]
        if rev:
            targets = [False] + [True] * (len(ps) - 1)
        if acc == "WP5587" and gid == "id864096aa":
            targets = [True, False]
        rn = dict(oldr.get(rid, {"id": rid, "label": f"{nsets[0][0]['label']} conversion"}))
        rn["direction"] = "reversible" if rev else "left_to_right"
        rn["category"] = "molecular_activity"
        reactions.append(rn)
        for p, ns, target in zip(ps, nsets, targets, strict=True):
            for n in ns:
                emit(
                    n,
                    "produces" if target else "consumes",
                    rid,
                    gid,
                    p.get("GraphRef"),
                    "The source has arrowheads on both endpoints; the displayed orientation is one direction of a reversible conversion."
                    if rev
                    else None,
                )
    kept = {n["id"] for n in reactions}
    for gid, i in ints.items():
        ps = points(i)
        ap = [p for p in ps if p.get("GraphRef") in anchors]
        if len(ap) != 1:
            continue
        a = ap[0]
        main = anchors[a.get("GraphRef")]
        if acc == "WP5587" and main == "id88645eca":
            main = "idc5e5e165"
        rid = ref + "/" + main
        if rid not in kept:
            continue
        for p in ps:
            if p is a:
                continue
            pred = (
                "catalyzes"
                if "catalysis" in arrow(a)
                else "consumes"
                if directed(a)
                else "produces"
                if directed(p)
                else None
            )
            if pred is None:
                continue
            for n in resolved(p.get("GraphRef")):
                if acc == "WP178" and n["id"] == "SGD:S000002238":
                    continue
                if pred == "catalyzes" and n["category"] != "protein":
                    continue
                if pred in {"consumes", "produces"} and n["category"] == "protein":
                    continue
                if pred == "catalyzes" and (
                    (acc == "WP296" and main in {"id238f9689", "ida3b8a465", "idaf5b761e", "b7797"})
                    or (acc == "WP5019" and p.get("GraphRef") in groups)
                    or (
                        acc == "WP5587"
                        and main in {"idf0d0e924", "idf107e51d", "id32159333", "idbd32b592"}
                    )
                    or (acc == "WP5060" and n["id"] == "UniProtKB:P0AF16")
                ):
                    pred = "enables"
                emit(n, pred, rid, gid, p.get("GraphRef"))
    # Source lines without arrowheads have no direction by themselves. In this
    # redox module the source comment explicitly describes reductase/peroxidase roles.
    if acc == "WP392":
        for gid, nodeids, main in [
            ("id50af4865", ["fe0", "efa82"], "id3206f739"),
            ("id3cdb2e84", ["d804d"], "idb13bbbe"),
        ]:
            for ng in nodeids:
                emit(
                    nodes[ng],
                    "consumes",
                    ref + "/" + main,
                    gid,
                    ng,
                    "Direction resolved from the source pathway redox description, not an unheaded line alone.",
                )
    if acc == "WP5019":
        rid = ref + "/ideb932d04"
        next(q for q in reactions if q["id"] == rid)["label"] = (
            "Corrinoid-dependent methyl transfer and acetyl-CoA assembly (aggregate)"
        )
        for ng, pred in [("aed66", "consumes"), ("baa9c", "consumes"), ("f4118", "produces")]:
            emit(
                nodes[ng],
                pred,
                rid,
                "id8e976caf" if ng != "baa9c" else "id2b845640",
                ng,
                "Aggregate of native corrinoid-bound methyl transfer and acetyl-CoA assembly; free methyl radical is not an intermediate.",
            )
        for ng in ["b31af", "c0d75", "f37ef", "d0c8a"]:
            emit(
                nodes[ng],
                "enables",
                rid,
                "id8e976caf" if ng != "c0d75" else "ideb932d04",
                ng,
                "Component of the combined corrinoid methyl transfer/acetyl-CoA assembly, not an independently catalytic complex subunit.",
            )
        edges = [
            e
            for e in edges
            if not (e["subject"] == nodes["c0d75"]["id"] and e["predicate"] == "catalyzes")
        ]
    if acc == "WP5587":
        emit(
            nodes["d8ea8"],
            "consumes",
            ref + "/idc5e5e165",
            "id88645eca",
            "d8ea8",
            "The two native DAHP input lines represent one condensation reaction.",
        )
    finish(r, list(nodes.values()), reactions, edges)
    add_reference(r, source_reference(acc, ref, manifest, cache))
    if acc == "WP178":
        add_reference(
            r,
            {
                "id": "DOI:10.1128/AEM.01675-12",
                "title": "Substrate Specificity of Thiamine Pyrophosphate-Dependent 2-Oxo-Acid Decarboxylases in Saccharomyces cerevisiae",
                "url": "https://doi.org/10.1128/AEM.01675-12",
            },
        )
    if acc == "WP5019":
        r["description"] += (
            " The corrinoid-mediated methyl transfer and carbonyl condensation are represented as one aggregate assembly step, with no free methyl-radical intermediate."
        )
    if acc == "WP5587":
        r["description"] += (
            " The graph distinguishes reversible phenylalanine transamination, DAHP condensation and the connected phenylpyruvate-to-phenylacetaldehyde Ehrlich route; collapsed upstream branches represent multiple enzymatic steps."
        )
    if acc == "WP392":
        r["description"] += (
            " The unresolved glutaredoxin redox partner is not specified; peroxidase assignments retain the diagram scope and do not establish glutathione as the exclusive physiological donor."
        )
    return {
        "source": acc,
        "source_nodes_examined": len(children(x, "DataNode")),
        "source_interactions_examined": len(ints),
        "normalizations_and_corrections": corrections,
        "unresolved_or_excluded_source_nodes": unresolved,
        "decision": NOTES[acc],
    }


def biopax(r, cache, manifest, conn):
    acc = r["id"].split(":")[1]
    ref = r["id"]
    x = ET.parse(cache / (acc + ".owl")).getroot()
    xx = bp._unification_xrefs(x)
    nodes, _ = bp._participants(x, xx, ref)
    elements = {bp._element_ref(e): e for e in x}
    for k, n in nodes.items():
        n["category"] = "protein" if k.startswith("Protein") else "small_molecule"
    for e in bp._elements(x, "Complex"):
        ident = bp._source_xref(e, xx, "Reactome")
        require(ident, "Migration precondition failed: ident")
        nodes[bp._element_ref(e)] = {
            "id": ident,
            "label": bp._text_child(e, "displayName"),
            "category": "complex",
        }
    cytosol = "GO:0005829"
    participants = list(nodes.values()) + [
        {"id": cytosol, "label": "cytosol", "category": "cellular_component"}
    ]
    edges = []
    reactions = []
    rmap = {}

    def be(s, p, o, loc, txt, description=None):
        edges.append(edge(s, p, o, ref, txt, loc, description))

    for e in bp._elements(x, "BiochemicalReaction"):
        native = bp._element_ref(e)
        rid = bp._source_xref(e, xx, "Reactome")
        rmap[native] = rid
        label = bp._text_child(e, "displayName")
        direction = bp._text_child(e, "conversionDirection")
        require(
            direction == "LEFT-TO-RIGHT",
            'Migration precondition failed: direction == "LEFT-TO-RIGHT"',
        )
        reactions.append(
            {
                "id": rid,
                "label": label,
                "category": "molecular_activity",
                "direction": "left_to_right",
            }
        )
        for side, p in [("left", "consumes"), ("right", "produces")]:
            for n in bp._children(e, side):
                nr = bp._resource(n)
                nd = nodes[nr]
                s, o = (nd["id"], rid) if side == "left" else (rid, nd["id"])
                be(
                    s,
                    p,
                    o,
                    f"#{native}/bp:{side}/#{nr}",
                    f"BioPAX {native} lists {nd['label']} on its {side} side with LEFT-TO-RIGHT conversionDirection.",
                )
        be(
            rid,
            "occurs_in",
            cytosol,
            f"#{native}; participating physicalEntity/bp:cellularLocation/#CellularLocationVocabulary1",
            f"The physical participants of BioPAX {native} are assigned to the cytosol.",
        )
    for e in bp._elements(x, "Catalysis"):
        c = bp._resource_child(e, "controller")
        target = bp._resource_child(e, "controlled")
        require(c in nodes, "Migration precondition failed: c in nodes")
        description = (
            "The native zinc-bound Mca assembly represents the aerobic purified form; Fe2+ is favored under physiological anaerobic conditions (PMID:26044118)."
            if nodes[c]["id"] == "Reactome:R-MTU-879260"
            else None
        )
        be(
            nodes[c]["id"],
            "catalyzes",
            rmap[target],
            f"#{bp._element_ref(e)}/bp:controller/#{c}; bp:controlled/#{target}",
            f"BioPAX {bp._element_ref(e)} identifies {nodes[c]['label']} as the controller of {target}.",
            description,
        )
    for k, n in nodes.items():
        e = elements[k]
        if bp._resource_child(e, "cellularLocation"):
            be(
                n["id"],
                "located_in",
                cytosol,
                f"#{k}/bp:cellularLocation/#CellularLocationVocabulary1",
                f"BioPAX {k} assigns {n['label']} to the cytosol.",
            )
        for component in bp._children(e, "component"):
            ck = bp._resource(component)
            cn = nodes[ck]
            if cn["id"] == "CHEBI:29105" or cn["id"] == "CHEBI:18420":
                cn["category"] = "cofactor"
            be(
                n["id"],
                "has_part",
                cn["id"],
                f"#{k}/bp:component/#{ck}",
                f"BioPAX {k} includes {cn['label']} as a component of {n['label']}.",
            )
    add_reference(r, source_reference(acc, ref, manifest, cache))
    note = "All native sides, controllers, complexes, cofactors and cytosol locations inspected; source comments are not attributed as quotations from cited papers."
    if acc == "R-MTU-868688":
        rid = "Reactome:R-MTU-868709"
        rhea = "CHEBI:18167"
        participants.append({"id": rhea, "label": "alpha-maltose", "category": "small_molecule"})
        edges = [
            e
            for e in edges
            if not (
                (e["subject"] == rid and e["predicate"] == "produces")
                or (e["object"] == rid and e["predicate"] == "consumes")
                or e["subject"] == "CHEBI:17306"
            )
        ]
        for s, p, o in [("CHEBI:16551", "consumes", rid), (rid, "produces", rhea)]:
            edges.append(
                edge(
                    s,
                    p,
                    o,
                    "PMID:23601637",
                    "Genetic and NMR experiments support mycobacterial TreS flux from trehalose to alpha-maltose; the biochemical reaction is reversible.",
                    "Results: TreS reaction products and physiological direction; Figure 3",
                    "Physiological direction differs from the older maltose-to-trehalose Reactome diagram.",
                )
            )
        rr = next(n for n in reactions if n["id"] == rid)
        rr["label"] = (
            "TreS interconverts trehalose and alpha-maltose (physiological trehalose consumption)"
        )
        rr["direction"] = "reversible"
        add_reference(
            r,
            {
                "id": "PMID:23601637",
                "title": "Flux through Trehalose Synthase Flows from Trehalose to the Alpha Anomer of Maltose in Mycobacteria",
                "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3918855/",
            },
        )
        r["description"] = (
            "Mycobacterium tuberculosis produces trehalose through OtsA/OtsB and TreY/TreZ routes. TreS is reversible in vitro, but experimental physiological flux consumes trehalose to produce alpha-maltose. Cytosolic catalytic assemblies include OtsA tetramer and magnesium-bound OtsB."
        )
        note += (
            " Corrected TreS physiological direction and alpha-maltose product using PMID23601637."
        )
    if acc == "R-MTU-879325":
        rid = "Reactome:R-MTU-879281"
        wrong = {"CHEBI:16768", "CHEBI:45563", "CHEBI:52283"}
        edges = [e for e in edges if not (e["subject"] in wrong or e["object"] in wrong)]
        for cid in ["CHEBI:59633", "CHEBI:58718", "CHEBI:58886"]:
            label = conn.execute(
                "select value from statements where subject=? and predicate='rdfs:label'", (cid,)
            ).fetchone()[0]
            participants.append({"id": cid, "label": label, "category": "small_molecule"})
        for s, p, o in [
            ("CHEBI:59633", "consumes", rid),
            (rid, "produces", "CHEBI:58718"),
            (rid, "produces", "CHEBI:58886"),
        ]:
            edges.append(
                edge(
                    s,
                    p,
                    o,
                    "UniProtKB:P9WJN1",
                    "Mca hydrolyzes a mycothiol S-conjugate to an S-substituted N-acetyl-L-cysteinate and glucosaminyl-inositol (RHEA:36543); the substrate is not unconjugated mycothiol.",
                    "comments[commentType=CATALYTIC ACTIVITY].reaction[RHEA:36543]",
                )
            )
        reactions[0]["label"] = (
            "Mca hydrolyzes mycothiol S-conjugates to mercapturic-acid conjugates and glucosaminyl-inositol"
        )
        r["label"] = "mycothiol S-conjugate catabolism"
        r["description"] = (
            "Mycobacterium tuberculosis Mca hydrolyzes detoxification conjugates of mycothiol to an N-acetyl-L-cysteine S-conjugate and glucosaminyl-inositol. Mca binds iron under anaerobic purification and zinc under aerobic purification; the native Reactome zinc complex describes the latter condition."
        )
        add_reference(
            r,
            {
                "id": "UniProtKB:P9WJN1",
                "title": "Mycothiol S-conjugate amidase Mca; curated catalytic reaction RHEA:36543",
                "url": "https://www.uniprot.org/uniprotkb/P9WJN1",
                "source_version": "UniProt entry retrieved 2026-10-05",
            },
        )
        participants.append({"id": "CHEBI:29033", "label": "iron(2+)", "category": "cofactor"})
        edges.append(
            edge(
                "CHEBI:29033",
                "enables",
                rid,
                "PMID:26044118",
                "Mca purified under anaerobic conditions contains stoichiometric Fe2+; the authors favor Fe2+-dependent activity under physiological conditions.",
                "Abstract: anaerobic versus aerobic Halo-Mca pull-down experiments",
                "Cofactor assignment is conditional: anaerobic Fe2+ form; the retained Reactome Zn2+ complex is the aerobic form.",
            )
        )
        note += " Replaced incorrect free-MSH/S-acetylcysteine identities with RHEA36543 conjugate classes; qualified metal dependence using PMID26044118."
    if acc in {"R-MTU-879325", "R-MTU-879299"}:
        add_reference(
            r,
            {
                "id": "PMID:26044118",
                "title": "Identity of cofactor bound to mycothiol conjugate amidase (Mca) influenced by expression and purification conditions",
                "url": "https://pubmed.ncbi.nlm.nih.gov/26044118/",
            },
        )
    if acc == "R-MTU-879299":
        r["description"] = (
            "Cytosolic mycothiol synthesis in Mycobacterium tuberculosis links Ino1, MshA, an unresolved phosphatase, MshB, MshC and MshD. Mca supplies a minor alternative deacetylase route. The source models zinc-containing Ino1, Mca and MshC assemblies; Mca metal occupancy depends on oxygen conditions. ImpC is not assigned as the unresolved phosphatase because later experiments identify it as histidinol-phosphatase."
        )
        # Resolve reaction identities and charge forms using current curated
        # UniProt/Rhea reactions, rather than erroneous legacy BioPAX xrefs.
        formulas = {
            "Reactome:R-MTU-879331": ("P9WKI1", "RHEA:10716", ["CHEBI:61548"], ["CHEBI:58401"]),
            "Reactome:R-MTU-879298": (
                "P9WMY7",
                "RHEA:26188",
                ["CHEBI:58401", "CHEBI:57705"],
                ["CHEBI:58892", "CHEBI:58223", "CHEBI:15378"],
            ),
            "Reactome:R-MTU-879319": (
                "P9WJM9",
                "RHEA:26176",
                ["CHEBI:58886", "CHEBI:35235", "CHEBI:30616"],
                ["CHEBI:58887", "CHEBI:456215", "CHEBI:33019", "CHEBI:15378"],
            ),
            "Reactome:R-MTU-879248": (
                "P9WJM7",
                "RHEA:26172",
                ["CHEBI:58887", "CHEBI:57288"],
                ["CHEBI:16768", "CHEBI:57287", "CHEBI:15378"],
            ),
        }
        affected = set(formulas)
        edges = [
            e
            for e in edges
            if not (
                (
                    e["predicate"] == "located_in"
                    and e["subject"] in {"CHEBI:58225", "CHEBI:58433", "CHEBI:52285"}
                )
                or (e["predicate"] == "consumes" and e["object"] in affected)
                or (e["predicate"] == "produces" and e["subject"] in affected)
                or (e["subject"] == "UniProtKB:P95189")
            )
        ]
        # The phosphatase substrate must match the correctly identified MshA
        # product, and the alternative Mca route feeds the charged MshC substrate.
        swaps = {
            "CHEBI:52443": "CHEBI:58892",
            "CHEBI:52283": "CHEBI:58886",
            "CHEBI:15366": "CHEBI:30089",
        }
        for e in edges:
            for k in ["subject", "object"]:
                if e[k] in swaps:
                    e[k] = swaps[e[k]]
                    e["description"] = (
                        "Chemical form reconciled with the curated MshA/MshB/MshC reaction definitions; native BioPAX topology retained."
                    )
        for rid, (protein, rhea, left, right) in formulas.items():
            ur = "UniProtKB:" + protein
            add_reference(
                r,
                {
                    "id": ur,
                    "title": f"Curated catalytic reaction {rhea} for {protein}",
                    "url": "https://www.uniprot.org/uniprotkb/" + protein,
                },
            )
            for cid in left + right:
                label = conn.execute(
                    "select value from statements where subject=? and predicate='rdfs:label'",
                    (cid,),
                ).fetchone()[0]
                participants.append({"id": cid, "label": label, "category": "small_molecule"})
            for cid in left:
                edges.append(
                    edge(
                        cid,
                        "consumes",
                        rid,
                        ur,
                        f"{rhea} identifies {cid} as a substrate.",
                        "comments[commentType=CATALYTIC ACTIVITY].reaction[" + rhea + "]",
                    )
                )
            for cid in right:
                edges.append(
                    edge(
                        rid,
                        "produces",
                        cid,
                        ur,
                        f"{rhea} identifies {cid} as a product.",
                        "comments[commentType=CATALYTIC ACTIVITY].reaction[" + rhea + "]",
                    )
                )
        # Principal MshB reaction is independently defined; retained Reactome Mca
        # activity remains an alternative with its low activity explicitly noted.
        rid = "RHEA:26180"
        ur = "UniProtKB:P9WJN3"
        reactions.append(
            {
                "id": rid,
                "label": "1D-myo-inositol 2-acetamido-2-deoxy-alpha-D-glucopyranoside + H2O = 1D-myo-inositol 2-amino-2-deoxy-alpha-D-glucopyranoside + acetate",
                "direction": "left_to_right",
                "category": "molecular_activity",
            }
        )
        participants.append({"id": ur, "label": "MshB", "category": "protein"})
        participants.append({"id": "CHEBI:30089", "label": "acetate", "category": "small_molecule"})
        for s, p, o in [
            ("CHEBI:52442", "consumes", rid),
            ("CHEBI:15377", "consumes", rid),
            (rid, "produces", "CHEBI:58886"),
            (rid, "produces", "CHEBI:30089"),
            (ur, "catalyzes", rid),
        ]:
            edges.append(
                edge(
                    s,
                    p,
                    o,
                    ur,
                    "MshB catalyzes GlcNAc-Ins deacetylation to glucosaminyl-inositol and acetate (RHEA:26180).",
                    "comments[commentType=CATALYTIC ACTIVITY].reaction[RHEA:26180]",
                )
            )
        edges.append(
            edge(
                "CHEBI:29105",
                "enables",
                rid,
                ur,
                "MshB binds one zinc ion per subunit.",
                "comments[commentType=COFACTOR]; evidence PMID:12958317, PMID:16630724",
            )
        )
        add_reference(
            r,
            {
                "id": ur,
                "title": "MshB mycothiol-biosynthesis deacetylase",
                "url": "https://www.uniprot.org/uniprotkb/P9WJN3",
                "source_version": "UniProt entry retrieved 2026-10-05",
            },
        )
        add_reference(
            r,
            {
                "id": "PMID:29752410",
                "title": "Identification and structural characterization of a histidinol phosphate phosphatase from Mycobacterium tuberculosis",
                "url": "https://pubmed.ncbi.nlm.nih.gov/29752410/",
            },
        )
        note += " Corrected Ino1/MshA stereochemical identity and MshA water/proton error; reconciled MshC/MshD charged forms/protons; added principal MshB alongside minor Mca. Removed unsupported ImpC catalyst, reidentified experimentally as HisN (PMID29752410); phosphatase catalyst remains unresolved."
    finish(r, participants, reactions, edges)
    return {
        "source": acc,
        "source_reactions_examined": len(bp._elements(x, "BiochemicalReaction")),
        "source_physical_entities_examined": len(nodes),
        "decision": note,
    }


def mibig(r, cache, manifest, conn):
    participants = [{"id": "NCBIProtein:AKL64828.1", "label": "LnyI", "category": "protein"}]
    for cid in ["CHEBI:202459", "CHEBI:202416", "CHEBI:210490"]:
        label = conn.execute(
            "select value from statements where subject=? and predicate='rdfs:label'", (cid,)
        ).fetchone()[0]
        participants.append({"id": cid, "label": label, "category": "small_molecule"})
    ref = "PMID:28919037"
    edges = [
        edge(
            "NCBIProtein:AKL64828.1",
            "enables",
            r["id"],
            ref,
            "Deleting lnyI eliminates detectable linearmycins A, B and C; complementation restores production.",
            "Results: lnyI deletion and complementation; HPLC profiles",
            "Genetic requirement for pathway output; this does not assert a specific starter-substrate reaction.",
        )
    ]
    for n in participants[1:]:
        edges.append(
            edge(
                r["id"],
                "produces",
                n["id"],
                ref,
                f"{n['label']} was detected among Streptomyces sp. Mg1 linearmycin products in the production and mutant experiments.",
                "Results: linearmycin identification and lnyI mutant/complement HPLC profiles",
            )
        )
    finish(r, participants, [], edges)
    r["references"] = [q for q in r["references"] if q["id"] != "PMID:32964081"]
    add_reference(r, source_reference("mibig-4.0", r["id"], manifest, cache))
    add_reference(
        r,
        {
            "id": ref,
            "title": "A Link between Linearmycin Biosynthesis and Extracellular Vesicle Genesis Connects Specialized Metabolism and Bacterial Membrane Physiology",
            "url": "https://doi.org/10.1016/j.chembiol.2017.08.008",
        },
    )
    genes = r["gene_clusters"][0]["genes"]
    if not any(g["id"] == "NCBIProtein:AKL64828.1" for g in genes):
        genes.append({"id": "NCBIProtein:AKL64828.1", "label": "lnyI"})
    r["description"] = (
        "The Streptomyces sp. Mg1 linearmycin gene cluster produces linearmycins A, B and C. Deletion and complementation establish LnyI as required for production. The graph records experimentally observed products and genetic dependence; detailed starter-unit chemistry and modular chain-extension assignments remain proposed."
    )
    return {
        "source": "MIBiG:BGC0002072",
        "source_compounds_examined": 4,
        "decision": "Reconstructed experimentally grounded LnyI dependence and three observed products; duplicated source linearmycin C is one entity. Proposed arginine-derived starter and PKS module skipping remain unasserted. Removed unrelated PMID32964081 (cigarette-smoking dataset). ChEBI product names, formulas and chain lengths checked against native structures.",
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--cache", type=Path, required=True)
    ap.add_argument("--chebi-db", type=Path, required=True)
    ap.add_argument("--report", type=Path, help="New preview or applied ledger destination")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    root = args.root
    manifest = {
        m["key"]: m for m in json.loads((root / "conf/identifier_sources.json").read_text())
    }
    conn = sqlite3.connect("file:" + str(args.chebi_db) + "?mode=ro", uri=True)
    sgd = {}
    for feature_line in (args.cache / "SGD_features.tab").read_text().splitlines():
        t = feature_line.split("\t")
        for key in t[3:5]:
            if key:
                sgd[key] = "SGD:" + t[0]
    wanted = set()
    prefix = {
        "CAS": "cas",
        "HMDB": "hmdb",
        "KEGG": "kegg.compound",
        "Kegg Compound": "kegg.compound",
        "KEGG Compound": "kegg.compound",
        "PubChem-compound": "pubchem.compound",
        "PubChem": "pubchem.compound",
    }
    for acc in WP:
        for n in ET.parse(args.cache / (acc + ".gpml")).getroot().iter():
            if local(n) == "Xref" and n.get("Database") in prefix:
                wanted.add(prefix[n.get("Database")] + ":" + n.get("ID"))
    wanted |= {"hmdb:HMDB" + q.split("HMDB")[1].zfill(7) for q in list(wanted) if ":HMDB" in q}
    xrefs = {}
    for s, v in conn.execute(
        "select subject,value from statements where predicate='oio:hasDbXref' and value in ("
        + ",".join("?" * len(wanted))
        + ")",
        sorted(wanted),
    ):
        xrefs.setdefault(v, set()).add(s)
    ledger, pending, targets = [], [], []
    for p in sorted((root / "data/pathways").glob("*.yaml")):
        if p.name not in [
            "2-phenylethanol-biosynthesis.yaml",
            "acetogenesis.yaml",
            "glutamate-degradation-i.yaml",
            "glutathione-glutaredoxin-redox-reaction.yaml",
            "glycogen-catabolism.yaml",
            "isoleucine-degradation.yaml",
            "linearmycin-biosynthetic-gene-cluster.yaml",
            "mycobacterium-trehalose-biosynthesis.yaml",
            "mycothiol-biosynthesis.yaml",
            "mycothiol-catabolism.yaml",
            "nad-salvage-pathway-v.yaml",
            "peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml",
            "phospholipids-degradation.yaml",
            "tca-cycle-detailed.yaml",
            "triglyceride-biosynthesis.yaml",
            "ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml",
        ]:
            continue
        targets.append(p)
    guard_baseline(targets, CAUSAL_REVIEW_BASELINE, root)
    for p in targets:
        r = yaml.safe_load(
            subprocess.check_output(
                [
                    "git",
                    "show",
                    "88744403c934a84828d373cfccb8cdaa7507ad77:" + str(p.relative_to(root)),
                ],
                cwd=root,
            )
        )
        acc = r["id"].split(":", 1)[1]
        if acc not in WP + REACTOME + ["BGC0002072"]:
            continue
        before = {k: len(r[k]) for k in ["participants", "reactions", "mechanistic_edges"]}
        if acc in WP:
            review = gpml(r, args.cache, manifest, conn, sgd, xrefs)
        elif acc in REACTOME:
            review = biopax(r, args.cache, manifest, conn)
        else:
            review = mibig(r, args.cache, manifest, conn)
        after = {k: len(r[k]) for k in before}
        review.update(
            {
                "file": str(p.relative_to(root)),
                "before": before,
                "after": after,
                "entity_scope": "All source objects, cofactors, proteins, metabolites and available compartments inspected. DNA/RNA nodes are added only when a native causal event supports them; pathway diagrams do not imply transcriptional regulation.",
            }
        )
        pending.append((p, r))
        ledger.append(review)
        print(p.name, before, "->", after)
    require(len(ledger) == 16, "Migration precondition failed: len(ledger) == 16")
    target = args.report or root / "reports/causal-graph-diagram-review.json"
    publish_curation(
        pending,
        target,
        {
            "scope": "12 WikiPathways + 3 Reactome + 1 MIBiG, every record",
            "baseline_commit": "88744403c934a84828d373cfccb8cdaa7507ad77",
            "sgd_crosswalk": {
                "url": "https://downloads.yeastgenome.org/curation/chromosomal_feature/SGD_features.tab",
                "sha256": hashlib.sha256(
                    (args.cache / "SGD_features.tab").read_bytes()
                ).hexdigest(),
            },
            "records": ledger,
        },
        apply=args.apply,
        baseline=(targets, CAUSAL_REVIEW_BASELINE, root),
    )


if __name__ == "__main__":
    main()
