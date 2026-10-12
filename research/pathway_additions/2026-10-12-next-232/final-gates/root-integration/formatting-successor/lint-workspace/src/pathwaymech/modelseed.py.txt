from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

MODELSEED_SEED_HEADER = "modelseed_id\tequation\tec_numbers\taliases"


@dataclass(frozen=True)
class ModelSeedReaction:
    id: str
    equation: str
    ec_numbers: str
    aliases: str


def load_modelseed_tsv(path: Path) -> list[ModelSeedReaction]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return [
            ModelSeedReaction(
                id=f"ModelSEED:{row['id'].removeprefix('ModelSEED:')}",
                equation=row.get("equation", ""),
                ec_numbers=row.get("ec_numbers", ""),
                aliases=row.get("aliases", ""),
            )
            for row in reader
        ]


def modelseed_seed_rows(reactions: list[ModelSeedReaction]) -> list[str]:
    return [
        MODELSEED_SEED_HEADER,
        *[
            "\t".join(
                [reaction.id, reaction.equation, reaction.ec_numbers, reaction.aliases]
            )
            for reaction in reactions
        ],
    ]
