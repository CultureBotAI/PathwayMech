# PathwayMech Cycle 9 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `9`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `8e384d43128ac5777458583683afb5a7bee35db7`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml) (`sha256: c210ca0128b95d60ea2dfee5e4e51a8d13dd7417a6e7d10468f8f65a5db70c8c`)
- **Structured Review ID**: `20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: 0150bc9f1333a79e2113c4932d5ddb742e4fb177b3d9f2bedb07df7d194b40d2`)
  - [`reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261031T211500Z-cycle9-stage4-frozen-corpus-cohort-review/review.md) (`sha256: 0fc2222315ecf5ebb5c3e04d88d71a05c0f9d76bd86c484866e3c619a4049402`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 992c2ffb8a27fbb611550ff99ed5a437630eae7b18ed4c1c72031aa1f979ef06`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **278** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `8e384d43128ac5777458583683afb5a7bee35db7` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 135 | 5 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `PathBank` | 18 | 18 | 18 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **278** | **278** | **273** | **5** | `retain` (all 278) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `8e384d43128ac5777458583683afb5a7bee35db7`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 278 pathway records against closed LinkML schema, authority snapshots, 980 history records, 22,889 evidence blocks, 33 source records, 6 documentation files, deep-research report contract, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8106 passed, 3 skipped at frozen base. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed! |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 213 pre-existing structured review bundles + new Cycle 9 Stage 4 bundle (`214` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C9-IDENTITY-AND-CAUSAL-GRAPHS-ALL-278` — `supported`)**:
   - All 278 maintained pathway records (including `PathBank:SMP0002063` added in Cycle 9 Stage 1, the 7 MetaCyc records enriched with 248 stoichiometric coefficients, 62 ECO codes, and 62 assay taxa in Cycle 9 Stage 2, and the 6 MetaCyc records enriched across 38 `UniProtKB:*` edges and 18 reference titles in Cycle 9 Stage 3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings (`105` unique `NCBITaxon:*` CURIEs across `277` records; `data/pathways/gallate-degradation-i.yaml` intentionally sets `taxa: []` because its component enzymes span multiple organisms without a single source organism establishing the complete route), verified participant/reaction CURIEs, and `1,064` `source_mappings` rows across `219` records exporting to `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping fructoselysine and psicoselysine degradation pathways (`PathBank:SMP0002063` `Fructoselysine and Psicoselysine Degradation` in *Escherichia coli* alongside `MetaCyc:PWY0-521` `fructoselysine and psicoselysine degradation` and `GO:1901281` `fructoselysine catabolic process to glucose-6-phosphate and L-lysine`) as well as curcumin degradation (`PathBank:SMP0001910` alongside `GO:0036040`), non-mevalonate isoprenoid, succinate-to-propanoate, thiazole/thiamine, purine, branched-chain amino acid, cysteine, and aspartate/threonine pathways were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped and organism-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 278 records (`7,868` participants including `975` `UniProtKB:*` protein participant instances across `158` records, `1,633` reactions including `733` `RHEA:*` reactions, `14,753` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`21,763` on `mechanistic_edges` + `918` on `endpoint_qualifiers` = `22,681` edge/qualifier evidence items; `22,889` total evidence blocks including `208` `reaction_mechanisms` evidence items), 100% of `1,633` reactions explicitly declare `category` (`1,595 molecular_activity`, `36 pathway`, `2 biological_process`), and 100% of `RHEA:*` reactions (`733 / 733`) declare explicit `direction` with zero cross-record `RHEA:*` direction conflicts.
   - All `7,863` concrete participant entries across the 278-record corpus explicitly declare `participants[].category` (and the 5 generic `gomodel:*` physical participant instances intentionally omit `category` per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`), all 64 `category: chemical_entity` participant entries represent genuine chemical classes, generic electron/methyl donors or acceptors, carrier-protein conjugates, or amino-acid residues (`0` concrete `CHEBI:*` small molecules with defined formulas typed as `chemical_entity`), 100% of participants (`7,868 / 7,868`) are connected by at least one `mechanistic_edges` entry (0 orphan participants), 0 reflexive self-loops (`subject == object`) exist across all `14,753` `mechanistic_edges`, 0 `biolink:Protein|biolink:SmallMolecule` category conflicts and 0 pure `chemical_entity` vs `small_molecule` `biolink:ChemicalEntity|biolink:SmallMolecule` merges exist across all `5,463` nodes in `pages/downloads/nodes.tsv`, and 0 bare CURIE reference titles (`title == id`) remain across all `7,107` `references[]` entries, confirming that Cycle 8 Stage 4/5 findings `F-C8S4-001` and `F-C8S4-002` remain 100% resolved.
2. **16 Structured `MetaCyc:*` Reaction/Monomer/Metabolite `references[]` Entries with Raw Local-ID Titles (`title == local_id`) Across 3 MetaCyc Records and 11 Paired `MetaCyc:*`/`EcoCyc:*` Structured `references[]` Entries with Raw Local-ID Titles Plus 6 `MetaCyc:*` `reactions[]` Entries with Raw Local-ID Labels Across 2 MetaCyc Records (`ASSESS-C9-RAW-LOCAL-ID-STRUCTURED-REF-TITLES-AND-RXN-LABELS-5` — `concern`)**:
   - Across **3** maintained `MetaCyc:*` pathway records (`MetaCyc:PWY-8132` `data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml`, `MetaCyc:PWY-7255` `data/pathways/ergothioneine-biosynthesis-i.yaml`, and `MetaCyc:PWY0-1241` `data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml`), **16** structured `MetaCyc:*` reaction, monomer, and metabolite `references[]` entries (`1` in `s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml`, `7` in `ergothioneine-biosynthesis-i.yaml`, and `8` in `adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml`) store an unprefixed raw database frame identifier (`title == local_id`) instead of a descriptive reaction, enzyme monomer, or metabolite reference title (`F-C9S4-001`).
   - Across **2** maintained `MetaCyc:*` pathway records (`MetaCyc:THIOREDOX-PWY` `data/pathways/thioredoxin-pathway.yaml` and `MetaCyc:PWY-8178` `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`), **11** paired `MetaCyc:*` and `EcoCyc:*` reaction, protein-complex, metabolite, and regulation `references[]` entries in `thioredoxin-pathway.yaml` store an unprefixed raw database frame identifier (`title == local_id`) instead of a descriptive title, and the **6** `MetaCyc:*` `reactions[]` entries (`reactions[0..5]`) in `pentose-phosphate-pathway-non-oxidative-branch-ii.yaml` store raw frame IDs as reaction labels (`label == local_id`) (`F-C9S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C9S4-001` and `F-C9S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 9 Stage 5 (`record_remediation`).

### 3.1. Three MetaCyc Records with 16 Structured `MetaCyc:*` Reaction/Monomer/Metabolite `references[]` Entries Having Raw Unprefixed Frame ID `title == local_id` (`F-C9S4-001`)

| # | Pathway ID | File Path | Structured `MetaCyc:*` `references[]` Entries with Raw Local-ID `title == local_id` (16 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:PWY-8132` | `data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml` | 1 entry (`references[26]`): `MetaCyc:NADH` (`title: NADH`) |
| 2 | `MetaCyc:PWY-7255` | `data/pathways/ergothioneine-biosynthesis-i.yaml` | 7 entries (`references[1..7]`): `MetaCyc:GLUTCYSLIG-RXN` (`title: GLUTCYSLIG-RXN`), `MetaCyc:RXN-14431` (`title: RXN-14431`), `MetaCyc:RXN-14430` (`title: RXN-14430`), `MetaCyc:RXN-14429` (`title: RXN-14429`), `MetaCyc:RXN-18088` (`title: RXN-18088`), `MetaCyc:RXN-18089` (`title: RXN-18089`), `MetaCyc:RXN-15804` (`title: RXN-15804`) |
| 3 | `MetaCyc:PWY0-1241` | `data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml` | 8 entries (`references[0, 4, 5, 6, 8, 9, 10, 11]`): `MetaCyc:5.1.3.20-RXN` (`title: 5.1.3.20-RXN`), `MetaCyc:EG10838-MONOMER` (`title: EG10838-MONOMER`), `MetaCyc:G6106-MONOMER` (`title: G6106-MONOMER`), `MetaCyc:G7590-MONOMER` (`title: G7590-MONOMER`), `MetaCyc:RXN0-4301` (`title: RXN0-4301`), `MetaCyc:RXN0-4341` (`title: RXN0-4341`), `MetaCyc:RXN0-4342` (`title: RXN0-4342`), `MetaCyc:RXN0-4361` (`title: RXN0-4361`) |

### 3.2. Two MetaCyc Records with 11 Paired `MetaCyc:*`/`EcoCyc:*` `references[]` Entries Having Raw Local-ID `title == local_id` and 6 `MetaCyc:*` `reactions[]` Entries Having Raw Local-ID `label == local_id` (`F-C9S4-002`)

| # | Pathway ID | File Path | Affected `references[]` (11 total) and `reactions[]` (6 total) Entries |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:THIOREDOX-PWY` | `data/pathways/thioredoxin-pathway.yaml` | 11 `references[]` entries (`references[60, 61, 66, 70, 77, 78, 106, 108, 110, 112, 114]`): `MetaCyc:THIOREDOXIN-REDUCT-NADPH-RXN`, `MetaCyc:THIOREDOXIN-RXN`, `MetaCyc:NADPH`, `EcoCyc:THIOREDOXIN-REDUCT-NADPH-CPLX`, `EcoCyc:REG0-6357`, `EcoCyc:REG0-6358`, `EcoCyc:THIOREDOXIN-REDUCT-NADPH-RXN`, `EcoCyc:REG0-10687`, `EcoCyc:REG0-9797`, `EcoCyc:REG0-9025`, `EcoCyc:REG0-9024` |
| 2 | `MetaCyc:PWY-8178` | `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml` | 6 `reactions[]` entries (`reactions[0..5].label`): `MetaCyc:RXN-21730` (`label: RXN-21730`), `MetaCyc:SEDOBISALDOL-RXN` (`label: SEDOBISALDOL-RXN`), `MetaCyc:1TRANSKETO-RXN` (`label: 1TRANSKETO-RXN`), `MetaCyc:2TRANSKETO-RXN` (`label: 2TRANSKETO-RXN`), `MetaCyc:RIB5PISOM-RXN` (`label: RIB5PISOM-RXN`), `MetaCyc:RIBULP3EPIM-RXN` (`label: RIBULP3EPIM-RXN`) |
