# Cycle 10 Stage 4 (`record_review`) Frozen-Corpus Cohort Review Report (Revision 2)

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage / Revision**: Cycle `10`, Stage `4` (`record_review`), Revision `2` (`revision-0002`)
- **Stage Action ID**: `013c9ceadd3c056f577e2344`
- **Workflow SHA-256**: `2b884e10c71589ce3f766556104bc45be8b6d17e8c301b3757a0f45808849ebe`
- **Frozen Inventory Snapshot**: `main` at commit `5d25cc28d8a2235ae9e98161043fc33c0efd600d` (pathway corpus bytes identical to `2c6bbbfc3fb9e53e1efbce7fb34f26da34b48093`)
- **Structured Review Bundle**: `reviews/structured/20261101T082500Z-cycle10-stage4-frozen-corpus-cohort-review-rev2/review.yaml` and `reviews/structured/20261101T082500Z-cycle10-stage4-frozen-corpus-cohort-review-rev2/review.md` (superseding `20261101T070500Z-cycle10-stage4-frozen-corpus-cohort-review`)
- **Superseded Workflow Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0001/evidence.yaml`
- **Skills Applied**:
  - `.claude/skills/pathwaymech-evolve-workflow/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/review-yaml-category/SKILL.md`

---

## 1. Frozen Inventory Scope & Provenance

In accordance with the Stage 4 (`record_review`) contract, the complete maintained PathwayMech pathway corpus in `data/pathways/*.yaml` was audited across all `279` eligible records without mutating any record in `data/pathways/*.yaml` or any rendered page in `pages/`. Revision `2` (`revision-0002`) supersedes `revision-0001` to incorporate four factual/prose corrections from the cold-start adversarial review of PR `#779` while preserving `revision-0001` and `20261101T070500Z-cycle10-stage4-frozen-corpus-cohort-review` byte-identical on `main`.

| Metric | Value |
| --- | --- |
| Eligible records in frozen inventory (`data/pathways/*.yaml`) | `279` (`100.0%` coverage; `0` maintained records excluded) |
| Newly added record since Cycle 9 Stage 4 (`#769`) | `1` (`PathBank:SMP0002091` — `data/pathways/methylglyoxal-degradation-iii-escherichia-coli.yaml`, added in Cycle 10 Stage 1 PR `#774`) |
| Records enriched in Cycle 10 Stage 2 (`#775`) | `8` (`MetaCyc:PWY1-3`, `MetaCyc:PWY0-43`, `MetaCyc:PWY-6534`, `MetaCyc:PWY-7181`, `MetaCyc:2PHENDEG-PWY`, `MetaCyc:PWY-6048`, `MetaCyc:SHIKIMATEDEG-PWY`, `MetaCyc:PWY-7990`) |
| Records enriched in Cycle 10 Stage 3 (`#778`) | `6` (`MetaCyc:PWY-6543`, `MetaCyc:PWY-6121`, `MetaCyc:PWY-6122`, `MetaCyc:ARO-PWY`, `MetaCyc:PROSYN-PWY`, `MetaCyc:TYRSYN`) |
| Prior Cycle 9 Stage 4 findings verified resolved | `2 / 2` (`F-C9S4-001` and `F-C9S4-002`, closed in Cycle 9 Stage 5 PR `#771`) |
| Pathway records by namespace (`id` prefix) | `MetaCyc: 140`, `gomodel: 86`, `PathBank: 19`, `WikiPathways: 12`, `GO: 10`, `Reactome: 6`, `KEGG: 3`, `MIBiG: 3` |
| Pathway records by `pathway_type` | `100%` (`279 / 279`) declare `pathway_type` across `120` distinct values (top categories: `amino-acid-biosynthesis: 29`, `cofactor-biosynthesis: 20`, `carbohydrate-degradation: 17`, `lipid-biosynthesis: 15`, `amino-acid-degradation: 12`, `nucleotide-biosynthesis: 9`, `aromatic-compound-catabolism: 9`, `degradation: 7`, `central-carbon-metabolism: 7`, `biopax-pathway: 6`, `metabolic: 5`, `aromatic-compound-degradation: 5`) |
| Total `participants` instances | `7,880` (`7,875` concrete with explicit `category` + `5` contract-verified generic `gomodel:*` physical participant instances; `977` `UniProtKB:*` protein participant instances across `159` records) |
| Total `reactions` instances | `1,635` (`1,597` `molecular_activity`, `36` `pathway`, `2` `biological_process`; `735` `RHEA:*` reactions with `100%` explicit `direction`: `577` `left_to_right`, `156` `right_to_left`, `2` `reversible`) |
| Total `mechanistic_edges` | `14,770` (`21,791` edge evidence items + `923` `endpoint_qualifiers` evidence items = `22,714` edge/qualifier evidence items; `22,922` total evidence blocks including `208` `reaction_mechanisms` evidence items) |
| Total `references` entries | `7,115` (`0` bare CURIE titles where `title == id`; `26` structured `MetaCyc:*` reaction reference entries across `2` records where `title == local_id`) |
| Total `source_mappings` entries | `1,066` across `220` records (`59` native records without `source_mappings`) |
| Stage 6 edge/qualifier extension adoption | `102` records (`36.56%`) carry at least one Stage 6 slot (`78` records carry `coefficient` on `1,735` edges; `45` records carry `evidence.evidence_code`; `44` records carry `evidence.taxon`) |
| Rendered KGX / browser parity | `279` records, `5,465` KGX nodes (`pages/downloads/nodes.tsv`), `14,770` KGX edges (`pages/downloads/edges.tsv`) |

Every record's exact relative path and `sha256` digest at frozen commit `5d25cc28d8a2235ae9e98161043fc33c0efd600d` is recorded in `reviews/structured/20261101T082500Z-cycle10-stage4-frozen-corpus-cohort-review-rev2/review.yaml` (`targets` and `evidence`) and in `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0002/coverage.json`.

---

## 2. Deterministic & Scientific Audit Summary

1. **Repository QC, Closed-Schema Validation, Pytest, Lint, Diff, and Review-Bundle Checks (`validate`, `test`, `lint`, `diff-check`, `review-check` — `passed`)**:
   - All `279` records pass strict LinkML schema validation (`src/pathwaymech/schema/pathwaymech.yaml`), semantic invariant checks (`src/pathwaymech/validate.py`), and `scripts/validate_id_label_correspondence.py` (`--check-plausibility`).
   - Full pytest suite (`8,110 passed, 3 skipped`), Ruff lint (`0` findings), `git diff --check` (`0` errors), and `scripts/record_review.py check` (`217` valid structured review bundles) all pass with exit code `0`.
   - Cross-record duplicate pathway check confirmed zero unintended duplicate records. Overlapping pathways across distinct curated authority namespaces (`MetaCyc:P121-PWY` vs `PathBank:SMP0002081`, `MetaCyc:PWY0-43` vs `PathBank:SMP0002070`, `GO:0036040` vs `PathBank:SMP0001910`, `MetaCyc:PWY-5453` vs `PathBank:SMP0002091`, and `GO:0043427` vs `MetaCyc:PWY-5744`) represent distinct authority-scoped or route-scoped decompositions and are retained as separate records under `boundary_decisions` (`action: retain`) per `docs/HARMONIZATION.md`.
2. **Taxonomy & Assay-Organism Grounding (`ASSESS-C10-IDENTITY-AND-CAUSAL-GRAPHS-ALL-279` — `supported`)**:
   - All `279` records declare valid `NCBITaxon:*` organism identifiers (`332` `taxa[]` entries across `78` distinct `NCBITaxon:*` IDs) with authoritative scientific names.
   - All edge-level and qualifier-level `evidence[].taxon` annotations added through Cycle 10 Stage 2 (`44` records) use verified `NCBITaxon:*` CURIEs.
3. **Participants & UniProtKB Protein Grounding (`ASSESS-C10-IDENTITY-AND-CAUSAL-GRAPHS-ALL-279` — `supported`)**:
   - `7,875 / 7,880` participant entries declare explicit `category` values (`small_molecule: 3,670`, `protein: 1,973`, `cofactor: 727`, `cellular_component: 460`, `complex: 403`, `molecular_activity: 255`, `gene: 140`, `biological_process: 86`, `lipid: 86`, `chemical_entity: 64`, `polymer: 6`, `pathway: 3`, `rna: 2`). The remaining `5` entries are contract-verified generic GO-CAM physical entity nodes in `gomodel:*` records (`gomodel:66187e4700000834` × 2, `gomodel:67c66be200001222` × 2, `gomodel:665912ed00002620` × 1) per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`.
   - `100%` of `7,880` participant nodes are connected by at least one `mechanistic_edges` entry (`0` orphan participants), and `0` concrete `CHEBI:*` small molecules with defined formulas are typed as `chemical_entity`.
   - `977` `UniProtKB:*` protein participant instances across `159` records (`56.99%` of corpus) match organism scope and verified UniProtKB accession identity.
4. **Reactions & RHEA Directionality (`ASSESS-C10-IDENTITY-AND-CAUSAL-GRAPHS-ALL-279` & `ASSESS-C10-RAW-LOCAL-ID-METACYC-RXN-REFS-AND-LABELS-6` — `concern`)**:
   - All `1,635` reactions across `279` records declare valid `category` (`molecular_activity: 1,597`, `pathway: 36`, `biological_process: 2`), `1,036` reactions declare explicit `direction` (`left_to_right: 797`, `right_to_left: 176`, `reversible: 63`), and `100%` of the `735` `RHEA:*` reactions declare explicit `direction` (`left_to_right: 577`, `right_to_left: 156`, `reversible: 2`) with `0` cross-record direction conflicts.
   - **Open Finding (`F-C10S4-002` / `EV-C10-RAW-LOCAL-ID-METACYC-REACTION-LABELS-4`)**: Across `4` maintained `MetaCyc:*` pathway records (`MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545`), `9` `MetaCyc:*` `reactions[]` entries store raw unprefixed MetaCyc reaction frame IDs (`label == local_id`, e.g., `ACETOACETYL-COA-TRANSFER-RXN`, `RXN-20154`, `RXN-2424`, `RXN0-5388`, `RXN-11496`) instead of descriptive biochemical reaction labels.
5. **Mechanistic Edges & Cycle 10 Stage 1–3 Verification (`ASSESS-C10-IDENTITY-AND-CAUSAL-GRAPHS-ALL-279` — `supported`)**:
   - All `14,770` `mechanistic_edges` use valid schema predicates (`produces: 2,299`, `consumes: 2,094`, `part_of: 1,200`, `has_output: 1,157`, `enables: 1,125`, `has_input: 1,095`, `has_cofactor: 1,066`, `catalyzes: 1,044`, `located_in: 872`, `provides_input_for: 772`, `has_part: 559`, `inhibits: 461`, `occurs_in: 361`, `precedes: 308`, `activates: 251`, `regulates: 65`, `encodes: 21`, `causally_upstream_of: 20`), connect declared intra-record nodes (`0` dangling endpoints, `0` reflexive self-loops), and carry `21,791` edge evidence items (`0` unsupported edges).
   - Newly added record `PathBank:SMP0002091` (`data/pathways/methylglyoxal-degradation-iii-escherichia-coli.yaml`, Cycle 10 Stage 1), all `8` records enriched in Cycle 10 Stage 2 (`103` stoichiometric coefficients, `19` ECO codes, `83` assay taxa across `59` edges), and all `6` records enriched in Cycle 10 Stage 3 (`64` `UniProtKB:*` `mechanistic_edges` and `28` reference titles) were verified against their structured sources and primary PMIDs.
6. **Evidence & Structured Reference Hygiene (`ASSESS-C10-RAW-LOCAL-ID-METACYC-RXN-REFS-AND-LABELS-6` — `concern`)**:
   - All `22,922` evidence blocks resolve to declared `references[]` entries (`0` unresolved `reference_id` values), and `0` `references[]` entries have bare CURIE titles (`title == id`).
   - Both Cycle 9 Stage 4 findings (`F-C9S4-001` across `MetaCyc:PWY-8132`, `MetaCyc:PWY-7255`, and `MetaCyc:PWY0-1241`, and `F-C9S4-002` across `MetaCyc:THIOREDOX-PWY` and `MetaCyc:PWY-8178`) were verified `100%` resolved in `main` following Cycle 9 Stage 5 (`#771`).
   - **Open Finding (`F-C10S4-001` / `EV-C10-RAW-LOCAL-ID-METACYC-RXN-REF-TITLES-2`)**: Across `2` maintained pathway records (`GO:0043427` and `MetaCyc:PWY-5744`), `26` structured `MetaCyc:*` reaction `references[]` entries (`13` in each record) store a raw unprefixed database frame identifier (`title == local_id`, e.g., `RXN0-5224`, `BIOTIN-CARBOXYL-RXN`, `RXN0-5055`, `RXN-8963`) instead of a descriptive MetaCyc reaction reference title.
7. **Source Mappings & Rendered KGX / Browser Parity (`ASSESS-C10-IDENTITY-AND-CAUSAL-GRAPHS-ALL-279` — `supported`)**:
   - All `1,066` `source_mappings` entries across `220` records have valid `target`, `predicate`, and `evidence` fields, and rendered browser data and KGX exports (`pages/data.js`, `pages/index.html`, `pages/pathways/*.html`, `pages/downloads/nodes.tsv`, `pages/downloads/edges.tsv`) are in exact sync (`pathwaymech-render-pages --check` exit `0`).

---

## 3. Open Findings Preserved for Cycle 10 Stage 5 (`resolve_review_findings`)

Two minor, confirmed `representation` findings spanning **6** distinct pathway records (`35` total field instances: `26` `references[].title` entries + `9` `reactions[].label` entries) are recorded with `status: open` and carried forward in `carry_forward_ids` for grouped remediation in Cycle 10 Stage 5 (`A-C10S4-001` and `A-C10S4-002`):

| Finding ID | Issue Key | Category | Severity | Certainty | Target Records (`6` total) | Affected Field Count | Assigned Action ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C10S4-001` | `raw-local-id-structured-metacyc-reaction-reference-titles-2-records` | `representation` | `minor` | `confirmed` | `GO:0043427`, `MetaCyc:PWY-5744` | `26` `references[].title` entries (`13` per record) | `A-C10S4-001` |
| `F-C10S4-002` | `raw-local-id-metacyc-reaction-labels-4-metacyc-records` | `representation` | `minor` | `confirmed` | `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545` | `9` `reactions[].label` entries (`4 + 1 + 2 + 2`) | `A-C10S4-002` |

See `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0002/review_findings.md` for the complete per-record and per-field specification.

---

## 4. Boundary Decisions & Limitations

- **Namespace & Cross-Authority Boundary Decisions (`boundary_decisions[0..8]` in `review.yaml`, `action: retain`)**:
  - Retain all `279` maintained pathway records across all `8` identifier namespaces (`GO: 10`, `KEGG: 3`, `MIBiG: 3`, `MetaCyc: 140`, `PathBank: 19`, `Reactome: 6`, `WikiPathways: 12`, `gomodel: 86`) as distinct, non-duplicate source-scoped pathway definitions verified against local authority snapshots and `docs/HARMONIZATION.md`.
  - Specifically retain `PathBank:SMP0002091` (`data/pathways/methylglyoxal-degradation-iii-escherichia-coli.yaml`, added in Cycle 10 Stage 1) alongside `MetaCyc:PWY-5386` (`data/pathways/methylglyoxal-degradation-i.yaml`), `MetaCyc:PWY-5453` (`data/pathways/methylglyoxal-degradation-iii.yaml`), and `gomodel:YeastPathways_PWY-901` (`data/pathways/methylglyoxal-catabolism.yaml`): `PathBank:SMP0002091` captures the native PathBank `PW002079.owl` BioPAX boundary in *Escherichia coli* (`NCBITaxon:562` / `NCBITaxon:83333`; NADPH-dependent methylglyoxal reduction to hydroxyacetone/acetol via L-glyceraldehyde 3-phosphate reductase Gpr/YghZ `UniProtKB:Q46851` `RHEA:27988` followed by NADH-dependent reduction of hydroxyacetone to `(S)`-propane-1,2-diol via the L-1,2-propanediol dehydrogenase / glycerol dehydrogenase complex `PathBank:SMP0002091/ProteinComplex/3935` `UniProtKB:P0A9S5` `RHEA:28668` and explicit SSSOM `source_mappings`).
- **Limitations (`limitations` in `review.yaml`)**:
  - Two maintained pathway records (`GO:0043427` and `MetaCyc:PWY-5744`) retain `26` structured `MetaCyc:*` reaction `references[]` entries with raw unprefixed frame ID titles (`title == local_id`) (`F-C10S4-001`), and four maintained `MetaCyc:*` records (`MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, and `MetaCyc:PWY-7545`) retain `9` `MetaCyc:*` `reactions[]` entries with raw frame ID labels (`label == local_id`) (`F-C10S4-002`); both are preserved unedited as open minor findings for Cycle 10 Stage 5 grouped remediation (`A-C10S4-001` and `A-C10S4-002`).
  - Verification of literature-backed evidence blocks relied on the repository's local authority snapshots and curated evidence quotes/abstracts at frozen commit `5d25cc28d8a2235ae9e98161043fc33c0efd600d` without re-fetching external publisher full texts over the network.
