#!/usr/bin/env python3
"""Apply explicitly reviewed GO-CAM identity corrections from independent sources.

The bounded decisions here are not a nearest-equation migration. UniProt
accessions, exact annotated reaction families, source bytes and independent
ChEBI/Rhea labels are checked before any record is published.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from copy import deepcopy
from pathlib import Path

import yaml

from pathwaymech.curation import publish_curation
from pathwaymech.schema import validate_record


def curate(
    root: Path,
    source: Path,
    provenance: Path,
    chebi_db: Path,
    rhea_db: Path,
    report: Path,
    apply: bool = False,
) -> list[dict]:
    raw = source.read_bytes()
    metadata = json.loads(provenance.read_text())
    if hashlib.sha256(raw).hexdigest() != metadata["sha256"]:
        raise ValueError("UniProt catalytic source checksum mismatch")
    proteins = {p["primaryAccession"]: (p, i) for i, p in enumerate(json.loads(raw)["results"])}
    con = sqlite3.connect(f"file:{chebi_db}?mode=ro", uri=True)
    rcon = sqlite3.connect(f"file:{rhea_db}?mode=ro", uri=True)
    ledger, pending = [], []

    def label(identifier):
        db = rcon if identifier.startswith("RHEA:") else con
        row = db.execute(
            "SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'", (identifier,)
        ).fetchone()
        if not row:
            raise ValueError(f"Missing independent label: {identifier}")
        return row[0]

    def evidence(record, accession, family, assertion):
        protein, index = proteins[accession]
        comments = [
            (i, c)
            for i, c in enumerate(protein.get("comments", []))
            if c["commentType"] == "CATALYTIC ACTIVITY"
            and any(x["id"] == family for x in c["reaction"].get("reactionCrossReferences", []))
        ]
        if len(comments) != 1:
            raise ValueError(f"Expected exact source reaction: {accession} {family}")
        ci, comment = comments[0]
        rid = "UniProtKB:" + accession
        if not any(x["id"] == rid for x in record["references"]):
            record["references"].append(
                {
                    "id": rid,
                    "title": f"UniProtKB {accession} catalytic annotations",
                    "url": metadata["url"],
                    "source_version": "2026_03",
                    "source_sha256": metadata["sha256"],
                }
            )
        return {
            "reference_id": rid,
            "source_assertion": assertion,
            "source_locator": (
                f"{metadata['url']} [sha256:{metadata['sha256']}] "
                f"#/results/{index}/comments/{ci}/reaction"
            ),
        }

    def read(name):
        path = root / "data/pathways" / (name + ".yaml")
        rec = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        return path, rec, deepcopy(rec)

    def finish(path, rec, before, reason):
        used = {e[k] for e in rec["mechanistic_edges"] for k in ["subject", "object"]}
        rec["participants"] = [n for n in rec["participants"] if n["id"] in used]
        validate_record(rec)
        ledger.append(
            {
                "path": str(path.relative_to(root)),
                "record": rec["id"],
                "reason": reason,
                "removed_or_changed_edges": [
                    e for e in before["mechanistic_edges"] if e not in rec["mechanistic_edges"]
                ],
                "added_or_changed_edges": [
                    e for e in rec["mechanistic_edges"] if e not in before["mechanistic_edges"]
                ],
                "reaction_labels_before": before["reactions"],
                "reaction_labels_after": rec["reactions"],
            }
        )
        pending.append((path, rec))

    def addchemical(rec, identifier):
        if not any(n["id"] == identifier for n in rec["participants"]):
            rec["participants"].append(
                {"id": identifier, "label": label(identifier), "category": "small_molecule"}
            )

    def replace_activity(rec, old, new, ev):
        node = next(n for n in rec["reactions"] if n["id"] == old)
        node.update(
            id=new, label=label(new), category="molecular_activity", direction="left_to_right"
        )
        for edge in rec["mechanistic_edges"]:
            if old not in (edge["subject"], edge["object"]):
                continue
            for key in ["subject", "object"]:
                if edge[key] == old:
                    edge[key] = new
            edge["evidence"].append(deepcopy(ev))

    # The two imported acetyl-CoA/glutamate reactions were mislabeled as methionine acylation.
    path, rec, before = read("l-arginine-biosynthesis-ii-acetyl-cycle")
    for aid, acc in [
        ("gomodel:N-ACETYLTRANSFER-RXN", "P40360"),
        ("gomodel:YeastPathways_ARGSYNBSUB-PWY/6a4c244800000704", "Q04728"),
    ]:
        node = next(n for n in rec["reactions"] if n["id"] == aid)
        node["label"] = "L-glutamate N-acetyltransferase activity, acetyl-CoA as donor"
        ev = evidence(
            rec,
            acc,
            "RHEA:24292",
            f"UniProtKB:{acc} annotates acetyl-CoA-dependent L-glutamate N-acetylation "
            "(RHEA:24292); this corrects the imported methionine-activity label.",
        )
        for edge in rec["mechanistic_edges"]:
            if edge["predicate"] == "enables" and edge["object"] == aid:
                edge["evidence"].append(deepcopy(ev))
    finish(
        path,
        rec,
        before,
        "Correct ARG2/ARG7 activity labels; chemical sides and enzyme identities retained.",
    )

    # MAE1 already has its genuine malate-to-pyruvate activity in this record.
    path, rec, before = read("gluconeogenesis-i")
    bad = "gomodel:YeastPathways_GLUCONEO-PWY-1/6690711d00001655"
    rec["reactions"] = [n for n in rec["reactions"] if n["id"] != bad]
    rec["mechanistic_edges"] = [
        e for e in rec["mechanistic_edges"] if bad not in (e["subject"], e["object"])
    ]
    correct = "gomodel:1.1.1.39-RXN"
    next(n for n in rec["reactions"] if n["id"] == correct)["label"] = (
        "malate dehydrogenase (oxaloacetate-decarboxylating) (NAD+) activity"
    )
    ev = evidence(
        rec,
        "P36013",
        "RHEA:12653",
        "UniProtKB:P36013 annotates oxidative decarboxylation of malate to "
        "pyruvate, carbon dioxide and NADH. The separate imported "
        "oxaloacetate-producing MAE1 activity is excluded.",
    )
    for e in rec["mechanistic_edges"]:
        if e["subject"] == correct or (e["predicate"] == "enables" and e["object"] == correct):
            e["evidence"].append(deepcopy(ev))
    finish(
        path,
        rec,
        before,
        "Exclude spurious nondecarboxylating MAE1 duplicate; retain independently "
        "supported MAE1 malic-enzyme branch and genuine MDH2 activity.",
    )

    # ARO8 transamination cannot consume both amino donors and produce both oxo acids.
    path, rec, before = read("tryptophan-degradation")
    aid = "gomodel:TRYPTOPHAN-AMINOTRANSFERASE-RXN"
    ev = evidence(
        rec,
        "P53090",
        "RHEA:17533",
        "UniProtKB:P53090 transaminates an aromatic L-amino acid with "
        "2-oxoglutarate to the corresponding oxo acid and L-glutamate (RHEA:17533); "
        "correct the swapped glutamate/2-oxoglutarate sides.",
    )
    for e in rec["mechanistic_edges"]:
        if e["subject"] == aid and (
            (e["predicate"] == "has_input" and e["object"] == "CHEBI:29985")
            or (e["predicate"] == "has_output" and e["object"] == "CHEBI:16810")
        ):
            e["object"] = {"CHEBI:29985": "CHEBI:16810", "CHEBI:16810": "CHEBI:29985"}[e["object"]]
            e["evidence"] = [deepcopy(ev)]
    finish(
        path,
        rec,
        before,
        "Repair ARO8 amino-group donor/acceptor sides without changing pathway "
        "direction or tryptophan identity.",
    )

    # PSA1 uses GTP and releases diphosphate, not GDP and orthophosphate.
    path, rec, before = read("dolichyl-phosphate-d-mannose-biosynthesis")
    old, new = "gomodel:MANNPGUANYLTRANGDP-RXN", "RHEA:15230"
    ev = evidence(
        rec,
        "P41940",
        "RHEA:15229",
        "UniProtKB:P41940 annotates alpha-D-mannose 1-phosphate plus GTP yielding "
        "GDP-alpha-D-mannose and diphosphate (RHEA:15229), correcting the imported "
        "GDP/orthophosphate reaction.",
    )
    replace_activity(rec, old, new, ev)
    for e in rec["mechanistic_edges"]:
        if e["subject"] == new and e["predicate"] in ["has_input", "has_output"]:
            replacement = {
                ("has_input", "CHEBI:58189"): "CHEBI:37565",
                ("has_output", "CHEBI:43474"): "CHEBI:33019",
            }.get((e["predicate"], e["object"]))
            if replacement:
                e["object"] = replacement
                addchemical(rec, replacement)
            e["evidence"] = [deepcopy(ev)]
    finish(
        path,
        rec,
        before,
        "Correct PSA1 guanylyl donor and leaving group; pathway intermediate GDP-mannose retained.",
    )

    path, rec, before = read("fatty-acid-oxidation-pathway")
    ev = evidence(
        rec,
        "Q02207",
        "RHEA:26526",
        "UniProtKB:Q02207 annotates (3R)-hydroxyacyl-CoA hydration/dehydration "
        "(RHEA:26526). FOX2 uses the R intermediate; the imported S assignment is "
        "corrected.",
    )
    replace_activity(rec, "gomodel:ENOYL-COA-HYDRAT-RXN", "RHEA:26528", ev)
    ev2 = evidence(
        rec,
        "Q02207",
        "RHEA:32711",
        "UniProtKB:Q02207 oxidizes (3R)-3-hydroxyacyl-CoA with NAD+ to "
        "3-oxoacyl-CoA and NADH (RHEA:32711), supporting the R intermediate shared "
        "with its hydratase activity.",
    )
    replace_activity(rec, "gomodel:OHACYL-COA-DEHYDROG-RXN", "RHEA:32712", ev2)
    addchemical(rec, "CHEBI:57319")
    for e in rec["mechanistic_edges"]:
        if e["object"] == "CHEBI:15455":
            e["object"] = "CHEBI:57319"
            e["evidence"] = [deepcopy(ev if e["subject"] == "RHEA:26528" else ev2)]
    old, new = "gomodel:ENOYL-COA-DELTA-ISOM-RXN", "RHEA:45241"
    ev3 = evidence(
        rec,
        "Q08558",
        "RHEA:45240",
        "UniProtKB:Q08558 annotates (3E,5Z)-dienoyl-CoA to (2E,4E)-dienoyl-CoA "
        "isomerization (RHEA:45240); DCI1 is distinct from the retained ECI1 "
        "monoene isomerase activity.",
    )
    # Native monoene ordering does not establish material flow from
    # the corrected dienoyl branch.
    rec["mechanistic_edges"] = [
        e
        for e in rec["mechanistic_edges"]
        if not (
            old in (e["subject"], e["object"])
            and e["predicate"] in ["provides_input_for", "causally_upstream_of"]
        )
    ]
    replace_activity(rec, old, new, ev3)
    for e in rec["mechanistic_edges"]:
        if e["subject"] == new and e["predicate"] in ["has_input", "has_output"]:
            e["object"] = "CHEBI:85110" if e["predicate"] == "has_input" else "CHEBI:85111"
            addchemical(rec, e["object"])
            e["evidence"] = [deepcopy(ev3)]
    finish(
        path,
        rec,
        before,
        "Correct FOX2 stereochemistry and distinguish DCI1 dienoyl auxiliary "
        "chemistry from ECI1 monoene isomerization.",
    )

    publish_curation(
        pending,
        report,
        {"source": metadata, "records": ledger},
        apply=apply,
        serialize=lambda record: yaml.safe_dump(
            record,
            sort_keys=False,
            allow_unicode=True,
            width=88,
        ),
    )
    return ledger


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path.cwd())
    p.add_argument("--uniprot-json", type=Path, required=True)
    p.add_argument("--provenance", type=Path, required=True)
    p.add_argument("--chebi-db", type=Path, required=True)
    p.add_argument("--rhea-db", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    p.add_argument("--apply", action="store_true")
    a = p.parse_args()
    rows = curate(a.root, a.uniprot_json, a.provenance, a.chebi_db, a.rhea_db, a.report, a.apply)
    print(f"{len(rows)} explicitly reviewed chemical identity corrections; applied={a.apply}")


if __name__ == "__main__":
    main()
