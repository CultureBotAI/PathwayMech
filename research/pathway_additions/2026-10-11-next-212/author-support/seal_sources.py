"""Seal original-source provenance for an external author draft."""

import hashlib
import importlib.util
import json
import re
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
OUT = ROOT / "draft"
SCOUT = Path("/private/tmp/pathwaymech-bacillibactin-scout-20261011")
REPO = Path("/private/tmp/pathwaymech-next-210-20261011")


def sha(p):
    with Path(p).open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def walk(x):
    if isinstance(x, dict):
        yield x
        for y in x.values():
            yield from walk(y)
    elif isinstance(x, list):
        for y in x:
            yield from walk(y)


receipts = {}
for base in [SCOUT, ROOT]:
    for p in base.rglob("*acquisition*.json"):
        for x in walk(json.loads(p.read_text())):
            path = (
                x.get("path")
                or x.get("original_path")
                or (str(p.parent / x["file"]) if x.get("file") else None)
            )
            status = x.get("status", x.get("http_status"))
            if path and x.get("url") and Path(path).is_file() and status == 200:
                receipts[path] = {
                    **x,
                    "status": status,
                    "retrieved_at": x.get("retrieved_at", x.get("finished_at")),
                }
record = yaml.safe_load((OUT / "bacillibactin-biosynthesis.yaml").read_text())
refpaths = json.loads((ROOT / "reference-paths.json").read_text())
paths = set(refpaths.values())
meta_ids = {record["id"]} | {
    x["id"]
    for k in ["participants", "reactions"]
    for x in record[k]
    if x["id"].startswith("MetaCyc:")
}
for cid in meta_ids:
    paths.add(str(ROOT / "originals" / (cid.split(":", 1)[1] + ".html")))
extra = [
    SCOUT / "followup/ena-AP025627.embl",
    SCOUT / "followup/Osaka-entry.html",
    SCOUT / "carrier-authority-followup/metanetx-release.html",
    SCOUT / "carrier-authority-followup/modelseed-compound_36.json",
    SCOUT / "carrier-authority-followup/modelseed-compound_36.provenance.tsv",
    SCOUT / "epmc-primary-metadata.json",
    SCOUT / "PMC1482855.html",
    SCOUT / "uniprot-P39135.json",
    ROOT / "originals/quickgo-bacillibactin.json",
]
extra.extend(
    SCOUT / (n + ".xml")
    for n in [
        "CPLX-7601",
        "CPLX-7602",
        "CPLX-7603",
        "CPLX-7604",
        "MONOMER-13911",
        "MONOMER-13919",
        "MONOMER-13920",
        "MONOMER-13921",
        "MONOMER-13922",
        "HOLO-ACP-SYNTH-RXN",
    ]
)
extra.append(SCOUT / "BGC0000309.json")
mibig = json.loads((ROOT / "mibig-member-replay.json").read_text())
assert sha(mibig["container_path"]) == mibig["container_sha256"]
paths.update(str(p) for p in extra)
originals = []
refs_by_path = {}
for ref in record["references"]:
    refs_by_path.setdefault(refpaths[ref["id"]], []).append(ref)
for p in sorted(paths):
    path = Path(p)
    assert path.is_file(), p
    source = receipts.get(p, {})
    member = p == mibig["member_path"]
    rs = refs_by_path.get(p, [])
    url = (mibig["container_url"] if member else source.get("url")) or (
        rs[0]["url"] if rs else None
    )
    if not url:
        raise ValueError("No acquisition URL for " + p)
    actual = sha(p)
    if source.get("sha256"):
        assert actual == source["sha256"], p
    originals.append(
        {
            "original_path": p,
            "url": url,
            "sha256": actual,
            "bytes": path.stat().st_size,
            "sha256_scope": "exact unmodified member of original MIBiG 4.0 tar archive"
            if member
            else "exact original retained response bytes"
            if path.suffix != ".db"
            else "complete original uncompressed Semantic SQL database",
            "retrieved_at": "Existing pinned archive; original retrieval time not claimed"
            if member
            else source.get("retrieved_at", "2026-10-11; exact time not claimed"),
            "status": source.get("status"),
            "content_type": source.get("content_type"),
            "reference_ids": [x["id"] for x in rs],
            **({"original_container": mibig} if member else {}),
        }
    )
