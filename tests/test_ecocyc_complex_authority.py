"""Bounded assembly fixtures; actual whole-original replay is separately sealed."""

from __future__ import annotations

import copy
import hashlib
import json
from xml.etree import ElementTree as ET

import pytest
import yaml

from pathwaymech.ecocyc_complex import ECOCYC_COMPLEX_KIND, complex_metadata, complex_term
from pathwaymech.identifiers import _load_authority, identifier_errors
from scripts.build_source_identifier_snapshot import build_snapshot

HOST = "bf2i-artsymbiocyc.insa-lyon.fr"
VERSION = "27.0"


def native(frame="ASSEMBLY", *, is_class=False):
    suffix = ' class="true"' if is_class else ""
    return ET.fromstring(f'''<ptools-xml ptools-version="27.0"
      xml:base="http://{HOST}:443/getxml?ECOLI:{frame}">
      <metadata><url>http://{HOST}:443/</url><service_name>getxml</service_name>
      <query>ECOLI:{frame}</query><num_results>1</num_results>
      <PGDB orgid="ECOLI" version="27.0"><species datatype="string">Escherichia coli</species>
      <strain datatype="string">K-12 substr. MG1655</strain><dblink>
      <dblink-db>NCBI-TAXONOMY-DB</dblink-db><dblink-oid>511145</dblink-oid>
      <dblink-relationship>unification</dblink-relationship>
      <dblink-URL>http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=511145</dblink-URL>
      </dblink></PGDB></metadata>
      <Protein ID="ECOLI:{frame}" orgid="ECOLI" frameid="{frame}" detail="full"{suffix}/>
      </ptools-xml>''')


def reference(parent, slot, frame, *, is_class=False):
    wrapper = ET.SubElement(parent, slot)
    attributes = {"resource": "getxml?ECOLI:" + frame, "orgid": "ECOLI", "frameid": frame}
    if is_class:
        attributes["class"] = "true"
    ET.SubElement(wrapper, "Protein", attributes)
    return wrapper


def document(shape="unnamed", frame="ASSEMBLY"):
    root = native(frame)
    entity = root.find("Protein")
    if shape == "synonym":
        reference(entity, "parent", "PC-1", is_class=True)
        ET.SubElement(entity, "synonym", datatype="string").text = "NativeAB"
    reference(entity, "parent", "Protein-Complexes", is_class=True)
    for part, coefficient in [("CHAIN", 6)] if shape == "unnamed" else [("B", 2), ("A", 2)]:
        wrapper = reference(entity, "component", part)
        ET.SubElement(wrapper, "coefficient", datatype="integer").text = str(coefficient)
    proof = native("PC-1", is_class=True)
    cls = proof.find("Protein")
    ET.SubElement(cls, "common-name", datatype="string").text = "a transporter"
    reference(cls, "subclass", "Transporter-subclass", is_class=True)
    reference(cls, "instance", frame)
    return root, proof


def original(tmp_path, name, root, frame):
    path = tmp_path / name
    path.write_bytes(ET.tostring(root, encoding="utf-8", xml_declaration=True))
    return {
        "path": name,
        "url": f"https://{HOST}/getxml?id=ECOLI:{frame}",
        "version": VERSION,
        "license": "Synthetic test fixture",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def entry(
    tmp_path, shape="unnamed", frame="ASSEMBLY", *, root=None, proof=None, name="original.xml"
):
    observed, class_body = document(shape, frame)
    result = {
        "key": name,
        "kind": ECOCYC_COMPLEX_KIND,
        **original(tmp_path, name, observed if root is None else root, frame),
    }
    if shape == "synonym":
        result["class_source"] = original(
            tmp_path, name + ".class.xml", class_body if proof is None else proof, "PC-1"
        )
    return result


def build(tmp_path, entries, selected="ASSEMBLY"):
    records = tmp_path / "records"
    records.mkdir(exist_ok=True)
    (records / "ids.yaml").write_text(yaml.safe_dump({"id": "EcoCyc:" + selected}))
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(entries))
    return build_snapshot(manifest, records, tmp_path)


