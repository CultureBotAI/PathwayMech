"""Fresh clones must retain verifiable reviews after squash and branch deletion."""

from copy import deepcopy

import pytest

from scripts import fetch_review_revisions as fetcher


@pytest.fixture
def historical_clone(tmp_path):
    writer = (tmp_path / "writer").resolve()
    writer.mkdir()
    def run(*args):
        return fetcher.git(writer, *args).stdout.strip()
    run("init", "-b", "main")
    run("config", "user.name", "Review fixture")
    run("config", "user.email", "fixture@example.invalid")
    run("remote", "add", "origin", fetcher.FETCH_URL)
    (writer / "record.yaml").write_text("id: EX:base\n")
    run("add", "record.yaml")
    run("commit", "-m", "Base")
    run("checkout", "-b", "feature")
    (writer / "record.yaml").write_text("id: EX:fixture\n")
    run("commit", "-am", "Historical review source")
    revision = run("rev-parse", "HEAD")
    targets = [{"target_id": "EX:fixture", "path": "record.yaml", "label": "Fixture",
                "kind": "maintained", "ownership_note": "Synthetic fixture only."}]
    source = fetcher.record_review.inspect_source(writer, targets)["source"]
    source["state"] = "git_commit"
    review = {
        "schema_version": "1.0.0", "review_id": "20260101T000000Z-fetch-fixture",
        "kind": "record", "repository": fetcher.REPOSITORY, "title": "Synthetic fixture",
        "started_at": "2026-01-01T00:00:00Z", "finished_at": "2026-01-01T00:00:00Z",
        "reviewer": {"identity": "fixture", "kind": "deterministic",
                     "independence": "not_applicable", "independence_basis": "Synthetic only."},
        "skill": "contract-test", "completion": "completed", "verdict": "pass",
        "scientific_review": False, "summary": "Historical synthetic fixture inspected.",
        "source": source, "targets": targets,
        "scope": {"description": "Fixture only.", "selection": "Explicit fixture.",
                  "coverage": "full", "population_size": 1, "reviewed_target_ids": ["EX:fixture"]},
        "checks": [{"check_id": "id", "name": "Identity", "required": True, "status": "passed",
                    "summary": "Fixture inspected.", "target_ids": ["EX:fixture"],
                    "evidence_ids": ["fixture"]}],
        "evidence": [{"evidence_id": "fixture", "kind": "record_content",
                      "reference": "record.yaml",
                      "accessed_at": "2026-01-01T00:00:00Z", "support": "supports",
                      "summary": "Fixture declares EX:fixture."}],
        "assessments": [{"assessment_id": "id", "area": "identity", "topic": "Fixture",
                         "outcome": "supported", "summary": "Fixture ID inspected.",
                         "target_ids": ["EX:fixture"], "evidence_ids": ["fixture"]}],
        "findings": [], "actions": [], "limitations": [],
    }
    run("checkout", "main")
    path = fetcher.record_review.save_review(writer, review).relative_to(writer)
    run("add", "reviews")
    run("commit", "-m", "Retain historical review after squash")
    bare = (tmp_path / "remote.git").resolve()
    run("init", "--bare", str(bare))
    run("push", str(bare), "main:refs/heads/main", f"{revision}:refs/pull/1/head")
    run("branch", "-D", "feature")
    fresh = (tmp_path / "fresh").resolve()
    run("clone", "--no-local", "--single-branch", "--branch", "main", str(bare), str(fresh))
    fetcher.git(fresh, "remote", "set-url", "origin", fetcher.FETCH_URL)
    assert fetcher.git(fresh, "cat-file", "-t", revision, check=False).returncode != 0
    return fresh, bare, revision, str(path), review


