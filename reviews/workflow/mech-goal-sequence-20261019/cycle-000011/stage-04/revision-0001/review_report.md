# Cycle 11 Stage 4 (`record_review`) Frozen-Corpus Cohort Review Report (Revision 1)

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage / Revision**: Cycle `11`, Stage `4` (`record_review`), Revision `1` (`revision-0001`)
- **Stage Action ID**: `333bc3800d62ed19e22c5576`
- **Workflow SHA-256**: `2b884e10c71589ce3f766556104bc45be8b6d17e8c301b3757a0f45808849ebe`
- **Frozen Inventory Snapshot**: `main` at commit `12cd8a123a63df8d89fa7517dd34c30eabd8c8bd`
- **Structured Review Bundle**: `reviews/structured/20261105T030500Z-cycle11-stage4-frozen-corpus-cohort-review/review.yaml` and `reviews/structured/20261105T030500Z-cycle11-stage4-frozen-corpus-cohort-review/review.md`
- **Previous Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-05/revision-0001/evidence.yaml` (`sha256: 18e651733d7ef10731c76e45fcbcb9a9f1f2e4c91c8fa111f3c14f77bcdfe2b9`)
- **Skills Applied**:
  - `.claude/skills/pathwaymech-evolve-workflow/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/review-yaml-category/SKILL.md`

---

## 1. Frozen Inventory Scope & Provenance

In accordance with the Stage 4 (`record_review`) contract, the complete maintained PathwayMech pathway corpus in `data/pathways/*.yaml` was audited across all `280` eligible records at frozen commit `12cd8a123a63df8d89fa7517dd34c30eabd8c8bd` without mutating any record in `data/pathways/*.yaml` or any rendered page in `pages/`.

| Metric | Value |
| --- | --- |
| Eligible records in frozen inventory (`data/pathways/*.yaml`) | `280` (`100.0%` coverage; `0` maintained records excluded) |
| Newly added record since Cycle 10 Stage 4 (`#779`) | `1` (`PathBank:SMP0002100` — `data/pathways/trehalose-biosynthesis-i-escherichia-coli.yaml`, added in Cycle 11 Stage 1 PR `#784`) |
| Records enriched in Cycle 11 Stage 2 (`#785`) | `8` (`MetaCyc:PWY-6419`, `MetaCyc:PWY-6223`, `GO:0019618`, `MetaCyc:QUINATEDEG-PWY`, `GO:0010139`, `GO:0019270`, `MetaCyc:PWY-6336`, `MetaCyc:THIOREDOX-PWY`) |
| Records enriched in Cycle 11 Stage 3 (`#788`) | `6` (`MetaCyc:PWY0-1312`, `MetaCyc:COA-PWY`, `MetaCyc:XYLCAT-PWY`, `MetaCyc:ARABCAT-PWY`, `MetaCyc:PYRIDOXSYN-PWY`, `MetaCyc:PWY-5686`) |
| Prior Cycle 10 Stage 4 findings verified resolved | `2 / 2` (`F-C10S4-001` and `F-C10S4-002`, closed in Cycle 10 Stage 5 PR `#781`) |
| Pathway records by namespace (`id` prefix) | `MetaCyc: 140`, `gomodel: 86`, `PathBank: 20`, `WikiPathways: 12`, `GO: 10`, `Reactome: 6`, `KEGG: 3`, `MIBiG: 3` |
| Pathway records by `pathway_type` | `100%` (`280 / 280`) declare `pathway_type` across `124` distinct values (top categories: `amino-acid-biosynthesis: 29`, `cofactor-biosynthesis: 20`, `carbohydrate-degradation: 17`, `lipid-biosynthesis: 15`, `amino-acid-degradation: 12`, `nucleotide-biosynthesis: 9`, `aromatic-compound-catabolism: 9`, `degradation: 7`, `central-carbon-metabolism: 7`, `biopax-pathway: 6`, `metabolic: 5`, `aromatic-compound-degradation: 5`) |
| Taxa coverage | `395` `taxa[]` entries across `105` distinct `NCBITaxon:*` IDs (`279` records have non-empty `taxa[]`; `1` record `MetaCyc:GALLATE-DEGRADATION-II-PWY` has `taxa: []`) |
| Total `participants` instances | `7,894` (`7,889` concrete with explicit `category` + `5` contract-verified generic `gomodel:*` physical participant instances; `979` `UniProtKB:*` protein participant instances across `160` records) |
| Total `reactions` instances | `1,637` (`1,599` `molecular_activity`, `36` `pathway`, `2` `biological_process`; `1,038` declare explicit `direction`: `799` `left_to_right`, `176` `right_to_left`, `63` `reversible`; `737` `RHEA:*` reactions across `160` records with `100%` explicit `direction`: `579` `left_to_right`, `156` `right_to_left`, `2` `reversible`) |
| Total `mechanistic_edges` | `14,788` (`21,823` edge evidence items + `923` `endpoint_qualifiers` evidence items = `22,746` edge/qualifier evidence items; `22,954` total evidence blocks including `208` `reaction_mechanisms` evidence items) |
| Total `references` entries | `7,121` (`0` bare CURIE titles where `title == id`; `79` structured `MetaCyc:*` reference entries across `4` records where `title == local_id`) |
| Total `source_mappings` entries | `1,068` across `221` records (`59` native records without `source_mappings`) |
| Stage 6 edge/qualifier extension adoption | `138` records (`49.29%`) carry at least one Stage 6 slot (`87` records carry `coefficient` on `1,876` edges; `103` records carry `eco_code` on `658` evidence items; `110` records carry `assay_taxon` on `1,404` evidence items; `41` records carry `endpoint_qualifiers` with `655` qualifiers on `644` edges; `5` records carry `encodes` on `21` edges) |
| Rendered KGX / browser parity | `280` records, `5,466` KGX nodes (`pages/downloads/nodes.tsv`), `14,788` KGX edges (`pages/downloads/edges.tsv`) |

Every record's exact relative path and `sha256` digest at frozen commit `12cd8a123a63df8d89fa7517dd34c30eabd8c8bd` is recorded in `reviews/structured/20261105T030500Z-cycle11-stage4-frozen-corpus-cohort-review/review.yaml` (`targets` and `evidence`) and in `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/coverage.json`.

---

## 2. Deterministic & Scientific Audit Summary

1. **Repository QC, Closed-Schema Validation, Pytest, Lint, Diff, and Review-Bundle Checks (`validate`, `test`, `lint`, `diff-check`, `review-check` — `passed`)**:
   - All `280` records pass strict LinkML schema validation (`src/pathwaymech/schema/pathwaymech.yaml`), semantic invariant checks (`src/pathwaymech/validate.py`), and `scripts/validate_id_label_correspondence.py` (`--check-plausibility`).
   - Full pytest suite (`8,124 passed, 3 skipped`), Ruff lint (`0` findings), `git diff --check` (`0` errors), and `scripts/record_review.py check` (`218` prior valid structured review bundles, `219` including this bundle) all pass with exit code `0`.
   - Cross-record duplicate pathway check confirmed zero unintended duplicate records. Overlapping pathways across distinct curated authority namespaces (`MetaCyc:P121-PWY` vs `PathBank:SMP0002081`, `MetaCyc:PWY0-43` vs `PathBank:SMP0002070`, `GO:0036040` vs `PathBank:SMP0001910`, `MetaCyc:PWY-5453` vs `PathBank:SMP0002091`, `MetaCyc:TRESYN-PWY` vs `PathBank:SMP0002100`, and `GO:0043427` vs `MetaCyc:PWY-5744`) represent distinct authority-scoped or route-scoped decompositions and are retained as separate records under `boundary_decisions` (`action: retain`) per `docs/HARMONIZATION.md`.
2. **Taxonomy & Assay-Organism Grounding (`ASSESS-C11-IDENTITY-AND-CAUSAL-GRAPHS-ALL-280` — `supported`)**:
   - All `395` `taxa[]` entries across `105` distinct `NCBITaxon:*` IDs (`279` records with non-empty `taxa[]`; `1` record `MetaCyc:GALLATE-DEGRADATION-II-PWY` with `taxa: []`) use verified `NCBITaxon:*` CURIEs and authoritative scientific names.
   - All `1,404` edge-level and qualifier-level `assay_taxon` annotations across `110` records (including those added in Cycle 11 Stage 2 and Stage 3) use verified `NCBITaxon:*` CURIEs.
3. **Participants & UniProtKB Protein Grounding (`ASSESS-C11-IDENTITY-AND-CAUSAL-GRAPHS-ALL-280` — `supported`)**:
   - `7,889 / 7,894` participant entries declare explicit `category` values (`small_molecule: 3,678`, `protein: 1,975`, `cofactor: 731`, `cellular_component: 460`, `complex: 403`, `molecular_activity: 255`, `gene: 140`, `biological_process: 86`, `lipid: 86`, `chemical_entity: 64`, `polymer: 6`, `pathway: 3`, `rna: 2`). The remaining `5` entries are contract-verified generic GO-CAM physical entity nodes in `gomodel:*` records (`gomodel:66187e4700000834` × 2, `gomodel:67c66be200001222` × 2, `gomodel:665912ed00002620` × 1) per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`.
   - `100%` of `7,894` participant nodes are connected by at least one `mechanistic_edges` entry (`0` orphan participants), and `0` concrete `CHEBI:*` small molecules with defined formulas are typed as `chemical_entity`.
   - `979` `UniProtKB:*` protein participant instances across `160` records (`57.14%` of corpus) match organism scope and verified UniProtKB accession identity.
4. **Reactions & RHEA Directionality (`ASSESS-C11-IDENTITY-AND-CAUSAL-GRAPHS-ALL-280` & `ASSESS-C11-RAW-LOCAL-ID-METACYC-REFS-AND-LABELS-11` — `concern`)**:
   - All `1,637` reactions across `280` records declare valid `category` (`molecular_activity: 1,599`, `pathway: 36`, `biological_process: 2`), `1,038` reactions declare explicit `direction` (`left_to_right: 799`, `right_to_left: 176`, `reversible: 63`), and `100%` of the `737` `RHEA:*` reactions across `160` records declare explicit `direction` (`left_to_right: 579`, `right_to_left: 156`, `reversible: 2`) with `0` cross-record direction conflicts.
   - **Open Finding (`F-C11S4-002` / `EV-C11-RAW-LOCAL-ID-METACYC-REACTION-LABELS-7`)**: Exhaustive check across all `1,637` reactions in the 280-record corpus confirmed that `49` `MetaCyc:*` `reactions[]` entries across `7` maintained `MetaCyc:*` pathway records (`MetaCyc:PWY0-321`: `11`; `MetaCyc:P321-PWY`: `8`; `MetaCyc:CENTBENZCOA-PWY`: `7`; `MetaCyc:PWY0-1477`: `6`; `MetaCyc:METH-ACETATE-PWY`: `6`; `MetaCyc:METHANOGENESIS-PWY`: `6`; `MetaCyc:PWY-5177`: `5`) store raw unprefixed MetaCyc reaction frame IDs (`label == local_id`) instead of descriptive biochemical reaction labels.
5. **Mechanistic Edges & Cycle 11 Stage 1–3 Verification (`ASSESS-C11-IDENTITY-AND-CAUSAL-GRAPHS-ALL-280` — `supported`)**:
   - All `14,788` `mechanistic_edges` use valid schema predicates (`produces: 2,304`, `consumes: 2,098`, `part_of: 1,202`, `has_output: 1,157`, `enables: 1,127`, `has_input: 1,095`, `has_cofactor: 1,070`, `catalyzes: 1,044`, `located_in: 872`, `provides_input_for: 773`, `has_part: 559`, `inhibits: 461`, `occurs_in: 361`, `precedes: 308`, `activates: 251`, `regulates: 65`, `encodes: 21`, `causally_upstream_of: 20`), connect declared intra-record nodes (`0` dangling endpoints, `0` reflexive self-loops), and carry `21,823` edge evidence items (`0` unsupported edges).
   - Newly added record `PathBank:SMP0002100` (`data/pathways/trehalose-biosynthesis-i-escherichia-coli.yaml`, Cycle 11 Stage 1), all `8` records enriched in Cycle 11 Stage 2 (`132` stoichiometric `coefficient` edges, `15` `eco_code` qualifiers across `14` edges, and `209` `assay_taxon` qualifiers across `125` edges), and all `6` records enriched in Cycle 11 Stage 3 (`61` `UniProtKB` protein edges enriched with `assay_taxon`, `25` with `eco_code`, and `26` `UniProtKB` reference titles replaced across `26` unique accessions) were verified against their structured sources and primary PMIDs.
6. **Evidence & Structured Reference Hygiene (`ASSESS-C11-RAW-LOCAL-ID-METACYC-REFS-AND-LABELS-11` — `concern`)**:
   - All `22,954` evidence blocks resolve to declared `references[]` entries (`0` unresolved `reference_id` values), and `0` `references[]` entries have bare CURIE titles (`title == id`).
   - Both Cycle 10 Stage 4 findings (`F-C10S4-001` across `GO:0043427` and `MetaCyc:PWY-5744`, and `F-C10S4-002` across `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, and `MetaCyc:PWY-7545`) were verified `100%` resolved in `main` following Cycle 10 Stage 5 (`#781`).
   - **Open Finding (`F-C11S4-001` / `EV-C11-RAW-LOCAL-ID-METACYC-REF-TITLES-4`)**: Exhaustive check across all `7,121` `references[]` entries in the 280-record corpus confirmed that `79` structured `MetaCyc:*` `references[]` entries across `4` maintained `MetaCyc:*` pathway records (`MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`: `31`; `MetaCyc:PWY-6823`: `20`; `MetaCyc:CALVIN-PWY`: `16`; `MetaCyc:THISYN-PWY`: `12`) store a raw unprefixed database frame identifier (`title == local_id`) instead of a descriptive MetaCyc reference title.
7. **Source Mappings & Rendered KGX / Browser Parity (`ASSESS-C11-IDENTITY-AND-CAUSAL-GRAPHS-ALL-280` — `supported`)**:
   - All `1,068` `source_mappings` entries across `221` records have valid `target`, `predicate`, and `evidence` fields, and rendered browser data and KGX exports (`pages/data.js`, `pages/index.html`, `pages/pathways/*.html`, `pages/downloads/nodes.tsv`, `pages/downloads/edges.tsv`) are in exact sync (`pathwaymech-render-pages --check` exit `0`).

---

## 3. Open Findings Preserved for Cycle 11 Stage 5 (`resolve_review_findings`)

Two minor, confirmed `representation` findings spanning **11** distinct pathway records (`128` total field instances: `79` `references[].title` entries + `49` `reactions[].label` entries) are recorded with `status: open` and carried forward in `carry_forward_ids` for grouped remediation in Cycle 11 Stage 5 (`A-C11S4-001` and `A-C11S4-002`):

| Finding ID | Issue Key | Category | Severity | Certainty | Target Records (`11` total) | Affected Field Count | Assigned Action ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C11S4-001` | `raw-local-id-structured-metacyc-reference-titles-4-records` | `representation` | `minor` | `confirmed` | `MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, `MetaCyc:THISYN-PWY` | `79` `references[].title` entries (`31 + 20 + 16 + 12`) | `A-C11S4-001` |
| `F-C11S4-002` | `raw-local-id-metacyc-reaction-labels-7-metacyc-records` | `representation` | `minor` | `confirmed` | `MetaCyc:PWY0-321`, `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, `MetaCyc:PWY-5177` | `49` `reactions[].label` entries (`11 + 8 + 7 + 6 + 6 + 6 + 5`) | `A-C11S4-002` |

See `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/review_findings.md` for the complete per-record and per-field specification.

---

## 4. Boundary Decisions & Limitations

- **Namespace & Cross-Authority Boundary Decisions (`boundary_decisions[0..8]` in `review.yaml`, `action: retain`)**:
  - Retain all `280` maintained pathway records across all `8` identifier namespaces (`GO: 10`, `KEGG: 3`, `MIBiG: 3`, `MetaCyc: 140`, `PathBank: 20`, `Reactome: 6`, `WikiPathways: 12`, `gomodel: 86`) as distinct, non-duplicate source-scoped pathway definitions verified against local authority snapshots and `docs/HARMONIZATION.md`.
  - Specifically retain `PathBank:SMP0002100` (`data/pathways/trehalose-biosynthesis-i-escherichia-coli.yaml`, added in Cycle 11 Stage 1) alongside `MetaCyc:TRESYN-PWY` (`data/pathways/trehalose-biosynthesis-i.yaml`): `PathBank:SMP0002100` captures the native PathBank `PW002088.owl` BioPAX boundary in *Escherichia coli* (`NCBITaxon:562` / `NCBITaxon:83333`) with cellular-compartment (`GO:0005829` cytosol) `located_in` and `occurs_in` qualifiers, protein complex participants (`PathBank:SMP0002100/ProteinComplex/3954` `UniProtKB:P31677` and `PathBank:SMP0002100/ProteinComplex/3955` `UniProtKB:P31678`), directional Rhea steps (`RHEA:18890` and `RHEA:23421`), and explicit SSSOM `source_mappings` (`skos:closeMatch` to `MetaCyc:TRESYN-PWY` and `skos:broadMatch` to `GO:0005992`).
- **Limitations (`limitations` in `review.yaml`)**:
  - Four maintained `MetaCyc:*` pathway records (`MetaCyc:BIOTIN-BIOSYNTHESIS-PWY`, `MetaCyc:PWY-6823`, `MetaCyc:CALVIN-PWY`, and `MetaCyc:THISYN-PWY`) retain `79` structured `MetaCyc:*` `references[]` entries with raw unprefixed frame ID titles (`title == local_id`) (`F-C11S4-001`), and seven maintained `MetaCyc:*` pathway records (`MetaCyc:PWY0-321`, `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, `MetaCyc:PWY0-1477`, `MetaCyc:METH-ACETATE-PWY`, `MetaCyc:METHANOGENESIS-PWY`, and `MetaCyc:PWY-5177`) retain `49` `MetaCyc:*` `reactions[]` entries with raw frame ID labels (`label == local_id`) (`F-C11S4-002`); both are preserved unedited as open minor findings for Cycle 11 Stage 5 grouped remediation (`A-C11S4-001` and `A-C11S4-002`).
  - Verification of literature-backed evidence blocks relied on the repository's local authority snapshots and curated evidence quotes/abstracts at frozen commit `12cd8a123a63df8d89fa7517dd34c30eabd8c8bd` without re-fetching external publisher full texts over the network.
