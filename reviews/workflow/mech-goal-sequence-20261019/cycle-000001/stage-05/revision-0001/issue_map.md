# Cycle 1 Stage 5 Issue Map and Finding Dispositions (`mech-goal-sequence-20261019`)

- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Run / Cycle / Stage / Revision**: `mech-goal-sequence-20261019` / Cycle `1` / Stage `5` (`resolve_review_findings`) / Revision `1`
- **Source Git Base (`main`)**: `12a62259e1fa38b8a4094dd23df00d7edc41659f`
- **Scope Frozen At**: `2026-10-22T03:08:27Z`
- **Predecessor Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`sha256: 4f8d1af7488189d8a0de7fe11e5ab21003e67af0380b66654f1fe3334b8c43c7`)
- **Predecessor Structured Review**: `reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml` (`sha256: ad033e8724d2b065a2a132fb15c571f5b6961bde6f56f298d3731735ea2d7ec3`)
- **Successor Structured Review**: `reviews/structured/20261022T033000Z-stage5-resolve-review-findings/review.yaml` (`sha256: 5be86eb8e95c884760ab207bd72954b497aabc34fb3d2c45e2c64066b5e48bc7`)

## 1. Root-Cause Grouping & GitHub Issue Deduplication

Before creating any GitHub issue, all 390 historical issues (33 open, 357 closed) in `CultureBotAI/PathwayMech` were searched via `gh issue list --repo CultureBotAI/PathwayMech --state all --limit 200` and targeted keyword queries (`GLCMANNANAUT`, `ACMANAptspp`, `mixed-reaction-category`, `F-STAGE4-001`, `F-STAGE4-002`). No existing open or closed issue covered the Stage 4 reaction `category` typing findings.

Both Stage 4 carried-forward findings (`F-STAGE4-001` and `F-STAGE4-002`) share a single root cause and repair ownership (`data/pathways/*.yaml` maintained curation records):

