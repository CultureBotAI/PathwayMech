# PathwayMech Cycle 3 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `62848bb7170f46df448678b50fdcf5a659769034`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml) (`sha256: 9b874bcf4999ee0e26c53a404b5c91a3dd2ae02ac6a8ad9f97ae0b5785d6fde2`)
- **Structured Review ID**: `20261023T152000Z-cycle3-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C3S4-001`, `F-C3S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 3 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C3S4-001` | `gomodel-missing-participant-category-in-7-records` | `representation` | `minor` | `open` | `confirmed` | 7 `gomodel:*` records (11 participant entries: 5 `CHEBI:*` + 6 `gomodel:*`) | `A-C3S4-001`: Add explicit `participants[].category` to all 11 untyped participant entries across the 7 affected `gomodel:*` records (`chemical_entity` for the 5 `CHEBI:*` polymer/polyanion/protein-group participants; `pathway` or `biological_process` for the 6 `gomodel:*` boundary nodes), record curation history, and refresh `pages/`. |
| `F-C3S4-002` | `gomodel-oxobutanoate-mislabeled-as-lipid-in-4-records` | `consistency` | `minor` | `open` | `confirmed` | 4 `gomodel:*` records (4 participant entries across `CHEBI:11851` and `CHEBI:16763`) | `A-C3S4-002`: Change `participants[].category` from `lipid` to `small_molecule` on `CHEBI:11851` (`3-methyl-2-oxobutanoate`) in `gomodel:YeastPathways_PWY3O-4105` and on `CHEBI:16763` (`2-oxobutanoate`) in `gomodel:YeastPathways_HOMOCYS-CYS-CONVERT`, `gomodel:YeastPathways_HOMOCYSDEGR-PWY-1`, and `gomodel:YeastPathways_THREOCAT2-PWY`, record curation history, and refresh `pages/`. |

## Detailed Findings

### `F-C3S4-001`: Seven maintained `gomodel` pathway records omit explicit `participants[].category` on 11 participant entries

