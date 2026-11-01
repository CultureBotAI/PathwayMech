# Cycle 10 Stage 4 (`record_review`) Findings & Stage 5 Carry-Forward Register

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage**: Cycle `10`, Stage `4` (`record_review`)
- **Stage Action ID**: `013c9ceadd3c056f577e2344`
- **Frozen Inventory Snapshot**: `main` at commit `2c6bbbfc3fb9e53e1efbce7fb34f26da34b48093` (`279` eligible records)
- **Structured Review Bundle**: `reviews/structured/20261101T070500Z-cycle10-stage4-frozen-corpus-cohort-review/review.yaml`
- **Carry-Forward Finding IDs**: `["F-C10S4-001", "F-C10S4-002"]`

---

## 1. Summary of Open Findings (`2` Findings across `6` Pathway Records)

| Finding ID | Issue Key | Category | Severity | Certainty | Status | Target Records (`6` total) | Affected Field Count | Assigned Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C10S4-001` | `raw-local-id-structured-metacyc-reaction-reference-titles-2-records` | `representation` | `minor` | `confirmed` | `open` | `GO:0043427`, `MetaCyc:PWY-5744` | `26` `references[].title` entries (`13` per record) | `act-01` (Cycle 10 Stage 5 `resolve_review_findings`) |
| `F-C10S4-002` | `raw-local-id-metacyc-reaction-labels-4-metacyc-records` | `representation` | `minor` | `confirmed` | `open` | `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545` | `9` `reactions[].label` entries (`4 + 1 + 2 + 2`) | `act-02` (Cycle 10 Stage 5 `resolve_review_findings`) |

---

## 2. Detailed Finding Specifications

### `F-C10S4-001` — Raw unprefixed MetaCyc reaction frame IDs in structured `references[].title` (`2` records, `26` entries)

- **Issue Key**: `raw-local-id-structured-metacyc-reaction-reference-titles-2-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Check ID**: `chk-06` (`evidence`)
- **Evidence IDs**:
  - `ev-011` (`data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml`, `sha256: 92e0c1a1a4f2ae4ebf5986a711a51788116037953a76e5ae0681097dcc5c4100`)
  - `ev-098` (`data/pathways/glyoxylate-assimilation.yaml`, `sha256: d0df038ad2114f8f5a27dae2a208764180c45f5f370c6a6a7a6cc4ad7980c22d`)
