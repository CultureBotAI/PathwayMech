# PathwayMech Cycle 1 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `556074d91f600aa9e5ca97e0b4baef6d99513930`
- **Structured Review ID**: `20261022T013600Z-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: a7adee7427cfe9a6d42cf1b80a50d8a0843a7a5a6c7a530fb7b19ce8734c815f`)
  - [`reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261022T013600Z-stage4-frozen-corpus-cohort-review/review.md) (`sha256: ea0646892d4c67a576e1352656318c2dcce8dc284588c8073130cde616191a55`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 961da5d09524e8c281634fe7baa6b75d3b45a25299cd6e2f0e802aa4102f3da8`)
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
   - Across all 270 records (`2,650` participants, `3,281` reactions, `17,676` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`22,085` evidence blocks total), 100% of `RHEA:*` reactions declare explicit `direction`, and zero cross-record `RHEA:*` direction conflicts exist.
3. **Within-Record Reaction Category Typing (`ASSESS-REACTION-CATEGORY-CONCERN-12` — `concern`)**:
   - Twelve maintained `MetaCyc:*` records mix explicit `category` declarations (`molecular_activity` or `pathway`) on a subset of their `reactions[]` entries while omitting `category: molecular_activity` on 33 sibling catalytic reaction entries (`30 RHEA:*`, `2 MetaCyc:RXN-*`, `1 BiGG:ACMANAptspp`).
   - In `MetaCyc:GLCMANNANAUT-PWY` (`data/pathways/amino-sugar-superpathway.yaml`), `reactions[13]` (`BiGG:ACMANAptspp`) omits `category: molecular_activity` and consequently falls back to `biolink:NamedThing` (with empty `source_category`) in `pages/downloads/nodes.tsv`.
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-STAGE4-001` and `F-STAGE4-002`) are preserved as `open` (`carry_forward_ids`) for Stage 5 (`resolve_review_findings`).
