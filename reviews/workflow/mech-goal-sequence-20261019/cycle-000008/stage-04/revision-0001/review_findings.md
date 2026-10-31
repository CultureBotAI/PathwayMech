# PathwayMech Cycle 8 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `2cf03ac05f40abb493c82adee36be1de3ea17ad8`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml) (`sha256: a6e2daa3ecbba006e1c180bf8404fc98f8e78fb7a688b28db565fef7a186c5e2`)
- **Structured Review ID**: `20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C8S4-001`, `F-C8S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 8 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C8S4-001` | `concrete-chebi-small-molecule-participants-typed-as-chemical-entity-4-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 4 `MetaCyc:*` records (`MetaCyc:SALVADEHYPOX-PWY`, `MetaCyc:P184-PWY`, `MetaCyc:PWY-6336`, `MetaCyc:PWY-7545`; 4 concrete `CHEBI:*` small-molecule `participants[]` entries) | `A-C8S4-001`: Change `category` from `chemical_entity` to `small_molecule` on all 4 concrete `CHEBI:*` small-molecule effector participants across the 4 affected MetaCyc records, record curation history, and regenerate `pages/` and `output/kgx/`. |
| `F-C8S4-002` | `raw-local-id-structured-reference-titles-4-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 4 `MetaCyc:*` records (`MetaCyc:PWY-6579`, `MetaCyc:PWY-7446`, `MetaCyc:PWY-7722`, `MetaCyc:DENITRIFICATION-PWY`; 17 structured `MetaCyc:*` reaction/complex `references[]` entries) | `A-C8S4-002`: Replace all 17 raw unprefixed frame ID `title == local_id` placeholders with descriptive MetaCyc reaction and enzyme-complex titles across the 4 affected MetaCyc records, record curation history, and refresh `pages/`. |

## Detailed Findings

### `F-C8S4-001`: Four maintained MetaCyc pathway records type 4 concrete `CHEBI:*` small-molecule effector participants as generic `category: chemical_entity` instead of `category: small_molecule`

- **Issue Key**: `concrete-chebi-small-molecule-participants-typed-as-chemical-entity-4-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (4)**:
  - `MetaCyc:SALVADEHYPOX-PWY` (`data/pathways/adenosine-nucleotides-degradation-ii.yaml`): `CHEBI:59640` (`N-acetylglucosamine`, formula `C8H15NO6`, `participants[62].category`, activates `Entrez:945283` in `salvadehypox-edge-087`)
  - `MetaCyc:P184-PWY` (`data/pathways/protocatechuate-meta-cleavage.yaml`): `CHEBI:22651` (`ascorbate`, formula `C6H7O6-`, `participants[61].category`, activates `MetaCyc:CPLX-2701` in `protocatechuate-meta-edge-075`)
  - `MetaCyc:PWY-6336` (`data/pathways/protocatechuate-para-cleavage.yaml`): `CHEBI:22651` (`ascorbate`, formula `C6H7O6-`, `participants[24].category`, activates `MetaCyc:CPLX-7915` in `protocatechuate-para-edge-035`)
  - `MetaCyc:PWY-7545` (`data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`): `CHEBI:203056` (`Microcin J25`, formula `C100H139N23O27`, `participants[27].category`, inhibits `EcoCyc:CYT-D-UBIOX-CPLX` in `pyruvate-bd-edge-030`)
- **Evidence**: `EV-C8-CONCRETE-CHEBI-SMALL-MOLECULE-CHEMICAL-ENTITY-4`
- **Description**:
  Across all 68 `category: chemical_entity` participant entries in the 277-record corpus, 64 represent genuine chemical classes, generic electron/methyl donors or acceptors, carrier-protein conjugates, or amino-acid residues, whereas these 4 `CHEBI:*` participant entries across 4 maintained MetaCyc pathway records are concrete small-molecule effectors with defined molecular formulas typed as generic `category: chemical_entity` instead of `category: small_molecule`, causing `CHEBI:59640`, `CHEBI:22651`, and `CHEBI:203056` to export as generic `biolink:ChemicalEntity` instead of `biolink:SmallMolecule` in `pages/downloads/nodes.tsv`.

### `F-C8S4-002`: Four maintained MetaCyc pathway records retain 17 structured `MetaCyc:*` reaction and enzyme-complex `references[]` entries with raw unprefixed frame ID titles (`title == local_id`) instead of descriptive titles

- **Issue Key**: `raw-local-id-structured-reference-titles-4-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (4)**:
  - `MetaCyc:PWY-6579` (`data/pathways/guanine-and-guanosine-salvage.yaml`): 3 reaction references at `references[3..5]` (`MetaCyc:RXN0-5199` `title: RXN0-5199`, `MetaCyc:GUANPRIBOSYLTRAN-RXN` `title: GUANPRIBOSYLTRAN-RXN`, `MetaCyc:GUANOSINEKIN-RXN` `title: GUANOSINEKIN-RXN`)
  - `MetaCyc:PWY-7446` (`data/pathways/sulfoquinovose-degradation-i.yaml`): 4 reaction references at `references[1..4]` (`MetaCyc:RXN-15296` `title: RXN-15296`, `MetaCyc:RXN-15297` `title: RXN-15297`, `MetaCyc:RXN-15298` `title: RXN-15298`, `MetaCyc:RXN-15299` `title: RXN-15299`)
  - `MetaCyc:PWY-7722` (`data/pathways/sulfoquinovose-degradation-ii.yaml`): 5 reaction references at `references[1..5]` (`MetaCyc:RXN-17096` `title: RXN-17096`, `MetaCyc:RXN-17095` `title: RXN-17095`, `MetaCyc:RXN-17097` `title: RXN-17097`, `MetaCyc:RXN-17098` `title: RXN-17098`, `MetaCyc:RXN-17101` `title: RXN-17101`)
  - `MetaCyc:DENITRIFICATION-PWY` (`data/pathways/nitrate-reduction-i-denitrification.yaml`): 4 reaction references and 1 enzyme-complex reference at `references[1, 3, 4, 5, 63]` (`MetaCyc:RXN-11236` `title: RXN-11236`, `MetaCyc:RXN-15838` `title: RXN-15838`, `MetaCyc:NITRIC-OXIDE-REDUCTASE-RXN` `title: NITRIC-OXIDE-REDUCTASE-RXN`, `MetaCyc:RXN-12130` `title: RXN-12130`, and `MetaCyc:CPLX-1701` `title: CPLX-1701`)
- **Evidence**: `EV-C8-RAW-LOCAL-ID-STRUCTURED-REFERENCE-TITLES-4`
- **Description**:
  Across these 4 maintained MetaCyc pathway records, 17 structured `MetaCyc:*` reaction and enzyme-complex `references[]` entries store an unprefixed raw database frame identifier (`title == local_id`) instead of a descriptive reaction or enzyme complex title.
