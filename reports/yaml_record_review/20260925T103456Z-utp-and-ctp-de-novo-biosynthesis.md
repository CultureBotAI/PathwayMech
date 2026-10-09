# YAML Record Review: UTP and CTP de novo biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
- Started UTC: 2026-09-25T10:34:56Z
- Finished UTC: 2026-09-25T10:34:56Z
- Verdict: PASS - no blocker, major, or minor findings.

## Target

- Resolved exactly one maintained record: `data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml`.
- Target identity: `gomodel:YeastPathways_PWY-7176`, `UTP and CTP de novo biosynthesis`, `nucleotide-biosynthesis`.
- Target shape: 1 local taxon, 15 local participants, 4 local reactions, 30 mechanistic edges, and 1 declared reference.
- Compared the maintained YAML against both requested source artifacts:
  - `/private/tmp/gocam-noctua/YeastPathways_PWY-7176.json`
  - `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-7176.json`
- Verified generated products:
  - `pages/records/gomodel_YeastPathways_PWY-7176.html`
  - `pages/browse.html`
- Target resolution used gitignore-independent searches with `rg --no-ignore --hidden` / `rg --files --no-ignore --hidden`, excluding `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`, over the repository and the two requested `/private/tmp` GO-CAM roots for the filename stem and `PWY-7176`.

## Validation

- `just validate`: passed; 5 Claude skills, 89 pathway records, 3440 evidence blocks, 12 source records, 6 documentation files, and the deep-research report contract validated.
- `just test`: passed; 34 tests.
- `just lint`: passed; `ruff check .` reported no findings.
- `git diff --check`: passed.
- Skipped validators: none.

## Identity and Grounding

- The maintained `id` exactly matches both JSON sources: `gomodel:YeastPathways_PWY-7176`.
- The raw Noctua title is `UTP and CTP <i>de novo</i> biosynthesis - imported from: Saccharomyces Genome Database`; the compact SGD JSON carries the same title. The YAML label strips source suffix and HTML while preserving the pathway identity.
- The raw Noctua annotations import `object=PWY-7176` from Saccharomyces Genome Database, matching the `YeastPathways_PWY-7176` GO-CAM identifier used as the record id and reference id.
- The only upstream taxon annotation is `NCBITaxon:559292`, and the YAML declares exactly that local taxon as `Saccharomyces cerevisiae S288C`.
- All 15 YAML participants are the 4 SGD gene products and 11 ChEBI molecules used by the raw RO reaction facts and compact `enabled_by`, `has_input`, and `has_output` associations:
  `SGD:S000001507`, `SGD:S000001550`, `SGD:S000003864`, `SGD:S000000135`,
  `CHEBI:57865`, `CHEBI:30616`, `CHEBI:58223`, `CHEBI:456216`,
  `CHEBI:46398`, `CHEBI:58359`, `CHEBI:15377`, `CHEBI:29985`,
  `CHEBI:15378`, `CHEBI:43474`, and `CHEBI:37563`.
- All 4 YAML reaction/activity nodes are present in both source JSONs:
  `gomodel:RXN-12002`, `gomodel:UDPKIN-RXN`, `gomodel:CTPSYN-RXN`, and `gomodel:YeastPathways_PWY-7176/6a4c244800000283`.

## Graph and Local References

- All 30 `mechanistic_edges` subjects and objects resolve to the record id, a local participant, or a local reaction.
- All predicates are in `ALLOWED_EDGE_PREDICATES`: `enables`, `consumes`, and `produces`.
- All 60 evidence blocks resolve to the sole local reference, `gomodel:YeastPathways_PWY-7176`.
- The raw Noctua model has 30 RO facts:
  - 4 `RO:0002333` enabled-by assertions
  - 12 `RO:0002233` input assertions
  - 14 `RO:0002234` output assertions
- Translating those RO facts through the raw individual type map produces the same multiset of 30 `(subject, predicate, object)` triples as the YAML. Translating the compact SGD `activities` through `enabled_by`, `has_input`, and `has_output` also produces the same 30 triples. Both source-minus-YAML and YAML-minus-source diffs were empty.
- `pages/records/gomodel_YeastPathways_PWY-7176.html` renders the same 30 edge triples in YAML order.
- `pages/browse.html` links `records/gomodel_YeastPathways_PWY-7176.html` with `gomodel:YeastPathways_PWY-7176 - 30 mechanistic edges`; the generated browse entry is current for this record.

## Edge Evidence

- Edges `edge-001` to `edge-005`, for `gomodel:RXN-12002`, match the raw and compact source assertions that URA6 enables the UMP kinase step, ATP and UMP are inputs, and UDP and ADP are outputs.
- Edges `edge-006` to `edge-010`, for `gomodel:UDPKIN-RXN`, match the raw and compact source assertions that YNK1 enables the nucleoside diphosphate kinase step, UDP and ATP are inputs, and UTP and ADP are outputs.
- Edges `edge-011` to `edge-020`, for `gomodel:CTPSYN-RXN`, match the raw and compact source assertions that URA8 enables one CTP synthase step, UTP, L-glutamine, ATP, and water are inputs, and L-glutamate, hydron, hydrogenphosphate, ADP, and CTP are outputs.
- Edges `edge-021` to `edge-030`, for `gomodel:YeastPathways_PWY-7176/6a4c244800000283`, match the raw and compact source assertions that URA7 enables the second CTP synthase step, UTP, L-glutamine, ATP, and water are inputs, and L-glutamate, hydron, hydrogenphosphate, ADP, and CTP are outputs.
- Every one of the 60 evidence quotes in `data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml` is an exact substring of `/private/tmp/gocam-noctua/YeastPathways_PWY-7176.json`.

## Completeness

- No raw `RO:0002333`, `RO:0002233`, or `RO:0002234` mechanistic fact from the Noctua source is missing from the YAML.
- No compact `enabled_by`, `has_input`, or `has_output` association from the SGD JSON is missing from the YAML.
- No compact causal association is present for this GO-CAM, so there are no upstream `precedes`, `regulates`, `activates`, or `inhibits` edges to preserve.
- The raw JSON also has 8 BFO facts: 4 `BFO:0000050` assertions that each activity is part of `GO:0006207` and 4 `BFO:0000066` assertions that each activity occurs in `GO:0005829`. The compact JSON preserves these as `part_of: GO:0006207` and `occurs_in: GO:0005829` on each of the 4 activities. The YAML omits them because `BFO:0000050` and `BFO:0000066` are outside the local `ALLOWED_EDGE_PREDICATES`; no maintained pathway edge is lost.

## Findings

None found

## Recommended Edits

None found

## Follow-up Checks

- No immediate follow-up is required.
- If `data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml` changes later, refresh generated HTML with `just render-pages`, then rerun `just validate`, `just test`, `just lint`, and `git diff --check`.

## Additional Notes

- The source GO-CAM is a production Saccharomyces Genome Database import with top-level taxon `NCBITaxon:559292` and GO-CAM date `2026-07-07`.
- The record intentionally cites the GO-CAM model as the local evidence source and uses raw Noctua JSON snippets to bind each YAML edge to its exact upstream fact and typed upstream individual.
