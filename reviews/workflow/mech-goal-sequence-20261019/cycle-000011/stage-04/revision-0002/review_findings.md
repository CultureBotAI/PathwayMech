# Cycle 11 Stage 4 (`record_review`) Findings & Stage 5 Carry-Forward Register (Revision 2)

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage / Revision**: Cycle `11`, Stage `4` (`record_review`), Revision `2` (`revision-0002`)
- **Stage Action ID**: `333bc3800d62ed19e22c5576`
- **Frozen Inventory Snapshot**: `main` at commit `12cd8a123a63df8d89fa7517dd34c30eabd8c8bd` (`280` eligible records)
- **Structured Review Bundle**: `reviews/structured/20261105T040000Z-cycle11-stage4-frozen-corpus-cohort-review-rev2/review.yaml`
- **Carry-Forward Finding IDs**: `["F-C11S4-001", "F-C11S4-002"]`

---

## 1. Summary of Open Findings (`2` Findings across `11` Pathway Records)

| Finding ID | Issue Key | Category | Severity | Certainty | Status | Target Records (`11` total) | Affected Field Count | Assigned Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C11S4-001` | `raw-local-id-structured-metacyc-reference-titles-4-records` | `representation` | `minor` | `confirmed` | `open` | `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, `MetaCyc:THISYN-PWY` | `79` `references[].title` entries (`31 + 20 + 16 + 12`) | `A-C11S4-001` (Cycle 11 Stage 5 `resolve_review_findings`) |
| `F-C11S4-002` | `raw-local-id-metacyc-reaction-labels-7-metacyc-records` | `representation` | `minor` | `confirmed` | `open` | `MetaCyc:PWY0-321`, `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, `MetaCyc:PWY-5177` | `49` `reactions[].label` entries (`11 + 8 + 7 + 6 + 6 + 6 + 5`) | `A-C11S4-002` (Cycle 11 Stage 5 `resolve_review_findings`) |

---

## 2. Detailed Finding Specifications

### `F-C11S4-001` — Raw unprefixed MetaCyc frame IDs in structured `references[].title` (`4` records, `79` entries)

- **Issue Key**: `raw-local-id-structured-metacyc-reference-titles-4-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Assessment ID**: `ASSESS-C11-RAW-LOCAL-ID-METACYC-REFS-AND-RXN-LABELS-11`
- **Rule ID**: `CURATION:no-raw-local-id-structured-reference-titles`
- **Evidence IDs**:
  - `EV-C11-RAW-LOCAL-ID-METACYC-REF-TITLES-4` (`data/pathways/biotin-biosynthesis-i.yaml`, `sha256: fb535867a1e72c871e9cecd15c0020263b060a7b1fc3060a6362c65257825d94`; `data/pathways/molybdenum-cofactor-biosynthesis.yaml`, `sha256: b3796af38685c27b5f3585479100a2bf159abdc0b12e477f516c493b7198229d`; `data/pathways/calvin-cycle.yaml`, `sha256: 6eb1a8146b3b24bd37ddcd259c039e51946514b06b823309ca06bb2f79d7c0be`; `data/pathways/thiamine-diphosphate-biosynthesis-i.yaml`, `sha256: 8b2c4338de39ff135ba82a7a1444c2653da3cb79c3f148f85f275a16a91d28e8`)