@pytest.mark.parametrize(
    "shape,frame",
    [
        ("unnamed", "ASSEMBLY"),
        ("unnamed", "SECOND-17"),
        ("synonym", "ASSEMBLY"),
        ("synonym", "OTHER.2"),
    ],
)
def test_supported_shapes_preserve_native_absence_types_components_and_proof(
    tmp_path, shape, frame
):
    item = entry(tmp_path, shape, frame)
    metadata = complex_metadata(item, tmp_path)
    native_data = metadata["native_complex"]
    identifier, term = complex_term(metadata, item["key"])
    assert identifier == "EcoCyc:" + frame and native_data["direct_common_name"] is None
    assert native_data["parent_classes"] == (
        ["Protein-Complexes"] if shape == "unnamed" else ["PC-1", "Protein-Complexes"]
    )
    assert native_data["components"] == (
        [{"id": "EcoCyc:CHAIN", "coefficient": 6}]
        if shape == "unnamed"
        else [{"id": "EcoCyc:B", "coefficient": 2}, {"id": "EcoCyc:A", "coefficient": 2}]
    )
    assert term["label"] == (
        "unnamed protein complex " + frame if shape == "unnamed" else "NativeAB"
    )
    assert term["label_kind"] == ("source_context" if shape == "unnamed" else "source_synonym")
    assert term["entity_type"] == "protein_complex" and term["synonyms"] == []
    assert native_data["name_status"] == ("unnamed" if shape == "unnamed" else "synonym_only")
    assert native_data["direct_synonyms"] == ([] if shape == "unnamed" else ["NativeAB"])
    if shape == "synonym":
        proof = native_data["class_source"]
        assert proof["sha256"] == item["class_source"]["sha256"]
        assert proof["id"] == "EcoCyc:PC-1" and proof["instances"] == [identifier]
    result = build(tmp_path, [item], frame)
    assert result["terms"] == {identifier: term} and result["sources"] == {item["key"]: metadata}
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(result))
    assert _load_authority(path) == result["terms"]


@pytest.mark.parametrize("shape", ["unnamed", "synonym"])
@pytest.mark.parametrize(
    "path,key,value",
    [
        (".", "ptools-version", "28.0"),
        ("metadata/PGDB", "orgid", "META"),
        ("metadata/PGDB", "version", "28.0"),
        ("Protein", "ID", "ECOLI:OTHER"),
        ("Protein", "frameid", "OTHER"),
        ("Protein", "orgid", "META"),
        ("Protein", "detail", "low"),
        ("Protein", "class", "true"),
        ("Protein", "resource", "#ECOLI:ASSEMBLY"),
        ("Protein/parent/Protein", "frameid", "Polypeptides"),
        ("Protein/parent/Protein", "class", "false"),
        ("Protein/parent/Protein", "orgid", "META"),
        ("Protein/component/Protein", "orgid", "META"),
        ("Protein/component/Protein", "class", "true"),
        ("Protein/component/Protein", "resource", "#ECOLI:CHAIN"),
        ("Protein/component/coefficient", "datatype", "float"),
    ],
)
def test_exact_identity_type_and_component_attributes_fail_closed(
    tmp_path, shape, path, key, value
):
    root, _ = document(shape)
    root.find(path).set(key, value)
    with pytest.raises(ValueError, match="EcoCyc complex"):
        complex_metadata(entry(tmp_path, shape, root=root), tmp_path)


