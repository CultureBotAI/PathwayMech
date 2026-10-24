# PathwayMech Cycle 4 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `9eae2f9a55e2ec246a4b729735bf06331f3072a2`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml) (`sha256: 0727d8c8d963a0a81c9f4086077a54f67df49d07748a6b22e6217d3dcd5f1da7`)
- **Structured Review ID**: `20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C4S4-001`, `F-C4S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 4 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C4S4-001` | `metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts` | `representation` | `minor` | `open` | `confirmed` | 1 `MetaCyc:*` record (`MetaCyc:ARGDEGRAD-PWY`, `data/pathways/l-arginine-degradation-v.yaml`) | `A-C4S4-001`: Update `description` to replace `hydrogencarbonate` with `carbamate` and `carbon dioxide`, remove orphan participant `CHEBI:17544` (`hydrogencarbonate`) at `participants[14]`, remove unreferenced `RHEA:10154` at `references[9]`, replace generic `RHEA:<ID> authority record` titles on `RHEA:30757`, `RHEA:15650`, `RHEA:19597`, and `RHEA:19513`, record curation history, and refresh `pages/`. |
| `F-C4S4-002` | `metacyc-superseded-unreferenced-rhea-references-in-15-records` | `representation` | `minor` | `open` | `confirmed` | 15 `MetaCyc:*` records (28 unreferenced superseded `RHEA:*` references + 29 generic replacement `RHEA:*` titles) | `A-C4S4-002`: Remove all 28 unreferenced superseded `RHEA:*` entries from `references[]`, replace the 29 generic `RHEA:<ID> authority record` placeholder titles with descriptive Rhea reaction titles across all 15 affected `MetaCyc:*` records, record curation history, and refresh `pages/`. |

## Detailed Findings

### `F-C4S4-001`: `MetaCyc:ARGDEGRAD-PWY` (`l-arginine-degradation-v.yaml`) retains orphan participant `CHEBI:17544` (`hydrogencarbonate`), stale `hydrogencarbonate` prose in `description`, unreferenced `RHEA:10154` in `references[]`, and generic placeholder titles on `RHEA:30757`/`15650`/`19597`/`19513`

- **Issue Key**: `metacyc-argdegrad-pwy-stale-rhea10154-hydrogencarbonate-artifacts`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Target (1)**: `MetaCyc:ARGDEGRAD-PWY` (`data/pathways/l-arginine-degradation-v.yaml`)
- **Affected Field Paths**:
  - `data/pathways/l-arginine-degradation-v.yaml#description`
  - `data/pathways/l-arginine-degradation-v.yaml#participants[14]` (`CHEBI:17544` `hydrogencarbonate`)
  - `data/pathways/l-arginine-degradation-v.yaml#references[9]` (`RHEA:10154`)
  - `data/pathways/l-arginine-degradation-v.yaml#references[11..14].title` (`RHEA:30757`, `RHEA:15650`, `RHEA:19597`, `RHEA:19513`)
- **Evidence**: `EV-C4-ARGDEGRAD-STALE-ARTIFACTS`
- **Description**:
  In `MetaCyc:ARGDEGRAD-PWY` (`data/pathways/l-arginine-degradation-v.yaml`), the carbamate kinase step is modeled as `RHEA:30757` (`carbamoyl phosphate + ADP => carbamate + ATP`, producing `CHEBI:13941` `carbamate`) followed by spontaneous `RHEA:15650` (`carbamate + 2 H(+) => NH4(+) + CO2`, producing `CHEBI:16526` `carbon dioxide`), superseding the composite reaction `RHEA:10154` (`ATP + NH4(+) + hydrogencarbonate = ADP + carbamoyl phosphate + H(+)`). However, three stale artifacts from `RHEA:10154` remain in the record: (1) `description` still states `"converts L-arginine to L-ornithine, ammonium, and hydrogencarbonate"`, (2) `participants[14]` still declares `CHEBI:17544` (`hydrogencarbonate`) with zero incident edges in `mechanistic_edges` (the sole orphan participant across all `7,763` participant entries in the 273-record corpus), and (3) `references[9]` still declares an unreferenced `RHEA:10154` entry while `references[11..14]` (`RHEA:30757`, `RHEA:15650`, `RHEA:19597`, `RHEA:19513`) carry generic `RHEA:<ID> authority record` placeholder titles.

### `F-C4S4-002`: Fifteen maintained `MetaCyc` pathway records retain 28 unreferenced superseded `RHEA:*` entries in `references[]` alongside 29 replacement `RHEA:*` entries with generic `RHEA:<ID> authority record` placeholder titles

