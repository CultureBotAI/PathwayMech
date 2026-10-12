"""Mixed-profile forward cycles from coherent whole legacy source mutations."""

from __future__ import annotations

import copy
import json

import pytest
import test_aceto_authority as h

from pathwaymech.ecocyc_complex import complex_metadata, complex_term


def legacy_leaf(tmp_path, cyclic):
    entry = copy.deepcopy(h.BY_ID["EcoCyc:ACETYL-COA-ACETYLTRANSFER-CPLX"]["entry"])
    root = h.original(entry, tmp_path)
    old, frame = root[1].get("frameid"), "ATOA-MONOMER"
    root[1].set("ID", "ECOLI:" + frame)
    root[1].set("frameid", frame)
    root.find("metadata/query").text = "ECOLI:" + frame
    root.set(
        "{http://www.w3.org/XML/1998/namespace}base",
        root.get("{http://www.w3.org/XML/1998/namespace}base").replace(old, frame),
    )
    for node in root.iter():
        for attr, value in list(node.attrib.items()):
            if old in value:
                node.set(attr, value.replace(old, frame))
    h.change_ref(
        root[1].find("component/Protein"),
        h.PARENT.split(":", 1)[1] if cyclic else "OUTSIDE-MONOMER",
    )
    entry.update(key="legacy-leaf", path="legacy-leaf.xml", url=entry["url"].replace(old, frame))
    h.save(entry, root, tmp_path)
    metadata = complex_metadata(entry, tmp_path)
    assert root[1].find("catalyzes/Enzymatic-Reaction/enzyme/Protein").get("frameid") == frame
    # Both graph variants pass the actual preexisting individual source parser.
    individual = h.build(tmp_path, [entry], ["EcoCyc:" + frame])
    assert individual["sources"][entry["key"]] == metadata
    assert h.consume(tmp_path, individual) == individual["terms"]
    return entry, metadata


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("selected", [False, True])
@pytest.mark.parametrize("cyclic", [False, True])
@pytest.mark.parametrize("surface", ["producer", "consumer"])
def test_mixed_profile_forward_cycle(tmp_path, reverse, selected, cyclic, surface):
    h.stage(tmp_path)
    parent = copy.deepcopy(h.BY_ID[h.PARENT]["entry"])
    legacy, metadata = legacy_leaf(tmp_path, cyclic)
    original_metadata = json.dumps(metadata)
    # Real reciprocal component-of context remains present in both whole children.
    for desc in parent["component_sources"]:
        refs = h.original(desc, tmp_path)[1].findall("component-of/Protein")
        assert any(n.get("frameid") == h.PARENT.split(":", 1)[1] for n in refs)
    entries = [parent, legacy]
    if reverse:
        entries.reverse()
    ident = metadata["native_complex"]["id"]
    wanted = [h.PARENT, ident] if selected else [h.PARENT]
    data = h.build(tmp_path, [parent], [h.PARENT])
    data["sources"][legacy["key"]] = metadata
    if selected:
        data["terms"][ident] = complex_term(metadata, legacy["key"])[1]
    if reverse:
        data["sources"] = dict(reversed(list(data["sources"].items())))
    before = json.dumps(data)

    def run():
        if surface == "producer":
            result = h.build(tmp_path, entries, wanted)
            if selected:
                assert json.dumps(result["sources"][legacy["key"]]) == original_metadata
            else:
                assert legacy["key"] not in result["sources"]
            assert h.consume(tmp_path, result) == result["terms"]
        else:
            assert h.consume(tmp_path, data) == data["terms"]

    if cyclic:
        with pytest.raises(ValueError, match="cyclic forward assembly components"):
            run()
    else:
        run()
    assert json.dumps(metadata) == original_metadata
    assert json.dumps(data) == before
