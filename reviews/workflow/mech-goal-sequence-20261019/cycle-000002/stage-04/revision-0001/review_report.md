# PathwayMech Cycle 2 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `e369fa425e64d4f794ce84e2fd71138a43660467`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml) (`sha256: 8179b1fbe2d53c88fac719216c530765c2a442d3a43e8a0395bc2062c279a2c6`)
- **Structured Review ID**: `20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: 4d88adc1bed0bf1833b05a3a531b9b9e98762de8004301c4f84182675c82174c`)
  - [`reviews/structured/20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261022T134000Z-cycle2-stage4-frozen-corpus-cohort-review/review.md) (`sha256: 10b6c19fed03e2c03ac51c8df688316f5745dfbe016fcb248b36f07e03a16624`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: b0beb4e8c1102ce5f1a534eed01922d118dbbad2fcab2833a80ca81a717aed77`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **271** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `e369fa425e64d4f794ce84e2fd71138a43660467` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 84 | 56 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `PathBank` | 11 | 11 | 11 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **271** | **271** | **215** | **56** | `retain` (all 271) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `e369fa425e64d4f794ce84e2fd71138a43660467`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 271 pathway records against closed LinkML schema, authority snapshots, 654 history records, 22,211 evidence blocks, 33 source records, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8,066 passed, 3 skipped. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed. |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 199 pre-existing structured review bundles + new Cycle 2 Stage 4 bundle (`200` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity & Grounding (`ASSESS-C2-IDENTITY-GROUNDING-ALL-271` — `supported`)**:
   - All 271 maintained pathway records carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings, verified participant/reaction CURIEs (`CHEBI`, `UniProtKB`, `ComplexPortal`, `GO`, `SGD`, `RHEA`, `MetaCyc`, `BiGG`, `EcoCyc`, `Reactome`, `WikiPathways`, `MIBiG`, `KEGG`), and `615` `source_mappings` rows across `112` records exporting to `612` unique SSSOM rows in `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping aspartate/homoserine/threonine/lysine/ectoine pathways (`PathBank:SMP0000992`, `MetaCyc:HOMOSERSYN-PWY`, `MetaCyc:HOMOSER-THRESYN-PWY`, `MetaCyc:DAPLYSINESYN-PWY`, `MetaCyc:P101-PWY`) were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped pathway boundaries and step topologies (`action: retain`).
2. **Causal Graph & Evidence (`ASSESS-C2-CAUSAL-GRAPH-EVIDENCE-ALL-271` — `supported`)**:
   - Across all 271 records (`7,684` participants, `1,597` reactions including `699` `RHEA:*` reactions, `14,393` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`21,085` edge-level evidence items; `22,211` total evidence blocks across records, steps, and edges), 100% of `RHEA:*` reactions (`699 / 699`) declare explicit `direction`, and zero cross-record `RHEA:*` direction conflicts exist.
3. **Cross-Record Reaction Category Typing (`ASSESS-C2-CROSS-RECORD-REACTION-CATEGORY-CONCERN-56` — `concern`)**:
   - While 212 maintained pathway records with `reactions[]` (`86 gomodel:*`, `84 MetaCyc:*`, `12 WikiPathways:*`, `11 PathBank:*`, `10 GO:*`, `6 Reactome:*`, `3 KEGG:*`) explicitly declare `category` on 100% of their `1,318` reaction entries (`1,312` `molecular_activity` and `6` `pathway`) and 3 `MIBiG:*` records have `0` `reactions[]`, **56** maintained `MetaCyc:*` records omit `category: molecular_activity` across all **279** of their `reactions[]` entries (`263 RHEA:*` and `16 MetaCyc:*`).
   - Specifically, **16** of those 56 `MetaCyc:*` records contain **28** untyped occurrences of **23** shared catalytic reaction CURIEs (`22 RHEA:*` + `1 MetaCyc:DHBAMPLIG-RXN`) that explicitly declare `category: molecular_activity` in sibling records (`F-C2S4-001`), producing mixed `source_contexts` on `biolink:MolecularActivity` nodes in `pages/downloads/nodes.tsv`, while **231** unique reaction CURIEs (`216 RHEA:*` and `15 MetaCyc:*`) appearing exclusively in those 56 records fall back to `biolink:BiochemicalReaction` with empty `source_category` (`F-C2S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C2S4-001` and `F-C2S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 2 Stage 5 (`resolve_review_findings`).

### 3.1. Sixteen `MetaCyc:*` Records with Shared Cross-Record Reaction Category Inconsistency (`F-C2S4-001`)

| # | Pathway ID | File Path | Untyped Occurrences of Shared Reaction CURIEs | Total `reactions[]` in Record | Sibling Records Where Shared Reaction(s) Declare `category: molecular_activity` |
| ---: | --- | --- | --- | ---: | --- |
| 1 | `MetaCyc:ARABCAT-PWY` | `data/pathways/l-arabinose-degradation-i.yaml` | 1 (`reactions[2]` (`RHEA:22369`)) | 3 | `MetaCyc:LYXMET-PWY`, `MetaCyc:PWY0-301` |
| 2 | `MetaCyc:ARGDEGRAD-PWY` | `data/pathways/l-arginine-degradation-v.yaml` | 2 (`reactions[2]` (`RHEA:30757`), `reactions[3]` (`RHEA:15650`)) | 4 | `MetaCyc:CYANCAT-PWY`, `MetaCyc:PWY0-1471`, `MetaCyc:PWY0-41` |
| 3 | `MetaCyc:CALVIN-PWY` | `data/pathways/calvin-cycle.yaml` | 5 (`reactions[2]` (`RHEA:13679`), `reactions[3]` (`RHEA:17462`), `reactions[4]` (`RHEA:27628`), `reactions[5]` (`RHEA:10509`), `reactions[7]` (`RHEA:30168`)) | 13 | `PathBank:SMP0002406` |
| 4 | `MetaCyc:DAPLYSINESYN-PWY` | `data/pathways/l-lysine-biosynthesis-i.yaml` | 3 (`reactions[0]` (`RHEA:23777`), `reactions[1]` (`RHEA:24286`), `reactions[2]` (`RHEA:34172`)) | 10 | `PathBank:SMP0000992` |
| 5 | `MetaCyc:GALACTUROCAT-PWY` | `data/pathways/d-galacturonate-degradation-i.yaml` | 1 (`reactions[2]` (`RHEA:17090`)) | 5 | `KEGG:M00008` |
| 6 | `MetaCyc:GLUAMCAT-PWY` | `data/pathways/n-acetylglucosamine-degradation-i.yaml` | 2 (`reactions[0]` (`RHEA:22937`), `reactions[1]` (`RHEA:12173`)) | 2 | `MetaCyc:GLCMANNANAUT-PWY` |
| 7 | `MetaCyc:GLUCARDEG-PWY` | `data/pathways/d-glucarate-degradation-i.yaml` | 1 (`reactions[3]` (`RHEA:27378`)) | 5 | `MetaCyc:GALACTARDEG-PWY`, `MetaCyc:PWY0-1300` |
| 8 | `MetaCyc:GLUTATHIONESYN-PWY` | `data/pathways/glutathione-biosynthesis.yaml` | 1 (`reactions[0]` (`RHEA:13286`)) | 2 | `MetaCyc:PWY-7255` |
| 9 | `MetaCyc:HOMOSER-THRESYN-PWY` | `data/pathways/l-threonine-biosynthesis.yaml` | 2 (`reactions[0]` (`RHEA:13986`), `reactions[1]` (`RHEA:10841`)) | 2 | `PathBank:SMP0000992` |
| 10 | `MetaCyc:HOMOSERSYN-PWY` | `data/pathways/l-homoserine-biosynthesis.yaml` | 3 (`reactions[0]` (`RHEA:23777`), `reactions[1]` (`RHEA:24286`), `reactions[2]` (`RHEA:15763`)) | 3 | `PathBank:SMP0000992` |
| 11 | `MetaCyc:NONMEVIPP-PWY` | `data/pathways/methylerythritol-phosphate-pathway-i.yaml` | 1 (`reactions[0]` (`RHEA:12606`)) | 9 | `MetaCyc:THISYN-PWY` |
| 12 | `MetaCyc:NONOXIPENT-PWY` | `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml` | 1 (`reactions[0]` (`RHEA:14659`)) | 5 | `PathBank:SMP0002406` |
| 13 | `MetaCyc:OXIDATIVEPENT-PWY` | `data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml` | 1 (`reactions[1]` (`RHEA:12557`)) | 3 | `KEGG:M00008` |
| 14 | `MetaCyc:P101-PWY` | `data/pathways/ectoine-biosynthesis.yaml` | 2 (`reactions[0]` (`RHEA:23777`), `reactions[1]` (`RHEA:24286`)) | 5 | `PathBank:SMP0000992` |
| 15 | `MetaCyc:PWY-8383` | `data/pathways/myxochelin-a-and-b-biosynthesis.yaml` | 1 (`reactions[0]` (`MetaCyc:DHBAMPLIG-RXN`)) | 9 | `MetaCyc:PWY-5903` |
| 16 | `MetaCyc:PYRIDOXSYN-PWY` | `data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml` | 1 (`reactions[4]` (`RHEA:12606`)) | 7 | `MetaCyc:THISYN-PWY` |

### 3.2. All 56 `MetaCyc:*` Records Omitting `category: molecular_activity` Across `reactions[]` (`F-C2S4-002`)

| # | Pathway ID | File Path | Omitted `reactions[]` Count (by Prefix) | Finding Membership |
| ---: | --- | --- | --- | --- |
| 1 | `MetaCyc:ARABCAT-PWY` | `data/pathways/l-arabinose-degradation-i.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 2 | `MetaCyc:ARGDEG-III-PWY` | `data/pathways/l-arginine-degradation-iv.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 3 | `MetaCyc:ARGDEGRAD-PWY` | `data/pathways/l-arginine-degradation-v.yaml` | 4 (`RHEA`: 4, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 4 | `MetaCyc:ARGSYN-PWY` | `data/pathways/l-arginine-biosynthesis-i.yaml` | 9 (`RHEA`: 9, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 5 | `MetaCyc:ARO-PWY` | `data/pathways/chorismate-biosynthesis-i.yaml` | 7 (`RHEA`: 7, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 6 | `MetaCyc:AST-PWY` | `data/pathways/l-arginine-degradation-ii-ast-pathway.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 7 | `MetaCyc:CALVIN-PWY` | `data/pathways/calvin-cycle.yaml` | 13 (`RHEA`: 13, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 8 | `MetaCyc:COA-PWY` | `data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml` | 4 (`RHEA`: 4, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 9 | `MetaCyc:CYSTSYN-PWY` | `data/pathways/l-cysteine-biosynthesis-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 10 | `MetaCyc:DAPLYSINESYN-PWY` | `data/pathways/l-lysine-biosynthesis-i.yaml` | 10 (`RHEA`: 10, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 11 | `MetaCyc:DARABCAT-PWY` | `data/pathways/d-arabinose-degradation-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 12 | `MetaCyc:DENITRIFICATION-PWY` | `data/pathways/nitrate-reduction-i-denitrification.yaml` | 5 (`RHEA`: 0, `MetaCyc`: 5) | No (`F-C2S4-002`) |
| 13 | `MetaCyc:FUCCAT-PWY` | `data/pathways/l-fucose-degradation-i.yaml` | 4 (`RHEA`: 4, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 14 | `MetaCyc:GALACTUROCAT-PWY` | `data/pathways/d-galacturonate-degradation-i.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 15 | `MetaCyc:GLUAMCAT-PWY` | `data/pathways/n-acetylglucosamine-degradation-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 16 | `MetaCyc:GLUCARDEG-PWY` | `data/pathways/d-glucarate-degradation-i.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 17 | `MetaCyc:GLUTATHIONESYN-PWY` | `data/pathways/glutathione-biosynthesis.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 18 | `MetaCyc:GLUTORN-PWY` | `data/pathways/l-ornithine-biosynthesis-i.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 19 | `MetaCyc:GLYCEROLMETAB-PWY` | `data/pathways/glycerol-degradation-v.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 20 | `MetaCyc:GLYOXYLATE-BYPASS` | `data/pathways/glyoxylate-cycle.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 21 | `MetaCyc:HISTSYN-PWY` | `data/pathways/l-histidine-biosynthesis.yaml` | 10 (`RHEA`: 10, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 22 | `MetaCyc:HOMOSER-METSYN-PWY` | `data/pathways/l-methionine-biosynthesis-i.yaml` | 7 (`RHEA`: 7, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 23 | `MetaCyc:HOMOSER-THRESYN-PWY` | `data/pathways/l-threonine-biosynthesis.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 24 | `MetaCyc:HOMOSERSYN-PWY` | `data/pathways/l-homoserine-biosynthesis.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 25 | `MetaCyc:ILEUSYN-PWY` | `data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml` | 7 (`RHEA`: 7, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 26 | `MetaCyc:LEUSYN-PWY` | `data/pathways/l-leucine-biosynthesis.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 27 | `MetaCyc:NONMEVIPP-PWY` | `data/pathways/methylerythritol-phosphate-pathway-i.yaml` | 9 (`RHEA`: 9, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 28 | `MetaCyc:NONOXIPENT-PWY` | `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 29 | `MetaCyc:OXIDATIVEPENT-PWY` | `data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 30 | `MetaCyc:P101-PWY` | `data/pathways/ectoine-biosynthesis.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 31 | `MetaCyc:PANTO-PWY` | `data/pathways/phosphopantothenate-biosynthesis-i.yaml` | 4 (`RHEA`: 4, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 32 | `MetaCyc:PHESYN` | `data/pathways/l-phenylalanine-biosynthesis-i.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 33 | `MetaCyc:PLPSAL-PWY` | `data/pathways/pyridoxal-5-phosphate-salvage-i.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 34 | `MetaCyc:PPGPPMET-PWY` | `data/pathways/ppgpp-metabolism.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 35 | `MetaCyc:PROSYN-PWY` | `data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml` | 4 (`RHEA`: 4, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 36 | `MetaCyc:PWY-5686` | `data/pathways/ump-biosynthesis-i.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 37 | `MetaCyc:PWY-6121` | `data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 38 | `MetaCyc:PWY-6122` | `data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 39 | `MetaCyc:PWY-6123` | `data/pathways/inosine-5-phosphate-biosynthesis-i.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 40 | `MetaCyc:PWY-6124` | `data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml` | 5 (`RHEA`: 5, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 41 | `MetaCyc:PWY-6151` | `data/pathways/s-adenosyl-l-methionine-cycle-i.yaml` | 6 (`RHEA`: 5, `MetaCyc`: 1) | No (`F-C2S4-002`) |
| 42 | `MetaCyc:PWY-6543` | `data/pathways/4-aminobenzoate-biosynthesis-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 43 | `MetaCyc:PWY-6579` | `data/pathways/guanine-and-guanosine-salvage.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 44 | `MetaCyc:PWY-8383` | `data/pathways/myxochelin-a-and-b-biosynthesis.yaml` | 9 (`RHEA`: 0, `MetaCyc`: 9) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 45 | `MetaCyc:PWY0-1312` | `data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 46 | `MetaCyc:PYRIDNUCSAL-PWY` | `data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 47 | `MetaCyc:PYRIDNUCSYN-PWY` | `data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 48 | `MetaCyc:PYRIDOXSYN-PWY` | `data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml` | 7 (`RHEA`: 7, `MetaCyc`: 0) | Yes (`F-C2S4-001`, `F-C2S4-002`) |
| 49 | `MetaCyc:RHAMCAT-PWY` | `data/pathways/l-rhamnose-degradation-i.yaml` | 5 (`RHEA`: 4, `MetaCyc`: 1) | No (`F-C2S4-002`) |
| 50 | `MetaCyc:RIBOSYN2-PWY` | `data/pathways/flavin-biosynthesis-i.yaml` | 9 (`RHEA`: 9, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 51 | `MetaCyc:SERSYN-PWY` | `data/pathways/l-serine-biosynthesis-i.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 52 | `MetaCyc:TRESYN-PWY` | `data/pathways/trehalose-biosynthesis-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 53 | `MetaCyc:TRPSYN-PWY` | `data/pathways/l-tryptophan-biosynthesis.yaml` | 6 (`RHEA`: 6, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 54 | `MetaCyc:TYRSYN` | `data/pathways/l-tyrosine-biosynthesis-i.yaml` | 3 (`RHEA`: 3, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 55 | `MetaCyc:VALSYN-PWY` | `data/pathways/l-valine-biosynthesis.yaml` | 4 (`RHEA`: 4, `MetaCyc`: 0) | No (`F-C2S4-002`) |
| 56 | `MetaCyc:XYLCAT-PWY` | `data/pathways/d-xylose-degradation-i.yaml` | 2 (`RHEA`: 2, `MetaCyc`: 0) | No (`F-C2S4-002`) |
