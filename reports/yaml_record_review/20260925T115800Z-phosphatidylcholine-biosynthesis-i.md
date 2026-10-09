# YAML Record Review: phosphatidylcholine biosynthesis I

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
- Started UTC: 2026-09-25T11:58:00Z
- Finished UTC: 2026-09-25T11:58:25Z
- Verdict: Pass - no blocker, major, or minor findings.

## Target

Reviewed PR #120 as an open PR with head branch
`add-gocam-phosphatidylcholine-biosynthesis` at
`4f413c2e275aadf29d3407e7cc8d7b37bc78131e`.

Resolved exactly one maintained YAML record:

- `data/pathways/phosphatidylcholine-biosynthesis-i.yaml`
- `id`: `gomodel:YeastPathways_PWY3O-450`
- `label`: `phosphatidylcholine biosynthesis I`
- `pathway_type`: `lipid-biosynthesis`
- `taxa`: `NCBITaxon:559292`
- `participants`: 14
- `reactions`: 3
- `mechanistic_edges`: 18
- `references`: `gomodel:YeastPathways_PWY3O-450`

The review used these local rubric files:

- `.claude/skills/review-yaml-record/SKILL.md`
- `.claude/skills/add-pathway/SKILL.md`
- `CLAUDE.md`
- `docs/CURATION.md`
- `docs/HARMONIZATION.md`
- `justfile`
- `src/pathwaymech/schema.py`

The source files checked were:

- `/private/tmp/gocam-noctua/YeastPathways_PWY3O-450.json`
- `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY3O-450.json`

The local checkout was already on `add-gocam-phosphatidylcholine-biosynthesis`
and `HEAD` was `4f413c2e275aadf29d3407e7cc8d7b37bc78131e`.

## Validation

All requested read-only validators passed:

- `just validate`: passed; 5 Claude skills, 103 pathway records, 4,654
  evidence blocks, 12 source records, 6 documentation files, and the
  deep-research report contract validated.
- `just test`: passed; 34 tests.
- `just lint`: passed.
- `git diff --check`: passed.

No validators were skipped.

## Identity and Grounding

No identity defect found.

The raw Noctua GO-CAM model identifies:

- model id: `gomodel:YeastPathways_PWY3O-450`
- title: `phosphatidylcholine biosynthesis I - imported from: Saccharomyces
  Genome Database`
- state: `production`
- taxon: `NCBITaxon:559292`
- pathway individual:
  `gomodel:YeastPathways_PWY3O-450/YeastPathways_PWY3O-450`
- pathway individual class: `GO:0006657`, `CDP-choline pathway`
- pathway individual label: `phosphatidylcholine biosynthesis I`

The compact SGD GO-CAM source independently reports:

- `id`: `gomodel:YeastPathways_PWY3O-450`
- `title`: `phosphatidylcholine biosynthesis I - imported from:
  Saccharomyces Genome Database`
- `status`: `production`
- `taxon`: `NCBITaxon:559292`
- 3 activities
- 20 normalized ontology objects

The YAML label strips only the SGD importer suffix from the compact title. The
record denotes the exact SGD-derived phosphatidylcholine biosynthesis I GO-CAM,
not the sibling `gomodel:YeastPathways_PWY3O-259` Kennedy-pathway
phospholipid-biosynthesis model, broad `GO:0006657` alone, or one of the three
single molecular-function activities.

The three local reaction nodes match the compact GO-CAM activities:

- `gomodel:RXN-5781` maps to `GO:0004142`, diacylglycerol
  cholinephosphotransferase activity.
- `gomodel:2.7.7.15-RXN` maps to `GO:0004105`,
  choline-phosphate cytidylyltransferase activity.
- `gomodel:CHOLINE-KINASE-RXN` maps to `GO:0004103`, choline kinase activity.

The three SGD participants are exactly the compact model's `enabled_by` terms:

- `SGD:S000005074`, CPT1 Scer, enables `gomodel:RXN-5781`.
- `SGD:S000003434`, PCT1 Scer, enables `gomodel:2.7.7.15-RXN`.
- `SGD:S000004123`, CKI1 Scer, enables `gomodel:CHOLINE-KINASE-RXN`.

All 11 ChEBI participants used by raw `RO:0002233` and `RO:0002234` facts, or
by compact `has_input` and `has_output` associations, are declared in the YAML.
The record does not invent a local CURIE.

## Graph and Local References

No graph or local-reference defect found.

