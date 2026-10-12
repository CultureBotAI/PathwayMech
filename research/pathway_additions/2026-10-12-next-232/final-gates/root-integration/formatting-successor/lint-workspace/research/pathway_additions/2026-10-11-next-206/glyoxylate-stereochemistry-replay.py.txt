import json
import sqlite3
import xml.etree.ElementTree as E
from pathlib import Path

from rdkit import Chem

p = Path("/private/tmp/pathwaymech-next-206-evidence/glyoxylate")
c = sqlite3.connect("file:/private/tmp/pathwaymech-curation-authorities/chebi.db?mode=ro", uri=True)
data = {}
for native, chebi in [("CPD-9409", "CHEBI:75634"), ("CPD-627", "CHEBI:58668")]:
    x = E.parse(p / (native + ".xml")).getroot()
    n = x.find(".//Compound/inchi").text
    q = c.execute(
        "select value from statements where subject=? and predicate='chemrof:inchi_string'", [chebi]
    ).fetchone()[0]
    pair = {}
    for key, s in [("native", n), ("chebi", q)]:
        m = Chem.MolFromInchi(s, removeHs=False)
        Chem.AssignStereochemistry(m, cleanIt=True, force=True)
        pair[key] = {
            "inchi": s,
            "canonical_smiles": Chem.MolToSmiles(m, isomericSmiles=True),
            "centers": [
                (
                    a.GetIdx(),
                    a.GetSymbol(),
                    a.GetProp("_CIPCode") if a.HasProp("_CIPCode") else "?",
                    [n.GetIdx() for n in a.GetNeighbors()],
                )
                for a in m.GetAtoms()
                if a.GetChiralTag() != Chem.ChiralType.CHI_UNSPECIFIED
            ],
        }
        for a in m.GetAtoms():
            a.SetAtomMapNum(a.GetIdx() + 1)
        pair[key]["mapped_smiles"] = Chem.MolToSmiles(m, isomericSmiles=True)
    data[native] = {"chebi_id": chebi, **pair}
(p / "stereochemistry-rdkit.json").write_text(json.dumps(data, indent=2) + "\n")
print(json.dumps(data, indent=2))
