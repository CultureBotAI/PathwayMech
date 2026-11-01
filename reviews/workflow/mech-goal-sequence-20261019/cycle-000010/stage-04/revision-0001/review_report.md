# Cycle 10 Stage 4 (`record_review`) Frozen-Corpus Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Repository**: `CultureBotAI/PathwayMech` (`pathwaymech`)
- **Cycle / Stage**: Cycle `10`, Stage `4` (`record_review`)
- **Stage Action ID**: `013c9ceadd3c056f577e2344`
- **Workflow SHA-256**: `2b884e10c71589ce3f766556104bc45be8b6d17e8c301b3757a0f45808849ebe`
- **Frozen Inventory Snapshot**: `main` at commit `2c6bbbfc3fb9e53e1efbce7fb34f26da34b48093`
- **Structured Review Bundle**: `reviews/structured/20261101T070500Z-cycle10-stage4-frozen-corpus-cohort-review/review.yaml` and `reviews/structured/20261101T070500Z-cycle10-stage4-frozen-corpus-cohort-review/review.md`
- **Skills Applied**:
  - `.claude/skills/pathwaymech-evolve-workflow/SKILL.md`
  - `.claude/skills/review-yaml-record/SKILL.md`
  - `.claude/skills/review-yaml-category/SKILL.md`

---

## 1. Frozen Inventory Scope & Provenance

In accordance with the Stage 4 (`record_review`) contract, the complete maintained PathwayMech pathway corpus in `data/pathways/*.yaml` was frozen at commit `2c6bbbfc3fb9e53e1efbce7fb34f26da34b48093` (immediately following Cycle 10 Stage 3 PR `#778`) and audited without mutating any record in `data/pathways/*.yaml` or any rendered page in `pages/`.

| Metric | Value |
| --- | --- |
| Eligible records in frozen inventory (`data/pathways/*.yaml`) | `279` (`100.0%` coverage; `0` excluded) |
| Newly added record since Cycle 9 Stage 4 (`#769`) | `1` (`PathBank:SMP0002091` — `data/pathways/pathbank-smp0002091-methylglyoxal-degradation-iii.yaml`, added in Cycle 10 Stage 1 PR `#774`) |
| Records enriched in Cycle 10 Stage 2 (`#775`) | `8` (`MetaCyc:PWY1-3`, `MetaCyc:PWY0-43`, `MetaCyc:PWY-6534`, `MetaCyc:PWY-7181`, `MetaCyc:2PHENDEG-PWY`, `MetaCyc:PWY-6048`, `MetaCyc:SHIKIMATEDEG-PWY`, `MetaCyc:PWY-7990`) |
| Records enriched in Cycle 10 Stage 3 (`#778`) | `6` (`MetaCyc:PWY-6543`, `MetaCyc:PWY-6121`, `MetaCyc:PWY-6122`, `MetaCyc:ARO-PWY`, `MetaCyc:PROSYN-PWY`, `MetaCyc:TYRSYN`) |
| Prior Cycle 9 Stage 4 findings verified resolved | `2 / 2` (`F-C9S4-001` and `F-C9S4-002`, closed in Cycle 9 Stage 5 PR `#771`) |
| Pathway records by namespace (`id` prefix) | `MetaCyc: 140`, `gomodel: 86`, `PathBank: 19`, `WikiPathways: 12`, `GO: 10`, `Reactome: 6`, `KEGG: 3`, `MIBiG: 3` |
| Pathway records by `curation_status` | `curated: 145`, `draft: 134` |
| Pathway records by `pathway_type` | `metabolic: 263`, `biosynthetic: 11`, `signaling: 4`, `transport: 1` |
| Total `participants` instances | `7,880` (`7,875` concrete with explicit `category` + `5` contract-verified generic `gomodel:*` physical participant instances; `977` `UniProtKB:*` protein participant instances across `159` records) |
| Total `reactions` instances | `1,635` (`1,597` `molecular_activity`, `36` `pathway`, `2` `biological_process`; `735` `RHEA:*` reactions with `100%` explicit `direction`) |
| Total `mechanistic_edges` | `14,770` (`21,791` edge evidence items + `923` `endpoint_qualifiers` evidence items = `22,714` edge/qualifier evidence items; `22,922` total evidence blocks including `208` `reaction_mechanisms` evidence items) |
| Total `references` entries | `7,115` (`0` bare CURIE titles where `title == id`; `26` structured `MetaCyc:*` reaction reference entries across `2` records where `title == local_id`) |
| Total `source_mappings` entries | `1,066` across `220` records (`59` native records without `source_mappings`) |
| Stage 6 edge/qualifier extension adoption | `102` records (`36.56%`) carry at least one Stage 6 slot (`78` records carry `coefficient` on `1,735` edges; `45` records carry `evidence.evidence_code`; `44` records carry `evidence.taxon`) |
| Rendered KGX / browser parity | `279` records, `5,465` KGX nodes (`pages/downloads/nodes.tsv`), `14,770` KGX edges (`pages/downloads/edges.tsv`) |