@pytest.mark.parametrize(
    "problem",
    [
        "no-parent",
        "duplicate-parent",
        "unrelated-parent",
        "conflicting-parent",
        "no-component",
        "duplicate-component",
        "class-component",
        "nested-component",
        "missing-coefficient",
        "duplicate-coefficient",
        "zero",
        "negative",
        "fractional",
        "padded",
        "self-component",
        "direct-name",
        "empty-direct-name",
        "copied-nested-name",
        "two-aliases",
        "duplicate-alias",
        "nested-alias",
        "empty-alias",
        "unsafe-alias",
        "unsupported-alias",
        "no-synonym",
        "wrong-type",
        "nested-entity",
        "extra-entity",
        "nested-parent",
        "modified-state",
        "extra-component-slot",
    ],
)
def test_ambiguous_assemblies_and_name_forgery_are_rejected_before_selection(tmp_path, problem):
    shape = "synonym" if "alias" in problem or problem == "no-synonym" else "unnamed"
    root, _ = document(shape)
    entity = root.find("Protein")
    if problem == "no-parent":
        entity.remove(entity.find("parent"))
    elif problem == "duplicate-parent":
        entity.append(copy.deepcopy(entity.find("parent")))
    elif problem in {"unrelated-parent", "conflicting-parent", "modified-state"}:
        reference(
            entity,
            "parent",
            {
                "unrelated-parent": "PC-8",
                "conflicting-parent": "Protein-Small-Molecule-Complexes",
                "modified-state": "Modified-Proteins",
            }[problem],
            is_class=True,
        )
    elif problem == "no-component":
        entity.remove(entity.find("component"))
    elif problem == "duplicate-component":
        entity.append(copy.deepcopy(entity.find("component")))
    elif problem == "class-component":
        entity.find("component/Protein").set("class", "true")
    elif problem == "nested-component":
        ET.SubElement(entity.find("component/Protein"), "Protein")
    elif problem == "missing-coefficient":
        entity.find("component").remove(entity.find("component/coefficient"))
    elif problem == "duplicate-coefficient":
        entity.find("component").append(copy.deepcopy(entity.find("component/coefficient")))
    elif problem in {"zero", "negative", "fractional", "padded"}:
        entity.find("component/coefficient").text = {
            "zero": "0",
            "negative": "-2",
            "fractional": "1.5",
            "padded": " 6 ",
        }[problem]
    elif problem == "self-component":
        node = entity.find("component/Protein")
        node.set("frameid", "ASSEMBLY")
        node.set("resource", "getxml?ECOLI:ASSEMBLY")
    elif problem in {"direct-name", "empty-direct-name", "copied-nested-name"}:
        ET.SubElement(entity, "common-name", datatype="string").text = (
            "" if problem == "empty-direct-name" else "Nested activity name"
        )
    elif problem in {"two-aliases", "duplicate-alias"}:
        ET.SubElement(entity, "synonym", datatype="string").text = (
            "Other" if problem == "two-aliases" else "NativeAB"
        )
    elif problem == "nested-alias":
        ET.SubElement(entity.find("synonym"), "b").text = "not direct string"
    elif problem in {"empty-alias", "unsafe-alias", "unsupported-alias"}:
        entity.find("synonym").text = {
            "empty-alias": "",
            "unsafe-alias": "<script>bad</script>",
            "unsupported-alias": "Ambiguous alias words",
        }[problem]
    elif problem == "no-synonym":
        entity.remove(entity.find("synonym"))
    elif problem == "wrong-type":
        entity.tag = "RNA"
    elif problem == "nested-entity":
        root.remove(entity)
        ET.SubElement(root, "wrapper").append(entity)
    elif problem == "extra-entity":
        root.append(copy.deepcopy(entity))
    elif problem == "nested-parent":
        node = entity.find("parent")
        entity.remove(node)
        ET.SubElement(entity, "wrapper").append(node)
    else:
        ET.SubElement(entity.find("component"), "unexpected")
    with pytest.raises(ValueError, match="EcoCyc complex"):
        build(tmp_path, [entry(tmp_path, shape, root=root)], "UNSELECTED")


def test_nested_activity_and_curator_names_are_never_promoted(tmp_path):
    root, _ = document()
    activity = ET.SubElement(ET.SubElement(root.find("Protein"), "catalyzes"), "Enzymatic-Reaction")
    ET.SubElement(activity, "common-name", datatype="string").text = "Forged nested canonical label"
    ET.SubElement(activity, "synonym", datatype="string").text = "ForgedAlias"
    item = entry(tmp_path, root=root)
    result = complex_metadata(item, tmp_path)
    assert result["native_complex"]["direct_synonyms"] == []
    assert complex_term(result, "test")[1]["label"] == "unnamed protein complex ASSEMBLY"


@pytest.mark.parametrize("shape", ["unnamed", "synonym"])
@pytest.mark.parametrize(
    "slot", ["unmodified-form", "gene", "instance", "subclass", "wrapper", "unexpected"]
)
def test_conflicting_state_chain_class_or_hidden_type_slots_are_rejected(tmp_path, shape, slot):
    root, _ = document(shape)
    ET.SubElement(root.find("Protein"), slot)
    with pytest.raises(ValueError, match="unsupported direct complex slots"):
        build(tmp_path, [entry(tmp_path, shape, root=root)], "UNSELECTED")


