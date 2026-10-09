# YAML Record Review: L-lysine biosynthesis IV

- Repository: CultureBotAI/PathwayMech
- Record: `data/pathways/l-lysine-biosynthesis-iv.yaml`
- Started UTC: 2026-09-25T11:00:00Z
- Finished UTC: 2026-09-25T11:11:45Z
- Verdict: Pass. No blockers, majors, or minors found.

## Target

Reviewed PR #112, `Add L-lysine biosynthesis IV GO-CAM`, on branch
`add-gocam-lysine-aminoadipate`, commit
`45bea6f76c62bb6ca250f20918d37a758f60023a`.

The target file resolves unambiguously to
`data/pathways/l-lysine-biosynthesis-iv.yaml`.

- Record id: `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2`
- Label: `L-lysine biosynthesis IV`
- Pathway type: `amino-acid-biosynthesis`
- Taxon: `NCBITaxon:559292`, `Saccharomyces cerevisiae S288C`
- Participants: 27
- Reactions: 9
- Mechanistic edges: 56
- References: 1, `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2`

PR #112 adds exactly this maintained YAML record, modifies `pages/browse.html`,
and adds `pages/records/gomodel_YeastPathways_LYSINE-AMINOAD-PWY-2.html`.

The duplicate/identity searches used `rg --no-ignore --hidden` with `.git`,
`.venv`, `.pytest_cache`, and `.ruff_cache` excluded. Exact searches for
`gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2`, `LYSINE-AMINOAD-PWY-2`, and
`L-lysine biosynthesis IV` found only this YAML record plus the generated
detail page and browse-index row.

## Validation

All requested validators passed.

- `just validate`
  - Validated 5 Claude skills.
  - Validated 95 pathway records.
  - Checked 4077 evidence blocks.
  - Validated 12 source records.
  - Checked 6 documentation files.
  - Checked the deep-research report contract.
- `just test`
  - 34 tests passed.
- `just lint`
  - Ruff reported `All checks passed!`.
- `git diff --check`
  - Passed with no whitespace errors.

## Identity and Grounding

The maintained record matches both supplied GO-CAM sources.

- Raw Noctua source:
  `/private/tmp/gocam-noctua/YeastPathways_LYSINE-AMINOAD-PWY-2.json`
  - `id`: `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2`
  - `title` annotation:
    `L-lysine biosynthesis IV - imported from: Saccharomyces Genome Database`
- Compact SGD GO-CAM source:
  `/private/tmp/sgd-yeast-gocams/YeastPathways_LYSINE-AMINOAD-PWY-2.json`
  - `id`: `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2`
  - `title`: `L-lysine biosynthesis IV - imported from: Saccharomyces Genome Database`
  - `taxon`: `NCBITaxon:559292`

The YAML intentionally normalizes the source title to the pathway label
`L-lysine biosynthesis IV`, keeps the GO-CAM model id as the record id, and
keeps the compact SGD taxon as the sole local taxon node.

## Graph and Local References

The local graph is internally closed.

- All 56 `mechanistic_edges` ids are unique.
- All 56 `(subject, predicate, object)` triples are unique.
- Every edge endpoint resolves to the record id or a local node in `taxa`,
  `participants`, or `reactions`.
- Every predicate is one of the schema predicates.
- Every edge cites the declared
  `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2` reference.
- No raw in-scope fact projected to an undeclared local participant or
  reaction.

The compact source has 9 activities and projects to 56 unique input, output,
and enabled-by edges. The YAML has the same 56 unique edges: no compact-source
extras and no compact-source misses.

The generated detail page exactly matches `pathwaymech.cli._record_page()` for
the validated YAML record. The generated browse index contains the expected
row:

```html
<li><a href="records/gomodel_YeastPathways_LYSINE-AMINOAD-PWY-2.html"><strong>L-lysine biosynthesis IV</strong><span>gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2 - 56 mechanistic edges</span></a></li>
```

## Edge Evidence

The raw Noctua source contains 74 facts:

- `RO:0002234`: 24 output facts
- `RO:0002233`: 23 input facts
- `RO:0002333`: 9 enabled-by facts
- `BFO:0000050`: 9 structural `part_of` facts
- `BFO:0000066`: 9 cytosol `occurs_in` facts

The source contains no `RO:0002413` or `RO:0002411` causal facts.

All 56 in-scope `RO:0002234`, `RO:0002233`, and `RO:0002333` facts project
exactly to the YAML:

- 56 raw in-scope facts
- 56 unique raw projections
- 56 YAML edges
- 56 unique YAML edges
- 0 raw projections missing from YAML
- 0 YAML edges absent from the raw source
- 0 duplicate raw projections
- 0 duplicate YAML triples

For every YAML edge, the first evidence quote exactly matches its raw Noctua
fact substring:

```json
"subject":"...","property":"...","property-label":"...","object":"..."
```

For every YAML edge, the second evidence quote exactly matches the raw Noctua
individual typing substring for the fact object:

```json
"id":"...","type":[{"type":"class","id":"..."
```

No edge has a stale quote, a quote from a different raw fact, a quote from a
different object individual, extra evidence, or missing evidence.

## Completeness

No in-scope raw source facts are missing from the curated record, and the
curated record does not add any in-scope input, output, enabled-by, upstream,
or regulation edge that is absent from the raw source.

The only raw Noctua facts intentionally omitted from the YAML are the expected
BFO structural and location facts:

- 9 `BFO:0000050` facts from activities to the model pathway individual,
  typed as `GO:0009085`
- 9 `BFO:0000066` facts from activities to cytosol location individuals,
  typed as `GO:0005829`

There are no other raw fact predicates in the model.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required for PR #112. No GitHub issues should be filed for this record
review.

## Additional Notes

This review did not edit the maintained YAML record and did not regenerate or
hand-edit `pages/`.
