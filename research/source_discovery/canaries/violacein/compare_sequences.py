#!/usr/bin/env python3
"""Reproduce the bounded violacein deposit comparison from hash-checked inputs."""

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from xml.etree import ElementTree

BASES = "TCAG"
AMINO_ACIDS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODONS = {
    "".join(bases): amino_acid
    for bases, amino_acid in zip(itertools.product(BASES, repeat=3), AMINO_ACIDS, strict=True)
}
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def translate(sequence):
    """Translate internal codons shared by NCBI tables 1 and 11; no start override."""
    return "".join(CODONS[sequence[i : i + 3]] for i in range(0, len(sequence) - 2, 3))


def parsed_input(cache_dir, artifact):
    raw = (cache_dir / artifact["file"]).read_bytes()
    if hashlib.sha256(raw).hexdigest() != artifact["sha256"]:
        raise ValueError(f"Checksum mismatch: {artifact['file']}")
    return ElementTree.fromstring(raw)


def coding_sequences(root):
    result = {}
    for feature in root.findall(".//GBFeature"):
        if feature.findtext("GBFeature_key") != "CDS":
            continue
        qualifiers = {
            qualifier.findtext("GBQualifier_name"): qualifier.findtext("GBQualifier_value")
            for qualifier in feature.findall(".//GBQualifier")
        }
        if "gene" in qualifiers and "translation" in qualifiers:
            result[qualifiers["gene"].replace(" ", "")] = {
                "protein": qualifiers["protein_id"],
                "sequence": qualifiers["translation"],
            }
    return result


def compare(cache_dir, manifest):
    artifacts = {entry["file"]: entry for entry in manifest["artifacts"]}
    names = ("AF172851.1.xml", "AB032799.1.xml", "AE016825.1-region.xml")
    roots = {name: parsed_input(cache_dir, artifacts[name]) for name in names}
    target_root = parsed_input(cache_dir, artifacts["AAQ60934.1.xml"])
    target = target_root.findtext(".//GBSeq_sequence").upper()
    matches = []
    for name, root in roots.items():
        sequence = root.findtext(".//GBSeq_sequence").upper()
        for strand, dna in (("+", sequence), ("-", sequence.translate(COMPLEMENT)[::-1])):
            for frame in range(3):
                amino_acids = translate(dna[frame:])
                offset = amino_acids.find(target)
                while offset >= 0:
                    start = frame + offset * 3
                    end = start + len(target) * 3
                    left, right = (
                        (start + 1, end)
                        if strand == "+"
                        else (len(sequence) - end + 1, len(sequence) - start)
                    )
                    match = {
                        "file": name,
                        "strand": strand,
                        "start_1based": left,
                        "end_1based_inclusive": right,
                        "amino_acids": len(target),
                        "stop_codon": dna[end : end + 3],
                    }
                    if name == "AE016825.1-region.xml":
                        match["genome_start_1based"] = left + 3558499
                        match["genome_end_1based_inclusive"] = right + 3558499
                    matches.append(match)
                    offset = amino_acids.find(target, offset + 1)
    deposited = {name: coding_sequences(root) for name, root in roots.items()}
    comparisons = []
    for gene in ("vioA", "vioB", "vioC", "vioD"):
        af, ab, ae = (deposited[name][gene] for name in names)
        comparisons.append(
            {
                "gene": gene,
                "proteins": {
                    "AF172851.1": af["protein"],
                    "AB032799.1": ab["protein"],
                    "AE016825.1": ae["protein"],
                },
                "lengths": {
                    "AF172851.1": len(af["sequence"]),
                    "AB032799.1": len(ab["sequence"]),
                    "AE016825.1": len(ae["sequence"]),
                },
                "AF_vs_AB_exact": af["sequence"] == ab["sequence"],
                "AB_vs_AE_exact": ab["sequence"] == ae["sequence"],
                "AF_vs_AB_substitutions": [
                    {"position_1based": i, "AF": left, "AB": right}
                    for i, (left, right) in enumerate(
                        zip(af["sequence"], ab["sequence"], strict=True), 1
                    )
                    if left != right
                ],
                "AB_vs_AE_substitutions": [
                    {"position_1based": i, "AB": left, "AE": right}
                    for i, (left, right) in enumerate(
                        zip(ab["sequence"], ae["sequence"], strict=True), 1
                    )
                    if left != right
                ],
            }
        )
    return {
        "method": "Exact deposited amino-acid comparison; VioE scanned in all six reading frames. "
        "Coordinates exclude the stop codon. No sequence correction or approximate match.",
        "target": "NCBIProtein:AAQ60934.1",
        "vioe_exact_matches": matches,
        "vioe_no_exact_match": [
            name for name in names if not any(m["file"] == name for m in matches)
        ],
        "four_annotated_proteins": comparisons,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache_dir", type=Path)
    parser.add_argument(
        "--manifest", type=Path, default=Path(__file__).with_name("source-manifest.json")
    )
    args = parser.parse_args()
    print(json.dumps(compare(args.cache_dir, json.loads(args.manifest.read_text())), indent=2))


if __name__ == "__main__":
    main()