- **Issue Key**: `gomodel-missing-participant-category-in-7-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (7)**:
  `gomodel:YeastPathways_PWY3O-15`, `gomodel:YeastPathways_PWY-5670-1`, `gomodel:YeastPathways_PWY3O-697`, `gomodel:YeastPathways_PWY-1801-1`, `gomodel:YeastPathways_PWY-5041`, `gomodel:YeastPathways_PWY3O-17`, `gomodel:YeastPathways_PWY-5080-1`
- **Untyped Participant CURIEs (11)**:
  - `CHEBI:17029` (`chitin` in `gomodel:YeastPathways_PWY3O-15`, `participants[0]`)
  - `gomodel:YeastPathways_PWY-5670-1/654d809000002591` (`trans, trans-farnesyl diphosphate biosynthesis` in `gomodel:YeastPathways_PWY-5670-1`, `participants[8]`)
  - `gomodel:YeastPathways_PWY-5670-1/654d809000002611` (`ergosterol biosynthesis I` in `gomodel:YeastPathways_PWY-5670-1`, `participants[15]`)
  - `CHEBI:134413` (`a tetrahydrofolyl-[Glu](n) polyanion` in `gomodel:YeastPathways_PWY3O-697`, `participants[11]`)
  - `gomodel:YeastPathways_PWY-1801-1/65692e7e00001183` (`10-formyl-tetrahydrofolate metabolism` in `gomodel:YeastPathways_PWY-1801-1`, `participants[7]`)
  - `gomodel:ba4cc2f6-35b0-45f1-a3b5-7bf7a1e71bf8_RXN-7605` (`SAM-dependent biomolecule methylation` in `gomodel:YeastPathways_PWY-5041`, `participants[15]`)
  - `CHEBI:143915` (`[ThiS protein]-C-terminal Gly-NH-CH2-C(O)SH` in `gomodel:YeastPathways_PWY3O-17`, `participants[30]`)
  - `CHEBI:29979` (`L-cysteine-S-yl group` in `gomodel:YeastPathways_PWY3O-17`, `participants[31]`)
  - `CHEBI:29950` (`L-alanin-3-yl group` in `gomodel:YeastPathways_PWY3O-17`, `participants[32]`)
  - `CHEBI:90873` (`carboxy-[ThiS protein]` in `gomodel:YeastPathways_PWY3O-17`, `participants[33]`)
  - `gomodel:46fed9f2-cf0b-4568-b40e-557bd0cfffe5_RXN3O-9813` (`palmitoleate biosynthesis` in `gomodel:YeastPathways_PWY-5080-1`, `participants[9]`)
- **Evidence**: `EV-C3-UNTYPED-11-PARTICIPANTS`, `EV-C3-KGX-EXPORT`, `EV-C3-NODES-TSV`
- **Description**:
  Across the 272 maintained pathway records (`7,721` total participant entries), `7,710` participant entries explicitly declare `participants[].category`, whereas these 11 participant entries across 7 `gomodel:*` records omit `participants[].category`. Because none of those 11 participant CURIEs has an explicit category in any other record, `src/pathwaymech/kgx.py` exports all 11 in `pages/downloads/nodes.tsv` via `_PREFIX_CATEGORIES` fallback with an empty `source_category` (`""`) — the only 11 participant/reaction nodes out of `5,442` KGX nodes in `pages/downloads/nodes.tsv` with empty `source_category`.

### `F-C3S4-002`: Four maintained `gomodel` pathway records type short-chain 2-oxoacid amino-acid intermediates (`CHEBI:11851` and `CHEBI:16763`) as `category: lipid` instead of `category: small_molecule`

- **Issue Key**: `gomodel-oxobutanoate-mislabeled-as-lipid-in-4-records`
- **Category / Severity / Status / Certainty**: `consistency` / `minor` / `open` / `confirmed`
- **Targets (4)**:
  `gomodel:YeastPathways_PWY3O-4105`, `gomodel:YeastPathways_HOMOCYS-CYS-CONVERT`, `gomodel:YeastPathways_HOMOCYSDEGR-PWY-1`, `gomodel:YeastPathways_THREOCAT2-PWY`
- **Affected Participant CURIEs (2)**:
  `CHEBI:11851` (`3-methyl-2-oxobutanoate`), `CHEBI:16763` (`2-oxobutanoate`)
- **Evidence**: `EV-C3-OXOBUTANOATE-LIPID-MISMATCH`, `EV-C3-KGX-EXPORT`, `EV-C3-NODES-TSV`
- **Description**:
  In `gomodel:YeastPathways_PWY3O-4105` (`data/pathways/valine-degradation.yaml`, `participants[3]`), `CHEBI:11851` (`3-methyl-2-oxobutanoate`, alpha-ketoisovalerate) is typed as `category: lipid`, whereas sibling records `MetaCyc:LEUSYN-PWY`, `MetaCyc:PANTO-PWY`, and `MetaCyc:VALSYN-PWY` type `CHEBI:11851` as `category: small_molecule`. Similarly, in `gomodel:YeastPathways_HOMOCYS-CYS-CONVERT` (`participants[13]`), `gomodel:YeastPathways_HOMOCYSDEGR-PWY-1` (`participants[9]`), and `gomodel:YeastPathways_THREOCAT2-PWY` (`participants[3]`), `CHEBI:16763` (`2-oxobutanoate`, alpha-ketobutyrate) is typed as `category: lipid`, whereas sibling record `MetaCyc:ILEUSYN-PWY` types `CHEBI:16763` as `category: small_molecule`. Chemically and in ChEBI, both `3-methyl-2-oxobutanoate` and `2-oxobutanoate` are short-chain 2-oxomonocarboxylic acid amino-acid metabolites rather than lipids, and this cross-record discrepancy causes `pages/downloads/nodes.tsv` to emit merged Biolink categories `biolink:ChemicalEntity|biolink:SmallMolecule` with `source_category='lipid|small_molecule'`.
