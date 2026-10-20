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
    summary: Add optional typed stoichiometry, gene-expression predicate, and construct/ECO evidence slots in src/pathwaymech/schema/pathwaymech.yaml
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
- **Observation**: `pathwaymech.curation.publish_curation` (`src/pathwaymech/curation.py`) serializes updated records with `yaml.safe_dump(doc, stream, sort_keys=False, allow_unicode=True, width=88)`. In `data/pathways/entner-doudoroff-pathway.yaml` (`GO:0008615`), `mechanistic_edges` evidence lists use YAML anchor aliases (`&id001`..`&id011` and `*id001`..`*id011`) across edges `ed-022`..`ed-068`, which `yaml.safe_dump` expands rather than preserving. In addition, records originally formatted at `width=120` (such as `data/pathways/adenine-and-adenosine-salvage-ii.yaml` and `data/pathways/ethylmalonyl-coa-pathway.yaml`) experience multi-hundred-line wrapping churn when rewritten with a fixed `width=88`.
- **Desired outcome**: Enhance `src/pathwaymech/curation.py` so guarded publication preserves existing YAML anchor aliases and per-file line-wrap formatting (or supports round-trip/surgical AST updates after open + closed LinkML validation).
- **Evidence paths**: `src/pathwaymech/curation.py`, `data/pathways/entner-doudoroff-pathway.yaml`, `data/pathways/adenine-and-adenosine-salvage-ii.yaml`, `data/pathways/ethylmalonyl-coa-pathway.yaml`, `history/other/stage2-causal-graph-review-2026-10-20/2026-10-20T090200Z-antigravity-a1d1e5.yaml`
- **Priority**: medium
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

### `pathwaymech-infra-0003` — Structured LinkML slots for stoichiometric coefficients, gene-to-protein expression edges, and construct/ECO qualifiers

- **Originating run / cycle / stage**: `mech-goal-sequence-20261019` / cycle `1` / stage `2` (`causal_graphs`)
- **Observation**: During whole-corpus Stage 2 causal-graph review of all 270 records in `data/pathways/*.yaml`, three schema-level representation constraints in `src/pathwaymech/schema/pathwaymech.yaml` were identified: (1) `MechanisticEdge` has no typed numeric `stoichiometric_coefficient` slot, requiring reaction and complex subunit stoichiometries on `consumes`, `produces`, `has_input`, `has_output`, `part_of`, and `has_part` edges to be recorded in prose `description` or `evidence[].source_assertion` fields; (2) `PredicateEnum` has no gene-expression predicate (`encodes` / `transcribed_to`), preventing `Entrez:*` gene participants regulated in `PathBank:SMP0002081`, `PathBank:SMP0002083`, and `KEGG:M00373` from being linked directly to their encoded `UniProtKB:*` protein participants by a formal `mechanistic_edges` edge; and (3) `EvidenceItem` lacks structured `construct_context`, `assay_taxon`, and `eco_code` slots, requiring recombinant tag, strain, and ECO evidence-code qualifiers to be embedded in `source_assertion` or edge `description`.
- **Desired outcome**: Evaluate and add optional backward-compatible LinkML slots/predicates in `src/pathwaymech/schema/pathwaymech.yaml` and `src/pathwaymech/schema.py` (with corresponding KGX/page rendering support) during Stage 6 infrastructure implementation.
- **Evidence paths**: `src/pathwaymech/schema/pathwaymech.yaml`, `src/pathwaymech/schema.py`, `docs/CAUSAL_GRAPHS.md`, `history/other/stage2-causal-graph-review-2026-10-20/2026-10-20T090200Z-antigravity-a1d1e5.yaml`
- **Priority**: low
- **Dependencies**: None
- **Status**: `note` (pending Stage 6 issue intake)

