# PathwayMech Cycle 1 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `556074d91f600aa9e5ca97e0b4baef6d99513930`
- **Structured Review ID**: `20261022T013600Z-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-STAGE4-001`, `F-STAGE4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-STAGE4-001` | `amino-sugar-superpathway-bigg-reaction-missing-category` | `representation` | `minor` | `open` | `confirmed` | `MetaCyc:GLCMANNANAUT-PWY` (1 record) | `A-STAGE4-001`: Add `category: molecular_activity` to `reactions[13]` (`BiGG:ACMANAptspp`) in `data/pathways/amino-sugar-superpathway.yaml` and refresh `pages/`. |
| `F-STAGE4-002` | `mixed-reaction-category-typing-in-maintained-pathways` | `consistency` | `minor` | `open` | `confirmed` | 12 `MetaCyc:*` records (33 reaction entries) | `A-STAGE4-002`: Standardize explicit `category: molecular_activity` on all 33 omitted catalytic reaction entries across the 12 mixed-typing `MetaCyc:*` records and refresh `pages/`. |

## Detailed Findings

### `F-STAGE4-001`: `BiGG:ACMANAptspp` reaction in `MetaCyc:GLCMANNANAUT-PWY` omits `category: molecular_activity` and exports as `biolink:NamedThing`

- **Issue Key**: `amino-sugar-superpathway-bigg-reaction-missing-category`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Target**: `MetaCyc:GLCMANNANAUT-PWY` (`data/pathways/amino-sugar-superpathway.yaml`)
- **Field Path**: `data/pathways/amino-sugar-superpathway.yaml#reactions[13].category (BiGG:ACMANAptspp)`
- **Evidence**: `EV-GLCMANNANAUT-PWY`, `EV-KGX-EXPORT`, `EV-NODES-TSV`
- **Description**:
  In `data/pathways/amino-sugar-superpathway.yaml` (`MetaCyc:GLCMANNANAUT-PWY`), `reactions[13]` (`BiGG:ACMANAptspp`, `N-acetyl-D-mannosamine transport via PTS  (periplasm)`) omits `category: molecular_activity` while `reactions[0..2]` (`MetaCyc:PWY0-1324`, `MetaCyc:GLUAMCAT-PWY`, `MetaCyc:GLYCOLYSIS`) declare `category: pathway`. Because `BiGG` is not in `_PREFIX_CATEGORIES` in `src/pathwaymech/kgx.py`, `BiGG:ACMANAptspp` falls back to `DEFAULT_CATEGORY` (`biolink:NamedThing`) with an empty `source_category` in `pages/downloads/nodes.tsv` instead of `biolink:MolecularActivity` (`source_category=molecular_activity`).

### `F-STAGE4-002`: Twelve maintained `MetaCyc` pathway records mix explicit and omitted reaction `category` fields within `reactions[]`

- **Issue Key**: `mixed-reaction-category-typing-in-maintained-pathways`
- **Category / Severity / Status / Certainty**: `consistency` / `minor` / `open` / `confirmed`
- **Targets (12)**:
  1. `MetaCyc:SALVADEHYPOX-PWY` (`data/pathways/adenosine-nucleotides-degradation-ii.yaml`) — 5 omitted (`reactions[1..5]`: `RHEA:29376`, `RHEA:24409`, `RHEA:27647`, `RHEA:24671`, `RHEA:16670`)
  2. `MetaCyc:PWY-7971` (`data/pathways/adenosylcobinamide-gdp-salvage-i.yaml`) — 1 omitted (`reactions[1]`: `RHEA:57693`)
  3. `MetaCyc:PWY0-41` (`data/pathways/allantoin-degradation-iv-anaerobic.yaml`) — 1 omitted (`reactions[6]`: `RHEA:15650`)
  4. `MetaCyc:GLCMANNANAUT-PWY` (`data/pathways/amino-sugar-superpathway.yaml`) — 11 omitted (`reactions[3..13]`: `RHEA:67737`, `RHEA:67741`, `RHEA:23297`, `RHEA:25254`, `RHEA:25259`, `RHEA:22937`, `RHEA:12173`, `RHEA:28989`, `RHEA:49241`, `RHEA:23881`, `BiGG:ACMANAptspp`)
  5. `MetaCyc:PWY-2503` (`data/pathways/benzoate-degradation-i-aerobic.yaml`) — 2 omitted (`reactions[5..6]`: `RHEA:12634`, `RHEA:11561`)
  6. `MetaCyc:PWY-1361` (`data/pathways/benzoyl-coa-degradation-i-aerobic.yaml`) — 6 omitted (`reactions[0..2,4..6]`: `RHEA:48313`, `RHEA:48309`, `RHEA:25392`, `RHEA:76649`, `RHEA:34852`, `RHEA:19483`)
  7. `MetaCyc:CYANCAT-PWY` (`data/pathways/cyanate-degradation.yaml`) — 1 omitted (`reactions[1]`: `RHEA:15650`)
  8. `MetaCyc:PWY-7255` (`data/pathways/ergothioneine-biosynthesis-i.yaml`) — 2 omitted (`reactions[5..6]`: `MetaCyc:RXN-18089`, `MetaCyc:RXN-15804`)
  9. `MetaCyc:PWY-5744` (`data/pathways/glyoxylate-assimilation.yaml`) — 1 omitted (`reactions[0]`: `RHEA:10750`)
  10. `MetaCyc:PWY-5789` (`data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml`) — 1 omitted (`reactions[0]`: `RHEA:10750`)
  11. `MetaCyc:PWY-6993` (`data/pathways/nicotine-degradation-ii.yaml`) — 1 omitted (`reactions[1]`: `RHEA:75416`)
  12. `MetaCyc:PWY0-1471` (`data/pathways/uracil-degradation-iii.yaml`) — 1 omitted (`reactions[3]`: `RHEA:15650`)
- **Evidence**: `EV-MIXED-REACTION-CATEGORY-RECORDS`, `EV-GLCMANNANAUT-PWY`, `EV-KGX-EXPORT`, `EV-NODES-TSV`
- **Description**:
  Across these 12 maintained `MetaCyc:*` records, `reactions[]` mixes entries with explicit `category` (`molecular_activity` or `pathway`) and 33 sibling catalytic reaction entries (`30 RHEA:*`, `2 MetaCyc:RXN-*`, `1 BiGG:ACMANAptspp`) that omit `category: molecular_activity`. Standardizing explicit `category: molecular_activity` on all 33 catalytic reaction entries in Stage 5 will align within-record reaction typing and KGX `biolink:MolecularActivity` node export.
