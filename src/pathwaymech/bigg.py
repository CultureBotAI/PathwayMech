from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

BIGG_SEED_HEADER = "model_id\treaction_id\tname\tgene_reaction_rule"


@dataclass(frozen=True)
class BiggReaction:
    model_id: str
    reaction_id: str
    name: str
    gene_reaction_rule: str


def load_bigg_model(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a BiGG JSON model object")
    return value


def bigg_reactions(model: dict[str, Any]) -> list[BiggReaction]:
    model_id = f"BiGG:{str(model.get('id', 'unknown')).removeprefix('BiGG:')}"
    return [
        BiggReaction(
            model_id=model_id,
            reaction_id=f"BiGG:{str(reaction.get('id', '')).removeprefix('BiGG:')}",
            name=str(reaction.get("name", "")),
            gene_reaction_rule=str(reaction.get("gene_reaction_rule", "")),
        )
        for reaction in model.get("reactions", [])
        if isinstance(reaction, dict) and reaction.get("id")
    ]


def bigg_seed_rows(reactions: list[BiggReaction]) -> list[str]:
    return [
        BIGG_SEED_HEADER,
        *[
            "\t".join(
                [
                    reaction.model_id,
                    reaction.reaction_id,
                    reaction.name,
                    reaction.gene_reaction_rule,
                ]
            )
            for reaction in reactions
        ],
    ]
