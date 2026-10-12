"""Independent unnamed-reaction fixtures; original source replay is external."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.identifiers import identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot, main, source_terms

HOST = "bf2i-artsymbiocyc.insa-lyon.fr"
KIND = "metacyc-reaction-xml"
FRAME = "RXN-999991"
URL = f"https://{HOST}/getxml?id=META:{FRAME}"


def native(frame=FRAME):
    return ET.fromstring(f'''<ptools-xml ptools-version="27.0"
      xml:base="http://{HOST}:443/getxml?META:{frame}">
      <metadata><url>http://{HOST}:443/</url><service_name>getxml</service_name>
        <query>META:{frame}</query><num_results>1</num_results>
        <PGDB orgid="META" version="27.0"><species datatype="string">MetaCyc</species></PGDB>
      </metadata>
      <Reaction ID="META:{frame}" orgid="META" frameid="{frame}" detail="full">
        <parent><Reaction resource="getxml?META:Chemical-Reactions" orgid="META"
          frameid="Chemical-Reactions" class="true"/></parent>
        <parent><Reaction resource="getxml?META:Small-Molecule-Reactions" orgid="META"
          frameid="Small-Molecule-Reactions" class="true"/></parent>
        <left><Compound resource="getxml?META:CPD-LEFT" orgid="META" frameid="CPD-LEFT"/></left>
        <right><Compound resource="getxml?META:CPD-RIGHT" orgid="META" frameid="CPD-RIGHT"/></right>
        <reaction-direction>REVERSIBLE</reaction-direction><orphan>YES-PUTATIVE</orphan>
        <spontaneous datatype="boolean">true</spontaneous>
        <physiologically-relevant datatype="boolean">true</physiologically-relevant>
        <credits><Person><common-name datatype="string">A curator</common-name></Person></credits>
      </Reaction></ptools-xml>''')


def parse(tmp_path, root=None, *, url=URL, version="27.0", raw=None):
    path = tmp_path / "native.xml"
    body = raw if raw is not None else ET.tostring(native() if root is None else root)
    path.write_bytes(body)
    result = list(source_terms(KIND, path, url=url, version=version))
    assert path.read_bytes() == body
    return result


@pytest.mark.parametrize("frame", [FRAME, "OTHER-RXN", "Reaction_17.2"])
def test_unnamed_identity_has_no_accession_exception_or_nested_name(tmp_path, frame):
    assert parse(tmp_path, native(frame), url=URL.replace(FRAME, frame)) == [
        ("MetaCyc:" + frame, frame, []),
    ]


def test_native_declared_encoding_and_exact_https_serialization(tmp_path):
    root = native()
    root.find("Reaction/credits/Person/common-name").text = "Curateur André"
    root.set("{http://www.w3.org/XML/1998/namespace}base", URL)
    root.find("metadata/url").text = f"https://{HOST}/"
    assert parse(tmp_path, raw=ET.tostring(root, encoding="iso-8859-1")) == [
        ("MetaCyc:" + FRAME, FRAME, []),
    ]


@pytest.mark.parametrize("url", [
    "", URL.replace("https:", "http:"), URL.replace(HOST, "example.org"),
    URL.replace(HOST, HOST + ".example.org"), URL.replace(HOST, "user@" + HOST),
    URL.replace(HOST, HOST + ":443"), URL.replace("META:", "ECOLI:"),
    URL.replace(FRAME, "RXN-OTHER"), URL.replace("id=", ""), URL + "&detail=full",
    URL + "&id=META:" + FRAME, URL + "&id=", URL + "#fragment", URL + " ", URL + "\n",
    URL.replace("getxml", "META/NEW-IMAGE"), URL.replace("META:", "META%3A"),
    URL.replace(FRAME, "%52XN-999991"), URL.replace(FRAME, "bad:frame"),
    URL.replace(FRAME, "bad/frame"), URL.replace(FRAME, ""),
])
def test_exact_issuing_request_required(tmp_path, url):
    with pytest.raises(ValueError, match="MetaCyc reaction"):
        parse(tmp_path, url=url)


@pytest.mark.parametrize("problem", [
    "root-tag", "root-extra", "base-host", "base-frame", "base-port", "base-query", "software",
    "metadata-missing", "metadata-duplicate", "metadata-extra", "service", "query", "count",
    "pgdb-missing", "pgdb-duplicate", "pgdb-org", "pgdb-version", "pgdb-extra", "species",
    "reaction-missing", "reaction-duplicate", "extra-object", "nested-only", "wrong-object",
    "id", "frame", "organism", "detail", "class", "resource", "extra-attribute",
    "parent-missing", "parent-duplicate", "parent-type", "parent-reference", "parent-class",
    "left-missing", "right-empty", "left-extra", "left-wrong-object", "compound-id",
    "compound-org", "compound-resource", "compound-class", "compound-nested", "side-duplicate",
    "direction-missing", "direction-duplicate", "direction-invalid", "direction-nested",
    "name-valid", "name-empty", "name-duplicate", "name-nested-copy", "flag-duplicate",
    "flag-invalid", "flag-nested", "html",
])
def test_ambiguous_native_identity_and_side_serialization_fail(tmp_path, problem):
    root = native()
    meta, reaction = root.find("metadata"), root.find("Reaction")
    if problem == "root-tag":
        root.tag = "wrong"
    elif problem == "root-extra":
        root.set("unknown", "yes")
    elif problem.startswith("base-"):
        old = root.get("{http://www.w3.org/XML/1998/namespace}base")
        changes = {"base-host": (HOST, "example.org"), "base-frame": (FRAME, "OTHER"),
                   "base-port": (":443", ":8080"), "base-query": ("?META:", "?id=META:")}
        root.set("{http://www.w3.org/XML/1998/namespace}base", old.replace(*changes[problem]))
    elif problem == "software":
        root.set("ptools-version", "99.0")
    elif problem in {"metadata-missing", "metadata-duplicate", "metadata-extra"}:
        if problem == "metadata-missing":
            root.remove(meta)
        elif problem == "metadata-duplicate":
            root.append(copy.deepcopy(meta))
        else:
            ET.SubElement(meta, "extra").text = "value"
    elif problem in {"service", "query", "count"}:
        tag = {"service": "service_name", "query": "query", "count": "num_results"}[problem]
        meta.find(tag).text = "invalid"
    elif problem.startswith("pgdb-") or problem == "species":
        pgdb = meta.find("PGDB")
        if problem == "pgdb-missing":
            meta.remove(pgdb)
        elif problem == "pgdb-duplicate":
            meta.append(copy.deepcopy(pgdb))
        elif problem == "pgdb-org":
            pgdb.set("orgid", "ECOLI")
        elif problem == "pgdb-version":
            pgdb.set("version", "99.0")
        elif problem == "pgdb-extra":
            ET.SubElement(pgdb, "strain").text = "MG1655"
        else:
            pgdb.find("species").text = "Escherichia coli"
    elif problem == "reaction-missing":
        root.remove(reaction)
    elif problem == "reaction-duplicate":
        root.append(copy.deepcopy(reaction))
    elif problem == "extra-object":
        ET.SubElement(root, "Protein")
    elif problem == "nested-only":
        root.remove(reaction)
        ET.SubElement(root, "wrapper").append(reaction)
    elif problem == "wrong-object":
        reaction.tag = "Protein"
    elif problem in {"id", "frame", "organism", "detail", "class", "resource", "extra-attribute"}:
        key = {"id": "ID", "frame": "frameid", "organism": "orgid",
               "detail": "detail", "class": "class", "resource": "resource",
               "extra-attribute": "other"}[problem]
        reaction.set(key, "true" if key == "class" else "wrong")
    elif problem.startswith("parent-"):
        parent = reaction.find("parent")
        child = parent.find("Reaction")
        if problem == "parent-missing":
            reaction.remove(parent)
        elif problem == "parent-duplicate":
            reaction.append(copy.deepcopy(parent))
        elif problem == "parent-type":
            child.tag = "Protein"
        elif problem == "parent-reference":
            child.set("resource", "getxml?ECOLI:Chemical-Reactions")
        else:
            child.set("class", "false")
    elif problem.startswith(("left-", "right-", "compound-", "side-")):
        slot = reaction.find("right" if problem == "right-empty" else "left")
        compound = slot.find("Compound")
        if problem == "left-missing":
            reaction.remove(slot)
        elif problem == "right-empty":
            slot.remove(compound)
        elif problem == "left-extra":
            ET.SubElement(slot, "coefficient").text = "2"
        elif problem == "left-wrong-object":
            compound.tag = "Protein"
        elif problem == "compound-nested":
            ET.SubElement(compound, "common-name").text = "Nested name"
        elif problem == "side-duplicate":
            reaction.append(copy.deepcopy(slot))
        else:
            key = {"compound-id": "frameid", "compound-org": "orgid",
                   "compound-resource": "resource", "compound-class": "class"}[problem]
            compound.set(key, "true" if key == "class" else "wrong")
    elif problem.startswith("direction-"):
        direction = reaction.find("reaction-direction")
        if problem == "direction-missing":
            reaction.remove(direction)
        elif problem == "direction-duplicate":
            reaction.append(copy.deepcopy(direction))
        elif problem == "direction-nested":
            ET.SubElement(direction, "nested").text = "REVERSIBLE"
        else:
            direction.text = "FORWARD"
    elif problem.startswith("name-"):
        node = ET.SubElement(reaction, "common-name", {"datatype": "string"})
        node.text = "A curator" if problem == "name-nested-copy" else "A chemical reaction"
        if problem == "name-empty":
            node.text = ""
        elif problem == "name-duplicate":
            reaction.append(copy.deepcopy(node))
    elif problem.startswith("flag-"):
        flag = reaction.find("spontaneous")
        if problem == "flag-duplicate":
            reaction.append(copy.deepcopy(flag))
        elif problem == "flag-invalid":
            flag.text = "yes"
        else:
            ET.SubElement(flag, "nested").text = "true"
    else:
        root = ET.fromstring("<html>Login required</html>")
    with pytest.raises(ValueError, match="MetaCyc reaction"):
        parse(tmp_path, root)


@pytest.mark.parametrize("version", ["", "27", "27.1", "27.0 ", "META 27.0"])
def test_manifest_version_must_match_native_pgdb_and_software(tmp_path, version):
    with pytest.raises(ValueError, match="MetaCyc reaction"):
        parse(tmp_path, version=version)


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16", "iso-8859-1"])
@pytest.mark.parametrize("declaration", [
    '<!DOCTYPE ptools-xml SYSTEM "https://example.invalid/forbidden.dtd">',
    '<!DOCTYPE ptools-xml [<!ENTITY x "forged">]>',
    '<!DOCTYPE ptools-xml [<!ENTITY x SYSTEM "file:///etc/passwd">]>',
])
def test_doctype_and_entities_fail_without_fetch_or_expansion(tmp_path, encoding, declaration):
    body = f'<?xml version="1.0" encoding="{encoding}"?>{declaration}' + ET.tostring(
        native(), encoding="unicode",
    )
    with pytest.raises(ValueError, match="DOCTYPE"):
        parse(tmp_path, raw=body.encode(encoding))


def fixture(tmp_path):
    raw = tmp_path / "native.xml"
    raw.write_bytes(ET.tostring(native()))
    html = tmp_path / "pathway.html"
    html.write_text("<TITLE>MetaCyc Native test pathway</TITLE>"
                    "<script>typeObjectPage = {object:'PWY-FIXTURE',orgid:'META'}</script>")
    entries = [
        {"key": "native", "kind": KIND, "path": raw.name, "url": URL,
         "version": "27.0", "license": "Synthetic fixture", "sha256": hashlib.sha256(
             raw.read_bytes()).hexdigest()},
        {"key": "pathway", "kind": "metacyc-html", "path": html.name,
         "url": f"https://{HOST}/META/NEW-IMAGE?object=PWY-FIXTURE", "version": "27.0",
         "license": "Synthetic fixture", "sha256": hashlib.sha256(html.read_bytes()).hexdigest()},
    ]
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    records = tmp_path / "data/pathways"
    records.mkdir(parents=True)
    record = {"id": "MetaCyc:PWY-FIXTURE", "label": "Native test pathway", "taxa": [],
              "participants": [], "reactions": [{"id": "MetaCyc:" + FRAME,
                  "label": "Curated reverse anomer flux", "category": "molecular_activity"}]}
    path = records / "fixture.yaml"
    path.write_text(yaml.safe_dump(record))
    return manifest, records, entries, record, path


def test_snapshot_retains_type_and_frame_token_without_invented_name(tmp_path):
    manifest, records, _, _, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    assert snapshot["terms"]["MetaCyc:" + FRAME] == {
        "label": FRAME, "synonyms": [], "source": "native",
        "label_kind": "source_context", "entity_type": "reaction",
    }
    assert snapshot["sources"]["native"]["kind"] == KIND
    assert "kind" not in snapshot["sources"]["pathway"]


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize("reverse", [True, False])
@pytest.mark.parametrize("problem", ["version", "side", "direction", "flag", "scope"])
def test_conflicts_fail_before_selection_and_never_replace_output(
    tmp_path, monkeypatch, selected, reverse, problem,
):
    manifest, records, entries, record, path = fixture(tmp_path)
    second = tmp_path / "second.xml"
    root = native()
    extra = {**entries[0], "key": "second", "path": second.name}
    if problem == "version":
        root.set("ptools-version", "28.0")
        root.find("metadata/PGDB").set("version", "28.0")
        extra["version"] = "28.0"
    elif problem == "side":
        node = root.find("Reaction/left/Compound")
        node.set("frameid", "OTHER")
        node.set("resource", "getxml?META:OTHER")
    elif problem == "direction":
        root.find("Reaction/reaction-direction").text = "LEFT-TO-RIGHT"
    elif problem == "flag":
        root.find("Reaction/spontaneous").text = "false"
    if problem == "scope":
        second.write_text(f"<TITLE>MetaCyc A resolved name</TITLE><script>"
                          f"typeObjectPage = {{object:'{FRAME}',orgid:'META'}}</script>")
        extra["kind"] = "metacyc-html"
    else:
        second.write_bytes(ET.tostring(root))
    extra["sha256"] = hashlib.sha256(second.read_bytes()).hexdigest()
    entries.append(extra)
    manifest.write_text(json.dumps(entries[::-1] if reverse else entries))
    if not selected:
        record["reactions"] = []
        path.write_text(yaml.safe_dump(record))
    output = tmp_path / "output.json"
    output.write_bytes(b"previous reviewed authority\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError, match="conflicting MetaCyc reaction"):
        main()
    assert output.read_bytes() == b"previous reviewed authority\n"


def test_matching_duplicate_keeps_first_provenance_and_type(tmp_path):
    manifest, records, entries, _, _ = fixture(tmp_path)
    entries.append({**entries[0], "key": "second"})
    manifest.write_text(json.dumps(entries))
    snapshot = build_snapshot(manifest, records, tmp_path)
    assert snapshot["terms"]["MetaCyc:" + FRAME]["source"] == "native"
    assert snapshot["terms"]["MetaCyc:" + FRAME]["entity_type"] == "reaction"
    assert "second" not in snapshot["sources"]


@pytest.mark.parametrize("existing", [True, False])
@pytest.mark.parametrize("problem", ["hash", "missing", "wrong-request", "name"])
def test_invalid_input_cannot_create_or_replace_snapshot(tmp_path, monkeypatch, existing, problem):
    manifest, records, entries, record, path = fixture(tmp_path)
    if problem == "hash":
        entries[0]["sha256"] = "0" * 64
    elif problem == "missing":
        record["reactions"][0]["id"] = "MetaCyc:RXN-MISSING"
        path.write_text(yaml.safe_dump(record))
    elif problem == "wrong-request":
        entries[0]["url"] = URL.replace("META:", "ECOLI:")
    else:
        root = native()
        ET.SubElement(root.find("Reaction"), "common-name").text = "A curator"
        raw = tmp_path / entries[0]["path"]
        raw.write_bytes(ET.tostring(root))
        entries[0]["sha256"] = hashlib.sha256(raw.read_bytes()).hexdigest()
    manifest.write_text(json.dumps(entries))
    output = tmp_path / "output.json"
    if existing:
        output.write_bytes(b"previous reviewed authority\n")
    monkeypatch.setattr(sys, "argv", [
        "builder", "--manifest", str(manifest), "--records", str(records),
        "--cache-dir", str(tmp_path), "--output", str(output),
    ])
    with pytest.raises(ValueError):
        main()
    assert (output.read_bytes() == b"previous reviewed authority\n"
            if existing else not output.exists())


def gate(tmp_path, snapshot, record, *, contextual=True):
    policy = {"version": 1, "namespaces": {"MetaCyc": {
        "snapshot": "data/identifier_authorities/sources.json", "policy": "canonical"}},
        "contextual_labels": [{"namespace": "MetaCyc", "sections": [
            "record", "taxa", "participants", "reactions"], "record_prefixes": ["MetaCyc"],
            "reason": "Deliberately broad fixture to verify pre-bypass type checks"}]
        if contextual else []}
    (tmp_path / "conf").mkdir(exist_ok=True)
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir(exist_ok=True)
    authority.write_text(json.dumps(snapshot))
    (tmp_path / "data/pathways/fixture.yaml").write_text(yaml.safe_dump(record))
    return identifier_errors(tmp_path)


@pytest.mark.parametrize("section,category", [
    ("record", "molecular_activity"), ("taxa", "molecular_activity"),
    ("participants", "protein"), ("participants", "complex"), ("participants", "small_molecule"),
    ("participants", "molecular_activity"), ("reactions", "pathway"),
    ("reactions", "chemical_entity"), ("reactions", None),
])
def test_native_type_restriction_precedes_even_broad_contextual_bypass(tmp_path, section, category):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    node = record["reactions"].pop()
    if category is None:
        del node["category"]
    else:
        node["category"] = category
    if section == "record":
        record.update(node)
    else:
        record[section].append(node)
    assert any("ENTITY_TYPE_MISMATCH" in e for e in gate(tmp_path, snapshot, record))


def test_correct_type_needs_explicit_contextual_policy(tmp_path):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    assert gate(tmp_path, snapshot, record) == []
    assert any("LABEL_AUTHORITY_UNAVAILABLE" in e for e in gate(
        tmp_path, snapshot, record, contextual=False,
    ))


@pytest.mark.parametrize("problem", [
    "missing-type", "unknown-type", "missing-kind", "unknown-kind", "canonical",
    "synonym", "invented-name", "wrong-namespace", "unknown-field",
])
def test_typed_authority_shape_is_closed_and_source_bound(tmp_path, problem):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    term = snapshot["terms"]["MetaCyc:" + FRAME]
    source = snapshot["sources"]["native"]
    if problem == "missing-type":
        del term["entity_type"]
    elif problem == "unknown-type":
        term["entity_type"] = "protein"
    elif problem == "missing-kind":
        del source["kind"]
    elif problem == "unknown-kind":
        source["kind"] = "other-native-source"
    elif problem == "canonical":
        term["label_kind"] = "canonical"
    elif problem == "synonym":
        term["synonyms"] = ["A curator"]
    elif problem == "invented-name":
        term["label"] = "A chemical equation"
    elif problem == "wrong-namespace":
        snapshot["terms"]["EcoCyc:" + FRAME] = snapshot["terms"].pop("MetaCyc:" + FRAME)
    else:
        term["allowed_sections"] = ["record"]
    assert any("authority unavailable or invalid" in e for e in gate(tmp_path, snapshot, record))


@pytest.mark.parametrize("url", [
    URL.replace("https:", "http:"), URL.replace(HOST, "example.org"),
    URL.replace(HOST, HOST + ".example.org"), URL.replace(HOST, "user@" + HOST),
    URL.replace(HOST, HOST + ":443"), URL.replace(HOST, HOST.upper()),
    URL.replace("getxml", "META/NEW-IMAGE"), URL.replace("getxml", "getxml/"),
    URL.replace("META:", "ECOLI:"), URL.replace("META:", "meta:"),
    URL.replace(FRAME, "RXN-OTHER"), URL.replace(FRAME, FRAME.lower()),
    URL.replace("id=", ""), URL.replace("id=", "ID="), URL + "&detail=full",
    URL + "&id=META:" + FRAME, URL + "&id=", URL + "&", URL + ";id=META:" + FRAME,
    URL + "?id=META:" + FRAME, URL + "#fragment", URL + "#", URL + " ", URL + "\n",
    "\t" + URL, URL.replace("getxml", "get\txml"),
    URL.replace("META:", "META%3A"), URL.replace(FRAME, "%52XN-999991"),
    URL.replace(FRAME, "bad:frame"), URL.replace(FRAME, "bad/frame"),
    URL.replace(FRAME, ""), URL.replace(FRAME, "-bad"),
])
def test_typed_authority_requires_exact_source_request_before_contextual_bypass(tmp_path, url):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    snapshot["sources"]["native"]["url"] = url
    assert any("invalid typed native reaction" in e for e in gate(tmp_path, snapshot, record))


@pytest.mark.parametrize("version", [
    "27", "27.", ".0", "27..0", "27.0 ", " 27.0", "27.0\n", "27.\t0",
    "META 27.0", "27.0-beta", "+27.0", "-27.0", "２７.０", "not a PGDB version",
])
def test_typed_authority_requires_native_version_grammar(tmp_path, version):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    snapshot["sources"]["native"]["version"] = version
    assert any("invalid typed native reaction request or version" in e
               for e in gate(tmp_path, snapshot, record))


@pytest.mark.parametrize("frame,version", [
    (FRAME, "27.0"), ("OTHER-RXN", "28.1"), ("Reaction_17.2", "29.0.1"),
])
def test_typed_provenance_has_no_accession_or_release_exception(tmp_path, frame, version):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    term = snapshot["terms"].pop("MetaCyc:" + FRAME)
    term["label"] = frame
    snapshot["terms"]["MetaCyc:" + frame] = term
    snapshot["sources"]["native"].update(url=URL.replace(FRAME, frame), version=version)
    record["reactions"][0]["id"] = "MetaCyc:" + frame
    assert gate(tmp_path, snapshot, record) == []


@pytest.mark.parametrize("selected", [True, False])
def test_one_typed_source_cannot_establish_a_second_identity(tmp_path, selected):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    second = copy.deepcopy(snapshot["terms"]["MetaCyc:" + FRAME])
    second["label"] = "RXN-OTHER"
    snapshot["terms"]["MetaCyc:RXN-OTHER"] = second
    if selected:
        record["reactions"].append({"id": "MetaCyc:RXN-OTHER", "label": "Second reaction",
                                    "category": "molecular_activity"})
    assert any("MetaCyc:RXN-OTHER: invalid typed native reaction authority" in e
               for e in gate(tmp_path, snapshot, record))


def test_unreferenced_typed_source_still_requires_valid_provenance(tmp_path):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    snapshot["sources"]["unused"] = {
        **snapshot["sources"]["native"], "url": "https://example.org/other.xml",
    }
    assert any("source unused: invalid typed native reaction request or version" in e
               for e in gate(tmp_path, snapshot, record))


def test_new_typed_provenance_rules_do_not_restrict_legacy_untyped_sources(tmp_path):
    manifest, records, _, record, _ = fixture(tmp_path)
    snapshot = build_snapshot(manifest, records, tmp_path)
    del snapshot["terms"]["MetaCyc:" + FRAME]["entity_type"]
    source = snapshot["sources"]["native"]
    del source["kind"]
    source.update(url="http://example.org/legacy.xml?release=old#record", version="Legacy release")
    assert gate(tmp_path, snapshot, record) == []
