"""Keep the source pathway visible when a primary interpretation disagrees."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree

import yaml

ROOT = Path(__file__).resolve().parents[1]
ORIGINALS = ROOT / "research/pathway_additions/2026-10-15-next-268/authority-source-originals"
RECORD = ROOT / "data/pathways/phenylacetate-degradation-i-aerobic.yaml"


def _original(identifier):
    rows = json.loads((ORIGINALS / "source-provenance.json").read_text())
    row = next(row for row in rows if row["id"] == identifier)
    body = (ROOT / row["maintained_original"]).read_bytes()
    assert hashlib.sha256(body).hexdigest() == row["manifest_entry"]["sha256"]
    return next(node for node in ElementTree.fromstring(body)
                if node.get("frameid") == identifier.split(":", 1)[1])


def _identifier(node):
    return "MetaCyc:" + node.get("frameid")


def test_every_native_member_and_material_occurrence_remains_source_visible():
    record = yaml.safe_load(RECORD.read_text())
    pathway = _original(record["id"])
    members = [_identifier(node) for node in pathway.findall("reaction-list/Reaction")]
    assert len(members) == len(set(members)) == 9
    declarations = {node["id"]: node for node in record["reactions"]}
    membership = [edge["subject"] for edge in record["mechanistic_edges"]
                  if edge["predicate"] == "part_of" and edge["object"] == record["id"]]
    assert Counter(membership) == Counter(members)
    layouts = {_identifier(row.find("Reaction")): row.findtext("direction")
               for row in pathway.findall("reaction-layout")}
    mechanisms = {item["source_reaction_id"]: item for item in record["reaction_mechanisms"]}
    source_materials = set()
    occurrence_count = 0
    for identifier in members:
        original = _original(identifier)
        reverse = layouts[identifier] == "R2L"
        assert declarations[identifier]["direction"] == (
            "right_to_left" if reverse else "left_to_right"
        )
        expected_equation = {"orientation": "reversed" if reverse else "as_reported"}
        expected_edges = []
        for native_side, equation_side in (("left", "inputs"), ("right", "outputs")):
            terms = []
            for slot in original.findall(native_side):
                material = _identifier(slot.find("Compound"))
                quantity = int(slot.findtext("coefficient", "1"))
                terms.append({"participant_id": material, "coefficient": quantity})
                source_materials.add(material)
                occurrence_count += 1
                is_input = (native_side == "left") != reverse
                expected_edges.append((material, "consumes", identifier) if is_input
                                      else (identifier, "produces", material))
            expected_equation[equation_side] = terms
        actual_edges = [(edge["subject"], edge["predicate"], edge["object"])
                        for edge in record["mechanistic_edges"]
                        if (edge["predicate"] == "consumes" and edge["object"] == identifier)
                        or (edge["predicate"] == "produces" and edge["subject"] == identifier)]
        assert Counter(actual_edges) == Counter(expected_edges), identifier
        assert mechanisms[identifier]["source_equation"] == expected_equation, identifier
    assert occurrence_count == 40
    assert len(source_materials) == 22
    assert source_materials <= {node["id"] for node in record["participants"]}
    assert not source_materials.intersection(record["detail_only_participant_ids"])


def test_isolated_c8_thiolysis_does_not_relabel_or_gain_the_native_net_identity():
    record = yaml.safe_load(RECORD.read_text())
    net = "MetaCyc:RXN0-6512"
    paaj = "MetaCyc:MONOMER-15952"
    cis = "MetaCyc:CIS-34-DEHYDROADIPYL-COA"
    mechanism = next(item for item in record["reaction_mechanisms"]
                     if item["source_reaction_id"] == net)
    assert len(mechanism["steps"]) == 2
    assert all(step["assertion_status"] == "inferred" for step in mechanism["steps"])
    assert cis in record["detail_only_participant_ids"]
    assert not any(edge["subject"] == paaj and edge["predicate"] == "catalyzes"
                   and edge["object"] == net for edge in record["mechanistic_edges"])
    material_uses = [edge for edge in mechanism["edges"]
                     if edge["subject"] == {"node_id": cis}
                     or edge["object"] == {"node_id": cis}]
    assert Counter(edge["predicate"] for edge in material_uses) == {
        "consumes": 1, "produces": 1,
    }
    assert all(edge["coefficient"] == 1 for edge in material_uses)