- **Affected Records & Exact Field Paths**:
  1. `GO:0043427` (`data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml`, `13` entries):
     - `references[11].title` (`id: MetaCyc:RXN0-5224`, current `title: RXN0-5224` — carbonic anhydrase reaction)
     - `references[13].title` (`id: MetaCyc:BIOTIN-CARBOXYL-RXN`, current `title: BIOTIN-CARBOXYL-RXN` — biotin carboxylase reaction)
     - `references[15].title` (`id: MetaCyc:RXN0-5055`, current `title: RXN0-5055` — acetyl-CoA carboxyltransferase reaction)
     - `references[17].title` (`id: MetaCyc:RXN-8963`, current `title: RXN-8963` — malonyl-CoA reductase (malonate semialdehyde-forming) reaction)
     - `references[19].title` (`id: MetaCyc:RXN-8974`, current `title: RXN-8974` — malonate semialdehyde reductase (3-hydroxypropionate-forming) reaction)
     - `references[21].title` (`id: MetaCyc:RXN-9086`, current `title: RXN-9086` — 3-hydroxypropionate---CoA ligase (AMP-forming) reaction)
     - `references[23].title` (`id: MetaCyc:RXN-6383`, current `title: RXN-6383` — 3-hydroxypropionyl-CoA dehydratase reaction)
     - `references[25].title` (`id: MetaCyc:RXN-9087`, current `title: RXN-9087` — acryloyl-CoA reductase (NADPH) reaction)
     - `references[27].title` (`id: MetaCyc:PROPIONYL-COA-CARBOXY-RXN`, current `title: PROPIONYL-COA-CARBOXY-RXN` — propionyl-CoA carboxylase reaction)
     - `references[29].title` (`id: MetaCyc:METHYLMALONYL-COA-EPIM-RXN`, current `title: METHYLMALONYL-COA-EPIM-RXN` — methylmalonyl-CoA epimerase reaction)
     - `references[31].title` (`id: MetaCyc:METHYLMALONYL-COA-MUT-RXN`, current `title: METHYLMALONYL-COA-MUT-RXN` — methylmalonyl-CoA mutase reaction)
     - `references[33].title` (`id: MetaCyc:RXN-8964`, current `title: RXN-8964` — succinyl-CoA:(S)-malate CoA-transferase reaction)
     - `references[37].title` (`id: MetaCyc:MALYL-COA-LYASE-RXN`, current `title: MALYL-COA-LYASE-RXN` — (S)-malyl-CoA lyase reaction)
  2. `MetaCyc:PWY-5744` (`data/pathways/glyoxylate-assimilation.yaml`, `13` entries):
     - `references[11].title` (`id: MetaCyc:RXN0-5224`, current `title: RXN0-5224` — carbonic anhydrase reaction)
     - `references[13].title` (`id: MetaCyc:BIOTIN-CARBOXYL-RXN`, current `title: BIOTIN-CARBOXYL-RXN` — biotin carboxylase reaction)
     - `references[15].title` (`id: MetaCyc:RXN0-5055`, current `title: RXN0-5055` — acetyl-CoA carboxyltransferase reaction)
     - `references[17].title` (`id: MetaCyc:RXN-8963`, current `title: RXN-8963` — malonyl-CoA reductase (malonate semialdehyde-forming) reaction)
     - `references[19].title` (`id: MetaCyc:RXN-8974`, current `title: RXN-8974` — malonate semialdehyde reductase (3-hydroxypropionate-forming) reaction)
     - `references[21].title` (`id: MetaCyc:RXN-9086`, current `title: RXN-9086` — 3-hydroxypropionate---CoA ligase (AMP-forming) reaction)
     - `references[23].title` (`id: MetaCyc:RXN-6383`, current `title: RXN-6383` — 3-hydroxypropionyl-CoA dehydratase reaction)
     - `references[25].title` (`id: MetaCyc:RXN-9087`, current `title: RXN-9087` — acryloyl-CoA reductase (NADPH) reaction)
     - `references[27].title` (`id: MetaCyc:RXN-8961`, current `title: RXN-8961` — (S)-malyl-CoA/beta-methylmalyl-CoA lyase (beta-methylmalyl-CoA-forming) reaction)
     - `references[29].title` (`id: MetaCyc:RXN-8960`, current `title: RXN-8960` — erythro-3-methylmalyl-CoA dehydratase reaction)
     - `references[31].title` (`id: MetaCyc:RXN-13230`, current `title: RXN-13230` — mesaconyl-C1-CoA-C4-methyltransferase reaction)
     - `references[33].title` (`id: MetaCyc:RXN-8965`, current `title: RXN-8965` — mesaconyl-C4-CoA hydratase reaction)
     - `references[35].title` (`id: MetaCyc:CITRAMALYL-COA-LYASE-RXN`, current `title: CITRAMALYL-COA-LYASE-RXN` — (3S)-citramalyl-CoA lyase reaction)
- **Proposed Remediation (`act-01` for Cycle 10 Stage 5)**:
  - Replace the `26` raw `local_id` `references[].title` strings across `GO:0043427` and `MetaCyc:PWY-5744` with descriptive MetaCyc reaction reference titles aligned with each reaction's curated enzymatic activity, append a `curation_history` event to each record, and refresh rendered pages (`pathwaymech-render-pages`).

---

### `F-C10S4-002` — Raw unprefixed MetaCyc reaction frame IDs in `reactions[].label` (`4` records, `9` entries)

