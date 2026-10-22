# PathwayMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `pathwaymech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/PathwayMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: pathwaymech-infra-0001
    summary: Register UniProtKB, RHEA, and PMID authority entries in conf/identifier_sources.json and data/identifier_authorities/sources.json for remaining Escherichia coli PathBank primary BioPAX pathways in pathbank_primary_biopax.zip
    status: note
  - task_id: pathwaymech-infra-0002
    summary: Preserve YAML anchor aliases and existing line-wrap widths during guarded causal-graph publication in src/pathwaymech/curation.py
    status: note
  - task_id: pathwaymech-infra-0003
    summary: Add optional MechanisticEdge stoichiometry, EdgePredicateEnum gene-expression predicate, and EvidenceItem ECO/taxon slots in src/pathwaymech/schema/pathwaymech.yaml
    status: note
  - task_id: pathwaymech-infra-0004
    summary: Add SGD, NCBIProtein, Reactome, gomodel, and Entrez prefix declarations to CURIE_MAP in src/pathwaymech/sssom.py for protein and gene source_mappings export
    status: note
  - task_id: pathwaymech-infra-0005
    summary: Add BiGG reaction prefix mapping to _PREFIX_CATEGORIES in src/pathwaymech/kgx.py and validate within-record reaction category consistency in src/pathwaymech/schema.py
    status: note