- **Affected Records & Exact Field Paths**:
  1. `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY` (`data/pathways/biotin-biosynthesis-i.yaml`, `31` entries):
     - `references[1].title` (`id: MetaCyc:PWY-6519`, current `title: PWY-6519`)
     - `references[2].title` (`id: MetaCyc:PWY0-1507`, current `title: PWY0-1507`)
     - `references[3].title` (`id: MetaCyc:RXN-11475`, current `title: RXN-11475`)
     - `references[12].title` (`id: MetaCyc:RXN-11483`, current `title: RXN-11483`)
     - `references[13].title` (`id: MetaCyc:RXN-11484`, current `title: RXN-11484`)
     - `references[14].title` (`id: MetaCyc:DAPASYN-RXN`, current `title: DAPASYN-RXN`)
     - `references[15].title` (`id: MetaCyc:DETHIOBIOTIN-SYN-RXN`, current `title: DETHIOBIOTIN-SYN-RXN`)
     - `references[16].title` (`id: MetaCyc:2.8.1.6-RXN`, current `title: 2.8.1.6-RXN`)
     - `references[18].title` (`id: MetaCyc:7KAPSYN-MONOMER`, current `title: 7KAPSYN-MONOMER`)
     - `references[20].title` (`id: MetaCyc:DAPASYN-MONOMER`, current `title: DAPASYN-MONOMER`)
     - `references[22].title` (`id: MetaCyc:DETHIOBIOTIN-SYN-MONOMER`, current `title: DETHIOBIOTIN-SYN-MONOMER`)
     - `references[24].title` (`id: MetaCyc:BIOTIN-SYN-MONOMER`, current `title: BIOTIN-SYN-MONOMER`)
     - `references[26].title` (`id: MetaCyc:3-OXOACYL-ACP-REDUCT-MONOMER`, current `title: 3-OXOACYL-ACP-REDUCT-MONOMER`)
     - `references[28].title` (`id: MetaCyc:FABZ-MONOMER`, current `title: FABZ-MONOMER`)
     - `references[30].title` (`id: MetaCyc:ENOYL-ACP-REDUCT-NADH-MONOMER`, current `title: ENOYL-ACP-REDUCT-NADH-MONOMER`)
     - `references[32].title` (`id: MetaCyc:FABB-MONOMER`, current `title: FABB-MONOMER`)
     - `references[33].title` (`id: MetaCyc:EG10119-MONOMER`, current `title: EG10119-MONOMER`)
     - `references[34].title` (`id: MetaCyc:EG10122-MONOMER`, current `title: EG10122-MONOMER`)
     - `references[35].title` (`id: MetaCyc:ENZRXN-17863`, current `title: ENZRXN-17863`)
     - `references[36].title` (`id: MetaCyc:ENZRXN-17867`, current `title: ENZRXN-17867`)
     - `references[37].title` (`id: MetaCyc:ENZRXN-17869`, current `title: ENZRXN-17869`)
     - `references[38].title` (`id: MetaCyc:ENZRXN-17871`, current `title: ENZRXN-17871`)
     - `references[39].title` (`id: MetaCyc:ENZRXN-17873`, current `title: ENZRXN-17873`)
     - `references[40].title` (`id: MetaCyc:ENZRXN-17868`, current `title: ENZRXN-17868`)
     - `references[41].title` (`id: MetaCyc:ENZRXN-17870`, current `title: ENZRXN-17870`)
     - `references[42].title` (`id: MetaCyc:ENZRXN-17872`, current `title: ENZRXN-17872`)
     - `references[43].title` (`id: MetaCyc:ENZRXN-17864`, current `title: ENZRXN-17864`)
     - `references[44].title` (`id: MetaCyc:ENZRXN-17865`, current `title: ENZRXN-17865`)
     - `references[45].title` (`id: MetaCyc:DAPASYN-ENZRXN`, current `title: DAPASYN-ENZRXN`)
     - `references[46].title` (`id: MetaCyc:DETHIOBIOTIN-SYN-ENZRXN`, current `title: DETHIOBIOTIN-SYN-ENZRXN`)
     - `references[47].title` (`id: MetaCyc:BIOTIN-SYN-ENZRXN`, current `title: BIOTIN-SYN-ENZRXN`)
  2. `MetaCyc:PWY-6823` (`data/pathways/molybdenum-cofactor-biosynthesis.yaml`, `20` entries):
     - `references[18].title` (`id: MetaCyc:RXN-8340`, current `title: RXN-8340`)
     - `references[19].title` (`id: MetaCyc:RXN-17809`, current `title: RXN-17809`)
     - `references[20].title` (`id: MetaCyc:RXN0-308`, current `title: RXN0-308`)
     - `references[21].title` (`id: MetaCyc:RXN-11361`, current `title: RXN-11361`)
     - `references[22].title` (`id: MetaCyc:RXN-12473`, current `title: RXN-12473`)
     - `references[23].title` (`id: MetaCyc:RXN-8342`, current `title: RXN-8342`)
     - `references[24].title` (`id: MetaCyc:RXN-8344`, current `title: RXN-8344`)
     - `references[25].title` (`id: MetaCyc:RXN-8348`, current `title: RXN-8348`)
     - `references[27].title` (`id: MetaCyc:EG11666-MONOMER`, current `title: EG11666-MONOMER`)
     - `references[29].title` (`id: MetaCyc:EG11597-MONOMER`, current `title: EG11597-MONOMER`)
     - `references[30].title` (`id: MetaCyc:EG11598-MONOMER`, current `title: EG11598-MONOMER`)
     - `references[32].title` (`id: MetaCyc:EG10154-MONOMER`, current `title: EG10154-MONOMER`)
     - `references[34].title` (`id: MetaCyc:EG11511-MONOMER`, current `title: EG11511-MONOMER`)
     - `references[36].title` (`id: MetaCyc:EG10153-MONOMER`, current `title: EG10153-MONOMER`)
     - `references[38].title` (`id: MetaCyc:G7325-MONOMER`, current `title: G7325-MONOMER`)
     - `references[39].title` (`id: MetaCyc:EG11595-MONOMER`, current `title: EG11595-MONOMER`)
     - `references[40].title` (`id: MetaCyc:ENZRXN-19108`, current `title: ENZRXN-19108`)
     - `references[41].title` (`id: MetaCyc:G6952-MONOMER`, current `title: G6952-MONOMER`)
     - `references[42].title` (`id: MetaCyc:CPD-19179`, current `title: CPD-19179`)
     - `references[43].title` (`id: MetaCyc:CPD-8123`, current `title: CPD-8123`)
  3. `MetaCyc:CALVIN-PWY` (`data/pathways/calvin-cycle.yaml`, `16` entries):
     - `references[2].title` (`id: MetaCyc:RIB5PISOM-RXN`, current `title: RIB5PISOM-RXN`)
     - `references[6].title` (`id: MetaCyc:PHOSPHORIBULOKINASE-RXN`, current `title: PHOSPHORIBULOKINASE-RXN`)
     - `references[12].title` (`id: MetaCyc:RIBULP3EPIM-RXN`, current `title: RIBULP3EPIM-RXN`)
     - `references[15].title` (`id: MetaCyc:SEDOHEPTULOSE-BISPHOSPHATASE-RXN`, current `title: SEDOHEPTULOSE-BISPHOSPHATASE-RXN`)
     - `references[21].title` (`id: MetaCyc:2TRANSKETO-RXN`, current `title: 2TRANSKETO-RXN`)
     - `references[26].title` (`id: MetaCyc:1TRANSKETO-RXN`, current `title: 1TRANSKETO-RXN`)
     - `references[28].title` (`id: MetaCyc:F16BDEPHOS-RXN`, current `title: F16BDEPHOS-RXN`)
     - `references[31].title` (`id: MetaCyc:SEDOBISALDOL-RXN`, current `title: SEDOBISALDOL-RXN`)
     - `references[34].title` (`id: MetaCyc:F16ALDOLASE-RXN`, current `title: F16ALDOLASE-RXN`)
     - `references[36].title` (`id: MetaCyc:TRIOSEPISOMERIZATION-RXN`, current `title: TRIOSEPISOMERIZATION-RXN`)
     - `references[38].title` (`id: MetaCyc:1.2.1.13-RXN`, current `title: 1.2.1.13-RXN`)
     - `references[43].title` (`id: MetaCyc:PHOSGLYPHOS-RXN`, current `title: PHOSGLYPHOS-RXN`)
     - `references[46].title` (`id: MetaCyc:RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN`, current `title: RIBULOSE-BISPHOSPHATE-CARBOXYLASE-RXN`)
     - `references[90].title` (`id: MetaCyc:REG-8538`, current `title: REG-8538`)
     - `references[91].title` (`id: MetaCyc:REG-8539`, current `title: REG-8539`)
     - `references[92].title` (`id: MetaCyc:REG-10188`, current `title: REG-10188`)
  4. `MetaCyc:THISYN-PWY` (`data/pathways/thiamine-diphosphate-biosynthesis-i.yaml`, `12` entries):
     - `references[16].title` (`id: MetaCyc:CPLX0-743`, current `title: CPLX0-743`)
     - `references[28].title` (`id: MetaCyc:RXN0-308`, current `title: RXN0-308`)
     - `references[29].title` (`id: MetaCyc:RXN-9789`, current `title: RXN-9789`)
     - `references[30].title` (`id: MetaCyc:DXS-RXN`, current `title: DXS-RXN`)
     - `references[31].title` (`id: MetaCyc:RXN-11319`, current `title: RXN-11319`)
     - `references[32].title` (`id: MetaCyc:THIAZOLSYN2-RXN`, current `title: THIAZOLSYN2-RXN`)
     - `references[33].title` (`id: MetaCyc:PYRIMSYN1-RXN`, current `title: PYRIMSYN1-RXN`)
     - `references[34].title` (`id: MetaCyc:PYRIMSYN3-RXN`, current `title: PYRIMSYN3-RXN`)
     - `references[36].title` (`id: MetaCyc:THI-P-KIN-RXN`, current `title: THI-P-KIN-RXN`)
     - `references[37].title` (`id: MetaCyc:RXN-14382`, current `title: RXN-14382`)
     - `references[38].title` (`id: MetaCyc:RXN-9788`, current `title: RXN-9788`)
     - `references[48].title` (`id: MetaCyc:HMP-P-KIN-CPLX`, current `title: HMP-P-KIN-CPLX`)
