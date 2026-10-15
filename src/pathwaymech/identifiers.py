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

from pathwaymech.biocyc_aceto import (
    ACETO_KINDS,
    RESIDUE_KIND,
    SGD_KIND,
    aceto_term,
    validate_aceto_assertions,
    validate_aceto_metadata,
)
from pathwaymech.biocyc_carrier import CARRIER_CLASS_KIND, class_term, validate_class_metadata
from pathwaymech.biocyc_chemical_class import (
    CHEMICAL_CLASS_KIND,
    chemical_class_term,
    validate_chemical_class_metadata,
)
from pathwaymech.biocyc_electron_transfer import (
    ELECTRON_TRANSFER_KIND,
    reaction_term,
    validate_reaction_metadata,
)
from pathwaymech.biocyc_pathway import PATHWAY_KIND, pathway_term, validate_pathway_metadata
from pathwaymech.biocyc_protein_carrier_reaction import (
    PROTEIN_CARRIER_REACTION_KIND,
    carrier_reaction_term,
    validate_carrier_reaction_assertions,
    validate_carrier_reaction_metadata,
)
from pathwaymech.ecocyc_complex import (
    ECOCYC_COMPLEX_KIND,
    complex_term,
    validate_complex_metadata,
)
from pathwaymech.ecocyc_named_complex import (
    NAMED_COMPLEX_KIND,
    named_complex_term,
    validate_named_complex_graph,
    validate_named_complex_metadata,
)
from pathwaymech.ecocyc_state import ECOCYC_STATE_KIND, state_term, validate_state_metadata
from pathwaymech.kegg_gene import (
    GENE_KIND,
    GENE_KINDS,
    PSEUDOGENE_KIND,
    gene_term,
    is_gene_id,
    validate_gene_assertions,
    validate_gene_metadata,
)
from pathwaymech.pathbank_context import (
    PATHBANK_CONTEXT_KIND,
    context_term,
    validate_context_assertions,
    validate_context_metadata,
)
from pathwaymech.pathbank_provenance import PATHBANK_ARCHIVE_KIND, validate_pathbank_archive
from pathwaymech.rhea_polymer import RHEA_POLYMER_KIND, polymer_term, validate_polymer_metadata
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
        _keys(
            rule, {"namespace", "sections", "record_prefixes", "reason"},
            {"authority_entity_types"}, "label rule",
        )
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
        if "authority_entity_types" in rule:
            types = rule["authority_entity_types"]
            if (
                not isinstance(types, list)
                or not types
                or any(not isinstance(value, str) or value != "reaction" for value in types)
            ):
                raise ValueError("label rule: invalid or empty authority_entity_types")
    return cfg


