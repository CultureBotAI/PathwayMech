# PathwayMech Cycle 5 Stage 4 Findings & Dispositions Ledger

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `4` (`record_review`)
- **Revision**: `1`
- **Frozen Git Base (`source_revision`)**: `071f8b00c1abb4c0b3e394a3b44d866f59d31bad`
- **Previous Review Lineage Evidence**: [`reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml`](../../../../../reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml) (`sha256: 6ae9515798a646c7637194cac974cf2608b4497991b79120365a9076a7d7b8de`)
- **Structured Review ID**: `20261025T152000Z-cycle5-stage4-frozen-corpus-cohort-review`
- **Open Carry-Forward Finding IDs**: `F-C5S4-001`, `F-C5S4-002`

## Summary Table

| Finding ID | Stable Issue Key | Category | Severity | Status | Certainty | Affected Targets | Planned Cycle 5 Stage 5 Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `F-C5S4-001` | `gomodel-pwy-6074-1-reflexive-self-loop-edge-069` | `representation` | `minor` | `open` | `confirmed` | 1 `gomodel:*` record (`gomodel:YeastPathways_PWY-6074-1`, `data/pathways/zymosterol-biosynthesis.yaml`) | `A-C5S4-001`: Remove reflexive self-loop `edge-069` (`gomodel:RXN3O-9822 causally_upstream_of gomodel:RXN3O-9822`) at `mechanistic_edges[58]`, record curation history under `history/records/zymosterol-biosynthesis/`, and refresh `pages/`. |
| `F-C5S4-002` | `non-uniprot-generic-authority-record-reference-titles-11-records` | `representation` | `minor` | `open` | `confirmed` | 11 records (10 `MetaCyc:*` + 1 `PathBank:*`; 29 non-UniProt `references[]` entries: 26 `RHEA:*`, 1 `MetaCyc:RXN-15356`, 2 `PMID:*`) | `A-C5S4-002`: Replace all 29 generic `<CURIE> authority record` placeholder titles with descriptive Rhea reaction, MetaCyc reaction, and PubMed titles across the 11 affected records, record curation history, and refresh `pages/`. |

## Detailed Findings

### `F-C5S4-001`: `gomodel:YeastPathways_PWY-6074-1` (`zymosterol-biosynthesis.yaml`) retains a reflexive reaction self-loop `edge-069` (`gomodel:RXN3O-9822 causally_upstream_of gomodel:RXN3O-9822`)

- **Issue Key**: `gomodel-pwy-6074-1-reflexive-self-loop-edge-069`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Target (1)**: `gomodel:YeastPathways_PWY-6074-1` (`data/pathways/zymosterol-biosynthesis.yaml`)
- **Affected Field Paths**:
  - `data/pathways/zymosterol-biosynthesis.yaml#mechanistic_edges[58]` (`id: edge-069`)
- **Evidence**: `EV-C5-ZYMOSTEROL-SELF-LOOP-EDGE-069`
- **Description**:
  In `gomodel:YeastPathways_PWY-6074-1` (`data/pathways/zymosterol-biosynthesis.yaml`), `mechanistic_edges[58]` (`id: edge-069`, lines 673–681) asserts a reflexive causal self-loop `gomodel:RXN3O-9822 causally_upstream_of gomodel:RXN3O-9822` (`source_assertion: "The model asserts gomodel:RXN3O-9822 RO:0002411 gomodel:RXN3O-9822."`, `source_locator: "./YeastPathways_PWY-6074-1.json#/facts/68; endpoint types: /individuals/58/type; /individuals/58/type"`). Across all `14,600` `mechanistic_edges` in the 274-record corpus, `edge-069` is the sole self-loop (`subject == object`). Reaction `gomodel:RXN3O-9822` (`C-4 methylsterol oxidase activity`) is already connected to its upstream substrate `CHEBI:87289` (`4alpha-hydroxymethyl-4beta-methylzymosterol`, produced by `gomodel:RXN3O-9821` via `edge-040` and consumed by `gomodel:RXN3O-9822` via `edge-025`) and its downstream product `CHEBI:87287` (`4beta-methylzymosterol-4-carbaldehyde`, produced by `gomodel:RXN3O-9822` via `edge-103` and consumed by `gomodel:RXN3O-9823` via `edge-077`).

