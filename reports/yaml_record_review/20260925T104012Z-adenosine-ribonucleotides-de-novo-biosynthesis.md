# YAML Record Review: adenosine ribonucleotides de novo biosynthesis

- Repository: PathwayMech
- Record: `data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml`
- Started UTC: 2026-09-25T10:40:12Z
- Finished UTC: 2026-09-25T10:40:12Z
- Verdict: pass

## Target

- Maintained YAML: `data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml`
- Record id: `gomodel:YeastPathways_PWY-7219`
- Record label: `adenosine ribonucleotides de novo biosynthesis`
- Pathway type: `nucleotide-biosynthesis`
- Local taxon: 1
- Local participants: 15
- Local reactions: 4
- Mechanistic edges: 20
- References: 1
- Raw Noctua source: `/private/tmp/gocam-noctua/YeastPathways_PWY-7219.json`
- Compact SGD GO-CAM source: `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-7219.json`

## Validation

- `just validate`: passed; validated 90 pathway records, checked 3480 evidence blocks, validated 12 source records, checked 6 documentation files, and checked the deep-research report contract.
- `just test`: passed; 34 tests passed.
- `just lint`: passed; Ruff reported `All checks passed!`.
- `git diff --check`: passed before this report was created.
- Skipped validators: none.

## Identity and Grounding

- Exact model identity matches both supplied sources:
  - YAML `id`: `gomodel:YeastPathways_PWY-7219`
  - raw Noctua `id`: `gomodel:YeastPathways_PWY-7219`
  - compact SGD GO-CAM `id`: `gomodel:YeastPathways_PWY-7219`
- The pathway label is supported by the GO-CAM title in both sources:
  `adenosine ribonucleotides <i>de novo</i> biosynthesis - imported from: Saccharomyces Genome Database`.
- The model is a production Saccharomyces Genome Database import:
  - raw `state`: `production`
  - compact `status`: `production`
  - compact import comment: `Imported from Saccharomyces Genome Database: https://pathway.yeastgenome.org/YEAST/NEW-IMAGE?object=PWY-7219`
- The local taxon id `NCBITaxon:559292` matches:
  - the raw Noctua `https://w3id.org/biolink/vocab/in_taxon` annotation
  - the compact SGD GO-CAM `taxon` field
- Every declared participant id and label matched a compact GO-CAM `objects[]`
  entry:
  - `SGD:S000005164` `ADE12 Scer`
  - `CHEBI:58053` `IMP(2-)`
  - `CHEBI:37565` `GTP(4-)`
  - `CHEBI:29991` `L-aspartate(1-)`
  - `CHEBI:15378` `hydron`
  - `CHEBI:57567` `N(6)-(1,2-dicarboxylatoethyl)-AMP(4-)`
  - `CHEBI:43474` `hydrogenphosphate`
  - `CHEBI:58189` `GDP(3-)`
  - `SGD:S000004351` `ADE13 Scer`
  - `CHEBI:29806` `fumarate(2-)`
  - `CHEBI:456215` `adenosine 5'-monophosphate(2-)`
  - `SGD:S000000972` `ADK2 Scer`
  - `CHEBI:30616` `ATP(4-)`
  - `CHEBI:456216` `ADP(3-)`
  - `SGD:S000002634` `ADK1 Scer`
- Every declared reaction id maps to the expected compact GO-CAM activity and
  molecular-function label:
  - `gomodel:ADENYLOSUCCINATE-SYNTHASE-RXN` -> `GO:0004019`
    `adenylosuccinate synthase activity`
  - `gomodel:AMPSYN-RXN` -> `GO:0004018`
    `N6-(1,2-dicarboxyethyl)AMP AMP-lyase (fumarate-forming) activity`
  - `gomodel:YeastPathways_PWY-7219/6a4c244800000590` -> `GO:0004017`
    `AMP kinase activity`
  - `gomodel:ADENYL-KIN-RXN` -> `GO:0004017`
    `AMP kinase activity`

## Graph and Local References

- Every `mechanistic_edges` subject and object resolves to the record id or a
  declared local participant/reaction node.
- Every edge predicate is in `ALLOWED_EDGE_PREDICATES` from
  `src/pathwaymech/schema.py`: this record uses only `enables`, `consumes`, and
  `produces`.
- All 20 edge ids are unique and sequential from `edge-001` through
  `edge-020`.
- Every evidence block cites the sole local reference
  `gomodel:YeastPathways_PWY-7219`, and that reference is declared in
  `references`.
- Translating the raw Noctua facts with `RO:0002333` as `enables`,
  `RO:0002233` as `consumes`, and `RO:0002234` as `produces` produced exactly
  the same 20 subject/predicate/object triples as the YAML.
