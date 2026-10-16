#!/usr/bin/env python3
"""Text-embed every PathwayMech pathway record into a dense vector with a LOCAL model.

Output (data/embeddings/, vectors gitignored — large and rebuildable):
  vectors.f16.npy   float16 [N, dim], L2-normalized, row i <-> ids[i]
  ids.json          the N record identifiers, in row order
  records.json      light metadata per record (id, slug, label, pathway_type, class, taxon)
  meta.json         {model, dim, count, normalized, excluded_fields, corpus_fingerprint}
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "pathways"
OUT = REPO_ROOT / "data" / "embeddings"

EXCLUDED = (
    "source_locator",
    "source_assertion",
    "layout",
    "curation_status",
)


def broad_pathway_class(pathway_type: str | None) -> str:
    """Group fine-grained pathway_type values into <=12 broad metabolic categories."""
    raw = (pathway_type or "").strip().lower()
    if not raw:
        return "other-pathway"
    if "amino-acid-biosynthesis" in raw or raw == "beta-alanine-biosynthesis":
        return "amino-acid-biosynthesis"
    if any(
        k in raw
        for k in (
            "amino-acid-degradation",
            "amino-acid-metabolism",
            "glycated-amino-acid",
            "leucine-degradation",
            "tyrosine-degradation",
            "threonine-catabolism",
        )
    ):
        return "amino-acid-degradation"
    if any(
        k in raw
        for k in (
            "cofactor",
            "folate",
            "biotin",
            "lipoate",
            "siroheme",
            "menaquinol",
            "pterin",
            "tetrapyrrole",
            "corrinoid",
            "nad-salvage",
            "prosthetic-group",
        )
    ):
        return "cofactor-biosynthesis"
    if any(
        k in raw
        for k in (
            "carbohydrate",
            "galactose",
            "galactonate",
            "glycogen",
            "pentose-phosphate",
            "sulfo-emp",
            "sulfo-ed",
            "ribose",
        )
    ):
        return "carbohydrate-metabolism"
    if any(
        k in raw
        for k in (
            "lipid-biosynthesis",
            "fatty-acid",
            "sphingolipid",
            "isoprenoid",
            "glycerol-biosynthesis",
            "inositol",
            "phospholipid",
            "carnitine",
        )
    ):
        return "lipid-and-fatty-acid"
    if any(
        k in raw
        for k in (
            "nucleotide",
            "purine",
            "pyrimidine",
            "deazapurine",
            "pseudouridine",
            "allantoin",
            "uracil",
        )
    ):
        return "nucleotide-metabolism"
    if any(
        k in raw
        for k in (
            "aromatic",
            "gentisate",
            "homogentisate",
            "curcumin",
        )
    ):
        return "aromatic-compound-catabolism"
    if any(
        k in raw
        for k in (
            "central-carbon",
            "carbon-fixation",
            "glyoxylate",
            "energy",
            "fermentation",
            "acetogenesis",
            "methanogenesis",
            "anaerobic-respiration",
            "acetyl-coa",
            "succinate",
            "propionate",
        )
    ):
        return "central-carbon-and-energy"
    if any(
        k in raw
        for k in (
            "biosynthetic-gene-cluster",
            "siderophore",
            "aerobactin",
            "bacillibactin",
            "desferrioxamine",
            "petrobactin",
            "pyochelin",
            "staphyloferrin",
            "dihydroxybenzoate",
            "ergothioneine",
        )
    ):
        return "siderophore-and-secondary"
    if any(
        k in raw
        for k in (
            "cell-wall",
            "glycan",
            "rhamnose",
            "heptose",
            "amino-sugar",
            "lipid-a",
            "storage-polymer",
            "compatible-solute",
            "polyamine-biosynthesis",
        )
    ):
        return "cell-wall-and-glycan"
    if any(
        k in raw
        for k in (
            "degradation",
            "detoxification",
            "catabolism",
            "glutathione",
            "thiol-redox",
        )
    ):
        return "other-degradation-and-detox"
    return "other-pathway"


def humanize(value: str) -> str:
    return (value or "").replace("_", " ").replace("-", " ").strip()


def build_document(record: dict) -> str:
    """One document per pathway record, ordered most discriminative first."""
    parts: list[str] = [str(record.get("label") or record.get("id"))]

    ptype = humanize(str(record.get("pathway_type") or ""))
    if ptype:
        parts.append(f"pathway type: {ptype}")

    taxa = [
        str(t.get("label") or t.get("id"))
        for t in (record.get("taxa") or [])
        if isinstance(t, dict) and (t.get("label") or t.get("id"))
    ]
    if taxa:
        parts.append("organisms: " + ", ".join(taxa[:6]))

    if record.get("description"):
        parts.append(str(record["description"]))

    participants = record.get("participants") or []
    proteins = [
        str(p.get("label") or p.get("id"))
        for p in participants
        if isinstance(p, dict) and p.get("category") in ("protein", "gene_product")
    ]
    if proteins:
        parts.append("enzymes and proteins: " + ", ".join(dict.fromkeys(proteins[:16])))

    metabolites = [
        str(p.get("label") or p.get("id"))
        for p in participants
        if isinstance(p, dict) and p.get("category") in ("small_molecule", "cofactor")
    ]
    if metabolites:
        parts.append("metabolites: " + ", ".join(dict.fromkeys(metabolites[:20])))

    processes = [
        str(p.get("label") or p.get("id"))
        for p in participants
        if isinstance(p, dict) and p.get("category") in ("biological_process", "cellular_component")
    ]
    if processes:
        parts.append("processes and locations: " + ", ".join(dict.fromkeys(processes[:10])))

    reactions = [
        str(r.get("label") or r.get("id"))
        for r in (record.get("reactions") or [])
        if isinstance(r, dict) and (r.get("label") or r.get("id"))
    ]
    if reactions:
        parts.append("reactions: " + "; ".join(dict.fromkeys(reactions[:12])))

    ground = [str(record.get("id"))]
    for xref in record.get("cross_references") or []:
        if isinstance(xref, dict):
            if xref.get("source_id"):
                ground.append(str(xref["source_id"]))
            if xref.get("target_id"):
                ground.append(str(xref["target_id"]))
    ground = list(dict.fromkeys(g for g in ground if g))[:12]
    parts.append("identifiers: " + ", ".join(ground))

    return ". ".join(p.rstrip().rstrip(".") for p in parts if p and p.strip())


def corpus_fingerprint(docs: list[str]) -> str:
    return hashlib.sha256("\x1f".join(docs).encode("utf-8")).hexdigest()[:16]


def load_corpus() -> tuple[list[str], list[str], list[dict]]:
    rows: list[tuple[Path, dict]] = []
    for path in sorted(CORPUS_DIR.glob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict) or not record.get("id"):
            continue
        rows.append((path, record))
    rows.sort(key=lambda item: str(item[1]["id"]))
    ids = [str(r["id"]) for _, r in rows]
    docs = [build_document(r) for _, r in rows]
    meta = []
    for path, r in rows:
        taxa_labels = [
            str(t.get("label") or t.get("id"))
            for t in (r.get("taxa") or [])
            if isinstance(t, dict) and (t.get("label") or t.get("id"))
        ]
        ptype = str(r.get("pathway_type") or "other-pathway")
        meta.append(
            {
                "id": str(r["id"]),
                "slug": path.stem,
                "href": f"records/{path.stem}.html",
                "label": str(r.get("label") or r["id"]),
                "pathway_type": ptype,
                "class": broad_pathway_class(ptype),
                "taxon": ", ".join(taxa_labels) if taxa_labels else "Unspecified",
            }
        )
    return ids, docs, meta


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--model", default="BAAI/bge-large-en-v1.5")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--device", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ids, docs, meta = load_corpus()
    if not ids:
        print("no records found under data/pathways/", file=sys.stderr)
        return 2
    if args.limit:
        ids, docs, meta = ids[: args.limit], docs[: args.limit], meta[: args.limit]

    if args.dry_run:
        print(f"{len(ids):,} records would be embedded with {args.model}\n")
        for i, d in zip(ids[:3], docs[:3], strict=True):
            print(f"--- {i} ---\n{d}\n")
        return 0

    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer

    device = args.device or (
        "mps"
        if torch.backends.mps.is_available()
        else "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )
    print(f"{len(ids):,} records -> embedding with {args.model} on {device}")
    model = SentenceTransformer(args.model, device=device)
    vectors = model.encode(
        docs,
        batch_size=args.batch,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    OUT.mkdir(parents=True, exist_ok=True)
    np.save(OUT / "vectors.f16.npy", vectors.astype(np.float16))
    (OUT / "ids.json").write_text(json.dumps(ids), encoding="utf-8")
    (OUT / "records.json").write_text(json.dumps(meta), encoding="utf-8")
    (OUT / "meta.json").write_text(
        json.dumps(
            {
                "model": args.model,
                "dim": int(vectors.shape[1]),
                "count": len(ids),
                "normalized": True,
                "excluded_fields": list(EXCLUDED),
                "corpus_fingerprint": corpus_fingerprint(docs),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(
        f"wrote {vectors.shape[0]:,} x {vectors.shape[1]} vectors to "
        f"{OUT.relative_to(REPO_ROOT)}/"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
