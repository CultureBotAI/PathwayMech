from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

import pytest

from pathwaymech.seed_subsystems import load_seed_subsystem_bundle, seed_subsystem_rows

SUBSYSTEM = "Synthetic subsystem"


def make_bundle(tmp_path: Path, *, roles=None, genomes=None) -> Path:
    payloads = {
        "roles": roles if roles is not None else [["Role A", "A"], ["Role B", "B"]],
        "pegs": genomes if genomes is not None else {
            "100.2:region-x": ["-1", ["Role A", "fig|100.2.peg.1"], ["Role B"]],
            "200.1": ["", ["Role B", "fig|200.1.peg.2", "fig|200.1.peg.3"]],
            "300.1": ["0"],
        },
        "version": "42", "curator": "Curator", "description": "Description\nwith\ttabs\rtoo",
    }
    entries = []
    for kind, value in payloads.items():
        data = json.dumps({SUBSYSTEM: value}).encode()
        filename = f"{kind}.json"
        (tmp_path / filename).write_bytes(data)
        if kind == "roles":
            method, parameters = "subsystem_roles", {"-ids": [SUBSYSTEM], "-aux": 1, "-abbr": 1}
        elif kind == "pegs":
            method, parameters = "pegs_in_variants", {"-subsystems": [SUBSYSTEM]}
        else:
            method, parameters = "subsystem_data", {"-ids": [SUBSYSTEM], "-field": kind}
        entries.append({"file": filename, "endpoint": "https://seed.example/sapling/server.cgi",
                        "method": method, "parameters": parameters, "encoding": "json",
                        "acquired_at": "2026-10-08T01:02:03Z", "http_status": "200",
                        "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps({"schema_version": 1, "subsystem": SUBSYSTEM,
                                    "artifacts": entries}))
    return manifest


def change_manifest(manifest: Path, edit) -> None:
    doc = json.loads(manifest.read_bytes())
    edit(doc)
    manifest.write_text(json.dumps(doc))


def change_response(manifest: Path, kind: str, data: bytes) -> None:
    doc = json.loads(manifest.read_bytes())
    entry = next(x for x in doc["artifacts"] if x["file"] == f"{kind}.json")
    (manifest.parent / entry["file"]).write_bytes(data)
    entry.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
    manifest.write_text(json.dumps(doc))


def test_lossless_roundtrip_preserves_negative_empty_variants_and_native_cells(tmp_path):
    manifest = make_bundle(tmp_path)
    bundle = load_seed_subsystem_bundle(manifest)
    rows = list(csv.DictReader(io.StringIO("\n".join(seed_subsystem_rows(bundle)) + "\n"),
                               delimiter="\t"))
    assert len(rows) == 8
    genomes = {row["genome_id"]: json.loads(row["native_value_json"])
               for row in rows if row["record_type"] == "genome_variant"}
    assert genomes == bundle.genomes
    assert genomes["100.2:region-x"][0] == "-1"
    assert genomes["200.1"][0] == ""
    assert genomes["300.1"] == ["0"]
    assert json.loads(rows[2]["native_value_json"]) == "Description\nwith\ttabs\rtoo"
    assert all(row["bundle_sha256"] == hashlib.sha256(manifest.read_bytes()).hexdigest()
               for row in rows)
    assert all(row["subsystem_version"] == "42" for row in rows)
    assert "NCBITaxon" not in "\n".join(seed_subsystem_rows(bundle))


def test_duplicate_role_occurrences_do_not_multiply_genome_observations(tmp_path):
    manifest = make_bundle(tmp_path, roles=[["Role A", "A"], ["Role A", "A"]],
                           genomes={"100.1": ["1", ["Role A", "fig|100.1.peg.1"]]})
    bundle = load_seed_subsystem_bundle(manifest)
    rows = list(csv.DictReader(io.StringIO("\n".join(seed_subsystem_rows(bundle))), delimiter="\t"))
    assert [row["role_position"] for row in rows if row["record_type"] == "role"] == ["1", "2"]
    assert sum(row["record_type"] == "genome_variant" for row in rows) == 1
    assert bundle.roles == (("Role A", "A"), ("Role A", "A"))


