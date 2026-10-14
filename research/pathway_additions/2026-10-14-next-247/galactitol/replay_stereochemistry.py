"""Replay the galactitol C5-oxidation check using RDKit and source-bound InChIs.

Usage: python replay_stereochemistry.py inputs.json [--output result.json]
This is a source-structure consistency check, not an experimental assay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from rdkit import Chem, rdBase


def require(condition: bool, message: str) -> None:
    """Keep validation active even when Python is invoked with optimization."""
    if not condition:
        raise ValueError(message)


def read_molecule(entry: dict[str, Any]) -> Chem.Mol:
    inchi = entry["inchi"]
    molecule = Chem.MolFromInchi(inchi)
    require(molecule is not None, f"Cannot parse {entry['id']}")
    require(Chem.MolToInchi(molecule) == inchi, f"Roundtrip changed {entry['id']}")
    return molecule


def atom_snapshot(molecule: Chem.Mol) -> list[dict[str, Any]]:
    return [
        {
            "index": atom.GetIdx(),
            "map": atom.GetAtomMapNum(),
            "element": atom.GetSymbol(),
            "formal_charge": atom.GetFormalCharge(),
            "explicit_hydrogens": atom.GetNumExplicitHs(),
            "implicit_hydrogens": atom.GetNumImplicitHs(),
            "chiral_tag": str(atom.GetChiralTag()),
            "ordered_neighbor_indices": [n.GetIdx() for n in atom.GetNeighbors()],
        }
        for atom in molecule.GetAtoms()
    ]


def carbon_chain_from_phosphate(molecule: Chem.Mol) -> list[int]:
    phosphorus = [a for a in molecule.GetAtoms() if a.GetAtomicNum() == 15]
    require(len(phosphorus) == 1, "Expected one phosphorus atom")
    bridges = [
        atom
        for atom in phosphorus[0].GetNeighbors()
        if atom.GetAtomicNum() == 8
        and any(neighbor.GetAtomicNum() == 6 for neighbor in atom.GetNeighbors())
    ]
    require(len(bridges) == 1, "Expected one phosphate-to-carbon oxygen bridge")
    first = [a.GetIdx() for a in bridges[0].GetNeighbors() if a.GetAtomicNum() == 6]
    require(len(first) == 1, "Expected one phosphate-bearing terminal carbon")
    chain = first[:]
    while len(chain) < 6:
        next_atoms = [
            a.GetIdx()
            for a in molecule.GetAtomWithIdx(chain[-1]).GetNeighbors()
            if a.GetAtomicNum() == 6 and a.GetIdx() not in chain
        ]
        require(len(next_atoms) == 1, "Expected an unbranched six-carbon chain")
        chain.append(next_atoms[0])
    carbons = {a.GetIdx() for a in molecule.GetAtoms() if a.GetAtomicNum() == 6}
    require(set(chain) == carbons, "Carbon chain does not cover the molecule")
    return chain


def oxidize_c5(molecule: Chem.Mol, chain: list[int]) -> tuple[Chem.Mol, int]:
    carbon = chain[4]
    oxygens = [
        a.GetIdx() for a in molecule.GetAtomWithIdx(carbon).GetNeighbors() if a.GetAtomicNum() == 8
    ]
    require(len(oxygens) == 1, "Expected one C5 hydroxyl oxygen")
    oxygen = oxygens[0]
    require(molecule.GetAtomWithIdx(carbon).GetTotalNumHs() == 1, "C5 must have one H")
    require(molecule.GetAtomWithIdx(oxygen).GetTotalNumHs() == 1, "C5-O must have one H")
    require(
        molecule.GetBondBetweenAtoms(carbon, oxygen).GetBondType() == Chem.BondType.SINGLE,
        "Expected a C5-O single bond",
    )
    before = atom_snapshot(molecule)
    edit = Chem.RWMol(molecule)
    edit.GetBondBetweenAtoms(carbon, oxygen).SetBondType(Chem.BondType.DOUBLE)
    edit.GetAtomWithIdx(carbon).SetNumExplicitHs(0)
    edit.GetAtomWithIdx(carbon).SetChiralTag(Chem.ChiralType.CHI_UNSPECIFIED)
    edit.GetAtomWithIdx(oxygen).SetNumExplicitHs(0)
    product = edit.GetMol()
    Chem.SanitizeMol(product)
    Chem.AssignStereochemistry(product, cleanIt=True, force=True)
    after = atom_snapshot(product)
    require(len(before) == len(after), "Atom count changed")
    for old, new in zip(before, after, strict=True):
        for field in ("index", "map", "element", "formal_charge", "ordered_neighbor_indices"):
            require(old[field] == new[field], f"Unexpected change at atom {old['map']}: {field}")
        if old["index"] != carbon:
            require(old["chiral_tag"] == new["chiral_tag"], "Surviving stereo tag changed")
        if old["index"] not in (carbon, oxygen):
            for field in ("explicit_hydrogens", "implicit_hydrogens"):
                require(old[field] == new[field], "Unrelated hydrogen count changed")
    for bond in molecule.GetBonds():
        first, second = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
        if {first, second} != {carbon, oxygen}:
            require(
                bond.GetBondType() == product.GetBondBetweenAtoms(first, second).GetBondType(),
                "Unrelated bond order changed",
            )
    return product, oxygen


def exact_graph_match(first: Chem.Mol, second: Chem.Mol) -> bool:
    return first.HasSubstructMatch(second, useChirality=True) and second.HasSubstructMatch(
        first, useChirality=True
    )


def replay(document: dict[str, Any]) -> dict[str, Any]:
    require(document["version"] == 1, "Unsupported input version")
    entries = document["structures"]
    substrate = read_molecule(entries["native_substrate"])
    d_product = read_molecule(entries["native_d_product"])
    l_product = read_molecule(entries["chebi_l_product"])
    require(
        entries["native_substrate"]["inchi"] == entries["chebi_substrate"]["inchi"],
        "Native substrate differs from the retained ChEBI substrate",
    )
    require(
        entries["native_d_product"]["inchi"] == entries["chebi_d_product"]["inchi"],
        "Native D product differs from the retained ChEBI D product",
    )
    for atom in substrate.GetAtoms():
        atom.SetAtomMapNum(atom.GetIdx() + 1)
    chain = carbon_chain_from_phosphate(substrate)
    product, oxygen = oxidize_c5(substrate, chain)
    mirror = Chem.Mol(substrate)
    inverted = []
    for atom in mirror.GetAtoms():
        if atom.GetChiralTag() != Chem.ChiralType.CHI_UNSPECIFIED:
            inverted.append(atom.GetAtomMapNum())
            atom.InvertChirality()
    require(len(inverted) == 4, "Expected four substrate stereocenters")
    mirror_product, _ = oxidize_c5(mirror, chain)
    actual = Chem.MolToInchi(product)
    mirror_actual = Chem.MolToInchi(mirror_product)
    checks = {
        "native_oxidation_equals_d_product": actual == Chem.MolToInchi(d_product),
        "native_oxidation_equals_l_product": actual == Chem.MolToInchi(l_product),
        "d_product_graph_match_with_chirality": exact_graph_match(product, d_product),
        "l_product_graph_match_with_chirality": exact_graph_match(product, l_product),
        "mirror_oxidation_equals_d_product": mirror_actual == Chem.MolToInchi(d_product),
        "mirror_d_product_graph_match_with_chirality": exact_graph_match(mirror_product, d_product),
    }
    require(
        not checks["native_oxidation_equals_d_product"], "Native oxidation unexpectedly yields D"
    )
    require(not checks["d_product_graph_match_with_chirality"], "Unexpected D graph match")
    for field in (
        "native_oxidation_equals_l_product",
        "l_product_graph_match_with_chirality",
        "mirror_oxidation_equals_d_product",
        "mirror_d_product_graph_match_with_chirality",
    ):
        require(checks[field], f"Expected check failed: {field}")
    return {
        "version": 1,
        "rdkit_version": rdBase.rdkitVersion,
        "scope": "Source-structure consistency check; not experimental sample identity.",
        "source_bindings": entries,
        "chain_c1_to_c6_from_phosphate_end_zero_based": chain,
        "oxidized_carbon_map": chain[4] + 1,
        "oxidized_oxygen_map": oxygen + 1,
        "edit": "Only C5-O single to double, two H removed, C5 chirality removed.",
        "validation": "Other atom identities, neighbor order, stereo tags and bonds retained.",
        "substrate_atoms": atom_snapshot(substrate),
        "product_atoms": atom_snapshot(product),
        "substrate_mapped_smiles": Chem.MolToSmiles(substrate),
        "product_mapped_smiles": Chem.MolToSmiles(product),
        "product_inchi": actual,
        "product_inchikey": Chem.MolToInchiKey(product),
        "mirror_inverted_atom_maps": inverted,
        "mirror_substrate_inchi": Chem.MolToInchi(mirror),
        "mirror_substrate_inchikey": Chem.MolToInchiKey(mirror),
        "mirror_product_inchi": mirror_actual,
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    original = args.inputs.read_bytes()
    result = replay(json.loads(original))
    result["input_file_sha256"] = hashlib.sha256(original).hexdigest()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output is None:
        print(encoded, end="")
    else:
        args.output.write_text(encoded)


if __name__ == "__main__":
    main()