- **Issue Key**: `metacyc-superseded-unreferenced-rhea-references-in-15-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (15)**:
  - `MetaCyc:DARABCAT-PWY` (`data/pathways/d-arabinose-degradation-i.yaml`): unreferenced superseded `RHEA:13852` (`references[2]`); generic title on `RHEA:13850` (`references[5].title`)
  - `MetaCyc:GALACTUROCAT-PWY` (`data/pathways/d-galacturonate-degradation-i.yaml`): unreferenced superseded `RHEA:27705` (`references[2]`), `RHEA:17816` (`references[4]`); generic title on `RHEA:27703` (`references[11].title`), `RHEA:17815` (`references[12].title`)
  - `MetaCyc:GLUCARDEG-PWY` (`data/pathways/d-glucarate-degradation-i.yaml`): unreferenced superseded `RHEA:27726` (`references[3]`), `RHEA:27729` (`references[4]`); generic title on `RHEA:27727` (`references[11].title`)
  - `MetaCyc:XYLCAT-PWY` (`data/pathways/d-xylose-degradation-i.yaml`): unreferenced superseded `RHEA:22819` (`references[2]`); generic title on `RHEA:22817` (`references[5].title`)
  - `MetaCyc:GLYCEROLMETAB-PWY` (`data/pathways/glycerol-degradation-v.yaml`): unreferenced superseded `RHEA:13772` (`references[2]`); generic title on `RHEA:13770` (`references[5].title`)
  - `MetaCyc:PWY-6124` (`data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml`): unreferenced superseded `RHEA:10795` (`references[2]`); generic title on `RHEA:10794` (`references[11].title`)
  - `MetaCyc:ARABCAT-PWY` (`data/pathways/l-arabinose-degradation-i.yaml`): unreferenced superseded `RHEA:14824` (`references[2]`), `RHEA:22371` (`references[6]`); generic title on `RHEA:14822` (`references[7].title`), `RHEA:22369` (`references[8].title`)
  - `MetaCyc:FUCCAT-PWY` (`data/pathways/l-fucose-degradation-i.yaml`): unreferenced superseded `RHEA:25583` (`references[2]`), `RHEA:17236` (`references[4]`); generic title on `RHEA:25582` (`references[9].title`), `RHEA:17234` (`references[10].title`)
  - `MetaCyc:ILEUSYN-PWY` (`data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml`): unreferenced superseded `RHEA:22108` (`references[1]`), `RHEA:22109` (`references[2]`); generic title on `RHEA:40676` (`references[16].title`), `RHEA:39968` (`references[17].title`), `RHEA:39976` (`references[18].title`)
  - `MetaCyc:LEUSYN-PWY` (`data/pathways/l-leucine-biosynthesis.yaml`): unreferenced superseded `RHEA:32287` (`references[3]`), `RHEA:32289` (`references[4]`), `RHEA:32271` (`references[5]`), `RHEA:32272` (`references[6]`); generic title on `RHEA:16295` (`references[13].title`), `RHEA:10678` (`references[14].title`), `RHEA:10893` (`references[15].title`), `RHEA:25079` (`references[16].title`)
  - `MetaCyc:HOMOSER-METSYN-PWY` (`data/pathways/l-methionine-biosynthesis-i.yaml`): unreferenced superseded `RHEA:13965` (`references[5]`), `RHEA:13966` (`references[6]`); generic title on `RHEA:43021` (`references[17].title`), `RHEA:40668` (`references[18].title`), `RHEA:40672` (`references[19].title`)
  - `MetaCyc:RHAMCAT-PWY` (`data/pathways/l-rhamnose-degradation-i.yaml`): unreferenced superseded `RHEA:25587` (`references[2]`), `RHEA:23163` (`references[4]`), `RHEA:19692` (`references[8]`); generic title on `RHEA:25585` (`references[10].title`), `RHEA:23161` (`references[11].title`), `RHEA:19690` (`references[12].title`)
  - `MetaCyc:TRPSYN-PWY` (`data/pathways/l-tryptophan-biosynthesis.yaml`): unreferenced superseded `RHEA:10532` (`references[9]`), `RHEA:10533` (`references[10]`); generic title on `RHEA:14082` (`references[16].title`), `RHEA:26435` (`references[17].title`)
  - `MetaCyc:GLUAMCAT-PWY` (`data/pathways/n-acetylglucosamine-degradation-i.yaml`): unreferenced superseded `RHEA:12175` (`references[4]`); generic title on `RHEA:12173` (`references[5].title`)
  - `MetaCyc:NONOXIPENT-PWY` (`data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml`): unreferenced superseded `RHEA:14660` (`references[2]`), `RHEA:13680` (`references[4]`), `RHEA:10511` (`references[6]`), `RHEA:17056` (`references[8]`), `RHEA:27629` (`references[10]`); generic title on `RHEA:14659` (`references[11].title`), `RHEA:13678` (`references[12].title`), `RHEA:10510` (`references[13].title`), `RHEA:17054` (`references[14].title`), `RHEA:27627` (`references[15].title`)
- **Evidence**: `EV-C4-METACYC-SUPERSEDED-RHEA-REFS-15`
- **Description**:
  Across these 15 maintained `MetaCyc:*` pathway records, prior RHEA reaction harmonization replaced directional or anomeric `RHEA:*` reaction nodes and edge citations with canonical master/stereospecific `RHEA:*` IDs, leaving 28 superseded `RHEA:*` entries in `references[]` with zero citations in `mechanistic_edges` and 29 replacement `RHEA:*` entries in `references[]` with generic `RHEA:<ID> authority record` placeholder titles.
