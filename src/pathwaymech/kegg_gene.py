"""Whole, singly requested KEGG bacterial CDS identities.

The native ENTRY locus labels a gene. NAME is retained functional annotation,
not a gene symbol. Sequence translation and experimental function are separate
scientific assertions; this profile verifies the issuing record and its shape.
"""

from __future__ import annotations

import hashlib
import json
import re
import stat
from pathlib import Path
from typing import Any

GENE_KIND = "kegg-gene-flatfile"
FIELD = "native_gene"
PROVENANCE = ("url", "version", "license", "sha256")
IDENTITY = r"([a-z][a-z0-9]{1,9}):([A-Za-z0-9][A-Za-z0-9_.-]*)"
REQUEST = rf"https://rest\.kegg\.jp/get/{IDENTITY}"
REQUIRED = {"ENTRY", "NAME", "ORGANISM", "POSITION", "AASEQ", "NTSEQ"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("KEGG gene: " + message)


def keys(value: Any, expected: set[str], message: str) -> None:
    require(isinstance(value, dict) and set(value) == expected, message)


def request(url: Any) -> tuple[str, str]:
    match = re.fullmatch(REQUEST, url) if isinstance(url, str) else None
    require(match is not None, "requires one exact official HTTPS organism:locus get request")
    return match[1], match[2]


def is_gene_id(identifier: Any) -> bool:
    return isinstance(identifier, str) and re.fullmatch("KEGG:" + IDENTITY, identifier) is not None


def project(raw: bytes, url: str) -> dict:
    organism, locus = request(url)
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError as error:
        raise ValueError("KEGG gene: original is not UTF-8") from error
    require(
        bool(text)
        and all(c == "\n" or (ord(c) >= 32 and not 127 <= ord(c) <= 159) for c in text)
        and not text.startswith("\ufeff"),
        "original contains a BOM or unsupported control character",
    )
    lines = text.split("\n")
    if lines[-1] == "":
        lines.pop()
    require(lines[-1] == "///" and "///" not in lines[:-1], "requires one complete terminated CDS")
    fields = []
    seen = set()
    current = None
    for line in lines[:-1]:
        require(len(line) > 12 and bool(line[12:].strip()), "empty or malformed field columns")
        column = line[:12]
        tag = column.strip()
        if not tag:
            require(current is not None, "orphan field continuation")
            current["lines"].append(line)
        elif column.startswith(" "):
            require(
                current is not None
                and current["tag"] == "REFERENCE"
                and column == "  " + tag + " " * (10 - len(tag))
                and tag in {"AUTHORS", "TITLE", "JOURNAL", "DOI"},
                "unsupported nested field",
            )
            current["lines"].append(line)
        else:
            require(
                re.fullmatch(r"[A-Z][A-Z0-9_]{0,10}", tag) is not None and column == tag.ljust(12),
                "malformed field header",
            )
            require(bool(fields) or tag == "ENTRY", "ENTRY must be first")
            require(tag not in seen or tag == "REFERENCE", "duplicate native field " + tag)
            seen.add(tag)
            current = {"tag": tag, "lines": [line]}
            fields.append(current)
    require(REQUIRED <= seen, "missing required native CDS fields")
    indexed = {field["tag"]: field["lines"] for field in fields}

    def single(tag: str) -> str:
        require(len(indexed[tag]) == 1, "continued identity field " + tag)
        return indexed[tag][0][12:]

    entry = re.fullmatch(r"([A-Za-z0-9][A-Za-z0-9_.-]*) +CDS +(T[0-9]{5})", single("ENTRY"))
    require(entry is not None and entry[1] == locus, "ENTRY locus/CDS/genome identity mismatch")
    org = re.fullmatch(r"([a-z][a-z0-9]{1,9}) +([^ ].*\S)", single("ORGANISM"))
    require(org is not None and org[1] == organism, "ORGANISM differs from requested organism")
    position = single("POSITION")
    match = re.fullmatch(r"(?:(complement)\()?([1-9][0-9]*)\.\.([1-9][0-9]*)(\))?", position)
    require(
        match is not None and bool(match[1]) == bool(match[4]) and int(match[2]) <= int(match[3]),
        "requires one complete forward or complement genomic span",
    )

    def sequence(tag: str, alphabet: str) -> dict:
        rows = indexed[tag]
        count = rows[0][12:]
        require(
            re.fullmatch(r"[1-9][0-9]*", count) is not None and len(rows) > 1,
            "invalid sequence count or missing sequence " + tag,
        )
        parts = []
        for line in rows[1:]:
            require(
                line[:12] == " " * 12 and re.fullmatch(alphabet + "+", line[12:]) is not None,
                "invalid sequence alphabet/columns " + tag,
            )
            parts.append(line[12:])
        value = "".join(parts)
        require(len(value) == int(count), "sequence length differs from count " + tag)
        return {"length": int(count), "sequence": value}

    aa = sequence("AASEQ", "[ACDEFGHIKLMNPQRSTVWY]")
    nt = sequence("NTSEQ", "[acgtACGT]")
    require(int(match[3]) - int(match[2]) + 1 == nt["length"], "POSITION span differs from NTSEQ")
    require(
        nt["length"] == 3 * (aa["length"] + 1), "complete CDS nucleotide/protein lengths disagree"
    )
    require(
        nt["sequence"][-3:].upper() in {"TAA", "TAG", "TGA"}, "complete CDS lacks terminal stop"
    )
    return {
        "id": "KEGG:" + organism + ":" + locus,
        "native_type": "CDS",
        "locus": locus,
        "organism_code": organism,
        "organism_name": org[2],
        "genome_id": entry[2],
        "name_annotation": [line[12:] for line in indexed["NAME"]],
        "position": {
            "native": position,
            "start": int(match[2]),
            "end": int(match[3]),
            "strand": "-" if match[1] else "+",
        },
        "aaseq": aa,
        "ntseq": nt,
        "fields": fields,
        "original_text": text,
    }


def validate_gene_metadata(metadata: Any) -> None:
    keys(metadata, set(PROVENANCE) | {"kind", FIELD}, "incomplete typed provenance")
    require(metadata["kind"] == GENE_KIND, "wrong source kind")
    require(
        all(isinstance(metadata[k], str) and bool(metadata[k].strip()) for k in PROVENANCE),
        "empty source provenance",
    )
    require(re.fullmatch(r"[0-9a-f]{64}", metadata["sha256"]) is not None, "invalid original hash")
    native = metadata[FIELD]
    require(
        isinstance(native, dict) and isinstance(native.get("original_text"), str),
        "missing whole original text",
    )
    try:
        raw = native["original_text"].encode("utf-8", errors="strict")
    except UnicodeError as error:
        raise ValueError("KEGG gene: retained original is not UTF-8") from error
    require(
        hashlib.sha256(raw).hexdigest() == metadata["sha256"], "retained original hash mismatch"
    )
    expected = project(raw, metadata["url"])
    require(
        json.dumps(native, sort_keys=True) == json.dumps(expected, sort_keys=True),
        "metadata differs from complete original projection",
    )


def gene_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(entry, set(PROVENANCE) | {"key", "kind", "path"}, "unsupported manifest fields")
    require(
        entry["kind"] == GENE_KIND and isinstance(entry["key"], str) and bool(entry["key"].strip()),
        "wrong manifest kind/key",
    )
    require(isinstance(entry["path"], str) and bool(entry["path"]), "missing original path")
    relative = Path(entry["path"])
    require(
        bool(relative.parts) and not relative.is_absolute() and ".." not in relative.parts,
        "requires relative original path without traversal",
    )
    path = cache_dir / relative
    require(stat.S_ISREG(path.stat().st_mode), "original must resolve to a regular file")
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == entry["sha256"], "original hash mismatch")
    result = {
        **{k: entry[k] for k in PROVENANCE},
        "kind": GENE_KIND,
        FIELD: project(raw, entry["url"]),
    }
    validate_gene_metadata(result)
    return result


def gene_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_gene_metadata(metadata)
    native = metadata[FIELD]
    return native["id"], {
        "label": native["locus"],
        "synonyms": [],
        "source": source,
        "entity_type": "native_gene",
        "label_kind": "canonical",
    }


def validate_gene_assertions(sources: dict) -> set[str]:
    """Check whole original claims before term selection, in either source order."""
    assertions = {}
    for metadata in sources.values():
        if metadata.get("kind") == GENE_KIND:
            validate_gene_metadata(metadata)
            native = metadata[FIELD]
            assertion = json.dumps(native, sort_keys=True), metadata["version"]
            previous = assertions.setdefault(native["id"], assertion)
            require(previous == assertion, "conflicting whole gene identity/context assertions")
        else:
            require(FIELD not in metadata, "native_gene metadata requires its source kind")
            url = metadata.get("url")
            require(
                not isinstance(url, str) or re.fullmatch(REQUEST, url) is None,
                "gene request requires the typed gene source kind",
            )
    return set(assertions)
