from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

GO_SEED_HEADER = "go_id\tname\tnamespace"


@dataclass(frozen=True)
class GoTerm:
    id: str
    name: str
    namespace: str


def load_go_obo(path: Path) -> list[GoTerm]:
    return go_obo_terms(path.read_text(encoding="utf-8").splitlines())


def go_obo_terms(lines: list[str]) -> list[GoTerm]:
    stanzas = []
    current: dict[str, str] | None = None
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
        current.setdefault(key, value)
    if current:
        stanzas.append(current)

    return [
        GoTerm(id=stanza["id"], name=stanza["name"], namespace=stanza["namespace"])
        for stanza in stanzas
        if stanza.get("id", "").startswith("GO:")
        and stanza.get("is_obsolete") != "true"
        and "name" in stanza
        and "namespace" in stanza
    ]


def go_seed_rows(terms: list[GoTerm]) -> list[str]:
    return [
        GO_SEED_HEADER,
        *["\t".join([term.id, term.name, term.namespace]) for term in terms],
    ]
