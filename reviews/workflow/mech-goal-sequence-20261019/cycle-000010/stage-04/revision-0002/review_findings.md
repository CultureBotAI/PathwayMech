# Cycle 10 Stage 4 (`record_review`) Findings & Stage 5 Carry-Forward Register (Revision 2)

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage / Revision**: Cycle `10`, Stage `4` (`record_review`), Revision `2` (`revision-0002`)
- **Stage Action ID**: `013c9ceadd3c056f577e2344`
- **Frozen Inventory Snapshot**: `main` at commit `5d25cc28d8a2235ae9e98161043fc33c0efd600d` (`279` eligible records)
- **Structured Review Bundle**: `reviews/structured/20261101T082500Z-cycle10-stage4-frozen-corpus-cohort-review-rev2/review.yaml`
- **Carry-Forward Finding IDs**: `["F-C10S4-001", "F-C10S4-002"]`

---

## 1. Summary of Open Findings (`2` Findings across `6` Pathway Records)

| Finding ID | Issue Key | Category | Severity | Certainty | Status | Target Records (`6` total) | Affected Field Count | Assigned Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C10S4-001` | `raw-local-id-structured-metacyc-reaction-reference-titles-2-records` | `representation` | `minor` | `confirmed` | `open` | `GO:0043427`, `MetaCyc:PWY-5744` | `26` `references[].title` entries (`13` per record) | `A-C10S4-001` (Cycle 10 Stage 5 `resolve_review_findings`) |
| `F-C10S4-002` | `raw-local-id-metacyc-reaction-labels-4-metacyc-records` | `representation` | `minor` | `confirmed` | `open` | `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545` | `9` `reactions[].label` entries (`4 + 1 + 2 + 2`) | `A-C10S4-002` (Cycle 10 Stage 5 `resolve_review_findings`) |

---

## 2. Detailed Finding Specifications

### `F-C10S4-001` — Raw unprefixed MetaCyc reaction frame IDs in structured `references[].title` (`2` records, `26` entries)

- **Issue Key**: `raw-local-id-structured-metacyc-reaction-reference-titles-2-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Assessment ID**: `ASSESS-C10-RAW-LOCAL-ID-METACYC-RXN-REFS-AND-LABELS-6`
- **Rule ID**: `CURATION:no-raw-local-id-structured-reference-titles`
- **Evidence IDs**:
  - `EV-C10-RAW-LOCAL-ID-METACYC-RXN-REF-TITLES-2` (`data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml`, `sha256: 92e0c1a1a4f2ae4ebf5986a711a51788116037953a76e5ae0681097dcc5c4100`; `data/pathways/glyoxylate-assimilation.yaml`, `sha256: d0df038ad2114f8f5a27dae2a208764180c45f5f370c6a6a7a6cc4ad7980c22d`)
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
- **Proposed Remediation (`A-C10S4-001` for Cycle 10 Stage 5)**:
  - Replace the `26` raw `local_id` `references[].title` strings across `GO:0043427` and `MetaCyc:PWY-5744` with descriptive MetaCyc reaction reference titles aligned with each reaction's curated enzymatic activity, record curation history entries under `history/records/<slug>/`, and refresh rendered pages (`pathwaymech-render-pages`).

---

### `F-C10S4-002` — Raw unprefixed MetaCyc reaction frame IDs in `reactions[].label` (`4` records, `9` entries)

