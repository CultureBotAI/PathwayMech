# PathwayMech Cycle 7 Stage 4 Record & Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `e210b77543f075397dd4ba90f003b9a95331bebd`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml) (`sha256: b262473fca4a270301e0fdb4d3498ca984811d29b00644395d5d7767dc850085`)
- **Structured Review ID**: `20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review`
- **Authoritative Structured Bundle**:
  - [`reviews/structured/20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review/review.yaml`](../../../../../reviews/structured/20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review/review.yaml) (`sha256: 53ea8869dd4122968268bf11cc30d189f016f2d092b5e3d238b7946902507b65`)
  - [`reviews/structured/20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review/review.md`](../../../../../reviews/structured/20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review/review.md) (`sha256: af33be0f3d1ee0d3b525b2026ea7ace290eefc073b7c91012d3c6f5846280349`)
- **Coverage Ledger**: [`coverage.json`](coverage.json) (`sha256: 52f62e1908e872efc0983e1abf2f77fecac2883852ef2d301ac1d0646806b28d`)
- **Completion / Verdict**: `completed` / `pass_with_limitations` (`native_verdict: coherent`)

## 1. Frozen Inventory Scope & Coverage

All **276** maintained pathway YAML records matching `data/pathways/*.yaml` at frozen commit `e210b77543f075397dd4ba90f003b9a95331bebd` were inspected and assessed across all 8 identifier namespaces:

| Prefix Namespace | Maintained Records | Reviewed | Supported (Clean) | With Minor Open Findings | Boundary Decision |
| --- | ---: | ---: | ---: | ---: | --- |
| `MetaCyc` | 140 | 140 | 134 | 6 | `retain` |
| `gomodel` | 86 | 86 | 86 | 0 | `retain` |
| `PathBank` | 16 | 16 | 16 | 0 | `retain` |
| `WikiPathways` | 12 | 12 | 12 | 0 | `retain` |
| `GO` | 10 | 10 | 10 | 0 | `retain` |
| `Reactome` | 6 | 6 | 6 | 0 | `retain` |
| `KEGG` | 3 | 3 | 3 | 0 | `retain` |
| `MIBiG` | 3 | 3 | 3 | 0 | `retain` |
| **Total** | **276** | **276** | **270** | **6** | `retain` (all 276) |

### Exclusions
- `research/pathway_additions/` (`GO:0033468` and `MetaCyc:PWY-5875`): withheld research draft pathways not promoted to `data/pathways/*.yaml`.
- `reports/yaml_record_review/` and `reports/yaml_category_review/`: historical prose reports retained without migration per `docs/record-review-profile.md`.

## 2. Read-Only Validation Gates Executed at `e210b77543f075397dd4ba90f003b9a95331bebd`

| Gate ID | Command | Exit Code | Result Summary |
| --- | --- | ---: | --- |
| `validate` | `.venv/bin/pathwaymech-run-qc` | `0` | Validated 276 pathway records against closed LinkML schema, authority snapshots, 932 history records, 22,794 evidence blocks, 33 source records, 6 documentation files, deep-research report contract, and `pages/` synchrony. |
| `test` | `.venv/bin/pytest -q` | `0` | 8091 passed, 3 skipped at frozen base. |
| `lint` | `.venv/bin/ruff check --no-cache .` | `0` | All checks passed! |
| `diff-check` | `git diff --check` | `0` | Clean worktree diff check. |
| `review-check` | `.venv/bin/python scripts/record_review.py check` | `0` | All 209 pre-existing structured review bundles + new Cycle 7 Stage 4 bundle (`210` total) valid. |

## 3. Scientific & Structural Assessment Summary

