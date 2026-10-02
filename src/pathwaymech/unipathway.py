from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

UNIPATHWAY_SEED_HEADER = (
    "unipathway_id\tterm_type\tname\txrefs\tparents\tpart_ofs\t"
    "input_compounds\toutput_compounds"
)

_XREF_PREFIXES = {"CHEBI", "EC", "GO", "KEGG", "MetaCyc", "PMID", "RHEA"}


@dataclass(frozen=True)
class UniPathwayTerm:
    id: str
    term_type: str
    name: str
    xrefs: tuple[str, ...]
    parents: tuple[str, ...]
    part_ofs: tuple[str, ...]
    input_compounds: tuple[str, ...]
    output_compounds: tuple[str, ...]


def load_unipathway_obo(path: Path) -> list[UniPathwayTerm]:
    return unipathway_obo_terms(path.read_text(encoding="utf-8").splitlines())


def unipathway_obo_terms(lines: list[str]) -> list[UniPathwayTerm]:
    stanzas = []
    current: dict[str, list[str]] | None = None
    for line in lines:
        if line == "[Term]":
            if current:
                stanzas.append(current)
            current = {}
            continue
        if line.startswith("["):
            if current:
                stanzas.append(current)
            current = None
            continue
        if current is None or ": " not in line:
            continue
        key, value = line.split(": ", 1)
        current.setdefault(key, []).append(value)
    if current:
        stanzas.append(current)

    terms = []
    for stanza in stanzas:
        term = _unipathway_term(stanza)
        if term:
            terms.append(term)
    return terms


def unipathway_seed_rows(terms: list[UniPathwayTerm]) -> list[str]:
    return [
        UNIPATHWAY_SEED_HEADER,
        *[
            "\t".join(
                [
                    term.id,
                    term.term_type,
                    term.name,
                    "|".join(term.xrefs),
                    "|".join(term.parents),
                    "|".join(term.part_ofs),
                    "|".join(term.input_compounds),
                    "|".join(term.output_compounds),
                ]
            )
            for term in terms
        ],
    ]


def _unipathway_term(stanza: dict[str, list[str]]) -> UniPathwayTerm | None:
    term_id = _first(stanza, "id")
    if not term_id.startswith("UPa:") or _first(stanza, "is_obsolete") == "true":
        return None

    relationships = stanza.get("relationship", [])
    return UniPathwayTerm(
        id=term_id,
        term_type=_first(stanza, "namespace"),
        name=_first(stanza, "name"),
        xrefs=_ordered_unique(
            xref for value in stanza.get("xref", []) if (xref := _xref(value))
        ),
        parents=_ordered_unique(
            parent for value in stanza.get("is_a", []) if (parent := _upa_target(value))
        ),
        part_ofs=_relationship_targets(relationships, "part_of"),
        input_compounds=_relationship_targets(relationships, "has_input_compound"),
        output_compounds=_relationship_targets(relationships, "has_output_compound"),
    )


def _xref(value: str) -> str:
    curie = value.split(" ", 1)[0]
    if ":" not in curie:
        return ""
    prefix, local_id = curie.split(":", 1)
    if prefix == "METACYC":
        prefix = "MetaCyc"
    if prefix not in _XREF_PREFIXES:
        return ""
    return f"{prefix}:{local_id}"


def _relationship_targets(
    relationships: list[str],
    predicate: str,
) -> tuple[str, ...]:
    prefix = f"{predicate} "
    return _ordered_unique(
        target
        for relationship in relationships
        if relationship.startswith(prefix)
        if (target := _upa_target(relationship.removeprefix(prefix)))
    )


def _upa_target(value: str) -> str:
    target = value.split(" ", 1)[0]
    if not target.startswith("UPa:"):
        return ""
    return target


def _ordered_unique(values: Iterable[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def _first(stanza: dict[str, list[str]], key: str) -> str:
    values = stanza.get(key, [])
    return values[0] if values else ""
