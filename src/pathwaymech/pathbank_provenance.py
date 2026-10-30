"""Closed provenance contract for independently acquired PathBank ZIP members."""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

PATHBANK_ARCHIVE_KIND = "pathbank-biopax-zip"
PATHBANK_ARCHIVE_URL = "https://pathbank.org/downloads/pathbank_primary_biopax.zip"
PATHBANK_ARCHIVE_DEFAULT_PATH = "pathbank-primary-biopax-original.zip"
PATHBANK_ARCHIVE_VERSION = (
    "2019-08-16 frozen primary BioPAX archive; acquisition retained by source ledger"
)
PATHBANK_ARCHIVE_LICENSE = "Upstream terms; public-release licensing deferred"


def validate_pathbank_archive(url: str, sha256: str, archive: Any) -> None:
    """Check typed bindings; the builder additionally verifies the original bytes."""
    if url != PATHBANK_ARCHIVE_URL:
        raise ValueError("PathBank ZIP requires the exact official archive URL")
    if not isinstance(sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", sha256):
        raise ValueError("PathBank ZIP requires an exact archive SHA-256")
    if not isinstance(archive, dict) or archive.keys() != {
        "bytes", "member", "member_bytes", "member_sha256", "root",
    }:
        raise ValueError("PathBank ZIP requires a closed archive provenance object")
    if any(type(archive[key]) is not int or archive[key] <= 0
           for key in ("bytes", "member_bytes")):
        raise ValueError("PathBank ZIP archive/member byte counts must be positive integers")
    patterns = {
        "member": r"PW[0-9]+\.owl",
        "member_sha256": r"[0-9a-f]{64}",
        "root": r"SMP[0-9]+",
    }
    if any(not isinstance(archive[key], str) or not re.fullmatch(pattern, archive[key])
           for key, pattern in patterns.items()):
        raise ValueError("PathBank ZIP requires exact native member, hash and root identities")


def _parse_validated_archive_member(
    archive_path: Path,
    member: str,
    root: str,
    *,
    key: str | None = None,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> tuple[dict[str, Any], ElementTree.Element, list[tuple[str, str, list[str]]]]:
    if not isinstance(member, str) or not re.fullmatch(r"PW[0-9]+\.owl", member):
        raise ValueError("PathBank ZIP requires an exact PW[0-9]+.owl member name")
    if not isinstance(root, str) or not re.fullmatch(r"SMP[0-9]+", root):
        raise ValueError("PathBank ZIP requires an exact SMP[0-9]+ root accession")
    if not isinstance(path, str) or not path.strip():
        raise ValueError("PathBank ZIP manifest path must be a non-empty string")
    relative_path = Path(path)
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(
            "PathBank ZIP manifest path must be a relative path without parent traversal"
        )
    if not isinstance(version, str) or not version.strip():
        raise ValueError("PathBank ZIP manifest version must be a non-empty string")
    if not isinstance(license, str) or not license.strip():
        raise ValueError("PathBank ZIP manifest license must be a non-empty string")
    archive_raw = Path(archive_path).read_bytes()
    archive_sha256 = hashlib.sha256(archive_raw).hexdigest()
    try:
        with zipfile.ZipFile(archive_path, "r") as zf:
            members = [info for info in zf.infolist() if info.filename == member]
            if not members:
                raise ValueError(f"PathBank ZIP archive missing member: {member}")
            if len(members) != 1 or members[0].is_dir():
                raise ValueError("PathBank ZIP requires one exact member")
            member_raw = zf.read(members[0])
    except zipfile.BadZipFile as exc:
        raise ValueError("PathBank ZIP requires a valid ZIP archive") from exc
    try:
        xml_root = ElementTree.fromstring(member_raw)
    except ElementTree.ParseError as exc:
        raise ValueError("PathBank ZIP member requires valid XML") from exc
    if xml_root.tag != "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF" or any(
        not node.tag.startswith("{http://www.biopax.org/release/biopax-level3.owl#}")
        and node.tag != "{http://www.w3.org/2002/07/owl#}Ontology"
        for node in xml_root
    ):
        raise ValueError("PathBank ZIP member requires native RDF/BioPAX object types")
    from pathwaymech.pathbank_context import pathbank_terms

    terms = list(pathbank_terms(xml_root, url=PATHBANK_ARCHIVE_URL, archive_root=root))
    archive = {
        "bytes": len(archive_raw),
        "member": member,
        "member_bytes": len(member_raw),
        "member_sha256": hashlib.sha256(member_raw).hexdigest(),
        "root": root,
    }
    validate_pathbank_archive(PATHBANK_ARCHIVE_URL, archive_sha256, archive)
    resolved_key = (
        key
        if key is not None
        else f"pathbank-primary-2019-{member.removesuffix('.owl')}-{root}"
    )
    if not isinstance(resolved_key, str) or not resolved_key.strip():
        raise ValueError("PathBank ZIP manifest key must be a non-empty string")
    manifest_entry = {
        "key": resolved_key,
        "kind": PATHBANK_ARCHIVE_KIND,
        "path": path,
        "url": PATHBANK_ARCHIVE_URL,
        "version": version,
        "license": license,
        "sha256": archive_sha256,
        "archive": archive,
    }
    return manifest_entry, xml_root, terms


def build_pathbank_archive_manifest_entry(
    archive_path: Path,
    member: str,
    root: str,
    *,
    key: str | None = None,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> dict[str, Any]:
    """Build and validate a closed PathBank primary BioPAX ZIP manifest entry."""
    manifest_entry, _, _ = _parse_validated_archive_member(
        archive_path,
        member,
        root,
        key=key,
        path=path,
        version=version,
        license=license,
    )
    return manifest_entry


def inspect_pathbank_archive_member(
    archive_path: Path,
    member: str,
    root: str,
    *,
    key: str | None = None,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> dict[str, Any]:
    """Validate a PathBank ZIP member and summarize its native terms and external xref CURIEs.

    External UnificationXref CURIEs (CHEBI, NCBITaxon, UniProtKB) are enumerated
    purely for pre-ingestion authority auditing against their respective issuing
    authorities; they are never used as identifier-label authorities by
    ``pathbank_terms``.
    """
    manifest_entry, xml_root, terms = _parse_validated_archive_member(
        archive_path,
        member,
        root,
        key=key,
        path=path,
        version=version,
        license=license,
    )
    bp = "{http://www.biopax.org/release/biopax-level3.owl#}"
    chebi_ids: set[str] = set()
    taxon_ids: set[str] = set()
    uniprot_ids: set[str] = set()
    for node in xml_root.findall(bp + "UnificationXref"):
        db = (node.findtext(bp + "db") or "").strip()
        ident = (node.findtext(bp + "id") or "").strip()
        if db == "ChEBI":
            match = re.fullmatch(r"(?:CHEBI:)?([0-9]+)", ident)
            if match:
                chebi_ids.add(f"CHEBI:{match[1]}")
        elif db == "TAXONOMY":
            match = re.fullmatch(r"(?:NCBITaxon:)?([0-9]+)", ident)
            if match:
                taxon_ids.add(f"NCBITaxon:{match[1]}")
        elif db == "UniProt":
            match = re.fullmatch(r"(?:UniProtKB:)?([A-Z0-9]{6,10})", ident)
            if match:
                uniprot_ids.add(f"UniProtKB:{match[1]}")
    return {
        "manifest_entry": manifest_entry,
        "pathway_id": terms[0][0],
        "pathway_label": terms[0][1],
        "native_term_ids": [term_id for term_id, _, _ in terms],
        "external_xrefs": {
            "CHEBI": sorted(chebi_ids),
            "NCBITaxon": sorted(taxon_ids),
            "UniProtKB": sorted(uniprot_ids),
        },
    }


def audit_pathbank_archive_member_authority(
    archive_path: Path,
    member: str,
    root: str,
    authority_snapshot_path: Path,
    *,
    key: str | None = None,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> dict[str, Any]:
    """Audit a PathBank ZIP member against a checked-in authority snapshot.

    Deterministically reports whether the member's manifest key is registered in
    ``sources`` and partitions its native ``PathBank:*`` terms and referenced
    external ``UnificationXref`` CURIEs (``CHEBI``, ``NCBITaxon``, ``UniProtKB``)
    into indexed vs. missing sets relative to ``terms`` in ``authority_snapshot_path``.
    """
    summary = inspect_pathbank_archive_member(
        archive_path,
        member,
        root,
        key=key,
        path=path,
        version=version,
        license=license,
    )
    try:
        snapshot = json.loads(Path(authority_snapshot_path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            "PathBank authority audit requires a valid JSON authority snapshot"
        ) from exc
    if (
        not isinstance(snapshot, dict)
        or not isinstance(snapshot.get("sources"), dict)
        or not isinstance(snapshot.get("terms"), dict)
    ):
        raise ValueError(
            "PathBank authority audit requires an authority snapshot "
            "with 'sources' and 'terms' mappings"
        )
    sources = snapshot["sources"]
    terms = snapshot["terms"]
    manifest_key = summary["manifest_entry"]["key"]
    manifest_key_registered = manifest_key in sources
    native_term_ids = summary["native_term_ids"]
    indexed_native_term_ids = [term_id for term_id in native_term_ids if term_id in terms]
    missing_native_term_ids = [term_id for term_id in native_term_ids if term_id not in terms]
    indexed_external_xrefs = {
        prefix: [curie for curie in curies if curie in terms]
        for prefix, curies in summary["external_xrefs"].items()
    }
    missing_external_xrefs = {
        prefix: [curie for curie in curies if curie not in terms]
        for prefix, curies in summary["external_xrefs"].items()
    }
    ready_for_check_identifiers = (
        manifest_key_registered
        and not missing_native_term_ids
        and all(not missing for missing in missing_external_xrefs.values())
    )
    return {
        **summary,
        "manifest_key_registered": manifest_key_registered,
        "indexed_native_term_ids": indexed_native_term_ids,
        "missing_native_term_ids": missing_native_term_ids,
        "indexed_external_xrefs": indexed_external_xrefs,
        "missing_external_xrefs": missing_external_xrefs,
        "ready_for_check_identifiers": ready_for_check_identifiers,
    }


def rank_pathbank_archive_member_candidates(
    archive_path: Path,
    candidates: list[tuple[str, str]] | tuple[tuple[str, str], ...],
    authority_snapshot_path: Path,
    *,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> list[dict[str, Any]]:
    """Audit and deterministically rank PathBank ZIP candidate members by authority readiness.

    Validates that ``candidates`` is a non-empty sequence of unique ``(member, root)``
    string pairs, audits each candidate against ``authority_snapshot_path``, attaches
    ``missing_external_xref_count`` and ``missing_native_term_count``, and returns the
    candidate audit dictionaries ordered from most ready (already ready for
    ``pathwaymech-check-identifiers``, then fewest missing external ``UnificationXref``
    CURIEs, then fewest missing native ``PathBank:*`` terms, then lexical ``member``
    and ``root``) to least ready.
    """
    if not isinstance(candidates, (list, tuple)) or not candidates:
        raise ValueError(
            "PathBank candidate ranking requires a non-empty sequence of (member, root) pairs"
        )
    seen_members: set[str] = set()
    seen_roots: set[str] = set()
    normalized_candidates: list[tuple[str, str]] = []
    for item in candidates:
        if (
            not isinstance(item, (list, tuple))
            or len(item) != 2
            or not isinstance(item[0], str)
            or not isinstance(item[1], str)
        ):
            raise ValueError(
                "PathBank candidate ranking requires 2-element (member, root) string pairs"
            )
        member, root = item[0], item[1]
        if member in seen_members:
            raise ValueError(f"PathBank candidate ranking duplicate member: {member}")
        if root in seen_roots:
            raise ValueError(f"PathBank candidate ranking duplicate root: {root}")
        seen_members.add(member)
        seen_roots.add(root)
        normalized_candidates.append((member, root))

    ranked: list[dict[str, Any]] = []
    for member, root in normalized_candidates:
        audit = audit_pathbank_archive_member_authority(
            archive_path,
            member,
            root,
            authority_snapshot_path,
            path=path,
            version=version,
            license=license,
        )
        missing_external_xref_count = sum(
            len(curies) for curies in audit["missing_external_xrefs"].values()
        )
        missing_native_term_count = len(audit["missing_native_term_ids"])
        ranked.append(
            {
                **audit,
                "missing_external_xref_count": missing_external_xref_count,
                "missing_native_term_count": missing_native_term_count,
            }
        )
    ranked.sort(
        key=lambda entry: (
            not entry["ready_for_check_identifiers"],
            entry["missing_external_xref_count"],
            entry["missing_native_term_count"],
            entry["manifest_entry"]["archive"]["member"],
            entry["manifest_entry"]["archive"]["root"],
        )
    )
    return ranked