- **Issue Key**: `raw-local-id-metacyc-reaction-labels-4-metacyc-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Assessment ID**: `ASSESS-C10-RAW-LOCAL-ID-METACYC-RXN-REFS-AND-LABELS-6`
- **Rule ID**: `CURATION:no-raw-local-id-reaction-labels`
- **Evidence IDs**:
  - `EV-C10-RAW-LOCAL-ID-METACYC-REACTION-LABELS-4` (`data/pathways/acetoacetate-degradation.yaml`, `sha256: 233b3b864987d0d4bd5434236eb7289624137abbaaa194e936766ebe344d92e4`; `data/pathways/benzoyl-coa-degradation-i-aerobic.yaml`, `sha256: 91552e9b4f36ece175f6cee1ff384423f11ddfbb76ce2ec1dd4b4b87cc2d7f08`; `data/pathways/nitrate-reduction-viii.yaml`, `sha256: 5243f546a62490581e35d29516f2ecb830b1284748d6b2b042b82e7d9f6303b7`; `data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`, `sha256: 08884edf95974a98a5dd9cc2583638b730fc0a8de687ab6b0e24461b68a50a7d`)
- **Affected Records & Exact Field Paths**:
  1. `MetaCyc:ACETOACETATE-DEG-PWY` (`data/pathways/acetoacetate-degradation.yaml`, `4` entries):
     - `reactions[0].label` (`id: MetaCyc:ACETOACETYL-COA-TRANSFER-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETOACETYL-COA-TRANSFER-RXN` — acetate CoA-transferase reaction)
     - `reactions[1].label` (`id: MetaCyc:ACETYL-COA-ACETYLTRANSFER-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETYL-COA-ACETYLTRANSFER-RXN` — acetyl-CoA C-acetyltransferase reaction)
     - `reactions[2].label` (`id: MetaCyc:RXN-20154`, `category: molecular_activity`, `direction: reversible`, current `label: RXN-20154` — acetate:[protein]-L-cysteine S-acetyltransferase reaction)
     - `reactions[3].label` (`id: MetaCyc:RXN-20155`, `category: molecular_activity`, `direction: reversible`, current `label: RXN-20155` — acetoacetyl-CoA:[protein]-L-cysteine S-acetoacetyltransferase reaction)
  2. `MetaCyc:PWY-1361` (`data/pathways/benzoyl-coa-degradation-i-aerobic.yaml`, `1` entry):
     - `reactions[3].label` (`id: MetaCyc:RXN-2424`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN-2424` — cis-3,4-dehydroadipyl-CoA isomerase reaction)
  3. `MetaCyc:PWY0-1352` (`data/pathways/nitrate-reduction-viii.yaml`, `2` entries):
     - `reactions[0].label` (`id: MetaCyc:RXN0-5388`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-5388` — NADH:menaquinone oxidoreductase reaction)
     - `reactions[1].label` (`id: MetaCyc:RXN0-3501`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-3501` — respiratory nitrate reductase (menaquinol) reaction)
  4. `MetaCyc:PWY-7545` (`data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`, `2` entries):
     - `reactions[0].label` (`id: MetaCyc:RXN-11496`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN-11496` — pyruvate:ubiquinone oxidoreductase reaction)
     - `reactions[1].label` (`id: MetaCyc:RXN0-5266`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-5266` — cytochrome bd-I ubiquinol oxidase reaction)
- **Proposed Remediation (`A-C10S4-002` for Cycle 10 Stage 5)**:
  - Replace the `9` raw `local_id` `reactions[].label` strings across `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, and `MetaCyc:PWY-7545` with descriptive biochemical reaction labels verified against each record's catalyzed substrates/products and structured `references[].title`, record curation history entries under `history/records/<slug>/`, and refresh rendered pages (`pathwaymech-render-pages`).

---

## 3. Prior Findings Verified Resolved in Cycle 9 Stage 5 (`#771`)

- **`F-C9S4-001`** (`raw-local-id-structured-reference-titles-3-metacyc-records`, `3` records: `MetaCyc:PWY-8132`, `MetaCyc:PWY-7255`, `MetaCyc:PWY0-1241`, `16` `references[].title` entries): Verified `resolved` (`0` remaining raw `local_id` reference titles in all `3` target records).
- **`F-C9S4-002`** (`raw-local-id-reference-titles-and-reaction-labels-2-metacyc-records`, `2` records: `MetaCyc:THIOREDOX-PWY` `11` `references[].title` entries and `MetaCyc:PWY-8178` `6` `reactions[].label` entries): Verified `resolved` (`0` remaining raw `local_id` reference titles or reaction labels in both target records).
