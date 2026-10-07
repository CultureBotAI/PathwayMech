"""Invalid input must not become successful, empty cross-corpus evidence."""

import json
import subprocess

import pytest
import yaml

from pathwaymech import cross_mech as cross

HEADERS = "Entry\tReviewed\tOrganism (ID)\tEC number\tRhea ID\tPathway\n"
PATHWAY = {"id": "GO:42", "label": "Example", "participants": [
    {"id": "UniProtKB:P0A749", "label": "MurA"},
]}


def cli_fixture(tmp_path):
    root = tmp_path / "PathwayMech"
    records = root / "data/pathways"
    records.mkdir(parents=True)
    (records / "record.yaml").write_text(yaml.safe_dump(PATHWAY))
    sibling = tmp_path / "Sibling"
    sibling.mkdir()
    (sibling / "record.yaml").write_text("identifier: example\n")
    config = tmp_path / "config.yaml"
    config.write_text(yaml.safe_dump({"version": 1, "mechs": {
        "Sibling": {"records": "*.yaml", "protein_slots": [], "link_slots": []},
    }}))
    return root, sibling, ["--config", str(config), "--mech", f"Sibling={sibling}"]


@pytest.mark.parametrize("payload", ["", "<html>maintenance</html>", "Entry\tEntry\n"])
def test_fetchers_reject_invalid_response_headers(payload):
    with pytest.raises(ValueError, match="headers"):
        cross.fetch_sgd_uniprot_map(lambda _: payload)
    with pytest.raises(ValueError, match="headers"):
        cross.fetch_uniprot_annotations(["P0A749"], fetch=lambda _: payload)


@pytest.mark.parametrize("row", ["P10614\n", "P10614\tS000001049\textra\n",
                                  "invalid\tS000001049\n", "P10614\tbad-sgd\n"])
def test_sgd_fetch_rejects_invalid_rows(row):
    with pytest.raises(ValueError):
        cross.fetch_sgd_uniprot_map(lambda _: "Entry\tSGD\n" + row)


def test_valid_header_only_responses_preserve_unknown_coverage():
    assert cross.fetch_sgd_uniprot_map(lambda _: "Entry\tSGD\n") == {}
    assert cross.fetch_uniprot_annotations(["P0A749"], fetch=lambda _: HEADERS) == {}


@pytest.mark.parametrize("mapping", [
    {"SGD:S000001049": "P10614"}, {"SGD:S000001049": ["P"]},
    {"wrong-id": ["P10614"]},
])
def test_index_refuses_malformed_sgd_mapping(mapping):
    with pytest.raises(ValueError, match="SGD-to-UniProt"):
        cross.build_pathway_index([PATHWAY], mapping)


@pytest.mark.parametrize("mapping", [
    {"P0A749": {"rhea": "RHEA:18681"}}, {"P0A749": "malformed"},
    {"P0A749": {"rhea": ["not-a-reaction"]}},
])
def test_index_refuses_malformed_annotation_mapping(mapping):
    with pytest.raises(ValueError, match="annotation mapping"):
        cross.build_pathway_index([PATHWAY], annotations=mapping)


@pytest.mark.parametrize("kind", ["sgd", "annotations"])
def test_failed_fetch_preserves_explicit_cache_and_report(tmp_path, monkeypatch, kind):
    root, _, args = cli_fixture(tmp_path)
    cache = tmp_path / "input.json"
    cache.write_text(json.dumps({"SGD:S000001049": ["P10614"]} if kind == "sgd"
                                else {"P0A749": {"rhea": ["RHEA:18681"]}}))
    prior = cache.read_bytes()
    output = tmp_path / "report"
    output.mkdir()
    (output / "summary.md").write_text("previous report\n")
    if kind == "sgd":
        fetch = cross.fetch_sgd_uniprot_map
        monkeypatch.setattr(cross, "fetch_sgd_uniprot_map",
                            lambda: fetch(lambda _: "<html>maintenance</html>"))
        args += ["--sgd-map", str(cache), "--fetch-sgd-map"]
    else:
        fetch = cross.fetch_uniprot_annotations
        monkeypatch.setattr(cross, "fetch_uniprot_annotations",
                            lambda ids: fetch(ids, fetch=lambda _: "<html>maintenance</html>"))
        args += ["--annotations", str(cache), "--fetch-annotations"]
    with pytest.raises(SystemExit) as error:
        cross.main([*args, "--out", str(output)], root)
    assert error.value.code == 2
    assert cache.read_bytes() == prior
    assert list(output.iterdir()) == [output / "summary.md"]
    assert (output / "summary.md").read_text() == "previous report\n"


