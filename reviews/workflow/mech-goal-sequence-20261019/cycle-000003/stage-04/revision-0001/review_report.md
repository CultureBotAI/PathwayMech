# PathwayMech Cycle 3 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `62848bb7170f46df448678b50fdcf5a659769034`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml) (`sha256: 9b874bcf4999ee0e26c53a404b5c91a3dd2ae02ac6a8ad9f97ae0b5785d6fde2`)
- **Structured Review ID**: `20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: fd03eb8c6906a6274d8fcd355d5bf22d73f69299c62c7c546cc7ff92f2fd2aa4`)
  - [`reviews/structured/20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review/review.md) (`sha256: e20cfc66a6bb319da1f836a67db2fed0c0ce322fe8e9b052561506c0fd36f319`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 6c128125322505089cfb9d042fd31ac284d7b40fafef51f3642b00e93819a1c5`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **272** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `62848bb7170f46df448678b50fdcf5a659769034` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 140 | 0 | `retain` |
| `gomodel` | 86 | 86 | 75 | 11 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `PathBank` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **272** | **272** | **261** | **11** | `retain` (all 272) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `62848bb7170f46df448678b50fdcf5a659769034`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 272 pathway records against closed LinkML schema, authority snapshots, 775 history records, 22,340 evidence blocks, 33 source records, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8,067 passed, 3 skipped at frozen base (`8,072 passed, 3 skipped` with new review bundle). |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed. |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 201 pre-existing structured review bundles + new Cycle 3 Stage 4 bundle (`202` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C3-IDENTITY-AND-CAUSAL-GRAPHS-ALL-272` — `supported`)**:
   - All 272 maintained pathway records (including `PathBank:SMP0000993` added in Cycle 3 Stage 1 and the 8 records enriched in Cycle 3 Stages 2-3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings, verified participant/reaction CURIEs (`CHEBI`, `UniProtKB`, `ComplexPortal`, `GO`, `SGD`, `RHEA`, `MetaCyc`, `BiGG`, `EcoCyc`, `Reactome`, `WikiPathways`, `MIBiG`, `KEGG`), and `796` `source_mappings` rows across `166` records exporting to `793` unique SSSOM rows in `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping cysteine biosynthesis from serine pathways (`PathBank:SMP0000993` `Secondary Metabolites: Cysteine Biosynthesis from Serine` and `MetaCyc:CYSTSYN-PWY` `cysteine biosynthesis I`), chorismate/enterobactin/2,3-dihydroxybenzoate biosynthesis pathways (`MetaCyc:ARO-PWY`, `MetaCyc:PWY-5901`, `MetaCyc:ENTBACSYN-PWY`), and aspartate/homoserine/threonine/lysine/ectoine pathways (`PathBank:SMP0000992`, `MetaCyc:HOMOSERSYN-PWY`, `MetaCyc:HOMOSER-THRESYN-PWY`, `MetaCyc:DAPLYSINESYN-PWY`, `MetaCyc:P101-PWY`) were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 272 records (`7,721` participants, `1,603` reactions including `704` `RHEA:*` reactions, `14,464` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`21,214` edge-level evidence items; `22,340` total evidence blocks across records, steps, and edges), 100% of `RHEA:*` reactions (`704 / 704`) declare explicit `direction`, and zero cross-record `RHEA:*` direction conflicts exist.
   - All `1,603 / 1,603` reaction nodes across the 272-record corpus explicitly declare `reactions[].category` (`1,565 molecular_activity`, `36 pathway`, `2 biological_process`), confirming that Cycle 2 Stage 4 findings `F-C2S4-001` and `F-C2S4-002` remain 100% resolved.
2. **Participant Category Typing & Cross-Record Chemical Entity Consistency (`ASSESS-C3-PARTICIPANT-TYPING-AND-CONSISTENCY-CONCERN-11` — `concern`)**:
   - While `7,710 / 7,721` participant entries across `265 / 272` maintained pathway records explicitly declare `participants[].category`, **7** maintained `gomodel:*` records omit explicit `participants[].category` on **11** participant entries (**6 `CHEBI:*` nodes** and **5 `gomodel:*` nodes**), causing all 11 participant CURIEs to export in `pages/downloads/nodes.tsv` with an empty `source_category` (`""`) and fallback Biolink categories (`F-C3S4-001`).
   - Additionally, **4** maintained `gomodel:*` amino-acid metabolism records type short-chain 2-oxoacid amino-acid intermediates (`CHEBI:11851` `3-methyl-2-oxobutanoate` and `CHEBI:16763` `2-oxobutanoate`) as `category: lipid` instead of `category: small_molecule`, conflicting with `small_molecule` typing in `MetaCyc:LEUSYN-PWY`, `MetaCyc:PANTO-PWY`, `MetaCyc:VALSYN-PWY`, and `MetaCyc:ILEUSYN-PWY` and producing merged Biolink category `biolink:ChemicalEntity|biolink:SmallMolecule` (`source_category='lipid|small_molecule'`) in `pages/downloads/nodes.tsv` (`F-C3S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C3S4-001` and `F-C3S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 3 Stage 5 (`resolve_review_findings`).

### 3.1. Seven `gomodel:*` Records with Omitted `participants[].category` (`F-C3S4-001`)

| # | Pathway ID | File Path | Untyped `participants[]` Entries | Participant CURIE(s) & Exact YAML Label(s) | Recommended `participants[].category` |
| ---: | --- | --- | --- | --- | --- |
| 1 | `gomodel:YeastPathways_PWY3O-15` | `data/pathways/chitin-biosynthesis.yaml` | `participants[0]` | `CHEBI:17029` (`chitin`) | `polymer` |
| 2 | `gomodel:YeastPathways_PWY-5670-1` | `data/pathways/epoxysqualene-biosynthesis.yaml` | `participants[8]`, `participants[15]` | `gomodel:YeastPathways_PWY-5670-1/654d809000002591` (`chemical entity`), `gomodel:YeastPathways_PWY-5670-1/654d809000002611` (`chemical entity`) | `chemical_entity`, `chemical_entity` |
| 3 | `gomodel:YeastPathways_PWY3O-697` | `data/pathways/folate-interconversions.yaml` | `participants[11]` | `CHEBI:134413` (`10-formyltetrahydrofolyl-(Glu)n polyanion`) | `small_molecule` |
| 4 | `gomodel:YeastPathways_PWY-1801-1` | `data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml` | `participants[7]` | `gomodel:YeastPathways_PWY-1801-1/65692e7e00001183` (`information biomacromolecule`) | `chemical_entity` |
| 5 | `gomodel:YeastPathways_PWY-5041` | `data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml` | `participants[15]` | `gomodel:ba4cc2f6-35b0-45f1-a3b5-7bf7a1e71bf8_RXN-7605` (`a methylated methyl donor`) | `chemical_entity` |
| 6 | `gomodel:YeastPathways_PWY3O-17` | `data/pathways/thiamine-biosynthesis.yaml` | `participants[30]`, `participants[31]`, `participants[32]`, `participants[33]` | `CHEBI:143915` (`[ThiS protein]-C-terminal Gly-NH-CH2-C(O)SH`), `CHEBI:29979` (`L-cysteine-S-yl group`), `CHEBI:29950` (`L-alanin-3-yl group`), `CHEBI:90873` (`carboxy-[ThiS protein]`) | `chemical_entity` (all 4) |
| 7 | `gomodel:YeastPathways_PWY-5080-1` | `data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml` | `participants[9]` | `gomodel:46fed9f2-cf0b-4568-b40e-557bd0cfffe5_RXN3O-9813` (`gomodel:46fed9f2-cf0b-4568-b40e-557bd0cfffe5_RXN3O-9813`, anonymous trans-2-enoyl-CoA intermediate) | `lipid` (or `chemical_entity`) |

### 3.2. Four `gomodel:*` Records Typing 2-Oxoacid Amino-Acid Intermediates as `category: lipid` (`F-C3S4-002`)

| # | Pathway ID | File Path | Affected `participants[]` Entry | Participant CURIE & Label | Current `category` | Sibling Records Typing Same CURIE as `small_molecule` |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `gomodel:YeastPathways_PWY3O-4105` | `data/pathways/valine-degradation.yaml` | `participants[3]` | `CHEBI:11851` (`3-methyl-2-oxobutanoate`) | `lipid` | `MetaCyc:LEUSYN-PWY`, `MetaCyc:PANTO-PWY`, `MetaCyc:VALSYN-PWY` |
| 2 | `gomodel:YeastPathways_HOMOCYS-CYS-CONVERT` | `data/pathways/homocysteine-and-cysteine-interconversion.yaml` | `participants[13]` | `CHEBI:16763` (`2-oxobutanoate`) | `lipid` | `MetaCyc:ILEUSYN-PWY` |
| 3 | `gomodel:YeastPathways_HOMOCYSDEGR-PWY-1` | `data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml` | `participants[9]` | `CHEBI:16763` (`2-oxobutanoate`) | `lipid` | `MetaCyc:ILEUSYN-PWY` |
| 4 | `gomodel:YeastPathways_THREOCAT2-PWY` | `data/pathways/threonine-degradation.yaml` | `participants[3]` | `CHEBI:16763` (`2-oxobutanoate`) | `lipid` | `MetaCyc:ILEUSYN-PWY` |
