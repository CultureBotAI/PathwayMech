# YAML Record Review: phospholipid biosynthesis II (Kennedy pathway)

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
- Started UTC: 2026-09-25T11:47:26Z
- Finished UTC: 2026-09-25T11:47:26Z
- Verdict: Pass - no blocker, major, or minor findings.

## Target

Reviewed exactly one maintained YAML record:

- `data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml`
- `id`: `gomodel:YeastPathways_PWY3O-259`
- `label`: `phospholipid biosynthesis II (Kennedy pathway)`
- `pathway_type`: `lipid-biosynthesis`
- `taxa`: `NCBITaxon:559292`
- `participants`: `SGD:S000002554`, `SGD:S000001165`, `SGD:S000003239`, `CHEBI:15378`, `CHEBI:58190`, `CHEBI:30616`, `CHEBI:17815`, `CHEBI:456216`, `CHEBI:60377`, `CHEBI:57603`, `CHEBI:16038`, `CHEBI:29888`, `CHEBI:57876`, `CHEBI:37563`
- `reactions`: `gomodel:ETHANOLAMINE-KINASE-RXN`, `gomodel:2.7.7.14-RXN`, `gomodel:ETHANOLAMINEPHOSPHOTRANSFERASE-RXN`
- `mechanistic_edges`: 18
- `references`: `gomodel:YeastPathways_PWY3O-259`

The local rubric files used were `.claude/skills/review-yaml-record/SKILL.md`,
`.claude/skills/add-pathway/SKILL.md`, `CLAUDE.md`, `docs/CURATION.md`,
`docs/HARMONIZATION.md`, `justfile`, and `src/pathwaymech/schema.py`.

## Validation

All required full-corpus read-only checks passed:

- `just validate`: passed; 5 Claude skills, 101 pathway records, 4,490 evidence blocks, 12 source records, 6 documentation files, and the deep-research report contract validated.
- `just test`: passed; 34 tests.
- `just lint`: passed.
- `git diff --check`: passed.

No validators were skipped.

## Identity and Grounding

The record identity matches both GO-CAM source files:

- Raw Noctua: `/private/tmp/gocam-noctua/YeastPathways_PWY3O-259.json`
- Compact SGD GO-CAM: `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY3O-259.json`
- GO-CAM model id: `gomodel:YeastPathways_PWY3O-259`
- Compact title: `phospholipid biosynthesis II (Kennedy pathway) - imported from: Saccharomyces Genome Database`
- Compact status: `production`
- Compact taxon: `NCBITaxon:559292`

The YAML label strips only the importer suffix from the compact title. The
record denotes the exact SGD-derived GO-CAM for Kennedy-pathway phospholipid
biosynthesis rather than `GO:0046474` as a broad glycerophospholipid parent or
any single reaction activity.

The three local reaction nodes match the three compact GO-CAM activities:

- `gomodel:ETHANOLAMINE-KINASE-RXN` maps to `GO:0004305`,
  ethanolamine kinase activity.
- `gomodel:2.7.7.14-RXN` maps to `GO:0004306`,
  ethanolamine-phosphate cytidylyltransferase activity.
- `gomodel:ETHANOLAMINEPHOSPHOTRANSFERASE-RXN` maps to `GO:0004307`,
  ethanolaminephosphotransferase activity.

The three SGD gene-product participants are exactly the compact model's
`enabled_by` terms:

- `SGD:S000002554`, EKI1 Scer, enables `gomodel:ETHANOLAMINE-KINASE-RXN`.
- `SGD:S000001165`, EPT1 Scer, enables
  `gomodel:ETHANOLAMINEPHOSPHOTRANSFERASE-RXN`.
- `SGD:S000003239`, ECT1 Scer, enables `gomodel:2.7.7.14-RXN`.

All ChEBI participant ids used by `has_input` or `has_output` in the compact
source are declared in YAML, and the record does not invent a local CURIE.

## Graph and Local References

Every `mechanistic_edges` endpoint resolves to the record id or to a declared
local participant/reaction. Every edge predicate is legal under
`ALLOWED_EDGE_PREDICATES` in `src/pathwaymech/schema.py`: this record uses only
`enables`, `consumes`, and `produces`.

Every edge evidence block cites the sole declared local reference,
`gomodel:YeastPathways_PWY3O-259`, and every quoted snippet is present verbatim
in the raw Noctua JSON.

The generated page `pages/records/gomodel_YeastPathways_PWY3O-259.html`
matches the maintained YAML title, description, and all 18 edge statements.
`pages/browse.html` links to the same rendered record and reports 18
mechanistic edges.

The YAML and rendered record omit all six BFO facts from the raw Noctua JSON:
three `BFO:0000050` containment assertions that make the activities part of the
model pathway individual and three `BFO:0000066` cytosol-location assertions.
They also omit the compact `occurs_in` value `GO:0005829` and compact
`part_of` value `GO:0046474`, so location and broad biological-process
containment did not leak into the maintained biochemical graph.

## Edge Evidence

Source edge projection is exact.

The compact SGD GO-CAM contains three activities that expand to 18 material
PathwayMech edges:

- 3 `enabled_by` associations projected to `enables`
- 7 `has_input` associations projected to `consumes`
- 8 `has_output` associations projected to `produces`

The raw Noctua JSON contains the same 18 material RO facts:

- 3 `RO:0002333` enabled-by facts
- 7 `RO:0002233` input facts
- 8 `RO:0002234` output facts

Comparing `(subject, predicate, object)` triples after compact-source
projection found no YAML-only edges and no compact-only edges. Each YAML edge
quotes the relevant raw Noctua fact and the raw typed object that maps the
Noctua individual to its stable SGD or ChEBI class.

## Completeness

No material source edge is missing from the YAML:

- Ethanolamine kinase has its EKI1 enabler, ATP and ethanolaminium inputs, and
  hydron, O-phosphonatoethanaminium, and ADP outputs.
- Ethanolaminephosphotransferase has its EPT1 enabler,
  1,2-diacyl-sn-glycerol and CDP-ethanolamine inputs, and CMP, hydron, and
  phosphatidylethanolamine outputs.
- Ethanolamine-phosphate cytidylyltransferase has its ECT1 enabler,
  O-phosphonatoethanaminium, hydron, and CTP inputs, and diphosphoric acid and
  CDP-ethanolamine outputs.

The compact model has no `causal_associations`, so no `precedes`, `activates`,
`inhibits`, or `regulates` edges were available to curate from this source.

Hidden-and-ignored duplicate coverage was included. Searches over `.` plus both
GO-CAM source directories, excluding only `/.git` and `/.venv`, found the exact
model CURIE and exact pathway label only in the target YAML, the generated
pages, and the two source JSON files. `SGD_PWY:PWY3O-259` occurred only in the
two source JSON files. A hidden-and-ignored `find` by `*kennedy*` found the
target YAML plus expected branch refs/logs only; no second maintained YAML or
rendered GO-CAM record with that stem exists.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

After any future YAML edit, regenerate pages and rerun:

- `just validate`
- `just render-pages`
- `just test`
- `just lint`
- `git diff --check`

## Additional Notes

No GitHub issue, pull request, comment, label, setting, generated page, source
code file, test, or documentation file was mutated for this read-only review.