- **Proposed Remediation (`A-C11S4-001` for Cycle 11 Stage 5)**:
  - Replace the `79` raw `local_id` `references[].title` strings across `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, and `MetaCyc:THISYN-PWY` with descriptive MetaCyc reference titles aligned with each reaction, subpathway, monomer/complex, compound, enzymatic-reaction, or regulation frame, record curation history entries under `history/records/<slug>/`, and refresh rendered pages (`pathwaymech-render-pages`).

---

### `F-C11S4-002` — Raw unprefixed MetaCyc reaction frame IDs in `reactions[].label` (`7` records, `49` entries)

- **Issue Key**: `raw-local-id-metacyc-reaction-labels-7-metacyc-records`
- **Category / Severity / Certainty / Status**: `representation` / `minor` / `confirmed` / `open`
- **Assessment ID**: `ASSESS-C11-RAW-LOCAL-ID-METACYC-REFS-AND-RXN-LABELS-11`
- **Rule ID**: `CURATION:no-raw-local-id-reaction-labels`
- **Evidence IDs**:
  - `EV-C11-RAW-LOCAL-ID-METACYC-REACTION-LABELS-7` (`data/pathways/phenylacetate-degradation-i-aerobic.yaml`, `sha256: b37ff12817f9e3688deebbb50bf0dc22a2a8966052124d64c236e501279ef36e`; `data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml`, `sha256: 0b096126f4df68b67b1d458731247d6460b476e0dd5835935f2c5b6e246260b6`; `data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml`, `sha256: 2639cd619925ab868a91ba562b9cbda48d2566c9630eb39c1130e19ff7df25da`; `data/pathways/ethanolamine-utilization.yaml`, `sha256: 136b709c441daefeb62640c11ff9b20dd38a172df232b003497c109e691486b4`; `data/pathways/methanogenesis-from-acetate.yaml`, `sha256: 750bc6d7df17f93de87a6b735eb2d44c3a440f08b6301b92ce68fb24ca180d3a`; `data/pathways/methanogenesis-from-h2-and-co2.yaml`, `sha256: 659ca41d9452d36b2be8d7ce8093b4736c81d4e6a7775f18b7e81737d2d93026`; `data/pathways/glutaryl-coa-degradation.yaml`, `sha256: 8fd6226fb55972dc964df7c16c636895a1087ceecdfdb81da0a9da6c294f235f`)
- **Affected Records & Exact Field Paths**:
  1. `MetaCyc:PWY0-321` (`data/pathways/phenylacetate-degradation-i-aerobic.yaml`, `11` entries):
     - `reactions[0].label` (`id: MetaCyc:RXN-10819`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN-10819`)
     - `reactions[1].label` (`id: MetaCyc:RXN0-2042`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-2042`)
     - `reactions[2].label` (`id: MetaCyc:RXN0-6510`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-6510`)
     - `reactions[3].label` (`id: MetaCyc:RXNMETA-12671`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXNMETA-12671`)
     - `reactions[4].label` (`id: MetaCyc:RXNMETA-12672`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXNMETA-12672`)
     - `reactions[5].label` (`id: MetaCyc:RXN0-6512`, `category: molecular_activity`, `direction: right_to_left`, current `label: RXN0-6512`)
     - `reactions[6].label` (`id: MetaCyc:RXN-2425`, `category: molecular_activity`, `direction: right_to_left`, current `label: RXN-2425`)
     - `reactions[7].label` (`id: MetaCyc:RXN0-2044`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-2044`)
     - `reactions[8].label` (`id: MetaCyc:RXN-3641`, `category: molecular_activity`, `direction: right_to_left`, current `label: RXN-3641`)
     - `reactions[9].label` (`id: MetaCyc:RXN-17752`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN-17752`)
     - `reactions[10].label` (`id: MetaCyc:RXN0-7103`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN0-7103`)
  2. `MetaCyc:P321-PWY` (`data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml`, `8` entries):
     - `reactions[0].label` (`id: MetaCyc:1.3.99.15-RXN`, `category: molecular_activity`, `direction: right_to_left`, current `label: 1.3.99.15-RXN`)
     - `reactions[1].label` (`id: MetaCyc:R265-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: R265-RXN`)
     - `reactions[2].label` (`id: MetaCyc:R266-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: R266-RXN`)
     - `reactions[3].label` (`id: MetaCyc:R267-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: R267-RXN`)
     - `reactions[4].label` (`id: MetaCyc:R268-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: R268-RXN`)
     - `reactions[5].label` (`id: MetaCyc:1.3.1.62-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: 1.3.1.62-RXN`)
     - `reactions[6].label` (`id: MetaCyc:RXN-8031`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN-8031`)
     - `reactions[7].label` (`id: MetaCyc:1.1.1.259-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: 1.1.1.259-RXN`)
  3. `MetaCyc:CENTBENZCOA-PWY` (`data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml`, `7` entries):
     - `reactions[0].label` (`id: MetaCyc:1.3.99.15-RXN`, `category: molecular_activity`, `direction: right_to_left`, current `label: 1.3.99.15-RXN`)
     - `reactions[1].label` (`id: MetaCyc:4.2.1.100-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: 4.2.1.100-RXN`)
     - `reactions[2].label` (`id: MetaCyc:HADTHAUERA-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: HADTHAUERA-RXN`)
     - `reactions[3].label` (`id: MetaCyc:RXN-15012`, `category: molecular_activity`, `direction: reversible`, current `label: RXN-15012`)
     - `reactions[4].label` (`id: MetaCyc:RXN-15013`, `category: molecular_activity`, `direction: reversible`, current `label: RXN-15013`)
     - `reactions[5].label` (`id: MetaCyc:1.1.1.259-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: 1.1.1.259-RXN`)
     - `reactions[7].label` (`id: MetaCyc:OAHTHAUERA-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: OAHTHAUERA-RXN`)
  4. `MetaCyc:PWY0-1477` (`data/pathways/ethanolamine-utilization.yaml`, `6` entries):
     - `reactions[0].label` (`id: MetaCyc:ACETALD-DEHYDROG-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETALD-DEHYDROG-RXN`)
     - `reactions[1].label` (`id: MetaCyc:ACETATEKIN-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETATEKIN-RXN`)
     - `reactions[2].label` (`id: MetaCyc:ALCOHOL-DEHYDROG-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ALCOHOL-DEHYDROG-RXN`)
     - `reactions[3].label` (`id: MetaCyc:ETHAMLY-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: ETHAMLY-RXN`)
     - `reactions[4].label` (`id: MetaCyc:PHOSACETYLTRANS-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: PHOSACETYLTRANS-RXN`)
     - `reactions[5].label` (`id: MetaCyc:RXN-19336`, `category: molecular_activity`, `direction: left_to_right`, current `label: RXN-19336`)
  5. `MetaCyc:METH-ACETATE-PWY` (`data/pathways/methanogenesis-from-acetate.yaml`, `6` entries):
     - `reactions[0].label` (`id: MetaCyc:1.2.7.4-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: 1.2.7.4-RXN`)
     - `reactions[1].label` (`id: MetaCyc:ACETATEKIN-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETATEKIN-RXN`)
     - `reactions[2].label` (`id: MetaCyc:ACETYLSYNCLTH-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETYLSYNCLTH-RXN`)
     - `reactions[3].label` (`id: MetaCyc:MTRMBARK-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: MTRMBARK-RXN`)
     - `reactions[4].label` (`id: MetaCyc:PHOSACETYLTRANS-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: PHOSACETYLTRANS-RXN`)
     - `reactions[5].label` (`id: MetaCyc:RXN-12908`, `category: molecular_activity`, `direction: reversible`, current `label: RXN-12908`)
  6. `MetaCyc:METHANOGENESIS-PWY` (`data/pathways/methanogenesis-from-h2-and-co2.yaml`, `6` entries):
     - `reactions[0].label` (`id: MetaCyc:2.1.1.86-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: 2.1.1.86-RXN`)
     - `reactions[1].label` (`id: MetaCyc:2.3.1.101-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: 2.3.1.101-RXN`)
     - `reactions[2].label` (`id: MetaCyc:3.5.4.27-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: 3.5.4.27-RXN`)
     - `reactions[3].label` (`id: MetaCyc:FORMYLMETHANOFURAN-DEHYDROGENASE-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: FORMYLMETHANOFURAN-DEHYDROGENASE-RXN`)
     - `reactions[4].label` (`id: MetaCyc:H2-METHYLENE-THMPT-DEHYDRO-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: H2-METHYLENE-THMPT-DEHYDRO-RXN`)
     - `reactions[5].label` (`id: MetaCyc:METHELENE-THMPT-OXI-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: METHELENE-THMPT-OXI-RXN`)
  7. `MetaCyc:PWY-5177` (`data/pathways/glutaryl-coa-degradation.yaml`, `5` entries):
     - `reactions[0].label` (`id: MetaCyc:ACETYL-COA-ACETYLTRANSFER-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: ACETYL-COA-ACETYLTRANSFER-RXN`)
     - `reactions[1].label` (`id: MetaCyc:GLUTACONYL-COA-DECARBOXYLASE-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: GLUTACONYL-COA-DECARBOXYLASE-RXN`)
     - `reactions[2].label` (`id: MetaCyc:GLUTARYL-COA-DEHYDROG-RXN`, `category: molecular_activity`, `direction: reversible`, current `label: GLUTARYL-COA-DEHYDROG-RXN`)
     - `reactions[3].label` (`id: MetaCyc:GLUTARYL-COA-DEHYDROGENASE-RXN`, `category: molecular_activity`, `direction: left_to_right`, current `label: GLUTARYL-COA-DEHYDROGENASE-RXN`)
     - `reactions[4].label` (`id: MetaCyc:RXN-11662`, `category: molecular_activity`, `direction: reversible`, current `label: RXN-11662`)
- **Proposed Remediation (`A-C11S4-002` for Cycle 11 Stage 5)**:
  - Replace the `49` raw `local_id` `reactions[].label` strings across `MetaCyc:PWY0-321`, `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, and `MetaCyc:PWY-5177` with descriptive biochemical reaction labels verified against each record's catalyzed substrates/products and structured `references[].title`, record curation history entries under `history/records/<slug>/`, and refresh rendered pages (`pathwaymech-render-pages`).

---

## 3. Prior Findings Verified Resolved in Cycle 10 Stage 5 (`#781`)

- **`F-C10S4-001`** (`raw-local-id-structured-metacyc-reaction-reference-titles-2-records`, `2` records: `GO:0043427` and `MetaCyc:PWY-5744`, `26` `references[].title` entries): Verified `resolved` (`0` remaining raw `local_id` reference titles in both target records).
- **`F-C10S4-002`** (`raw-local-id-metacyc-reaction-labels-4-metacyc-records`, `4` records: `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, and `MetaCyc:PWY-7545`, `9` `reactions[].label` entries): Verified `resolved` (`0` remaining raw `local_id` reaction labels in all `4` target records).
