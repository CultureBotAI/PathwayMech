"""Validate local BRENDA reaction-role projections without inferring mechanisms.

The saved query scopes observations to one pathway. Artifact integrity does not
verify the endpoint's assertions or connect reactions to enzymes or organisms.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

from rfc3339_validator import validate_rfc3339

BRENDA_ROLE_VARIABLES = ("reaction", "role", "roleType", "compound", "name", "inchi", "inchikey")
_ENDPOINT = "https://sparql.dsmz.de/api/brenda"
_NATIVE = "https://purl.dsmz.de/brenda/"
_SCHEMA = "https://purl.dsmz.de/schema/"
_MANIFEST_FIELDS = {
    "format_version",
    "pathway_uri",
    "results_file",
    "query_file",
    "results_sha256",
    "query_sha256",
    "source_url",
    "retrieved_at",
    "row_limit",
}


@dataclass(frozen=True)
class BrendaRoleBundle:
    """Validated query observations; not a pathway graph or evidence join."""

    pathway_uri: str
    source_url: str
    retrieved_at: str
    row_limit: int
    results_sha256: str
    query_sha256: str
    bindings: tuple[dict[str, dict[str, str]], ...]


def brenda_role_query(pathway_uri: str, row_limit: int) -> str:
    """Return the one supported, bounded reaction-role query including a newline."""
    if not isinstance(pathway_uri, str) or not re.fullmatch(
        re.escape(_NATIVE) + r"pathway/[0-9]+", pathway_uri
    ):
        raise ValueError("BRENDA pathway_uri must be an exact native numeric pathway URI")
    if type(row_limit) is not int or not 1 <= row_limit <= 10_000:
        raise ValueError("BRENDA row_limit must be an integer between 1 and 10000")
    return (
        "PREFIX d3o: <https://purl.dsmz.de/schema/>\n"
        "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
        "PREFIX dcterms: <http://purl.org/dc/terms/>\n"
        "SELECT DISTINCT ?reaction ?role ?roleType ?compound ?name ?inchi ?inchikey "
        f"WHERE {{ <{pathway_uri}> d3o:hasReaction ?reaction . "
        "VALUES ?roleType { d3o:Substrate d3o:Product } "
        "?role a ?roleType ; d3o:partOf ?reaction ; d3o:refersToCompound ?compound . "
        "OPTIONAL { ?compound rdfs:label ?name } "
        "OPTIONAL { ?compound d3o:hasStructure ?structure . ?structure d3o:hasInChI ?inchi . "
        "OPTIONAL { ?structure d3o:hasInChIKey ?inchikey } } } "
        f"ORDER BY ?reaction ?roleType ?compound LIMIT {row_limit}\n"
    )


def load_brenda_role_bundle(manifest_path: Path) -> BrendaRoleBundle:
    """Validate all local files and rows before returning any observations.

    The manifest pins bytes, query scope, timestamp and requested result limit.
    A result below that limit is not proof of completeness beyond this query.
    """
    manifest = _json_object(manifest_path.read_bytes(), "manifest")
    if set(manifest) != _MANIFEST_FIELDS:
        raise ValueError("BRENDA manifest must contain exactly the documented fields")
    if type(manifest["format_version"]) is not int or manifest["format_version"] != 1:
        raise ValueError("BRENDA manifest format_version must be 1")
    expected_query = brenda_role_query(manifest["pathway_uri"], manifest["row_limit"])
    timestamp = manifest["retrieved_at"]
    if not isinstance(timestamp, str) or not validate_rfc3339(timestamp):
        raise ValueError("BRENDA retrieved_at must be an RFC 3339 timestamp with timezone")
    base = manifest_path.parent.resolve(strict=True)
    query_bytes, query_hash = _artifact(base, manifest, "query")
    result_bytes, result_hash = _artifact(base, manifest, "results")
    try:
        query = query_bytes.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("BRENDA query must be UTF-8") from error
    if query not in (expected_query, expected_query.removesuffix("\n")):
        raise ValueError("BRENDA query does not match the supported pathway scope and row limit")
    source_url = manifest["source_url"]
    _check_source_url(source_url, query)
    result = _json_object(result_bytes, "results")
    if set(result) != {"head", "results"}:
        raise ValueError("BRENDA results must contain exactly head and results")
    if result["head"] != {"vars": list(BRENDA_ROLE_VARIABLES)}:
        raise ValueError("BRENDA results head must declare the seven expected variables in order")
    rows_container = result["results"]
    if not isinstance(rows_container, dict) or set(rows_container) != {"bindings"}:
        raise ValueError("BRENDA results must contain only a bindings list")
    bindings = rows_container["bindings"]
    if not isinstance(bindings, list):
        raise ValueError("BRENDA bindings must be a list")
    if len(bindings) >= manifest["row_limit"]:
        raise ValueError("BRENDA result reaches row_limit and may be truncated")
    seen = set()
    for index, binding in enumerate(bindings):
        _check_binding(binding, index)
        canonical = json.dumps(binding, sort_keys=True, ensure_ascii=True)
        if canonical in seen:
            raise ValueError(f"BRENDA binding {index}: duplicate row contradicts DISTINCT query")
        seen.add(canonical)
    return BrendaRoleBundle(
        pathway_uri=manifest["pathway_uri"],
        source_url=source_url,
        retrieved_at=timestamp,
        row_limit=manifest["row_limit"],
        results_sha256=result_hash,
        query_sha256=query_hash,
        bindings=tuple(bindings),
    )


def brenda_seed_rows(bundle: BrendaRoleBundle) -> Iterator[str]:
    """Render support TSV records, retaining complete RDF bindings as JSON."""
    yield _tsv_line(
        (
            "source",
            "pathway_uri",
            "source_url",
            "retrieved_at",
            "results_sha256",
            "query_sha256",
            "row_limit",
            "source_locator",
            "claim_type",
            "reaction_uri",
            "role_uri",
            "role_type_uri",
            "compound_uri",
            "raw_binding_json",
        )
    )
    for index, binding in enumerate(bundle.bindings):
        yield _tsv_line(
            (
                "brenda",
                bundle.pathway_uri,
                bundle.source_url,
                bundle.retrieved_at,
                bundle.results_sha256,
                bundle.query_sha256,
                str(bundle.row_limit),
                f"results.bindings[{index}]",
                "source_reported_reaction_role",
                binding["reaction"]["value"],
                binding["role"]["value"],
                binding["roleType"]["value"],
                binding["compound"]["value"],
                json.dumps(binding, ensure_ascii=True, separators=(",", ":")),
            )
        )


def _json_object(payload: bytes, label: str) -> dict:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"BRENDA {label}: duplicate JSON key {key!r}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"BRENDA {label}: invalid JSON constant {value}")

    try:
        result = json.loads(
            payload.decode("utf-8"), object_pairs_hook=pairs, parse_constant=reject_constant
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"BRENDA {label}: malformed UTF-8 JSON") from error
    if not isinstance(result, dict):
        raise ValueError(f"BRENDA {label} must be a JSON object")
    return result


def _artifact(base: Path, manifest: dict, kind: str) -> tuple[bytes, str]:
    name = manifest[f"{kind}_file"]
    if (
        not isinstance(name, str)
        or not name
        or name in {".", ".."}
        or "/" in name
        or "\\" in name
        or "\x00" in name
    ):
        raise ValueError(f"BRENDA {kind}_file must be a local basename")
    path = (base / name).resolve(strict=True)
    if path.parent != base:
        raise ValueError(f"BRENDA {kind}_file escapes the manifest directory")
    expected = manifest[f"{kind}_sha256"]
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
        raise ValueError(f"BRENDA {kind}_sha256 must be 64 hexadecimal characters")
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    if digest != expected.lower():
        raise ValueError(f"BRENDA {kind} SHA-256 mismatch")
    return payload, digest


def _check_source_url(source_url: str, query: str) -> None:
    if (
        not isinstance(source_url, str)
        or not source_url.startswith(_ENDPOINT + "?")
        or re.search(r"[\s\x00-\x1f\x7f]", source_url)
    ):
        raise ValueError("BRENDA source_url must use the official SPARQL endpoint")
    try:
        parts = urlsplit(source_url)
        fields = parse_qsl(parts.query, keep_blank_values=True, strict_parsing=True)
    except ValueError as error:
        raise ValueError("BRENDA source_url is malformed") from error
    if (
        f"{parts.scheme}://{parts.netloc}{parts.path}" != _ENDPOINT
        or parts.fragment
        or len(fields) != 2
        or set(dict(fields)) != {"query", "format"}
        or dict(fields).get("format") != "json"
        or dict(fields).get("query") not in (query, query.removesuffix("\n"))
    ):
        raise ValueError("BRENDA source_url must encode the exact saved query and format=json")


def _check_binding(binding: object, index: int) -> None:
    label = f"BRENDA binding {index}"
    required = set(BRENDA_ROLE_VARIABLES[:4])
    if (
        not isinstance(binding, dict)
        or not required <= set(binding)
        or not set(binding) <= set(BRENDA_ROLE_VARIABLES)
    ):
        raise ValueError(f"{label}: expected required URI terms and supported optional terms")
    for variable, term in binding.items():
        if not isinstance(term, dict) or not {"type", "value"} <= set(term):
            raise ValueError(f"{label}: malformed {variable} term")
        if not all(isinstance(value, str) for value in term.values()):
            raise ValueError(f"{label}: {variable} term fields must be strings")
        if variable in required:
            if set(term) != {"type", "value"} or term["type"] != "uri":
                raise ValueError(f"{label}: {variable} must be a URI term")
        else:
            if term["type"] != "literal" or not set(term) <= {
                "type",
                "value",
                "datatype",
                "xml:lang",
            }:
                raise ValueError(f"{label}: {variable} must be a supported literal term")
            if "datatype" in term and "xml:lang" in term:
                raise ValueError(f"{label}: literal cannot specify both datatype and language")
            if "xml:lang" in term and not re.fullmatch(
                r"[A-Za-z]+(?:-[A-Za-z0-9]+)*", term["xml:lang"]
            ):
                raise ValueError(f"{label}: invalid literal language tag")
            if "datatype" in term and not re.fullmatch(
                r"[A-Za-z][A-Za-z0-9+.-]*:[^\s<>\x00-\x1f\x7f]+", term["datatype"]
            ):
                raise ValueError(f"{label}: literal datatype must be an absolute IRI")
    role_type = binding["roleType"]["value"]
    if role_type not in {_SCHEMA + "Substrate", _SCHEMA + "Product"}:
        raise ValueError(f"{label}: unsupported roleType")
    patterns = {
        "reaction": r"reaction/[A-Z]+/[0-9]+",
        "role": ("substrate" if role_type.endswith("Substrate") else "product") + r"/[0-9]+",
        "compound": r"compound/[0-9]+",
    }
    for variable, pattern in patterns.items():
        if not re.fullmatch(re.escape(_NATIVE) + pattern, binding[variable]["value"]):
            raise ValueError(f"{label}: {variable} is outside its native BRENDA namespace")
    if "inchikey" in binding and "inchi" not in binding:
        raise ValueError(f"{label}: inchikey cannot be bound without inchi in this query")


def _tsv_line(values: tuple[str, ...]) -> str:
    buffer = io.StringIO(newline="")
    csv.writer(buffer, delimiter="\t", lineterminator="\n").writerow(values)
    return buffer.getvalue().removesuffix("\n")
