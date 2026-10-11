from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

RHEA_SEED_HEADER = "rhea_id\tequation\tchebi_ids\tec_numbers\tgo_terms\txrefs"


@dataclass(frozen=True)
class RheaReaction:
    id: str
    equation: str
    chebi_ids: tuple[str, ...]
    ec_numbers: tuple[str, ...]
    go_terms: tuple[str, ...]
    xrefs: tuple[str, ...]


def load_rhea_tsv(path: Path) -> list[RheaReaction]:
    with path.open(encoding="utf-8", newline="") as stream:
        return rhea_tsv_reactions(stream)


def rhea_tsv_reactions(lines: object) -> list[RheaReaction]:
    reader = csv.DictReader(lines, delimiter="\t")
    return [rhea_reaction(row) for row in reader]


def rhea_reaction(row: dict[str, str]) -> RheaReaction:
    return RheaReaction(
        id=_required(row, "rhea-id"),
        equation=_required(row, "equation"),
        chebi_ids=_split_curies(row.get("chebi-id", ""), "CHEBI"),
        ec_numbers=_split_curies(row.get("ec", ""), "EC"),
        go_terms=_split_curies(row.get("go", ""), "GO"),
        xrefs=tuple(
            [
                *_prefixed_xrefs(row, "reaction-xref(KEGG)", "KEGG"),
                *_prefixed_xrefs(row, "reaction-xref(MetaCyc)", "MetaCyc"),
            ]
        ),
    )


def rhea_seed_rows(reactions: list[RheaReaction]) -> list[str]:
    rows = [RHEA_SEED_HEADER]
    for reaction in reactions:
        rows.append(
            "\t".join(
                [
                    reaction.id,
                    reaction.equation,
                    ";".join(reaction.chebi_ids),
                    ";".join(reaction.ec_numbers),
                    ";".join(reaction.go_terms),
                    ";".join(reaction.xrefs),
                ]
            )
        )
    return rows


def _required(row: dict[str, str], field: str) -> str:
    value = row.get(field, "")
    if value:
        return value
    raise ValueError(f"Rhea TSV row missing {field}")


def _split_curies(value: str, prefix: str) -> tuple[str, ...]:
    curies = []
    for item in _split_list(value):
        if item.startswith(f"{prefix}:"):
            curies.append(item.split()[0])
    return tuple(curies)


def _prefixed_xrefs(row: dict[str, str], field: str, prefix: str) -> list[str]:
    xrefs = []
    for item in _split_list(row.get(field, "")):
        xrefs.append(f"{prefix}:{item.removeprefix(f'{prefix}:')}")
    return xrefs


def _split_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]
