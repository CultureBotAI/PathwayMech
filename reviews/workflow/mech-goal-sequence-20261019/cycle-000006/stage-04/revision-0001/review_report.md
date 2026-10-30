# PathwayMech Cycle 6 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `bac5a3bcd954ece28631747e28cfb3da8ba4df91`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml) (`sha256: a5ad35ab3e54ad3f562ba0612165b39204b6493518ec41ba28d001380f51630c`)
- **Structured Review ID**: `20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: 90e3a74d2a6d543506129fbe8bf95d72e78abd28483852735ae3b32a220b2ac3`)
  - [`reviews/structured/20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review/review.md) (`sha256: 6f13f5b7eb8688d352fa2d7914cb9e29242604e3442b46abc72d576531d67a1c`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 0633b9b071b069c60d276a22b144723841f563118dfb4ee8f1cc9b85267584eb`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **275** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `bac5a3bcd954ece28631747e28cfb3da8ba4df91` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 135 | 5 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `PathBank` | 15 | 15 | 15 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 11 | 1 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **275** | **275** | **269** | **6** | `retain` (all 275) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `bac5a3bcd954ece28631747e28cfb3da8ba4df91`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 275 pathway records against closed LinkML schema, authority snapshots, 909 history records, 22,750 evidence blocks, 33 source records, 6 documentation files, deep-research report contract, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8084 passed, 3 skipped at frozen base. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed! |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 207 pre-existing structured review bundles + new Cycle 6 Stage 4 bundle (`208` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C6-IDENTITY-AND-CAUSAL-GRAPHS-ALL-275` — `supported`)**:
   - All 275 maintained pathway records (including `PathBank:SMP0000991` added in Cycle 6 Stage 1, the 8 MetaCyc/gomodel/GO records enriched with 387 stoichiometric coefficients, 43 ECO codes, and 77 assay taxa in Cycle 6 Stage 2, and the 6 MetaCyc records enriched across 34 `UniProtKB:*` edges and 16 reference titles in Cycle 6 Stage 3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings (`385` taxon entries across `105` unique `NCBITaxon:*` CURIEs), verified participant/reaction CURIEs, and `1,057` `source_mappings` rows across `216` records exporting to `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping non-mevalonate isoprenoid biosynthesis pathways (`PathBank:SMP0000991` `Secondary Metabolites: Isoprenoid Biosynthesis (Nonmevalonate Pathway)` in *Escherichia coli* K-12 alongside `MetaCyc:NONMEVIPP-PWY` `methylerythritol phosphate pathway I`) as well as thiazole/thiamine, purine, branched-chain amino acid, cysteine, and aspartate/threonine pathways were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 275 records (`7,830` participants including `968` `UniProtKB:*` protein participants across `155` records, `1,625` reactions including `726` `RHEA:*` reactions, `14,691` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`22,542` edge/qualifier evidence items; `22,750` total evidence blocks across records, steps, mechanisms, clusters, and edges), 100% of `1,625` reactions explicitly declare `category` (`1,587 molecular_activity`, `36 pathway`, `2 biological_process`) and `reaction_type` (`1,562 catalytic`, `49 transport`, `13 spontaneous`, `1 conformational_change`), and 100% of `RHEA:*` reactions (`726 / 726`) declare explicit `direction` with zero cross-record `RHEA:*` direction conflicts.
   - All `7,825` concrete participant entries across the 275-record corpus explicitly declare `participants[].category` (and the 5 generic `gomodel:*` physical participant instances intentionally omit `category` per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`), 100% of participants (`7,830 / 7,830`) are connected by at least one `mechanistic_edges` entry (0 orphan participants), 0 reflexive self-loops (`subject == object`) exist across all `14,691` `mechanistic_edges`, and 0 non-UniProt generic `<CURIE> authority record` reference titles remain across all `7,082` `references[]` entries, confirming that Cycle 5 Stage 4/5 findings `F-C5S4-001` and `F-C5S4-002` remain 100% resolved.
2. **Ferredoxin Participant Category Conflict in `WikiPathways:WP5019` and 23 Bare CURIE Reference Titles Across 5 MetaCyc Records (`ASSESS-C6-FERREDOXIN-CATEGORY-AND-BARE-CURIE-TITLES-6` — `concern`)**:
   - In `WikiPathways:WP5019` (`data/pathways/acetogenesis.yaml`), `participants[28]` (`id: CHEBI:17908`, `label: oxidized ferredoxin`, lines 97–99) and `participants[29]` (`id: CHEBI:17513`, `label: reduced ferredoxin`, lines 100–102) are typed as `category: small_molecule` instead of `category: protein` (`F-C6S4-001`). In `data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml` (`MetaCyc:PWY-8132`, lines 39–41 and `participants[12,14]` at lines 232–238), `CHEBI:17908` and `CHEBI:17513` are documented and typed as iron-sulfur protein redox classes (`category: protein`), consistent with all other protein redox carriers in the corpus (`CHEBI:15033`, `CHEBI:15967`, `CHEBI:18191`, `CHEBI:18097`, `CHEBI:16518`, `MetaCyc:Oxidized-ferredoxins`, `MetaCyc:Reduced-ferredoxins`). Because `src/pathwaymech/kgx.py` maps `small_molecule` to `biolink:SmallMolecule` and `protein` to `biolink:Protein`, this mistyping causes `pages/downloads/nodes.tsv` to export both `CHEBI:17908` and `CHEBI:17513` with conflicting disjoint Biolink ontological categories `biolink:Protein|biolink:SmallMolecule`—the only two nodes in the 6,053-node KGX graph with a `Protein|SmallMolecule` class conflict.
   - Across **5** maintained `MetaCyc:*` pathway records, **23** structured-database `references[]` entries (`11` `MetaCyc:*`, `7` `EcoCyc:*`, `3` `Entrez:*`, and `2` `UniProtKB:*`) retain a bare CURIE string identical to `id` (`title == id`) as their `title`, even though descriptive labels are already recorded on the corresponding local `reactions[]`, `participants[]`, pathway `label`, or quoted authority fields (`F-C6S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C6S4-001` and `F-C6S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 6 Stage 5 (`resolve_review_findings`).

### 3.1. `WikiPathways:WP5019` (`acetogenesis.yaml`) Ferredoxin Participant Category Mismatch (`F-C6S4-001`)

| Pathway ID | File Path | Field Path | Current Value | Required Remediation in Cycle 6 Stage 5 |
| --- | --- | --- | --- | --- |
| `WikiPathways:WP5019` | `data/pathways/acetogenesis.yaml` | `participants[28].category` (`CHEBI:17908`, `oxidized ferredoxin`) & `participants[29].category` (`CHEBI:17513`, `reduced ferredoxin`) | `small_molecule` (exporting `biolink:Protein|biolink:SmallMolecule` in `pages/downloads/nodes.tsv`) | Change both `participants[28].category` and `participants[29].category` to `protein`, record curation history under `history/records/acetogenesis/`, and regenerate `pages/downloads/nodes.tsv`. |

### 3.2. Five MetaCyc Records with 23 Bare CURIE `title == id` Reference Titles (`F-C6S4-002`)

| # | Pathway ID | File Path | `references[]` Entries with Bare CURIE `title == id` (23 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:PWY-8130` | `data/pathways/5-prime-deoxyadenosine-degradation-i.yaml` | `MetaCyc:RXN-14304` (`references[1]`), `MetaCyc:RXN-21315` (`references[2]`), `MetaCyc:RXN-21316` (`references[3]`) |
| 2 | `MetaCyc:SALVADEHYPOX-PWY` | `data/pathways/adenosine-nucleotides-degradation-ii.yaml` | `EcoCyc:AMP-DEPHOSPHORYLATION-RXN` (`references[27]`), `UniProtKB:P23841` (`references[31]`), `EcoCyc:CPLX0-7681` (`references[32]`), `EcoCyc:EG11146-MONOMER` (`references[33]`), `EcoCyc:TU301` (`references[34]`), `EcoCyc:TU0-45226` (`references[35]`), `EcoCyc:G85` (`references[36]`), `Entrez:946878` (`references[37]`), `Entrez:945283` (`references[38]`), `Entrez:945654` (`references[39]`) |
| 3 | `MetaCyc:GLCMANNANAUT-PWY` | `data/pathways/amino-sugar-superpathway.yaml` | `MetaCyc:GLCMANNANAUT-PWY` (`references[18]`) |
| 4 | `MetaCyc:GALLATE-DEGRADATION-II-PWY` | `data/pathways/gallate-degradation-i.yaml` | `MetaCyc:CPLX-7916` (`references[42]`), `UniProtKB:P22636` (`references[43]`) |
| 5 | `MetaCyc:PWY-8132` | `data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml` | `MetaCyc:5.3.1.23-RXN` (`references[0]`), `MetaCyc:O-ACETYLHOMOSERINE-THIOL-LYASE-RXN` (`references[1]`), `MetaCyc:RXN-21318` (`references[3]`), `MetaCyc:RXN-21319` (`references[4]`), `MetaCyc:RXN-21320` (`references[5]`), `MetaCyc:CPLX-8242` (`references[33]`), `MetaCyc:MONOMER-21153` (`references[38]`) |
