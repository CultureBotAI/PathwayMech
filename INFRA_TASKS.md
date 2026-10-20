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