- The raw Noctua JSON contains 28 facts total. The eight facts intentionally
  outside the YAML biochemical subgraph are BFO pathway/location assertions:
  - 4 `BFO:0000050` activity-part-of-`GO:0046086` facts
  - 4 `BFO:0000066` activity-occurs-in-`GO:0005829` facts
- Those eight BFO predicates are not permitted PathwayMech edge predicates, and
  neither `GO:0046086` nor `GO:0005829` is a declared local participant or
  reaction node in this record.

## Edge Evidence

- All 40 maintained evidence quotes are exact substrings of
  `/private/tmp/gocam-noctua/YeastPathways_PWY-7219.json`.
- Each YAML edge has one evidence quote for the relevant raw fact and one quote
  for the object individual's stable type:
  - `edge-001`: `ADE12 Scer` enables `ADENYLOSUCCINATE-SYNTHASE-RXN`
  - `edge-002`: `IMP(2-)` consumed by `ADENYLOSUCCINATE-SYNTHASE-RXN`
  - `edge-003`: `GTP(4-)` consumed by `ADENYLOSUCCINATE-SYNTHASE-RXN`
  - `edge-004`: `L-aspartate(1-)` consumed by
    `ADENYLOSUCCINATE-SYNTHASE-RXN`
  - `edge-005`: `ADENYLOSUCCINATE-SYNTHASE-RXN` produces `hydron`
  - `edge-006`: `ADENYLOSUCCINATE-SYNTHASE-RXN` produces
    `N(6)-(1,2-dicarboxylatoethyl)-AMP(4-)`
  - `edge-007`: `ADENYLOSUCCINATE-SYNTHASE-RXN` produces
    `hydrogenphosphate`
  - `edge-008`: `ADENYLOSUCCINATE-SYNTHASE-RXN` produces `GDP(3-)`
  - `edge-009`: `ADE13 Scer` enables `AMPSYN-RXN`
  - `edge-010`: `N(6)-(1,2-dicarboxylatoethyl)-AMP(4-)` consumed by
    `AMPSYN-RXN`
  - `edge-011`: `AMPSYN-RXN` produces `fumarate(2-)`
  - `edge-012`: `AMPSYN-RXN` produces `adenosine 5'-monophosphate(2-)`
  - `edge-013`: `ADK2 Scer` enables
    `gomodel:YeastPathways_PWY-7219/6a4c244800000590`
  - `edge-014`: `adenosine 5'-monophosphate(2-)` consumed by
    `gomodel:YeastPathways_PWY-7219/6a4c244800000590`
  - `edge-015`: `ATP(4-)` consumed by
    `gomodel:YeastPathways_PWY-7219/6a4c244800000590`
  - `edge-016`: `gomodel:YeastPathways_PWY-7219/6a4c244800000590` produces
    `ADP(3-)`
  - `edge-017`: `ADK1 Scer` enables `ADENYL-KIN-RXN`
  - `edge-018`: `adenosine 5'-monophosphate(2-)` consumed by
    `ADENYL-KIN-RXN`
  - `edge-019`: `ATP(4-)` consumed by `ADENYL-KIN-RXN`
  - `edge-020`: `ADENYL-KIN-RXN` produces `ADP(3-)`
- The reused molecule individuals are source-backed: the AMP individual from
  `AMPSYN-RXN` is reused as an input to both AMP kinase activities, and the
  adenylo-succinate individual produced by `ADENYLOSUCCINATE-SYNTHASE-RXN` is
  reused as the `AMPSYN-RXN` input.

## Completeness

- The YAML captures every non-BFO mechanistic fact in the raw Noctua JSON.
- The compact SGD GO-CAM JSON has four activities and all four are declared as
  local reactions in the YAML.
- The compact `causal_associations` value is `null` on all four activities, so
  the supplied compact source does not contribute ordering, activation,
  inhibition, or regulation edges beyond the 20 biochemical input/output/enabler
  edges.
- `pages/records/gomodel_YeastPathways_PWY-7219.html` is present and lists the
  same 20 mechanistic edges as the YAML.
- `pages/browse.html` is present and contains the expected browse link
  `records/gomodel_YeastPathways_PWY-7219.html` with `20 mechanistic edges`.

## Findings

None found.

Severity counts:

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None found.

## Follow-up Checks

No corrective follow-up is required for this record. If the maintained YAML is
changed later, refresh generated pages with `just render-pages` and rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

## Additional Notes

- The rendered page and browse entry were used only to detect staleness, not as
  source evidence.
- Absence-sensitive checks used `rg --no-ignore --hidden` or `find` and
  excluded `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache` where applicable.
  Exact searches covered `PWY-7219`, `GO:0046086`, `GO_REF:0000123`, and
  `NCBITaxon:559292` across the workspace and the supplied local GO-CAM
  sources; the prior-report check used `find reports/yaml_record_review` for
  `*adenosine-ribonucleotides-de-novo-biosynthesis.md`.
- No YAML files, generated pages, GitHub state, or issue state were edited.
