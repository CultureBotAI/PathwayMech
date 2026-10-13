"""Whole valid HTML claims must not evade the carrier preselection boundary."""

from __future__ import annotations

import copy
import hashlib

import pytest
from test_protein_carrier_reaction_authority import (
    IDENT,
    build,
    consume,
    item,
    original,
    unrelated,
)

from pathwaymech.biocyc_carrier import HOST
from pathwaymech.biocyc_protein_carrier_reaction import (
    carrier_reaction_metadata,
    carrier_reaction_term,
)
from scripts.build_source_identifier_snapshot import source_terms


def html_entry(tmp_path, ident=IDENT, route="metacyc"):
    frame = ident.split(":", 1)[1]
    body = (
        "<HTML><TITLE>MetaCyc test native reaction label</TITLE><SCRIPT>"
        f"typeObjectPage={{object:'{frame}',orgid:'META',type:'Reactions'}};"
        "</SCRIPT></HTML>"
    ).encode()
    if route == "opaque":
        # The existing profile establishes identity from the body, not this URL.
        url = "https://metacyc.org/META/NEW-IMAGE?type=REACTION"
    else:
        host = "www.metacyc.org" if route == "www-metacyc" else "metacyc.org"
        url = f"https://{host}/META/NEW-IMAGE?type=REACTION&object={frame}"
    entry = {
        "key": "ordinary-html",
        "kind": "metacyc-html",
        "path": "protected.html",
        "url": url,
        "version": "27.0",
        "license": "synthetic-test-only",
        "sha256": hashlib.sha256(body).hexdigest(),
    }
    path = tmp_path / entry["path"]
    path.write_bytes(body)
    assert list(source_terms(entry["kind"], path, url=url, version="27.0")) == [
        (ident, "test native reaction label", [])
    ]
    return entry


@pytest.mark.parametrize("route", ["metacyc", "www-metacyc", "opaque"])
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("typed_present", [False, True])
def test_producer_whole_html_claim_before_selection(
    tmp_path, route, selected, reverse, typed_present
):
    bad = html_entry(tmp_path, route=route)
    control, other = unrelated(tmp_path)
    entries = [bad] + ([item(tmp_path)] if typed_present else []) + [control]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="complete typed scope"):
        build(tmp_path, entries, (IDENT, other) if selected else (other,))


@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("reverse", [False, True])
def test_dynamic_typed_identity_body_claim_before_selection(tmp_path, selected, reverse):
    ident = "MetaCyc:RXN-SYNTHETIC-CARRIER"
    root = original()
    for node in root.iter():
        for key, value in list(node.attrib.items()):
            node.set(key, value.replace("RXN-21320", "RXN-SYNTHETIC-CARRIER"))
        if node.text:
            node.text = node.text.replace("RXN-21320", "RXN-SYNTHETIC-CARRIER")
    typed = item(
        tmp_path,
        root,
        url="https://" + HOST + "/getxml?id=META:RXN-SYNTHETIC-CARRIER",
    )
    assert (
        carrier_reaction_metadata(typed, tmp_path)["native_protein_carrier_reaction"]["id"] == ident
    )
    bad = html_entry(tmp_path, ident, route="opaque")
    control, other = unrelated(tmp_path)
    entries = [bad, typed, control]
    if reverse:
        entries.reverse()
    with pytest.raises(ValueError, match="complete typed scope"):
        build(tmp_path, entries, (ident, other) if selected else (other,))


HOST_ROUTES = [
    (host, "/META/NEW-IMAGE?type=REACTION&object=RXN-21320")
    for host in (HOST, "biocyc.org", "www.biocyc.org", "metacyc.org", "www.metacyc.org")
] + [
    ("metacyc.org", "/getxml?id=META:RXN-21320"),
    ("www.metacyc.org", "/getxml?orgid=META&id=RXN-21320"),
]


@pytest.mark.parametrize("host,route", HOST_ROUTES)
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("typed_present", [False, True])
def test_consumer_official_request_claim_before_terms(
    tmp_path, host, route, selected, reverse, typed_present
):
    entry = html_entry(tmp_path)
    metadata = {k: entry[k] for k in ("url", "version", "license", "sha256")}
    metadata["url"] = "https://" + host + route
    control, other = unrelated(tmp_path)
    data = build(tmp_path, [control], (other,))
    pairs = [("ordinary-html", metadata)]
    if typed_present:
        pairs.append(("mar", carrier_reaction_metadata(item(tmp_path), tmp_path)))
    if reverse:
        pairs.reverse()
    data["sources"].update(pairs)
    if selected:
        data["terms"][IDENT] = {
            "label": "test native reaction label",
            "synonyms": [],
            "source": "ordinary-html",
        }
    with pytest.raises(ValueError, match="complete typed scope"):
        consume(tmp_path, data)


@pytest.mark.parametrize("route", ["metacyc", "www-metacyc", "opaque"])
@pytest.mark.parametrize("selected", [False, True])
def test_other_native_html_identity_remains_accepted(tmp_path, route, selected):
    ident = "MetaCyc:RXN-SYNTHETIC-ORDINARY"
    entry = html_entry(tmp_path, ident, route=route)
    control, other = unrelated(tmp_path)
    data = build(tmp_path, [entry, control], (ident, other) if selected else (other,))
    assert consume(tmp_path, copy.deepcopy(data)) == data["terms"]
    assert (ident in data["terms"]) == selected


@pytest.mark.parametrize("route", ["metacyc", "www-metacyc"])
@pytest.mark.parametrize("reverse", [False, True])
def test_selected_typed_term_does_not_hide_unselected_html_owner(tmp_path, route, reverse):
    ordinary = html_entry(tmp_path, route=route)
    control, other = unrelated(tmp_path)
    data = build(tmp_path, [control], (other,))
    metadata = carrier_reaction_metadata(item(tmp_path), tmp_path)
    pairs = [
        ("mar", metadata),
        ("ordinary-html", {k: ordinary[k] for k in ("url", "version", "license", "sha256")}),
    ]
    if reverse:
        pairs.reverse()
    data["sources"].update(pairs)
    data["terms"][IDENT] = carrier_reaction_term(metadata, "mar")[1]
    with pytest.raises(ValueError, match="complete typed scope"):
        consume(tmp_path, data)
