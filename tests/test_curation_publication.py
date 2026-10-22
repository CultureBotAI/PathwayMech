"""Regression coverage for destructive migration and ledger replay."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

SCRIPTS = Path(
    os.environ.get("PATHWAYMECH_MIGRATION_SCRIPTS", Path(__file__).parents[1] / "scripts")
)


def record(identifier="gomodel:test"):
    return {
        "id": identifier,
        "label": "Test",
        "description": "Migration test.",
        "pathway_type": "test",
        "taxa": [],
        "participants": [],
        "reactions": [],
        "mechanistic_edges": [],
        "references": [{"id": identifier, "title": "Source"}],
    }


def supplement_fixture(tmp_path, *, second_ready=True):
    paths = tmp_path / "data/pathways"
    paths.mkdir(parents=True)
    first = record()
    first["participants"] = [
        {"id": "SGD:S000000207", "label": "COQ1"},
        {"id": "CHEBI:58179", "label": "hexaprenyl diphosphate"},
    ]
    first["reactions"] = [
        {"id": "gomodel:RXN3O-9805", "label": "heptaprenyl diphosphate synthase activity"}
    ]
    for i, (s, p, o) in enumerate(
        [
            ("SGD:S000000207", "enables", "gomodel:RXN3O-9805"),
            ("gomodel:RXN3O-9805", "has_output", "CHEBI:58179"),
        ]
    ):
        first["mechanistic_edges"].append(
            {
                "id": f"edge-{i}",
                "subject": s,
                "predicate": p,
                "object": o,
                "evidence": [{"reference_id": first["id"], "quote": "Native assertion."}],
            }
        )
    second = record("gomodel:second")
    if second_ready:
        second["reactions"] = [{"id": "gomodel:RXN0-745", "label": "Excluded activity"}]
    files = [
        paths / "hexaprenyl-diphosphate-biosynthesis.yaml",
        paths / "adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml",
    ]
    for path, value in zip(files, [first, second], strict=True):
        path.write_text(yaml.safe_dump(value))
    source = tmp_path / "uniprot.json"
    source.write_text(
        json.dumps(
            {
                "results": [
                    {
                        "primaryAccession": "P18900",
                        "proteinDescription": {
                            "recommendedName": {
                                "fullName": {
                                    "value": "Hexaprenyl pyrophosphate synthase, mitochondrial"
                                }
                            }
                        },
                    }
                ]
            }
        )
    )
    provenance = tmp_path / "provenance.json"
    provenance.write_text(
        json.dumps(
            {
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "url": "https://example.org/source",
            }
        )
    )
    command = [
        str(SCRIPTS / "curate_gocam_chemical_supplement.py"),
        "--root",
        str(tmp_path),
        "--uniprot-json",
        str(source),
        "--provenance",
        str(provenance),
        "--report",
        str(tmp_path / "report.json"),
    ]
    return files, command


def test_supplement_defaults_to_preview_without_record_writes(tmp_path):
    files, command = supplement_fixture(tmp_path)
    before = [p.read_bytes() for p in files]
    result = subprocess.run([sys.executable, *command], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert [p.read_bytes() for p in files] == before
    assert json.loads((tmp_path / "report.json").read_text())["applied"] is False


@pytest.mark.parametrize("optimized", [False, True])
def test_supplement_preflights_second_record_before_first_write(tmp_path, optimized):
    files, command = supplement_fixture(tmp_path, second_ready=False)
    before = [p.read_bytes() for p in files]
    result = subprocess.run(
        [sys.executable, *(["-O"] if optimized else []), *command], capture_output=True, text=True
    )
    assert [p.read_bytes() for p in files] == before
    assert result.returncode != 0
    assert not (tmp_path / "report.json").exists()


def test_publication_validates_every_record_before_writing(tmp_path):
    from pathwaymech.curation import publish_curation

    paths = [tmp_path / "one.yaml", tmp_path / "two.yaml"]
    for path in paths:
        path.write_text(yaml.safe_dump(record()))
    before = [p.read_bytes() for p in paths]
    first, second = record(), record()
    first["description"] = "Changed"
    second["unknown_field"] = "invalid"
    with pytest.raises(ValueError):
        publish_curation(
            list(zip(paths, [first, second], strict=True)), tmp_path / "report.json", {}, apply=True
        )
    assert [p.read_bytes() for p in paths] == before
    assert not (tmp_path / "report.json").exists()


@pytest.mark.parametrize("apply", [False, True])
@pytest.mark.parametrize("marked", [False, True])
def test_noop_preserves_applied_and_legacy_ledgers(tmp_path, apply, marked):
    from pathwaymech.curation import publish_curation

    path = tmp_path / "record.yaml"
    path.write_text(yaml.safe_dump(record()))
    report = tmp_path / "report.json"
    prior = {"records": [{"excluded_source_edges": ["superseded source assertion"]}]}
    if marked:
        prior["applied"] = True
    report.write_text(json.dumps(prior))
    before = report.read_bytes()
    assert publish_curation([(path, record())], report, {"records": []}, apply=apply) == 0
    assert report.read_bytes() == before


@pytest.mark.parametrize("apply", [False, True])
def test_changed_replay_cannot_replace_historical_report(tmp_path, apply):
    from pathwaymech.curation import publish_curation

    path, report = tmp_path / "record.yaml", tmp_path / "report.json"
    path.write_text(yaml.safe_dump(record()))
    report.write_text('{"applied":true,"records":["original review"]}')
    before = path.read_bytes(), report.read_bytes()
    changed = deepcopy(record())
    changed["description"] = "Changed"
    with pytest.raises(ValueError, match="choose a new report path"):
        publish_curation([(path, changed)], report, {}, apply=apply)
    assert (path.read_bytes(), report.read_bytes()) == before


def test_baseline_guard_includes_changes_only_in_later_target(tmp_path):
    from pathwaymech.curation import guard_baseline

    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    paths = [tmp_path / "one.yaml", tmp_path / "two.yaml"]
    for path in paths:
        path.write_text("original\n")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.org",
            "commit",
            "-qm",
            "baseline",
        ],
        cwd=tmp_path,
        check=True,
    )
    guard_baseline(paths, "HEAD", tmp_path)
    paths[1].write_text("later independent curation\n")
    with pytest.raises(ValueError, match="two.yaml"):
        guard_baseline(paths, "HEAD", tmp_path)
    assert paths[0].read_text() == "original\n"


@pytest.mark.parametrize("directory", [False, True])
def test_preview_does_not_authorize_overwriting_unowned_supplement(tmp_path, directory):
    from pathwaymech.curation import publish_curation

    path, report, extra = (
        tmp_path / "record.yaml",
        tmp_path / "report.json",
        tmp_path / "source.json",
    )
    path.write_text(yaml.safe_dump(record()))
    report.write_text('{"applied":false}')
    if directory:
        extra.mkdir()
    else:
        extra.write_text('{"excluded_facts":["historical source evidence"]}')
    before = path.read_bytes(), report.read_bytes()
    changed = record()
    changed["description"] = "Changed"
    with pytest.raises(ValueError, match="supplemental ledger"):
        publish_curation([(path, changed)], report, {}, apply=True, extra_reports={extra: "{}\n"})
    assert (path.read_bytes(), report.read_bytes()) == before


def test_report_staging_failure_leaves_records_and_report_unchanged(tmp_path, monkeypatch):
    import pathwaymech.curation as curation

    path, report = tmp_path / "record.yaml", tmp_path / "report.json"
    path.write_text(yaml.safe_dump(record()))
    report.write_text('{"applied":false}')
    before = path.read_bytes(), report.read_bytes()
    changed = record()
    changed["description"] = "Changed"
    original = curation.tempfile.NamedTemporaryFile

    def fail_report(**kwargs):
        if kwargs["prefix"].startswith(".report.json."):
            raise OSError("report destination unavailable")
        return original(**kwargs)

    monkeypatch.setattr(curation.tempfile, "NamedTemporaryFile", fail_report)
    with pytest.raises(OSError, match="report destination unavailable"):
        curation.publish_curation([(path, changed)], report, {}, apply=True)
    assert (path.read_bytes(), report.read_bytes()) == before
    assert not list(tmp_path.glob(".*.tmp"))


def test_publish_curation_preserves_existing_line_wrap_width(tmp_path):
    from pathwaymech.curation import publish_curation

    path = tmp_path / "record.yaml"
    report = tmp_path / "report.json"
    initial = record()
    initial["description"] = (
        "This long pathway description spans well over eighty-eight characters so that "
        "wrapping differs visibly between width=88 and width=100 during guarded publication."
    )
    path.write_text(
        yaml.safe_dump(initial, sort_keys=False, allow_unicode=True, width=88),
        encoding="utf-8",
    )
    updated = deepcopy(initial)
    updated["pathway_type"] = "updated-test"
    assert publish_curation([(path, updated)], report, {"records": []}, apply=True) == 1
    expected = yaml.safe_dump(updated, sort_keys=False, allow_unicode=True, width=88)
    assert path.read_text(encoding="utf-8") == expected
    assert path.read_text(encoding="utf-8") != yaml.safe_dump(
        updated, sort_keys=False, allow_unicode=True, width=100
    )


def test_publish_curation_preserves_yaml_anchor_aliases_across_deep_copies(tmp_path):
    from pathwaymech.curation import publish_curation

    path = tmp_path / "anchored.yaml"
    report = tmp_path / "report.json"
    initial = record()
    initial["participants"] = [
        {"id": "CHEBI:15377", "label": "water"},
        {"id": "CHEBI:15378", "label": "hydron"},
    ]
    initial["reactions"] = [{"id": "RHEA:10000", "label": "test reaction"}]
    shared_evidence = [
        {"reference_id": initial["id"], "quote": "Shared verbatim evidence across edges."}
    ]
    initial["mechanistic_edges"] = [
        {
            "id": "edge-1",
            "subject": "CHEBI:15377",
            "predicate": "consumes",
            "object": "RHEA:10000",
            "evidence": shared_evidence,
        },
        {
            "id": "edge-2",
            "subject": "RHEA:10000",
            "predicate": "produces",
            "object": "CHEBI:15378",
            "evidence": shared_evidence,
        },
    ]
    dumped_initial = yaml.safe_dump(
        initial, sort_keys=False, allow_unicode=True, width=100
    )
    assert "&id001" in dumped_initial and "*id001" in dumped_initial
    path.write_text(dumped_initial, encoding="utf-8")

    # Round-trip through JSON to break Python object identity on shared_evidence
    unlinked = json.loads(json.dumps(yaml.safe_load(path.read_text(encoding="utf-8"))))
    unlinked["reactions"][0]["category"] = "molecular_activity"
    assert publish_curation([(path, unlinked)], report, {"records": []}, apply=True) == 1
    published_text = path.read_text(encoding="utf-8")
    assert "&id001" in published_text and "*id001" in published_text