@pytest.mark.parametrize(
    "problem",
    [
        "missing",
        "hash",
        "url",
        "version",
        "absolute",
        "traversal",
        "extra",
        "class-false",
        "wrong-id",
        "wrong-org",
        "wrong-version",
        "wrong-label",
        "missing-instance",
        "duplicate-instance",
        "nested-instance",
        "wrong-instance",
        "instance-class",
        "duplicate-subclass",
        "extra-slot",
    ],
)
def test_PC1_proof_is_independently_bound_and_typed(tmp_path, problem):
    root, proof = document("synonym")
    entity = proof.find("Protein")
    if problem == "class-false":
        entity.set("class", "false")
    elif problem == "wrong-id":
        entity.set("ID", "ECOLI:PC-8")
    elif problem == "wrong-org":
        proof.find("metadata/PGDB").set("orgid", "META")
    elif problem == "wrong-version":
        proof.find("metadata/PGDB").set("version", "28.0")
    elif problem == "wrong-label":
        entity.find("common-name").text = "a reaction"
    elif problem == "missing-instance":
        entity.remove(entity.find("instance"))
    elif problem == "duplicate-instance":
        entity.append(copy.deepcopy(entity.find("instance")))
    elif problem == "nested-instance":
        node = entity.find("instance")
        entity.remove(node)
        ET.SubElement(entity, "nested").append(node)
    elif problem == "wrong-instance":
        node = entity.find("instance/Protein")
        node.set("frameid", "OTHER")
        node.set("resource", "getxml?ECOLI:OTHER")
    elif problem == "instance-class":
        entity.find("instance/Protein").set("class", "true")
    elif problem == "duplicate-subclass":
        entity.append(copy.deepcopy(entity.find("subclass")))
    elif problem == "extra-slot":
        ET.SubElement(entity, "parent")
    item = entry(tmp_path, "synonym", root=root, proof=proof)
    if problem == "missing":
        del item["class_source"]
    elif problem in {"hash", "url", "version", "absolute", "traversal", "extra"}:
        key, value = {
            "hash": ("sha256", "0" * 64),
            "url": ("url", "https://example.org/PC-1"),
            "version": ("version", "28.0"),
            "absolute": ("path", "/tmp/class.xml"),
            "traversal": ("path", "../class.xml"),
            "extra": ("untrusted", True),
        }[problem]
        item["class_source"][key] = value
    with pytest.raises(ValueError, match="EcoCyc complex"):
        build(tmp_path, [item], "UNSELECTED")


@pytest.mark.parametrize("selected", ["ASSEMBLY", "UNSELECTED"])
@pytest.mark.parametrize("change", ["component", "coefficient", "parent-kind", "name-status"])
def test_duplicate_conflicts_fail_before_selection(tmp_path, selected, change):
    first = entry(tmp_path)
    root, _ = document()
    overrides = {}
    if change == "component":
        node = root.find("Protein/component/Protein")
        node.set("frameid", "OTHER")
        node.set("resource", "getxml?ECOLI:OTHER")
    elif change == "coefficient":
        root.find("Protein/component/coefficient").text = "8"
    elif change == "parent-kind":
        root.find("Protein/parent/Protein").set("frameid", "Protein-Small-Molecule-Complexes")
        root.find("Protein/parent/Protein").set(
            "resource", "getxml?ECOLI:Protein-Small-Molecule-Complexes"
        )
        ET.SubElement(root.find("Protein"), "common-name", datatype="string").text = "Named complex"
        overrides["kind"] = "ecocyc-protein-xml"
    else:
        root, _ = document("synonym")
    second = entry(
        tmp_path, "synonym" if change == "name-status" else "unnamed", root=root, name="second.xml"
    )
    second.update(overrides)
    with pytest.raises(ValueError, match="conflicting EcoCyc native identity"):
        build(tmp_path, [first, second], selected)


def test_duplicate_agreement_retains_complete_first_source(tmp_path):
    first, second = entry(tmp_path), entry(tmp_path, name="second.xml")
    snapshot = build(tmp_path, [first, second])
    assert list(snapshot["sources"]) == [first["key"]]
    assert snapshot["terms"]["EcoCyc:ASSEMBLY"]["source"] == first["key"]


