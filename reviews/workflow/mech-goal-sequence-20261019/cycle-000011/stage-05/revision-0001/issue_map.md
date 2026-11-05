# Cycle 11 Stage 5 (`resolve_review_findings`) — Issue Map & Root-Cause Grouping

## 1. Predecessor Evidence & Review Linkage

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019` / Cycle `11` / Stage `5` (`resolve_review_findings`)
- **Git base SHA**: `76578ff449edb6a71d13000353f0832e2a12710e`
- **Predecessor workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0002/evidence.yaml` (SHA-256 `20ef127fa86a0db4ee596a79048b06dfc0e8fbfde5f5667ec94b3e39ccdd7e90`)
- **Predecessor structured review**: `reviews/structured/20261105T040000Z-cycle11-stage4-frozen-corpus-cohort-review-rev2/review.yaml` (`review_id: 20261105T040000Z-cycle11-stage4-frozen-corpus-cohort-review-rev2`, SHA-256 `b6a7e63c23499db8d51132257739195a952955755301c97c3e6c167dd2d13cb7`)
- **Successor structured review**: `reviews/structured/20261105T054000Z-cycle11-stage5-resolve-review-findings/review.yaml` (`review_id: 20261105T054000Z-cycle11-stage5-resolve-review-findings`, SHA-256 `3f33c9acce72d931426546775c460845f414946d36dd3504bef21b5a6d532a98`)

## 2. Root-Cause Grouping & GitHub Issue Deduplication

