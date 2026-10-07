"""Reproduce this dated audit from pinned git objects and committed offline inputs."""

import argparse
from pathlib import Path
from tempfile import TemporaryDirectory

import yaml

from pathwaymech.cross_mech import (
    MechSpec,
    ScanCoverage,
    build_pathway_index,
    build_report,
    git_documents,
    load_config,
    load_json,
    scan_sibling,
    write_report,
)
from pathwaymech.rhea_directions import load_rhea_directions

# The pathway cohort is just as historical as the sibling inputs. Reading the
# working tree here would silently replace this audit's 152-record cohort.
PATHWAY_PIN = "aa305727458c44ab05614901334540e2c87a9f3a"
# This reviewed revision has the same cohort plus the corrected Rhea projection
# and offline evidence inputs. Freeze every input, including sibling slot config.
AUDIT_REF = "e53cf3f159e918a0737bb43c1a64a77a2466df68"
AUDIT_PATH = Path("research/cross_mech/2026-10-05")

PINS = {
    "TraitMech": "9dea24521a32e92c3425449321fc36b1dbc621f1",
    "ProteinTraitsMech": "316a8005e69bb3f2ee5d53bb0c6bd41beb018421",
    "NaturalProductMech": "aa0e38c4ac899ca5534b4ce02318c019fc44db29",
    "AntibioticMech": "f1604be2ab31232faf63ad6a9bc4b1441af0ac1d",
    "CellStructureMech": "6f9c21f864a0ec71523dda358491e96263934d21",
}


def pathway_records(root: Path, ref: str | None = None) -> list[dict]:
    source_ref = PATHWAY_PIN if ref is None else ref
    spec = MechSpec("PathwayMech", ["data/pathways/**/*.yaml"])
    records = []
    for name, payload in git_documents(root, source_ref, spec):
        record = yaml.safe_load(payload)
        if record is None:
            record = {}
        if not isinstance(record, dict):
            raise ValueError(f"{name} must contain a YAML mapping")
        records.append(record)
    if not records:
        raise ValueError(f"No PathwayMech records at audit revision {source_ref}")
    return records


def load_audit_inputs(root: Path, ref: str = AUDIT_REF):
    records = pathway_records(root, ref)
    spec = MechSpec("PathwayMech audit inputs", records=[
        "conf/sibling_mechs.yaml",
        "conf/rhea_directions.json",
        f"{AUDIT_PATH}/inputs/*.json",
    ])
    with TemporaryDirectory(prefix="pathwaymech-dated-audit-") as temporary:
        snapshot = Path(temporary)
        for name, content in git_documents(root, ref, spec):
            path = snapshot / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        inputs = snapshot / AUDIT_PATH / "inputs"
        return (
            records,
            load_json(inputs / "uniprot_annotations.json"),
            load_rhea_directions(snapshot / "conf/rhea_directions.json"),
            load_json(inputs / "sgd_uniprot.json"),
            load_config(snapshot / "conf/sibling_mechs.yaml"),
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mechs-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    audit = Path(__file__).resolve().parent
    root = audit.parents[2]
    records, annotations, directions, sgd_map, specs = load_audit_inputs(root)
    print(f"read PathwayMech audit inputs at {AUDIT_REF}", flush=True)
    index = build_pathway_index(records, sgd_map, annotations, directions)
    scans, coverage = {}, {}
    for spec in specs:
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