def test_annotation_late_batch_failure_is_not_partial_success():
    replies = iter([HEADERS + "P0A749\treviewed\t83333\t\t\t\n", "<html>error</html>"])
    with pytest.raises(ValueError, match="headers"):
        cross.fetch_uniprot_annotations(["P0A749", "P10614"], fetch=lambda _: next(replies),
                                       batch=1)


@pytest.mark.parametrize("use_git", [False, True])
def test_zero_selected_files_are_incomplete(tmp_path, use_git):
    if use_git:
        for args in [("init", "-q"), ("-c", "user.name=Test", "-c",
                     "user.email=test@example.invalid", "commit", "--allow-empty", "-qm", "empty")]:
            subprocess.run(["git", "-C", str(tmp_path), *args], check=True)
    coverage = cross.ScanCoverage()
    _, _, errors = cross.scan_sibling(tmp_path, cross.MechSpec("Sibling", ["data/*.yaml"]),
                                     ref="HEAD" if use_git else None, coverage=coverage)
    assert errors and "no records match" in errors[0]
    assert coverage.status == "incomplete"
    assert coverage.files_seen == 0


def test_empty_pathway_cohort_is_an_error(tmp_path):
    root, _, args = cli_fixture(tmp_path)
    (root / "data/pathways/record.yaml").unlink()
    with pytest.raises(SystemExit) as error:
        cross.main([*args, "--check-links"], root)
    assert error.value.code == 2


def test_incomplete_scan_does_not_replace_refreshed_cache_or_reports(tmp_path, monkeypatch):
    root, sibling, args = cli_fixture(tmp_path)
    (sibling / "record.yaml").unlink()
    cache = tmp_path / "sgd.json"
    cache.write_text('{"SGD:S000001049": ["P10614"]}\n')
    prior = cache.read_bytes()
    monkeypatch.setattr(cross, "fetch_sgd_uniprot_map", lambda: {})
    output = tmp_path / "report"
    output.mkdir()
    (output / "summary.md").write_text("previous report\n")
    assert cross.main([*args, "--check-links", "--sgd-map", str(cache), "--fetch-sgd-map",
                       "--out", str(output)], root) == 1
    assert cache.read_bytes() == prior
    assert (output / "summary.md").read_text() == "previous report\n"
    assert list(output.iterdir()) == [output / "summary.md"]


@pytest.mark.parametrize("target", [None, "", [], 42])
def test_selected_link_requires_nonempty_string_target(tmp_path, target):
    (tmp_path / "record.yaml").write_text(yaml.safe_dump({"related_records": [
        {"corpus": "PathwayMech", "identifier": target},
    ]}))
    spec = cross.MechSpec("Sibling", ["*.yaml"], link_slots=[
        cross.SlotSpec("related_records[]", id_key="identifier", when={"corpus": "PathwayMech"}),
    ])
    _, links, errors = cross.scan_sibling(tmp_path, spec)
    assert not links
    assert errors and "nonempty string target" in errors[0]


@pytest.mark.parametrize("prefilter", [False, True])
def test_wrong_case_stray_url_is_detected_as_broken(tmp_path, prefilter):
    url = cross.record_url("GO:42").replace("/PathwayMech/", "/pathwaymech/")
    (tmp_path / "record.yaml").write_text(yaml.safe_dump({"notes": url}))
    scan = cross.scan_sibling(tmp_path, cross.MechSpec("Sibling", ["*.yaml"], prefilter=prefilter))
    report = cross.build_report(cross.build_pathway_index([PATHWAY]), {"Sibling": scan})
    assert len(report.link_checks) == 1
    assert report.link_checks[0]["status"] == "unknown_record"


def test_pinned_blob_reader_preserves_duplicate_blobs_and_unusual_paths(tmp_path):
    names = ["data/a.yaml", "data/nested/tab\tline\ncopy.yaml"]
    payload = b"identifier: same-record\n"
    for name in names:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    for args in [("init", "-q"), ("add", "."), ("-c", "user.name=Test", "-c",
                 "user.email=test@example.invalid", "commit", "-qm", "pinned records")]:
        subprocess.run(["git", "-C", str(tmp_path), *args], check=True)
    for name in names:
        (tmp_path / name).write_text("working tree changed\n")
    spec = cross.MechSpec("Sibling", ["data/**/*.yaml"])
    actual = list(cross.git_documents(tmp_path, "HEAD", spec))
    assert actual == [(name, payload) for name in names]
