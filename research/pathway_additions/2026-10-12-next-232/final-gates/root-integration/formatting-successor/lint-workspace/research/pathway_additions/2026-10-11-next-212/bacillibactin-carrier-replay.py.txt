"""Independent original-MetaNetX structure replay; no source mutation or equivalence waiver."""

import hashlib
import html
import json
import re
from datetime import UTC, datetime
from pathlib import Path

from rdkit import Chem, rdBase
from rdkit.Chem import rdMolDescriptors

ROOT = Path(__file__).resolve().parent.parent
SCOUT = Path("/private/tmp/pathwaymech-bacillibactin-scout-20261011")
p = SCOUT / "carrier-authority-followup/metanetx-MNXM743865.html"
page = p.read_text()
smiles = html.unescape(re.search(r"<tr><td>SMILES</td><td[^>]*>([^<]+)</td>", page)[1])
mol = Chem.MolFromSmiles(smiles)
assert mol is not None
query = Chem.MolFromSmarts(
    "[S:1]-[C:2](=[O:3])-[C:4]([N:5]-[C:6](=[O:7])-[CH2:8]-[N:9]-"
    "[C:10](=[O:11])-[c:12])-[C:13]([O:14])-[CH3:15]"
)
match = mol.GetSubstructMatches(query)
assert len(match) == 1
roles = {a.GetAtomMapNum(): match[0][a.GetIdx()] for a in query.GetAtoms()}
Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
assert mol.GetAtomWithIdx(roles[4]).GetProp("_CIPCode") == "S"
assert mol.GetAtomWithIdx(roles[13]).GetProp("_CIPCode") == "R"
assert sum(a.GetAtomicNum() == 0 for a in mol.GetAtoms()) == 2
assert Chem.GetFormalCharge(mol) == -1
# Derive a common formal holo-carrier fragment by cleaving only the terminal thioester.
# This is a reactive-part calculation, not a source-issued whole-protein formula.
edit = Chem.RWMol(mol)
edit.RemoveBond(roles[1], roles[2])
cut = edit.GetMol()
Chem.SanitizeMol(cut)
fragments = Chem.GetMolFrags(cut, asMols=True, sanitizeFrags=True)
holo = next(f for f in fragments if any(a.GetAtomicNum() == 16 for a in f.GetAtoms()))
assert Chem.GetFormalCharge(holo) == -1
assert rdMolDescriptors.CalcMolFormula(mol) == "C27H39*2N5O14PS-"
assert rdMolDescriptors.CalcMolFormula(holo) == "C14H25*2N3O8PS-"
# Formula difference equals one third of the native bacillibactin formula.
difference = {"C": 13, "H": 14, "N": 2, "O": 6, "charge": 0}
modelseed = json.loads(
    (SCOUT / "carrier-authority-followup/modelseed-compound_36.json").read_text()
)
old = next(x for x in modelseed if x["id"] == "cpd36242")
assert "arginyl" in old["name"] and old["charge"] == 0
other = Chem.MolFromSmiles(old["smiles"])
assert other is not None and Chem.GetFormalCharge(other) == 0
assert Chem.MolToSmiles(other, True) != Chem.MolToSmiles(mol, True)
report = {
    "checked_at": datetime.now(UTC).isoformat(),
    "status": "passed_scoped_structure_replay",
    "rdkit_version": rdBase.rdkitVersion,
    "original_path": str(p),
    "original_sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
    "canonical_native_smiles": Chem.MolToSmiles(mol, True),
    "native_reactive_class_formula": rdMolDescriptors.CalcMolFormula(mol),
    "native_charge": -1,
    "threonine_alpha_CIP": "S",
    "threonine_beta_CIP": "R",
    "protein_wildcards": 2,
    "derived_holo_fragment_smiles": Chem.MolToSmiles(holo, True),
    "derived_holo_fragment_formula": rdMolDescriptors.CalcMolFormula(holo),
    "derived_loaded_minus_holo": difference,
    "derivation_scope": "Cleaves only the thioester S-C bond. Common reactive-part "
    "scaffold calculation; not an independently issued free carrier identity "
    "or whole-protein formula.",
    "modelseed_raw_exact_equivalence": False,
    "whole_protein_sequence_or_assembly_claim": False,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT / "draft/bacillibactin-carrier-replay.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