The YAML graph is internally closed:

- 19 local nodes are declared: the record id, 1 taxon, 14 participants, and 3
  reaction nodes.
- Every `mechanistic_edges` subject and object resolves to one of those local
  nodes.
- All 18 edge predicates are legal under `ALLOWED_EDGE_PREDICATES`: this record
  uses only `enables`, `consumes`, and `produces`.
- All 18 edge ids are unique.
- The 18 `(subject, predicate, object)` triples have no duplicates.
- Every edge cites the sole declared reference,
  `gomodel:YeastPathways_PWY3O-450`.
- All 36 YAML evidence quote strings are exact substrings of the raw Noctua
  JSON after stable JSON minification.
- No evidence quote exceeds the 400-character schema limit.

The generated page
`pages/records/gomodel_YeastPathways_PWY3O-450.html` matches the YAML title,
description, and all 18 edge statements in order. `pages/browse.html` links to
that rendered record and reports `gomodel:YeastPathways_PWY3O-450 - 18
mechanistic edges`.

## Edge Evidence

No edge-evidence defect found.

The raw Noctua JSON contains 24 total facts:

- `RO:0002233`: 7 input facts projected to `consumes`
- `RO:0002234`: 8 output facts projected to `produces`
- `RO:0002333`: 3 enabled-by facts projected to `enables`
- `BFO:0000050`: 3 pathway-containment facts intentionally omitted
- `BFO:0000066`: 3 cytosol-location facts intentionally omitted

Projection of every in-scope `RO:0002233`, `RO:0002234`, and `RO:0002333` fact
to YAML triples is exact:

- Missing from YAML: none
- Extra in YAML: none
- Duplicate projected raw edges: none
- Duplicate YAML edges: none
- Dangling projected endpoints: none

The compact SGD source has the same 18 molecular projections as the raw Noctua
source:

- 3 `enabled_by` associations
- 7 `has_input` associations
- 8 `has_output` associations
- 0 `causal_associations`

Every YAML edge includes the relevant raw Noctua fact quote plus the raw typed
individual quote that maps the GO-CAM individual to the stable SGD or ChEBI
participant id projected into the YAML.

## Completeness

No completeness defect found for this raw Noctua GO-CAM projection.

All compact SGD material associations are represented:

- `gomodel:CHOLINE-KINASE-RXN` has the CKI1 enabler, ATP and choline inputs,
  and hydron, ADP, and choline phosphate outputs.
- `gomodel:2.7.7.15-RXN` has the PCT1 enabler, CTP, hydron, and choline
  phosphate inputs, and CDP-choline and diphosphoric acid outputs.
- `gomodel:RXN-5781` has the CPT1 enabler, 1,2-diacyl-sn-glycerol and
  CDP-choline inputs, and CMP, phosphatidylcholine, and hydron outputs.

The compact source carries 3 `part_of` associations to `GO:0006657` and 3
`occurs_in` associations to `GO:0005829`. The raw Noctua source carries the
same placement as 3 `BFO:0000050` facts to
`gomodel:YeastPathways_PWY3O-450/YeastPathways_PWY3O-450` and 3
`BFO:0000066` facts to `reaction_*_location_lociGO_0005829` nodes. Exact
searches confirmed that `BFO:0000050`, `BFO:0000066`, `GO:0005829`, the raw
pathway individual, and raw location node ids are absent from the maintained
YAML and generated record page.

Hidden-and-ignored duplicate coverage was included. `rg --no-ignore --hidden`
searches over `.` excluding only `/.git` and `/.venv`, plus a hidden-aware
`find` by `*phosphatidylcholine*`, found the exact model CURIE, exact model
stem, exact pathway label, and all three reaction ids only in the target YAML
and generated pages. Exact hidden-and-ignored searches for the source
biological-process and molecular-function CURIEs `GO:0006657`, `GO:0004103`,
`GO:0004105`, and `GO:0004142` found no repository matches. No duplicate
maintained pathway record was found.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If `data/pathways/phosphatidylcholine-biosynthesis-i.yaml` changes, rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

If the generated page is refreshed, also rerun `just render-pages` and confirm
that `pages/records/gomodel_YeastPathways_PWY3O-450.html` and
`pages/browse.html` still match the YAML.

## Additional Notes

No GitHub issue, pull request, comment, label, setting, generated page,
maintained pathway YAML, source code file, test, or documentation file was
mutated for this read-only review.