@pytest.mark.parametrize("genomes,error", [
    ({"100.1": ["1", ["Stale role name", "fig|100.1.peg.1"]]}, "Unmapped"),
    ({"100.1": ["1", ["Role A"], ["Role A"]]}, "Duplicate SEED role cell"),
    ({"100.1": [1, ["Role A"]]}, "variant code"),
    ({"100.1": []}, "variant code"),
    ({"100.1": ["1", []]}, "role cell"),
    ({"100.1": ["1", ["Role A", None]]}, "feature identifier"),
    ({"100.1": ["1", "Role A"]}, "role cell"),
    ({"": ["1"]}, "genome identifier"),
    ({}, "at least one genome"),
    ([], "at least one genome"),
])
def test_invalid_native_rows_refused_before_output(tmp_path, genomes, error):
    with pytest.raises(ValueError, match=error):
        load_seed_subsystem_bundle(make_bundle(tmp_path, genomes=genomes))


@pytest.mark.parametrize("roles", [[], {}, [["Role A"]], [["Role A", "A", "extra"]],
                                    [[None, "A"]], [["Role A", 2]]])
def test_invalid_roles(tmp_path, roles):
    with pytest.raises(ValueError):
        load_seed_subsystem_bundle(make_bundle(tmp_path, roles=roles))


@pytest.mark.parametrize("edit,error", [
    (lambda d: d.update(schema_version=True), "schema_version"),
    (lambda d: d.update(extra="unsupported"), "schema_version"),
    (lambda d: d["artifacts"].pop(), "five"),
    (lambda d: d["artifacts"].__setitem__(1, d["artifacts"][0]), "Duplicate"),
    (lambda d: d["artifacts"][0].update(sha256="bad"), "SHA-256"),
    (lambda d: d["artifacts"][0].update(sha256="0" * 64), "SHA-256 mismatch"),
    (lambda d: d["artifacts"][0].update(bytes=1), "byte count"),
    (lambda d: d["artifacts"][0].update(file="../roles.json"), "basename"),
    (lambda d: d["artifacts"][0].update(endpoint="http://seed.example/api"), "HTTPS"),
    (lambda d: d["artifacts"][0].update(endpoint="https://user:pass@seed.example/api"), "HTTPS"),
    (lambda d: d["artifacts"][0].update(acquired_at="2026-10-08"), "timezone"),
    (lambda d: d["artifacts"][0].update(acquired_at="yesterday"), "timestamp"),
    (lambda d: d["artifacts"][0].update(http_status=500), "successful"),
    (lambda d: d["artifacts"][0].update(returncode=28), "acquisition failed"),
    (lambda d: d["artifacts"][0].update(encoding="yaml"), "JSON response"),
    (lambda d: d["artifacts"][0]["parameters"].update({"-aux": 0}), "-aux=1"),
    (lambda d: d["artifacts"][0]["parameters"].update({"-aux": True}), "-aux=1"),
    (lambda d: d["artifacts"][1].update(endpoint="https://different.example/api"), "one endpoint"),
    (lambda d: d["artifacts"][1]["parameters"].update({"-genomes": ["100.2"]}), "no genome filter"),
    (lambda d: d["artifacts"][0]["parameters"].update({"-ids": ["Other"]}), "exact subsystem"),
])
def test_manifest_contract(tmp_path, edit, error):
    manifest = make_bundle(tmp_path)
    change_manifest(manifest, edit)
    with pytest.raises(ValueError, match=error):
        load_seed_subsystem_bundle(manifest)


@pytest.mark.parametrize("data,error", [
    (b'{"Other subsystem": []}', "subsystem mismatch"),
    (b'{"Synthetic subsystem": [], "Synthetic subsystem": []}', "Duplicate JSON key"),
    (b'{"Synthetic subsystem": NaN}', "Invalid JSON constant"),
    (b'<html>Database unavailable</html>', "Invalid SEED JSON"),
    (b'\xff', "Invalid SEED JSON"),
    (b'{"Synthetic subsystem": 42}', "SEED version"),
])
def test_hash_valid_but_malformed_responses_are_refused(tmp_path, data, error):
    manifest = make_bundle(tmp_path)
    change_response(manifest, "version", data)
    with pytest.raises(ValueError, match=error):
        load_seed_subsystem_bundle(manifest)


def test_symlink_cannot_escape_bundle_directory(tmp_path):
    directory = tmp_path / "bundle"
    directory.mkdir()
    manifest = make_bundle(directory)
    original = (directory / "roles.json").read_bytes()
    (directory / "roles.json").unlink()
    (tmp_path / "outside.json").write_bytes(original)
    (directory / "roles.json").symlink_to(tmp_path / "outside.json")
    with pytest.raises(ValueError, match="escape"):
        load_seed_subsystem_bundle(manifest)
