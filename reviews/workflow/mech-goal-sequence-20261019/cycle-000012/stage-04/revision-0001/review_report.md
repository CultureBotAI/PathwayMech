# Cycle 12 Stage 4 (`record_review`) Frozen-Corpus Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage / Revision**: Cycle `12`, Stage `4` (`record_review`), Revision `1` (`revision-0001`)
- **Stage Action ID**: `ca56939ca2d904840a8dcf04` / `e7089a79d28f75ad8ddc9a2f`
- **Workflow SHA-256**: `2b884e10c71589ce3f766556104bc45be8b6d17e8c301b3757a0f45808849ebe`
- **Frozen Inventory Snapshot**: `main` at commit `b3ce30812ac7cf1bb39965a9073a225f5736ee93`
- **Structured Review Bundle**: `reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml` and `reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.md`
- **Previous Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-05/revision-0001/evidence.yaml` (`sha256: 520e37ef722598d97d2672a6f2aaec81594aa5d606f0a0cb2bc0f5d9540a51bc`)
- **Skills Applied**:
  - `.claude/skills/pathwaymech-evolve-workflow/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/review-yaml-category/SKILL.md`

---

## 1. Frozen Inventory Scope & Provenance

In accordance with the Stage 4 (`record_review`) contract, the complete maintained PathwayMech pathway corpus in `data/pathways/*.yaml` was audited across all `281` eligible records at frozen commit `b3ce30812ac7cf1bb39965a9073a225f5736ee93` without mutating any record in `data/pathways/*.yaml` or any rendered page in `pages/`.

| Metric | Value |
| --- | --- |
| Eligible records in frozen inventory (`data/pathways/*.yaml`) | `281` (`100.0%` coverage; `0` maintained records excluded) |
| Newly added record since Cycle 11 Stage 4 (`#790`) | `1` (`PathBank:SMP0002086` — `data/pathways/guanine-and-guanosine-salvage-escherichia-coli.yaml`, added in Cycle 12 Stage 1 PR `#794`) |
| Records enriched in Cycle 12 Stage 2 (`#795`) | `8` (`MetaCyc:PWY-8132`, `MetaCyc:PWY-6376`, `MetaCyc:PWY0-1338`, `MetaCyc:PWY-6151`, `MetaCyc:PWY0-301`, `MetaCyc:PWY-6416`, `MetaCyc:RIBOKIN-PWY`, `MetaCyc:PWY0-1517`) |
| Records enriched in Cycle 12 Stage 3 (`#796`) | `6` (`MetaCyc:GLYOXYLATE-BYPASS`, `MetaCyc:PWY-6123`, `MetaCyc:PWY-6124`, `MetaCyc:HOMOSER-METSYN-PWY`, `MetaCyc:NONMEVIPP-PWY`, `MetaCyc:NONOXIPENT-PWY`) |
| Prior Cycle 11 Stage 4 findings verified resolved | `2 / 2` (`F-C11S4-001` and `F-C11S4-002`, closed in Cycle 11 Stage 5 PR `#792` / issue `#791`) |
| Pathway records by namespace (`id` prefix) | `MetaCyc: 140`, `gomodel: 86`, `PathBank: 21`, `WikiPathways: 12`, `GO: 10`, `Reactome: 6`, `KEGG: 3`, `MIBiG: 3` |
| Pathway records by `pathway_type` | `100%` (`281 / 281`) declare `pathway_type` across `124` distinct values (top categories: `amino-acid-biosynthesis: 29`, `cofactor-biosynthesis: 20`, `carbohydrate-degradation: 17`, `lipid-biosynthesis: 15`, `amino-acid-degradation: 12`, `nucleotide-biosynthesis: 9`, `aromatic-compound-catabolism: 9`, `degradation: 7`, `central-carbon-metabolism: 7`, `biopax-pathway: 6`, `metabolic: 5`, `aromatic-compound-degradation: 5`) |
| Taxa coverage | `397` `taxa[]` entries across `105` distinct `NCBITaxon:*` IDs (`280` records have non-empty `taxa[]`; `1` record `MetaCyc:GALLATE-DEGRADATION-II-PWY` has `taxa: []`) |
| Total `participants` instances | `7,912` (`7,907` concrete with explicit `category` + `5` contract-verified generic `gomodel:*` physical participant instances; `982` `UniProtKB:*` protein participant instances across `161` records) |
| Total `reactions` instances | `1,640` (`1,602` `molecular_activity`, `36` `pathway`, `2` `biological_process`; `1,041` declare explicit `direction`: `801` `left_to_right`, `177` `right_to_left`, `63` `reversible`; `740` `RHEA:*` reactions across `161` records with `100%` explicit `direction`: `581` `left_to_right`, `157` `right_to_left`, `2` `reversible`) |
| Total `mechanistic_edges` | `14,814` (`21,878` edge evidence items + `923` `endpoint_qualifiers` evidence items = `22,801` edge/qualifier evidence items; `23,009` total evidence blocks including `208` `reaction_mechanisms` evidence items) |
| Total `references` entries | `7,132` (`0` bare CURIE titles where `title == id`; `0` raw local-ID titles where `title == local_id`; `7,085 / 7,132` carry an explicit `url`; `47` across `10` records omit `url`; `13` across `4` records carry generic `'Reactome reaction <id>'` or `'MIBiG literature reference <id>'` placeholder titles) |
| Total `source_mappings` entries | `1,071` across `222` records (`59` native records without `source_mappings`) |
| Stage 6 edge/qualifier extension adoption | `149` records (`53.02%`) carry at least one Stage 6 slot (`96` records carry `coefficient` on `2,002` edges; `115` records carry `eco_code` on `747` evidence items; `125` records carry `assay_taxon` on `1,935` evidence items; `41` records carry `endpoint_qualifiers` with `655` qualifiers on `644` edges; `5` records carry `encodes` on `21` edges) |
| Rendered KGX / browser parity | `281` records, `5,469` KGX nodes (`pages/downloads/nodes.tsv`), `14,814` KGX edges (`pages/downloads/edges.tsv`) |

Every record's exact relative path and `sha256` digest at frozen commit `b3ce30812ac7cf1bb39965a9073a225f5736ee93` is recorded in `reviews/structured/20261105T145000Z-cycle12-stage4-frozen-corpus-cohort-review/review.yaml` (`targets` and `evidence`) and in `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/coverage.json`.

---

## 2. Deterministic & Scientific Audit Summary

1. **Repository QC, Closed-Schema Validation, Pytest, Lint, Diff, and Review-Bundle Checks (`validate`, `test`, `lint`, `diff-check`, `review-check` — `passed`)**:
   - All `281` records pass strict LinkML schema validation (`src/pathwaymech/schema/pathwaymech.yaml`), semantic invariant checks (`src/pathwaymech/validate.py`), and `scripts/validate_id_label_correspondence.py` (`--check-plausibility`).
   - Full pytest suite (`8,126 passed, 3 skipped`), Ruff lint (`0` findings), `git diff --check` (`0` errors), and `scripts/record_review.py check` (`221` prior valid structured review bundles, `222` including this Cycle 12 Stage 4 bundle) all pass with exit code `0`.
   - Cross-record duplicate pathway check confirmed zero unintended duplicate records. Overlapping pathways across distinct curated authority namespaces (`MetaCyc:P121-PWY` vs `PathBank:SMP0002081`, `MetaCyc:PWY0-43` vs `PathBank:SMP0002070`, `GO:0036040` vs `PathBank:SMP0001910`, `MetaCyc:PWY-5453` vs `PathBank:SMP0002091`, `MetaCyc:TRESYN-PWY` vs `PathBank:SMP0002100`, `MetaCyc:PWY-6579` vs `PathBank:SMP0002086`, and `GO:0043427` vs `MetaCyc:PWY-5744`) represent distinct authority-scoped or route-scoped decompositions and are retained as separate records under `boundary_decisions` (`action: retain`) per `docs/HARMONIZATION.md`.
2. **Taxonomy & Assay-Organism Grounding (`ASSESS-C12-IDENTITY-AND-CAUSAL-GRAPHS-ALL-281` — `supported`)**:
   - All `397` `taxa[]` entries across `105` distinct `NCBITaxon:*` IDs (`280` records with non-empty `taxa[]`; `1` record `MetaCyc:GALLATE-DEGRADATION-II-PWY` with `taxa: []`) use verified `NCBITaxon:*` CURIEs and authoritative scientific names.
   - All `1,935` edge-level and qualifier-level `assay_taxon` annotations across `125` records (including those added in Cycle 12 Stage 1, Stage 2, and Stage 3) use verified `NCBITaxon:*` CURIEs.
3. **Participants & UniProtKB Protein Grounding (`ASSESS-C12-IDENTITY-AND-CAUSAL-GRAPHS-ALL-281` — `supported`)**:
   - `7,907 / 7,912` participant entries declare explicit `category` values (`small_molecule: 3,690`, `protein: 1,978`, `cofactor: 732`, `cellular_component: 460`, `complex: 405`, `molecular_activity: 255`, `gene: 140`, `biological_process: 86`, `lipid: 86`, `chemical_entity: 64`, `polymer: 6`, `pathway: 3`, `rna: 2`). The remaining `5` entries are contract-verified generic GO-CAM physical entity nodes in `gomodel:*` records (`gomodel:66187e4700000834` × 2, `gomodel:67c66be200001222` × 2, `gomodel:665912ed00002620` × 1) per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`.
   - `100%` of `7,912` participant nodes are connected by at least one `mechanistic_edges` entry (`0` orphan participants), and `0` concrete `CHEBI:*` small molecules with defined formulas are typed as `chemical_entity`.
   - `982` `UniProtKB:*` protein participant instances across `161` records (`57.30%` of corpus) match organism scope and verified UniProtKB accession identity.
4. **Reactions & RHEA Directionality (`ASSESS-C12-IDENTITY-AND-CAUSAL-GRAPHS-ALL-281` — `supported`)**:
   - All `1,640` reactions across `281` records declare valid `category` (`molecular_activity: 1,602`, `pathway: 36`, `biological_process: 2`), `1,041` reactions declare explicit `direction` (`left_to_right: 801`, `right_to_left: 177`, `reversible: 63`), and `100%` of the `740` `RHEA:*` reactions across `161` records declare explicit `direction` (`left_to_right: 581`, `right_to_left: 157`, `reversible: 2`) with `0` cross-record direction conflicts.
   - Prior Cycle 11 Stage 4 finding `F-C11S4-002` (`16` `source_context`-eligible `MetaCyc:*` `reactions[].label` entries across `MetaCyc:P321-PWY`, `MetaCyc:CENTBENZCOA-PWY`, and `MetaCyc:PWY-5177[0]` plus `33` verified authority-locked frame-only fallback reaction labels across `PHENYLACETATE_NODE_ROLES`, `ETHANOLAMINE_NODE_ROLES`, `ACETATE_METHANOGENESIS_NODE_ROLES`, `METHANOGENESIS_NODE_ROLES`, and `GLUTARYL_NODE_ROLES`) remains `100%` resolved.
5. **Mechanistic Edges & Cycle 12 Stage 1–3 Verification (`ASSESS-C12-IDENTITY-AND-CAUSAL-GRAPHS-ALL-281` — `supported`)**:
   - All `14,814` `mechanistic_edges` use valid schema predicates (`produces: 2,311`, `consumes: 2,104`, `part_of: 1,207`, `has_output: 1,157`, `enables: 1,128`, `has_input: 1,095`, `has_cofactor: 1,072`, `catalyzes: 1,046`, `located_in: 872`, `provides_input_for: 774`, `has_part: 559`, `inhibits: 463`, `occurs_in: 361`, `precedes: 308`, `activates: 251`, `regulates: 65`, `encodes: 21`, `causally_upstream_of: 20`), connect declared intra-record nodes (`0` dangling endpoints, `0` reflexive self-loops), and carry `21,878` edge evidence items (`0` unsupported edges).
   - Newly added record `PathBank:SMP0002086` (`data/pathways/guanine-and-guanosine-salvage-escherichia-coli.yaml`, Cycle 12 Stage 1), all `8` records enriched in Cycle 12 Stage 2 (`111` stoichiometric `coefficient` edges, `22` `eco_code` qualifiers across `22` edges, and `388` top-level / `440` total `assay_taxon` qualifiers across `235` edges), and all `6` records enriched in Cycle 12 Stage 3 (`78` `UniProtKB` protein edges enriched with `assay_taxon`, `54` with `eco_code`, and `32` `UniProtKB` reference titles replaced across `32` unique accessions) were verified against their structured sources and primary PMIDs.
6. **Evidence & Reference Hygiene (`ASSESS-C12-MISSING-REF-URLS-AND-PLACEHOLDER-TITLES-10` — `concern`)**:
   - All `23,009` evidence blocks resolve to declared `references[]` entries (`0` unresolved `reference_id` values), `0` `references[]` entries have bare CURIE titles (`title == id`), and `0` `references[]` entries have raw local-ID titles (`title == local_id`, confirming `F-C11S4-001` remains `100%` resolved).
   - **Open Finding (`F-C12S4-001` / `EV-C12-MISSING-REF-URLS-10`)**: Exhaustive check across all `7,132` `references[]` entries in the 281-record corpus confirmed that `47` `references[]` entries across `10` maintained pathway records (`Reactome:R-MTU-868688`: `12` at `references[0..11]`; `Reactome:R-MTU-879299`: `12` at `references[0..11]`; `Reactome:R-MTU-936721`: `8` at `references[0..7]`; `Reactome:R-MTU-936635`: `5` at `references[0..4]`; `Reactome:R-MTU-936654`: `3` at `references[0..2]`; `Reactome:R-MTU-879325`: `2` at `references[0..1]`; `WikiPathways:WP5060`: `2` at `references[0..1]`; `WikiPathways:WP5587`: `1` at `references[0]`; `MIBiG:BGC0002072`: `1` at `references[0]`; and `WikiPathways:WP296`: `1` at `references[0]`) omit an explicit resolvable `url` field (`7,085 / 7,132` carry `url`).
   - **Open Finding (`F-C12S4-002` / `EV-C12-PLACEHOLDER-REF-TITLES-4`)**: Exhaustive check across all `7,132` `references[]` entries in the 281-record corpus confirmed that `13` `references[]` entries across `4` maintained pathway records (`Reactome:R-MTU-879299`: `6` at `references[0..5]`; `Reactome:R-MTU-868688`: `5` at `references[0..4]`; `Reactome:R-MTU-879325`: `1` at `references[0]`; and `MIBiG:BGC0002072`: `1` at `references[0]`) retain generic identifier-repeating `'Reactome reaction <id>'` or `'MIBiG literature reference <id>'` placeholder titles instead of descriptive reaction or publication titles.
7. **Source Mappings & Rendered KGX / Browser Parity (`ASSESS-C12-IDENTITY-AND-CAUSAL-GRAPHS-ALL-281` — `supported`)**:
   - All `1,071` `source_mappings` entries across `222` records have valid `subject_id`, `predicate_id`, and `object_id` fields, and rendered browser data and KGX exports (`pages/data.js`, `pages/index.html`, `pages/pathways/*.html`, `pages/downloads/nodes.tsv`, `pages/downloads/edges.tsv`) are in exact sync (`pathwaymech-render-pages --check` exit `0`).

---

## 3. Open Findings Preserved for Cycle 12 Stage 5 (`resolve_review_findings`)

Two minor, confirmed `representation` findings spanning **10** distinct pathway records (`60` total field instances across `47` `references[]` entries: `47` missing `references[].url` fields + `13` placeholder `references[].title` fields) are recorded with `status: open` and carried forward in `carry_forward_ids` for grouped remediation in Cycle 12 Stage 5 (`A-C12S4-001` and `A-C12S4-002`):

| Finding ID | Issue Key | Category | Severity | Certainty | Target Records (`10` distinct total) | Affected Field Count | Assigned Action ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C12S4-001` | `missing-reference-urls-10-records` | `representation` | `minor` | `confirmed` | `Reactome:R-MTU-868688`, `Reactome:R-MTU-879299`, `Reactome:R-MTU-936721`, `Reactome:R-MTU-936635`, `Reactome:R-MTU-936654`, `Reactome:R-MTU-879325`, `WikiPathways:WP5060`, `WikiPathways:WP5587`, `MIBiG:BGC0002072`, `WikiPathways:WP296` | `47` `references[].url` entries (`12 + 12 + 8 + 5 + 3 + 2 + 2 + 1 + 1 + 1`) | `A-C12S4-001` |
| `F-C12S4-002` | `placeholder-reactome-and-mibig-reference-titles-4-records` | `representation` | `minor` | `confirmed` | `Reactome:R-MTU-879299`, `Reactome:R-MTU-868688`, `Reactome:R-MTU-879325`, `MIBiG:BGC0002072` | `13` `references[].title` entries (`6 + 5 + 1 + 1`) | `A-C12S4-002` |

See `reviews/workflow/mech-goal-sequence-20261019/cycle-000012/stage-04/revision-0001/review_findings.md` for the complete per-record and per-field specification.

---

## 4. Boundary Decisions & Limitations

- **Namespace & Cross-Authority Boundary Decisions (`boundary_decisions[0..8]` in `review.yaml`, `action: retain`)**:
   - Retain all `281` maintained pathway records across all `8` identifier namespaces (`GO: 10`, `KEGG: 3`, `MIBiG: 3`, `MetaCyc: 140`, `PathBank: 21`, `Reactome: 6`, `WikiPathways: 12`, `gomodel: 86`) as distinct, non-duplicate source-scoped pathway definitions verified against local authority snapshots and `docs/HARMONIZATION.md`.
   - Specifically retain `PathBank:SMP0002086` (`data/pathways/guanine-and-guanosine-salvage-escherichia-coli.yaml`, added in Cycle 12 Stage 1) alongside `MetaCyc:PWY-6579` (`data/pathways/guanine-and-guanosine-salvage.yaml`): `PathBank:SMP0002086` captures the native PathBank `PW002074.owl` BioPAX boundary in *Escherichia coli* (`NCBITaxon:562` / `NCBITaxon:83333`) with direct monomeric `Gsk` (`UniProtKB:P0AEW6`) catalysis of `RHEA:27711` alongside hexameric `DeoD` (`PathBank:SMP0002086/ProteinComplex/4056`) catalyzing `RHEA:13234` and tetrameric `Gpt` (`PathBank:SMP0002086/ProteinComplex/4059`) catalyzing `RHEA:25426` and 3 SSSOM `source_mappings`.
- **Limitations (`limitations` in `review.yaml`)**:
   - Ten maintained pathway records (`Reactome:R-MTU-868688`, `Reactome:R-MTU-879299`, `Reactome:R-MTU-936721`, `Reactome:R-MTU-936635`, `Reactome:R-MTU-936654`, `Reactome:R-MTU-879325`, `WikiPathways:WP5060`, `WikiPathways:WP5587`, `MIBiG:BGC0002072`, and `WikiPathways:WP296`) retain `47` `references[]` entries omitting a resolvable `url` field (`F-C12S4-001`), and four of those records (`Reactome:R-MTU-879299`, `Reactome:R-MTU-868688`, `Reactome:R-MTU-879325`, and `MIBiG:BGC0002072`) retain `13` `references[]` entries with generic `'Reactome reaction <id>'` or `'MIBiG literature reference <id>'` placeholder titles (`F-C12S4-002`); both are preserved unedited as open minor findings for Cycle 12 Stage 5 grouped remediation (`A-C12S4-001` and `A-C12S4-002`).
   - Verification of literature-backed evidence blocks relied on the repository's local authority snapshots and curated evidence quotes/abstracts at frozen commit `b3ce30812ac7cf1bb39965a9073a225f5736ee93` without re-fetching external publisher full texts over the network.
