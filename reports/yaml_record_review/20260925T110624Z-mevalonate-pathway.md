# YAML Record Review: mevalonate pathway

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/mevalonate-pathway.yaml
- Started UTC: 2026-09-25 11:06:24 UTC
- Finished UTC: 2026-09-25 11:06:40 UTC
- Verdict: Pass. No blocker, major, or minor findings.

## Target

Reviewed PR #111, `Add mevalonate GO-CAM`, on branch
`add-gocam-mevalonate` against `main`.

The PR changes exactly the expected three files for this import:

- `data/pathways/mevalonate-pathway.yaml`
- `pages/records/gomodel_YeastPathways_IPPSYN-PWY.html`
- `pages/browse.html`

The maintained YAML record resolves to:

- `id`: `gomodel:YeastPathways_IPPSYN-PWY`
- `label`: `mevalonate pathway`
- `pathway_type`: `lipid-biosynthesis`
- `taxa`: `NCBITaxon:559292`, Saccharomyces cerevisiae S288C
- 25 participants, 7 reaction nodes, 40 mechanistic edges, and 1 declared
  reference

The raw source was
`/private/tmp/gocam-noctua/YeastPathways_IPPSYN-PWY.json`. The compact SGD
GO-CAM source was
`/private/tmp/sgd-yeast-gocams/YeastPathways_IPPSYN-PWY.json`.

## Validation

All requested validation gates passed:

- `just validate`
  - `validated 5 Claude skills`
  - `validated 94 pathway records`
  - `checked 3965 evidence blocks`
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

The raw Noctua model and compact SGD source both identify the same model as
`gomodel:YeastPathways_IPPSYN-PWY`. The compact source title is
`mevalonate pathway - imported from: Saccharomyces Genome Database`, and its
taxon is `NCBITaxon:559292`, matching the YAML record's identifier, pathway
label, and Saccharomyces cerevisiae S288C taxon scope.

Duplicate/identity searches used `rg --no-ignore --hidden` while excluding
`.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.

- An exact `data/pathways/*.yaml` search for
  `gomodel:YeastPathways_IPPSYN-PWY` found only
  `data/pathways/mevalonate-pathway.yaml`.
- An exact duplicate search for
  `YeastPathways_IPPSYN-PWY|IPPSYN-PWY|PWY-922|mevalonate pathway`, excluding
  `data/pathways/mevalonate-pathway.yaml`, found no other records under
  `data/pathways/`.
- A repository-wide search for
  `YeastPathways_IPPSYN-PWY|IPPSYN-PWY|SGD_PWY:PWY-922|PWY-922|mevalonate pathway`
  matched only the target YAML, its generated record page, and the generated
  browse index before this report was written.

No identity collision or duplicate pathway record was found.

## Graph and Local References

The YAML graph is internally closed:

- Every `mechanistic_edges` subject and object resolves to the pathway id or to
  a declared local participant or reaction.
- Every edge predicate is in `ALLOWED_EDGE_PREDICATES`.
- Every edge cites the declared `gomodel:YeastPathways_IPPSYN-PWY` reference.
- The 40 YAML edge triples contain no duplicates.
- All 80 YAML evidence quote strings are exact substrings of the raw Noctua
  JSON.

## Edge Evidence

The raw Noctua model contains 54 total facts:

- `RO:0002333`: 8 `enabled_by` facts
- `RO:0002233`: 14 `has_input` facts
- `RO:0002234`: 18 `has_output` facts
- `RO:0002413`: 0 causal precedes facts
- `RO:0002411`: 0 causal regulates facts
- `BFO:0000050`: 7 structural `part_of` facts
- `BFO:0000066`: 7 cytosol `occurs_in` facts

Projection of the 40 in-scope `RO:0002333`, `RO:0002233`, and `RO:0002234`
facts to YAML triples is exact:

- Missing from YAML: none
- Extra in YAML: none
- Duplicate projected raw edges: none
- Duplicate YAML edges: none
- Dangling projected endpoints: none

The compact SGD GO-CAM source has the same 40 unique molecular projections as
the raw source. It has 46 total activity projections because
`gomodel:1.1.1.34-RXN` appears once for `HMG2` and once for `HMG1`, duplicating
six substrate/product projections before uniqueing. The YAML follows the raw
Noctua fact set and does not duplicate those substrate/product edges.

## Completeness

All raw in-scope RO facts project into `mechanistic_edges`.

The only raw facts intentionally omitted from the YAML are the 14 BFO facts:

- 7 `BFO:0000050` facts connecting reaction nodes to the model pathway
  individual of type `GO:0008299`
- 7 `BFO:0000066` facts connecting reaction nodes to cytosol location
  individuals of type `GO:0005829`

No other raw facts are absent from the curated YAML.

The generated page
`pages/records/gomodel_YeastPathways_IPPSYN-PWY.html` contains 40 edge list
items that exactly match the YAML edge triples in order, and its title, `h1`,
and description match the YAML.

The generated `pages/browse.html` entry exactly matches the YAML label,
identifier-derived page path, and `40 mechanistic edges` count.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

If `data/pathways/mevalonate-pathway.yaml` changes, rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

If the GO-CAM import is regenerated from
`/private/tmp/sgd-yeast-gocams/YeastPathways_IPPSYN-PWY.json`, also recompare
the output against `/private/tmp/gocam-noctua/YeastPathways_IPPSYN-PWY.json`
so the duplicate compact `gomodel:1.1.1.34-RXN` activity does not introduce
duplicate substrate or product edges.

## Additional Notes

No GitHub issues should be filed.

Finding counts:

- Blocker: 0
- Major: 0
- Minor: 0