```
<!-- mech-infra-tasks:end -->

## Tasks

### `pathwaymech-infra-0001` — Offline authority coverage for remaining *E. coli* PathBank primary BioPAX pathways

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `1` (`add_records`)
- **Observation**: `reports/local_source_ingestion/2026-10-08-pathbank-dbcan/pathbank/pathbank_primary_biopax.zip` contains 2,687 BioPAX Level 3 `.owl` files total, including 313 *Escherichia coli* (`NCBITaxon:562`) entries. Currently 10 `PathBank:*` primary records are in `data/pathways/` (including `PathBank:SMP0002081` from `PW002069.owl` in `data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml`) and 17 `pathbank-primary-2019-*` source keys are registered in `conf/identifier_sources.json` and `data/identifier_authorities/sources.json`. In the Stage 1 bounded slice (`PW002057`–`PW002078`, 21 *E. coli* metabolic `.owl` entries present in the archive), 4 are now represented as `PathBank:*` primary records (`PW002065` → `SMP0002077`, `PW002069` → `SMP0002081`, `PW002071` → `SMP0002083`, `PW002077` → `SMP0002089`), 6 duplicate existing `MetaCyc:*` or `KEGG:*` *E. coli* records (`PW002058`, `PW002061`, `PW002074`, `PW002075`, `PW002076`, `PW002078`), and the remaining 11 (`PW002057`, `PW002059`, `PW002060`, `PW002062`, `PW002063`, `PW002064`, `PW002066`, `PW002067`, `PW002068`, `PW002072`, `PW002073`)—along with uningested *E. coli* `.owl` entries in the 313-file archive—cannot yet pass `pathwaymech-check-identifiers` because their referenced `UniProtKB` protein accessions, `RHEA` reaction IDs, and `PMID` literature citations are not yet registered in `conf/identifier_sources.json` and `data/identifier_authorities/sources.json`.
- **Desired outcome**: Batch-register verified `UniProtKB`, `RHEA`, `PMID`, and `pathbank-primary-2019-PW*` authority entries in `conf/identifier_sources.json` and `data/identifier_authorities/sources.json` so the remaining non-duplicate *E. coli* PathBank pathways in `reports/local_source_ingestion/2026-10-08-pathbank-dbcan/pathbank/pathbank_primary_biopax.zip` can be admitted under `pathwaymech-check-identifiers`.
- **Evidence paths**: `conf/identifier_sources.json`, `data/identifier_authorities/sources.json`, `reports/local_source_ingestion/2026-10-08-pathbank-dbcan/pathbank/pathbank_primary_biopax.zip`, `src/pathwaymech/identifiers.py`
- **Priority**: medium
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

### `pathwaymech-infra-0002` — Preserve YAML anchor aliases and line-wrap widths in `pathwaymech.curation.publish_curation`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `2` (`causal_graphs`)
- **Observation**: `pathwaymech.curation.publish_curation` (`src/pathwaymech/curation.py`) serializes updated records by default with `yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=100)` (while custom `serialize=` lambdas in `scripts/curate_uniprot_cofactors.py` and `scripts/curate_gocam_chemical_identities.py` use `width=88`). In `data/pathways/entner-doudoroff-pathway.yaml` (`KEGG:M00008`), `mechanistic_edges` evidence lists use YAML anchor definitions (`&id001`..`&id011`) on edges `ed-edge-007`, `ed-edge-012`, `ed-edge-015`, `ed-edge-018`, `ed-edge-020`, `ed-edge-024` and aliases (`*id001`..`*id011`) across edges `ed-edge-034`..`ed-edge-037`, which `yaml.safe_dump` expands rather than preserving. In addition, records originally formatted at different line-wrap widths (such as `data/pathways/adenine-and-adenosine-salvage-ii.yaml` and `data/pathways/ethylmalonyl-coa-pathway.yaml`) experience multi-hundred-line wrapping churn when rewritten via full-document `yaml.safe_dump`.
- **Desired outcome**: Enhance `src/pathwaymech/curation.py` so guarded publication preserves existing YAML anchor aliases and per-file line-wrap formatting (or supports round-trip/surgical AST updates after open + closed LinkML validation).
- **Evidence paths**: `src/pathwaymech/curation.py`, `data/pathways/entner-doudoroff-pathway.yaml`, `data/pathways/adenine-and-adenosine-salvage-ii.yaml`, `data/pathways/ethylmalonyl-coa-pathway.yaml`, `history/other/stage2-causal-graph-review-2026-10-20/2026-10-20T090200Z-antigravity-a1d1e5.yaml`
- **Priority**: medium
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

### `pathwaymech-infra-0003` — Optional LinkML slots for `MechanisticEdge` stoichiometry, `EdgePredicateEnum` gene-to-protein expression edges, and `EvidenceItem` ECO/taxon qualifiers

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `2` (`causal_graphs`)
- **Observation**: While `MechanismEdge` (`src/pathwaymech/schema/pathwaymech.yaml:266-274`) defines `coefficient: integer` and `MechanisticEdge` (`src/pathwaymech/schema/pathwaymech.yaml:425-461`) defines structured `endpoint_qualifiers` (`EndpointQualifier` with `kind: experimental_construct | molecular_state`) to capture construct context and molecular states, three schema-level representation constraints in `src/pathwaymech/schema/pathwaymech.yaml` were identified during whole-corpus Stage 2 causal-graph review of all 270 records in `data/pathways/*.yaml`: (1) `MechanisticEdge` has no typed numeric `coefficient` / `stoichiometric_coefficient` slot, requiring reaction and complex subunit stoichiometries on top-level `consumes`, `produces`, `has_input`, `has_output`, `part_of`, and `has_part` edges in `mechanistic_edges` to be recorded in prose `description` or `evidence[].source_assertion` fields; (2) `EdgePredicateEnum` (`src/pathwaymech/schema/pathwaymech.yaml:621-662`) has no gene-expression predicate (`encodes` / `transcribed_to`), preventing `Entrez:*` gene participants regulated in `PathBank:SMP0002081` (`data/pathways/adenine-and-adenosine-salvage-i-escherichia-coli.yaml`) and `PathBank:SMP0002083` (`data/pathways/adenine-and-adenosine-salvage-ii.yaml`) from being linked directly to their encoded `UniProtKB:*` protein participants by a formal `mechanistic_edges` edge; and (3) `EvidenceItem` lacks structured `assay_taxon` and `eco_code` slots, requiring strain and ECO evidence-code qualifiers to be embedded in `source_assertion` or edge `description`.
- **Desired outcome**: Evaluate and add optional backward-compatible LinkML slots/predicates in `src/pathwaymech/schema/pathwaymech.yaml` and `src/pathwaymech/schema.py` (with corresponding KGX/page rendering support) during Stage 6 infrastructure implementation.
- **Evidence paths**: `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `docs/CAUSAL_GRAPHS.md`, `history/other/stage2-causal-graph-review-2026-10-20/2026-10-20T090200Z-antigravity-a1d1e5.yaml`
- **Priority**: low
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

### `pathwaymech-infra-0004` — Expand `CURIE_MAP` in `src/pathwaymech/sssom.py` to support `SGD`, `NCBIProtein`, `Reactome`, `gomodel`, and `Entrez` prefixes in `source_mappings`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `3` (`protein_examples`)
- **Observation**: During the Stage 3 (`protein_examples`) review of all 270 pathway records in `data/pathways/*.yaml`, `_validate_row` in `src/pathwaymech/sssom.py` (`lines 122–136`) validates `subject_id` and `object_id` in `source_mappings` against `CURIE_MAP` (`src/pathwaymech/sssom.py:13–32`), which currently declares only `CAS`, `CHEBI`, `ChemSpider`, `EcoCyc`, `HMDB`, `infores`, `KEGG`, `MetaCyc`, `PathBank`, `PubChem`, `semapv`, `skos`, `UniProt`, and `UniProtKB`. Consequently, `EcoCyc:`, `MetaCyc:`, and `UniProt:` protein unification links to `UniProtKB:` are accepted in `source_mappings`, whereas the 95 `Saccharomyces cerevisiae` records with native `SGD:S000...` protein participants (`85` `gomodel:YeastPathways_*` + `10` `WikiPathways:WP*`), the 5 records with `NCBIProtein:` participants (`biotin-biosynthesis-from-8-amino-7-oxononanoate-ii.yaml`, `d-galactonate-degradation.yaml`, `etheno-dna-adduct-alkb-dioxygenase-direct-reversal-repair.yaml`, `factor-420-biosynthesis-ii-mycobacterial.yaml`, `intra-aerobic-nitrite-reduction.yaml`), the `Reactome:R-MTU-*` record (`defective-mmp-1-causes-epidermolysis-bullosa-dystrophica-recessive.yaml`), and `Entrez:` gene records (`adenine-and-adenosine-salvage-i-escherichia-coli.yaml`, `adenine-and-adenosine-salvage-ii.yaml`) cannot record `SGD:`/`NCBIProtein:`/`Reactome:`/`gomodel:`/`Entrez:` → `UniProtKB:` rows in `source_mappings` without raising `ValueError: subject_id prefix '<PREFIX>' is not declared in the SSSOM curie_map` during `pathwaymech-render-pages` (`write_sssom_exports`).
- **Desired outcome**: Add `SGD`, `NCBIProtein`, `Reactome`, `gomodel`, and `Entrez` URI expansions to `CURIE_MAP` in `src/pathwaymech/sssom.py` (with corresponding unit tests in `tests/`) during Stage 6 infrastructure implementation so non-`EcoCyc`/`MetaCyc`/`UniProt` protein and gene cross-references can also be exported to `pages/downloads/mappings.sssom.tsv`.
- **Evidence paths**: `src/pathwaymech/sssom.py`, `src/pathwaymech/pages.py`, `data/pathways/*.yaml`, `history/other/stage3-uniprot-protein-review-2026-10-21/2026-10-21T194000Z-antigravity-a1d1e5.yaml`
- **Priority**: medium
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

### `pathwaymech-infra-0005` — Add `BiGG` reaction prefix mapping in `src/pathwaymech/kgx.py` and validate reaction `category` consistency in `src/pathwaymech/schema.py`

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `4` (`record_review`)
- **Observation**: During the Stage 4 (`record_review`) cohort and record review of all 270 pathway records in `data/pathways/*.yaml` at frozen commit `556074d91f600aa9e5ca97e0b4baef6d99513930` (`reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml`), two schema/exporter typing gaps were identified: (1) `_PREFIX_CATEGORIES` in `src/pathwaymech/kgx.py` (`lines 125–153`) maps `RHEA` and `EC` to `biolink:MolecularActivity` and `MetaCyc` to `biolink:Pathway`, but omits `BiGG`, so any `BiGG:*` reaction entry lacking an explicit `category: molecular_activity` (such as `BiGG:ACMANAptspp` at `reactions[13]` of `data/pathways/amino-sugar-superpathway.yaml` / `MetaCyc:GLCMANNANAUT-PWY`, tracked as `F-STAGE4-001`) falls back to `biolink:NamedThing` with an empty `source_category` in `pages/downloads/nodes.tsv`; and (2) `src/pathwaymech/schema.py` does not warn or fail when a single pathway record mixes `reactions[]` entries with explicit `category` values (`molecular_activity` or `pathway`) and `reactions[]` entries without `category` (tracked across 12 `MetaCyc:*` records and 33 reaction nodes as `F-STAGE4-002`).
- **Desired outcome**: While Stage 5 (`remediate_reviews`) resolves `F-STAGE4-001` and `F-STAGE4-002` directly in the affected `data/pathways/*.yaml` records, update `_PREFIX_CATEGORIES` in `src/pathwaymech/kgx.py` and reaction-category consistency validation in `src/pathwaymech/schema.py` during Stage 6 infrastructure implementation so future `BiGG:*` reaction nodes and mixed-category `reactions[]` lists are caught automatically.
- **Evidence paths**: `src/pathwaymech/kgx.py`, `src/pathwaymech/schema.py`, `data/pathways/amino-sugar-superpathway.yaml`, `reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`
- **Priority**: medium
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

