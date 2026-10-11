from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

GAPMIND_SEED_HEADER = (
    "family\tpathway_slug\telement_id\telement_type\tdescription\tec_numbers\t"
    "uniprot_ids\tmetacyc_ids\thmm_ids\tother_identifiers\tignored_identifiers\timports\t"
    "components"
)
_EC = re.compile(r"(?:EC[: ]+)?(\d+(?:\.(?:\d+|-)){3})")
_SPACE = re.compile(r"[\t\r\n]+")
_TAGGED = re.compile(r"^(?P<kind>curated|ignore):(?P<source>[^:]+)::(?P<value>.+)$")
_UNIPROT_SOURCES = frozenset({"brenda", "swissprot", "tcdb"})


@dataclass(frozen=True)
class GapMindElement:
    family: str
    pathway_slug: str
    element_id: str
    element_type: str
    description: str = ""
    ec_numbers: tuple[str, ...] = ()
    uniprot_ids: tuple[str, ...] = ()
    metacyc_ids: tuple[str, ...] = ()
    hmm_ids: tuple[str, ...] = ()
    other_identifiers: tuple[str, ...] = ()
    ignored_identifiers: tuple[str, ...] = ()
    imports: tuple[str, ...] = ()
    components: tuple[str, ...] = ()


def load_gapmind_steps(path: Path) -> list[GapMindElement]:
    family = path.parent.name if path.parent.name in {"aa", "carbon"} else ""
    pathway_slug = path.name.removesuffix(".steps")
    elements = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("import "):
            elements.append(_import_element(family, pathway_slug, line))
        elif "\t" in line:
            elements.append(_step_element(family, pathway_slug, line))
        elif ":" in line:
            elements.append(_variant_element(family, pathway_slug, line))
        else:
            raise ValueError(f"{path}: unsupported GapMind line: {line}")
    return elements


def gapmind_seed_rows(elements: list[GapMindElement]) -> list[str]:
    return [
        GAPMIND_SEED_HEADER,
        *[
            "\t".join(
                [
                    _cell(element.family),
                    _cell(element.pathway_slug),
                    _cell(element.element_id),
                    element.element_type,
                    _cell(element.description),
                    _joined(element.ec_numbers),
                    _joined(element.uniprot_ids),
                    _joined(element.metacyc_ids),
                    _joined(element.hmm_ids),
                    _joined(element.other_identifiers),
                    _joined(element.ignored_identifiers),
                    _joined(element.imports),
                    _joined(element.components),
                ]
            )
            for element in elements
        ],
    ]


def _import_element(family: str, pathway_slug: str, line: str) -> GapMindElement:
    imported = line.removeprefix("import ").strip()
    imported_step = imported.rsplit(":", 1)[-1]
    return GapMindElement(
        family=family,
        pathway_slug=pathway_slug,
        element_id=imported_step,
        element_type="import",
        imports=(imported,),
    )


def _step_element(family: str, pathway_slug: str, line: str) -> GapMindElement:
    parts = line.split("\t")
    if len(parts) < 2:
        raise ValueError(f"GapMind step rows need at least an id and description: {line}")

    tokens = parts[2:]
    return GapMindElement(
        family=family,
        pathway_slug=pathway_slug,
        element_id=parts[0],
        element_type="step",
        description=parts[1],
        ec_numbers=tuple(_unique(_direct_ec(tokens))),
        uniprot_ids=tuple(_unique(_direct_uniprot(tokens))),
        metacyc_ids=tuple(_unique(_direct_metacyc(tokens))),
        hmm_ids=tuple(_unique(_hmm(tokens))),
        other_identifiers=tuple(_unique(_direct_other(tokens))),
        ignored_identifiers=tuple(_unique(_ignored(tokens))),
    )


def _variant_element(family: str, pathway_slug: str, line: str) -> GapMindElement:
    element_id, raw_components = line.split(":", 1)
    return GapMindElement(
        family=family,
        pathway_slug=pathway_slug,
        element_id=element_id,
        element_type="variant",
        components=tuple(raw_components.split()),
    )


def _direct_ec(tokens: list[str]) -> list[str]:
    return [f"EC:{match.group(1)}" for token in tokens if (match := _EC.fullmatch(token))]


def _direct_uniprot(tokens: list[str]) -> list[str]:
    identifiers = []
    for token in tokens:
        if token.startswith("uniprot:") or token.startswith("predicted:"):
            identifiers.append(f"UniProtKB:{token.split(':', 1)[1]}")
            continue
        match = _TAGGED.fullmatch(token)
        if match and match.group("kind") == "curated":
            source = match.group("source").casefold()
            if source in _UNIPROT_SOURCES:
                identifiers.append(f"UniProtKB:{match.group('value')}")
    return identifiers


def _direct_metacyc(tokens: list[str]) -> list[str]:
    identifiers = []
    for token in tokens:
        match = _TAGGED.fullmatch(token)
        if (
            match
            and match.group("kind") == "curated"
            and match.group("source").casefold() == "metacyc"
        ):
            identifiers.append(f"MetaCyc:{match.group('value')}")
    return identifiers


def _hmm(tokens: list[str]) -> list[str]:
    return [token.removeprefix("hmm:") for token in tokens if token.startswith("hmm:")]


def _direct_other(tokens: list[str]) -> list[str]:
    identifiers = []
    for token in tokens:
        match = _TAGGED.fullmatch(token)
        if not match or match.group("kind") != "curated":
            continue
        source = match.group("source").casefold()
        if source not in _UNIPROT_SOURCES | {"metacyc"}:
            identifiers.append(f"{match.group('source')}:{match.group('value')}")
    return identifiers


def _ignored(tokens: list[str]) -> list[str]:
    identifiers = []
    for token in tokens:
        if token.startswith("ignore_other:"):
            ignored = token.removeprefix("ignore_other:")
            identifiers.append(_ec_or_raw(ignored))
            continue

        match = _TAGGED.fullmatch(token)
        if not match or match.group("kind") != "ignore":
            continue

        source = match.group("source").casefold()
        value = match.group("value")
        if source in _UNIPROT_SOURCES:
            identifiers.append(f"UniProtKB:{value}")
        elif source == "metacyc":
            identifiers.append(f"MetaCyc:{value}")
        else:
            identifiers.append(f"{match.group('source')}:{value}")
    return identifiers


def _ec_or_raw(value: str) -> str:
    if match := _EC.fullmatch(value.strip()):
        return f"EC:{match.group(1)}"
    return value


def _joined(values: tuple[str, ...]) -> str:
    return "|".join(_cell(value) for value in values)


def _cell(value: str) -> str:
    return _SPACE.sub(" ", value).strip()


def _unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))
