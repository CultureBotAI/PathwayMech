#!/usr/bin/env python3
"""Apply bounded, independently reviewed corrections to native GO-CAM chemistry.

Run after native reconstruction and compartment review. Dry-run by default;
every removed edge is retained in the output ledger. Exact raw UniProt records
are supplied in --source-dir, with matching .provenance.json sidecars.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path

import yaml

from pathwaymech.curation import may_publish_report as may_publish_report
from pathwaymech.curation import publish_curation
from pathwaymech.schema import validate_record

SOURCE_HASHES = {
    "P26364": "6f63766ee236ebf46d0823f592d7405d0c8fbec5c26ef084abcdbd93762cb44d",
    "Q07560": "4776cb2392de0f791dccac79c1e4ce3b203239abfb46d2dcab9ae4ffada2c30d",
    "Q07748": "3b3a42882440ce399581bed512ee732900b8883a786945a0ffa216a8b33a7755",
    "P31373": "638720a084d63d174e8dbe326df5ad3926c75ee314967ab5e42554c3e95acfd0",
    "P10127": "97be223ce25902e49752471334cdf199b06ac58a39c7874ad16412defbcb31f8",
    "P38113": "436f2f181751408bc68ab665aff1edcd6e29386b153cbed7fab0d959f55d14cf",
    "P15700": "0558d409b3620b20cc57c77b6e3cf019b4606d9c0402d6568ceb0e6440aa4385",
    "P32318": "c07f0cf9365410e43a34cc0f50d55b265f76a045e0dddb5821c6bb3c9120ec60",
}


def load_sources(directory: Path) -> dict:
    sources = {}
    for acc, digest in SOURCE_HASHES.items():
        raw = (directory / f"{acc}.json").read_bytes()
        meta = json.loads((directory / f"{acc}.provenance.json").read_text())
        if hashlib.sha256(raw).hexdigest() != digest or meta["sha256"] != digest:
            raise ValueError(f"Unreviewed source representation: {acc}")
        entry = json.loads(raw)
        if entry["primaryAccession"] != acc or "reviewed" not in entry["entryType"]:
            raise ValueError(f"Wrong reviewed protein identity: {acc}")
        sources[acc] = {"entry": entry, "provenance": meta}
    return sources


def evidence(sources: dict, acc: str, pointer: str, assertion: str) -> dict:
    if len(assertion) > 400:
        raise ValueError("Structured assertion exceeds schema limit")
    meta = sources[acc]["provenance"]
    return {
        "reference_id": f"UniProtKB:{acc}",
        "source_assertion": assertion,
        "source_locator": f"{meta['url']} [sha256:{meta['sha256']}] #{pointer}",
    }


def add_reference(record: dict, sources: dict, acc: str) -> None:
    if any(ref["id"] == f"UniProtKB:{acc}" for ref in record["references"]):
        return
    meta = sources[acc]["provenance"]
    record["references"].append(
        {
            "id": f"UniProtKB:{acc}",
            "title": f"Reviewed UniProt {acc}: bounded catalytic-function review",
            "url": meta["url"],
            "source_version": meta["release"],
            "source_sha256": meta["sha256"],
        }
    )


def add_edge(record: dict, subject: str, predicate: str, obj: str, ev: list, note: str) -> None:
    digest = hashlib.sha256(f"{subject}|{predicate}|{obj}".encode()).hexdigest()[:12]
    edge = {
        "id": f"function-{digest}",
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "description": note,
        "evidence": ev,
    }
    if not any(e["id"] == edge["id"] for e in record["mechanistic_edges"]):
        record["mechanistic_edges"].append(edge)


def remove_edges(record: dict, predicate, ledger: dict, reason: str) -> None:
    kept = []
    for edge in record["mechanistic_edges"]:
        if predicate(edge):
            ledger["superseded_edges"].append({"edge": deepcopy(edge), "reason": reason})
        else:
            kept.append(edge)
    record["mechanistic_edges"] = kept


def remove_activity(record: dict, activity: str, protein: str, ledger: dict, reason: str):
    remove_edges(
        record,
        lambda e: activity in (e["subject"], e["object"]),
        ledger,
        reason,
    )
    record["reactions"] = [n for n in record["reactions"] if n["id"] != activity]
    if not any(
        e["subject"] == protein and e["predicate"] == "enables" for e in record["mechanistic_edges"]
    ):
        remove_edges(record, lambda e: protein in (e["subject"], e["object"]), ledger, reason)
        record["participants"] = [n for n in record["participants"] if n["id"] != protein]


def replace_chemistry(
    record, activity, inputs, outputs, sources, acc, labels, ledger, note, *, assertion=None
):
    remove_edges(
        record,
        lambda e: e["subject"] == activity and e["predicate"] in ("has_input", "has_output"),
        ledger,
        note,
    )
    add_reference(record, sources, acc)
    entry = sources[acc]["entry"]
    ci = next(
        i for i, c in enumerate(entry["comments"]) if c["commentType"] == "CATALYTIC ACTIVITY"
    )
    # A bounded assertion can retain only the supported portion of an inherited
    # equation. The full source equation remains in the review ledger.
    statement = assertion or entry["comments"][ci]["reaction"]["name"]
    ev = [evidence(sources, acc, f"/comments/{ci}/reaction", statement)]
    if acc == "P26364":
        ev.append(
            evidence(
                sources,
                acc,
                "/comments/0/texts/0",
                (
                    "ADK2 has GTP:AMP and ITP:AMP phosphotransferase activity and does not "
                    "accept ATP as phosphate donor. This branch represents its GTP reaction."
                ),
            )
        )
    for predicate, ids in (("has_input", inputs), ("has_output", outputs)):
        for curie in ids:
            if not any(n["id"] == curie for n in record["participants"]):
                node = {"id": curie, "label": labels[curie]}
                if "residue" not in labels[curie]:
                    node["category"] = (
                        "lipid"
                        if curie in {"CHEBI:58332", "CHEBI:62237", "CHEBI:64716"}
                        else "small_molecule"
                    )
                record["participants"].append(node)
            add_edge(record, activity, predicate, curie, ev, note)


def curate(record: dict, sources: dict, labels: dict) -> tuple[dict, dict]:
    record = deepcopy(record)
    ledger = {"record": record["id"], "superseded_edges": [], "decisions": []}
    rid = record["id"]
    if rid == "gomodel:YeastPathways_PWY3O-4300":
        for acc, activity, protein in (
            ("P10127", "gomodel:YeastPathways_PWY3O-4300/6a4c244800003351", "SGD:S000003225"),
            ("P38113", "gomodel:YeastPathways_PWY3O-4300/6a4c244800003369", "SGD:S000000349"),
        ):
            reason = (
                f"{acc}: reviewed FUNCTION reports no physiological ethanol oxidation "
                "role; exclude this imported ethanol-degradation branch. This does not "
                "negate in-vitro alcohol dehydrogenase activity or higher-alcohol routes."
            )
            remove_activity(record, activity, protein, ledger, reason)
            add_reference(record, sources, acc)
            ledger["decisions"].append(
                {
                    "reason": reason,
                    "evidence": evidence(sources, acc, "/comments/0/texts/0", reason),
                }
            )
    elif rid == "gomodel:YeastPathways_PWY-7219":
        activity = "gomodel:YeastPathways_PWY-7219/6a4c244800000590"
        note = "Reviewed ADK2 uses GTP, not ATP, to phosphorylate AMP; native instance retained."
        replace_chemistry(
            record,
            activity,
            ["CHEBI:37565", "CHEBI:456215"],
            ["CHEBI:58189", "CHEBI:456216"],
            sources,
            "P26364",
            labels,
            ledger,
            note,
        )
        next(n for n in record["reactions"] if n["id"] == activity)["label"] = (
            "GTP:AMP phosphotransferase activity"
        )
        ledger["decisions"].append(note)
    elif rid == "gomodel:YeastPathways_PHOSLIPSYN2-PWY-1":
        note = (
            "Yeast CRD1 is the CMP-forming cardiolipin synthase: CDP-diacylglycerol "
            "and phosphatidylglycerol are inputs; cardiolipin, CMP and H+ are outputs. "
            "The imported bacterial glycerol-forming chemistry is superseded."
        )
        replace_chemistry(
            record,
            "gomodel:CARDIOLIPSYN-RXN",
            ["CHEBI:58332", "CHEBI:64716"],
            ["CHEBI:62237", "CHEBI:60377", "CHEBI:15378"],
            sources,
            "Q07560",
            labels,
            ledger,
            note,
        )
        ledger["decisions"].append(note)
    elif rid == "gomodel:YeastPathways_PWY3O-17":
        activity = "gomodel:RXN3O-9804"
        note = (
            "Single-turnover THI13 chemistry inferred by similarity to THI5 (ECO:0000250, "
            "UniProtKB:P43534). Histidine and PLP-lysine are protein-bound residues, "
            "not free histidine substrates. HMP-phosphate is the product. "
            "The inherited exact iron redox, water/proton balance, 3-oxopropanoate and "
            "residue-product assertions are quarantined: "
            "PMID:35675507 reports Fe(II)/oxygen dependence and different PLP-derived "
            "products for Candida albicans THI5, and a histidine-derived alpha-ketoacid "
            "for both Candida THI5 and S. cerevisiae THI5. These homolog experiments are "
            "not direct evidence for S. cerevisiae THI13; no replacement oxygen or product edges, "
            "or complete net stoichiometry, are inferred. Omitted products and balancing "
            "species remain unresolved, rather than asserted absent."
        )
        replace_chemistry(
            record,
            activity,
            ["CHEBI:143915", "CHEBI:29979"],
            ["CHEBI:58354"],
            sources,
            "Q07748",
            labels,
            ledger,
            note,
            assertion=(
                "The THI13 annotation, inferred by similarity to THI5, uses protein-bound "
                "PLP-lysine and histidine residues and forms HMP-phosphate. This bounded "
                "projection retains those core endpoints of the source equation, without "
                "asserting its exact net stoichiometry or residue and small-molecule products."
            ),
        )
        if not any(ref["id"] == "PMID:35675507" for ref in record["references"]):
            record["references"].append(
                {
                    "id": "PMID:35675507",
                    "title": (
                        "Mechanistic Studies on the Single-Turnover Yeast Thiamin "
                        "Pyrimidine Synthase: Characterization of the Inactive Enzyme"
                    ),
                    "url": "https://doi.org/10.1021/jacs.2c03322",
                }
            )
        ledger["decisions"].append(
            {
                "source_conflict": "PMID:35675507",
                "source_locator": (
                    "JACS 144 (2022), pp. 10711-10714, Results and Discussion; Figures 2-5"
                ),
                "scope": note,
                "inherited_reaction": deepcopy(
                    sources["Q07748"]["entry"]["comments"][1]["reaction"]
                ),
                "quarantined_endpoints": [
                    "CHEBI:29034",
                    "CHEBI:29033",
                    "CHEBI:33190",
                    "CHEBI:15377",
                    "CHEBI:15378",
                    "CHEBI:157692",
                    "CHEBI:29969",
                ],
            }
        )
        remove_edges(
            record,
            lambda e: e["subject"] == activity and e["predicate"] == "provides_input_for",
            ledger,
            "HMP-phosphate bypasses HMP kinase; original unphosphorylated-HMP linkage superseded.",
        )
        ev = [
            evidence(
                sources,
                "Q07748",
                "/comments/1/reaction",
                (
                    "THI13 has HMP-phosphate as a product; it supplies the substrate of "
                    "the source model's phosphomethylpyrimidine kinase activities."
                ),
            )
        ]
        for target in ("gomodel:PYRIMSYN3-RXN", "gomodel:YeastPathways_PWY3O-17/6a4c244800007677"):
            # Join the independently corrected product to inspected native input evidence.
            native = next(
                e
                for e in record["mechanistic_edges"]
                if e["subject"] == target
                and e["predicate"] == "has_input"
                and e["object"] == "CHEBI:58354"
            )
            add_edge(
                record,
                activity,
                "provides_input_for",
                target,
                ev + deepcopy(native["evidence"]),
                note,
            )
        for e in record["mechanistic_edges"]:
            if e["object"] == activity and e["predicate"] == "enables":
                e["description"] = note
                ev = evidence(
                    sources,
                    "Q07748",
                    "/comments/0/texts/0",
                    (
                        "THI13 uses its active-site histidine and protein-bound PLP to form "
                        "HMP-phosphate in a single turnover, generating inactive enzyme; "
                        "this annotation is inferred by similarity to THI5."
                    ),
                )
                if ev not in e["evidence"]:
                    e["evidence"].append(ev)
        ledger["decisions"].append(note)
        note = (
            "THI4 forms ADP-thiazole using its own cysteine residue as sulfur donor, "
            "leaving a dehydroalanine residue after one turnover. The reviewed "
            "equation produces three waters and two H+; it does not identify THI4 "
            "as the enzyme for downstream ADP-thiazole hydrolysis."
        )
        replace_chemistry(
            record,
            "gomodel:RXN3O-401",
            ["CHEBI:29950", "CHEBI:57305", "CHEBI:57540"],
            ["CHEBI:90873", "CHEBI:139151", "CHEBI:17154", "CHEBI:15377", "CHEBI:15378"],
            sources,
            "P32318",
            labels,
            ledger,
            note,
        )
        remove_edges(
            record,
            lambda e: (
                e["subject"] == "SGD:S000003376"
                and e["predicate"] == "enables"
                and e["object"] == "gomodel:RXNQT-4301"
            ),
            ledger,
            "THI4 supports ADP-thiazole formation, not the model's downstream hydrolysis.",
        )
        for e in record["mechanistic_edges"]:
            if e["subject"] == "gomodel:RXNQT-4301" and e["predicate"] in (
                "has_input",
                "has_output",
            ):
                e["description"] = (
                    "Native model bridge from ADP-thiazole to thiazole phosphate; "
                    "the physiological enzyme assignment remains unresolved. "
                    "THI4 is not assigned to this hydrolysis/decarboxylation step."
                )
        ledger["decisions"].append(note)
    elif rid == "gomodel:YeastPathways_THREOCAT2-PWY":
        note = (
            "CYS3 physiologically cleaves cystathionine to cysteine and 2-oxobutanoate. "
            "Its imported reverse condensation is unsupported and is a neighbouring "
            "cysteine-pathway reaction, not a threonine degradation step."
        )
        remove_activity(record, "gomodel:CYSTAGLY-RXN", "SGD:S000000010", ledger, note)
        record["description"] = (
            "Threonine degradation in Saccharomyces cerevisiae S288C includes "
            "CHA1-enabled threonine deamination to 2-oxobutanoate and the GLY1 "
            "threonine aldolase route to glycine and acetaldehyde. The broader native "
            "outline contains unassigned or neighbouring reactions; KBL is absent "
            "and threonine dehydrogenase is uncertain in yeast. An unsupported "
            "reverse cystathionine-condensation branch is excluded."
        )
        add_reference(record, sources, "P31373")
        ledger["decisions"].append(
            {
                "reason": note,
                "evidence": evidence(
                    sources, "P31373", "/comments/1/physiologicalReactions/0", note
                ),
            }
        )
    elif rid == "gomodel:YeastPathways_YEAST-RNT-SALV":
        note = (
            "URA6-mediated CMP phosphorylation is disputed: UniProt's CAUTION reports "
            "positive results in PMID:1333436/Ref.8 and negative results in "
            "PMID:2172245/8391780. Retain the native branch as a qualified biochemical "
            "possibility, not an established physiological substrate assignment."
        )
        add_reference(record, sources, "P15700")
        ci = next(
            i
            for i, c in enumerate(sources["P15700"]["entry"]["comments"])
            if c["commentType"] == "CAUTION"
        )
        for e in record["mechanistic_edges"]:
            if e["object"] == "gomodel:RXN-11832" and e["predicate"] == "enables":
                e["description"] = note
                ev = evidence(sources, "P15700", f"/comments/{ci}/texts/0", note)
                if ev not in e["evidence"]:
                    e["evidence"].append(ev)
        ledger["decisions"].append(note)
    if ledger["decisions"]:
        # Prune newly orphaned participants, without changing unrelated preexisting nodes.
        involved = {
            x
            for item in ledger["superseded_edges"]
            for x in (item["edge"]["subject"], item["edge"]["object"])
        }
        used = {x for e in record["mechanistic_edges"] for x in (e["subject"], e["object"])}
        record["participants"] = [
            n for n in record["participants"] if n["id"] not in involved or n["id"] in used
        ]
    validate_record(record)
    return record, ledger


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--chebi-db", type=Path, required=True)
    parser.add_argument("--records", type=Path, default=Path("data/pathways"))
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    sources = load_sources(args.source_dir)
    with sqlite3.connect(args.chebi_db) as connection:
        labels = dict(
            connection.execute("SELECT subject,value FROM statements WHERE predicate='rdfs:label'")
        )
    report = {"applied": args.apply, "sources": {}, "records": []}
    for acc, src in sources.items():
        report["sources"][acc] = {
            **src["provenance"],
            "comments": [
                {"pointer": f"/comments/{i}", "assertion": c}
                for i, c in enumerate(src["entry"]["comments"])
                if c["commentType"] in ("FUNCTION", "CATALYTIC ACTIVITY", "CAUTION")
            ],
        }
    candidates = []
    for path in sorted(args.records.rglob("*.yaml")):
        before = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if not before["id"].startswith("gomodel:"):
            continue
        after, ledger = curate(before, sources, labels)
        if after != before:
            candidates.append((path, after))
            report["records"].append({"path": str(path), **ledger})
    if args.apply:
        stamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        for _path, record in candidates:
            record.setdefault("curation_history", []).append(
                {
                    "timestamp": stamp,
                    "curator": "Codex",
                    "action": "review-catalytic-function",
                    "changes": "Reconciled native GO-CAM chemistry with independently reviewed "
                    "enzyme specificity, direction, physiological scope and source cautions; "
                    "superseded facts remain in the function review ledger.",
                    "llm_assisted": True,
                }
            )
    publish_curation(candidates, args.report, report, apply=args.apply)
    print(f"{len(candidates)} records {'updated' if args.apply else 'would change'}")


if __name__ == "__main__":
    main()
