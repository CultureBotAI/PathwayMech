"""A dated audit must survive later committed and uncommitted input changes."""

import os
import runpy
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/cross_mech/2026-10-05/reproduce.py"
load_audit_inputs = runpy.run_path(str(SCRIPT))["load_audit_inputs"]


def git(root, *args):
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    return subprocess.check_output(
        ["git", "-C", str(root), "-c", "user.name=Audit test",
         "-c", "user.email=audit@example.invalid", *args],
        env=env, text=True,
    ).strip()


@pytest.fixture
def audit_repo(tmp_path):
    git(tmp_path, "init", "-q", "-b", "main")
    files = {
        "data/pathways/example.yaml": "id: GO:1\nlabel: Original pathway\n",
        "conf/sibling_mechs.yaml": (
            "version: 1\nmechs:\n  ExampleMech:\n"
            "    records: data/traits/**/*.yaml\n    protein_slots: []\n"
        ),
        "research/cross_mech/2026-10-05/inputs/sgd_uniprot.json": '{"SGD:S000000001": ["P12345"]}',
        "research/cross_mech/2026-10-05/inputs/uniprot_annotations.json": (
            '{"P12345": {"ec": ["1.1.1.1"], "rhea": []}}'
        ),
    }
    for name, content in files.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    shutil.copy(ROOT / "conf/rhea_directions.json", tmp_path / "conf/rhea_directions.json")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "-qm", "Original audit inputs")
    return tmp_path, git(tmp_path, "rev-parse", "HEAD")


def test_audit_inputs_ignore_new_head_and_dirty_worktree(audit_repo):
    root, original = audit_repo
    expected = load_audit_inputs(root, original)
    assert expected[0][0]["label"] == "Original pathway"
    for path in root.rglob("*"):
        if path.is_file() and ".git" not in path.relative_to(root).parts:
            path.write_text("invalid newer committed input")
    git(root, "add", ".")
    git(root, "commit", "-qm", "Later curation and input changes")
    assert git(root, "rev-parse", "HEAD") != original
    assert load_audit_inputs(root, original) == expected
    (root / "data/pathways/example.yaml").write_text("id: GO:2\nlabel: Dirty pathway\n")
    (root / "conf/sibling_mechs.yaml").write_text("dirty configuration")
    assert load_audit_inputs(root, original) == expected


@pytest.mark.parametrize("content", ["[]\n", "not a mapping\n"])
def test_audit_rejects_non_mapping_records(audit_repo, content):
    root, _ = audit_repo
    (root / "data/pathways/example.yaml").write_text(content)
    git(root, "add", ".")
    git(root, "commit", "-qm", "Malformed record")
    with pytest.raises(ValueError, match="YAML mapping"):
        load_audit_inputs(root, "HEAD")


def test_audit_rejects_empty_record_selection(audit_repo):
    root, _ = audit_repo
    git(root, "rm", "data/pathways/example.yaml")
    git(root, "commit", "-qm", "No records")
    with pytest.raises(ValueError, match="No PathwayMech records"):
        load_audit_inputs(root, "HEAD")


def test_replay_entrypoint_uses_frozen_config_and_evidence(audit_repo, monkeypatch):
    root, original = audit_repo
    replay = runpy.run_path(str(SCRIPT))
    main = replay["main"]
    namespace = main.__globals__
    loader = namespace["load_audit_inputs"]
    monkeypatch.setitem(namespace, "load_audit_inputs", lambda path: loader(path, original))
    monkeypatch.setitem(namespace, "__file__",
                        str(root / "research/cross_mech/2026-10-05/reproduce.py"))
    monkeypatch.setitem(namespace, "PINS", {"ExampleMech": original})
    seen_specs = []

    def scan(root, spec, **kwargs):
        seen_specs.append(spec)
        return [], [], []

    monkeypatch.setitem(namespace, "scan_sibling", scan)
    monkeypatch.setitem(namespace, "write_report", lambda *args: [])
    monkeypatch.setattr("sys.argv", ["reproduce.py", "--mechs-root", str(root)])
    for name in ["conf/sibling_mechs.yaml", "conf/rhea_directions.json",
                 "research/cross_mech/2026-10-05/inputs/sgd_uniprot.json",
                 "research/cross_mech/2026-10-05/inputs/uniprot_annotations.json"]:
        (root / name).write_text("invalid dirty input")
    main()
    assert [spec.name for spec in seen_specs] == ["ExampleMech"]
    assert seen_specs[0].records == ["data/traits/**/*.yaml"]