@pytest.mark.parametrize("shape", ["unnamed", "synonym"])
@pytest.mark.parametrize(
    "change", ["http", "host", "port", "query", "fragment", "frame", "pgdb", "encoding", "newline"]
)
def test_issuing_transport_and_request_cannot_drift(tmp_path, shape, change):
    item = entry(tmp_path, shape)
    url = item["url"]
    item["url"] = {
        "http": url.replace("https:", "http:"),
        "host": url.replace(HOST, "example.org"),
        "port": url.replace(HOST, HOST + ":443"),
        "query": url + "&detail=full",
        "fragment": url + "#entity",
        "frame": url.replace("ASSEMBLY", "OTHER"),
        "pgdb": url.replace("ECOLI:", "META:"),
        "encoding": url.replace("ECOLI:", "ECOLI%3A"),
        "newline": url + "\n",
    }[change]
    with pytest.raises(ValueError, match="EcoCyc complex"):
        complex_metadata(item, tmp_path)


@pytest.mark.parametrize(
    "path,value",
    [
        ("metadata/service_name", "other"),
        ("metadata/query", "ECOLI:OTHER"),
        ("metadata/num_results", "2"),
        ("metadata/PGDB/species", "Salmonella enterica"),
        ("metadata/PGDB/strain", "K-12"),
        ("metadata/PGDB/dblink/dblink-oid", "562"),
        ("metadata/PGDB/dblink/dblink-db", "OTHER"),
        ("metadata/PGDB/dblink/dblink-relationship", "related"),
        ("metadata/PGDB/dblink/dblink-URL", "https://example.org/511145"),
    ],
)
def test_closed_native_metadata_values(tmp_path, path, value):
    root, _ = document()
    root.find(path).text = value
    with pytest.raises(ValueError, match="EcoCyc complex"):
        complex_metadata(entry(tmp_path, root=root), tmp_path)


@pytest.mark.parametrize(
    "path", ["metadata", "metadata/query", "metadata/PGDB", "metadata/PGDB/dblink", "Protein"]
)
def test_duplicate_native_identity_slots(tmp_path, path):
    root, _ = document()
    owner = root.find(path.rsplit("/", 1)[0]) if "/" in path else root
    owner.append(copy.deepcopy(root.find(path)))
    with pytest.raises(ValueError, match="EcoCyc complex"):
        complex_metadata(entry(tmp_path, root=root), tmp_path)


@pytest.mark.parametrize("encoding", ["utf-8", "utf-16"])
def test_doctype_rejected_in_primary_and_class_original(tmp_path, encoding):
    for target in ("primary", "class"):
        item = entry(tmp_path, "synonym")
        binding = item if target == "primary" else item["class_source"]
        root = ET.parse(tmp_path / binding["path"]).getroot()
        body = (
            '<?xml version="1.0" encoding="'
            + encoding
            + '"?><!DOCTYPE ptools-xml [<!ENTITY bad "forged">]>'
            + ET.tostring(root, encoding="unicode")
        ).encode(encoding)
        (tmp_path / binding["path"]).write_bytes(body)
        binding["sha256"] = hashlib.sha256(body).hexdigest()
        with pytest.raises(ValueError, match="DOCTYPE"):
            complex_metadata(item, tmp_path)


@pytest.mark.parametrize("value", ["unknown", "Error", "notfound", "ASSEMBLY"])
def test_unresolved_synonym_tokens_fail(tmp_path, value):
    root, _ = document("synonym")
    root.find("Protein/synonym").text = value
    with pytest.raises(ValueError, match="EcoCyc complex"):
        complex_metadata(entry(tmp_path, "synonym", root=root), tmp_path)


def test_class_companion_cannot_be_attached_to_legacy_adapter(tmp_path):
    item = entry(tmp_path, "synonym")
    item["kind"] = "ecocyc-protein-xml"
    with pytest.raises(ValueError, match="class_source requires the typed"):
        build(tmp_path, [item])


