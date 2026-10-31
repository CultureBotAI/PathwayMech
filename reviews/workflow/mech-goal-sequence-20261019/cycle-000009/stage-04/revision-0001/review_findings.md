# PathwayMech Cycle 9 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `9`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `8e384d43128ac5777458583683afb5a7bee35db7`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml) (`sha256: c210ca0128b95d60ea2dfee5e4e51a8d13dd7417a6e7d10468f8f65a5db70c8c`)
- **Structured Review ID**: `20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C9S4-001`, `F-C9S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 9 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C9S4-001` | `raw-local-id-structured-reference-titles-3-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 3 `MetaCyc:*` records (`MetaCyc:PWY-8132`, `MetaCyc:PWY-7255`, `MetaCyc:PWY0-1241`; 16 structured `MetaCyc:*` reaction/monomer/metabolite `references[]` entries) | `A-C9S4-001`: Replace all 16 raw unprefixed frame ID `title == local_id` placeholders with descriptive MetaCyc reaction, enzyme monomer, and metabolite titles across the 3 affected MetaCyc records, record curation history, and refresh `pages/`. |
| `F-C9S4-002` | `raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 2 `MetaCyc:*` records (`MetaCyc:THIOREDOX-PWY`, `MetaCyc:PWY-8178`; 11 paired `MetaCyc:*`/`EcoCyc:*` `references[]` entries + 6 `MetaCyc:*` `reactions[]` labels) | `A-C9S4-002`: Replace all 11 raw unprefixed frame ID `title == local_id` placeholders in `MetaCyc:THIOREDOX-PWY` with descriptive MetaCyc/EcoCyc titles, replace the 6 raw frame ID `reactions[].label` values in `MetaCyc:PWY-8178` with descriptive biochemical reaction labels, record curation history, and refresh `pages/` and `output/kgx/`. |

## Detailed Findings

### `F-C9S4-001`: Three maintained MetaCyc pathway records retain 16 structured `MetaCyc:*` reaction, monomer, and metabolite `references[]` entries with raw unprefixed frame ID titles (`title == local_id`) instead of descriptive titles

- **Issue Key**: `raw-local-id-structured-reference-titles-3-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (3)**:
  - `MetaCyc:PWY-8132` (`data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml`): 1 metabolite reference at `references[26]` (`MetaCyc:NADH` `title: NADH`)
  - `MetaCyc:PWY-7255` (`data/pathways/ergothioneine-biosynthesis-i.yaml`): 7 reaction references at `references[1..7]` (`MetaCyc:GLUTCYSLIG-RXN` `title: GLUTCYSLIG-RXN`, `MetaCyc:RXN-14431` `title: RXN-14431`, `MetaCyc:RXN-14430` `title: RXN-14430`, `MetaCyc:RXN-14429` `title: RXN-14429`, `MetaCyc:RXN-18088` `title: RXN-18088`, `MetaCyc:RXN-18089` `title: RXN-18089`, `MetaCyc:RXN-15804` `title: RXN-15804`)
  - `MetaCyc:PWY0-1241` (`data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml`): 5 reaction references and 3 enzyme monomer references at `references[0, 4, 5, 6, 8, 9, 10, 11]` (`MetaCyc:5.1.3.20-RXN` `title: 5.1.3.20-RXN`, `MetaCyc:EG10838-MONOMER` `title: EG10838-MONOMER`, `MetaCyc:G6106-MONOMER` `title: G6106-MONOMER`, `MetaCyc:G7590-MONOMER` `title: G7590-MONOMER`, `MetaCyc:RXN0-4301` `title: RXN0-4301`, `MetaCyc:RXN0-4341` `title: RXN0-4341`, `MetaCyc:RXN0-4342` `title: RXN0-4342`, `MetaCyc:RXN0-4361` `title: RXN0-4361`)
- **Evidence**: `EV-C9-RAW-LOCAL-ID-METACYC-REFERENCE-TITLES-3`
- **Description**:
  Across these 3 maintained MetaCyc pathway records, 16 structured `MetaCyc:*` reaction, monomer, and metabolite `references[]` entries store an unprefixed raw database frame identifier (`title == local_id`) instead of a descriptive reaction, enzyme monomer, or metabolite reference title.

### `F-C9S4-002`: Two maintained MetaCyc pathway records retain 11 paired `MetaCyc:*`/`EcoCyc:*` structured `references[]` entries in `MetaCyc:THIOREDOX-PWY` with raw unprefixed frame ID titles (`title == local_id`) and 6 `MetaCyc:*` `reactions[]` entries in `MetaCyc:PWY-8178` with raw frame ID labels (`label == local_id`)

- **Issue Key**: `raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (2)**:
  - `MetaCyc:THIOREDOX-PWY` (`data/pathways/thioredoxin-pathway.yaml`): 11 structured references at `references[60, 61, 66, 70, 77, 78, 106, 108, 110, 112, 114]` (`MetaCyc:THIOREDOXIN-REDUCT-NADPH-RXN`, `MetaCyc:THIOREDOXIN-RXN`, `MetaCyc:NADPH`, `EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX`, `EcoCyc:REG0-6357`, `EcoCyc:REG0-6358`, `EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN`, `EcoCyc:REG0-10687`, `EcoCyc:REG0-9797`, `EcoCyc:REG0-9025`, `EcoCyc:REG0-9024`)
  - `MetaCyc:PWY-8178` (`data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`): 6 reaction labels at `reactions[0..5].label` (`MetaCyc:RXN-21730` through `MetaCyc:RIBULP3EPIM-RXN`)
- **Evidence**: `EV-C9-RAW-LOCAL-ID-PAIRED-METACYC-ECOCYC-REFS-AND-RXN-LABELS-2`
- **Description**:
  Across these 2 maintained MetaCyc pathway records, 11 paired `MetaCyc:*` and `EcoCyc:*` structured `references[]` entries in `MetaCyc:THIOREDOX-PWY` store an unprefixed raw database frame identifier (`title == local_id`) instead of a descriptive title, and the 6 `MetaCyc:*` `reactions[]` entries in `MetaCyc:PWY-8178` store raw local frame IDs as reaction labels (`label == local_id`).