def test_fresh_clone_restores_exact_commit_and_preserves_review(historical_clone):
    root, remote, revision, relative, review = historical_clone
    path = root / relative
    before = (path.read_bytes(), path.with_suffix(".md").read_bytes())
    head = fetcher.git(root, "rev-parse", "HEAD").stdout
    with pytest.raises(fetcher.record_review.ReviewError, match="unverified"):
        fetcher.record_review.read_review(root, relative)
    paths, revisions = fetcher.collect_revisions(root)
    assert paths == [relative] and revisions == [revision]
    assert fetcher.restore_revisions(root, revisions, str(remote)) == [revision]
    assert fetcher.record_review.read_review(root, relative) == review
    assert fetcher.restore_revisions(root, revisions, str(remote)) == []
    assert fetcher.git(root, "rev-parse", "HEAD").stdout == head
    assert before == (path.read_bytes(), path.with_suffix(".md").read_bytes())
    retained = fetcher.git(root, "rev-parse", f"refs/record-reviews/{revision}").stdout.strip()
    assert retained == revision
    # Retrieval must not weaken historical-byte verification.
    changed = deepcopy(review)
    changed["source"]["inputs"][0]["sha256"] = "0" * 64
    assert fetcher.record_review.source_provenance(root, changed)["status"] == "invalid"


def test_failed_fetch_does_not_succeed_or_create_ref(historical_clone):
    root, remote, _, _, _ = historical_clone
    revision = "1" * 40
    with pytest.raises(fetcher.subprocess.CalledProcessError):
        fetcher.restore_revisions(root, [revision], str(remote))
    assert fetcher.git(root, "rev-parse", "--verify", f"refs/record-reviews/{revision}",
                       check=False).returncode != 0


def test_noncommit_and_conflicting_retention_ref_fail(historical_clone):
    root, remote, revision, _, _ = historical_clone
    blob = fetcher.git(root, "rev-parse", "HEAD:record.yaml").stdout.strip()
    with pytest.raises(ValueError, match="not a commit"):
        fetcher.restore_revisions(root, [blob], str(remote))
    fetcher.git(root, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                "tag", "-a", "review-tag", "HEAD", "-m", "Must not accept a peeled tag")
    tag = fetcher.git(root, "rev-parse", "review-tag").stdout.strip()
    with pytest.raises(ValueError, match="not a commit"):
        fetcher.restore_revisions(root, [tag], str(remote))
    head = fetcher.git(root, "rev-parse", "HEAD").stdout.strip()
    ref = f"refs/record-reviews/{revision}"
    fetcher.git(root, "update-ref", ref, head)
    with pytest.raises(ValueError, match="retention ref disagrees"):
        fetcher.restore_revisions(root, [revision], str(remote))
    assert fetcher.git(root, "rev-parse", ref).stdout.strip() == head


@pytest.mark.parametrize("revision", ["HEAD", "--all", "a" * 39, "a" * 64, "A" * 40])
def test_invalid_revision_rejected_before_git(tmp_path, monkeypatch, revision):
    def forbidden(*args, **kwargs):
        pytest.fail("Git must not run for an invalid revision")
    monkeypatch.setattr(fetcher, "git", forbidden)
    with pytest.raises(ValueError, match="SHA-1"):
        fetcher.restore_revisions(tmp_path, [revision], fetcher.FETCH_URL)


@pytest.mark.parametrize("defect", ["foreign", "markdown", "revision", "origin"])
def test_all_pairs_validate_before_fetch(historical_clone, monkeypatch, defect):
    root, _, _, relative, review = historical_clone
    path = root / relative
    if defect == "markdown":
        path.with_suffix(".md").write_text("Mismatching review\n")
    elif defect == "origin":
        fetcher.git(root, "remote", "set-url", "origin", "https://github.com/Example/Other.git")
    else:
        changed = deepcopy(review)
        if defect == "foreign":
            changed["repository"] = "Example/Other"
        else:
            changed["source"]["git_revision"] = "a" * 64
        path.write_text(fetcher.record_review._dump_document(changed))
        path.with_suffix(".md").write_text(fetcher.record_review.render_markdown(changed))
    def forbidden(*args, **kwargs):
        pytest.fail("No fetch or ref mutation is allowed for invalid inputs")
    monkeypatch.setattr(fetcher, "restore_revisions", forbidden)
    assert fetcher.main(["--repo-root", str(root)]) == 1


def test_ignored_review_pair_is_included(historical_clone):
    root, _, revision, relative, _ = historical_clone
    fetcher.git(root, "rm", "--cached", "-r", "reviews")
    (root / ".gitignore").write_text("reviews/\n")
    assert fetcher.collect_revisions(root) == ([relative], [revision])
