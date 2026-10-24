# PathwayMech Cycle 4 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `9eae2f9a55e2ec246a4b729735bf06331f3072a2`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml) (`sha256: 0727d8c8d963a0a81c9f4086077a54f67df49d07748a6b22e6217d3dcd5f1da7`)
- **Structured Review ID**: `20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: bbc3ffaef8a1bc97dab9e7b2c8549d7cbf29d0aa02df0739957be7c8b40b6b99`)
  - [`reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261024T045000Z-cycle4-stage4-frozen-corpus-cohort-review/review.md) (`sha256: 84020d7ec43dc4cdd8d87fe463919f0e6766e2e47f1882d2c5ab78a7077fcd83`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 2f0027676ad1018ccfd9ea2e85a8894d5fbd07ac402c35127890bdb79cc82443`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **273** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `9eae2f9a55e2ec246a4b729735bf06331f3072a2` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 124 | 16 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `PathBank` | 13 | 13 | 13 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **273** | **273** | **257** | **16** | `retain` (all 273) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `9eae2f9a55e2ec246a4b729735bf06331f3072a2`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 273 pathway records against closed LinkML schema, authority snapshots, 843 history records, 22,533 evidence blocks, 33 source records, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8,075 passed, 3 skipped at frozen base. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed. |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 203 pre-existing structured review bundles + new Cycle 4 Stage 4 bundle (`204` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C4-IDENTITY-AND-CAUSAL-GRAPHS-ALL-273` — `supported`)**:
   - All 273 maintained pathway records (including `PathBank:SMP0002042` added in Cycle 4 Stage 1, the 22 records enriched in Cycle 4 Stage 2, and the 44 records enriched in Cycle 4 Stage 3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings (`381` taxon entries across `105` unique `NCBITaxon:*` CURIEs), verified participant/reaction CURIEs, and `1,015` `source_mappings` rows across `197` records exporting to `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping branched-chain amino acid biosynthesis pathways (`PathBank:SMP0002042` `Leucine, Isoleucine and Valine Biosynthesis` in *Escherichia coli* K-12 alongside `MetaCyc:LEUSYN-PWY`, `MetaCyc:ILEUSYN-PWY`, `MetaCyc:VALSYN-PWY`, and `gomodel:YeastPathways_PWY3O-4112`), cysteine biosynthesis pathways (`PathBank:SMP0000993` and `MetaCyc:CYSTSYN-PWY`), and aspartate/threonine/lysine/ectoine pathways (`PathBank:SMP0000992`, `MetaCyc:HOMOSERSYN-PWY`, `MetaCyc:HOMOSER-THRESYN-PWY`, `MetaCyc:DAPLYSINESYN-PWY`, `MetaCyc:P101-PWY`) were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 273 records (`7,763` participants, `1,613` reactions including `714` `RHEA:*` reactions, `14,563` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`22,325` edge/qualifier evidence items; `22,533` total evidence blocks across records, steps, mechanisms, clusters, and edges), 100% of `1,613` reactions explicitly declare `category` (`1,575 molecular_activity`, `36 pathway`, `2 biological_process`) and `reaction_type` (`1,551 catalytic`, `48 transport`, `13 spontaneous`, `1 conformational_change`), and 100% of `RHEA:*` reactions (`714 / 714`) declare explicit `direction` with zero cross-record `RHEA:*` direction conflicts.
   - All `7,758` concrete participant entries across the 273-record corpus explicitly declare `participants[].category` (and the 5 generic `gomodel:*` physical participant instances intentionally omit `category` per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`), and `CHEBI:11851` / `CHEBI:16763` are uniformly typed as `small_molecule`, confirming that Cycle 3 Stage 4/5 findings `F-C3S4-001` and `F-C3S4-002` remain 100% resolved.
2. **Stale Superseded `RHEA:*` Reaction Artifacts in 16 `MetaCyc:*` Records (`ASSESS-C4-METACYC-SUPERSEDED-RHEA-ARTIFACTS-16` — `concern`)**:
   - In `MetaCyc:ARGDEGRAD-PWY` (`data/pathways/l-arginine-degradation-v.yaml`), prior decomposition of the carbamate kinase step from composite `RHEA:10154` (`ATP + NH4(+) + hydrogencarbonate = ADP + carbamoyl phosphate + H(+)`) into `RHEA:30757` (producing `CHEBI:13941` `carbamate`) and spontaneous `RHEA:15650` (producing `CHEBI:16526` `carbon dioxide`) left three stale artifacts: (a) `description` still states `"converts L-arginine to L-ornithine, ammonium, and hydrogencarbonate"`, (b) `participants[14]` still declares an orphan participant `CHEBI:17544` (`hydrogencarbonate`) with zero incident edges in `mechanistic_edges` (the only orphan participant across all `7,763` participant entries in the 273-record corpus), and (c) `references[9]` still declares an unreferenced `RHEA:10154` entry while `references[11..14]` (`RHEA:30757`, `RHEA:15650`, `RHEA:19597`, `RHEA:19513`) carry generic `RHEA:<ID> authority record` placeholder titles (`F-C4S4-001`).
   - Across **15** additional maintained `MetaCyc:*` records, prior RHEA reaction harmonization replaced directional or anomeric `RHEA:*` reaction nodes and edge citations with canonical master/stereospecific `RHEA:*` IDs, leaving **28** unreferenced superseded `RHEA:*` entries in `references[]` alongside **29** replacement `RHEA:*` entries with generic `RHEA:<ID> authority record` placeholder titles (`F-C4S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C4S4-001` and `F-C4S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 4 Stage 5 (`resolve_review_findings`).

### 3.1. `MetaCyc:ARGDEGRAD-PWY` Stale `RHEA:10154` / `CHEBI:17544` (`hydrogencarbonate`) Artifacts (`F-C4S4-001`)

| Pathway ID | File Path | Field Path | Current Stale Value | Required Remediation in Cycle 4 Stage 5 |
| --- | --- | --- | --- | --- |
| `MetaCyc:ARGDEGRAD-PWY` | `data/pathways/l-arginine-degradation-v.yaml` | `description` | `"Bacterial arginine deiminase pathway that converts L-arginine to L-ornithine, ammonium, and hydrogencarbonate while generating ATP via carbamate kinase."` | Update prose to `"converts L-arginine to L-ornithine, ammonium, and carbon dioxide via L-citrulline, carbamoyl phosphate, and carbamate while generating ATP via carbamate kinase."` |
| `MetaCyc:ARGDEGRAD-PWY` | `data/pathways/l-arginine-degradation-v.yaml` | `participants[14]` | `CHEBI:17544` (`hydrogencarbonate`, `category: small_molecule`, 0 incident edges) | Remove orphan `CHEBI:17544` participant entry (`CHEBI:13941` `carbamate` and `CHEBI:16526` `carbon dioxide` are already present and connected). |
| `MetaCyc:ARGDEGRAD-PWY` | `data/pathways/l-arginine-degradation-v.yaml` | `references[9]` | `RHEA:10154` (`Rhea ATP-forming carbamate kinase direction`, 0 citations) | Remove superseded unreferenced `RHEA:10154` entry. |
| `MetaCyc:ARGDEGRAD-PWY` | `data/pathways/l-arginine-degradation-v.yaml` | `references[11..14].title` | `RHEA:30757 authority record`, `RHEA:15650 authority record`, `RHEA:19597 authority record`, `RHEA:19513 authority record` | Replace generic placeholder titles with descriptive Rhea reaction titles. |

### 3.2. Fifteen `MetaCyc:*` Records with Unreferenced Superseded `RHEA:*` References and Generic Replacement Titles (`F-C4S4-002`)

| # | Pathway ID | File Path | Unreferenced Superseded `RHEA:*` in `references[]` (28 total) | Replacement `RHEA:*` with Generic `RHEA:<ID> authority record` Title (29 total) |
| ---: | --- | --- | --- | --- |
| 1 | `MetaCyc:DARABCAT-PWY` | `data/pathways/d-arabinose-degradation-i.yaml` | `RHEA:13852` (`references[2]`: Rhea bidirectional D-arabinose isomerase reaction) | `RHEA:13850` (`references[5]`) |
| 2 | `MetaCyc:GALACTUROCAT-PWY` | `data/pathways/d-galacturonate-degradation-i.yaml` | `RHEA:27705` (`references[2]`: Rhea bidirectional D-galacturonate isomerase reaction), `RHEA:17816` (`references[4]`: Rhea bidirectional tagaturonate reductase reaction) | `RHEA:27703` (`references[11]`), `RHEA:17815` (`references[12]`) |
| 3 | `MetaCyc:GLUCARDEG-PWY` | `data/pathways/d-glucarate-degradation-i.yaml` | `RHEA:27726` (`references[3]`: Rhea 5-dehydro-4-deoxy-D-glucarate aldolase reaction), `RHEA:27729` (`references[4]`: Rhea bidirectional 5-dehydro-4-deoxy-D-glucarate aldolase reaction) | `RHEA:27727` (`references[11]`) |
| 4 | `MetaCyc:XYLCAT-PWY` | `data/pathways/d-xylose-degradation-i.yaml` | `RHEA:22819` (`references[2]`: Rhea bidirectional xylose isomerase reaction) | `RHEA:22817` (`references[5]`) |
| 5 | `MetaCyc:GLYCEROLMETAB-PWY` | `data/pathways/glycerol-degradation-v.yaml` | `RHEA:13772` (`references[2]`: Rhea bidirectional glycerol dehydrogenase reaction) | `RHEA:13770` (`references[5]`) |
| 6 | `MetaCyc:PWY-6124` | `data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml` | `RHEA:10795` (`references[2]`: Rhea CAIR/AIR carboxylase bidirectional reaction) | `RHEA:10794` (`references[11]`) |
| 7 | `MetaCyc:ARABCAT-PWY` | `data/pathways/l-arabinose-degradation-i.yaml` | `RHEA:14824` (`references[2]`: Rhea bidirectional L-arabinose isomerase reaction), `RHEA:22371` (`references[6]`: Rhea bidirectional L-ribulose-5-phosphate 4-epimerase reaction) | `RHEA:14822` (`references[7]`), `RHEA:22369` (`references[8]`) |
| 8 | `MetaCyc:FUCCAT-PWY` | `data/pathways/l-fucose-degradation-i.yaml` | `RHEA:25583` (`references[2]`: Rhea bidirectional L-fucose mutarotase reaction), `RHEA:17236` (`references[4]`: Rhea bidirectional L-fucose isomerase reaction) | `RHEA:25582` (`references[9]`), `RHEA:17234` (`references[10]`) |
| 9 | `MetaCyc:ILEUSYN-PWY` | `data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml` | `RHEA:22108` (`references[1]`: Rhea L-threonine ammonia-lyase reaction), `RHEA:22109` (`references[2]`: Rhea L-threonine-to-2-oxobutanoate direction) | `RHEA:40676` (`references[16]`), `RHEA:39968` (`references[17]`), `RHEA:39976` (`references[18]`) |
| 10 | `MetaCyc:LEUSYN-PWY` | `data/pathways/l-leucine-biosynthesis.yaml` | `RHEA:32287` (`references[3]`: Rhea 3-isopropylmalate dehydratase reaction), `RHEA:32289` (`references[4]`: Rhea biosynthetic 3-isopropylmalate dehydratase direction), `RHEA:32271` (`references[5]`: Rhea 3-isopropylmalate dehydrogenase reaction), `RHEA:32272` (`references[6]`: Rhea 4-methyl-2-oxopentanoate-forming direction) | `RHEA:16295` (`references[13]`), `RHEA:10678` (`references[14]`), `RHEA:10893` (`references[15]`), `RHEA:25079` (`references[16]`) |
| 11 | `MetaCyc:HOMOSER-METSYN-PWY` | `data/pathways/l-methionine-biosynthesis-i.yaml` | `RHEA:13965` (`references[5]`: Rhea cystathionine beta-lyase reaction), `RHEA:13966` (`references[6]`: Rhea L-homocysteine-forming cystathionine beta-lyase direction) | `RHEA:43021` (`references[17]`), `RHEA:40668` (`references[18]`), `RHEA:40672` (`references[19]`) |
| 12 | `MetaCyc:RHAMCAT-PWY` | `data/pathways/l-rhamnose-degradation-i.yaml` | `RHEA:25587` (`references[2]`: Rhea bidirectional L-rhamnose mutarotase reaction), `RHEA:23163` (`references[4]`: Rhea bidirectional L-rhamnose isomerase reaction), `RHEA:19692` (`references[8]`: Rhea bidirectional rhamnulose-1-phosphate aldolase reaction) | `RHEA:25585` (`references[10]`), `RHEA:23161` (`references[11]`), `RHEA:19690` (`references[12]`) |
| 13 | `MetaCyc:TRPSYN-PWY` | `data/pathways/l-tryptophan-biosynthesis.yaml` | `RHEA:10532` (`references[9]`: Rhea tryptophan synthase reaction), `RHEA:10533` (`references[10]`: Rhea L-tryptophan-forming tryptophan synthase direction) | `RHEA:14082` (`references[16]`), `RHEA:26435` (`references[17]`) |
| 14 | `MetaCyc:GLUAMCAT-PWY` | `data/pathways/n-acetylglucosamine-degradation-i.yaml` | `RHEA:12175` (`references[4]`: Rhea bidirectional glucosamine-6-phosphate deaminase reaction) | `RHEA:12173` (`references[5]`) |
| 15 | `MetaCyc:NONOXIPENT-PWY` | `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml` | `RHEA:14660` (`references[2]`: Rhea bidirectional ribose-5-phosphate isomerase reaction), `RHEA:13680` (`references[4]`: Rhea bidirectional ribulose-phosphate 3-epimerase reaction), `RHEA:10511` (`references[6]`: Rhea bidirectional transketolase sedoheptulose-7-phosphate reaction), `RHEA:17056` (`references[8]`: Rhea bidirectional transaldolase reaction), `RHEA:27629` (`references[10]`: Rhea bidirectional transketolase fructose-6-phosphate reaction) | `RHEA:14659` (`references[11]`), `RHEA:13678` (`references[12]`), `RHEA:10510` (`references[13]`), `RHEA:17054` (`references[14]`), `RHEA:27627` (`references[15]`) |
