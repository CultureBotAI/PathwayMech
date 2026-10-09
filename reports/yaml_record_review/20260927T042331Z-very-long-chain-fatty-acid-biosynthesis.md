# YAML Record Review: very long chain fatty acid biosynthesis I

- Repository: CultureBotAI/PathwayMech
- Record: `data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml`
- Started UTC: 2026-09-27T04:23:31Z
- Finished UTC: 2026-09-27T04:23:31Z
- Verdict: Pass; no blocker, major, or minor findings.

## Target

PR #180 adds `gomodel:YeastPathways_PWY-5080-1` as
`very long chain fatty acid biosynthesis I`.

The maintained YAML declares:

- 1 taxon: `NCBITaxon:559292`
- 16 participants
- 5 reaction/activity nodes
- 27 mechanistic edges
- 1 source reference: `gomodel:YeastPathways_PWY-5080-1`

## Validation

Passed:

- `uv run python /private/tmp/audit_vlcfa.py`
- `uv run pathwaymech-validate`
- `just render-pages`
- `just validate`
- `just test`
- `just lint`
- `git diff --check`
- `git diff --cached --check`

No validator was skipped.

## Identity and Grounding

The YAML `id` exactly matches the refreshed compact SGD GO-CAM model
`gomodel:YeastPathways_PWY-5080-1`.

The compact source at
`/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-5080-1.json` reports:

- `id`: `gomodel:YeastPathways_PWY-5080-1`
- `title`: `very long chain fatty acid biosynthesis I - imported from: Saccharomyces Genome Database`
- `taxon`: `NCBITaxon:559292`
- 5 activities

The raw Noctua source at
`/private/tmp/gocam-noctua/YeastPathways_PWY-5080-1.json` reports the matching
model `id` and title and includes the source comment
`https://pathway.yeastgenome.org/YEAST/NEW-IMAGE?object=PWY-5080-1`.

Exact duplicate searches used `rg --no-ignore --hidden` across the repository,
excluding only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`. Searches for
`gomodel:YeastPathways_PWY-5080-1`, `YeastPathways_PWY-5080-1`,
`very long chain fatty acid biosynthesis I`, `RXN3O-9811`, `RXN3O-9812`,
`RXN3O-9813`, and `RXN3O-9814` found only this new YAML record and its generated
HTML after the PR change.

The closest existing fatty-acid record,
`data/pathways/fatty-acid-elongation.yaml`, is a distinct
`gomodel:YeastPathways_FASYN-ELONG2-PWY` ACP/palmitoyl-CoA elongation model and
does not duplicate the `PWY-5080-1` very-long-chain acyl-CoA route.

## Graph and Local References

The local graph is valid. `uv run pathwaymech-validate` accepted 146 pathway
records, including this YAML, and therefore confirmed that every edge endpoint
resolves to the record itself, a local participant, or a local reaction, every
edge predicate is supported, every evidence `reference_id` is declared, and all
CURIE prefixes are accepted.

The record declares only nodes that appear in retained edges. The five reaction
nodes are the compact GO-CAM activities:

- `gomodel:RXN3O-9811`
- `gomodel:RXN3O-9812`
- `gomodel:RXN3O-9813`
- `gomodel:RXN3O-9814`
- `gomodel:YeastPathways_PWY-5080-1/6a2b236300005423`

## Edge Evidence

`/private/tmp/audit_vlcfa.py` reconstructed the evidenced compact edge set as:

- 5 `enabled_by` edges
- 10 `has_input` edges
- 11 `has_output` edges
- 1 `RO:0002411` causal edge

Those 27 expected compact associations exactly match the 27 YAML
`mechanistic_edges`. Every YAML quote is an exact substring of
`/private/tmp/gocam-noctua/YeastPathways_PWY-5080-1.json`.

## Completeness

No material completeness defect found.

The compact SGD GO-CAM currently includes one term-bearing ELO3 output
association from `gomodel:YeastPathways_PWY-5080-1/6a2b236300005423` to
`CHEBI:15489` with an empty evidence array. That raw fact has no `evidence`
annotation, and the YAML intentionally omits it instead of citing unsupported
contributor/date metadata.

The generated page
`pages/records/gomodel_YeastPathways_PWY-5080-1.html` renders all 27 YAML edges,
and `pages/browse.html` links to that page with `27 mechanistic edges`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

Before merge, rerun:

```bash
uv run python /private/tmp/audit_vlcfa.py
just validate
just test
just lint
git diff --check
```

## Additional Notes

The ignored-and-hidden duplicate searches intentionally excluded generated and
local-environment directories only: `.git`, `.venv`, `.pytest_cache`, and
`.ruff_cache`.
