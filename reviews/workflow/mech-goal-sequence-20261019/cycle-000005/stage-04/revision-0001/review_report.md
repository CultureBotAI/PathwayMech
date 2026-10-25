# PathwayMech Cycle 5 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `071f8b00c1abb4c0b3e394a3b44d866f59d31bad`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml) (`sha256: 6ae9515798a646c7637194cac974cf2608b4497991b79120365a9076a7d7b8de`)
- **Structured Review ID**: `20261025T152000Z-cycle5-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261025T152000Z-cycle5-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261025T152000Z-cycle5-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: c66a487f7259fe86e7436d49a4b2dfc3dd7e97974163a731f93c275cb4eca5ab`)
  - [`reviews/structured/20261025T152000Z-cycle5-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261025T152000Z-cycle5-stage4-frozen-corpus-cohort-review/review.md) (`sha256: 858b5146a0c2f010d7b5387059a560d5a2e9ffa8ceee1f838a96e52303b7163f`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 52d863131017d5f64addd3f08b6aefe27dbe5173d62143dde684bcf4da8f3364`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **274** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `071f8b00c1abb4c0b3e394a3b44d866f59d31bad` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 130 | 10 | `retain` |
| `gomodel` | 86 | 86 | 85 | 1 | `retain` |
| `PathBank` | 14 | 14 | 13 | 1 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **274** | **274** | **262** | **12** | `retain` (all 274) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `071f8b00c1abb4c0b3e394a3b44d866f59d31bad`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 274 pathway records against closed LinkML schema, authority snapshots, 880 history records, 22,608 evidence blocks, 33 source records, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8,078 passed, 3 skipped at frozen base. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed. |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 205 pre-existing structured review bundles + new Cycle 5 Stage 4 bundle (`206` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C5-IDENTITY-AND-CAUSAL-GRAPHS-ALL-274` — `supported`)**:
   - All 274 maintained pathway records (including `PathBank:SMP0002055` added in Cycle 5 Stage 1, the 8 records enriched in Cycle 5 Stage 2, and the 10 records enriched in Cycle 5 Stage 3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings (`382` taxon entries across `105` unique `NCBITaxon:*` CURIEs), verified participant/reaction CURIEs, and `1,049` `source_mappings` rows across `215` records exporting to `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping thiazole and thiamine biosynthesis pathways (`PathBank:SMP0002055` `Thiazole Biosynthesis I` in *Escherichia coli* K-12 alongside `PathBank:SMP0002042`, `MetaCyc:THISYN-PWY`, and `gomodel:YeastPathways_PWY3O-17`) as well as purine, branched-chain amino acid, cysteine, and aspartate/threonine pathways were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 274 records (`7,788` participants, `1,616` reactions including `717` `RHEA:*` reactions, `14,600` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`22,400` edge/qualifier evidence items; `22,608` total evidence blocks across records, steps, mechanisms, clusters, and edges), 100% of `1,616` reactions explicitly declare `category` (`1,578 molecular_activity`, `36 pathway`, `2 biological_process`) and `reaction_type` (`1,554 catalytic`, `48 transport`, `13 spontaneous`, `1 conformational_change`), and 100% of `RHEA:*` reactions (`717 / 717`) declare explicit `direction` with zero cross-record `RHEA:*` direction conflicts.
   - All `7,783` concrete participant entries across the 274-record corpus explicitly declare `participants[].category` (and the 5 generic `gomodel:*` physical participant instances intentionally omit `category` per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`), 100% of participants (`7,788 / 7,788`) are connected by at least one `mechanistic_edges` entry (0 orphan participants), and zero unreferenced `RHEA:*` entries remain in `references[]`, confirming that Cycle 4 Stage 4/5 findings `F-C4S4-001` and `F-C4S4-002` remain 100% resolved.
2. **Reflexive Self-Loop Edge in `gomodel:YeastPathways_PWY-6074-1` and 29 Non-UniProt Generic Authority Titles Across 11 Records (`ASSESS-C5-SELF-LOOP-AND-GENERIC-REFERENCE-TITLES-12` — `concern`)**:
   - In `gomodel:YeastPathways_PWY-6074-1` (`data/pathways/zymosterol-biosynthesis.yaml`), `mechanistic_edges[58]` (`id: edge-069`, lines 673–681) asserts a reflexive causal self-loop `gomodel:RXN3O-9822 causally_upstream_of gomodel:RXN3O-9822` (`source_assertion: "The model asserts gomodel:RXN3O-9822 RO:0002411 gomodel:RXN3O-9822."`, `source_locator: "./YeastPathways_PWY-6074-1.json#/facts/68; endpoint types: /individuals/58/type; /individuals/58/type"`). This is the sole reflexive self-loop (`subject == object`) across all `14,600` `mechanistic_edges` in the 274-record corpus (`F-C5S4-001`). Reaction `gomodel:RXN3O-9822` (`C-4 methylsterol oxidase activity`) is already connected to its upstream substrate `CHEBI:87289` (`4alpha-hydroxymethyl-4beta-methylzymosterol`, produced by `gomodel:RXN3O-9821` via `edge-040` and consumed via `edge-025`) and its downstream product `CHEBI:87287` (`4beta-methylzymosterol-4-carbaldehyde`, produced via `edge-103` and consumed by `gomodel:RXN3O-9823` via `edge-077`).
   - Across **11** maintained pathway records (**10** `MetaCyc:*` and **1** `PathBank:*`), **29** non-UniProt `references[]` entries (**26** `RHEA:*`, **1** `MetaCyc:RXN-15356`, and **2** `PMID:*`) retain generic `"<CURIE> authority record"` placeholder titles instead of descriptive reaction or literature titles (`F-C5S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C5S4-001` and `F-C5S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 5 Stage 5 (`resolve_review_findings`).

### 3.1. `gomodel:YeastPathways_PWY-6074-1` Reflexive Reaction Self-Loop (`F-C5S4-001`)

| Pathway ID | File Path | Field Path | Current Stale Value | Required Remediation in Cycle 5 Stage 5 |
| --- | --- | --- | --- | --- |
| `gomodel:YeastPathways_PWY-6074-1` | `data/pathways/zymosterol-biosynthesis.yaml` | `mechanistic_edges[58]` (`id: edge-069`) | `gomodel:RXN3O-9822 causally_upstream_of gomodel:RXN3O-9822` (`#/facts/68; endpoint types: /individuals/58/type; /individuals/58/type`) | Remove degenerate reflexive self-loop `edge-069` while retaining all substrate (`edge-025`, `edge-038`, `edge-068`), product (`edge-002`, `edge-058`, `edge-103`), catalysis (`edge-090`), and process-part (`edge-016`) edges on `gomodel:RXN3O-9822`. |

### 3.2. Eleven Records with Non-UniProt Generic `<CURIE> authority record` Reference Titles (`F-C5S4-002`)

| # | Pathway ID | File Path | Non-UniProt `references[]` Entries with Generic `<CURIE> authority record` Title (29 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:P101-PWY` | `data/pathways/ectoine-biosynthesis.yaml` | `RHEA:23776` (`references[7]`), `RHEA:24284` (`references[8]`), `RHEA:11160` (`references[9]`), `RHEA:16901` (`references[10]`), `RHEA:17281` (`references[11]`) |
| 2 | `MetaCyc:GLYOXYLATE-BYPASS` | `data/pathways/glyoxylate-cycle.yaml` | `RHEA:16846` (`references[7]`), `RHEA:10229` (`references[8]`), `RHEA:22145` (`references[9]`), `RHEA:21433` (`references[10]`), `RHEA:16845` (`references[11]`), `RHEA:21432` (`references[12]`), `PMID:16027371` (`references[13]`) |
| 3 | `MetaCyc:PWY-6124` | `data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml` | `PMID:21548610` (`references[12]`) |
| 4 | `MetaCyc:ARGSYN-PWY` | `data/pathways/l-arginine-biosynthesis-i.yaml` | `RHEA:18634` (`references[17]`), `RHEA:18633` (`references[18]`) |
| 5 | `MetaCyc:ARGDEG-III-PWY` | `data/pathways/l-arginine-degradation-iv.yaml` | `RHEA:17641` (`references[5]`), `RHEA:18037` (`references[6]`), `RHEA:22284` (`references[7]`) |
| 6 | `MetaCyc:CYSTSYN-PWY` | `data/pathways/l-cysteine-biosynthesis-i.yaml` | `RHEA:24560` (`references[6]`) |
| 7 | `MetaCyc:HOMOSERSYN-PWY` | `data/pathways/l-homoserine-biosynthesis.yaml` | `RHEA:23776` (`references[5]`), `RHEA:24284` (`references[6]`), `RHEA:15761` (`references[7]`) |
| 8 | `MetaCyc:RHAMCAT-PWY` | `data/pathways/l-rhamnose-degradation-i.yaml` | `MetaCyc:RXN-15356` (`references[6]`) |
| 9 | `MetaCyc:SERSYN-PWY` | `data/pathways/l-serine-biosynthesis-i.yaml` | `RHEA:12641` (`references[5]`), `RHEA:14329` (`references[6]`), `RHEA:21208` (`references[7]`) |
| 10 | `MetaCyc:HOMOSER-THRESYN-PWY` | `data/pathways/l-threonine-biosynthesis.yaml` | `RHEA:13985` (`references[5]`) |
| 11 | `PathBank:SMP0000992` | `data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml` | `RHEA:15761` (`references[5]`), `RHEA:13985` (`references[7]`) |
