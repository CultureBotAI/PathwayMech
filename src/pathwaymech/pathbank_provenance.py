"""Closed provenance contract for independently acquired PathBank ZIP members."""

from __future__ import annotations

import copy
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


def _load_validated_authority_snapshot(
    authority_snapshot_path: Path,
) -> dict[str, Any]:
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
    return snapshot


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
    snapshot = _load_validated_authority_snapshot(authority_snapshot_path)
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


def _validate_candidate_selection_filters(
    excluded_pathway_ids: set[str] | frozenset[str] | list[str] | tuple[str, ...],
    require_unregistered_manifest: bool,
) -> set[str]:
    if not isinstance(require_unregistered_manifest, bool):
        raise ValueError(
            "PathBank candidate selection requires a boolean "
            "require_unregistered_manifest flag"
        )
    if not isinstance(excluded_pathway_ids, (set, frozenset, list, tuple)):
        raise ValueError(
            "PathBank candidate selection requires excluded_pathway_ids to be "
            "a collection of PathBank:SMP[0-9]+ CURIEs"
        )
    excluded: set[str] = set()
    for pathway_id in excluded_pathway_ids:
        if not isinstance(pathway_id, str) or not re.fullmatch(
            r"PathBank:SMP[0-9]+", pathway_id
        ):
            raise ValueError(
                "PathBank candidate selection requires excluded_pathway_ids "
                "entries to match PathBank:SMP[0-9]+"
            )
        excluded.add(pathway_id)
    return excluded