@pytest.mark.parametrize(
    "change",
    [
        "label",
        "alias",
        "label-kind",
        "entity-type",
        "source-kind",
        "native-name",
        "component-bool",
        "component-duplicate",
        "parents-duplicate",
        "parents-unsupported",
        "proof",
        "proof-instance",
        "proof-version",
    ],
)
def test_snapshot_consumer_rejects_forged_typed_metadata(tmp_path, change):
    snapshot = build(tmp_path, [entry(tmp_path, "synonym")])
    term = snapshot["terms"]["EcoCyc:ASSEMBLY"]
    source = snapshot["sources"][term["source"]]
    native_data = source["native_complex"]
    if change == "label":
        term["label"] = "Invented canonical name"
    elif change == "alias":
        term["synonyms"] = ["Invented"]
    elif change == "label-kind":
        term["label_kind"] = "canonical"
    elif change == "entity-type":
        term["entity_type"] = "reaction"
    elif change == "source-kind":
        source["kind"] = "ecocyc-protein-xml"
    elif change == "native-name":
        native_data["direct_common_name"] = "Invented"
    elif change == "component-bool":
        native_data["components"][0]["coefficient"] = True
    elif change == "component-duplicate":
        native_data["components"].append(copy.deepcopy(native_data["components"][0]))
    elif change == "parents-duplicate":
        native_data["parent_classes"].append("PC-1")
    elif change == "parents-unsupported":
        native_data["parent_classes"].append("Modified-Proteins")
    elif change == "proof":
        native_data["class_source"] = None
    elif change == "proof-instance":
        native_data["class_source"]["instances"] = ["EcoCyc:OTHER"]
    else:
        native_data["class_source"]["version"] = "28.0"
    path = tmp_path / "snapshot.json"
    path.write_text(json.dumps(snapshot))
    with pytest.raises(ValueError):
        _load_authority(path)


@pytest.mark.parametrize("shape", ["unnamed", "synonym"])
@pytest.mark.parametrize(
    "change,expected",
    [
        (None, None),
        ("display", "LABEL_MISMATCH"),
        ("category", "ENTITY_TYPE_MISMATCH"),
        ("section", "ENTITY_TYPE_MISMATCH"),
        ("context-rule", "LABEL_MISMATCH"),
        ("canonical-only", "LABEL_AUTHORITY_UNAVAILABLE"),
    ],
)
def test_only_honest_displays_on_complex_participants_pass(tmp_path, shape, change, expected):
    snapshot = build(tmp_path, [entry(tmp_path, shape)])
    snapshot["sources"]["fixture"] = {
        "url": "https://example.org/native",
        "version": "fixture",
        "license": "fixture",
        "sha256": "a" * 64,
    }
    snapshot["terms"]["MetaCyc:TEST"] = {"label": "test", "synonyms": [], "source": "fixture"}
    node = {
        "id": "EcoCyc:ASSEMBLY",
        "label": snapshot["terms"]["EcoCyc:ASSEMBLY"]["label"],
        "category": "complex",
    }
    record = {
        "id": "MetaCyc:TEST",
        "label": "test",
        "taxa": [],
        "participants": [node],
        "reactions": [],
    }
    if change in {"display", "context-rule"}:
        node["label"] = "Scientifically interpreted name"
    elif change == "category":
        node["category"] = "protein"
    elif change == "section":
        record["participants"] = []
        record["reactions"] = [node]
    directory = tmp_path / "data/pathways"
    directory.mkdir(parents=True)
    (directory / "record.yaml").write_text(yaml.safe_dump(record))
    policy = {
        "version": 1,
        "namespaces": {
            prefix: {
                "snapshot": "data/identifier_authorities/sources.json",
                "policy": "canonical_or_synonym",
            }
            for prefix in ("EcoCyc", "MetaCyc")
        },
        "contextual_labels": [],
    }
    if change == "context-rule":
        policy["contextual_labels"] = [
            {
                "namespace": "EcoCyc",
                "sections": ["participants"],
                "record_prefixes": ["MetaCyc"],
                "reason": "Synthetic bypass attempt",
            }
        ]
    if change == "canonical-only":
        policy["namespaces"]["EcoCyc"]["policy"] = "canonical"
        if shape == "unnamed":
            expected = None  # Explicit fallback verifies identity, without claiming a native name.
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf/identifier_policy.yaml").write_text(yaml.safe_dump(policy))
    authority = tmp_path / "data/identifier_authorities/sources.json"
    authority.parent.mkdir()
    authority.write_text(json.dumps(snapshot))
    errors = identifier_errors(tmp_path)
    assert any(expected in error for error in errors) if expected else errors == []
