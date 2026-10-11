"""Lossless, offline support rows from hash-bound native SEED API snapshots.

Role positions align the source spreadsheet; they are not reaction order. Genome
and feature identifiers remain native opaque strings, and a variant is not an
experimental assertion that a complete pathway is present.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

_FIELDS = ("roles", "pegs", "version", "curator", "description")
SEED_SUBSYSTEM_HEADER = (
    "record_type\tsubsystem\tgenome_id\tvariant_code\trole_position\trole_name\t"
    "role_abbreviation\tnative_value_json\tsource_file\tsource_sha256\tsource_url\t"
    "source_method\tsource_parameters_json\tacquired_at\tsubsystem_version\tbundle_sha256"
)


@dataclass(frozen=True)
class SeedSubsystemBundle:
    subsystem: str
    roles: tuple[tuple[str, str], ...]
    genomes: dict[str, list]
    metadata: dict[str, str]
    artifacts: dict[str, dict]
    sha256: str


def _object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _json(data: bytes) -> object:
    try:
        return json.loads(data, object_pairs_hook=_object,
                          parse_constant=lambda value: _invalid(f"Invalid JSON constant: {value}"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValueError(f"Invalid SEED JSON: {error}") from error


def _invalid(message: str):
    raise ValueError(message)


def _text(value: object, context: str, *, empty: bool = False) -> str:
    if not isinstance(value, str) or (not empty and not value.strip()):
        raise ValueError(f"{context} must be a {'possibly empty ' if empty else 'nonempty '}string")
    return value


def _source_kind(entry: dict, subsystem: str) -> str:
    method, parameters = entry.get("method"), entry.get("parameters")
    if method == "subsystem_roles":
        if (parameters != {"-ids": [subsystem], "-aux": 1, "-abbr": 1}
                or type(parameters.get("-aux")) is not int
                or type(parameters.get("-abbr")) is not int):
            raise ValueError("SEED roles require the exact subsystem, -aux=1 and -abbr=1")
        return "roles"
    if method == "pegs_in_variants":
        if parameters != {"-subsystems": [subsystem]}:
            raise ValueError("SEED variants require the exact subsystem and no genome filter")
        return "pegs"
    if method == "subsystem_data" and isinstance(parameters, dict):
        field = parameters.get("-field")
        if field in ("version", "curator", "description") and parameters == {
            "-ids": [subsystem], "-field": field
        }:
            return field
    raise ValueError("Unsupported SEED API method or parameters")


def load_seed_subsystem_bundle(manifest: Path) -> SeedSubsystemBundle:
    """Validate all five native responses before exposing any support rows.

    The manifest binds exact requests, retrieval timestamps and response hashes.
    It is an acquisition record, not authentication of the remote database.
    """
    manifest_bytes = manifest.read_bytes()
    document = _json(manifest_bytes)
    if not isinstance(document, dict) or set(document) != {
        "schema_version", "subsystem", "artifacts"
    } or type(document["schema_version"]) is not int or document["schema_version"] != 1:
        raise ValueError("SEED manifest requires schema_version=1, subsystem and artifacts")
    subsystem = _text(document["subsystem"], "SEED subsystem")
    entries = document["artifacts"]
    if not isinstance(entries, list) or len(entries) != len(_FIELDS):
        raise ValueError("SEED manifest requires five response artifacts")
    artifacts, payloads, seen_files = {}, {}, set()
    endpoints = set()
    root = manifest.parent.resolve()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("SEED artifact must be an object")
        required = {"file", "endpoint", "method", "parameters", "encoding", "acquired_at",
                    "http_status", "sha256", "bytes"}
        if not required <= entry.keys() or entry.keys() - required - {"returncode", "error"}:
            raise ValueError("SEED artifact has missing or unsupported fields")
        if entry["encoding"] != "json" or entry["http_status"] not in (200, "200"):
            raise ValueError("SEED artifact must be a successful JSON response")
        if entry.get("returncode", 0) != 0 or entry.get("error", "") != "":
            raise ValueError("SEED artifact acquisition failed")
        kind = _source_kind(entry, subsystem)
        if kind in artifacts:
            raise ValueError(f"Duplicate SEED artifact kind: {kind}")
        filename = _text(entry["file"], "SEED artifact filename")
        if Path(filename).name != filename or filename in {".", ".."} or filename in seen_files:
            raise ValueError("SEED artifact requires a unique local basename")
        seen_files.add(filename)
        source = root / filename
        if not source.resolve().is_relative_to(root):
            raise ValueError("SEED artifact may not escape manifest directory")
        endpoint = urlsplit(_text(entry["endpoint"], "SEED endpoint"))
        if (endpoint.scheme != "https" or not endpoint.netloc or endpoint.username
                or endpoint.password or endpoint.fragment or endpoint.query):
            raise ValueError("SEED endpoint requires HTTPS and no credentials/query")
        endpoints.add(entry["endpoint"])
        if len(endpoints) > 1:
            raise ValueError("SEED response bundle must use one endpoint")
        timestamp = _text(entry["acquired_at"], "SEED acquisition timestamp")
        try:
            acquired = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except ValueError as error:
            raise ValueError("Invalid SEED acquisition timestamp") from error
        if acquired.tzinfo is None:
            raise ValueError("SEED acquisition timestamp requires a timezone")
        digest = entry["sha256"]
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError("Invalid SEED SHA-256")
        data = source.read_bytes()
        if type(entry["bytes"]) is not int or len(data) != entry["bytes"]:
            raise ValueError(f"SEED byte count mismatch: {filename}")
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f"SEED SHA-256 mismatch: {filename}")
        payload = _json(data)
        if not isinstance(payload, dict) or set(payload) != {subsystem}:
            raise ValueError(f"SEED response subsystem mismatch: {filename}")
        artifacts[kind] = entry
        payloads[kind] = payload[subsystem]
    if set(payloads) != set(_FIELDS):
        raise ValueError("SEED responses require roles, variants and three metadata fields")
    roles = payloads["roles"]
    if not isinstance(roles, list) or not roles:
        raise ValueError("SEED roles must be a nonempty list")
    for pair in roles:
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("SEED role must contain exactly its name and abbreviation")
        _text(pair[0], "SEED role name")
        _text(pair[1], "SEED role abbreviation", empty=True)
    # Duplicate role occurrences are native spreadsheet positions, not new identities.
    role_names = {pair[0] for pair in roles}
    genomes = payloads["pegs"]
    if not isinstance(genomes, dict) or not genomes:
        raise ValueError("SEED variants must contain at least one genome row")
    for genome, row in genomes.items():
        _text(genome, "SEED genome identifier")
        if not isinstance(row, list) or not row:
            raise ValueError("SEED genome row requires a variant code")
        _text(row[0], "SEED variant code", empty=True)
        seen_roles = set()
        for cell in row[1:]:
            if not isinstance(cell, list) or not cell:
                raise ValueError("SEED role cell requires a role name")
            role = _text(cell[0], "SEED cell role")
            if role not in role_names:
                raise ValueError(f"Unmapped SEED role: {role}")
            if role in seen_roles:
                raise ValueError(f"Duplicate SEED role cell for genome {genome}: {role}")
            seen_roles.add(role)
            for feature in cell[1:]:
                _text(feature, "SEED feature identifier")
    metadata = {field: _text(payloads[field], f"SEED {field}", empty=field != "version")
                for field in ("version", "curator", "description")}
    return SeedSubsystemBundle(subsystem, tuple(tuple(pair) for pair in roles), genomes,
                               metadata, artifacts, hashlib.sha256(manifest_bytes).hexdigest())


def seed_subsystem_rows(bundle: SeedSubsystemBundle) -> list[str]:
    """Emit lossless native source values; no biological edges or IDs are invented."""
    output = [SEED_SUBSYSTEM_HEADER]

    def row(kind: str, value: object, *, genome: str = "", variant: str = "",
            position: str = "", role: str = "", abbreviation: str = "") -> None:
        source = bundle.artifacts[kind]
        stream = io.StringIO(newline="")
        csv.writer(stream, delimiter="\t", lineterminator="\r\n").writerow([
            "role" if kind == "roles" else "genome_variant" if kind == "pegs" else kind,
            bundle.subsystem, genome, variant, position, role, abbreviation,
            json.dumps(value, ensure_ascii=False, separators=(",", ":")), source["file"],
            source["sha256"], source["endpoint"], source["method"],
            json.dumps(source["parameters"], ensure_ascii=False, sort_keys=True,
                       separators=(",", ":")), source["acquired_at"],
            bundle.metadata["version"], bundle.sha256,
        ])
        output.append(stream.getvalue().removesuffix("\r\n"))

    for field in ("version", "curator", "description"):
        row(field, bundle.metadata[field])
    for position, (role, abbreviation) in enumerate(bundle.roles, 1):
        row("roles", [role, abbreviation], position=str(position), role=role,
            abbreviation=abbreviation)
    for genome, native in sorted(bundle.genomes.items()):
        row("pegs", native, genome=genome, variant=native[0])
    return output
