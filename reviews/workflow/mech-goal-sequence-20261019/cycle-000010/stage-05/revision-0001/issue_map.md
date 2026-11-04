# Cycle 10 Stage 5 (`resolve_review_findings`) — Issue Map & Root-Cause Grouping

## 1. Predecessor Evidence & Review Linkage

- **Run / Cycle / Stage**: `mech-goal-sequence-20261019` / Cycle `10` / Stage `5` (`resolve_review_findings`)
- **Git base SHA**: `80deae2e3bc3c79eb57f4e434581e8744ddd0167`
- **Predecessor workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0002/evidence.yaml` (SHA-256 `a21d5053725717a5df06cd3b9fe915a998fdf6a817b5dd3065e078f91daa7f2c`)
- **Predecessor structured review**: `reviews/structured/20261101T082500Z-cycle10-stage4-frozen-corpus-cohort-review-rev2/review.yaml` (`review_id: 20261101T082500Z-cycle10-stage4-frozen-corpus-cohort-review-rev2`, SHA-256 `8969af2dc829d18f9f2096d0560e96c9166106896966f93987cfe717c1b4ed35`)
- **Successor structured review**: `reviews/structured/20261104T015200Z-cycle10-stage5-resolve-review-findings/review.yaml` (`review_id: 20261104T015200Z-cycle10-stage5-resolve-review-findings`, SHA-256 `4737939a20eb37465b7cc84334c3530366fc6794734af1a558e8f08ca75a4f2a`)

## 2. Root-Cause Grouping & GitHub Issue Deduplication

Before creating any GitHub issue, open and closed issues in `CultureBotAI/PathwayMech` were searched via `gh issue list --repo CultureBotAI/PathwayMech --state all --limit 100`. Prior Stage 5 raw-title / bare-CURIE issues (`#724`, `#745`, `#753`, `#762`, `#771`) were closed and scoped to earlier record cohorts (`MetaCyc:PWY-8132`, `MetaCyc:PWY-7255`, `MetaCyc:PWY0-1241`, `MetaCyc:THIOREDOX-PWY`, `MetaCyc:PWY-8178`, etc.). Neither `F-C10S4-001` nor `F-C10S4-002` duplicated an open issue. Because both findings share a single root cause and repair ownership—legacy MetaCyc/EcoCyc importer frame-token strings (`title == local_id` on `references[]` or `label == local_id` on `reactions[]`)—they were grouped into a single root-cause remediation group (`G-C10S5-001`) and tracked under new GitHub issue [#781](https://github.com/CultureBotAI/PathwayMech/issues/781).