# Canonical parser inspection never transcodes a malformed body to make it pass.
spec = importlib.util.spec_from_file_location(
    "authority", REPO / "scripts/build_source_identifier_snapshot.py"
)
auth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auth)
canonical = []
proposal = []
baseline = json.loads((REPO / "data/identifier_authorities/sources.json").read_text())["terms"]
for cid in sorted(meta_ids):
    frame = cid.split(":", 1)[1]
    p = ROOT / "originals" / (frame + ".html")
    raw = p.read_bytes()
    item = {"id": cid, "original_path": str(p), "sha256": sha(p)}
    try:
        terms = list(auth.metacyc_terms(raw.decode("utf-8")))
        assert len(terms) == 1 and terms[0][0] == cid
        item.update(status="current_canonical_parser_pass", label=terms[0][1])
    except UnicodeDecodeError as error:
        # Independent ASCII byte extraction is an inspection fact, not canonical gate success.
        m = re.search(rb"typeObjectPage\s*=\s*\{object:'([^']+)',orgid:'META'", raw)
        title = re.search(rb"<TITLE>MetaCyc (.*?)</TITLE>", raw, re.S | re.I)
        assert m and title and m[1].decode("ascii") == frame
        label = title[1].decode("ascii")
        item.update(
            status="pending_original_byte_decoder_fix",
            label=label,
            error=str(error),
            invalid_byte_positions=[i for i, b in enumerate(raw) if b == 0x96],
        )
    canonical.append(item)
    proposal.append(
        {
            "manifest_entry": {
                "key": "metacyc-" + frame.lower() + "-2026-10-11-bacillibactin",
                "kind": "metacyc-html",
                "path": "metacyc-" + frame + "-2026-10-11-bacillibactin.html",
                "url": receipts[str(p)]["url"],
                "version": "22.5; original retrieved 2026-10-11",
                "license": "BioCyc terms; public-release licensing review pending",
                "sha256": sha(p),
            },
            "original_path": str(p),
            "identifiers": [cid],
            "current_parser_status": item["status"],
            "already_present_in_reference_baseline": cid in baseline,
        }
    )
protein = SCOUT / "followup/ncbi-kh34-proteins.xml"
proposal.append(
    {
        "manifest_entry": {
            "key": "ncbi-kh34-bacillibactin-2026-10-11",
            "kind": "ncbi-protein-xml",
            "path": "ncbi-kh34-bacillibactin-2026-10-11.xml",
            "url": receipts[str(protein)]["url"],
            "version": "versioned NCBI GenPept records; 2026-10-11",
            "license": "NCBI source terms",
            "sha256": sha(protein),
        },
        "original_path": str(protein),
        "identifiers": [
            x["id"] for x in record["participants"] if x["id"].startswith("NCBIProtein:")
        ],
    }
)
mnx = SCOUT / "carrier-authority-followup/metanetx-MNXM743865.html"
proposal.append(
    {
        "manifest_entry": {
            "key": "metanetx-mnxm743865-bacillibactin-2026-10-11",
            "kind": "metanetx-chemical-html",
            "path": "metanetx-MNXM743865-2026-10-11.html",
            "url": "https://www.metanetx.org/chem_info/MNXM743865",
            "version": "MNXref production 4.5; original HTML retrieved 2026-10-11",
            "license": "MetaNetX source terms and upstream licensing; "
            "public-release review pending",
            "sha256": sha(mnx),
        },
        "original_path": str(mnx),
        "identifiers": ["metanetx.chemical:MNXM743865"],
        "current_parser_status": "pending independently reviewed implementation integration",
    }
)
manifest = {
    "created_at": datetime.now(UTC).isoformat(),
    "record_sha256": sha(OUT / "bacillibactin-biosynthesis.yaml"),
    "original_sources": originals,
    "reference_original_paths": refpaths,
    "response_metadata_policy": "No cookie, session, authorization or response headers retained; "
    "only URL/status/content type/retrieval time/exact-body digests.",
    "acquisition_receipt_paths": [str(p) for p in ROOT.glob("acquisition*.json")],
    "failed_attempts": [
        {"url": x["url"], "error": x.get("error"), "accepted": False}
        for p in ROOT.glob("acquisition*.json")
        for x in json.loads(p.read_text())
        if not x.get("accepted", False)
    ],
}
(OUT / "bacillibactin-source-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
(OUT / "bacillibactin-authority-inputs.json").write_text(
    json.dumps(
        {
            "record_sha256": manifest["record_sha256"],
            "proposed_original_source_inputs": proposal,
            "native_identity_inspection": canonical,
            "no_shared_snapshot_or_manifest_mutation": True,
        },
        indent=2,
    )
    + "\n"
)
print(
    json.dumps(
        {
            "sources": len(originals),
            "proposed_inputs": len(proposal),
            "pending_metacyc_decoder": [
                x["id"] for x in canonical if x["status"].startswith("pending")
            ],
        }
    )
)