Before creating any GitHub issue, open and closed issues in `CultureBotAI/PathwayMech` were searched via `gh issue list --repo CultureBotAI/PathwayMech --state all --limit 100`. Prior Stage 5 raw-title / bare-CURIE issues (`#724`, `#745`, `#753`, `#762`, `#771`, `#781`) were closed and scoped to earlier record cohorts. Neither `F-C11S4-001` nor `F-C11S4-002` duplicated an open issue. Because both findings share a single root cause and repair ownership—legacy MetaCyc importer frame-token strings (`title == local_id` on `references[]` or `label == local_id` on `reactions[]`)—they were grouped into a single root-cause remediation group (`G-C11S5-001`) and tracked under new GitHub issue [#791](https://github.com/CultureBotAI/PathwayMech/issues/791).

| Group ID | Predecessor Findings | Rule ID(s) | Issue Key(s) | GitHub Issue | Target Records | Total Field Updates & Dispositions | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `G-C11S5-001` | `F-C11S4-001`, `F-C11S4-002` | `CURATION:no-raw-local-id-structured-reference-titles`, `CURATION:no-raw-local-id-reaction-labels` | `raw-local-id-structured-metacyc-reference-titles-4-records`, `raw-local-id-metacyc-reaction-labels-7-metacyc-records` | [#791](https://github.com/CultureBotAI/PathwayMech/issues/791) | `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, `MetaCyc:THISYN-PWY`, `MetaCyc:PWY0-321`, `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, `MetaCyc:PWY-5177` | `79` `references[].title` + `16` `source_context` `reactions[].label` updated (`95` YAML edits across `7` records) + `33` `native_roles` `reactions[].label` verified as authority-locked frame-only fallbacks | `resolved` |

## 3. Record-Level Curation Ledger (`G-C11S5-001`)

| Target ID | File Path | Pre-Curation SHA-256 | Post-Curation SHA-256 | Curation History Path | Updated / Verified Fields |
| --- | --- | --- | --- | --- | --- |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `data/pathways/biotin-biosynthesis-i.yaml` | `96ef911aa3e61f888318443a3414158c041f66ea1db8e3895630c7317a729f0d` | `2bb360670be1cacab32bb01c5c225b8a3001e7884639382dfdeed47dac161239` | `history/records/biotin-biosynthesis-i/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `31` (`references[1].title, references[2].title, references[3].title, references[12].title, references[13].title, references[14].title, references[15].title, references[16].title, references[18].title, references[20].title, references[22].title, references[24].title, references[26].title, references[28].title, references[30].title, references[32].title, references[33].title, references[34].title, references[35].title, references[36].title, references[37].title, references[38].title, references[39].title, references[40].title, references[41].title, references[42].title, references[43].title, references[44].title, references[45].title, references[46].title, references[47].title`) |
| `MetaCyc:PWY-6823` | `data/pathways/molybdenum-cofactor-biosynthesis.yaml` | `be34e968a813d3542e42036d4b56f0b17a94de1e365f09e160fb95a636fa6eb8` | `72b426dff2696543bbbe47648a42de9bf497bb6b19ea76fd217ce9d8330466bd` | `history/records/molybdenum-cofactor-biosynthesis/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `20` (`references[18].title, references[19].title, references[20].title, references[21].title, references[22].title, references[23].title, references[24].title, references[25].title, references[27].title, references[29].title, references[30].title, references[32].title, references[34].title, references[36].title, references[38].title, references[39].title, references[40].title, references[41].title, references[42].title, references[43].title`) |
| `MetaCyc:CALVIN-PWY` | `data/pathways/calvin-cycle.yaml` | `afbdd8f0562e83d0556f6171b1f5812e82575d53c5baf536c31322280c13adcc` | `322cf7dbc0e6c47bb71c016413e199a001dd1d569e2225af73bbc4111f7e7298` | `history/records/calvin-cycle/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `16` (`references[2].title, references[6].title, references[12].title, references[15].title, references[21].title, references[26].title, references[28].title, references[31].title, references[34].title, references[36].title, references[38].title, references[43].title, references[46].title, references[90].title, references[91].title, references[92].title`) |
| `MetaCyc:THISYN-PWY` | `data/pathways/thiamine-diphosphate-biosynthesis-i.yaml` | `bceec45211c8f3b0c39072d6d8e123944b28c35562bbe0f582a265e8d25ff296` | `7efcdbf561c66b1ef1d3601b9516375757a8572b544df0eadc619af169f5737b` | `history/records/thiamine-diphosphate-biosynthesis-i/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `12` (`references[16].title, references[28].title, references[29].title, references[30].title, references[31].title, references[32].title, references[33].title, references[34].title, references[36].title, references[37].title, references[38].title, references[48].title`) |
| `MetaCyc:P321-PWY` | `data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml` | `32f3d830f2932266bd3fff36fae2e08e738929c282ad46ed4b97f32fa726636d` | `4be0b63bed1fde74849478bf8d3b879fae288e787ce8a3554e900122541642c7` | `history/records/benzoyl-coa-degradation-iii-anaerobic/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `8` (`reactions[0].label, reactions[1].label, reactions[2].label, reactions[3].label, reactions[4].label, reactions[5].label, reactions[6].label, reactions[7].label`) |
| `MetaCyc:CENTBENZCOA-PWY` | `data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml` | `45b132d52f255bc06c2c3892d6d225c920b10469febc474ecb94bb16441fbd3c` | `b903e3a9924a6c2e1cee62d12e3d854194b1f8e78a7664e353a7470f82c4af8e` | `history/records/benzoyl-coa-degradation-ii-anaerobic/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `7` (`reactions[0].label, reactions[1].label, reactions[2].label, reactions[3].label, reactions[4].label, reactions[5].label, reactions[7].label`) |
| `MetaCyc:PWY-5177` | `data/pathways/glutaryl-coa-degradation.yaml` | `3c2ac2ae8443a7bdac87bd8ca9e612eee869fb479f3625231fadf84658e16317` | `26dddc6fb787931723b24ac9eb781aa323c2c4ed23c107245281cf5c5e0a0cd8` | `history/records/glutaryl-coa-degradation/2026-11-05T053500Z-antigravity-a1d1e5.yaml` | `1` (`reactions[0].label`) |
| `MetaCyc:PWY0-321` | `data/pathways/phenylacetate-degradation-i-aerobic.yaml` | `e99722d1ee920cf64aaeae7b00f1de9b59f939bd96a03a7ac5f2885933a72227` | `e99722d1ee920cf64aaeae7b00f1de9b59f939bd96a03a7ac5f2885933a72227` | `N/A (authority-locked via PHENYLACETATE_NODE_ROLES)` | `0` YAML edits (`11` `reactions[].label` verified as authority-locked frame-only fallbacks in `src/pathwaymech/identifiers.py`) |
| `MetaCyc:PWY0-1477` | `data/pathways/ethanolamine-utilization.yaml` | `f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e` | `f1fd9402cab31bf3c62d53ef630abc52308c2c0e2d7b61d7ad6b9c0aaba8fb1e` | `N/A (authority-locked via ETHANOLAMINE_NODE_ROLES)` | `0` YAML edits (`6` `reactions[].label` verified as authority-locked frame-only fallbacks in `src/pathwaymech/identifiers.py`) |
| `MetaCyc:METH-ACETATE-PWY` | `data/pathways/methanogenesis-from-acetate.yaml` | `47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3` | `47d1c71951ce5806e5c9570ee00b2ab9f8634158251ee06821a0f77017b0eca3` | `N/A (authority-locked via ACETATE_METHANOGENESIS_NODE_ROLES)` | `0` YAML edits (`6` `reactions[].label` verified as authority-locked frame-only fallbacks in `src/pathwaymech/identifiers.py`) |
| `MetaCyc:METHANOGENESIS-PWY` | `data/pathways/methanogenesis-from-h2-and-co2.yaml` | `553922ede0ecdb12ebe569dbb9d8af1c70d4aa190e4fd60e69a9bc7ea0cf8e1e` | `553922ede0ecdb12ebe569dbb9d8af1c70d4aa190e4fd60e69a9bc7ea0cf8e1e` | `N/A (authority-locked via METHANOGENESIS_NODE_ROLES)` | `0` YAML edits (`6` `reactions[].label` verified as authority-locked frame-only fallbacks in `src/pathwaymech/identifiers.py`) |

## 4. Field-Level Remediation & Disposition Details

### 4.1 `F-C11S4-001` (`MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, `MetaCyc:THISYN-PWY` — 79 `references[].title` updates)

| Pathway ID | Field Path | Reference ID | Before (`title == local_id`) | After (Verified Descriptive Title) |
| --- | --- | --- | --- | --- |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[1].title` | `MetaCyc:PWY-6519` | `PWY-6519` | `8-amino-7-oxononanoate biosynthesis I (MetaCyc:PWY-6519)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[2].title` | `MetaCyc:PWY0-1507` | `PWY0-1507` | `biotin biosynthesis from 8-amino-7-oxononanoate I (MetaCyc:PWY0-1507)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[3].title` | `MetaCyc:RXN-11475` | `RXN-11475` | `malonyl-[acyl-carrier protein] O-methyltransferase reaction (MetaCyc:RXN-11475)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[12].title` | `MetaCyc:RXN-11483` | `RXN-11483` | `pimeloyl-[acyl-carrier protein] methyl ester esterase reaction (MetaCyc:RXN-11483)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[13].title` | `MetaCyc:RXN-11484` | `RXN-11484` | `8-amino-7-oxononanoate synthase reaction (MetaCyc:RXN-11484)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[14].title` | `MetaCyc:DAPASYN-RXN` | `DAPASYN-RXN` | `adenosylmethionine-8-amino-7-oxononanoate aminotransferase reaction (MetaCyc:DAPASYN-RXN)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[15].title` | `MetaCyc:DETHIOBIOTIN-SYN-RXN` | `DETHIOBIOTIN-SYN-RXN` | `dethiobiotin synthetase reaction (MetaCyc:DETHIOBIOTIN-SYN-RXN)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[16].title` | `MetaCyc:2.8.1.6-RXN` | `2.8.1.6-RXN` | `biotin synthase reaction (MetaCyc:2.8.1.6-RXN)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[18].title` | `MetaCyc:7KAPSYN-MONOMER` | `7KAPSYN-MONOMER` | `8-amino-7-oxononanoate synthase monomer BioF (MetaCyc:7KAPSYN-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[20].title` | `MetaCyc:DAPASYN-MONOMER` | `DAPASYN-MONOMER` | `adenosylmethionine-8-amino-7-oxononanoate aminotransferase monomer BioA (MetaCyc:DAPASYN-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[22].title` | `MetaCyc:DETHIOBIOTIN-SYN-MONOMER` | `DETHIOBIOTIN-SYN-MONOMER` | `dethiobiotin synthetase monomer BioD (MetaCyc:DETHIOBIOTIN-SYN-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[24].title` | `MetaCyc:BIOTIN-SYN-MONOMER` | `BIOTIN-SYN-MONOMER` | `biotin synthase monomer BioB (MetaCyc:BIOTIN-SYN-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[26].title` | `MetaCyc:3-OXOACYL-ACP-REDUCT-MONOMER` | `3-OXOACYL-ACP-REDUCT-MONOMER` | `3-oxoacyl-[acyl-carrier-protein] reductase monomer FabG (MetaCyc:3-OXOACYL-ACP-REDUCT-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[28].title` | `MetaCyc:FABZ-MONOMER` | `FABZ-MONOMER` | `3-hydroxy-acyl-[acyl-carrier-protein] dehydratase monomer FabZ (MetaCyc:FABZ-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[30].title` | `MetaCyc:ENOYL-ACP-REDUCT-NADH-MONOMER` | `ENOYL-ACP-REDUCT-NADH-MONOMER` | `enoyl-[acyl-carrier-protein] reductase [NADH] monomer FabI (MetaCyc:ENOYL-ACP-REDUCT-NADH-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[32].title` | `MetaCyc:FABB-MONOMER` | `FABB-MONOMER` | `beta-ketoacyl-[acyl-carrier-protein] synthase I monomer FabB (MetaCyc:FABB-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[33].title` | `MetaCyc:EG10119-MONOMER` | `EG10119-MONOMER` | `malonyl-[acyl-carrier protein] O-methyltransferase monomer BioC (MetaCyc:EG10119-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[34].title` | `MetaCyc:EG10122-MONOMER` | `EG10122-MONOMER` | `pimeloyl-[acyl-carrier protein] methyl ester esterase monomer BioH (MetaCyc:EG10122-MONOMER)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[35].title` | `MetaCyc:ENZRXN-17863` | `ENZRXN-17863` | `malonyl-[acyl-carrier protein] O-methyltransferase enzymatic reaction (MetaCyc:ENZRXN-17863)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[36].title` | `MetaCyc:ENZRXN-17867` | `ENZRXN-17867` | `3-oxoacyl-[acyl-carrier-protein] reductase FabG glutaryl-step enzymatic reaction (MetaCyc:ENZRXN-17867)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[37].title` | `MetaCyc:ENZRXN-17869` | `ENZRXN-17869` | `3-hydroxy-acyl-[acyl-carrier-protein] dehydratase FabZ glutaryl-step enzymatic reaction (MetaCyc:ENZRXN-17869)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[38].title` | `MetaCyc:ENZRXN-17871` | `ENZRXN-17871` | `enoyl-[acyl-carrier-protein] reductase FabI glutaryl-step enzymatic reaction (MetaCyc:ENZRXN-17871)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[39].title` | `MetaCyc:ENZRXN-17873` | `ENZRXN-17873` | `beta-ketoacyl-[acyl-carrier-protein] synthase I FabB pimeloyl-condensation enzymatic reaction (MetaCyc:ENZRXN-17873)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[40].title` | `MetaCyc:ENZRXN-17868` | `ENZRXN-17868` | `3-oxoacyl-[acyl-carrier-protein] reductase FabG pimeloyl-step enzymatic reaction (MetaCyc:ENZRXN-17868)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[41].title` | `MetaCyc:ENZRXN-17870` | `ENZRXN-17870` | `3-hydroxy-acyl-[acyl-carrier-protein] dehydratase FabZ pimeloyl-step enzymatic reaction (MetaCyc:ENZRXN-17870)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[42].title` | `MetaCyc:ENZRXN-17872` | `ENZRXN-17872` | `enoyl-[acyl-carrier-protein] reductase FabI pimeloyl-step enzymatic reaction (MetaCyc:ENZRXN-17872)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[43].title` | `MetaCyc:ENZRXN-17864` | `ENZRXN-17864` | `pimeloyl-[acyl-carrier protein] methyl ester esterase BioH enzymatic reaction (MetaCyc:ENZRXN-17864)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[44].title` | `MetaCyc:ENZRXN-17865` | `ENZRXN-17865` | `8-amino-7-oxononanoate synthase BioF enzymatic reaction (MetaCyc:ENZRXN-17865)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[45].title` | `MetaCyc:DAPASYN-ENZRXN` | `DAPASYN-ENZRXN` | `adenosylmethionine-8-amino-7-oxononanoate aminotransferase BioA enzymatic reaction (MetaCyc:DAPASYN-ENZRXN)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[46].title` | `MetaCyc:DETHIOBIOTIN-SYN-ENZRXN` | `DETHIOBIOTIN-SYN-ENZRXN` | `dethiobiotin synthetase BioD enzymatic reaction (MetaCyc:DETHIOBIOTIN-SYN-ENZRXN)` |
| `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` | `references[47].title` | `MetaCyc:BIOTIN-SYN-ENZRXN` | `BIOTIN-SYN-ENZRXN` | `biotin synthase BioB enzymatic reaction (MetaCyc:BIOTIN-SYN-ENZRXN)` |
| `MetaCyc:PWY-6823` | `references[18].title` | `MetaCyc:RXN-8340` | `RXN-8340` | `GTP 3',8-cyclase reaction (MetaCyc:RXN-8340)` |
| `MetaCyc:PWY-6823` | `references[19].title` | `MetaCyc:RXN-17809` | `RXN-17809` | `cyclic pyranopterin monophosphate synthase reaction (MetaCyc:RXN-17809)` |
| `MetaCyc:PWY-6823` | `references[20].title` | `MetaCyc:RXN0-308` | `RXN0-308` | `cysteine desulfurase reaction (MetaCyc:RXN0-308)` |
| `MetaCyc:PWY-6823` | `references[21].title` | `MetaCyc:RXN-11361` | `RXN-11361` | `molybdopterin-synthase adenylyltransferase reaction (MetaCyc:RXN-11361)` |
| `MetaCyc:PWY-6823` | `references[22].title` | `MetaCyc:RXN-12473` | `RXN-12473` | `[molybdopterin-synthase sulfur-carrier protein] sulfurtransferase reaction (MetaCyc:RXN-12473)` |
| `MetaCyc:PWY-6823` | `references[23].title` | `MetaCyc:RXN-8342` | `RXN-8342` | `molybdopterin synthase reaction (MetaCyc:RXN-8342)` |
| `MetaCyc:PWY-6823` | `references[24].title` | `MetaCyc:RXN-8344` | `RXN-8344` | `molybdopterin adenylyltransferase reaction (MetaCyc:RXN-8344)` |
| `MetaCyc:PWY-6823` | `references[25].title` | `MetaCyc:RXN-8348` | `RXN-8348` | `molybdopterin molybdotransferase reaction (MetaCyc:RXN-8348)` |
| `MetaCyc:PWY-6823` | `references[27].title` | `MetaCyc:EG11666-MONOMER` | `EG11666-MONOMER` | `cyclic pyranopterin monophosphate synthase monomer MoaC (MetaCyc:EG11666-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[29].title` | `MetaCyc:EG11597-MONOMER` | `EG11597-MONOMER` | `molybdopterin synthase sulfur carrier subunit MoaD (MetaCyc:EG11597-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[30].title` | `MetaCyc:EG11598-MONOMER` | `EG11598-MONOMER` | `molybdopterin synthase catalytic subunit MoaE (MetaCyc:EG11598-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[32].title` | `MetaCyc:EG10154-MONOMER` | `EG10154-MONOMER` | `molybdopterin-synthase adenylyltransferase monomer MoeB (MetaCyc:EG10154-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[34].title` | `MetaCyc:EG11511-MONOMER` | `EG11511-MONOMER` | `molybdopterin adenylyltransferase monomer Mog (MetaCyc:EG11511-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[36].title` | `MetaCyc:EG10153-MONOMER` | `EG10153-MONOMER` | `molybdopterin molybdenumtransferase monomer MoeA (MetaCyc:EG10153-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[38].title` | `MetaCyc:G7325-MONOMER` | `G7325-MONOMER` | `cysteine desulfurase monomer IscS (MetaCyc:G7325-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[39].title` | `MetaCyc:EG11595-MONOMER` | `EG11595-MONOMER` | `GTP 3',8-cyclase monomer MoaA (MetaCyc:EG11595-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[40].title` | `MetaCyc:ENZRXN-19108` | `ENZRXN-19108` | `GTP 3',8-cyclase MoaA enzymatic reaction (MetaCyc:ENZRXN-19108)` |
| `MetaCyc:PWY-6823` | `references[41].title` | `MetaCyc:G6952-MONOMER` | `G6952-MONOMER` | `thiosulfate sulfurtransferase monomer YnjE (MetaCyc:G6952-MONOMER)` |
| `MetaCyc:PWY-6823` | `references[42].title` | `MetaCyc:CPD-19179` | `CPD-19179` | `(8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate compound frame (MetaCyc:CPD-19179)` |
| `MetaCyc:PWY-6823` | `references[43].title` | `MetaCyc:CPD-8123` | `CPD-8123` | `molybdenum cofactor compound frame (MetaCyc:CPD-8123)` |
| `MetaCyc:CALVIN-PWY` | `references[2].title` | `MetaCyc:RIB5PISOM-RXN` | `RIB5PISOM-RXN` | `D-ribose 5-phosphate isomerase reaction (MetaCyc:RIB5PISOM-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[6].title` | `MetaCyc:PHOSPHORIBULOKINASE-RXN` | `PHOSPHORIBULOKINASE-RXN` | `phosphoribulokinase reaction (MetaCyc:PHOSPHORIBULOKINASE-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[12].title` | `MetaCyc:RIBULP3EPIM-RXN` | `RIBULP3EPIM-RXN` | `D-ribulose 5-phosphate 3-epimerase reaction (MetaCyc:RIBULP3EPIM-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[15].title` | `MetaCyc:SEDOHEPTULOSE-BISPHOSPHATASE-RXN` | `SEDOHEPTULOSE-BISPHOSPHATASE-RXN` | `sedoheptulose-1,7-bisphosphatase reaction (MetaCyc:SEDOHEPTULOSE-BISPHOSPHATASE-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[21].title` | `MetaCyc:2TRANSKETO-RXN` | `2TRANSKETO-RXN` | `transketolase reaction (D-fructose 6-phosphate and D-glyceraldehyde 3-phosphate) (MetaCyc:2TRANSKETO-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[26].title` | `MetaCyc:1TRANSKETO-RXN` | `1TRANSKETO-RXN` | `transketolase reaction (D-sedoheptulose 7-phosphate and D-glyceraldehyde 3-phosphate) (MetaCyc:1TRANSKETO-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[28].title` | `MetaCyc:F16BDEPHOS-RXN` | `F16BDEPHOS-RXN` | `fructose-1,6-bisphosphatase reaction (MetaCyc:F16BDEPHOS-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[31].title` | `MetaCyc:SEDOBISALDOL-RXN` | `SEDOBISALDOL-RXN` | `sedoheptulose-1,7-bisphosphate aldolase reaction (MetaCyc:SEDOBISALDOL-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[34].title` | `MetaCyc:F16ALDOLASE-RXN` | `F16ALDOLASE-RXN` | `fructose-1,6-bisphosphate aldolase reaction (MetaCyc:F16ALDOLASE-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[36].title` | `MetaCyc:TRIOSEPISOMERIZATION-RXN` | `TRIOSEPISOMERIZATION-RXN` | `triosephosphate isomerase reaction (MetaCyc:TRIOSEPISOMERIZATION-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[38].title` | `MetaCyc:1.2.1.13-RXN` | `1.2.1.13-RXN` | `glyceraldehyde-3-phosphate dehydrogenase (NADP+) (phosphorylating) reaction (MetaCyc:1.2.1.13-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[43].title` | `MetaCyc:PHOSGLYPHOS-RXN` | `PHOSGLYPHOS-RXN` | `phosphoglycerate kinase reaction (MetaCyc:PHOSGLYPHOS-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[46].title` | `MetaCyc:RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN` | `RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN` | `ribulose-bisphosphate carboxylase reaction (MetaCyc:RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN)` |
| `MetaCyc:CALVIN-PWY` | `references[90].title` | `MetaCyc:REG-8538` | `REG-8538` | `AMP inhibition of CPLX-162 fructose-1,6-bisphosphatase activity (MetaCyc:REG-8538)` |
| `MetaCyc:CALVIN-PWY` | `references[91].title` | `MetaCyc:REG-8539` | `REG-8539` | `AMP inhibition of CPLX-162 sedoheptulose-1,7-bisphosphatase activity (MetaCyc:REG-8539)` |
| `MetaCyc:CALVIN-PWY` | `references[92].title` | `MetaCyc:REG-10188` | `REG-10188` | `Mg2+ allosteric activation of ribulose bisphosphate carboxylase/oxygenase CPLX-105 (MetaCyc:REG-10188)` |
| `MetaCyc:THISYN-PWY` | `references[16].title` | `MetaCyc:CPLX0-743` | `CPLX0-743` | `1-deoxy-D-xylulose-5-phosphate synthase complex (MetaCyc:CPLX0-743)` |
| `MetaCyc:THISYN-PWY` | `references[28].title` | `MetaCyc:RXN0-308` | `RXN0-308` | `cysteine desulfurase reaction (MetaCyc:RXN0-308)` |
| `MetaCyc:THISYN-PWY` | `references[29].title` | `MetaCyc:RXN-9789` | `RXN-9789` | `sulfur-carrier protein ThiS adenylyltransferase reaction (MetaCyc:RXN-9789)` |
| `MetaCyc:THISYN-PWY` | `references[30].title` | `MetaCyc:DXS-RXN` | `DXS-RXN` | `1-deoxy-D-xylulose-5-phosphate synthase reaction (MetaCyc:DXS-RXN)` |
| `MetaCyc:THISYN-PWY` | `references[31].title` | `MetaCyc:RXN-11319` | `RXN-11319` | `2-iminoacetate synthase reaction (MetaCyc:RXN-11319)` |
| `MetaCyc:THISYN-PWY` | `references[32].title` | `MetaCyc:THIAZOLSYN2-RXN` | `THIAZOLSYN2-RXN` | `thiazole synthase reaction (MetaCyc:THIAZOLSYN2-RXN)` |
| `MetaCyc:THISYN-PWY` | `references[33].title` | `MetaCyc:PYRIMSYN1-RXN` | `PYRIMSYN1-RXN` | `phosphomethylpyrimidine synthase reaction (MetaCyc:PYRIMSYN1-RXN)` |
| `MetaCyc:THISYN-PWY` | `references[34].title` | `MetaCyc:PYRIMSYN3-RXN` | `PYRIMSYN3-RXN` | `phosphomethylpyrimidine kinase reaction (MetaCyc:PYRIMSYN3-RXN)` |
| `MetaCyc:THISYN-PWY` | `references[36].title` | `MetaCyc:THI-P-KIN-RXN` | `THI-P-KIN-RXN` | `thiamine-monophosphate kinase reaction (MetaCyc:THI-P-KIN-RXN)` |
| `MetaCyc:THISYN-PWY` | `references[37].title` | `MetaCyc:RXN-14382` | `RXN-14382` | `L-cysteine desulfurase IscS to ThiI sulfur-transfer reaction (MetaCyc:RXN-14382)` |
| `MetaCyc:THISYN-PWY` | `references[38].title` | `MetaCyc:RXN-9788` | `RXN-9788` | `ThiI persulfide to adenylated ThiS sulfur-transfer reaction (MetaCyc:RXN-9788)` |
| `MetaCyc:THISYN-PWY` | `references[48].title` | `MetaCyc:HMP-P-KIN-CPLX` | `HMP-P-KIN-CPLX` | `phosphomethylpyrimidine kinase complex ThiD (MetaCyc:HMP-P-KIN-CPLX)` |

### 4.2 `F-C11S4-002` Part A (`MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY-5177` — 16 `source_context` `reactions[].label` updates)

| Pathway ID | Field Path | Reaction ID | Before (`label == local_id`) | After (Verified Descriptive Reaction Label) |
| --- | --- | --- | --- | --- |
| `MetaCyc:P321-PWY` | `reactions[0].label` | `MetaCyc:1.3.99.15-RXN` | `1.3.99.15-RXN` | `benzoyl-CoA reductase reaction` |
| `MetaCyc:P321-PWY` | `reactions[1].label` | `MetaCyc:R265-RXN` | `R265-RXN` | `cyclohex-1-ene-1-carbonyl-CoA dehydrogenase reaction` |
| `MetaCyc:P321-PWY` | `reactions[2].label` | `MetaCyc:R266-RXN` | `R266-RXN` | `cyclohex-1-ene-1-carboxyl-CoA hydratase reaction` |
| `MetaCyc:P321-PWY` | `reactions[3].label` | `MetaCyc:R267-RXN` | `R267-RXN` | `2-hydroxycyclohexanecarboxyl-CoA dehydrogenase reaction` |
| `MetaCyc:P321-PWY` | `reactions[4].label` | `MetaCyc:R268-RXN` | `R268-RXN` | `2-ketocyclohexanecarboxyl-CoA hydrolase reaction` |
| `MetaCyc:P321-PWY` | `reactions[5].label` | `MetaCyc:1.3.1.62-RXN` | `1.3.1.62-RXN` | `pimeloyl-CoA dehydrogenase reaction` |
| `MetaCyc:P321-PWY` | `reactions[6].label` | `MetaCyc:RXN-8031` | `RXN-8031` | `6-carboxyhex-2-enoyl-CoA hydratase reaction` |
| `MetaCyc:P321-PWY` | `reactions[7].label` | `MetaCyc:1.1.1.259-RXN` | `1.1.1.259-RXN` | `3-hydroxypimeloyl-CoA dehydrogenase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[0].label` | `MetaCyc:1.3.99.15-RXN` | `1.3.99.15-RXN` | `benzoyl-CoA reductase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[1].label` | `MetaCyc:4.2.1.100-RXN` | `4.2.1.100-RXN` | `cyclohexa-1,5-diene-1-carbonyl-CoA hydratase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[2].label` | `MetaCyc:HADTHAUERA-RXN` | `HADTHAUERA-RXN` | `6-hydroxycyclohex-1-ene-1-carbonyl-CoA dehydrogenase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[3].label` | `MetaCyc:RXN-15012` | `RXN-15012` | `6-oxocyclohex-1-ene-1-carbonyl-CoA hydratase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[4].label` | `MetaCyc:RXN-15013` | `RXN-15013` | `2-hydroxy-6-oxocyclohexane-1-carbonyl-CoA hydrolase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[5].label` | `MetaCyc:1.1.1.259-RXN` | `1.1.1.259-RXN` | `3-hydroxypimeloyl-CoA dehydrogenase reaction` |
| `MetaCyc:CENTBENZCOA-PWY` | `reactions[7].label` | `MetaCyc:OAHTHAUERA-RXN` | `OAHTHAUERA-RXN` | `6-oxocyclohex-1-ene-1-carbonyl-CoA hydrolase reaction` |
| `MetaCyc:PWY-5177` | `reactions[0].label` | `MetaCyc:ACETYL-COA-ACETYLTRANSFER-RXN` | `ACETYL-COA-ACETYLTRANSFER-RXN` | `acetyl-CoA C-acetyltransferase reaction` |

### 4.3 `F-C11S4-002` Part B (`MetaCyc:PWY0-321`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, `MetaCyc:PWY-5177[1..4]` — 33 Authority-Locked `native_roles` Reaction Labels)

Per `src/pathwaymech/identifiers.py` lines 783–806 (`native_roles = PHENYLACETATE_NODE_ROLES | GLUTARYL_NODE_ROLES | METHANOGENESIS_NODE_ROLES | ACETATE_METHANOGENESIS_NODE_ROLES | ETHANOLAMINE_NODE_ROLES`), complete native issuing-original profiles enforce that *"Source-derived names and explicit frame-only fallbacks cannot be overridden by a namespace's broad contextual-label rule"* because the issuing MetaCyc `<Reaction>` XML frames for these 33 reactions lack a direct `<common-name>` slot. Their human-readable biochemical step descriptions are preserved in `reactions[].description` and on the paired `<Enzymatic-Reaction>` participant nodes.

| Pathway ID | Field Path | Reaction ID | Authority-Locked `label` | Enforcing `native_roles` Profile | Preserved Step `description` |
| --- | --- | --- | --- | --- | --- |
| `MetaCyc:PWY0-321` | `reactions[0].label` | `MetaCyc:RXN-10819` | `RXN-10819` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[1].label` | `MetaCyc:RXN0-2042` | `RXN0-2042` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[2].label` | `MetaCyc:RXN0-6510` | `RXN0-6510` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[3].label` | `MetaCyc:RXNMETA-12671` | `RXNMETA-12671` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[4].label` | `MetaCyc:RXNMETA-12672` | `RXNMETA-12672` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[5].label` | `MetaCyc:RXN0-6512` | `RXN0-6512` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[6].label` | `MetaCyc:RXN-2425` | `RXN-2425` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[7].label` | `MetaCyc:RXN0-2044` | `RXN0-2044` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[8].label` | `MetaCyc:RXN-3641` | `RXN-3641` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[9].label` | `MetaCyc:RXN-17752` | `RXN-17752` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-321` | `reactions[10].label` | `MetaCyc:RXN0-7103` | `RXN0-7103` | `PHENYLACETATE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-1477` | `reactions[0].label` | `MetaCyc:ACETALD-DEHYDROG-RXN` | `ACETALD-DEHYDROG-RXN` | `ETHANOLAMINE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-1477` | `reactions[1].label` | `MetaCyc:ACETATEKIN-RXN` | `ACETATEKIN-RXN` | `ETHANOLAMINE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-1477` | `reactions[2].label` | `MetaCyc:ALCOHOL-DEHYDROG-RXN` | `ALCOHOL-DEHYDROG-RXN` | `ETHANOLAMINE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-1477` | `reactions[3].label` | `MetaCyc:ETHAMLY-RXN` | `ETHAMLY-RXN` | `ETHANOLAMINE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-1477` | `reactions[4].label` | `MetaCyc:PHOSACETYLTRANS-RXN` | `PHOSACETYLTRANS-RXN` | `ETHANOLAMINE_NODE_ROLES` | `` |
| `MetaCyc:PWY0-1477` | `reactions[5].label` | `MetaCyc:RXN-19336` | `RXN-19336` | `ETHANOLAMINE_NODE_ROLES` | `` |
| `MetaCyc:METH-ACETATE-PWY` | `reactions[0].label` | `MetaCyc:1.2.7.4-RXN` | `1.2.7.4-RXN` | `ACETATE_METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METH-ACETATE-PWY` | `reactions[1].label` | `MetaCyc:ACETATEKIN-RXN` | `ACETATEKIN-RXN` | `ACETATE_METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METH-ACETATE-PWY` | `reactions[2].label` | `MetaCyc:ACETYLSYNCLTH-RXN` | `ACETYLSYNCLTH-RXN` | `ACETATE_METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METH-ACETATE-PWY` | `reactions[3].label` | `MetaCyc:MTRMBARK-RXN` | `MTRMBARK-RXN` | `ACETATE_METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METH-ACETATE-PWY` | `reactions[4].label` | `MetaCyc:PHOSACETYLTRANS-RXN` | `PHOSACETYLTRANS-RXN` | `ACETATE_METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METH-ACETATE-PWY` | `reactions[5].label` | `MetaCyc:RXN-12908` | `RXN-12908` | `ACETATE_METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METHANOGENESIS-PWY` | `reactions[0].label` | `MetaCyc:2.1.1.86-RXN` | `2.1.1.86-RXN` | `METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METHANOGENESIS-PWY` | `reactions[1].label` | `MetaCyc:2.3.1.101-RXN` | `2.3.1.101-RXN` | `METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METHANOGENESIS-PWY` | `reactions[2].label` | `MetaCyc:3.5.4.27-RXN` | `3.5.4.27-RXN` | `METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METHANOGENESIS-PWY` | `reactions[3].label` | `MetaCyc:FORMYLMETHANOFURAN-DEHYDROGENASE-RXN` | `FORMYLMETHANOFURAN-DEHYDROGENASE-RXN` | `METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METHANOGENESIS-PWY` | `reactions[4].label` | `MetaCyc:H2-METHYLENE-THMPT-DEHYDRO-RXN` | `H2-METHYLENE-THMPT-DEHYDRO-RXN` | `METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:METHANOGENESIS-PWY` | `reactions[5].label` | `MetaCyc:METHELENE-THMPT-OXI-RXN` | `METHELENE-THMPT-OXI-RXN` | `METHANOGENESIS_NODE_ROLES` | `` |
| `MetaCyc:PWY-5177` | `reactions[1].label` | `MetaCyc:GLUTACONYL-COA-DECARBOXYLASE-RXN` | `GLUTACONYL-COA-DECARBOXYLASE-RXN` | `GLUTARYL_NODE_ROLES` | `` |
| `MetaCyc:PWY-5177` | `reactions[2].label` | `MetaCyc:GLUTARYL-COA-DEHYDROG-RXN` | `GLUTARYL-COA-DEHYDROG-RXN` | `GLUTARYL_NODE_ROLES` | `` |
| `MetaCyc:PWY-5177` | `reactions[3].label` | `MetaCyc:GLUTARYL-COA-DEHYDROGENASE-RXN` | `GLUTARYL-COA-DEHYDROGENASE-RXN` | `GLUTARYL_NODE_ROLES` | `` |
| `MetaCyc:PWY-5177` | `reactions[4].label` | `MetaCyc:RXN-11662` | `RXN-11662` | `GLUTARYL_NODE_ROLES` | `` |
