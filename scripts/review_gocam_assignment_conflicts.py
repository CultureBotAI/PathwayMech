#!/usr/bin/env python3
"""Resolve three independently inspected GO-CAM enzyme-assignment conflicts.

Run after native reconstruction and location review. Sources must be the pinned
public responses used in the 2026-10-05 review. Removed source assertions remain
in the review ledger. This is a bounded curation, not an enzyme-name matcher.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml
from review_gocam_graphs import IndentedDumper

from pathwaymech.curation import publish_curation, require
from pathwaymech.schema import validate_record

CATALYSIS_SHA = "9600fe7f1e55a4f51554b244607a706b1604904dc71de8960b2f399bf75b0c7c"
LOCATION_SHA = "95f72dcc644358c480e0e59f996cf88533558b5fa4256460a030e0a1eaf9678d"
PRIMARY_SHA = {
    "18205391.json": "b9820457a9d76383f1d6f6c3ad703ab588658bdfb3a6062e5600da3e91cc89ae",
    "23106124.xml": "e94acef71d3565c9573458d08d460e98af470a29bd69e63f57d7a716d0f77649",
    "STR2.html": "ea882c3e1f62e6e4d44e3d5b9851f6899b2b7c69b15d38f27ee169abd20e6917",
}


def curate(
    records: dict,
    batch: dict,
    provenance: dict,
    primary: dict,
    locations: dict,
    location_meta: dict,
) -> dict:
    ledger = {"sources": primary, "superseded_edges": [], "decisions": []}
    proteins = {p["primaryAccession"]: (i, p) for i, p in enumerate(batch["results"])}

    def reference(record, acc):
        rid = f"UniProtKB:{acc}"
        if not any(r["id"] == rid for r in record["references"]):
            record["references"].append(
                {
                    "id": rid,
                    "title": f"Reviewed UniProt {acc}: catalytic-function assertions",
                    "url": provenance["url"],
                    "source_version": "2026_03",
                    "source_sha256": CATALYSIS_SHA,
                }
            )

    def ev(acc, comment_index, text):
        index, _ = proteins[acc]
        return {
            "reference_id": f"UniProtKB:{acc}",
            "source_assertion": text,
            "source_locator": f"{provenance['url']} [sha256:{CATALYSIS_SHA}] "
            f"#/results/{index}/comments/{comment_index}",
        }

    def remove(record, predicate, reason):
        keep = []
        for edge in record["mechanistic_edges"]:
            if predicate(edge):
                ledger["superseded_edges"].append(
                    {
                        "record": record["id"],
                        "edge": copy.deepcopy(edge),
                        "reason": reason,
                    }
                )
            else:
                keep.append(edge)
        record["mechanistic_edges"] = keep

    record = records["l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde"]
    obsolete = {"gomodel:ARYLFORMAMIDASE-RXN", "SGD:S000003596"}
    reason = (
        "PMID:18205391 experimentally rejects BNA3 as formylkynurenine formamidase "
        "and identifies BNA7. The independently represented BNA7 reaction is retained."
    )
    remove(record, lambda e: bool(obsolete & {e["subject"], e["object"]}), reason)
    for key in ("participants", "reactions"):
        record[key] = [n for n in record[key] if n["id"] not in obsolete]
    record["description"] = record["description"].replace(
        "through BNA3 or BNA7 arylformamidase activity", "through BNA7 arylformamidase activity"
    )
    reference(record, "Q04066")
    for edge in record["mechanistic_edges"]:
        if edge["subject"] == "SGD:S000002836" and edge["predicate"] == "enables":
            evidence = ev(
                "Q04066",
                0,
                "UniProt Q04066 assigns N-formyl-L-kynurenine hydrolysis to BNA7, "
                "with experimental support from PMID:18205391.",
            )
            if evidence not in edge["evidence"]:
                edge["evidence"].append(evidence)
            edge["description"] = reason
    ledger["decisions"].append({"record": record["id"], "decision": reason})

    record = records["l-lysine-biosynthesis-iv"]
    reaction = "gomodel:RXN3O-1983"
    reason = (
        "PMID:23106124 separates homocitrate dehydration (ACO2, with minor ACO1 "
        "contribution) from homoaconitate hydration (LYS4)."
    )
    remove(
        record,
        lambda e: (
            e["subject"] == "SGD:S000002642"
            and e["object"] == reaction
            and e["predicate"] == "enables"
        ),
        reason,
    )
    for node in record["reactions"]:
        if node["id"] == reaction:
            node["label"] = "homocitrate dehydratase activity"
    for acc, sgd, label, statement in [
        (
            "P39533",
            "S000003736",
            "ACO2 Scer",
            "UniProt P39533 assigns reversible (R)-homocitrate dehydration to "
            "cis-homoaconitate to ACO2, supported by PMID:23106124.",
        ),
        (
            "P19414",
            "S000004295",
            "ACO1 Scer",
            "UniProt P19414 assigns a minor contribution to reversible (R)-homocitrate "
            "dehydration to ACO1, supported by PMID:23106124.",
        ),
    ]:
        protein = f"SGD:{sgd}"
        index, row = proteins[acc]
        require(
            any(x["database"] == "SGD" and x["id"] == sgd for x in row["uniProtKBCrossReferences"]),
            "Reviewed migration source or record precondition failed",
        )
        reference(record, acc)
        if not any(n["id"] == protein for n in record["participants"]):
            record["participants"].append({"id": protein, "label": label, "category": "protein"})
        eid = f"assignment-{acc}-homocitrate"
        if not any(e["id"] == eid for e in record["mechanistic_edges"]):
            record["mechanistic_edges"].append(
                {
                    "id": eid,
                    "subject": protein,
                    "predicate": "enables",
                    "object": reaction,
                    "description": reason,
                    "evidence": [
                        ev(acc, 0, statement),
                        {
                            "reference_id": f"UniProtKB:{acc}",
                            "source_assertion": (
                                f"UniProt {acc} has the exact SGD cross-reference {protein}."
                            ),
                            "source_locator": f"{provenance['url']} [sha256:{CATALYSIS_SHA}] "
                            f"#/results/{index}/uniProtKBCrossReferences",
                        },
                    ],
                }
            )
        loc_index, loc_protein = next(
            (i, p) for i, p in enumerate(locations["results"]) if p["primaryAccession"] == acc
        )
        loc_comment = loc_protein["comments"][1]
        require(
            loc_comment["commentType"] == "SUBCELLULAR LOCATION",
            "Reviewed migration source or record precondition failed",
        )
        for j, loc in enumerate(loc_comment["subcellularLocations"]):
            sid = loc["location"]["id"]
            oid, label = {
                "SL-0173": ("GO:0005739", "mitochondrion"),
                "SL-0086": ("GO:0005737", "cytoplasm"),
            }[sid]
            if not any(n["id"] == oid for n in record["participants"]):
                record["participants"].append(
                    {
                        "id": oid,
                        "label": label,
                        "category": "cellular_component",
                    }
                )
            eid = f"assignment-location-{acc}-{sid}"
            if not any(e["id"] == eid for e in record["mechanistic_edges"]):
                record["mechanistic_edges"].append(
                    {
                        "id": eid,
                        "subject": protein,
                        "predicate": "located_in",
                        "object": oid,
                        "description": "Physical protein location; does not place every activity "
                        "of this enzyme in this compartment. ACO1 is mainly mitochondrial.",
                        "evidence": [
                            {
                                "reference_id": f"UniProtKB:{acc}",
                                "source_assertion": f"UniProt {acc} annotates location "
                                f"{loc['location']['value']} ({sid}).",
                                "source_locator": f"{location_meta['url']} [sha256:{LOCATION_SHA}] "
                                f"#/results/{loc_index}/comments/1/subcellularLocations/{j}",
                            }
                        ],
                    }
                )
    record["description"] += (
        (
            " Homocitrate dehydration is assigned to ACO2 with a minor ACO1 contribution; "
            "LYS4 catalyzes the following homoaconitate hydration."
        )
        if "Homocitrate dehydration is assigned" not in record["description"]
        else ""
    )
    ledger["decisions"].append({"record": record["id"], "decision": reason})

    record = records["homocysteine-and-cysteine-interconversion"]
    str2 = primary["STR2.html"]
    if not any(r["id"] == "SGD:S000003891" for r in record["references"]):
        record["references"].append(
            {
                "id": "SGD:S000003891",
                "title": "YeastCyc STR2: two annotated reactions",
                "url": str2["url"],
                "source_version": "YeastCyc 22.5; retrieved 2026-10-05",
                "source_sha256": str2["sha256"],
            }
        )
    reason = (
        "Retain the native O-acetylhomoserine reaction: inspected YeastCyc STR2 "
        "lists both O-acetyl and O-succinyl reactions. UniProt P47164 lists only "
        "O-succinylhomoserine; that difference does not disprove the O-acetyl route."
    )
    for edge in record["mechanistic_edges"]:
        if edge["subject"] == "SGD:S000003891" and edge["predicate"] == "enables":
            edge["description"] = reason
            evidence = {
                "reference_id": "SGD:S000003891",
                "source_assertion": "YeastCyc STR2 lists RXN-721: L-cysteine + "
                "O-acetyl-L-homoserine -> L-cystathionine + acetate, as well as "
                "O-SUCCHOMOSERLYASE-RXN with O-succinyl-L-homoserine.",
                "source_locator": f"{str2['url']} [sha256:{str2['sha256']}] "
                "Reactions table / RXN-721 and O-SUCCHOMOSERLYASE-RXN",
            }
            if evidence not in edge["evidence"]:
                edge["evidence"].append(evidence)
    ledger["decisions"].append({"record": record["id"], "decision": reason})
    return ledger


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--records", type=Path, default=Path("data/pathways"))
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    raw = (args.source_dir / "uniprot-yeast-reviewed-catalysis.json").read_bytes()
    require(
        hashlib.sha256(raw).hexdigest() == CATALYSIS_SHA,
        "Reviewed migration source or record precondition failed",
    )
    meta = json.loads(
        (args.source_dir / "uniprot-yeast-reviewed-catalysis.provenance.json").read_text()
    )
    require(
        meta["sha256"] == CATALYSIS_SHA, "Reviewed migration source or record precondition failed"
    )
    loc_raw = (args.source_dir / "uniprot-yeast-reviewed-locations.json").read_bytes()
    require(
        hashlib.sha256(loc_raw).hexdigest() == LOCATION_SHA,
        "Reviewed migration source or record precondition failed",
    )
    loc_meta = json.loads(
        (args.source_dir / "uniprot-yeast-reviewed-locations.provenance.json").read_text()
    )
    require(
        loc_meta["sha256"] == LOCATION_SHA,
        "Reviewed migration source or record precondition failed",
    )
    primary = {}
    for filename, digest in PRIMARY_SHA.items():
        path = args.source_dir / "root-function-review" / filename
        require(
            hashlib.sha256(path.read_bytes()).hexdigest() == digest,
            "Reviewed migration source or record precondition failed",
        )
        primary[filename] = json.loads(path.with_name(filename + ".provenance.json").read_text())
        require(
            primary[filename]["sha256"] == digest,
            "Reviewed migration source or record precondition failed",
        )
    names = [
        "l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde",
        "l-lysine-biosynthesis-iv",
        "homocysteine-and-cysteine-interconversion",
    ]
    records = {n: yaml.safe_load((args.records / f"{n}.yaml").read_text()) for n in names}
    old = copy.deepcopy(records)
    report = curate(records, json.loads(raw), meta, primary, json.loads(loc_raw), loc_meta)
    for record in records.values():
        validate_record(record)
    changed = [n for n in names if old[n] != records[n]]
    if args.report.exists():
        previous = json.loads(args.report.read_text())
        for item in previous["superseded_edges"]:
            if item not in report["superseded_edges"]:
                report["superseded_edges"].append(item)
    publish_curation(
        [(args.records / f"{name}.yaml", records[name]) for name in changed],
        args.report,
        report,
        apply=args.apply,
        serialize=lambda record: yaml.dump(
            record,
            Dumper=IndentedDumper,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        ),
    )
    print(json.dumps({"changed": changed, "removed_edges": len(report["superseded_edges"])}))


if __name__ == "__main__":
    main()
