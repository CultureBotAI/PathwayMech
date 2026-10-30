# PathwayMech Cycle 6 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `bac5a3bcd954ece28631747e28cfb3da8ba4df91`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml) (`sha256: a5ad35ab3e54ad3f562ba0612165b39204b6493518ec41ba28d001380f51630c`)
- **Structured Review ID**: `20261030T095500Z-cycle6-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C6S4-001`, `F-C6S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 6 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C6S4-001` | `acetogenesis-ferredoxin-small-molecule-category-mismatch` | `representation` | `minor` | `open` | `confirmed` | 1 `WikiPathways:*` record (`WikiPathways:WP5019`, `data/pathways/acetogenesis.yaml`) | `A-C6S4-001`: Change `participants[28].category` (`CHEBI:17908`, `oxidized ferredoxin`) and `participants[29].category` (`CHEBI:17513`, `reduced ferredoxin`) from `small_molecule` to `protein`, record curation history under `history/records/acetogenesis/`, and regenerate `pages/downloads/nodes.tsv`. |
| `F-C6S4-002` | `bare-curie-reference-titles-5-metacyc-records` | `representation` | `minor` | `open` | `confirmed` | 5 `MetaCyc:*` records (`MetaCyc:PWY-8130`, `MetaCyc:SALVADEHYPOX-PWY`, `MetaCyc:GLCMANNANAUT-PWY`, `MetaCyc:GALLATE-DEGRADATION-II-PWY`, `MetaCyc:PWY-8132`; 23 `references[]` entries) | `A-C6S4-002`: Replace all 23 bare CURIE `title == id` placeholders with descriptive reaction, pathway, complex, transcription unit, gene, and protein titles across the 5 affected MetaCyc records, record curation history, and refresh `pages/`. |

## Detailed Findings

### `F-C6S4-001`: `WikiPathways:WP5019` (`acetogenesis.yaml`) types iron-sulfur protein redox carriers `CHEBI:17908` (`oxidized ferredoxin`) and `CHEBI:17513` (`reduced ferredoxin`) as `category: small_molecule` instead of `category: protein`

- **Issue Key**: `acetogenesis-ferredoxin-small-molecule-category-mismatch`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Target (1)**: `WikiPathways:WP5019` (`data/pathways/acetogenesis.yaml`)
- **Affected Field Paths**:
  - `data/pathways/acetogenesis.yaml#participants[28].category` (`id: CHEBI:17908`, `label: oxidized ferredoxin`)
  - `data/pathways/acetogenesis.yaml#participants[29].category` (`id: CHEBI:17513`, `label: reduced ferredoxin`)
- **Evidence**: `EV-C6-ACETOGENESIS-FERREDOXIN-CATEGORY-MISMATCH`
- **Description**:
  In `WikiPathways:WP5019` (`data/pathways/acetogenesis.yaml`), `participants[28]` (`id: CHEBI:17908`, `label: oxidized ferredoxin`, lines 97–99) and `participants[29]` (`id: CHEBI:17513`, `label: reduced ferredoxin`, lines 100–102) are typed as `category: small_molecule`. As explicitly documented in `data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml` (`MetaCyc:PWY-8132`, lines 39–41 and `participants[12,14]` at lines 232–238), `CHEBI:17908` and `CHEBI:17513` denote iron-sulfur protein redox classes (`category: protein`), consistent with all other protein redox carriers in the corpus (`CHEBI:15033` thioredoxin, `CHEBI:15967` thioredoxin dithiol, `CHEBI:18191` thioredoxin disulfide, `CHEBI:18097` ferricytochrome b5, `CHEBI:16518` ferrocytochrome b5, `MetaCyc:Oxidized-ferredoxins`, `MetaCyc:Reduced-ferredoxins`). Because `src/pathwaymech/kgx.py` maps `small_molecule` to `biolink:SmallMolecule` and `protein` to `biolink:Protein`, this mistyping causes `pages/downloads/nodes.tsv` to export both `CHEBI:17908` and `CHEBI:17513` with conflicting disjoint Biolink categories `biolink:Protein|biolink:SmallMolecule`—the only two nodes in the 6,053-node KGX graph with a `Protein|SmallMolecule` class conflict.

### `F-C6S4-002`: Five maintained MetaCyc pathway records retain 23 structured-database `references[]` entries (`11` `MetaCyc:*`, `7` `EcoCyc:*`, `3` `Entrez:*`, `2` `UniProtKB:*`) with bare CURIE `title == id` placeholders

- **Issue Key**: `bare-curie-reference-titles-5-metacyc-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (5)**:
  - `MetaCyc:PWY-8130` (`data/pathways/5-prime-deoxyadenosine-degradation-i.yaml`): bare CURIE titles on `MetaCyc:RXN-14304` (`references[1].title`), `MetaCyc:RXN-21315` (`references[2].title`), `MetaCyc:RXN-21316` (`references[3].title`)
  - `MetaCyc:SALVADEHYPOX-PWY` (`data/pathways/adenosine-nucleotides-degradation-ii.yaml`): bare CURIE titles on `EcoCyc:AMP-DEPHOSPHORYLATION-RXN` (`references[27].title`), `UniProtKB:P23841` (`references[31].title`), `EcoCyc:CPLX0-7681` (`references[32].title`), `EcoCyc:EG11146-MONOMER` (`references[33].title`), `EcoCyc:TU301` (`references[34].title`), `EcoCyc:TU0-45226` (`references[35].title`), `EcoCyc:G85` (`references[36].title`), `Entrez:946878` (`references[37].title`), `Entrez:945283` (`references[38].title`), `Entrez:945654` (`references[39].title`)
  - `MetaCyc:GLCMANNANAUT-PWY` (`data/pathways/amino-sugar-superpathway.yaml`): bare CURIE title on `MetaCyc:GLCMANNANAUT-PWY` (`references[18].title`)
  - `MetaCyc:GALLATE-DEGRADATION-II-PWY` (`data/pathways/gallate-degradation-i.yaml`): bare CURIE titles on `MetaCyc:CPLX-7916` (`references[42].title`), `UniProtKB:P22636` (`references[43].title`)
  - `MetaCyc:PWY-8132` (`data/pathways/s-methyl-5-thio-alpha-d-ribose-1-phosphate-degradation-iii.yaml`): bare CURIE titles on `MetaCyc:5.3.1.23-RXN` (`references[0].title`), `MetaCyc:O-ACETYLHOMOSERINE-THIOL-LYASE-RXN` (`references[1].title`), `MetaCyc:RXN-21318` (`references[3].title`), `MetaCyc:RXN-21319` (`references[4].title`), `MetaCyc:RXN-21320` (`references[5].title`), `MetaCyc:CPLX-8242` (`references[33].title`), `MetaCyc:MONOMER-21153` (`references[38].title`)
- **Evidence**: `EV-C6-BARE-CURIE-REFERENCE-TITLES-5`
- **Description**:
  Across these 5 maintained MetaCyc pathway records, 23 non-literature structured-database `references[]` entries (`11` `MetaCyc:*`, `7` `EcoCyc:*`, `3` `Entrez:*`, `2` `UniProtKB:*`) store a bare CURIE string identical to `id` (`title == id`) as their `title` instead of the descriptive reaction, pathway, complex, transcription unit, gene, or protein title already recorded in the local YAML record or quoted authority fields (separate from 16 `PMID:*`/`DOI:*` literature `references[]` entries in `adenosine-nucleotides-degradation-ii.yaml` `references[40..45]`, `amino-sugar-superpathway.yaml` `references[52,53,56]`, and `gallate-degradation-i.yaml` `references[41,44..49]`).