### `F-C5S4-002`: Eleven maintained pathway records retain 29 non-UniProt `references[]` entries (`26` `RHEA:*`, `1` `MetaCyc:RXN-15356`, and `2` `PMID:*`) with generic `<CURIE> authority record` placeholder titles

- **Issue Key**: `non-uniprot-generic-authority-record-reference-titles-11-records`
- **Category / Severity / Status / Certainty**: `representation` / `minor` / `open` / `confirmed`
- **Targets (11)**:
  - `MetaCyc:P101-PWY` (`data/pathways/ectoine-biosynthesis.yaml`): generic titles on `RHEA:23776` (`references[7].title`), `RHEA:24284` (`references[8].title`), `RHEA:11160` (`references[9].title`), `RHEA:16901` (`references[10].title`), `RHEA:17281` (`references[11].title`)
  - `MetaCyc:GLYOXYLATE-BYPASS` (`data/pathways/glyoxylate-cycle.yaml`): generic titles on `RHEA:16846` (`references[7].title`), `RHEA:10229` (`references[8].title`), `RHEA:22145` (`references[9].title`), `RHEA:21433` (`references[10].title`), `RHEA:16845` (`references[11].title`), `RHEA:21432` (`references[12].title`), `PMID:16027371` (`references[13].title`)
  - `MetaCyc:PWY-6124` (`data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml`): generic title on `PMID:21548610` (`references[12].title`)
  - `MetaCyc:ARGSYN-PWY` (`data/pathways/l-arginine-biosynthesis-i.yaml`): generic titles on `RHEA:18634` (`references[17].title`), `RHEA:18633` (`references[18].title`)
  - `MetaCyc:ARGDEG-III-PWY` (`data/pathways/l-arginine-degradation-iv.yaml`): generic titles on `RHEA:17641` (`references[5].title`), `RHEA:18037` (`references[6].title`), `RHEA:22284` (`references[7].title`)
  - `MetaCyc:CYSTSYN-PWY` (`data/pathways/l-cysteine-biosynthesis-i.yaml`): generic title on `RHEA:24560` (`references[6].title`)
  - `MetaCyc:HOMOSERSYN-PWY` (`data/pathways/l-homoserine-biosynthesis.yaml`): generic titles on `RHEA:23776` (`references[5].title`), `RHEA:24284` (`references[6].title`), `RHEA:15761` (`references[7].title`)
  - `MetaCyc:RHAMCAT-PWY` (`data/pathways/l-rhamnose-degradation-i.yaml`): generic title on `MetaCyc:RXN-15356` (`references[6].title`)
  - `MetaCyc:SERSYN-PWY` (`data/pathways/l-serine-biosynthesis-i.yaml`): generic titles on `RHEA:12641` (`references[5].title`), `RHEA:14329` (`references[6].title`), `RHEA:21208` (`references[7].title`)
  - `MetaCyc:HOMOSER-THRESYN-PWY` (`data/pathways/l-threonine-biosynthesis.yaml`): generic title on `RHEA:13985` (`references[5].title`)
  - `PathBank:SMP0000992` (`data/pathways/threonine-biosynthesis-from-aspartate-escherichia-coli.yaml`): generic titles on `RHEA:15761` (`references[5].title`), `RHEA:13985` (`references[7].title`)
- **Evidence**: `EV-C5-NON-UNIPROT-GENERIC-AUTHORITY-TITLES-11`
- **Description**:
  Across these 11 maintained pathway records, 29 non-UniProt `references[]` entries (`26` `RHEA:*`, `1` `MetaCyc:RXN-15356`, and `2` `PMID:*`) retain generic `<CURIE> authority record` placeholder titles instead of descriptive reaction or PubMed titles.
