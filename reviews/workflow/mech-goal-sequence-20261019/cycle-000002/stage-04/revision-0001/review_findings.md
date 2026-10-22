# PathwayMech Cycle 2 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `e369fa425e64d4f794ce84e2fd71138a43660467`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml) (`sha256: 8179b1fbe2d53c88fac719216c530765c2a442d3a43e8a0395bc2062c279a2c6`)
- **Structured Review ID**: `20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C2S4-001`, `F-C2S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 2 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C2S4-001` | `cross-record-shared-reaction-category-inconsistency` | `consistency` | `minor` | `open` | `confirmed` | 16 `MetaCyc:*` records (28 occurrences across 23 shared reaction CURIEs) | `A-C2S4-001`: Add `category: molecular_activity` to all 28 untyped occurrences of the 23 shared reaction CURIEs across the 16 affected `MetaCyc:*` records. |
| `F-C2S4-002` | `corpus-wide-untyped-reactions-in-56-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 56 `MetaCyc:*` records (279 reaction entries: 263 `RHEA:*` + 16 `MetaCyc:*`) | `A-C2S4-002`: Standardize explicit `category: molecular_activity` across all 279 catalytic reaction entries in the 56 untyped `MetaCyc:*` records, record curation history, and refresh `pages/`. |

## Detailed Findings

### `F-C2S4-001`: Sixteen maintained `MetaCyc` pathway records omit `category: molecular_activity` on 28 occurrences of 23 reaction CURIEs that are explicitly typed in sibling records

- **Issue Key**: `cross-record-shared-reaction-category-inconsistency`
- **Category / Severity / Status / Certainty**: `consistency` / `minor` / `open` / `confirmed`
- **Targets (16)**:
  `MetaCyc:ARABCAT-PWY`, `MetaCyc:ARGDEGRAD-PWY`, `MetaCyc:CALVIN-PWY`, `MetaCyc:DAPLYSINESYN-PWY`, `MetaCyc:GALACTUROCAT-PWY`, `MetaCyc:GLUAMCAT-PWY`, `MetaCyc:GLUCARDEG-PWY`, `MetaCyc:GLUTATHIONESYN-PWY`, `MetaCyc:HOMOSER-THRESYN-PWY`, `MetaCyc:HOMOSERSYN-PWY`, `MetaCyc:NONMEVIPP-PWY`, `MetaCyc:NONOXIPENT-PWY`, `MetaCyc:OXIDATIVEPENT-PWY`, `MetaCyc:P101-PWY`, `MetaCyc:PWY-8383`, `MetaCyc:PYRIDOXSYN-PWY`
- **Shared Reaction CURIEs (23)**:
  `MetaCyc:DHBAMPLIG-RXN`, `RHEA:10509`, `RHEA:10841`, `RHEA:12173`, `RHEA:12557`, `RHEA:12606`, `RHEA:13286`, `RHEA:13679`, `RHEA:13986`, `RHEA:14659`, `RHEA:15650`, `RHEA:15763`, `RHEA:17090`, `RHEA:17462`, `RHEA:22369`, `RHEA:22937`, `RHEA:23777`, `RHEA:24286`, `RHEA:27378`, `RHEA:27628`, `RHEA:30168`, `RHEA:30757`, `RHEA:34172`
- **Evidence**: `EV-C2-SHARED-REACTION-INCONSISTENCY`, `EV-C2-KGX-EXPORT`, `EV-C2-NODES-TSV`
- **Description**:
  Across these 16 maintained `MetaCyc:*` records, 28 `reactions[]` entries spanning 23 shared catalytic reaction CURIEs omit `category: molecular_activity` even though those exact same 23 reaction CURIEs explicitly declare `category: molecular_activity` in sibling maintained pathway records (`PathBank:SMP0000992`, `PathBank:SMP0002406`, `KEGG:M00008`, `MetaCyc:CYANCAT-PWY`, `MetaCyc:GALACTARDEG-PWY`, `MetaCyc:GLCMANNANAUT-PWY`, `MetaCyc:LYXMET-PWY`, `MetaCyc:PWY-5903`, `MetaCyc:PWY-7255`, `MetaCyc:PWY0-1300`, `MetaCyc:PWY0-1471`, `MetaCyc:PWY0-301`, `MetaCyc:PWY0-41`, and `MetaCyc:THISYN-PWY`). In `pages/downloads/nodes.tsv`, `_add_node` in `src/pathwaymech/kgx.py` promotes each of these 23 deduplicated nodes to `biolink:MolecularActivity` (`source_category=molecular_activity`) while serializing mixed reaction contexts (with and without `"category": "molecular_activity"`) inside `source_contexts`.

### `F-C2S4-002`: Fifty-six maintained `MetaCyc` pathway records omit explicit `category: molecular_activity` across all 279 `reactions[]` entries

- **Issue Key**: `corpus-wide-untyped-reactions-in-56-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (56)**:
  All 56 maintained `MetaCyc:*` pathway records that omit `category` on `reactions[]` (16 records in `F-C2S4-001` with 87 total reactions + 40 additional `MetaCyc:*` records with 192 total reactions = 279 catalytic reaction occurrences: 263 `RHEA:*` and 16 `MetaCyc:*`, spanning 254 unique reaction CURIEs).
- **Evidence**: `EV-C2-UNTYPED-56-METACYC-RECORDS`, `EV-C2-SHARED-REACTION-INCONSISTENCY`, `EV-C2-KGX-EXPORT`, `EV-C2-NODES-TSV`
- **Description**:
  Across the 271 maintained pathway records, 212 records with `reactions[]` (`86 gomodel:*`, `84 MetaCyc:*`, `12 WikiPathways:*`, `11 PathBank:*`, `10 GO:*`, `6 Reactome:*`, `3 KEGG:*`) explicitly declare `category` on 100% of their 1,318 reaction entries (`1,312 molecular_activity` and `6 pathway`) and 3 `MIBiG:*` records have 0 `reactions[]`, whereas these 56 maintained `MetaCyc:*` records omit `category: molecular_activity` across all 279 of their `reactions[]` entries. Because 231 unique reaction CURIEs (`216 RHEA:*` and `15 MetaCyc:*`) appear exclusively in these 56 records, `src/pathwaymech/kgx.py` exports them in `pages/downloads/nodes.tsv` via `_PREFIX_CATEGORIES` fallback as `biolink:BiochemicalReaction` with an empty `source_category` (`""`) instead of `biolink:MolecularActivity` (`source_category=molecular_activity`). Standardizing explicit `category: molecular_activity` on all 279 catalytic reaction entries across these 56 `MetaCyc:*` records in Cycle 2 Stage 5 will bring 100% of the 271-record corpus (`1,597 / 1,597` reactions) to explicit `category` typing and uniform KGX export.
