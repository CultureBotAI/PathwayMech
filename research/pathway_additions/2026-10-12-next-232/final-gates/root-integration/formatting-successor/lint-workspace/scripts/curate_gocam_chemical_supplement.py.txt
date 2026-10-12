"""Apply two reviewed GO-CAM source-context corrections to the original imported records.

Dry-run by default. Both records are preflighted before --apply publishes changes.
"""

import argparse
import hashlib
import json
from copy import deepcopy
from pathlib import Path

import yaml

from pathwaymech.curation import publish_curation, require
from pathwaymech.schema import validate_record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--uniprot-json", type=Path, required=True)
    parser.add_argument("--provenance", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root
    src = args.uniprot_json
    raw = src.read_bytes()
    meta = json.load(open(args.provenance))
    require(
        hashlib.sha256(raw).hexdigest() == meta["sha256"],
        "Reviewed migration source or record precondition failed",
    )
    source = json.loads(raw)
    proteins = {p["primaryAccession"]: (p, i) for i, p in enumerate(source["results"])}
    rows, pending = [], []

    def save(slug, rec, before, rationale, sources):
        validate_record(rec)
        rows.append(
            {
                "path": f"data/pathways/{slug}.yaml",
                "record": rec["id"],
                "reason": rationale,
                "sources": sources,
                "reactions_before": before["reactions"],
                "reactions_after": rec["reactions"],
                "removed_or_changed_edges": [
                    e for e in before["mechanistic_edges"] if e not in rec["mechanistic_edges"]
                ],
                "added_or_changed_edges": [
                    e for e in rec["mechanistic_edges"] if e not in before["mechanistic_edges"]
                ],
            }
        )
        pending.append((root / "data/pathways" / f"{slug}.yaml", rec))

    slug = "hexaprenyl-diphosphate-biosynthesis"
    rec = yaml.load((root / "data/pathways" / f"{slug}.yaml").read_text(), Loader=yaml.CSafeLoader)
    before = deepcopy(rec)
    p, idx = proteins["P18900"]
    require(
        p["proteinDescription"]["recommendedName"]["fullName"]["value"]
        == "Hexaprenyl pyrophosphate synthase, mitochondrial",
        "Reviewed migration source or record precondition failed",
    )
    node = next(n for n in rec["reactions"] if n["id"] == "gomodel:RXN3O-9805")
    require(
        node["label"] == "heptaprenyl diphosphate synthase activity",
        "Reviewed migration source or record precondition failed",
    )
    node["label"] = "hexaprenyl diphosphate synthase activity"
    require(
        any(
            e["subject"] == node["id"]
            and e["predicate"] == "has_output"
            and e["object"] == "CHEBI:58179"
            for e in rec["mechanistic_edges"]
        ),
        "Reviewed migration source or record precondition failed",
    )
    ref = "UniProtKB:P18900"
    if not any(r["id"] == ref for r in rec["references"]):
        rec["references"].append(
            {
                "id": ref,
                "title": "UniProtKB COQ1 hexaprenyl pyrophosphate synthase",
                "url": meta["url"],
                "source_version": "2026_03",
                "source_sha256": meta["sha256"],
            }
        )
    ev = {
        "reference_id": ref,
        "source_assertion": (
            "UniProtKB:P18900 is the yeast mitochondrial hexaprenyl pyrophosphate "
            "synthase COQ1; the native RXN3O-9805 product is hexaprenyl diphosphate, "
            "not heptaprenyl diphosphate."
        ),
        "source_locator": (
            f"{meta['url']} [sha256:{meta['sha256']}] "
            f"#/results/{idx}/proteinDescription/recommendedName"
        ),
    }
    next(
        e
        for e in rec["mechanistic_edges"]
        if e["subject"] == "SGD:S000000207"
        and e["predicate"] == "enables"
        and e["object"] == node["id"]
    )["evidence"].append(ev)
    save(
        slug,
        rec,
        before,
        "Correct imported heptaprenyl label to hexaprenyl; chemical endpoints and "
        "COQ1 assignment unchanged.",
        [ev],
    )
    slug = "adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii"
    rec = yaml.load((root / "data/pathways" / f"{slug}.yaml").read_text(), Loader=yaml.CSafeLoader)
    before = deepcopy(rec)
    aid = "gomodel:RXN0-745"
    require(
        any(n["id"] == aid for n in rec["reactions"]),
        "Reviewed migration source or record precondition failed",
    )
    require(
        not any(
            e["predicate"] == "enables" and e["object"] == aid for e in rec["mechanistic_edges"]
        ),
        "Reviewed migration source or record precondition failed",
    )
    rec["reactions"] = [n for n in rec["reactions"] if n["id"] != aid]
    rec["mechanistic_edges"] = [
        e for e in rec["mechanistic_edges"] if aid not in (e["subject"], e["object"])
    ]
    used = {e[k] for e in rec["mechanistic_edges"] for k in ["subject", "object"]}
    rec["participants"] = [n for n in rec["participants"] if n["id"] in used]
    rec["description"] = (
        "Adenosine deoxyribonucleotide biosynthesis in Saccharomyces cerevisiae "
        "S288C reduces ADP to dADP through the represented "
        "ribonucleoside-diphosphate reductase complexes and phosphorylates dADP "
        "to dATP through YNK1. The imported formate-dependent ATP-to-dATP branch "
        "has no yeast enzyme assignment and is excluded: it describes class III "
        "anaerobic ribonucleotide reductase chemistry, whereas the independently "
        "characterized yeast system reduces ribonucleoside diphosphates."
    )
    ref = {
        "id": "PMID:6370695",
        "title": (
            "Deoxyribonucleotide biosynthesis in yeast (Saccharomyces cerevisiae). A "
            "ribonucleotide reductase system of sufficient activity for DNA synthesis"
        ),
        "url": "https://pubmed.ncbi.nlm.nih.gov/6370695/",
    }
    if not any(r["id"] == ref["id"] for r in rec["references"]):
        rec["references"].append(ref)
    for e in rec["mechanistic_edges"]:
        if e["predicate"] == "enables" and e["object"] in [
            "gomodel:ADPREDUCT-RXN",
            "gomodel:YeastPathways_PWY-7220-1/6a2b236300005372",
        ]:
            e["evidence"].append(
                {
                    "reference_id": ref["id"],
                    "source_assertion": (
                        "The characterized yeast ribonucleotide reductase reduces all four "
                        "natural ribonucleoside diphosphates; ADP reduction yields the dADP "
                        "precursor used in this route."
                    ),
                    "source_locator": "https://pubmed.ncbi.nlm.nih.gov/6370695/#abstract",
                }
            )
    save(
        slug,
        rec,
        before,
        "Exclude unenabled class III formate-dependent ATP reduction from the "
        "yeast graph. Native source inclusion alone does not establish yeast "
        "activity; the directly characterized yeast reductase and exact yeast "
        "UniProt entries support diphosphate reduction.",
        [
            ref,
            {
                "url": "https://pathway.yeastgenome.org/YEAST/NEW-IMAGE?detail-level=4&object=EC-1.1.98.6&type=EC-NUMBER",
                "locator": (
                    "Summary and unofficial reactions: formate-dependent class III "
                    "Escherichia coli enzyme; not organism-specific experimental evidence for "
                    "yeast."
                ),
            },
            {
                "url": meta["url"],
                "sha256": meta["sha256"],
                "accessions": ["P21524", "P21672", "P09938", "P49723"],
                "rhea": "RHEA:23252",
            },
        ],
    )
    publish_curation(
        pending,
        args.report,
        {"source": meta, "records": rows},
        apply=args.apply,
        serialize=lambda record: yaml.safe_dump(
            record, sort_keys=False, allow_unicode=True, width=88
        ),
    )
    print(f"2 records reviewed; applied={args.apply}")


if __name__ == "__main__":
    main()