def _native_assertion_kinds(
    sources: dict[str, Any], reaction_requests: dict[str, str]
) -> dict[str, str]:
    """Bind every retained native identity before selected terms choose an owner.

    Compare the same projections as the producer, including state counterparts
    and all retained Polymer members. Aceto companion/provenance compatibility
    remains with its specialized validator rather than a reduced projection.
    """
    fields = {
        CARRIER_CLASS_KIND: "native_carrier_class",
        ECOCYC_STATE_KIND: "native_protein_state",
        ECOCYC_COMPLEX_KIND: "native_complex",
        ELECTRON_TRANSFER_KIND: "native_electron_transfer",
        CHEMICAL_CLASS_KIND: "native_chemical_class",
        NAMED_COMPLEX_KIND: "native_named_complex",
        PATHWAY_KIND: "native_pathway",
        PROTEIN_CARRIER_REACTION_KIND: "native_protein_carrier_reaction",
    }
    assertions = {}
    claims = []

    def add(identifier: str, kind: str, native: Any, version: str | None, source: str) -> None:
        assertion = kind, json.dumps(native, sort_keys=True), version
        if identifier in assertions and assertions[identifier] != assertion:
            description = {
                NAMED_COMPLEX_KIND: "named-complex",
                PATHWAY_KIND: "pathway",
            }.get(kind, "identity/context")
            raise ValueError(f"{identifier}: conflicting typed native {description} assertions")
        assertions[identifier] = assertion
        claims.append((identifier, source))

    for source, metadata in sources.items():
        kind = metadata.get("kind")
        if kind in fields:
            field = fields[kind]
            observations = [metadata]
            if kind == ECOCYC_STATE_KIND:
                observations.append(metadata["counterpart"])
            for observation in observations:
                native = observation[field]
                add(native["id"], kind, native, observation["version"], source)
        elif kind == RHEA_POLYMER_KIND:
            for identifier, native in metadata["native_polymers"].items():
                # The producer compares complete Polymer facts across releases.
                add(identifier, kind, native, None, source)
        elif source in reaction_requests:
            # This older profile retains its identity, not its complete XML.
            add(reaction_requests[source], kind, None, None, source)
    # Include companion identities in the existing aceto scope guard too; a
    # counterpart can conflict even if its owning state's term is not selected.
    validate_aceto_assertions(sources, claims)
    return {identifier: assertion[0] for identifier, assertion in assertions.items()}


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
                "native_electron_transfer",
                "native_protein_carrier_reaction",
                "native_chemical_class",
                "native_named_complex",
                "native_aceto",
                "native_pathway",
                "native_gene",
                "native_pathbank_context",
                "native_polymers",
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
                "native_electron_transfer",
                "native_protein_carrier_reaction",
                "native_chemical_class",
                "native_named_complex",
                "native_aceto",
                "native_pathway",
                "native_gene",
                "native_pathbank_context",
                "native_polymers",
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
        if "kind" in metadata and metadata["kind"] not in ACETO_KINDS | {
            "metacyc-reaction-xml",
            PATHBANK_ARCHIVE_KIND,
            PATHBANK_CONTEXT_KIND,
            ECOCYC_COMPLEX_KIND,
            CARRIER_CLASS_KIND,
            ECOCYC_STATE_KIND,
            ELECTRON_TRANSFER_KIND,
            PROTEIN_CARRIER_REACTION_KIND,
            CHEMICAL_CLASS_KIND,
            NAMED_COMPLEX_KIND,
            PATHWAY_KIND,
            RHEA_POLYMER_KIND,
            GENE_KIND,
            PSEUDOGENE_KIND,
        }:
            raise ValueError(f"source {source}: unknown typed authority source kind")
        if metadata.get("kind") == PATHBANK_CONTEXT_KIND:
            validate_context_metadata(metadata)
        elif "native_pathbank_context" in metadata:
            raise ValueError("PathBank context metadata requires its typed source kind")
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
        if metadata.get("kind") in ACETO_KINDS:
            validate_aceto_metadata(metadata)
        elif "native_aceto" in metadata:
            raise ValueError("aceto native metadata requires a matching typed source kind")
        for native_kind, field, validator in [
            (
                PROTEIN_CARRIER_REACTION_KIND,
                "native_protein_carrier_reaction",
                validate_carrier_reaction_metadata,
            ),
            (ELECTRON_TRANSFER_KIND, "native_electron_transfer", validate_reaction_metadata),
            (CHEMICAL_CLASS_KIND, "native_chemical_class", validate_chemical_class_metadata),
            (NAMED_COMPLEX_KIND, "native_named_complex", validate_named_complex_metadata),
            (PATHWAY_KIND, "native_pathway", validate_pathway_metadata),
            (RHEA_POLYMER_KIND, "native_polymers", validate_polymer_metadata),
        ]:
            if metadata.get("kind") == native_kind:
                validator(metadata)
            elif field in metadata:
                raise ValueError(f"source {source}: typed native metadata requires its source kind")
        if metadata.get("kind") in GENE_KINDS:
            validate_gene_metadata(metadata)
        elif "native_gene" in metadata:
            raise ValueError(f"source {source}: typed native metadata requires its source kind")
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
    validate_aceto_assertions(data["sources"], [])
    validate_gene_assertions(data["sources"])
    carrier_reaction_ids = validate_carrier_reaction_assertions(data["sources"])
    context_projections = validate_context_assertions(data["sources"])
    context_ids = {ident for projection in context_projections.values() for ident in projection}
    native_kinds = _native_assertion_kinds(data["sources"], native_reaction_requests)
    validate_named_complex_graph(
        [
            metadata["native_named_complex"]
            for metadata in data["sources"].values()
            if metadata.get("kind") == NAMED_COMPLEX_KIND
        ]
    )
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
            {"label_kind", "entity_type", "allowed_categories"},
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
        if is_gene_id(identifier) and source_kind not in GENE_KINDS:
            raise ValueError("KEGG gene identity requires its complete typed source")
        if identifier in context_ids and source_kind != PATHBANK_CONTEXT_KIND:
            raise ValueError("PathBank context requires its complete typed owner")
        if source_kind == PATHBANK_CONTEXT_KIND:
            expected = context_term(identifier, context_projections[term["source"]], term["source"])
            if term != expected:
                raise ValueError("PathBank context term differs from its complete native owner")
        if identifier in carrier_reaction_ids and source_kind != PROTEIN_CARRIER_REACTION_KIND:
            raise ValueError(f"{identifier}: protein-carrier reaction requires whole typed scope")
        native_kind = native_kinds.get(identifier)
        compatible_kinds = {native_kind, SGD_KIND} if native_kind == PATHWAY_KIND else {native_kind}
        if native_kind is not None and source_kind not in compatible_kinds:
            raise ValueError(f"{identifier}: conflicting typed native identity scope")
        if "allowed_categories" in term and source_kind not in {CHEMICAL_CLASS_KIND, RESIDUE_KIND}:
            raise ValueError(f"{identifier}: category proof requires typed native chemical class")
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
        if source_kind in ACETO_KINDS:
            expected_id, expected_term = aceto_term(data["sources"][term["source"]], term["source"])
            if identifier != expected_id or term != expected_term:
                raise ValueError(f"{identifier}: invalid typed aceto authority projection")
        elif source_kind in {
            ELECTRON_TRANSFER_KIND,
            PROTEIN_CARRIER_REACTION_KIND,
            CHEMICAL_CLASS_KIND,
            NAMED_COMPLEX_KIND,
            PATHWAY_KIND,
            RHEA_POLYMER_KIND,
            GENE_KIND,
            PSEUDOGENE_KIND,
        }:
            metadata = data["sources"][term["source"]]
            if source_kind == RHEA_POLYMER_KIND:
                if identifier not in metadata["native_polymers"]:
                    raise ValueError(f"{identifier}: missing whole Polymer metadata")
                expected_id, expected_term = polymer_term(metadata, term["source"], identifier)
            else:
                projector = {
                    PROTEIN_CARRIER_REACTION_KIND: carrier_reaction_term,
                    PATHWAY_KIND: pathway_term,
                    ELECTRON_TRANSFER_KIND: reaction_term,
                    CHEMICAL_CLASS_KIND: chemical_class_term,
                    NAMED_COMPLEX_KIND: named_complex_term,
                    GENE_KIND: gene_term,
                    PSEUDOGENE_KIND: gene_term,
                }[source_kind]
                expected_id, expected_term = projector(metadata, term["source"])
            if identifier != expected_id or json.dumps(term, sort_keys=True) != json.dumps(
                expected_term, sort_keys=True
            ):
                raise ValueError(f"{identifier}: invalid typed native authority projection")
        elif source_kind == ECOCYC_COMPLEX_KIND:
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
    validate_aceto_assertions(
        data["sources"], [(ident, term["source"]) for ident, term in data["terms"].items()]
    )
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
            if term.get("entity_type") == "native_pathway":
                if section != "record":
                    errors.append(
                        f"{where}: ENTITY_TYPE_MISMATCH {identifier!r}; "
                        "typed native pathway requires the record node"
                    )
                elif _normalize(label) != _normalize(term["label"]):
                    errors.append(
                        f"{where}: LABEL_MISMATCH {identifier!r}: {label!r}; "
                        f"authority label is {term['label']!r}"
                    )
                continue
            if term.get("entity_type") == "native_gene":
                if section != "participants" or node.get("category") != "gene":
                    errors.append(
                        f"{where}: ENTITY_TYPE_MISMATCH {identifier!r}; "
                        "typed native gene requires participants/category gene"
                    )
                elif _normalize(label) != _normalize(term["label"]):
                    errors.append(
                        f"{where}: LABEL_MISMATCH {identifier!r}: {label!r}; "
                        f"authority locus is {term['label']!r}"
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
            if (
                term.get("entity_type") == "protein_complex"
                and term.get("label_kind") == "canonical"
            ) or term.get("entity_type") in {"native_chemical_class", "rhea_polymer"}:
                allowed = (
                    ["complex"]
                    if term["entity_type"] == "protein_complex"
                    else ["polymer"]
                    if term["entity_type"] == "rhea_polymer"
                    else term["allowed_categories"]
                )
                if section != "participants" or node.get("category") not in allowed:
                    errors.append(
                        f"{where}: ENTITY_TYPE_MISMATCH {identifier!r}; "
                        f"typed native participant requires category in {allowed!r}"
                    )
                else:
                    labels = [term["label"]]
                    if (
                        entry["policy"] == "canonical_or_synonym"
                        and term["entity_type"] != "rhea_polymer"
                    ):
                        labels += term["synonyms"]
                    if _normalize(label) not in {_normalize(value) for value in labels}:
                        errors.append(
                            f"{where}: LABEL_MISMATCH {identifier!r}: {label!r}; "
                            f"authority label is {term['label']!r}"
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
                and (
                    "authority_entity_types" not in rule
                    or term.get("entity_type") in rule["authority_entity_types"]
                )
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
