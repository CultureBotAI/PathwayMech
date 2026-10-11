"""Retention must never redirect writes through a symbolic ref to another branch."""

import subprocess

import pytest

from scripts import fetch_review_revisions as fetcher


@pytest.fixture
def repository(tmp_path):
    root = tmp_path.resolve()
    fetcher.git(root, "init", "-b", "main")
    fetcher.git(root, "config", "user.name", "Ref fixture")
    fetcher.git(root, "config", "user.email", "fixture@example.invalid")
    (root / "data.txt").write_text("first\n")
    fetcher.git(root, "add", "data.txt")
    fetcher.git(root, "commit", "-m", "First")
    revision = fetcher.git(root, "rev-parse", "HEAD").stdout.strip()
    (root / "data.txt").write_text("second\n")
    fetcher.git(root, "commit", "-am", "Second")
    other = fetcher.git(root, "rev-parse", "HEAD").stdout.strip()
    return root, revision, other


@pytest.mark.parametrize("target_state", ["dangling", "same", "other"])
def test_existing_symbolic_refs_reject_without_ref_or_network_changes(
    repository, monkeypatch, target_state,
):
    root, revision, other = repository
    ref = f"refs/record-reviews/{revision}"
    target = "refs/heads/unrelated"
    if target_state != "dangling":
        fetcher.git(root, "update-ref", target, revision if target_state == "same" else other)
    fetcher.git(root, "symbolic-ref", ref, target)
    before = fetcher.git(root, "for-each-ref", "--format=%(refname) %(objectname)").stdout
    original = fetcher.git

    def no_fetch(root, *args, **kwargs):
        assert args[0] != "fetch", "Symbolic ref must be rejected before fetching"
        return original(root, *args, **kwargs)

    monkeypatch.setattr(fetcher, "git", no_fetch)
    with pytest.raises(ValueError, match="symbolic"):
        fetcher.restore_revisions(root, [revision], fetcher.FETCH_URL)
    assert fetcher.git(root, "for-each-ref", "--format=%(refname) %(objectname)").stdout == before
    assert fetcher.git(root, "symbolic-ref", ref).stdout.strip() == target


@pytest.mark.parametrize("existing_direct_ref", [False, True])
@pytest.mark.parametrize("target_state", ["dangling", "same", "other"])
def test_symbolic_substitution_at_update_cannot_mutate_unrelated_target(
    repository, monkeypatch, existing_direct_ref, target_state,
):
    root, revision, other = repository
    ref = f"refs/record-reviews/{revision}"
    target = "refs/heads/unrelated"
    if existing_direct_ref:
        fetcher.git(root, "update-ref", ref, revision)
    if target_state != "dangling":
        fetcher.git(root, "update-ref", target, revision if target_state == "same" else other)
    before = fetcher.git(root, "show-ref", "--verify", target, check=False)
    original = fetcher.git
    substituted = False

    def substitute(root, *args, **kwargs):
        nonlocal substituted
        if args[0] == "update-ref":
            assert not substituted
            original(root, "symbolic-ref", ref, target)
            substituted = True
        return original(root, *args, **kwargs)

    monkeypatch.setattr(fetcher, "git", substitute)
    try:
        fetcher.restore_revisions(root, [revision], fetcher.FETCH_URL)
    except subprocess.CalledProcessError:
        pass  # A compare-and-swap conflict is an acceptable safe outcome.
    else:
        assert original(root, "symbolic-ref", "--quiet", ref, check=False).returncode != 0
        assert original(root, "rev-parse", ref).stdout.strip() == revision
    assert substituted
    after = original(root, "show-ref", "--verify", target, check=False)
    assert (after.returncode, after.stdout) == (before.returncode, before.stdout)