Every record's exact relative path and `sha256` digest at frozen commit `2c6bbbfc3fb9e53e1efbce7fb34f26da34b48093` is recorded in `reviews/structured/20261101T070500Z-cycle10-stage4-frozen-corpus-cohort-review/review.yaml` (`targets` and `evidence`) and in `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0001/coverage.json`.

---

## 2. Deterministic & Scientific Audit Summary (`chk-01` .. `chk-08`)

1. **`chk-01` (`identity` — `pass`)**:
   - All `279` records pass strict LinkML schema validation (`src/pathwaymech/schema/pathwaymech.yaml`), semantic invariant checks (`src/pathwaymech/validate.py`), and `scripts/validate_id_label_correspondence.py` (`--check-plausibility`).
   - Exact 1:1 `id`, `slug`, and filename alignment holds across all `279` records.
   - Cross-record duplicate pathway check confirmed zero unintended duplicate records. Three pairs of records share an `NCBITaxon` and normalized `name` across distinct curated authority layers (`MetaCyc:ARGSYNBSUB-PWY` vs `PathBank:SMP0002153`, `MetaCyc:GLUTORN-PWY` vs `PathBank:SMP0029754`, and `GO:0043427` vs `MetaCyc:PWY-5744`) and are documented as explicit `keep_separate` boundary decisions (`bd-01`).
2. **`chk-02` (`taxonomy` — `pass`)**:
   - All `279` records declare valid `NCBITaxon:*` organism identifiers (`332` `taxa[]` entries across `78` distinct `NCBITaxon:*` IDs) with authoritative scientific names and explicit `role`.
   - All edge-level and qualifier-level `evidence[].taxon` annotations added through Cycle 10 Stage 2 (`44` records) use verified `NCBITaxon:*` CURIEs and canonical labels.
3. **`chk-03` (`participants` — `pass`)**:
   - `7,875 / 7,880` participant entries declare explicit `category` values (`small_molecule: 5,274`, `protein: 1,416`, `chemical_entity: 970`, `gene_product: 109`, `protein_complex: 61`, `macromolecular_complex: 23`, `nucleic_acid: 22`). The remaining `5` entries are contract-verified generic GO-CAM physical entity nodes in `gomodel:*` records (`gomodel:66187e4700000834` × 2, `gomodel:67c66be200001222` × 2, `gomodel:665912ed00002620` × 1), documented under boundary decision `bd-02`.
   - `977` `UniProtKB:*` protein participant instances across `159` records (`56.99%` of corpus) match organism scope and verified UniProtKB accession identity.
4. **`chk-04` (`reactions` — `pass_with_caveats`)**:
   - All `1,635` reactions across `279` records declare valid `category`, valid `ec_number` format where present (`1,059` reactions), and `100%` explicit `direction` on all `735` `RHEA:*` reactions (`left_to_right: 676`, `bidirectional: 50`, `right_to_left: 6`, `unspecified: 3`).
   - All `208` `reaction_mechanisms` entries across `54` records carry valid step orders, MCSA/EBI/Rhea cross-references, and primary `PMID:*` / `DOI:*` support.
   - **Caveat (`F-C10S4-002`)**: Across `4` maintained `MetaCyc:*` pathway records (`MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545`), `9` `MetaCyc:*` `reactions[]` entries store raw unprefixed MetaCyc reaction frame IDs (`label == local_id`, e.g., `RXN-20154`, `RXN-2424`, `RXN0-5388`, `RXN-11496`) instead of descriptive reaction names.
5. **`chk-05` (`mechanistic_edges` — `pass`)**:
   - All `14,770` `mechanistic_edges` use valid schema predicates (`has_input: 5,442`, `has_output: 5,321`, `catalyzes: 2,621`, `precedes: 993`, `positively_regulates: 162`, `negatively_regulates: 109`, `transports: 67`, `requires_cofactor: 55`), connect declared intra-record nodes (`0` dangling endpoints), and carry `21,791` edge evidence items (`0` unsupported edges).
   - All `6` records enriched in Cycle 10 Stage 3 (`MetaCyc:PWY-6543`, `MetaCyc:PWY-6121`, `MetaCyc:PWY-6122`, `MetaCyc:ARO-PWY`, `MetaCyc:PROSYN-PWY`, `MetaCyc:TYRSYN`; `64` `UniProtKB:*` `mechanistic_edges` and `28` reference titles) and all `8` records enriched in Cycle 10 Stage 2 (`MetaCyc:PWY1-3`, `MetaCyc:PWY0-43`, `MetaCyc:PWY-6534`, `MetaCyc:PWY-7181`, `MetaCyc:2PHENDEG-PWY`, `MetaCyc:PWY-6048`, `MetaCyc:SHIKIMATEDEG-PWY`, `MetaCyc:PWY-7990`; `103` stoichiometric coefficients, `19` ECO codes, `83` assay taxa across `59` edges) were spot-checked against their structured sources and primary PMIDs.
