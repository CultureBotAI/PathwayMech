# YAML Record Review: dolichyl phosphate D-mannose biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
- Started UTC: 2026-09-25 11:32 UTC
- Finished UTC: 2026-09-25 11:34 UTC
- Verdict: Pass. No blocker, major, or minor findings.

## Target

Reviewed PR #116, `Add dolichyl phosphate D-mannose GO-CAM`, on branch
`add-gocam-dolichyl-phosphate-mannose` against `main`.

PR metadata verified through `gh pr view 116`:

- State: open
- Draft: false
- Mergeable: `MERGEABLE`
- Head repository: `CultureBotAI/PathwayMech`
- Base branch: `main`
- Head commit: `e91a03492110efe602aed44b0ae1113506d5586a`

The local checkout was on `add-gocam-dolichyl-phosphate-mannose` and `HEAD`
matched the PR head commit.

The PR changes exactly these three files:

- `data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml`
- `pages/browse.html`
- `pages/records/gomodel_YeastPathways_PWY3O-123.html`

The maintained YAML record resolves to:

- `id`: `gomodel:YeastPathways_PWY3O-123`
- `label`: `dolichyl phosphate D-mannose biosynthesis`
- `pathway_type`: `glycan-biosynthesis`
- `taxa`: `NCBITaxon:559292`, Saccharomyces cerevisiae S288C
- 13 participants, 4 reaction nodes, 20 mechanistic edges, and 1 declared
  reference

Raw sources checked:

- `/private/tmp/gocam-noctua/YeastPathways_PWY3O-123.json`
- `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY3O-123.json`

## Validation

All requested validation gates passed:

- `just validate`
  - `validated 5 Claude skills`
  - `validated 99 pathway records`
  - `checked 4332 evidence blocks`
  - `validated 12 source records`
  - `checked 6 documentation files`
  - `checked deep-research report contract`
- `just test`
  - 34 tests passed
- `just lint`
  - Ruff reported `All checks passed!`
- `git diff --check`
  - passed with no whitespace errors

## Identity and Grounding

The raw Noctua model identifies the source model as
`gomodel:YeastPathways_PWY3O-123`, marks it `production`, titles it
`dolichyl phosphate D-mannose biosynthesis - imported from: Saccharomyces
Genome Database`, and annotates `NCBITaxon:559292` as its taxon. The pathway
individual `gomodel:YeastPathways_PWY3O-123/YeastPathways_PWY3O-123` carries
`rdfs:label` `dolichyl phosphate D-mannose biosynthesis` and the source SGD
xref `YeastPathways_PWY3O-123`.

The compact SGD GO-CAM source independently reports:

- `id`: `gomodel:YeastPathways_PWY3O-123`
- `title`: `dolichyl phosphate D-mannose biosynthesis - imported from: Saccharomyces Genome Database`
- `taxon`: `NCBITaxon:559292`
- `status`: `production`
- 4 activities, 17 ontology objects, and 1 top-level provenance block

Duplicate and identity searches used `rg --no-ignore --hidden` while excluding
only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.

- Exact repository-wide searches for `gomodel:YeastPathways_PWY3O-123`,
  `PWY3O-123`, `dolichyl phosphate D-mannose biosynthesis`,
  `MANNPGUANYLTRANGDP-RXN`, `PHOSMANMUT-RXN`, `MANNPISOM-RXN`, and
  `2.4.1.83-RXN` matched only the new target YAML, the new generated record
  page, and the new generated browse entry before this report was written.
- Exact repository-wide searches for the intentionally omitted `GO:0006013`
  source pathway type found no matches before this report was written.

No identity collision or duplicate maintained pathway record was found.

## Graph and Local References

The YAML graph is internally closed:

- The record declares 19 local nodes: the record id, 1 taxon, 13 participants,
  and 4 reactions.
- Every `mechanistic_edges` subject and object resolves to the pathway id or a
  declared local participant or reaction.
- Every edge predicate is in `ALLOWED_EDGE_PREDICATES`.
- All 20 edge ids are unique.
- The 20 YAML edge triples contain no duplicates.
- Every edge cites the declared `gomodel:YeastPathways_PWY3O-123` reference.
- All 37 YAML evidence quote strings are exact substrings of the raw Noctua
  JSON.

## Edge Evidence

The raw Noctua model contains 28 total facts:

- `RO:0002233`: 7 `has_input` facts
- `RO:0002234`: 6 `has_output` facts
- `RO:0002333`: 4 `enabled_by` facts
- `RO:0002413`: 3 causal `precedes` facts
- `RO:0002411`: 0 causal `regulates` facts
- `BFO:0000050`: 4 structural `part_of` facts
- `BFO:0000066`: 4 cellular-location `occurs_in` facts

Projection of every in-scope `RO:0002233`, `RO:0002234`, `RO:0002333`,
`RO:0002413`, and `RO:0002411` fact to YAML triples is exact:

- Missing from YAML: none
- Extra in YAML: none
- Duplicate projected raw edges: none
- Duplicate YAML edges: none
- Dangling projected endpoints: none

The compact SGD GO-CAM export has the same 20 unique molecular projections as
the raw Noctua source:

- `RO:0002233`: 7 normalized `has_input` associations
- `RO:0002234`: 6 normalized `has_output` associations
- `RO:0002333`: 4 normalized `enabled_by` associations
- `RO:0002413`: 3 causal associations
- `RO:0002411`: 0 causal associations

The maintained YAML includes all 20 compact SGD molecular projections and adds
no edge absent from the compact source.

## Completeness

All raw in-scope RO facts project into `mechanistic_edges`.

The only raw Noctua facts intentionally omitted from the YAML are the 8 BFO
facts:

- 4 `BFO:0000050` facts connecting `gomodel:MANNPGUANYLTRANGDP-RXN`,
  `gomodel:2.4.1.83-RXN`, `gomodel:PHOSMANMUT-RXN`, and
  `gomodel:MANNPISOM-RXN` to
  `gomodel:YeastPathways_PWY3O-123/YeastPathways_PWY3O-123`
- 4 `BFO:0000066` facts connecting the same reaction nodes to cytosol
  location individuals

The compact SGD source carries the same 4 `part_of` associations to
`GO:0006013` and 4 `occurs_in` associations to `GO:0005829`, and those
BFO-derived facts are absent from
`data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml` and
`pages/records/gomodel_YeastPathways_PWY3O-123.html`. An exact
`rg --no-ignore --hidden` search of those two files for `BFO:0000050`,
`BFO:0000066`, `GO:0006013`, `GO:0005829`, `lociGO`, and the raw
`reaction_*_location` node prefix found no leaks.

The generated page `pages/records/gomodel_YeastPathways_PWY3O-123.html`
contains 20 edge list items that match the YAML edge triples in order, and its
`title` and `h1` match the YAML label.

The generated `pages/browse.html` entry matches the YAML label,
identifier-derived page path, and `20 mechanistic edges` count.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If `data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml` changes,
rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

If the record is regenerated from
`/private/tmp/sgd-yeast-gocams/YeastPathways_PWY3O-123.json`, also recompare
the output against `/private/tmp/gocam-noctua/YeastPathways_PWY3O-123.json` so
all 7 inputs, 6 outputs, 4 enabled-by associations, and 3 causal precedences
stay represented.

## Additional Notes

No GitHub issues should be filed.

Finding counts:

- Blocker: 0
- Major: 0
- Minor: 0
