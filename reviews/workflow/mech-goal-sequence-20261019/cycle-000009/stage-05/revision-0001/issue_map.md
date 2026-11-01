# Cycle 9 Stage 5 (`resolve_review_findings`) — Issue Map & Root-Cause Grouping

## 1. Predecessor Evidence & Review Linkage

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019` / Cycle `9` / Stage `5` (`resolve_review_findings`)
- **Git base SHA**: `8f2f8900a1700102259d5cf86cd3c03134c57fcb`
- **Predecessor workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-04/revision-0001/evidence.yaml` (SHA-256 `408845b19529fccbfbf0a42923a1a238ed6bc1cf8c6b260fd8baf0e230c1ed0d`)
- **Predecessor structured review**: `reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml` (`review_id: 20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review`)
- **Successor structured review**: `reviews/structured/20261031T231000Z-cycle9-stage5-resolve-review-findings/review.yaml` (`review_id: 20261031T231000Z-cycle9-stage5-resolve-review-findings`, SHA-256 `a2b9bb5a357500065a2347c75578299463f0dde3d0059dda716816a2476ceb68`)

## 2. Root-Cause Grouping & GitHub Issue Deduplication

Before creating any GitHub issue, open and closed issues in `CultureBotAI/PathwayMech` were searched via `gh issue list --repo CultureBotAI/PathwayMech --state all --limit 100`. Prior Stage 5 raw-title / bare-CURIE issues (`#724`, `#745`, `#753`, `#762`) were closed and scoped to earlier record cohorts (`MetaCyc:PWY-6579`, `MetaCyc:PWY-7446`, `MetaCyc:PWY-7722`, `MetaCyc:DENITRIFICATION-PWY`, etc.). Neither `F-C9S4-001` nor `F-C9S4-002` duplicated an open issue. Because both findings share a single root cause and repair ownership—legacy MetaCyc/EcoCyc importer frame-token strings (`title == local_id` on `references[]` or `label == local_id` on `reactions[]`)—they were grouped into a single root-cause remediation group (`G-C9S5-001`) and tracked under new GitHub issue [#771](https://github.com/CultureBotAI/PathwayMech/issues/771).

| Group ID | Predecessor Findings | Rule ID | Issue Key(s) | GitHub Issue | Repair PR | Target Records | Total Field Updates | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `G-C9S5-001` | `F-C9S4-001`, `F-C9S4-002` | `CURATION:no-raw-local-id-structured-reference-titles` | `raw-local-id-structured-reference-titles-3-metacyc-records`, `raw-local-id-metacyc-ecocyc-reference-titles-and-reaction-labels-2-metacyc-records` | [#771](https://github.com/CultureBotAI/PathwayMech/issues/771) | [#772](https://github.com/CultureBotAI/PathwayMech/pull/772) | `MetaCyc:PWY-8132`, `MetaCyc:PWY-7255`, `MetaCyc:PWY0-1241`, `MetaCyc:THIOREDOX-PWY`, `MetaCyc:PWY-8178` | `27` `references[].title` + `6` `reactions[].label` (`33` total) | `resolved` |

## 3. Record-Level Curation Ledger (`G-C9S5-001`)

| Target ID | File Path | Pre-Curation SHA-256 | Post-Curation SHA-256 | Curation History Path | Updated Fields |
| --- | --- | --- | --- | --- | --- |
| `MetaCyc:PWY-8132` | `data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml` | `5aa35424ed5c8e99270b6defc3b2a5fb850350b157295149f477d2145c143c3b` | `9824120ec979ae03f95b9ac2ebcee6506c62f25b352e56a4d4dc47a6612efa32` | `history/records/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii/2026-10-31T230500Z-antigravity-a1d1e5.yaml` | `1` (`references[26].title`) |
| `MetaCyc:PWY-7255` | `data/pathways/ergothioneine-biosynthesis-i.yaml` | `6d2fb20f5a664a6b7e43e9efb48ac1b65fd59a3e5c5daa1aa95b6bae35184dec` | `e94253e682dc839e3917b7f1f28d2b7c384758be6dcfa17439e451ec3804aa73` | `history/records/ergothioneine-biosynthesis-i/2026-10-31T230500Z-antigravity-a1d1e5.yaml` | `7` (`references[1].title, references[2].title, references[3].title, references[4].title, references[5].title, references[6].title, references[7].title`) |
| `MetaCyc:PWY0-1241` | `data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml` | `03a96e6d64062187955d9e66afc5fe1530880ec64f0f44bfc011675ec48546d6` | `54f54fb3e1ba485704a342681578ec8f8bb1e0c8dc9c93a5f1e5636cc046f3e1` | `history/records/adp-l-glycero-beta-d-manno-heptose-biosynthesis/2026-10-31T230500Z-antigravity-a1d1e5.yaml` | `8` (`references[0].title, references[4].title, references[5].title, references[6].title, references[8].title, references[9].title, references[10].title, references[11].title`) |
| `MetaCyc:THIOREDOX-PWY` | `data/pathways/thioredoxin-pathway.yaml` | `565fbfe8ef69b7728ce8d720c53845071b90938cb845d2cd87db963b13f0080c` | `6ba7bd4434c799c0576ced58654dba8c79058d2288498c5cd9e0a2cec14fac42` | `history/records/thioredoxin-pathway/2026-10-31T230500Z-antigravity-a1d1e5.yaml` | `11` (`references[60].title, references[61].title, references[66].title, references[70].title, references[77].title, references[78].title, references[106].title, references[108].title, references[110].title, references[112].title, references[114].title`) |
| `MetaCyc:PWY-8178` | `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml` | `828076d310a64976bf416e52a9c5acc8ce9979807149c3cc171dfda3db009312` | `01e7513a09bcdd3f0cac559a377757d145bb3764838743469bd811409f8a793a` | `history/records/pentose-phosphate-pathway-non-oxidative-branch-ii/2026-10-31T230500Z-antigravity-a1d1e5.yaml` | `6` (`reactions[0].label, reactions[1].label, reactions[2].label, reactions[3].label, reactions[4].label, reactions[5].label`) |

## 4. Field-Level Remediation Details

### 4.1 `F-C9S4-001` (`MetaCyc:PWY-8132`, `MetaCyc:PWY-7255`, `MetaCyc:PWY0-1241` — 16 `references[].title` updates)

| Pathway ID | Field Path | Reference ID | Before (`title == local_id`) | After (Verified Descriptive Title) |
| --- | --- | --- | --- | --- |
| `MetaCyc:PWY-8132` | `references[26].title` | `MetaCyc:NADH` | `NADH` | `NADH (MetaCyc:NADH)` |
| `MetaCyc:PWY-7255` | `references[1].title` | `MetaCyc:GLUTCYSLIG-RXN` | `GLUTCYSLIG-RXN` | `glutamate--cysteine ligase reaction (MetaCyc:GLUTCYSLIG-RXN)` |
| `MetaCyc:PWY-7255` | `references[2].title` | `MetaCyc:RXN-14431` | `RXN-14431` | `L-histidine N-alpha-methyltransferase reaction (MetaCyc:RXN-14431)` |
| `MetaCyc:PWY-7255` | `references[3].title` | `MetaCyc:RXN-14430` | `RXN-14430` | `N-alpha,N-alpha-dimethyl-L-histidine N-alpha-methyltransferase reaction (MetaCyc:RXN-14430)` |
| `MetaCyc:PWY-7255` | `references[4].title` | `MetaCyc:RXN-14429` | `RXN-14429` | `hercynine/gamma-L-glutamyl-L-cysteine sulfoxide synthase reaction (MetaCyc:RXN-14429)` |
| `MetaCyc:PWY-7255` | `references[5].title` | `MetaCyc:RXN-18088` | `RXN-18088` | `gamma-glutamyl-hercynylcysteine sulfoxide hydrolase reaction (MetaCyc:RXN-18088)` |
| `MetaCyc:PWY-7255` | `references[6].title` | `MetaCyc:RXN-18089` | `RXN-18089` | `hercynylcysteine sulfoxide lyase reaction (MetaCyc:RXN-18089)` |
| `MetaCyc:PWY-7255` | `references[7].title` | `MetaCyc:RXN-15804` | `RXN-15804` | `2-(hydroxysulfanyl)hercynine reduction to ergothioneine (MetaCyc:RXN-15804)` |
| `MetaCyc:PWY0-1241` | `references[0].title` | `MetaCyc:5.1.3.20-RXN` | `5.1.3.20-RXN` | `ADP-glyceromanno-heptose 6-epimerase reaction (MetaCyc:5.1.3.20-RXN)` |
| `MetaCyc:PWY0-1241` | `references[4].title` | `MetaCyc:EG10838-MONOMER` | `EG10838-MONOMER` | `ADP-L-glycero-D-manno-heptose-6-epimerase HldD monomer (MetaCyc:EG10838-MONOMER)` |
| `MetaCyc:PWY0-1241` | `references[5].title` | `MetaCyc:G6106-MONOMER` | `G6106-MONOMER` | `D-sedoheptulose 7-phosphate isomerase GmhA monomer (MetaCyc:G6106-MONOMER)` |
| `MetaCyc:PWY0-1241` | `references[6].title` | `MetaCyc:G7590-MONOMER` | `G7590-MONOMER` | `bifunctional D-glycero-beta-D-manno-heptose 7-phosphate kinase / 1-phosphate adenylyltransferase HldE monomer (MetaCyc:G7590-MONOMER)` |
| `MetaCyc:PWY0-1241` | `references[8].title` | `MetaCyc:RXN0-4301` | `RXN0-4301` | `D-sedoheptulose 7-phosphate isomerase reaction (MetaCyc:RXN0-4301)` |
| `MetaCyc:PWY0-1241` | `references[9].title` | `MetaCyc:RXN0-4341` | `RXN0-4341` | `D-glycero-beta-D-manno-heptose 7-phosphate 1-kinase reaction (MetaCyc:RXN0-4341)` |
| `MetaCyc:PWY0-1241` | `references[10].title` | `MetaCyc:RXN0-4342` | `RXN0-4342` | `D-glycero-beta-D-manno-heptose 1,7-bisphosphate 7-phosphatase reaction (MetaCyc:RXN0-4342)` |
| `MetaCyc:PWY0-1241` | `references[11].title` | `MetaCyc:RXN0-4361` | `RXN0-4361` | `D-glycero-beta-D-manno-heptose 1-phosphate adenylyltransferase reaction (MetaCyc:RXN0-4361)` |

### 4.2 `F-C9S4-002` (`MetaCyc:THIOREDOX-PWY` 11 `references[].title` updates + `MetaCyc:PWY-8178` 6 `reactions[].label` updates)

| Pathway ID | Field Path | Node / Reference ID | Before (`== local_id`) | After (Verified Descriptive Title / Reaction Label) |
| --- | --- | --- | --- | --- |
| `MetaCyc:THIOREDOX-PWY` | `references[60].title` | `MetaCyc:THIOREDOXIN-REDUCT-NADPH-RXN` | `THIOREDOXIN-REDUCT-NADPH-RXN` | `thioredoxin-disulfide reductase reaction (MetaCyc:THIOREDOXIN-REDUCT-NADPH-RXN)` |
| `MetaCyc:THIOREDOX-PWY` | `references[61].title` | `MetaCyc:THIOREDOXIN-RXN` | `THIOREDOXIN-RXN` | `thioredoxin oxidation reaction (MetaCyc:THIOREDOXIN-RXN)` |
| `MetaCyc:THIOREDOX-PWY` | `references[66].title` | `MetaCyc:NADPH` | `NADPH` | `reduced nicotinamide adenine dinucleotide phosphate (MetaCyc:NADPH)` |
| `MetaCyc:THIOREDOX-PWY` | `references[70].title` | `EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX` | `THIOREDOXIN-REDUCT-NADPH-CPLX` | `thioredoxin reductase complex TrxB (EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX)` |
| `MetaCyc:THIOREDOX-PWY` | `references[77].title` | `EcoCyc:REG0-6357` | `REG0-6357` | `OxyR transcriptional activation of trxC (EcoCyc:REG0-6357)` |
| `MetaCyc:THIOREDOX-PWY` | `references[78].title` | `EcoCyc:REG0-6358` | `REG0-6358` | `IscR transcriptional repression of trxC (EcoCyc:REG0-6358)` |
| `MetaCyc:THIOREDOX-PWY` | `references[106].title` | `EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN` | `THIOREDOXIN-REDUCT-NADPH-RXN` | `thioredoxin-disulfide reductase reaction (EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN)` |
| `MetaCyc:THIOREDOX-PWY` | `references[108].title` | `EcoCyc:REG0-10687` | `REG0-10687` | `SoxS transcriptional activation of trxA (EcoCyc:REG0-10687)` |
| `MetaCyc:THIOREDOX-PWY` | `references[110].title` | `EcoCyc:REG0-9797` | `REG0-9797` | `BaeR transcriptional activation of trxA (EcoCyc:REG0-9797)` |
| `MetaCyc:THIOREDOX-PWY` | `references[112].title` | `EcoCyc:REG0-9025` | `REG0-9025` | `ppGpp/DksA transcriptional activation of trxA (EcoCyc:REG0-9025)` |
| `MetaCyc:THIOREDOX-PWY` | `references[114].title` | `EcoCyc:REG0-9024` | `REG0-9024` | `Fis transcriptional repression of trxA (EcoCyc:REG0-9024)` |
| `MetaCyc:PWY-8178` | `reactions[0].label` | `MetaCyc:RXN-21730` | `RXN-21730` | `diphosphate-dependent D-sedoheptulose 7-phosphate 1-phosphotransferase reaction` |
| `MetaCyc:PWY-8178` | `reactions[1].label` | `MetaCyc:SEDOBISALDOL-RXN` | `SEDOBISALDOL-RXN` | `D-sedoheptulose 1,7-bisphosphate aldolase reaction` |
| `MetaCyc:PWY-8178` | `reactions[2].label` | `MetaCyc:1TRANSKETO-RXN` | `1TRANSKETO-RXN` | `transketolase reaction (D-ribose 5-phosphate and D-xylulose 5-phosphate)` |
| `MetaCyc:PWY-8178` | `reactions[3].label` | `MetaCyc:2TRANSKETO-RXN` | `2TRANSKETO-RXN` | `transketolase reaction (D-erythrose 4-phosphate and D-xylulose 5-phosphate)` |
| `MetaCyc:PWY-8178` | `reactions[4].label` | `MetaCyc:RIB5PISOM-RXN` | `RIB5PISOM-RXN` | `D-ribose 5-phosphate isomerase reaction` |
| `MetaCyc:PWY-8178` | `reactions[5].label` | `MetaCyc:RIBULP3EPIM-RXN` | `RIBULP3EPIM-RXN` | `D-ribulose 5-phosphate 3-epimerase reaction` |
