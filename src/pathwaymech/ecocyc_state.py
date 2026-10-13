"""Named ECOLI thioredoxin state instances with separately hashed pair evidence."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from pathwaymech.biocyc_carrier import (
    FRAME,
    PROVENANCE,
    PROVENANCE_ORDER,
    keys,
    names,
    native_identity,
    one,
    original_path,
    provenance,
    reference,
    require,
    valid_label,
)

ECOCYC_STATE_KIND = "ecocyc-protein-state-xml"
NATIVE_KEYS = {
    "id",
    "is_class",
    "parent_classes",
    "direct_common_name",
    "direct_synonyms",
    "state_link",
    "gene",
}


def state_native(path: Path, url: str, version: str) -> dict:
    entity, frame = native_identity(path, url, version, "ECOLI", is_class=False)
    allowed = {
        "parent",
        "common-name",
        "synonym",
        "modified-form",
        "unmodified-form",
        "gene",
        "comment",
        "credits",
        "dblink",
        "citation",
        "evidence",
        "location",
        "has-go-term",
        "molecular-weight-seq",
        "pi",
        "catalyzes",
        "has-feature",
        "isozyme-sequence-similarity",
    }
    require(all(node.tag in allowed for node in entity), "unsupported direct protein-state slots")
    parents = [
        reference(node, "ECOLI", "Protein", is_class=True) for node in entity.findall("parent")
    ]
    require(
        len(parents) == len(set(parents))
        and set(parents) in ({"Red-Thioredoxin"}, {"Modified-Proteins", "Ox-Thioredoxin"}),
        "unsupported protein-state parents",
    )
    relation = "unmodified-form" if "Modified-Proteins" in parents else "modified-form"
    opposite = "modified-form" if relation == "unmodified-form" else "unmodified-form"
    require(not entity.findall(opposite), "conflicting protein-state relations")
    target = reference(one(entity, relation), "ECOLI", "Protein", is_class=False)
    require(target != frame, "self protein-state relation")
    gene = reference(one(entity, "gene"), "ECOLI", "Gene", is_class=False)
    label, aliases = names(entity, frame)
    return {
        "id": "EcoCyc:" + frame,
        "is_class": False,
        "parent_classes": sorted(parents),
        "direct_common_name": label,
        "direct_synonyms": aliases,
        "state_link": {"kind": relation, "id": "EcoCyc:" + target},
        "gene": "EcoCyc:" + gene,
    }


def validate_native_state(native: Any, frame: str) -> None:
    keys(native, NATIVE_KEYS, "incomplete native protein-state metadata")
    require(
        native["id"] == "EcoCyc:" + frame and native["is_class"] is False,
        "invalid protein-state identity/type",
    )
    parents = native["parent_classes"]
    require(
        parents in [["Red-Thioredoxin"], ["Modified-Proteins", "Ox-Thioredoxin"]],
        "invalid protein-state parents",
    )
    require(valid_label(native["direct_common_name"], frame), "invalid protein-state common-name")
    aliases = native["direct_synonyms"]
    require(
        isinstance(aliases, list)
        and all(valid_label(alias, frame) for alias in aliases)
        and aliases == sorted(set(aliases)),
        "invalid protein-state synonyms",
    )
    link = native["state_link"]
    keys(link, {"kind", "id"}, "invalid protein-state link")
    require(
        link["kind"] == ("unmodified-form" if "Modified-Proteins" in parents else "modified-form")
        and isinstance(link["id"], str)
        and re.fullmatch("EcoCyc:" + FRAME, link["id"]) is not None
        and link["id"] != native["id"],
        "invalid protein-state link identity",
    )
    require(
        isinstance(native["gene"], str)
        and re.fullmatch("EcoCyc:" + FRAME, native["gene"]) is not None
        and native["gene"] not in {native["id"], link["id"]},
        "invalid protein-state gene identity",
    )


def validate_state_metadata(metadata: Any) -> None:
    keys(
        metadata,
        PROVENANCE | {"kind", "native_protein_state", "counterpart"},
        "incomplete typed protein-state provenance",
    )
    frame = provenance({key: metadata[key] for key in PROVENANCE}, "ECOLI")
    require(metadata["kind"] == ECOCYC_STATE_KIND, "wrong protein-state source kind")
    native = metadata["native_protein_state"]
    validate_native_state(native, frame)
    partner = metadata["counterpart"]
    keys(partner, PROVENANCE | {"native_protein_state"}, "incomplete counterpart provenance")
    other_frame = provenance({key: partner[key] for key in PROVENANCE}, "ECOLI")
    other = partner["native_protein_state"]
    validate_native_state(other, other_frame)
    require(
        partner["version"] == metadata["version"]
        and other["id"] == native["state_link"]["id"]
        and other["state_link"]["id"] == native["id"]
        and other["state_link"]["kind"] != native["state_link"]["kind"]
        and other["gene"] == native["gene"],
        "nonreciprocal or gene-mismatched state counterpart",
    )


def state_metadata(entry: dict, cache_dir: Path) -> dict:
    keys(
        entry,
        PROVENANCE | {"key", "kind", "path", "counterpart_source"},
        "unsupported protein-state manifest fields",
    )
    require(
        entry["kind"] == ECOCYC_STATE_KIND and isinstance(entry["key"], str) and bool(entry["key"]),
        "wrong protein-state kind/key",
    )
    source = {key: entry[key] for key in PROVENANCE_ORDER}
    provenance(source, "ECOLI")
    path = original_path(entry, cache_dir)
    other_entry = entry["counterpart_source"]
    keys(
        other_entry,
        PROVENANCE | {"path"},
        "counterpart_source requires closed whole-original provenance",
    )
    other_source = {key: other_entry[key] for key in PROVENANCE_ORDER}
    provenance(other_source, "ECOLI")
    other_path = original_path(other_entry, cache_dir)
    require(other_path.resolve() != path.resolve(), "counterpart must be a separate whole original")
    result = {
        **source,
        "kind": ECOCYC_STATE_KIND,
        "native_protein_state": state_native(path, entry["url"], entry["version"]),
        "counterpart": {
            **other_source,
            "native_protein_state": state_native(
                other_path, other_entry["url"], other_entry["version"]
            ),
        },
    }
    validate_state_metadata(result)
    return result


def state_term(metadata: dict, source: str) -> tuple[str, dict]:
    validate_state_metadata(metadata)
    native = metadata["native_protein_state"]
    return native["id"], {
        "label": native["direct_common_name"],
        "synonyms": sorted(set(native["direct_synonyms"]) - {native["direct_common_name"]}),
        "source": source,
        "entity_type": "protein_state",
    }
