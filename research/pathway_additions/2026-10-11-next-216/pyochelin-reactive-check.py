"""Original-native reactive-group replay. Derived anchors are not issued structures."""

import argparse
import json
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as E

from rdkit import Chem, rdBase

p = argparse.ArgumentParser()
p.add_argument("--manifest", type=Path, required=True)
p.add_argument("--projection", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args()
if not __debug__:
    raise RuntimeError("optimized Python is not permitted")
if a.output.exists():
    raise FileExistsError(a.output)
m = json.loads(a.manifest.read_text())
proj = json.loads(a.projection.read_text())
originals = Path(m["roles"]["native_originals"])
# Explicit stoichiometric derivations from native class names and original 2022 SI Fig1c.
# Unspecified stereo serves atom counting only; these are not new carrier identities.
smiles = {
    "PchE": "*S",
    "PchF": "*S",
    "Salicyl-PchE": "*SC(=O)c1ccccc1O",
    "L-cysteinyl-PchE": "*SC(=O)C([NH3+])CS",
    "L-cysteinyl-PchF": "*SC(=O)C([NH3+])CS",
    "Salicyl-L-cysteinyl-PchE": "*SC(=O)C(CS)NC(=O)c1ccccc1O",
    "hydroxyphenyl-thiazolinyl-PchE": "*SC(=O)C1CSC(=N1)c1ccccc1O",
    "Hydroxyphenyl-bis-thiazolinyl-PchF": "*SC(=O)C1CSC(=N1)C2CSC(=N2)c2ccccc2O",
    "N-desmethyl-pyochelin-PchF": "*SC(=O)C1CSC(N1)C2CSC(=N2)c2ccccc2O",
    "Pyochelinyl-PchF": "*SC(=O)C1CSC(N1C)C2CSC(=N2)c2ccccc2O",
}


def node(f):
    return next(n for n in E.parse(originals / (f + ".xml")).getroot() if n.get("frameid") == f)


rows = proj["source_to_graph"]
facts = {}
net = Counter()
checks = []
for row in rows:
    n = node(row["id"])
    sides = {}
    for side in ["left", "right"]:
        sides[side] = [
            (
                next(c for c in x if c.get("frameid")).get("frameid"),
                int(x.findtext("coefficient") or "1"),
            )
            for x in n.findall(side)
        ]
    assert {k: sorted(v) for k, v in sides.items()} == {
        k: sorted((f, int(v)) for f, v in vs) for k, vs in row["sides"].items()
    }
    delta = Counter()
    for side, sign in [("left", -1), ("right", 1)]:
        for f, c in sides[side]:
            if f not in facts:
                mol = (
                    Chem.MolFromSmiles(smiles[f])
                    if f in smiles
                    else Chem.MolFromInchi(node(f).findtext("inchi"))
                )
                assert mol is not None, f
                v = Counter(x.GetSymbol() for x in Chem.AddHs(mol).GetAtoms())
                v["charge"] = Chem.GetFormalCharge(mol)
                if "*" in v:
                    assert v.pop("*") == 1
                    v["PchE_domain_anchor" if "PchE" in f else "PchF_domain_anchor"] = 1
                facts[f] = dict(v)
            for k, v in facts[f].items():
                delta[k] += sign * c * v
            net[f] += sign * c * (2 if row["id"] == "RXN-11115" else 1)
    residual = {k: v for k, v in delta.items() if v}
    assert not residual, (row["id"], residual)
    checks.append(dict(id=row["id"], residual=residual))
net = {k: v for k, v in net.items() if v}
assert net == proj["formal_net"]
assert net["ATP"] == -3 and net["CYS"] == -2
# Issued product identity: monoanion vs neutral I/II; no erasure of stereo differences.
i = node("CPD-9992").findtext("inchi")
assert "/p-1" in i and "/t9-,10+,13-/m1/s1" in i
out = dict(
    status="passed",
    rdkit=rdBase.rdkitVersion,
    checks=checks,
    reactive_vectors=facts,
    net=net,
    scope=(
        "Formal native-site equations; no full-polypeptide balance "
        "or exclusive-I physiological assertion; 3ATP is a reaction-sum derivation"
    ),
)
with a.output.open("x") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print("PASS 11 qualified reactive-group balances")
