"""Synthetic page fixtures exercise the parser; they are never authority inputs."""

from __future__ import annotations

import hashlib
import html
import io
import json
import sys
import tarfile
from pathlib import Path

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from pathwaymech.kgx import kgx_nodes
from pathwaymech.schema import ValidationError, validate_record
from pathwaymech.strict import strict_errors
from scripts.build_source_identifier_snapshot import (
    build_snapshot,
    main,
    metanetx_chemical_terms,
    source_terms,
)

URL = "https://www.metanetx.org/chem_info/MNXM999999"
CURIE = "metanetx.chemical:MNXM999999"
LABEL = "a generic (S)-carrier state(2-)"


def entity(**changes):
    return {
        "@context": "https://schema.org",
        "@type": "MolecularEntity",
        "@id": URL,
        "identifier": CURIE,
        "url": URL,
        "name": LABEL,
        "alternateName": ["Conflicting upstream name"],
        "sameAs": ["https://identifiers.org/seed.compound:cpd99999"],
        **changes,
    }


def native(value=None, heading=LABEL, visible="MNXM999999"):
    return (
        '<html><script type="application/ld+json">'
        + json.dumps(entity() if value is None else value)
        + "</script><h1>"
        + html.escape(heading)
        + "</h1><table><tr><td>MNX_ID</td><td><span>"
        + visible
        + '</span></td><td><img alt="Not an identifier"></td></tr></table></html>'
    )


def test_identity_name_and_visible_page_agree_without_aliases():
    assert metanetx_chemical_terms(native(), URL) == [(CURIE, LABEL, [])]
    text = native(entity(name="test & carrier"), heading="test & carrier")
    assert metanetx_chemical_terms(text, URL) == [(CURIE, "test & carrier", [])]


def test_complete_unrelated_table_preserves_native_identity():
    text = native() + "<table><tr><td>Note</td><td>Native source</td></tr></table>"
    assert metanetx_chemical_terms(text, URL) == [(CURIE, LABEL, [])]


@pytest.mark.parametrize(
    "unfinished",
    [
        "<table><tr><td>MNX_ID</td><td>MNXM999998",
        "<table><tr><td>MNX_ID</td><td>MNXM999998</td>",
        "<table><tr><td>MNX_ID</td><td>MNXM999998</tr>",
        "<table><tr><td>MNX_ID</td><td>MNXM999999</td>",
        "<table><tr><td>Note</td><td>Unfinished",
    ],
)
def test_unfinished_visible_table_state_is_rejected(unfinished):
    with pytest.raises(ValueError, match="unfinished identity surface"):
        metanetx_chemical_terms(native() + unfinished, URL)


@pytest.mark.parametrize(
    "changes",
    [
        {"@type": "ChemicalSubstance"},
        {"@type": ["MolecularEntity", "Thing"]},
        {"@context": "http://example.org"},
        {"identifier": "MetaNetX:MNXM999999"},
        {"identifier": "metanetx.chemical:MNXM999998"},
        {"identifier": [CURIE]},
        {"@id": "https://beta.metanetx.org/chem_info/MNXM999999"},
        {"url": URL + "?redirect=1"},
        {"name": ""},
        {"name": "   "},
        {"name": "MNXM999999"},
        {"name": CURIE},
        {"name": "Unknown compound"},
        {"name": "Error: not found"},
        {"name": [LABEL]},
        {"name": None},
    ],
)
def test_inconsistent_or_unresolved_native_objects_are_rejected(changes):
    with pytest.raises(ValueError, match="MetaNetX"):
        metanetx_chemical_terms(native(entity(**changes)), URL)


@pytest.mark.parametrize(
    "url",
    [
        "https://beta.metanetx.org/chem_info/MNXM999999",
        "http://www.metanetx.org/chem_info/MNXM999999",
        "https://metanetx.org/chem_info/MNXM999999",
        "https://www.metanetx.org.evil/chem_info/MNXM999999",
        "https://www.metanetx.org/chem_info/MNXR999999",
        URL + "/",
        URL + "?x=1",
        URL + "#x",
        URL.replace("999999", "１２３"),
        URL.replace("MNXM", "mnxm"),
        "",
    ],
)
def test_only_exact_production_chemical_urls_are_supported(url):
    with pytest.raises(ValueError, match="MetaNetX"):
        metanetx_chemical_terms(native(), url)


