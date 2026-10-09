# YAML Record Review: Glycogen catabolism

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/glycogen-catabolism.yaml
- Started UTC: 2026-09-27T07:01:41Z
- Finished UTC: 2026-09-27T07:03:12Z
- Verdict: Pass

## Target

Reviewed `data/pathways/glycogen-catabolism.yaml`, a new WikiPathways:WP478
record for the supported Saccharomyces cerevisiae GPH1 glycogen
phosphorolysis branch and downstream PGM1/PGM2 phosphoglucomutase conversion.

## Validation

- `just validate`: pass, 148 pathway records, 7,853 evidence blocks, 12 source
  records, 6 documentation files, and the deep-research report contract.
- `just render-pages`: pass, 148 pathway records rendered.
- `just test`: pass, 35 tests.
- `just lint`: pass.
- `git diff --check`: pass.

## Identity and Grounding

The record identity `WikiPathways:WP478` matches the current WikiPathways
Glycogen catabolism GPML map. The local record deliberately keeps only the
WP478 GPH1 phosphorolysis and PGM1/PGM2 conversion segment whose metabolites
and gene products have supported ChEBI and SGD identifiers in the GPML.

## Graph and Local References

All seven mechanistic edges connect the pathway, participant, and reaction
nodes declared in the same YAML file. The two reaction nodes are WP478
interaction identifiers, all participants use supported `CHEBI` or `SGD`
CURIEs, and every edge cites the local `WikiPathways:WP478` reference.

## Edge Evidence

The evidence snippets quote the exact GPML interactions, anchors, data nodes,
and group declaration needed for the maintained edges:

- glycogen input into `id16beba20`
- `e9034` side output from `id16beba20` to glucose-1-phosphate
- GPH1 catalysis through the shared `e9034` anchor
- glucose-1-phosphate conversion to glucose-6-phosphate through `id5442c585`
- PGM1 and PGM2 catalysis through the `e41dc` anchor and `e000d` group

## Completeness

The omitted SGA1 and GDB1 branches are appropriate omissions for this record:
the current GPML grounds their branch metabolites with unsupported CAS or
Wikidata identifiers, and SGA1 itself is present only as an Ensembl xref. Adding
those edges would require either broader identifier support or explicit manual
crosswalk evidence.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

- Re-run `just validate`, `just test`, `just lint`, and `git diff --check`
  after any future WP478 edge expansion.
- Re-run `just render-pages` if `data/pathways/glycogen-catabolism.yaml`
  changes.

## Additional Notes

Duplicate checks for the WP478 identifier, Glycogen catabolism label, branch
reaction identifiers, GPH1/GDB1/PGM accessions, and the WP478 PubMed support
lead used ignored and hidden files before the record was written.
