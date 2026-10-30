# PathwayMech Cycle 7 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `e210b77543f075397dd4ba90f003b9a95331bebd`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml) (`sha256: b262473fca4a270301e0fdb4d3498ca984811d29b00644395d5d7767dc850085`)
- **Structured Review ID**: `20261030T205500Z-cycle7-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C7S4-001`, `F-C7S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 7 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C7S4-001` | `bare-curie-literature-reference-titles-3-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 3 `MetaCyc:*` records (`MetaCyc:SALVADEHYPOX-PWY`, `MetaCyc:GLCMANNANAUT-PWY`, `MetaCyc:GALLATE-DEGRADATION-II-PWY`; 16 literature `references[]` entries) | `A-C7S4-001`: Replace all 16 bare CURIE `title == id` placeholders (`15` `PMID:*` and `1` `DOI:*`) with verified peer-reviewed publication titles across the 3 affected MetaCyc records, record curation history, and refresh `pages/`. |
| `F-C7S4-002` | `concrete-small-molecule-participants-typed-as-chemical-entity-3-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 3 `MetaCyc:*` records (`MetaCyc:GALLATE-DEGRADATION-I-PWY`, `MetaCyc:PWY-8178`, `MetaCyc:THIOREDOX-PWY`; 52 concrete small-molecule `participants[]` entries) | `A-C7S4-002`: Change `category` from `chemical_entity` to `small_molecule` on all 52 concrete small-molecule metabolite, salt, and effector participants across the 3 affected MetaCyc records, record curation history, and regenerate `pages/` and `output/kgx/`. |

## Detailed Findings

### `F-C7S4-001`: Three maintained MetaCyc pathway records retain 16 literature `references[]` entries (`15` `PMID:*` and `1` `DOI:*`) with bare CURIE `title == id` placeholders instead of peer-reviewed article titles

- **Issue Key**: `bare-curie-literature-reference-titles-3-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (3)**:
  - `MetaCyc:SALVADEHYPOX-PWY` (`data/pathways/adenosine-nucleotides-degradation-ii.yaml`): bare CURIE titles on `PMID:7559336` (`references[40].title`), `PMID:10986234` (`references[41].title`), `PMID:19542235` (`references[42].title`), `PMID:41070194` (`references[43].title`), `PMID:31978345` (`references[44].title`), `PMID:40632566` (`references[45].title`)
  - `MetaCyc:GLCMANNANAUT-PWY` (`data/pathways/amino-sugar-superpathway.yaml`): bare CURIE titles on `PMID:33790291` (`references[52].title`), `PMID:19700525` (`references[53].title`), `PMID:28634232` (`references[56].title`)
  - `MetaCyc:GALLATE-DEGRADATION-II-PWY` (`data/pathways/gallate-degradation-i.yaml`): bare CURIE titles on `PMID:23977959` (`references[41].title`), `PMID:21219457` (`references[44].title`), `PMID:16030198` (`references[45].title`), `PMID:30346405` (`references[46].title`), `DOI:10.1016/j.procbio.2021.01.019` (`references[47].title`), `PMID:26867578` (`references[48].title`), `PMID:24657997` (`references[49].title`)
- **Evidence**: `EV-C7-BARE-CURIE-LITERATURE-TITLES-3`
- **Description**:
  Across these 3 maintained MetaCyc pathway records, the last 16 bare CURIE `references[]` entries in the 276-record corpus (`15` `PMID:*` and `1` `DOI:*`) store their CURIE string as `title` (`title == id`) instead of the actual peer-reviewed article title.

### `F-C7S4-002`: Three maintained MetaCyc pathway records type 52 concrete small-molecule metabolite, salt, and effector participants as generic `category: chemical_entity` instead of `category: small_molecule`

- **Issue Key**: `concrete-small-molecule-participants-typed-as-chemical-entity-3-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (3)**:
  - `MetaCyc:GALLATE-DEGRADATION-I-PWY` (`data/pathways/gallate-degradation-ii.yaml`): 32 concrete metabolite, salt, and effector participants at `participants[51..62, 65..74, 78..81, 83..87, 89]` (`CHEBI:15356`, `CHEBI:15422`, `CHEBI:16526`, `CHEBI:16761`, `CHEBI:16763`, `CHEBI:16810`, `CHEBI:16856`, `CHEBI:16947`, `CHEBI:173437`, `CHEBI:17742`, `CHEBI:18320`, `CHEBI:22629`, `CHEBI:29888`, `CHEBI:30808`, `CHEBI:31823`, `CHEBI:32139`, `CHEBI:32588`, `CHEBI:3312`, `CHEBI:34887`, `CHEBI:35780`, `CHEBI:36655`, `CHEBI:44976`, `CHEBI:53351`, `CHEBI:57499`, `CHEBI:58222`, `CHEBI:58276`, `CHEBI:62843`, `CHEBI:63317`, `CHEBI:747199`, `CHEBI:86228`, `CHEBI:9532`, `PubChem:6098323`)
  - `MetaCyc:PWY-8178` (`data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`): 16 concrete sugar-phosphate, inorganic, and effector participants at `participants[5..16, 32..35]` (`MetaCyc:D-SEDOHEPTULOSE-1-7-P2`, `MetaCyc:D-SEDOHEPTULOSE-7-P`, `MetaCyc:DIHYDROXY-ACETONE-PHOSPHATE`, `MetaCyc:ERYTHROSE-4P`, `MetaCyc:FRUCTOSE-6P`, `MetaCyc:GAP`, `MetaCyc:PPI`, `MetaCyc:PROTON`, `MetaCyc:Pi`, `MetaCyc:RIBOSE-5P`, `MetaCyc:RIBULOSE-5P`, `MetaCyc:XYLULOSE-5-PHOSPHATE`, `CHEBI:28938`, `CHEBI:29103`, `CHEBI:29105`, `CHEBI:30616`)
  - `MetaCyc:THIOREDOX-PWY` (`data/pathways/thioredoxin-pathway.yaml`): 4 concrete small-molecule inhibitor participants at `participants[32..35]` (`CHEBI:18407` `hydrogen cyanide`, `CHEBI:35456` `cadmium dichloride`, `CHEBI:20435` `p-mercuribenzoate`, `CHEBI:29242` `arsenite(1-)`)
- **Evidence**: `EV-C7-CONCRETE-SMALL-MOLECULE-CHEMICAL-ENTITY-3`
- **Description**:
  Across these 3 maintained MetaCyc pathway records, 52 concrete small-molecule metabolite, salt, and effector participants participating in `consumes`, `produces`, `activates`, or `inhibits` edges are typed as generic `category: chemical_entity` instead of `category: small_molecule` (unlike generic electron-carrier classes `MetaCyc:Acceptor` and `MetaCyc:Donor-H2` at `participants[8..9]` in `thioredoxin-pathway.yaml`). Because `src/pathwaymech/kgx.py` maps `chemical_entity` to `biolink:ChemicalEntity` and `small_molecule` to `biolink:SmallMolecule`, 17 of these concrete small molecules that are typed exclusively as `small_molecule` in all other maintained records export with merged `biolink:ChemicalEntity|biolink:SmallMolecule` categories in `pages/downloads/nodes.tsv`.