@pytest.mark.parametrize(
    "body",
    [
        "",
        "<h1>Sign in</h1>",
        "<h1>Not found</h1>",
        native().replace('"name":', '"name": "First", "name":'),
        native().replace('"name":', '"name": invalid,'),
        native([entity(), entity()]),
        native({"@graph": [entity(), entity()]}),
        native().replace("</html>", native()),
        native(heading="Wrong name"),
        native(visible="MNXM999998"),
        native().replace("<h1>", "<h1>Other</h1><h1>"),
        native().replace("</table>", "<tr><td>MNX_ID</td><td>MNXM999999</td></tr></table>"),
        native().replace("MNX_ID", "Upstream ID"),
        native().replace("</h1>", ""),
        native().replace("</script>", ""),
        native({"@type": "Thing"}),
    ],
)
def test_missing_duplicate_or_disagreeing_surfaces_fail_closed(body):
    with pytest.raises(ValueError, match="MetaNetX"):
        metanetx_chemical_terms(body, URL)


def test_source_kind_requires_url_and_emits_only_native_curie(tmp_path):
    path = tmp_path / "unrelated-name.html"
    path.write_text(native())
    assert list(source_terms("metanetx-chemical-html", path, url=URL)) == [(CURIE, LABEL, [])]
    with pytest.raises(ValueError, match="MetaNetX"):
        list(source_terms("metanetx-chemical-html", path))


def fixture(tmp_path):
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    record_path = records / "fixture.yaml"
    record_path.write_text(yaml.safe_dump({"id": CURIE, "label": "Curator name"}))
    source = tmp_path / "original.html"
    source.write_text(native())
    entries = [
        {
            "key": "native",
            "kind": "metanetx-chemical-html",
            "path": source.name,
            "url": URL,
            "version": "synthetic fixture",
            "license": "synthetic fixture",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        }
    ]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return manifest, records, record_path, source, entries


def test_native_name_is_independent_of_curator_and_upstream_labels(tmp_path):
    manifest, records, _, _, _ = fixture(tmp_path)
    result = build_snapshot(manifest, records, tmp_path)
    assert result["terms"] == {CURIE: {"label": LABEL, "synonyms": [], "source": "native"}}
    assert "Curator name" not in json.dumps(result)
    assert "ModelSEED" not in json.dumps(result)


