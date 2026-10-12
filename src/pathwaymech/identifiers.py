"""Resolve named pathway nodes against versioned, independently sourced authorities.

Snapshots make the enforcing command deterministic and offline. A new identifier
must be verified by a snapshot refresh; the corpus is never its own authority.
Contextual label policies change comparison only, never identifier existence.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from pathwaymech.biocyc_carrier import CARRIER_CLASS_KIND, class_term, validate_class_metadata
from pathwaymech.ecocyc_complex import (
    ECOCYC_COMPLEX_KIND,
    complex_term,
    validate_complex_metadata,
)
from pathwaymech.ecocyc_state import ECOCYC_STATE_KIND, state_term, validate_state_metadata
from pathwaymech.pathbank_provenance import PATHBANK_ARCHIVE_KIND, validate_pathbank_archive
from pathwaymech.schema import ALLOWED_CURIE_PREFIXES
from pathwaymech.yaml_io import load_yaml_file, pathway_files

SECTIONS = {"record", "taxa", "participants", "reactions"}
POLICIES = {"canonical", "canonical_or_synonym"}


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _keys(value: Any, required: set[str], optional: set[str], where: str) -> None:
    if not isinstance(value, dict):
        raise ValueError(f"{where}: expected a mapping")
    missing = required - value.keys()
    unknown = value.keys() - required - optional
    if missing or unknown:
        raise ValueError(f"{where}: missing keys {sorted(missing)}, unknown keys {sorted(unknown)}")


def _relative_file(root: Path, value: Any) -> Path:
    if not _text(value) or Path(value).is_absolute():
        raise ValueError("authority snapshot must be a relative repository path")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("authority snapshot must remain inside the repository")
    return path


def _load_policy(path: Path, root: Path) -> dict[str, Any]:
    cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    _keys(cfg, {"version", "namespaces", "contextual_labels"}, set(), "identifier policy")
    if type(cfg["version"]) is not int or cfg["version"] != 1:
        raise ValueError("unsupported identifier policy version")
    namespaces = cfg["namespaces"]
    if not isinstance(namespaces, dict) or not namespaces:
        raise ValueError("identifier policy must configure at least one namespace")
    for prefix, entry in namespaces.items():
        if prefix not in ALLOWED_CURIE_PREFIXES:
            raise ValueError(f"unknown configured namespace: {prefix}")
        _keys(entry, {"snapshot", "policy"}, set(), str(prefix))
        _relative_file(root, entry["snapshot"])
        if entry["policy"] not in POLICIES:
            raise ValueError(f"{prefix}: unknown label policy {entry['policy']!r}")
    if not isinstance(cfg["contextual_labels"], list):
        raise ValueError("contextual_labels must be a list")
    for rule in cfg["contextual_labels"]:
        _keys(rule, {"namespace", "sections", "record_prefixes", "reason"}, set(), "label rule")
        if rule["namespace"] not in namespaces:
            raise ValueError(f"label rule: unconfigured namespace {rule['namespace']!r}")
        for key, allowed in [("sections", SECTIONS), ("record_prefixes", namespaces.keys())]:
            values = rule[key]
            if (
                not isinstance(values, list)
                or not values
                or any(not isinstance(value, str) or value not in allowed for value in values)
            ):
                raise ValueError(f"label rule: invalid or empty {key}")
        if not _text(rule["reason"]):
            raise ValueError("label rule: a contextual label needs a documented reason")
    return cfg


def _load_authority(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    _keys(data, {"version", "sources", "terms"}, set(), str(path))
    if type(data["version"]) is not int or data["version"] != 1:
        raise ValueError(f"{path}: unsupported authority version")
    if not isinstance(data["sources"], dict) or not data["sources"]:
        raise ValueError(f"{path}: authority has no source provenance")
    native_reaction_requests: dict[str, str] = {}
    for source, metadata in data["sources"].items():
        _keys(
            metadata,
            {"url", "version", "sha256", "license"},
            {
                "sha256_scope",
                "kind",
                "archive",
                "pathway_accessions",
                "native_complex",
                "native_carrier_class",
                "native_protein_state",
                "counterpart",
            },
            f"source {source}",
        )
        if any(
            not _text(value)
            for name, value in metadata.items()
            if name
            not in {
                "archive",
                "pathway_accessions",
                "native_complex",
                "native_carrier_class",
                "native_protein_state",
                "counterpart",
            }
        ):
            raise ValueError(f"source {source}: provenance fields must be nonempty strings")
        url = urlparse(metadata["url"])
        if url.scheme not in {"http", "https"} or not url.netloc:
            raise ValueError(f"source {source}: expected a public source URL")
        if not re.fullmatch(r"[0-9a-f]{64}", metadata["sha256"]):
            raise ValueError(f"source {source}: invalid SHA-256")
        if "kind" in metadata and metadata["kind"] not in {
            "metacyc-reaction-xml",
            PATHBANK_ARCHIVE_KIND,
            ECOCYC_COMPLEX_KIND,
            CARRIER_CLASS_KIND,
            ECOCYC_STATE_KIND,
        }:
            raise ValueError(f"source {source}: unknown typed authority source kind")
        if metadata.get("kind") == PATHBANK_ARCHIVE_KIND:
            if set(metadata) != {
                "url",
                "version",
                "sha256",
                "license",
                "kind",
                "archive",
                "pathway_accessions",
            }:
                raise ValueError(f"source {source}: incomplete typed PathBank ZIP provenance")
            validate_pathbank_archive(metadata["url"], metadata["sha256"], metadata["archive"])
            accessions = metadata["pathway_accessions"]
            if (
                not isinstance(accessions, list)
                or not accessions
                or any(
                    not isinstance(value, str) or not re.fullmatch(r"SMP[0-9]+", value)
                    for value in accessions
                )
                or len(accessions) != len(set(accessions))
                or accessions[0] != metadata["archive"]["root"]
            ):
                raise ValueError(f"source {source}: invalid selected PathBank pathway identities")
        elif "archive" in metadata or "pathway_accessions" in metadata:
            raise ValueError(f"source {source}: archive provenance requires typed PathBank ZIP")
        if metadata.get("kind") == ECOCYC_COMPLEX_KIND:
            validate_complex_metadata(metadata)
        elif "native_complex" in metadata:
            raise ValueError(
                f"source {source}: native complex provenance requires its typed source kind"
            )
        if metadata.get("kind") == CARRIER_CLASS_KIND:
            validate_class_metadata(metadata)
        elif "native_carrier_class" in metadata:
            raise ValueError(
                f"source {source}: native class provenance requires its typed source kind"
            )
        if metadata.get("kind") == ECOCYC_STATE_KIND:
            validate_state_metadata(metadata)
        elif "native_protein_state" in metadata or "counterpart" in metadata:
            raise ValueError(
                f"source {source}: native state provenance requires its typed source kind"
            )
        if metadata.get("kind") == "metacyc-reaction-xml":
            request = re.fullmatch(
                r"https://bf2i-artsymbiocyc\.insa-lyon\.fr/getxml\?id=META:"
                r"([A-Za-z0-9][A-Za-z0-9_.-]*)",
                metadata["url"],
            )
            if request is None or not re.fullmatch(r"[0-9]+(?:\.[0-9]+)+", metadata["version"]):
                raise ValueError(
                    f"source {source}: invalid typed native reaction request or version"
                )
            # Check internal request/identity consistency. Original XML bytes
            # and their agreement with the request remain the builder's remit.
            native_reaction_requests[source] = "MetaCyc:" + request.group(1)
    if not isinstance(data["terms"], dict) or not data["terms"]:
        raise ValueError(f"{path}: authority has no terms; verification is unavailable")
    for identifier, term in data["terms"].items():
        if (
            not isinstance(identifier, str)
            or ":" not in identifier
            or identifier.split(":", 1)[0] not in ALLOWED_CURIE_PREFIXES
            or not identifier.split(":", 1)[1]
            or any(character.isspace() for character in identifier)
        ):
            raise ValueError(f"{path}: invalid authority identifier {identifier!r}")
        _keys(
            term,
            {"label", "synonyms", "source"},
            {"label_kind", "entity_type"},
            f"authority {identifier}",
        )
        if term.get("label_kind", "canonical") not in {
            "canonical",
            "source_context",
            "source_synonym",
        }:
            raise ValueError(f"{identifier}: unknown authority label kind")
        if not _text(term["label"]):
            raise ValueError(f"{identifier}: authority label must be nonempty")
        if not isinstance(term["synonyms"], list) or any(
            not _text(value) for value in term["synonyms"]
        ):
            raise ValueError(f"{identifier}: authority synonyms must be a list of labels")
        if not isinstance(term["source"], str) or term["source"] not in data["sources"]:
            raise ValueError(f"{identifier}: missing source provenance")
        source_kind = data["sources"][term["source"]].get("kind")
        if term.get("label_kind") == "source_synonym" and source_kind != ECOCYC_COMPLEX_KIND:
            raise ValueError(
                f"{identifier}: source-synonym authority requires a typed native complex"
            )
        if source_kind == PATHBANK_ARCHIVE_KIND:
            provenance = data["sources"][term["source"]]
            native = identifier.removeprefix("PathBank:")
            root, separator, local = native.partition("/")
            if (
                not identifier.startswith("PathBank:")
                or (not separator and root not in provenance["pathway_accessions"])
                or (
                    separator
                    and (
                        root != provenance["archive"]["root"]
                        or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._~/-]*", local)
                        or any(part in {".", "..", ""} for part in local.split("/"))
                    )
                )
                or term.get("label_kind", "canonical")
                != ("source_context" if separator else "canonical")
                or "entity_type" in term
            ):
                raise ValueError(f"{identifier}: invalid typed PathBank archive term scope")
        if source_kind == ECOCYC_COMPLEX_KIND:
            expected_id, expected_term = complex_term(
                data["sources"][term["source"]], term["source"]
            )
            if identifier != expected_id or term != expected_term:
                raise ValueError(f"{identifier}: invalid typed native complex authority")
        elif source_kind in {CARRIER_CLASS_KIND, ECOCYC_STATE_KIND}:
            projector = class_term if source_kind == CARRIER_CLASS_KIND else state_term
            expected_id, expected_term = projector(data["sources"][term["source"]], term["source"])
            if identifier != expected_id or term != expected_term:
                raise ValueError(f"{identifier}: invalid typed native carrier authority")
        elif "entity_type" in term or source_kind == "metacyc-reaction-xml":
            if (
                term.get("entity_type") != "reaction"
                or source_kind != "metacyc-reaction-xml"
                or native_reaction_requests.get(term["source"]) != identifier
                or not re.fullmatch(r"MetaCyc:[A-Za-z0-9][A-Za-z0-9_.-]*", identifier)
                or term.get("label_kind") != "source_context"
                or term["label"] != identifier.split(":", 1)[1]
                or term["synonyms"] != []
            ):
                raise ValueError(f"{identifier}: invalid typed native reaction authority")
    return data["terms"]


def _normalize(label: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", label).split()).casefold()


def _named_nodes(record: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    nodes = [("record", "record", record)]
    for section in ("taxa", "participants", "reactions"):
        if not isinstance(record.get(section), list):
            raise ValueError(f"{section}: required named-node list is missing or invalid")
        for index, node in enumerate(record[section]):
            if not isinstance(node, dict):
                raise ValueError(f"{section}[{index}]: expected a named node")
            nodes.append((section, f"{section}[{index}]", node))
    return nodes


def identifier_errors(root: Path, config_path: Path | None = None) -> list[str]:
    """Check the same recursive corpus as QC, failing closed on unavailable evidence."""
    root = root.resolve()
    config_path = config_path or root / "conf" / "identifier_policy.yaml"
    try:
        cfg = _load_policy(config_path, root)
    except (OSError, ValueError, TypeError, yaml.YAMLError) as error:
        return [f"identifier policy unavailable or invalid: {error}"]

    paths = pathway_files(root / "data" / "pathways")
    if not paths:
        return ["identifier gate: empty corpus; no pathway records selected"]

    authorities: dict[Path, dict[str, Any]] = {}
    try:
        for entry in cfg["namespaces"].values():
            path = _relative_file(root, entry["snapshot"])
            if path not in authorities:
                authorities[path] = _load_authority(path)
        for prefix, entry in cfg["namespaces"].items():
            terms = authorities[_relative_file(root, entry["snapshot"])]
            if not any(identifier.startswith(f"{prefix}:") for identifier in terms):
                raise ValueError(f"{prefix}: configured authority contains no identifiers")
    except (OSError, ValueError, TypeError) as error:
        return [f"identifier authority unavailable or invalid: {error}"]

    errors = []
    for path in paths:
        shown = path.relative_to(root)
        try:
            record = load_yaml_file(path)
            nodes = _named_nodes(record)
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"{shown}: {error}")
            continue
        record_prefix = str(record.get("id", "")).partition(":")[0]
        for section, locator, node in nodes:
            identifier, label = node.get("id"), node.get("label")
            where = f"{shown}:{locator}"
            if not _text(identifier) or not _text(label):
                errors.append(f"{where}: nonempty identifier and label required")
                continue
            prefix, _, _ = identifier.partition(":")
            entry = cfg["namespaces"].get(prefix)
            if entry is None:
                errors.append(f"{where}: UNKNOWN_NAMESPACE {identifier!r}; configure an authority")
                continue
            terms = authorities[_relative_file(root, entry["snapshot"])]
            term = terms.get(identifier)
            if term is None:
                errors.append(
                    f"{where}: ID_NOT_FOUND {identifier!r} in the verified authority snapshot; "
                    "resolve against the source before refreshing the snapshot"
                )
                continue
            # Native Reaction identity is not a pathway/protein/chemical
            # authority, even where the namespace permits contextual labels.
            if term.get("entity_type") == "reaction" and (
                section != "reactions" or node.get("category") != "molecular_activity"
            ):
                errors.append(
                    f"{where}: ENTITY_TYPE_MISMATCH {identifier!r}; "
                    "typed native reaction requires reactions/category molecular_activity"
                )
                continue
            if term.get("entity_type") == "protein_complex":
                if section != "participants" or node.get("category") != "complex":
                    errors.append(
                        f"{where}: ENTITY_TYPE_MISMATCH {identifier!r}; "
                        "typed native complex requires participants/category complex"
                    )
                elif (
                    term["label_kind"] == "source_synonym"
                    and entry["policy"] != "canonical_or_synonym"
                ):
                    errors.append(
                        f"{where}: LABEL_AUTHORITY_UNAVAILABLE {identifier!r}; "
                        "native source supplies a synonym, not a common-name"
                    )
                elif _normalize(label) != _normalize(term["label"]):
                    errors.append(
                        f"{where}: LABEL_MISMATCH {identifier!r}: {label!r}; "
                        f"typed source display is {term['label']!r}"
                    )
                # No broad contextual-label rule may invent names for this
                # bounded unnamed/synonym-only authority representation.
                continue
            carrier_category = {
                "protein_class": "protein",
                "chemical_class": "chemical_entity",
                "protein_state": "protein",
            }.get(term.get("entity_type"))
            if carrier_category is not None:
                if section != "participants" or node.get("category") != carrier_category:
                    errors.append(
                        f"{where}: ENTITY_TYPE_MISMATCH {identifier!r}; "
                        f"typed native carrier requires participants/category {carrier_category}"
                    )
                else:
                    labels = [term["label"]]
                    if entry["policy"] == "canonical_or_synonym":
                        labels += term["synonyms"]
                    if _normalize(label) not in {_normalize(value) for value in labels}:
                        errors.append(
                            f"{where}: LABEL_MISMATCH {identifier!r}: {label!r}; "
                            f"authority label is {term['label']!r}"
                        )
                # A generic namespace rule cannot erase class/state scope or
                # manufacture a name for these explicitly typed identities.
                continue
            contextual = any(
                rule["namespace"] == prefix
                and section in rule["sections"]
                and record_prefix in rule["record_prefixes"]
                for rule in cfg["contextual_labels"]
            )
            if contextual:
                continue
            if term.get("label_kind", "canonical") != "canonical":
                errors.append(
                    f"{where}: LABEL_AUTHORITY_UNAVAILABLE {identifier!r}; "
                    "source cross-reference text is not a canonical label authority"
                )
                continue
            labels = [term["label"]]
            if entry["policy"] == "canonical_or_synonym":
                labels += term["synonyms"]
            if _normalize(label) not in {_normalize(value) for value in labels}:
                errors.append(
                    f"{where}: LABEL_MISMATCH {identifier!r}: {label!r}; "
                    f"authority label is {term['label']!r}"
                )
    return errors
