# PathwayMech Cycle 8 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `2cf03ac05f40abb493c82adee36be1de3ea17ad8`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml) (`sha256: a6e2daa3ecbba006e1c180bf8404fc98f8e78fb7a688b28db565fef7a186c5e2`)
- **Structured Review ID**: `20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: cddd8690b03dff36b5b2c5b60fd75022c84cc928c30dafea8d75513aa82304f8`)
  - [`reviews/structured/20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261031T094500Z-cycle8-stage4-frozen-corpus-cohort-review/review.md) (`sha256: e901193926e4c117752193588f8f75644de1738109dab3ae55c3883f9a0b1728`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 60e85b9bbc1f3fee8b419f2975529627f1d50b99f992b4cae017603886800b41`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **277** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `2cf03ac05f40abb493c82adee36be1de3ea17ad8` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 132 | 8 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `PathBank` | 17 | 17 | 17 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **277** | **277** | **269** | **8** | `retain` (all 277) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `2cf03ac05f40abb493c82adee36be1de3ea17ad8`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 277 pathway records against closed LinkML schema, authority snapshots, 955 history records, 22,832 evidence blocks, 33 source records, 6 documentation files, deep-research report contract, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8096 passed, 3 skipped at frozen base. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed! |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 211 pre-existing structured review bundles + new Cycle 8 Stage 4 bundle (`212` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C8-IDENTITY-AND-CAUSAL-GRAPHS-ALL-277` — `supported`)**:
   - All 277 maintained pathway records (including `PathBank:SMP0001910` added in Cycle 8 Stage 1, the 8 MetaCyc/gomodel records enriched with 248 stoichiometric coefficients, 62 ECO codes, and 62 assay taxa in Cycle 8 Stage 2, and the 6 MetaCyc records enriched across 38 `UniProtKB:*` edges and 16 reference titles in Cycle 8 Stage 3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings (`105` unique `NCBITaxon:*` CURIEs across `276` records; `data/pathways/gallate-degradation-i.yaml` intentionally sets `taxa: []` because its component enzymes span multiple organisms without a single source organism establishing the complete route), verified participant/reaction CURIEs, and `1,061` `source_mappings` rows across `218` records exporting to `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping curcumin degradation pathways (`PathBank:SMP0001910` `Curcumin Degradation` in *Escherichia coli* alongside `GO:0036040` `curcumin catabolic process`) as well as non-mevalonate isoprenoid, succinate-to-propanoate, thiazole/thiamine, purine, branched-chain amino acid, cysteine, and aspartate/threonine pathways were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped and organism-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 277 records (`7,851` participants including `972` `UniProtKB:*` protein participants across `157` records, `1,630` reactions including `731` `RHEA:*` reactions, `14,730` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`21,706` on `mechanistic_edges` + `918` on `endpoint_qualifiers` = `22,624` edge/qualifier evidence items; `22,832` total evidence blocks including `208` `reaction_mechanisms` evidence items), 100% of `1,630` reactions explicitly declare `category` (`1,592 molecular_activity`, `36 pathway`, `2 biological_process`), and 100% of `RHEA:*` reactions (`731 / 731`) declare explicit `direction` with zero cross-record `RHEA:*` direction conflicts.
   - All `7,846` concrete participant entries across the 277-record corpus explicitly declare `participants[].category` (and the 5 generic `gomodel:*` physical participant instances intentionally omit `category` per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`), 100% of participants (`7,851 / 7,851`) are connected by at least one `mechanistic_edges` entry (0 orphan participants), 0 reflexive self-loops (`subject == object`) exist across all `14,730` `mechanistic_edges`, 0 `biolink:Protein|biolink:SmallMolecule` category conflicts and 0 pure `chemical_entity` vs `small_molecule` `biolink:ChemicalEntity|biolink:SmallMolecule` merges exist across all `5,457` nodes in `pages/downloads/nodes.tsv`, and 0 bare CURIE reference titles (`title == id`) remain across all `7,099` `references[]` entries, confirming that Cycle 7 Stage 4/5 findings `F-C7S4-001` and `F-C7S4-002` remain 100% resolved.
2. **4 Concrete `CHEBI:*` Small-Molecule Effector Participants Typed as `chemical_entity` Across 4 MetaCyc Records and 17 Structured `MetaCyc:*` Reaction/Complex `references[]` Entries with Raw Local-ID Titles (`title == local_id`) Across 4 MetaCyc Records (`ASSESS-C8-SMALL-MOLECULE-EFFECTORS-AND-STRUCTURED-REF-TITLES-8` — `concern`)**:
   - Across **4** maintained `MetaCyc:*` pathway records (`MetaCyc:SALVADEHYPOX-PWY`, `MetaCyc:P184-PWY`, `MetaCyc:PWY-6336`, and `MetaCyc:PWY-7545`), **4** concrete `CHEBI:*` small-molecule effector participants with defined molecular formulas (`CHEBI:59640` `N-acetylglucosamine` in `adenosine-nucleotides-degradation-ii.yaml`, `CHEBI:22651` `ascorbate` in `protocatechuate-meta-cleavage.yaml` and `protocatechuate-para-cleavage.yaml`, and `CHEBI:203056` `Microcin J25` in `pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml`) are typed as generic `category: chemical_entity` instead of `category: small_molecule` (`F-C8S4-001`), whereas the remaining 64 `chemical_entity` entries in the corpus represent genuine chemical classes, generic electron/methyl donors or acceptors, carrier-protein conjugates, or amino-acid residues.
   - Across **4** maintained `MetaCyc:*` pathway records (`MetaCyc:PWY-6579` `data/pathways/guanine-and-guanosine-salvage.yaml`, `MetaCyc:PWY-7446` `data/pathways/sulfoquinovose-degradation-i.yaml`, `MetaCyc:PWY-7722` `data/pathways/sulfoquinovose-degradation-ii.yaml`, and `MetaCyc:DENITRIFICATION-PWY` `data/pathways/nitrate-reduction-i-denitrification.yaml`), **17** structured `MetaCyc:*` reaction and enzyme-complex `references[]` entries (`3` in `guanine-and-guanosine-salvage.yaml`, `4` in `sulfoquinovose-degradation-i.yaml`, `5` in `sulfoquinovose-degradation-ii.yaml`, and `5` in `nitrate-reduction-i-denitrification.yaml`) store an unprefixed raw database frame identifier (`title == local_id`) instead of a descriptive reaction or enzyme complex title (`F-C8S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C8S4-001` and `F-C8S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 8 Stage 5 (`record_remediation`).

### 3.1. Four MetaCyc Records with 4 Concrete `CHEBI:*` Small-Molecule Effector Participants Typed as `category: chemical_entity` (`F-C8S4-001`)

| # | Pathway ID | File Path | Concrete `CHEBI:*` Small-Molecule Effector `participants[]` Entry Typed as `chemical_entity` (4 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:SALVADEHYPOX-PWY` | `data/pathways/adenosine-nucleotides-degradation-ii.yaml` | `CHEBI:59640` (`N-acetylglucosamine`, formula `C8H15NO6`, `participants[62]`, activates `Entrez:945283` in `salvadehypox-edge-087`) |
| 2 | `MetaCyc:P184-PWY` | `data/pathways/protocatechuate-meta-cleavage.yaml` | `CHEBI:22651` (`ascorbate`, formula `C6H7O6-`, `participants[61]`, activates `MetaCyc:CPLX-2701` in `protocatechuate-meta-edge-075`) |
| 3 | `MetaCyc:PWY-6336` | `data/pathways/protocatechuate-para-cleavage.yaml` | `CHEBI:22651` (`ascorbate`, formula `C6H7O6-`, `participants[24]`, activates `MetaCyc:CPLX-7915` in `protocatechuate-para-edge-035`) |
| 4 | `MetaCyc:PWY-7545` | `data/pathways/pyruvate-to-cytochrome-bd-oxidase-electron-transfer.yaml` | `CHEBI:203056` (`Microcin J25`, formula `C100H139N23O27`, `participants[27]`, inhibits `EcoCyc:CYT-D-UBIOX-CPLX` in `pyruvate-bd-edge-030`) |

### 3.2. Four MetaCyc Records with 17 Structured `MetaCyc:*` Reaction/Complex `references[]` Entries Having Raw Unprefixed Frame ID `title == local_id` (`F-C8S4-002`)

| # | Pathway ID | File Path | Structured `MetaCyc:*` `references[]` Entries with Raw Local-ID `title == local_id` (17 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:PWY-6579` | `data/pathways/guanine-and-guanosine-salvage.yaml` | 3 entries (`references[3..5]`): `MetaCyc:RXN0-5199` (`title: RXN0-5199`), `MetaCyc:GUANPRIBOSYLTRAN-RXN` (`title: GUANPRIBOSYLTRAN-RXN`), `MetaCyc:GUANOSINEKIN-RXN` (`title: GUANOSINEKIN-RXN`) |
| 2 | `MetaCyc:PWY-7446` | `data/pathways/sulfoquinovose-degradation-i.yaml` | 4 entries (`references[1..4]`): `MetaCyc:RXN-15296` (`title: RXN-15296`), `MetaCyc:RXN-15297` (`title: RXN-15297`), `MetaCyc:RXN-15298` (`title: RXN-15298`), `MetaCyc:RXN-15299` (`title: RXN-15299`) |
| 3 | `MetaCyc:PWY-7722` | `data/pathways/sulfoquinovose-degradation-ii.yaml` | 5 entries (`references[1..5]`): `MetaCyc:RXN-17096` (`title: RXN-17096`), `MetaCyc:RXN-17095` (`title: RXN-17095`), `MetaCyc:RXN-17097` (`title: RXN-17097`), `MetaCyc:RXN-17098` (`title: RXN-17098`), `MetaCyc:RXN-17101` (`title: RXN-17101`) |
| 4 | `MetaCyc:DENITRIFICATION-PWY` | `data/pathways/nitrate-reduction-i-denitrification.yaml` | 5 entries (`references[1, 3, 4, 5, 63]`): `MetaCyc:RXN-11236` (`title: RXN-11236`), `MetaCyc:RXN-15838` (`title: RXN-15838`), `MetaCyc:NITRIC-OXIDE-REDUCTASE-RXN` (`title: NITRIC-OXIDE-REDUCTASE-RXN`), `MetaCyc:RXN-12130` (`title: RXN-12130`), `MetaCyc:CPLX-1701` (`title: CPLX-1701`) |