1. **Identity, Grounding, Causal Graph & Prior Finding Verification (`ASSESS-C7-IDENTITY-AND-CAUSAL-GRAPHS-ALL-276` — `supported`)**:
   - All 276 maintained pathway records (including `PathBank:SMP0002070` added in Cycle 7 Stage 1, the 8 MetaCyc/gomodel/GO records enriched with 328 stoichiometric coefficients, 77 ECO codes, and 77 assay taxa in Cycle 7 Stage 2, and the 6 MetaCyc records enriched across 35 `UniProtKB:*` edges and 18 reference titles in Cycle 7 Stage 3) carry authority-verified primary pathway CURIEs, `NCBITaxon:*` organism groundings (`387` taxon entries across `105` unique `NCBITaxon:*` CURIEs), verified participant/reaction CURIEs, and `1,060` `source_mappings` rows across `217` records exporting to `output/sssom/source_mappings.sssom.tsv`.
   - Overlapping succinate-to-propanoate decarboxylation pathways (`PathBank:SMP0002070` `Conversion of Succinate to Propanoate` in *Escherichia coli* K-12 alongside `MetaCyc:PWY0-43` `conversion of succinate to propanoate`) as well as non-mevalonate isoprenoid, thiazole/thiamine, purine, branched-chain amino acid, cysteine, and aspartate/threonine pathways were audited against `docs/HARMONIZATION.md` and confirmed to represent distinct authority-scoped pathway boundaries and step topologies (`action: retain`).
   - Across all 276 records (`7,843` participants including `971` `UniProtKB:*` protein participants across `156` records, `1,628` reactions including `729` `RHEA:*` reactions, `14,713` `mechanistic_edges`), 100% of edges carry valid structured `evidence` items (`21,668` on `mechanistic_edges` + `918` on `endpoint_qualifiers` = `22,586` edge/qualifier evidence items; `22,794` total evidence blocks including `208` `reaction_mechanisms` evidence items), 100% of `1,628` reactions explicitly declare `category` (`1,590 molecular_activity`, `36 pathway`, `2 biological_process`), and 100% of `RHEA:*` reactions (`729 / 729`) declare explicit `direction` with zero cross-record `RHEA:*` direction conflicts.
   - All `7,838` concrete participant entries across the 276-record corpus explicitly declare `participants[].category` (and the 5 generic `gomodel:*` physical participant instances intentionally omit `category` per `src/pathwaymech/gocam_native.py:30-32` and `tests/test_kgx_export.py:142-159`), 100% of participants (`7,843 / 7,843`) are connected by at least one `mechanistic_edges` entry (0 orphan participants), 0 reflexive self-loops (`subject == object`) exist across all `14,713` `mechanistic_edges`, 0 `biolink:Protein|biolink:SmallMolecule` category conflicts exist across all `5,456` nodes in `pages/downloads/nodes.tsv`, and 0 non-literature bare CURIE reference titles remain across all `7,094` `references[]` entries, confirming that Cycle 6 Stage 4/5 findings `F-C6S4-001` and `F-C6S4-002` remain 100% resolved.
2. **16 Bare CURIE Literature Reference Titles Across 3 MetaCyc Records and 52 Concrete Small-Molecule Participants Typed as `chemical_entity` Across 3 MetaCyc Records (`ASSESS-C7-LITERATURE-TITLES-AND-SMALL-MOLECULE-CATEGORIES-6` — `concern`)**:
   - Across **3** maintained `MetaCyc:*` pathway records (`MetaCyc:SALVADEHYPOX-PWY`, `MetaCyc:GLCMANNANAUT-PWY`, and `MetaCyc:GALLATE-DEGRADATION-II-PWY`), the last **16** bare CURIE `references[]` entries in the 276-record corpus (`15` `PMID:*` and `1` `DOI:*`) still repeat their identifier string as `title` (`title == id`) instead of storing the peer-reviewed article title (`F-C7S4-001`).
   - Across **3** maintained `MetaCyc:*` pathway records (`MetaCyc:GALLATE-DEGRADATION-I-PWY` `data/pathways/gallate-degradation-ii.yaml`, `MetaCyc:PWY-8178` `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`, and `MetaCyc:THIOREDOX-PWY` `data/pathways/thioredoxin-pathway.yaml`), **52** concrete small-molecule metabolite, salt, and effector participants (`32` in `gallate-degradation-ii.yaml`, `16` in `pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`, and `4` in `thioredoxin-pathway.yaml`, excluding the 2 generic electron-carrier classes `MetaCyc:Acceptor` and `MetaCyc:Donor-H2` in `thioredoxin-pathway.yaml`) are typed as generic `category: chemical_entity` instead of `category: small_molecule`, causing **17** pure `chemical_entity` vs `small_molecule` cross-record `biolink:ChemicalEntity|biolink:SmallMolecule` category merges in `pages/downloads/nodes.tsv` (`F-C7S4-002`).
   - Per Stage 4 policy, no pathway YAML records were edited during this review stage; both findings (`F-C7S4-001` and `F-C7S4-002`) are preserved as `open` (`carry_forward_ids`) for Cycle 7 Stage 5 (`record_remediation`).