6. **`chk-06` (`evidence` — `pass_with_caveats`)**:
   - All `22,922` evidence blocks resolve to declared `references[]` entries (`0` unresolved `reference_id` values), and `0` `references[]` entries have bare CURIE titles (`title == id`).
   - Both Cycle 9 Stage 4 findings (`F-C9S4-001` across `11` records and `F-C9S4-002` across `5` records) were verified closed in `main` following Cycle 9 Stage 5 (`#771`).
   - **Caveat (`F-C10S4-001`)**: Across `2` maintained pathway records (`GO:0043427` and `MetaCyc:PWY-5744`), `26` structured `MetaCyc:*` reaction `references[]` entries (`13` in each record) store a raw unprefixed database frame identifier (`title == local_id`, e.g., `RXN0-5224`, `BIOTIN-CARBOXYL-RXN`, `RXN0-5055`, `RXN-8963`) instead of a descriptive MetaCyc reaction reference title.
7. **`chk-07` (`source_mappings` — `pass`)**:
   - All `1,066` `source_mappings` entries across `220` records have valid `source_database`, `source_id`, `mapping_type`, and `evidence_tier`.
8. **`chk-08` (`cohort_duplicates` — `pass`)**:
   - Rendered browser data and KGX exports (`pages/data.js`, `pages/index.html`, `pages/pathways/*.html`, `pages/downloads/nodes.tsv`, `pages/downloads/edges.tsv`) are in exact sync (`pathwaymech-render-pages --check` exit `0`).

---

## 3. Open Findings Preserved for Cycle 10 Stage 5 (`resolve_review_findings`)

Two minor, confirmed `representation` findings spanning **6** distinct pathway records (`35` total field instances: `26` `references[].title` entries + `9` `reactions[].label` entries) are recorded with `status: open` and carried forward in `carry_forward_ids` for grouped remediation in Cycle 10 Stage 5:

| Finding ID | Issue Key | Category | Severity | Certainty | Target Records (`6` total) | Affected Field Count |
| --- | --- | --- | --- | --- | --- | --- |
| `F-C10S4-001` | `raw-local-id-structured-metacyc-reaction-reference-titles-2-records` | `representation` | `minor` | `confirmed` | `GO:0043427`, `MetaCyc:PWY-5744` | `26` `references[].title` entries (`13` per record) |
| `F-C10S4-002` | `raw-local-id-metacyc-reaction-labels-4-metacyc-records` | `representation` | `minor` | `confirmed` | `MetaCyc:ACETOACETATE-DEG-PWY`, `MetaCyc:PWY-1361`, `MetaCyc:PWY0-1352`, `MetaCyc:PWY-7545` | `9` `reactions[].label` entries (`4 + 1 + 2 + 2`) |

See `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-04/revision-0001/review_findings.md` for the complete per-record and per-field specification.

---

## 4. Limitations & Boundary Decisions

- **Boundary Decision `bd-01` (`keep_separate`)**: Three pairs of records (`MetaCyc:ARGSYNBSUB-PWY` vs `PathBank:SMP0002153`, `MetaCyc:GLUTORN-PWY` vs `PathBank:SMP0029754`, and `GO:0043427` vs `MetaCyc:PWY-5744`) represent distinct curated database decompositions across authority namespaces (`MetaCyc`, `PathBank`, `GO`) and are intentionally maintained as separate records.
- **Boundary Decision `bd-02` (`keep_as_is`)**: Five generic GO-CAM physical entity participant nodes across three `gomodel:*` records (`gomodel:66187e4700000834`, `gomodel:67c66be200001222`, `gomodel:665912ed00002620`) intentionally omit `participants[].category` where upstream GO-CAM models use `GO:0005575` (`cellular_component`) or `CHEBI:36080` (`protein`) as an unqualified physical entity placeholder.
- **Boundary Decision `bd-03` (`defer`)**: Remediation of `F-C10S4-001` (`2` records, `26` `references[].title` entries) and `F-C10S4-002` (`4` records, `9` `reactions[].label` entries) is deferred to Cycle 10 Stage 5 (`resolve_review_findings`) in accordance with the Stage 4 read-only pathway corpus contract.
- **Limitations (`lim-01`, `lim-02`, `lim-03`)**:
  - `lim-01`: Offline/sandboxed cohort review verifies primary literature quotes against curated record evidence blocks and local authority caches (`references_cache/`, `uniprot_cache/`) rather than re-fetching full-text paywalled publisher PDFs for all `7,115` references.
  - `lim-02`: `177 / 279` records (`63.44%`), primarily imported `gomodel:*`, `WikiPathways:*`, and legacy `MetaCyc:*` drafts, do not yet populate optional Stage 6 stoichiometric `coefficient`, `evidence.evidence_code`, or `evidence.taxon` slots; incremental backfill continues in Stage 2 (`curate_causal_graphs`) cycles.
  - `lim-03`: `120 / 279` records (`43.01%`) do not yet carry concrete `UniProtKB:*` protein participant nodes because they represent multi-taxon canonical pathways, imported GO-CAM models keyed by non-UniProt gene product identifiers (`SGD`, `NCBIProtein`, `ZFIN`, `MGI`), or non-enzymatic/pathway-level graphs; incremental backfill continues in Stage 3 (`add_uniprot_protein_examples`) cycles.
