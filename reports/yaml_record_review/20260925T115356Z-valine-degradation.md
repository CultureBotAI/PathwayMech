# YAML Record Review: valine degradation

- Repository: PathwayMech
- Record: `data/pathways/valine-degradation.yaml`
- Started UTC: 2026-09-25T11:48:00Z
- Finished UTC: 2026-09-25T11:54:06Z
- Verdict: Pass; no blockers, major findings, or minor findings found.

## Target

Reviewed exactly one maintained YAML record:

- File: `data/pathways/valine-degradation.yaml`
- Record id: `gomodel:YeastPathways_PWY3O-4105`
- Label: `valine degradation`
- Description scope: Saccharomyces cerevisiae S288C conversion of L-valine to 3-methyl-2-oxobutanoate, then isobutyraldehyde, then isobutanol
- Pathway type: `amino-acid-degradation`
- Taxa: one local taxon, `NCBITaxon:559292` / Saccharomyces cerevisiae S288C
- Participants: 20 local participants, comprising 9 CHEBI metabolites/cofactors and 11 SGD gene products
- Reactions: 11 local GO-CAM reaction/activity nodes
- Mechanistic edges: 76
- References: one, `gomodel:YeastPathways_PWY3O-4105`

The branch was `add-gocam-valine-degradation` and `HEAD` was
`0d14e07dcb0bbf6f1b83b403a911daf48a5e971f`, matching the requested PR #119
head.

## Validation

All requested read-only validators passed:

- `just validate`
  - validated 5 Claude skills
  - validated 102 pathway records
  - checked 4618 evidence blocks
  - validated 12 source records
  - checked 6 documentation files
  - checked the deep-research report contract
- `just test`
  - 34 passed
- `just lint`
  - `ruff check .`: all checks passed
- `git diff --check`
  - passed with no whitespace errors

No validator was skipped.

## Identity and Grounding

The pathway identity is exact. The maintained record id
`gomodel:YeastPathways_PWY3O-4105` matches both local source files:

- Raw Noctua:
  `/private/tmp/gocam-noctua/YeastPathways_PWY3O-4105.json`
- Compact SGD:
  `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY3O-4105.json`

The compact SGD file identifies the same model as
`gomodel:YeastPathways_PWY3O-4105`, has title
`valine degradation - imported from: Saccharomyces Genome Database`, has
`status: production`, and scopes the model to `NCBITaxon:559292`. The raw
Noctua annotations carry the same title, `state: production`, the same in-taxon
annotation, and the SGD provenance comment for `PWY3O-4105`.

The record preserves the compact model shape: 11 source activities become 11
local reaction nodes. The compact source has 26 GO-CAM objects; the YAML keeps
only the objects needed by mechanistic edges, leaving out source-only evidence,
location, and biological-process objects that are not PathwayMech participants.

No near-miss pathway was conflated with this record. A hidden-and-ignored
repository search for `gomodel:YeastPathways_PWY3O-4105`, `PWY3O-4105`, and
`valine degradation` found only this maintained YAML plus its generated pages.
The similarly named `data/pathways/l-valine-biosynthesis.yaml` is
`MetaCyc:VALSYN-PWY` for Escherichia coli biosynthesis, not a duplicate of the
SGD valine-degradation GO-CAM.

## Graph and Local References

`just validate` confirmed that every mechanistic edge endpoint resolves to the
record id or to a declared taxon, participant, or reaction in the same YAML
file, and that every predicate appears in `ALLOWED_EDGE_PREDICATES` from
`src/pathwaymech/schema.py`.

The reviewed graph has no duplicate YAML edges and uses this predicate
distribution:

- `consumes`: 19
- `enables`: 11
- `precedes`: 24
- `produces`: 22

Every edge cites the sole declared reference,
`gomodel:YeastPathways_PWY3O-4105`. All 128 evidence quotes were present as
exact substrings in the minified raw Noctua JSON file.

The generated page
`pages/records/gomodel_YeastPathways_PWY3O-4105.html` exactly matches
`pathwaymech.cli._record_page()` output for the current YAML record: 6875
bytes expected, 6875 bytes actual, 76 listed edges.

## Edge Evidence

The source-edge projection is complete and exact against both the raw Noctua
facts and the compact SGD activity export:

- YAML `enables`: 11; raw `RO:0002333`: 11; compact `enabled_by`: 11
- YAML `consumes`: 19; raw `RO:0002233`: 19; compact `has_input`: 19
- YAML `produces`: 22; raw `RO:0002234`: 22; compact `has_output`: 22
- YAML `precedes`: 24; raw `RO:0002413`: 24; compact `causal_associations`: 24

There were no `raw minus YAML`, `YAML minus raw`, `compact minus YAML`, or
`YAML minus compact` mechanistic edges after projecting:

- `RO:0002413` to `precedes`
- `RO:0002233` plus the object individual's local type to `consumes`
- `RO:0002234` plus the object individual's local type to `produces`
- `RO:0002333` plus the controller individual's local type to `enables`

The 24 causal `RO:0002413` edges are the explicit isozyme fan-out encoded by
SGD/Noctua, not a PathwayMech expansion bug:

- two branched-chain aminotransferase activities feed three pyruvate
  decarboxylase activities, yielding 6 source causal edges
- three pyruvate decarboxylase activities feed six alcohol dehydrogenase
  activities, yielding 18 source causal edges

The YAML preserves all 24 of those source causal edges and adds none beyond
them.

## Completeness

The record intentionally omits raw GO-CAM containment and location facts that
are not legal PathwayMech mechanistic edges:

- 11 raw `BFO:0000050` facts connecting activities to the GO-CAM biological
  process individual
- 11 raw `BFO:0000066` facts connecting activities to cytosol
- compact `part_of` and `occurs_in` associations for each activity
- raw individual annotations such as `comment: located_in cytosol`

A direct search of the maintained YAML and generated record page for `BFO`,
`GO:0005829`, `occurs`, `located_in`, and `cytosol` found no matches, so these
facts were not accidentally rendered as participants or edges.

Hidden-and-ignored duplicate searches covered the full repository with
`rg --no-ignore --hidden`, excluding only `.git` and `.venv`. Searches for the
model id, exact label, `PWY3O-4105`, `SGD_PWY:PWY3O-4105`, representative
reaction ids `RXN3O-4133`, `RXN3O-4141`, and
`BRANCHED-CHAINAMINOTRANSFERVAL-RXN`, and representative SGD grounding
`SGD:S000004034` found no second maintained `data/pathways/` record for this
GO-CAM.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for the reviewed record. If the YAML changes later, refresh the
generated page with `just render-pages` and rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

## Additional Notes

The current worktree was clean before this report was written.