def test_other_sources_cannot_supply_native_metanetx_authority(tmp_path):
    manifest, records, _, _, entries = fixture(tmp_path)
    source = tmp_path / "gocam.tar.gz"
    body = json.dumps({"id": CURIE, "annotations": [{"key": "title", "value": LABEL}]}).encode()
    with tarfile.open(source, "w:gz") as archive:
        member = tarfile.TarInfo("source.json")
        member.size = len(body)
        archive.addfile(member, io.BytesIO(body))
    manifest.write_text(
        json.dumps(
            [
                {
                    **entries[0],
                    "kind": "gocam-tar",
                    "path": source.name,
                    "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                }
            ]
        )
    )
    with pytest.raises(ValueError, match="require native chemical HTML"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
def test_conflicting_names_reject_both_orders_even_before_selection(tmp_path, selected, reverse):
    manifest, records, record, _, entries = fixture(tmp_path)
    if not selected:
        record.write_text("id: metanetx.chemical:MNXM1\nlabel: Not selected\n")
    second = tmp_path / "second.html"
    second.write_text(native(entity(name="Changed name"), heading="Changed name"))
    entries.append(
        {
            **entries[0],
            "key": "second",
            "path": second.name,
            "sha256": hashlib.sha256(second.read_bytes()).hexdigest(),
        }
    )
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    with pytest.raises(ValueError, match="conflicting MetaNetX native names"):
        build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize(
    "problem",
    ["digest", "unselected-id", "bad-page", "wrong-url", "unfinished-cell", "unfinished-row"],
)
def test_failed_build_preserves_previous_output(tmp_path, monkeypatch, problem):
    manifest, records, record, source, entries = fixture(tmp_path)
    if problem == "digest":
        source.write_text(native() + "changed bytes")
    elif problem == "unselected-id":
        record.write_text("id: metanetx.chemical:MNXM1\nlabel: Unresolved\n")
    elif problem == "bad-page":
        source.write_text("<h1>Sign in</h1>")
        entries[0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    elif problem.startswith("unfinished-"):
        ending = "</td>" if problem == "unfinished-row" else ""
        source.write_text(native() + "<table><tr><td>MNX_ID</td><td>MNXM999998" + ending)
        entries[0]["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    else:
        entries[0]["url"] = URL + "?x=1"
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "snapshot.json"
    output.write_bytes(b"reviewed prior snapshot\n")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "builder",
            "--manifest",
            str(manifest),
            "--records",
            str(records),
            "--cache-dir",
            str(tmp_path),
            "--output",
            str(output),
        ],
    )
    with pytest.raises(ValueError):
        main()
    assert output.read_bytes() == b"reviewed prior snapshot\n"


def test_adding_native_source_preserves_prior_selected_terms_and_metadata(tmp_path):
    manifest, records, record, source, entries = fixture(tmp_path)
    baseline = build_snapshot(manifest, records, tmp_path)
    other_url = URL.replace("999999", "999998")
    other_id = CURIE.replace("999999", "999998")
    other = tmp_path / "other.html"
    other.write_text(native().replace("999999", "999998"))
    record.write_text(yaml.safe_dump({"id": CURIE, "participants": [{"id": other_id}]}))
    entries.append(
        {
            **entries[0],
            "key": "other",
            "path": other.name,
            "url": other_url,
            "sha256": hashlib.sha256(other.read_bytes()).hexdigest(),
        }
    )
    manifest.write_text(json.dumps(entries))
    expanded = build_snapshot(manifest, records, tmp_path)
    assert expanded["terms"][CURIE] == baseline["terms"][CURIE]
    assert expanded["sources"]["native"] == baseline["sources"]["native"]
    assert set(expanded["terms"]) == {CURIE, other_id}
    assert hashlib.sha256(source.read_bytes()).hexdigest() == entries[0]["sha256"]


@pytest.mark.parametrize(
    "problem,code",
    [
        (None, None),
        ("missing", "ID_NOT_FOUND"),
        ("alias", "LABEL_MISMATCH"),
        ("context", "LABEL_AUTHORITY_UNAVAILABLE"),
    ],
)
def test_native_policy_requires_canonical_authority_without_waiver(tmp_path, problem, code):
    manifest, records, record_path, _, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    record = {"id": CURIE, "label": LABEL, "taxa": [], "participants": [], "reactions": []}
    if problem == "missing":
        record["id"] = "metanetx.chemical:MNXM1"
    elif problem == "alias":
        record["label"] = "Conflicting upstream name"
    elif problem == "context":
        snapshot["terms"][CURIE]["label_kind"] = "source_context"
    record_path.write_text(yaml.safe_dump(record))
    policy = yaml.safe_load(Path("conf/identifier_policy.yaml").read_text())
    assert policy["namespaces"]["metanetx.chemical"]["policy"] == "canonical"
    assert not any(x["namespace"] == "metanetx.chemical" for x in policy["contextual_labels"])
    policy["namespaces"] = {"metanetx.chemical": policy["namespaces"]["metanetx.chemical"]}
    policy["contextual_labels"] = []
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(snapshot))
    errors = identifier_errors(tmp_path)
    assert any(code in error for error in errors) if code else errors == []


@pytest.mark.parametrize(
    "prefix,valid",
    [
        ("metanetx.chemical", True),
        ("metanetxXchemical", False),
    ],
)
def test_both_schemas_preserve_exact_native_namespace_and_generic_kgx_kind(tmp_path, prefix, valid):
    path = next(Path("data/pathways").glob("*.yaml"))
    record = yaml.safe_load(path.read_text())
    identifier = prefix + ":MNXM999999"
    record["participants"].append({"id": identifier, "label": LABEL})
    target = tmp_path / "record.yaml"
    target.write_text(yaml.safe_dump(record))
    if valid:
        model = validate_record(record)
        assert strict_errors([target], tmp_path) == []
        row = next(node for node in kgx_nodes([model]) if node.id == identifier)
        assert row.category == "biolink:ChemicalEntity"
        assert row.name == LABEL
    else:
        with pytest.raises(ValidationError, match="unsupported prefix"):
            validate_record(record)
        assert strict_errors([target], tmp_path)