| Group ID | Predecessor Findings | Rule ID(s) | Issue Key(s) | GitHub Issue | Repair PR | Target Records | Total Field Updates | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `G-C10S5-001` | `F-C10S4-001`, `F-C10S4-002` | `CURATION:no-raw-local-id-structured-reference-titles`, `CURATION:no-raw-local-id-reaction-labels` | `raw-local-id-structured-reference-titles-2-records`, `raw-local-id-metacyc-reaction-labels-4-records` | [#781](https://github.com/CultureBotAI/PathwayMech/issues/781) | [#782](https://github.com/CultureBotAI/PathwayMech/pull/782) | `GO:0043427`, `MetaCyc:PWY-5744`, `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545` | `26` `references[].title` + `9` `reactions[].label` (`35` total) | `resolved` |

## 3. Record-Level Curation Ledger (`G-C10S5-001`)

| Target ID | File Path | Pre-Curation SHA-256 | Post-Curation SHA-256 | Curation History Path | Updated Fields |
| --- | --- | --- | --- | --- | --- |
| `GO:0043427` | `data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml` | `92e0c1a1a4f2ae4ebf5986a711a51788116037953a76e5ae0681097dcc5c4100` | `43690bab21e93a6be11922c7e9bc7a69136712814c12792544d7cfa7bb82905c` | `history/records/carbon-fixation-by-3-hydroxypropionate-cycle/2026-11-04T014200Z-antigravity-a1d1e5.yaml` | `13` (`references[11].title, references[13].title, references[15].title, references[17].title, references[19].title, references[21].title, references[23].title, references[25].title, references[27].title, references[29].title, references[31].title, references[33].title, references[37].title`) |
| `MetaCyc:PWY-5744` | `data/pathways/glyoxylate-assimilation.yaml` | `d0df038ad2114f8f5a27dae2a208764180c45f5f370c6a6a7a6cc4ad7980c22d` | `28e0fdabc83307309eaf433fa061191a82f917d99ebcdcadb73797c5992780ea` | `history/records/glyoxylate-assimilation/2026-11-04T014200Z-antigravity-a1d1e5.yaml` | `13` (`references[11].title, references[13].title, references[15].title, references[17].title, references[19].title, references[21].title, references[23].title, references[25].title, references[27].title, references[29].title, references[31].title, references[33].title, references[35].title`) |
| `MetaCyc:ACETOACETATE-DEG-PWY` | `data/pathways/acetoacetate-degradation.yaml` | `233b3b864987d0d4bd5434236eb7289624137abbaaa194e936766ebe344d92e4` | `cb0e61c5d265e6634beb6dbc8bdbc7b9723b75a53aee11204520f5b54ff94290` | `history/records/acetoacetate-degradation/2026-11-04T014200Z-antigravity-a1d1e5.yaml` | `4` (`reactions[0].label, reactions[1].label, reactions[2].label, reactions[3].label`) |
| `MetaCyc:PWY-1361` | `data/pathways/benzoyl-coa-degradation-i-aerobic.yaml` | `91552e9b4f36ece175f6cee1ff384423f11ddfbb76ce2ec1dd4b4b87cc2d7f08` | `0dcaa9927b4907c2a0ace6a40ed59f841dffb45708ca4d49a6959621e9dfe99b` | `history/records/benzoyl-coa-degradation-i-aerobic/2026-11-04T014200Z-antigravity-a1d1e5.yaml` | `1` (`reactions[3].label`) |
| `MetaCyc:PWY0-1352` | `data/pathways/nitrate-reduction-viii.yaml` | `5243f546a62490581e35d29516f2ecb830b1284748d6b2b042b82e7d9f6303b7` | `a7ac9a583ed038c8f5cf6dd38131fcf7285c5dc0403c87df6b36c43d9036ca28` | `history/records/nitrate-reduction-viii/2026-11-04T014200Z-antigravity-a1d1e5.yaml` | `2` (`reactions[0].label, reactions[1].label`) |
| `MetaCyc:PWY-7545` | `data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml` | `08884edf95974a98a5dd9cc2583638b730fc0a8de687ab6b0e24461b68a50a7d` | `f2970a865bed13e70e05ec1d27e89cd415790aa64584fa526abd1c391c1d0104` | `history/records/pyruvate-to-cytochrome-bd-oxidase-electron-transfer/2026-11-04T014200Z-antigravity-a1d1e5.yaml` | `2` (`reactions[0].label, reactions[1].label`) |

## 4. Field-Level Remediation Details

### 4.1 `F-C10S4-001` (`GO:0043427`, `MetaCyc:PWY-5744` — 26 `references[].title` updates)

| Pathway ID | Field Path | Reference ID | Before (`title == local_id`) | After (Verified Descriptive Title) |
| --- | --- | --- | --- | --- |
| `GO:0043427` | `references[11].title` | `MetaCyc:RXN0-5224` | `RXN0-5224` | `carbonic anhydrase reaction (MetaCyc:RXN0-5224)` |
| `GO:0043427` | `references[13].title` | `MetaCyc:BIOTIN-CARBOXYL-RXN` | `BIOTIN-CARBOXYL-RXN` | `biotin carboxylase reaction (MetaCyc:BIOTIN-CARBOXYL-RXN)` |
| `GO:0043427` | `references[15].title` | `MetaCyc:RXN0-5055` | `RXN0-5055` | `acetyl-CoA carboxyltransferase reaction (MetaCyc:RXN0-5055)` |
| `GO:0043427` | `references[17].title` | `MetaCyc:RXN-8963` | `RXN-8963` | `malonyl-CoA reductase (malonate semialdehyde-forming) reaction (MetaCyc:RXN-8963)` |
| `GO:0043427` | `references[19].title` | `MetaCyc:RXN-8974` | `RXN-8974` | `malonate semialdehyde reductase (3-hydroxypropionate-forming) reaction (MetaCyc:RXN-8974)` |
| `GO:0043427` | `references[21].title` | `MetaCyc:RXN-9086` | `RXN-9086` | `3-hydroxypropionate---CoA ligase (AMP-forming) reaction (MetaCyc:RXN-9086)` |
| `GO:0043427` | `references[23].title` | `MetaCyc:RXN-6383` | `RXN-6383` | `3-hydroxypropionyl-CoA dehydratase reaction (MetaCyc:RXN-6383)` |
| `GO:0043427` | `references[25].title` | `MetaCyc:RXN-9087` | `RXN-9087` | `acryloyl-CoA reductase (NADPH) reaction (MetaCyc:RXN-9087)` |
| `GO:0043427` | `references[27].title` | `MetaCyc:PROPIONYL-COA-CARBOXY-RXN` | `PROPIONYL-COA-CARBOXY-RXN` | `propionyl-CoA carboxylase reaction (MetaCyc:PROPIONYL-COA-CARBOXY-RXN)` |
| `GO:0043427` | `references[29].title` | `MetaCyc:METHYLMALONYL-COA-EPIM-RXN` | `METHYLMALONYL-COA-EPIM-RXN` | `methylmalonyl-CoA epimerase reaction (MetaCyc:METHYLMALONYL-COA-EPIM-RXN)` |
| `GO:0043427` | `references[31].title` | `MetaCyc:METHYLMALONYL-COA-MUT-RXN` | `METHYLMALONYL-COA-MUT-RXN` | `methylmalonyl-CoA mutase reaction (MetaCyc:METHYLMALONYL-COA-MUT-RXN)` |
| `GO:0043427` | `references[33].title` | `MetaCyc:RXN-8964` | `RXN-8964` | `succinyl-CoA:(S)-malate CoA-transferase reaction (MetaCyc:RXN-8964)` |
| `GO:0043427` | `references[37].title` | `MetaCyc:MALYL-COA-LYASE-RXN` | `MALYL-COA-LYASE-RXN` | `(S)-malyl-CoA lyase reaction (MetaCyc:MALYL-COA-LYASE-RXN)` |
| `MetaCyc:PWY-5744` | `references[11].title` | `MetaCyc:RXN0-5224` | `RXN0-5224` | `carbonic anhydrase reaction (MetaCyc:RXN0-5224)` |
| `MetaCyc:PWY-5744` | `references[13].title` | `MetaCyc:BIOTIN-CARBOXYL-RXN` | `BIOTIN-CARBOXYL-RXN` | `biotin carboxylase reaction (MetaCyc:BIOTIN-CARBOXYL-RXN)` |
| `MetaCyc:PWY-5744` | `references[15].title` | `MetaCyc:RXN0-5055` | `RXN0-5055` | `acetyl-CoA carboxyltransferase reaction (MetaCyc:RXN0-5055)` |
| `MetaCyc:PWY-5744` | `references[17].title` | `MetaCyc:RXN-8963` | `RXN-8963` | `malonyl-CoA reductase (malonate semialdehyde-forming) reaction (MetaCyc:RXN-8963)` |
| `MetaCyc:PWY-5744` | `references[19].title` | `MetaCyc:RXN-8974` | `RXN-8974` | `malonate semialdehyde reductase (3-hydroxypropionate-forming) reaction (MetaCyc:RXN-8974)` |
| `MetaCyc:PWY-5744` | `references[21].title` | `MetaCyc:RXN-9086` | `RXN-9086` | `3-hydroxypropionate---CoA ligase (AMP-forming) reaction (MetaCyc:RXN-9086)` |
| `MetaCyc:PWY-5744` | `references[23].title` | `MetaCyc:RXN-6383` | `RXN-6383` | `3-hydroxypropionyl-CoA dehydratase reaction (MetaCyc:RXN-6383)` |
| `MetaCyc:PWY-5744` | `references[25].title` | `MetaCyc:RXN-9087` | `RXN-9087` | `acryloyl-CoA reductase (NADPH) reaction (MetaCyc:RXN-9087)` |
| `MetaCyc:PWY-5744` | `references[27].title` | `MetaCyc:RXN-8961` | `RXN-8961` | `(S)-malyl-CoA/beta-methylmalyl-CoA lyase (beta-methylmalyl-CoA-forming) reaction (MetaCyc:RXN-8961)` |
| `MetaCyc:PWY-5744` | `references[29].title` | `MetaCyc:RXN-8960` | `RXN-8960` | `erythro-3-methylmalyl-CoA dehydratase reaction (MetaCyc:RXN-8960)` |
| `MetaCyc:PWY-5744` | `references[31].title` | `MetaCyc:RXN-13230` | `RXN-13230` | `mesaconyl-C1-CoA-C4-methyltransferase reaction (MetaCyc:RXN-13230)` |
| `MetaCyc:PWY-5744` | `references[33].title` | `MetaCyc:RXN-8965` | `RXN-8965` | `mesaconyl-C4-CoA hydratase reaction (MetaCyc:RXN-8965)` |
| `MetaCyc:PWY-5744` | `references[35].title` | `MetaCyc:CITRAMALYL-COA-LYASE-RXN` | `CITRAMALYL-COA-LYASE-RXN` | `(3S)-citramalyl-CoA lyase reaction (MetaCyc:CITRAMALYL-COA-LYASE-RXN)` |

### 4.2 `F-C10S4-002` (`MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545` — 9 `reactions[].label` updates)

| Pathway ID | Field Path | Reaction ID | Before (`label == local_id`) | After (Verified Descriptive Reaction Label) |
| --- | --- | --- | --- | --- |
| `MetaCyc:ACETOACETATE-DEG-PWY` | `reactions[0].label` | `MetaCyc:ACETOACETYL-COA-TRANSFER-RXN` | `ACETOACETYL-COA-TRANSFER-RXN` | `acetate CoA-transferase reaction` |
| `MetaCyc:ACETOACETATE-DEG-PWY` | `reactions[1].label` | `MetaCyc:ACETYL-COA-ACETYLTRANSFER-RXN` | `ACETYL-COA-ACETYLTRANSFER-RXN` | `acetyl-CoA C-acetyltransferase reaction` |
| `MetaCyc:ACETOACETATE-DEG-PWY` | `reactions[2].label` | `MetaCyc:RXN-20154` | `RXN-20154` | `acetate:[protein]-L-cysteine S-acetyltransferase reaction` |
| `MetaCyc:ACETOACETATE-DEG-PWY` | `reactions[3].label` | `MetaCyc:RXN-20155` | `RXN-20155` | `acetoacetyl-CoA:[protein]-L-cysteine S-acetoacetyltransferase reaction` |
| `MetaCyc:PWY-1361` | `reactions[3].label` | `MetaCyc:RXN-2424` | `RXN-2424` | `cis-3,4-dehydroadipyl-CoA isomerase reaction` |
| `MetaCyc:PWY0-1352` | `reactions[0].label` | `MetaCyc:RXN0-5388` | `RXN0-5388` | `NADH:menaquinone oxidoreductase reaction` |
| `MetaCyc:PWY0-1352` | `reactions[1].label` | `MetaCyc:RXN0-3501` | `RXN0-3501` | `respiratory nitrate reductase (menaquinol) reaction` |
| `MetaCyc:PWY-7545` | `reactions[0].label` | `MetaCyc:RXN-11496` | `RXN-11496` | `pyruvate:ubiquinone oxidoreductase reaction` |
| `MetaCyc:PWY-7545` | `reactions[1].label` | `MetaCyc:RXN0-5266` | `RXN0-5266` | `cytochrome bd-I ubiquinol oxidase reaction` |
