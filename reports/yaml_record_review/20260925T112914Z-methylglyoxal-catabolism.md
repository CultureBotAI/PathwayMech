# YAML Record Review: methylglyoxal catabolism

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/methylglyoxal-catabolism.yaml
- Started UTC: 2026-09-25 11:29:14 UTC
- Finished UTC: 2026-09-25 11:29:14 UTC
- Verdict: Pass. No blocker, major, or minor findings.

## Target

Reviewed PR #115, `Add methylglyoxal catabolism GO-CAM`, on branch
`add-gocam-methylglyoxal-catabolism` against `main`.

PR metadata verified through `gh pr view 115`:

- State: open
- Draft: false
- Merge state: clean
- Head repository: `CultureBotAI/PathwayMech`
- Base branch: `main`
- Head commit: `20709382eaa7ff34735741a679142a134ccf50ee`

The local checkout was on `add-gocam-methylglyoxal-catabolism` and `HEAD`
matched the PR commit.

The PR changes exactly the expected three files for this import:

- `data/pathways/methylglyoxal-catabolism.yaml`
- `pages/browse.html`
- `pages/records/gomodel_YeastPathways_PWY-901.html`

The maintained YAML record resolves to:

- `id`: `gomodel:YeastPathways_PWY-901`
- `label`: `methylglyoxal catabolism`
- `pathway_type`: `detoxification`
- `taxa`: `NCBITaxon:559292`, Saccharomyces cerevisiae S288C
- 9 participants, 3 reaction nodes, 16 mechanistic edges, and 1 declared
  reference

Raw sources checked:

- `/private/tmp/gocam-noctua/YeastPathways_PWY-901.json`
- `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-901.json`

## Validation

All requested validation gates passed:

- `just validate`
  - `validated 5 Claude skills`
  - `validated 98 pathway records`
  - `checked 4295 evidence blocks`
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
`gomodel:YeastPathways_PWY-901`, has `state` `production`, carries title
`methylglyoxal catabolism - imported from: Saccharomyces Genome Database`, and
annotates `NCBITaxon:559292` as its taxon. Its pathway individual
`gomodel:YeastPathways_PWY-901/YeastPathways_PWY-901` is typed as
`GO:0051596` / `methylglyoxal catabolic process`.

The compact SGD GO-CAM source independently reports:

- `id`: `gomodel:YeastPathways_PWY-901`
- `title`: `methylglyoxal catabolism - imported from: Saccharomyces Genome Database`
- `taxon`: `NCBITaxon:559292`
- `status`: `production`
- 3 activities, 14 ontology objects, 1 top-level provenance block, and 3
  comments

Duplicate and identity searches used `rg --no-ignore --hidden` while excluding
only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.

- Exact repository-wide searches for `gomodel:YeastPathways_PWY-901`,
  `YeastPathways_PWY-901`, `PWY-901`, `methylglyoxal catabolism`,
  `GLYOXI-RXN`, and `GLYOXII-RXN` matched the new target YAML, the new
  generated record page, and the new generated browse entry before this report
  was written.
- Exact repository-wide searches for `GO:0051596` and `SGD_PWY:PWY-901` found
  no matches before this report was written.

No identity collision or duplicate pathway record was found.

## Graph and Local References

The YAML graph is internally closed:

- The record declares 14 local nodes: the record id, 1 taxon, 9 participants,
  and 3 reactions.
- Every `mechanistic_edges` subject and object resolves to the pathway id or a
  declared local participant or reaction.
- Every edge predicate is in `ALLOWED_EDGE_PREDICATES`.
- All 16 edge ids are unique.
- The 16 YAML edge triples contain no duplicates.
- Every edge cites the declared `gomodel:YeastPathways_PWY-901` reference.
- All 32 YAML evidence quote strings are exact substrings of the raw Noctua
  JSON.

## Edge Evidence

The raw Noctua model contains 22 total facts:

- `RO:0002233`: 6 `has_input` facts
- `RO:0002234`: 7 `has_output` facts
- `RO:0002333`: 3 `enabled_by` facts
- `RO:0002413`: 0 causal `precedes` facts
- `RO:0002411`: 0 causal `regulates` facts
- `BFO:0000050`: 3 structural `part_of` facts
- `BFO:0000066`: 3 cellular-location `occurs_in` facts

Projection of every in-scope `RO:0002233`, `RO:0002234`, `RO:0002333`,
`RO:0002413`, and `RO:0002411` fact to YAML triples is exact:

- Missing from YAML: none
- Extra in YAML: none
- Duplicate projected raw edges: none
- Duplicate YAML edges: none
- Dangling projected endpoints: none

The compact SGD GO-CAM export has the same unique molecular projections as the
raw Noctua source:

- `RO:0002233`: 6 normalized `has_input` associations
- `RO:0002234`: 7 normalized `has_output` associations
- `RO:0002333`: 3 normalized `enabled_by` associations
- `RO:0002413`: 0 causal associations
- `RO:0002411`: 0 causal associations

The maintained YAML includes all 16 compact SGD molecular projections and adds
no edge that is absent from the compact source.

## Completeness

All raw in-scope RO facts project into `mechanistic_edges`.

The only raw Noctua facts intentionally omitted from the YAML are the 6 BFO
facts:

- 3 `BFO:0000050` facts connecting `gomodel:GLYOXI-RXN`,
  `gomodel:GLYOXII-RXN`, and
  `gomodel:YeastPathways_PWY-901/6a46ef0600000777` to the model pathway
  individual
- 3 `BFO:0000066` facts connecting the same reaction nodes to cytosol
  location individuals

The compact SGD source carries the same 3 `part_of` and 3 `occurs_in`
associations for the same activities, and those BFO-derived facts are absent
from `data/pathways/methylglyoxal-catabolism.yaml` and
`pages/records/gomodel_YeastPathways_PWY-901.html`. An exact
`rg --no-ignore --hidden` search of those two files for `BFO:0000050`,
`BFO:0000066`, `GO:0005829`, `cytosol`, the raw pathway individual, and the raw
cytosol location node prefix found no leaks.

The generated page `pages/records/gomodel_YeastPathways_PWY-901.html` contains
16 edge list items that exactly match the YAML edge triples in order, and its
`title` and `h1` match the YAML label.

The generated `pages/browse.html` entry matches the YAML label,
identifier-derived page path, and `16 mechanistic edges` count.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If `data/pathways/methylglyoxal-catabolism.yaml` changes, rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

If the record is regenerated from
`/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-901.json`, also recompare the
output against `/private/tmp/gocam-noctua/YeastPathways_PWY-901.json` so the
GLO2 and GLO4 hydroxyacylglutathione hydrolase activities stay represented as
parallel enzymatic activities with distinct enablers.

## Additional Notes

No GitHub issues should be filed.

Finding counts:

- Blocker: 0
- Major: 0
- Minor: 0
