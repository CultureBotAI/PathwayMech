"""Reproduce this dated audit from pinned git objects and committed offline inputs."""

import argparse
from pathlib import Path

from pathwaymech.cross_mech import (
    ScanCoverage,
    build_pathway_index,
    build_report,
    load_config,
    load_json,
    scan_sibling,
    write_report,
)
from pathwaymech.rhea_directions import load_rhea_directions
from pathwaymech.yaml_io import load_yaml_file, pathway_files

PINS = {
    "TraitMech": "9dea24521a32e92c3425449321fc36b1dbc621f1",
    "ProteinTraitsMech": "316a8005e69bb3f2ee5d53bb0c6bd41beb018421",
    "NaturalProductMech": "aa0e38c4ac899ca5534b4ce02318c019fc44db29",
    "AntibioticMech": "f1604be2ab31232faf63ad6a9bc4b1441af0ac1d",
    "CellStructureMech": "6f9c21f864a0ec71523dda358491e96263934d21",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mechs-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    audit = Path(__file__).resolve().parent
    root = audit.parents[2]
    records = [load_yaml_file(path) for path in pathway_files(root / "data/pathways")]
    annotations = load_json(audit / "inputs/uniprot_annotations.json")
    directions = load_rhea_directions(root / "conf/rhea_directions.json")
    index = build_pathway_index(records, load_json(audit / "inputs/sgd_uniprot.json"),
                                annotations, directions)
    scans, coverage = {}, {}
    for spec in load_config(root / "conf/sibling_mechs.yaml"):
        pin = PINS[spec.name]
        coverage[spec.name] = ScanCoverage(commit=pin, source="pinned audit git objects")
        scans[spec.name] = scan_sibling(args.mechs_root / spec.name, spec,
                                        prefilter_terms=index.proteins, ref=pin,
                                        coverage=coverage[spec.name])
        print(f"read {spec.name} at {pin}", flush=True)
    report = build_report(index, scans, annotations, coverage=coverage, rhea_normalized=True)
    if report.errors:
        raise ValueError("\n".join(report.errors))
    for path in write_report(report, args.out):
        print(path)


if __name__ == "__main__":
    main()
