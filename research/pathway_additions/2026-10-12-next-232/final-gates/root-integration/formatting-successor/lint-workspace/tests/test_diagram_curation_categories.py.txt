"""ChEBI 255 ancestry counterexamples to chemical-name category inference."""

import hashlib
import importlib.util
import os
import sqlite3
from pathlib import Path

import pytest

SCRIPTS = Path(
    os.environ.get("PATHWAYMECH_MIGRATION_SCRIPTS", Path(__file__).parents[1] / "scripts")
)
SPEC = importlib.util.spec_from_file_location(
    "diagram_curation", SCRIPTS / "curate_diagram_causal_graphs.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


@pytest.mark.parametrize(
    "identifier,label,expected",
    [
        ("CHEBI:15354", "choline", "small_molecule"),
        ("CHEBI:57597", "sn-glycerol 3-phosphate(2-)", "small_molecule"),
        ("CHEBI:16763", "pyruvate", "lipid"),
        ("CHEBI:11851", "4-methyl-2-oxopentanoate", "lipid"),
    ],
)
def test_gpml_category_uses_ontology_ancestry(tmp_path, identifier, label, expected):
    # Named is_a paths inspected in ChEBI release 255, OBO SHA-256
    # 6cd3c7f18d8b22c577e110e00008fb288d8f5b34424bbe5011858747062f9dd9.
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE statements(subject TEXT, predicate TEXT, object TEXT, value TEXT)")
    for subject, parent in [
        ("CHEBI:16763", "CHEBI:58951"),
        ("CHEBI:58951", "CHEBI:28868"),
        ("CHEBI:11851", "CHEBI:58955"),
        ("CHEBI:58955", "CHEBI:28868"),
        ("CHEBI:28868", "CHEBI:18059"),
    ]:
        db.execute(
            "INSERT INTO statements VALUES (?, 'rdfs:subClassOf', ?, NULL)", (subject, parent)
        )
    for subject, name in [(identifier, label), ("CHEBI:15377", "water")]:
        db.execute("INSERT INTO statements VALUES (?, 'rdfs:label', NULL, ?)", (subject, name))
    raw = f'''<Pathway><DataNode GraphId="a" Type="Metabolite" TextLabel="{label}">
      <Xref Database="ChEBI" ID="{identifier}"/></DataNode>
      <DataNode GraphId="b" Type="Metabolite" TextLabel="water">
      <Xref Database="ChEBI" ID="15377"/></DataNode>
      <Interaction GraphId="r"><Graphics><Point GraphRef="a"/>
      <Point GraphRef="b" ArrowHead="Arrow"/></Graphics></Interaction></Pathway>'''
    source = tmp_path / "WP71.gpml"
    source.write_text(raw)
    rec = {
        "id": "WikiPathways:WP71",
        "participants": [],
        "reactions": [{"id": "WikiPathways:WP71/r", "label": "Test"}],
        "references": [],
        "mechanistic_edges": [],
    }
    manifest = {
        "WP71": {
            "path": source.name,
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "url": "https://example.org/WP71.gpml",
            "version": "test",
        }
    }
    MODULE.gpml(rec, tmp_path, manifest, db, {}, {})
    assert (
        next(node["category"] for node in rec["participants"] if node["id"] == identifier)
        == expected
    )
