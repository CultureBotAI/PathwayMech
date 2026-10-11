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
    for source, metadata in data["sources"].items():
        _keys(
            metadata, {"url", "version", "sha256", "license"},
            {"sha256_scope"}, f"source {source}",
        )
        if any(not _text(value) for value in metadata.values()):
            raise ValueError(f"source {source}: provenance fields must be nonempty strings")
        url = urlparse(metadata["url"])
        if url.scheme not in {"http", "https"} or not url.netloc:
            raise ValueError(f"source {source}: expected a public source URL")
        if not re.fullmatch(r"[0-9a-f]{64}", metadata["sha256"]):
            raise ValueError(f"source {source}: invalid SHA-256")
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
            term, {"label", "synonyms", "source"}, {"label_kind"}, f"authority {identifier}"
        )
        if term.get("label_kind", "canonical") not in {"canonical", "source_context"}:
            raise ValueError(f"{identifier}: unknown authority label kind")
        if not _text(term["label"]):
            raise ValueError(f"{identifier}: authority label must be nonempty")
        if not isinstance(term["synonyms"], list) or any(
            not _text(value) for value in term["synonyms"]
        ):
            raise ValueError(f"{identifier}: authority synonyms must be a list of labels")
        if not isinstance(term["source"], str) or term["source"] not in data["sources"]:
            raise ValueError(f"{identifier}: missing source provenance")
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