- **Issue Key**: `raw-local-id-metacyc-reaction-labels-4-metacyc-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Check ID**: `chk-04` (`reactions`)
- **Evidence IDs**:
  - `ev-006` (`data/pathways/acetoacetate-degradation.yaml`, `sha256: 233b3b864987d0d4bd5434236eb7289624137abbaaa194e936766ebe344d92e4`)
  - `ev-008` (`data/pathways/benzoyl-coa-degradation-i-aerobic.yaml`, `sha256: 91552e9b4f36ece175f6cee1ff384423f11ddfbb76ce2ec1dd4b4b87cc2d7f08`)
  - `ev-164` (`data/pathways/nitrate-reduction-viii.yaml`, `sha256: 5243f546a62490581e35d29516f2ecb830b1284748d6b2b042b82e7d9f6303b7`)
  - `ev-221` (`data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`, `sha256: 08884edf95974a98a5dd9cc2583638b730fc0a8de687ab6b0e24461b68a50a7d`)
- **Affected Records & Exact Field Paths**:
  1. `MetaCyc:ACETOACETATE-DEG-PWY` (`data/pathways/acetoacetate-degradation.yaml`, `4` entries):
     - `reactions[0].label` (`id: MetaCyc:ACETOACETYL-COA-TRANSFER-RXN`, `ec_number: 2.8.3.8`, current `label: ACETOACETYL-COA-TRANSFER-RXN` — acetate CoA-transferase reaction)
     - `reactions[1].label` (`id: MetaCyc:ACETYL-COA-ACETYLTRANSFER-RXN`, `ec_number: 2.3.1.9`, current `label: ACETYL-COA-ACETYLTRANSFER-RXN` — acetyl-CoA C-acetyltransferase reaction)
     - `reactions[2].label` (`id: MetaCyc:RXN-20154`, `ec_number: 6.2.1.16`, current `label: RXN-20154` — acetoacetate---CoA ligase (acetoacetyl-AMP-forming) reaction)
     - `reactions[3].label` (`id: MetaCyc:RXN-20155`, `ec_number: 6.2.1.16`, current `label: RXN-20155` — acetoacetyl-AMP:CoA acetoacetyltransferase reaction)
  2. `MetaCyc:PWY-1361` (`data/pathways/benzoyl-coa-degradation-i-aerobic.yaml`, `1` entry):
     - `reactions[3].label` (`id: MetaCyc:RXN-2424`, `ec_number: 2.3.1.174`, current `label: RXN-2424` — 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase reaction)
  3. `MetaCyc:PWY0-1352` (`data/pathways/nitrate-reduction-viii.yaml`, `2` entries):
     - `reactions[0].label` (`id: MetaCyc:RXN0-5388`, `ec_number: 1.7.5.1`, current `label: RXN0-5388` — respiratory nitrate reductase (menaquinol) reaction)
     - `reactions[1].label` (`id: MetaCyc:RXN0-3501`, `ec_number: 1.7.2.2`, current `label: RXN0-3501` — periplasmic nitrite reductase (cytochrome c552) reaction)
  4. `MetaCyc:PWY-7545` (`data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`, `2` entries):
     - `reactions[0].label` (`id: MetaCyc:RXN-11496`, `ec_number: 1.2.5.1`, current `label: RXN-11496` — pyruvate dehydrogenase (menaquinone) reaction)
     - `reactions[1].label` (`id: MetaCyc:RXN0-5266`, `ec_number: 7.1.1.7`, current `label: RXN0-5266` — cytochrome bd-I ubiquinol/menaquinol oxidase reaction)
- **Proposed Remediation (`act-02` for Cycle 10 Stage 5)**:
  - Replace the `9` raw `local_id` `reactions[].label` strings across `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, and `MetaCyc:PWY-7545` with descriptive enzymatic reaction labels verified against each record's EC number, catalyzed substrates/products, and structured `references[].title`, append a `curation_history` event to each record, and refresh rendered pages (`pathwaymech-render-pages`).

---

## 3. Prior Findings Verified Resolved in Cycle 9 Stage 5 (`#771`)

- **`F-C9S4-001`** (`raw-local-id-structured-reference-titles-11-metacyc-records`, `11` records, `42` `references[].title` entries): Verified `resolved` (`0` remaining raw `local_id` reference titles in all `11` target records).
- **`F-C9S4-002`** (`raw-local-id-metacyc-reaction-labels-5-metacyc-records`, `5` records, `12` `reactions[].label` entries): Verified `resolved` (`0` remaining raw `local_id` reaction labels in all `5` target records).
