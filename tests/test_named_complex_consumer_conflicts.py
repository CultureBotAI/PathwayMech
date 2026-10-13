"""Issue 500: full native assembly assertions agree before term selection."""

from __future__ import annotations

import copy

import pytest
from test_nitrate_native_authority import PATHWAY, build, consume, item, original

from pathwaymech.ecocyc_named_complex import named_complex_metadata

NARA = "EcoCyc:NITRATREDUCTA-CPLX"


def alternate(tmp_path, change):
    root = original(NARA)
    if change == "coefficient":
        root[1].find("component/coefficient").text = "1"
    elif change == "GO_evidence_context":
        root[1].find("has-go-term/evidence/with").text = "conflicting retained evidence"
    elif change == "version":
        root.set("ptools-version", "26.0")
        root.find("metadata/PGDB").set("version", "26.0")
    entry = item(tmp_path, NARA, root, "alternate-" + change)
    if change == "version":
        entry["version"] = "26.0"
    return entry


def pair(tmp_path, change, reverse, selected):
    base = item(tmp_path, NARA)
    changed = alternate(tmp_path, change)
    entries = [base, changed]
    if reverse:
        entries.reverse()
    # Each original is independently well formed, including the version variant.
    metadata = {e["key"]: named_complex_metadata(e, tmp_path) for e in entries}
    if selected:
        data = build(tmp_path, [entries[0]], [NARA])
        data["sources"] = metadata
        wanted = [NARA]
    else:
        anchor = item(tmp_path, PATHWAY)
        data = build(tmp_path, [anchor], [PATHWAY])
        data["sources"].update(metadata)
        wanted = [PATHWAY]
        entries.append(anchor)
        assert all(t["source"] not in metadata for t in data["terms"].values())
    return entries, data, wanted


@pytest.mark.parametrize("change", ["coefficient", "GO_evidence_context", "version"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_consumer_rejects_the_same_complete_assertion_conflicts_as_producer(
    tmp_path, change, reverse, selected
):
    entries, data, wanted = pair(tmp_path, change, reverse, selected)
    with pytest.raises(ValueError, match="conflicting native identity/context assertions"):
        build(tmp_path, entries, wanted)
    with pytest.raises(ValueError, match="conflicting typed native named-complex assertions"):
        consume(tmp_path, copy.deepcopy(data))


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
def test_identical_complete_assertions_allow_duplicate_unselected_owners(
    tmp_path, reverse, selected
):
    entries, data, wanted = pair(tmp_path, "identical", reverse, selected)
    assert consume(tmp_path, copy.deepcopy(data)) == data["terms"]
    built = build(tmp_path, entries, wanted)
    assert consume(tmp_path, built) == built["terms"]
    if selected:
        assert built["terms"][NARA]["source"] == entries[0]["key"]
        assert data["terms"][NARA]["source"] == entries[0]["key"]
    else:
        assert NARA not in built["terms"]
        assert NARA not in data["terms"]