def select_next_pathbank_archive_candidate(
    archive_path: Path,
    candidates: list[tuple[str, str]] | tuple[tuple[str, str], ...],
    authority_snapshot_path: Path,
    *,
    excluded_pathway_ids: set[str] | frozenset[str] | list[str] | tuple[str, ...] = (),
    require_unregistered_manifest: bool = True,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> dict[str, Any] | None:
    """Select the highest-readiness uncurated PathBank ZIP candidate slice.

    Validates ``excluded_pathway_ids`` (each entry must be an exact
    ``PathBank:SMP[0-9]+`` CURIE) and ``require_unregistered_manifest``, ranks
    ``candidates`` with :func:`rank_pathbank_archive_member_candidates`, filters out
    candidates whose ``pathway_id`` is in ``excluded_pathway_ids`` or (when
    ``require_unregistered_manifest`` is ``True``) whose ``manifest_key_registered``
    is ``True``, and returns the first remaining candidate audit dictionary (or
    ``None`` when no eligible candidate remains).
    """
    excluded = _validate_candidate_selection_filters(
        excluded_pathway_ids, require_unregistered_manifest
    )
    ranked = rank_pathbank_archive_member_candidates(
        archive_path,
        candidates,
        authority_snapshot_path,
        path=path,
        version=version,
        license=license,
    )
    for entry in ranked:
        if entry["pathway_id"] in excluded:
            continue
        if require_unregistered_manifest and entry["manifest_key_registered"]:
            continue
        return entry
    return None


def summarize_pathbank_archive_candidate_frontier(
    archive_path: Path,
    candidates: list[tuple[str, str]] | tuple[tuple[str, str], ...],
    authority_snapshot_path: Path,
    *,
    excluded_pathway_ids: set[str] | frozenset[str] | list[str] | tuple[str, ...] = (),
    require_unregistered_manifest: bool = True,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> dict[str, Any]:
    """Summarize the PathBank ZIP candidate frontier and aggregated missing external CURIEs.

    Ranks ``candidates`` with :func:`rank_pathbank_archive_member_candidates`,
    identifies already-registered pathway IDs and excluded pathway IDs, filters the
    remaining eligible candidate slices, and computes the sorted deduplicated union of
    missing external ``UnificationXref`` CURIEs (``CHEBI``, ``NCBITaxon``,
    ``UniProtKB``) across the remaining candidate frontier.
    """
    excluded = _validate_candidate_selection_filters(
        excluded_pathway_ids, require_unregistered_manifest
    )
    ranked = rank_pathbank_archive_member_candidates(
        archive_path,
        candidates,
        authority_snapshot_path,
        path=path,
        version=version,
        license=license,
    )
    registered_pathway_ids = [
        entry["pathway_id"] for entry in ranked if entry["manifest_key_registered"]
    ]
    remaining_candidates: list[dict[str, Any]] = []
    missing_union: dict[str, set[str]] = {
        "CHEBI": set(),
        "NCBITaxon": set(),
        "UniProtKB": set(),
    }
    for entry in ranked:
        if entry["pathway_id"] in excluded:
            continue
        if require_unregistered_manifest and entry["manifest_key_registered"]:
            continue
        remaining_candidates.append(entry)
        for prefix, curies in entry["missing_external_xrefs"].items():
            missing_union.setdefault(prefix, set()).update(curies)
    return {
        "total_candidates": len(ranked),
        "registered_count": len(registered_pathway_ids),
        "registered_pathway_ids": registered_pathway_ids,
        "excluded_pathway_ids": sorted(excluded),
        "remaining_count": len(remaining_candidates),
        "next_candidate": remaining_candidates[0] if remaining_candidates else None,
        "remaining_candidates": remaining_candidates,
        "missing_external_xrefs_union": {
            prefix: sorted(curies) for prefix, curies in missing_union.items()
        },
    }


def _load_validated_manifest_entries(manifest_path: Path) -> list[dict[str, Any]]:
    try:
        raw_entries = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            "PathBank manifest registration plan requires a valid JSON manifest file"
        ) from exc
    if not isinstance(raw_entries, list):
        raise ValueError(
            "PathBank manifest registration plan requires a JSON list of source entries"
        )
    seen_keys: set[str] = set()
    seen_archive_pairs: set[tuple[str, str]] = set()
    validated: list[dict[str, Any]] = []
    for entry in raw_entries:
        if not isinstance(entry, dict):
            raise ValueError(
                "PathBank manifest registration plan requires object source entries"
            )
        entry_key = entry.get("key")
        if not isinstance(entry_key, str) or not entry_key.strip():
            raise ValueError(
                "PathBank manifest registration plan requires non-empty string keys"
            )
        if entry_key in seen_keys:
            raise ValueError(
                f"PathBank manifest registration plan duplicate key: {entry_key}"
            )
        seen_keys.add(entry_key)
        if entry.get("kind") == PATHBANK_ARCHIVE_KIND:
            validate_pathbank_archive(
                entry.get("url"), entry.get("sha256"), entry.get("archive")
            )
            archive = entry["archive"]
            pair = (archive["member"], archive["root"])
            if pair in seen_archive_pairs:
                raise ValueError(
                    "PathBank manifest registration plan duplicate archive "
                    f"(member, root): {pair[0]} / {pair[1]}"
                )
            seen_archive_pairs.add(pair)
        validated.append(copy.deepcopy(entry))
    return validated


def plan_next_pathbank_archive_candidate_registration(
    archive_path: Path,
    candidates: list[tuple[str, str]] | tuple[tuple[str, str], ...],
    authority_snapshot_path: Path,
    manifest_path: Path,
    *,
    excluded_pathway_ids: set[str] | frozenset[str] | list[str] | tuple[str, ...] = (),
    require_unregistered_manifest: bool = True,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
) -> dict[str, Any]:
    """Build a deterministic manifest-and-authority registration plan for the next slice.

    Validates ``manifest_path`` (``conf/identifier_sources.json``), summarizes the
    candidate frontier against ``authority_snapshot_path``
    (``data/identifier_authorities/sources.json``), verifies that the selected
    candidate's manifest entry does not conflict with existing manifest entries, and
    returns the selected candidate, its closed ``pathbank-biopax-zip`` manifest entry,
    required missing native/external CURIEs, and the updated manifest entry list.
    """
    manifest_entries = _load_validated_manifest_entries(manifest_path)
    frontier = summarize_pathbank_archive_candidate_frontier(
        archive_path,
        candidates,
        authority_snapshot_path,
        excluded_pathway_ids=excluded_pathway_ids,
        require_unregistered_manifest=require_unregistered_manifest,
        path=path,
        version=version,
        license=license,
    )
    selected = frontier["next_candidate"]
    if selected is None:
        return {
            "frontier": frontier,
            "selected_candidate": None,
            "manifest_entry": None,
            "manifest_already_present": False,
            "required_native_term_ids": [],
            "required_external_xrefs": {
                "CHEBI": [],
                "NCBITaxon": [],
                "UniProtKB": [],
            },
            "updated_manifest_entries": manifest_entries,
        }

    manifest_entry = copy.deepcopy(selected["manifest_entry"])
    target_key = manifest_entry["key"]
    target_pair = (
        manifest_entry["archive"]["member"],
        manifest_entry["archive"]["root"],
    )
    manifest_already_present = False
    for existing in manifest_entries:
        existing_key = existing["key"]
        existing_pair = None
        if existing.get("kind") == PATHBANK_ARCHIVE_KIND:
            existing_archive = existing["archive"]
            existing_pair = (existing_archive["member"], existing_archive["root"])
        if existing_key == target_key or existing_pair == target_pair:
            if existing != manifest_entry:
                raise ValueError(
                    "PathBank manifest registration plan conflicts with existing "
                    f"manifest entry for {target_key}"
                )
            if require_unregistered_manifest:
                raise ValueError(
                    "PathBank manifest registration plan found manifest key already "
                    f"present in manifest file while unregistered in snapshot: {target_key}"
                )
            manifest_already_present = True
            break

    updated_manifest_entries = (
        manifest_entries
        if manifest_already_present
        else [*manifest_entries, copy.deepcopy(manifest_entry)]
    )
    return {
        "frontier": frontier,
        "selected_candidate": selected,
        "manifest_entry": manifest_entry,
        "manifest_already_present": manifest_already_present,
        "required_native_term_ids": list(selected["missing_native_term_ids"]),
        "required_external_xrefs": {
            prefix: list(curies)
            for prefix, curies in selected["missing_external_xrefs"].items()
        },
        "updated_manifest_entries": updated_manifest_entries,
    }


def audit_pathbank_manifest_snapshot_sync(
    manifest_path: Path,
    authority_snapshot_path: Path,
) -> dict[str, Any]:
    """Audit PathBank ZIP provenance synchronization between manifest and authority snapshot.

    Validates ``manifest_path`` (``conf/identifier_sources.json``) and
    ``authority_snapshot_path`` (``data/identifier_authorities/sources.json``),
    verifies closed ``pathbank-biopax-zip`` provenance invariants on both sides,
    rejects conflicting keys or ``(member, root)`` pairs, and partitions
    ``pathbank-biopax-zip`` keys into ``synchronized_keys``,
    ``pending_snapshot_keys``, and ``orphan_snapshot_keys``.
    """
    manifest_entries = _load_validated_manifest_entries(manifest_path)
    snapshot = _load_validated_authority_snapshot(authority_snapshot_path)
    sources = snapshot["sources"]

    manifest_archive_by_key: dict[str, dict[str, Any]] = {}
    manifest_key_by_pair: dict[tuple[str, str], str] = {}
    for entry in manifest_entries:
        if entry.get("kind") != PATHBANK_ARCHIVE_KIND:
            continue
        if entry.keys() != {
            "key",
            "kind",
            "path",
            "url",
            "version",
            "license",
            "sha256",
            "archive",
        }:
            raise ValueError(
                "PathBank manifest-snapshot sync requires closed manifest entry fields "
                f"for {entry['key']}"
            )
        pair = (entry["archive"]["member"], entry["archive"]["root"])
        manifest_archive_by_key[entry["key"]] = entry
        manifest_key_by_pair[pair] = entry["key"]

    snapshot_archive_by_key: dict[str, dict[str, Any]] = {}
    seen_snapshot_pairs: set[tuple[str, str]] = set()
    for key, meta in sources.items():
        if not isinstance(meta, dict):
            raise ValueError(
                f"PathBank manifest-snapshot sync requires object snapshot source for {key}"
            )
        if key in manifest_archive_by_key and meta.get("kind") != PATHBANK_ARCHIVE_KIND:
            raise ValueError(
                f"PathBank manifest-snapshot sync kind mismatch for {key}"
            )
        if meta.get("kind") != PATHBANK_ARCHIVE_KIND:
            continue
        validate_pathbank_archive(
            meta.get("url"), meta.get("sha256"), meta.get("archive")
        )
        accessions = meta.get("pathway_accessions")
        if (
            not isinstance(accessions, list)
            or not accessions
            or any(
                not isinstance(acc, str) or not re.fullmatch(r"SMP[0-9]+", acc)
                for acc in accessions
            )
            or len(set(accessions)) != len(accessions)
            or accessions[0] != meta["archive"]["root"]
        ):
            raise ValueError(
                "PathBank manifest-snapshot sync requires valid pathway_accessions "
                f"headed by archive root for {key}"
            )
        pair = (meta["archive"]["member"], meta["archive"]["root"])
        if pair in seen_snapshot_pairs:
            raise ValueError(
                "PathBank manifest-snapshot sync duplicate snapshot archive "
                f"(member, root): {pair[0]} / {pair[1]}"
            )
        seen_snapshot_pairs.add(pair)
        if pair in manifest_key_by_pair and manifest_key_by_pair[pair] != key:
            raise ValueError(
                "PathBank manifest-snapshot sync conflicting archive "
                f"(member, root) key for {pair[0]} / {pair[1]}"
            )
        snapshot_archive_by_key[key] = meta

    synchronized_keys: list[str] = []
    pending_snapshot_keys: list[str] = []
    shared_fields = ("kind", "url", "version", "license", "sha256", "archive")
    for key, manifest_entry in manifest_archive_by_key.items():
        snapshot_meta = snapshot_archive_by_key.get(key)
        if snapshot_meta is None:
            pending_snapshot_keys.append(key)
            continue
        if any(manifest_entry.get(field) != snapshot_meta.get(field) for field in shared_fields):
            raise ValueError(
                f"PathBank manifest-snapshot sync provenance mismatch for {key}"
            )
        synchronized_keys.append(key)

    orphan_snapshot_keys = sorted(
        key for key in snapshot_archive_by_key if key not in manifest_archive_by_key
    )
    return {
        "manifest_archive_count": len(manifest_archive_by_key),
        "snapshot_archive_count": len(snapshot_archive_by_key),
        "manifest_archive_keys": list(manifest_archive_by_key),
        "snapshot_archive_keys": sorted(snapshot_archive_by_key),
        "synchronized_keys": synchronized_keys,
        "pending_snapshot_keys": pending_snapshot_keys,
        "orphan_snapshot_keys": orphan_snapshot_keys,
        "in_sync": not pending_snapshot_keys and not orphan_snapshot_keys,
    }


def verify_pathbank_archive_candidate_post_registration(
    archive_path: Path,
    member: str,
    root: str,
    manifest_path: Path,
    authority_snapshot_path: Path,
    *,
    key: str | None = None,
    path: str = PATHBANK_ARCHIVE_DEFAULT_PATH,
    version: str = PATHBANK_ARCHIVE_VERSION,
    license: str = PATHBANK_ARCHIVE_LICENSE,
    require_corpus_slice_verified: bool = False,
    require_fully_verified: bool = False,
) -> dict[str, Any]:
    """Verify post-registration readiness and manifest-snapshot sync for a PathBank ZIP member.

    Validates ``manifest_path`` (``conf/identifier_sources.json``),
    ``authority_snapshot_path`` (``data/identifier_authorities/sources.json``),
    and the ``(member, root)`` BioPAX entry in ``archive_path``. Confirms whether
    the computed closed ``manifest_entry`` is present in ``manifest_path`` without
    provenance drift, whether ``manifest_path`` and ``authority_snapshot_path``
    are synchronized on ``manifest_key``, whether the ``sources.json``-scoped
    corpus slice invariants hold (``pathway_id_indexed`` and
    ``uniprot_xrefs_indexed``), and whether all native ``PathBank:*`` terms and
    external ``CHEBI`` / ``NCBITaxon`` / ``UniProtKB`` ``UnificationXref`` CURIEs
    are indexed in ``authority_snapshot_path``.
    """
    if not isinstance(require_corpus_slice_verified, bool):
        raise ValueError(
            "PathBank post-registration verification require_corpus_slice_verified must be a bool"
        )
    if not isinstance(require_fully_verified, bool):
        raise ValueError(
            "PathBank post-registration verification require_fully_verified must be a bool"
        )
    member_audit = audit_pathbank_archive_member_authority(
        archive_path,
        member,
        root,
        authority_snapshot_path,
        key=key,
        path=path,
        version=version,
        license=license,
    )
    sync_audit = audit_pathbank_manifest_snapshot_sync(
        manifest_path,
        authority_snapshot_path,
    )
    manifest_entries = _load_validated_manifest_entries(manifest_path)
    snapshot = _load_validated_authority_snapshot(authority_snapshot_path)
    manifest_entry = member_audit["manifest_entry"]
    target_key = manifest_entry["key"]
    target_pair = (
        manifest_entry["archive"]["member"],
        manifest_entry["archive"]["root"],
    )

    manifest_registered = False
    for existing in manifest_entries:
        existing_pair = (
            (existing["archive"]["member"], existing["archive"]["root"])
            if existing.get("kind") == PATHBANK_ARCHIVE_KIND
            else None
        )
        if existing["key"] == target_key or existing_pair == target_pair:
            if existing != manifest_entry:
                raise ValueError(
                    "PathBank post-registration verification conflicts with manifest "
                    f"entry for {target_key}"
                )
            manifest_registered = True
            break

    snapshot_registered = bool(member_audit["manifest_key_registered"])
    shared_fields = ("kind", "url", "version", "license", "sha256", "archive")
    if snapshot_registered:
        snapshot_meta = snapshot["sources"].get(target_key)
        if not isinstance(snapshot_meta, dict) or any(
            manifest_entry.get(field) != snapshot_meta.get(field)
            for field in shared_fields
        ):
            raise ValueError(
                "PathBank post-registration verification conflicts with snapshot "
                f"source for {target_key}"
            )

    manifest_synchronized = (
        manifest_registered
        and snapshot_registered
        and target_key in sync_audit["synchronized_keys"]
    )
    pathway_id_indexed = (
        member_audit["pathway_id"] in member_audit["indexed_native_term_ids"]
    )
    uniprot_xrefs_indexed = not member_audit["missing_external_xrefs"]["UniProtKB"]
    ready_for_check_identifiers = bool(member_audit["ready_for_check_identifiers"])
    corpus_slice_verified = bool(
        manifest_synchronized
        and sync_audit["in_sync"]
        and pathway_id_indexed
        and uniprot_xrefs_indexed
    )
    fully_verified = bool(
        manifest_synchronized
        and sync_audit["in_sync"]
        and ready_for_check_identifiers
    )
    if require_corpus_slice_verified and not corpus_slice_verified:
        raise ValueError(
            f"PathBank candidate {target_key} is not corpus-slice verified post-registration"
        )
    if require_fully_verified and not fully_verified:
        raise ValueError(
            f"PathBank candidate {target_key} is not fully verified post-registration"
        )
    return {
        "manifest_key": target_key,
        "pathway_id": member_audit["pathway_id"],
        "pathway_label": member_audit["pathway_label"],
        "manifest_entry": copy.deepcopy(manifest_entry),
        "manifest_registered": manifest_registered,
        "snapshot_registered": snapshot_registered,
        "manifest_synchronized": manifest_synchronized,
        "pathway_id_indexed": pathway_id_indexed,
        "uniprot_xrefs_indexed": uniprot_xrefs_indexed,
        "ready_for_check_identifiers": ready_for_check_identifiers,
        "corpus_slice_verified": corpus_slice_verified,
        "fully_verified": fully_verified,
        "member_audit": member_audit,
        "sync_audit": sync_audit,
    }