### 3.1. Three MetaCyc Records with 16 Literature `references[]` Entries Having Bare CURIE `title == id` (`F-C7S4-001`)

| # | Pathway ID | File Path | Literature `references[]` Entries with Bare CURIE `title == id` (16 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:SALVADEHYPOX-PWY` | `data/pathways/adenosine-nucleotides-degradation-ii.yaml` | `PMID:7559336` (`references[40]`), `PMID:10986234` (`references[41]`), `PMID:19542235` (`references[42]`), `PMID:41070194` (`references[43]`), `PMID:31978345` (`references[44]`), `PMID:40632566` (`references[45]`) |
| 2 | `MetaCyc:GLCMANNANAUT-PWY` | `data/pathways/amino-sugar-superpathway.yaml` | `PMID:33790291` (`references[52]`), `PMID:19700525` (`references[53]`), `PMID:28634232` (`references[56]`) |
| 3 | `MetaCyc:GALLATE-DEGRADATION-II-PWY` | `data/pathways/gallate-degradation-i.yaml` | `PMID:23977959` (`references[41]`), `PMID:21219457` (`references[44]`), `PMID:16030198` (`references[45]`), `PMID:30346405` (`references[46]`), `DOI:10.1016/j.procbio.2021.01.019` (`references[47]`), `PMID:26867578` (`references[48]`), `PMID:24657997` (`references[49]`) |

### 3.2. Three MetaCyc Records with 52 Concrete Small-Molecule Participants Typed as `category: chemical_entity` (`F-C7S4-002`)

| # | Pathway ID | File Path | Concrete Small-Molecule `participants[]` Entries Typed as `chemical_entity` (52 total) |
| ---: | --- | --- | --- |
| 1 | `MetaCyc:GALLATE-DEGRADATION-I-PWY` | `data/pathways/gallate-degradation-ii.yaml` | 32 entries (`participants[51..62, 65..74, 78..81, 83..87, 89]`): `CHEBI:15356`, `CHEBI:15422`, `CHEBI:16526`, `CHEBI:16761`, `CHEBI:16763`, `CHEBI:16810`, `CHEBI:16856`, `CHEBI:16947`, `CHEBI:173437`, `CHEBI:17742`, `CHEBI:18320`, `CHEBI:22629`, `CHEBI:29888`, `CHEBI:30808`, `CHEBI:31823`, `CHEBI:32139`, `CHEBI:32588`, `CHEBI:3312`, `CHEBI:34887`, `CHEBI:35780`, `CHEBI:36655`, `CHEBI:44976`, `CHEBI:53351`, `CHEBI:57499`, `CHEBI:58222`, `CHEBI:58276`, `CHEBI:62843`, `CHEBI:63317`, `CHEBI:747199`, `CHEBI:86228`, `CHEBI:9532`, `PubChem:6098323` |
| 2 | `MetaCyc:PWY-8178` | `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml` | 16 entries (`participants[5..16, 32..35]`): `MetaCyc:D-SEDOHEPTULOSE-1-7-P2`, `MetaCyc:D-SEDOHEPTULOSE-7-P`, `MetaCyc:DIHYDROXY-ACETONE-PHOSPHATE`, `MetaCyc:ERYTHROSE-4P`, `MetaCyc:FRUCTOSE-6P`, `MetaCyc:GAP`, `MetaCyc:PPI`, `MetaCyc:PROTON`, `MetaCyc:Pi`, `MetaCyc:RIBOSE-5P`, `MetaCyc:RIBULOSE-5P`, `MetaCyc:XYLULOSE-5-PHOSPHATE`, `CHEBI:28938`, `CHEBI:29103`, `CHEBI:29105`, `CHEBI:30616` |
| 3 | `MetaCyc:THIOREDOX-PWY` | `data/pathways/thioredoxin-pathway.yaml` | 4 entries (`participants[32..35]`): `CHEBI:18407` (`hydrogen cyanide`), `CHEBI:35456` (`cadmium dichloride`), `CHEBI:20435` (`p-mercuribenzoate`), `CHEBI:29242` (`arsenite(1-)`) |