| Group ID | Finding IDs | Issue Key(s) | Repair Owner | GitHub Issue | Status |
| --- | --- | --- | --- | --- | --- |
| `G-STAGE5-001` | `F-STAGE4-001`, `F-STAGE4-002` | `amino-sugar-superpathway-bigg-reaction-missing-category`, `mixed-reaction-category-typing-in-maintained-pathways` | Maintained pathway YAML curation (`data/pathways/*.yaml`, 12 records) | [CultureBotAI/PathwayMech#670](https://github.com/CultureBotAI/PathwayMech/issues/670) | `resolved` |

## 2. Finding Dispositions

| Finding ID | Carried From | Issue Key | Severity | Group ID | GitHub Issue | Disposition Status | Resolution Summary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-STAGE4-001` | `F-STAGE4-001` | `amino-sugar-superpathway-bigg-reaction-missing-category` | `minor` | `G-STAGE5-001` | [https://github.com/CultureBotAI/PathwayMech/issues/670](https://github.com/CultureBotAI/PathwayMech/issues/670) | `resolved` | Added `category: molecular_activity` to `reactions[13]` (`BiGG:ACMANAptspp`) in `data/pathways/amino-sugar-superpathway.yaml` (`MetaCyc:GLCMANNANAUT-PWY`), recorded history entry `history/records/amino-sugar-superpathway/2026-10-22T032500Z-antigravity-a1d1e5.yaml`, and regenerated `pages/` so `BiGG:ACMANAptspp` exports as `biolink:MolecularActivity` with `source_category=molecular_activity` in `pages/downloads/nodes.tsv`. |
| `F-STAGE4-002` | `F-STAGE4-002` | `mixed-reaction-category-typing-in-maintained-pathways` | `minor` | `G-STAGE5-001` | [https://github.com/CultureBotAI/PathwayMech/issues/670](https://github.com/CultureBotAI/PathwayMech/issues/670) | `resolved` | Added explicit `category: molecular_activity` to all 33 catalytic reaction entries (`30` `RHEA:*`, `2` `MetaCyc:RXN-*`, `1` `BiGG:ACMANAptspp`) across the 12 mixed-typing `MetaCyc:*` records in `data/pathways/*.yaml`, recorded 12 `history/records/<slug>/2026-10-22T032500Z-antigravity-a1d1e5.yaml` files, and regenerated `pages/` artifacts. Zero maintained records now mix explicit and omitted reaction `category` values. |

## 3. Per-Record Remediation Inventory (12 Maintained Pathway Records, 33 Reaction Entries)

| Pathway ID | File Path | Remediated Reaction Indices & CURIEs | Count | Pre-Fix SHA-256 | Post-Fix SHA-256 | History Record |
| --- | --- | --- | ---: | --- | --- | --- |
| `MetaCyc:SALVADEHYPOX-PWY` | `data/pathways/adenosine-nucleotides-degradation-ii.yaml` | `reactions[1..5]`: `RHEA:29376`, `RHEA:24409`, `RHEA:27647`, `RHEA:24671`, `RHEA:16670` | 5 | `b7f837be8676b08c9a8a0f417ca17a695664e8614b30e7847f4f7e05c845cbf6` | `dc082d3edc6391cd6d85a503e3fbf3e77b96d34f0ee93eecad51f6e6272b1025` | `history/records/adenosine-nucleotides-degradation-ii/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-7971` | `data/pathways/adenosylcobinamide-gdp-salvage-i.yaml` | `reactions[1]`: `RHEA:57693` | 1 | `2e4943a2b36d529ef076e8a8ee561c120e65dc2e8e9c6c4452e2544a180645cd` | `ee0c344a18b4b981b244ee8fcd00e651258990a3323d973fb0d978f47e26efef` | `history/records/adenosylcobinamide-gdp-salvage-i/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY0-41` | `data/pathways/allantoin-degradation-iv-anaerobic.yaml` | `reactions[6]`: `RHEA:15650` | 1 | `bd9c6c24677b6852478f2dd9e2846ade22d13dd722951a50acfb8b4516f1a8fb` | `bf7b150b5b6d0647a1f2b7f4d90c8b3e5ff3c6e73c36f00acc1fe542ba1f034c` | `history/records/allantoin-degradation-iv-anaerobic/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:GLCMANNANAUT-PWY` | `data/pathways/amino-sugar-superpathway.yaml` | `reactions[3..13]`: `RHEA:67737`, `RHEA:67741`, `RHEA:23297`, `RHEA:25254`, `RHEA:25259`, `RHEA:22937`, `RHEA:12173`, `RHEA:28989`, `RHEA:49241`, `RHEA:23881`, `BiGG:ACMANAptspp` | 11 | `fc436f537303f50121c472a4ece19249f3e6eb74d7304933fbafb37e04a61978` | `1c93e912f2e349fbfab5458f309f526fcfc9d381560ac04ba35b7c442f2295f8` | `history/records/amino-sugar-superpathway/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-2503` | `data/pathways/benzoate-degradation-i-aerobic.yaml` | `reactions[5..6]`: `RHEA:12634`, `RHEA:11561` | 2 | `3f8bbb8eceaa4420fa822e87ce01cca6b9d1967908dc117628aba71f54030696` | `1f5d025ef0b00ff3a1bdbaa90bff4f7e38068ba608d9b5e179604c705e0de8f7` | `history/records/benzoate-degradation-i-aerobic/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-1361` | `data/pathways/benzoyl-coa-degradation-i-aerobic.yaml` | `reactions[0..2,4..6]`: `RHEA:48313`, `RHEA:48309`, `RHEA:25392`, `RHEA:76649`, `RHEA:34852`, `RHEA:19483` | 6 | `b2fc0cca6ac455fcc1820766caeb49a13beea64e49477bb774d3893e8bde3fff` | `9bc02c7a8f188c099343f47d6ad7c3f2a33b999209dda2ff93f2bc6356883b70` | `history/records/benzoyl-coa-degradation-i-aerobic/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:CYANCAT-PWY` | `data/pathways/cyanate-degradation.yaml` | `reactions[1]`: `RHEA:15650` | 1 | `7972d75389eb8cc316ff268467d6846351fc313850aa165ae51983bf87ed717f` | `bc0ac1b2ce20a5c3e0eeb98d220e6dc55513ed5eb4fcd9aaadcace5ec1899d84` | `history/records/cyanate-degradation/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-7255` | `data/pathways/ergothioneine-biosynthesis-i.yaml` | `reactions[5..6]`: `MetaCyc:RXN-18089`, `MetaCyc:RXN-15804` | 2 | `238df68728e041e3afe989e226cecf689924db2318fc51dd700b9028f6920527` | `6d2fb20f5a664a6b7e43e9efb48ac1b65fd59a3e5c5daa1aa95b6bae35184dec` | `history/records/ergothioneine-biosynthesis-i/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-5744` | `data/pathways/glyoxylate-assimilation.yaml` | `reactions[0]`: `RHEA:10750` | 1 | `218feaba4c438ac1f7dff5765e5993153040fa1b0cc80b135440ad4ece8622ea` | `a29098d8e62a0aa632744a9c6aa5c4a1a712b38ab93927a7e292691bc64c9392` | `history/records/glyoxylate-assimilation/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-5789` | `data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml` | `reactions[0]`: `RHEA:10750` | 1 | `6a85a549351ff95acd904261afac28bfe5712e553efbd41b3e4bd40ebbcb080a` | `5d8033312de8e878df2437be4e6c78fa1e0c5580f074f13d8225852f2f1e140c` | `history/records/hydroxypropionate-hydroxybutyrate-cycle/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY-6993` | `data/pathways/nicotine-degradation-ii.yaml` | `reactions[1]`: `RHEA:75416` | 1 | `59d1a699b4e40ce680715afa958f8a659feae11b6b1786a5867f25733b83d36c` | `1a79d1bd199a0de57780f18c7d416a91d2b6f69b6f0f025f6ebbd4ac2b788e99` | `history/records/nicotine-degradation-ii/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |
| `MetaCyc:PWY0-1471` | `data/pathways/uracil-degradation-iii.yaml` | `reactions[3]`: `RHEA:15650` | 1 | `ba58586f9b2eb4c29ff6ec99010da3618849dd29d4d023bf2ee82a1c155a4521` | `d138b4df9a26d47451b1a5637de2a39e857e92519874410d7e8170b0f6cbdcdd` | `history/records/uracil-degradation-iii/2026-10-22T032500Z-antigravity-a1d1e5.yaml` |

## 4. Carry-Forward & Unresolved Blockers

- **Carry-Forward Finding IDs (`carry_forward_ids`)**: `[]` (0 open or deferred findings remain).
- **Unresolved Blockers**: None. Exporter/validator hardening for future `BiGG:*` reaction prefixes and automated within-record reaction category consistency checks remains tracked as infrastructure note `pathwaymech-infra-0005` in `INFRA_TASKS.md` for Stage 6 (`implement_infrastructure`).
