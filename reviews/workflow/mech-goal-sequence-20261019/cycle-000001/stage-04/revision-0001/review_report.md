# PathwayMech Cycle 1 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `556074d91f600aa9e5ca97e0b4baef6d99513930`
- **Structured Review ID**: `20261022T013600Z-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: ad033e8724d2b065a2a132fb15c571f5b6961bde6f56f298d3731735ea2d7ec3`)
  - [`reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.md) (`sha256: 8181c68a112b4c0bde8128b972923612f00c87bc0f703296dc2f5e09699ee295`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: c940c56636a5a8ee0b15465511c8127c1a52151f4f9d551cb199bda54bfd1233`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **270** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `556074d91f600aa9e5ca97e0b4baef6d99513930` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 128 | 12 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `PathBank` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **270** | **270** | **258** | **12** | `retain` (all 270) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `556074d91f600aa9e5ca97e0b4baef6d99513930`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 270 pathway records against closed LinkML schema, authority snapshots, 537 history records, 22,085 evidence blocks, 33 source records, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8,045 passed, 3 skipped. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed. |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 197 pre-existing structured review bundles + new Stage 4 bundle (`198` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity & Grounding (`ASSESS-IDENTITY-GROUNDING-ALL-270` — `supported`)**:
   - All 270 maintained pathway records carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings, and verified participant/reaction CURIEs (`CHEBI`, `UniProtKB`, `ComplexPortal`, `GO`, `RHEA`, `MetaCyc`, `BiGG`, `EcoCyc`, `Reactome`, `WikiPathways`, `MIBiG`, `KEGG`).
   - Overlapping purine salvage pathways (`MetaCyc:P121-PWY`, `PathBank:SMP0002081`, `PathBank:SMP0002083`, `MetaCyc:PWY-6609`) were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped topologies and transport/salvage boundaries (`action: retain`).
2. **Causal Graph & Evidence (`ASSESS-CAUSAL-GRAPH-EVIDENCE-ALL-270` — `supported`)**:
   - Across all 270 records (`7,652` participants, `1,591` reactions including `693` `RHEA:*` reactions, `14,322` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`20,959` edge-level evidence items; `22,085` total evidence blocks across records, steps, and edges), 100% of `RHEA:*` reactions (`693 / 693`) declare explicit `direction`, and zero cross-record `RHEA:*` direction conflicts exist.
3. **Within-Record Reaction Category Typing (`ASSESS-REACTION-CATEGORY-CONCERN-12` — `concern`)**:
   - Twelve maintained `MetaCyc:*` records mix explicit `category` declarations (`molecular_activity` or `pathway`) on a subset of their `reactions[]` entries while omitting `category: molecular_activity` on 33 sibling catalytic reaction entries (`30 RHEA:*`, `2 MetaCyc:RXN-*`, `1 BiGG:ACMANAptspp`).
   - In `MetaCyc:GLCMANNANAUT-PWY` (`data/pathways/amino-sugar-superpathway.yaml`), `reactions[13]` (`BiGG:ACMANAptspp`) omits `category: molecular_activity` and consequently falls back to `biolink:NamedThing` (with empty `source_category`) in `pages/downloads/nodes.tsv`.
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-STAGE4-001` and `F-STAGE4-002`) are preserved as `open` (`carry_forward_ids`) for Stage 5 (`resolve_review_findings`).

| # | Pathway ID | File Path | Omitted `category: molecular_activity` Reaction Entries | Explicitly Typed Sibling `reactions[]` Entries |
| ---: | --- | --- | --- | --- |
| 1 | `MetaCyc:SALVADEHYPOX-PWY` | `data/pathways/adenosine-nucleotides-degradation-ii.yaml` | 5 (`reactions[1..5]`: `RHEA:29376`, `RHEA:24409`, `RHEA:27647`, `RHEA:24671`, `RHEA:16670`) | `reactions[0]` (`MetaCyc:PWY-5691`, `category: pathway`) |
| 2 | `MetaCyc:PWY-7971` | `data/pathways/adenosylcobinamide-gdp-salvage-i.yaml` | 1 (`reactions[1]`: `RHEA:57693`) | `reactions[0,2..4]` (`category: molecular_activity`) |
| 3 | `MetaCyc:PWY0-41` | `data/pathways/allantoin-degradation-iv-anaerobic.yaml` | 1 (`reactions[6]`: `RHEA:15650`) | `reactions[0..5]` (`category: molecular_activity`) |
| 4 | `MetaCyc:GLCMANNANAUT-PWY` | `data/pathways/amino-sugar-superpathway.yaml` | 11 (`reactions[3..13]`: `RHEA:67737`, `RHEA:67741`, `RHEA:23297`, `RHEA:25254`, `RHEA:25259`, `RHEA:22937`, `RHEA:12173`, `RHEA:28989`, `RHEA:49241`, `RHEA:23881`, `BiGG:ACMANAptspp`) | `reactions[0..2]` (`MetaCyc:PWY0-1324`, `MetaCyc:GLUAMCAT-PWY`, `MetaCyc:GLYCOLYSIS`, `category: pathway`) |
| 5 | `MetaCyc:PWY-2503` | `data/pathways/benzoate-degradation-i-aerobic.yaml` | 2 (`reactions[5..6]`: `RHEA:12634`, `RHEA:11561`) | `reactions[0..4]` (`category: molecular_activity`) |
| 6 | `MetaCyc:PWY-1361` | `data/pathways/benzoyl-coa-degradation-i-aerobic.yaml` | 6 (`reactions[0..2,4..6]`: `RHEA:48313`, `RHEA:48309`, `RHEA:25392`, `RHEA:76649`, `RHEA:34852`, `RHEA:19483`) | `reactions[3]` (`MetaCyc:RXN-2424`, `category: molecular_activity`) |
| 7 | `MetaCyc:CYANCAT-PWY` | `data/pathways/cyanate-degradation.yaml` | 1 (`reactions[1]`: `RHEA:15650`) | `reactions[0,2]` (`category: molecular_activity`) |
| 8 | `MetaCyc:PWY-7255` | `data/pathways/ergothioneine-biosynthesis-i.yaml` | 2 (`reactions[5..6]`: `MetaCyc:RXN-18089`, `MetaCyc:RXN-15804`) | `reactions[0..4]` (`category: molecular_activity`) |
| 9 | `MetaCyc:PWY-5744` | `data/pathways/glyoxylate-assimilation.yaml` | 1 (`reactions[0]`: `RHEA:10750`) | `reactions[1..12]` (`category: molecular_activity`) |
| 10 | `MetaCyc:PWY-5789` | `data/pathways/hydroxypropionate-hydroxybutyrate-cycle.yaml` | 1 (`reactions[0]`: `RHEA:10750`) | `reactions[1..16]` (`category: molecular_activity`) |
| 11 | `MetaCyc:PWY-6993` | `data/pathways/nicotine-degradation-ii.yaml` | 1 (`reactions[1]`: `RHEA:75416`) | `reactions[0,2..10]` (`category: molecular_activity`) |
| 12 | `MetaCyc:PWY0-1471` | `data/pathways/uracil-degradation-iii.yaml` | 1 (`reactions[3]`: `RHEA:15650`) | `reactions[0..2,4..5]` (`category: molecular_activity`) |
