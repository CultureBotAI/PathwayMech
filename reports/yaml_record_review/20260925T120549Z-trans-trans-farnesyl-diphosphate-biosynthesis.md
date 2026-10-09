# YAML Record Review: trans, trans-farnesyl diphosphate biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: `data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml`
- Started UTC: 2026-09-25T12:05:49Z
- Finished UTC: 2026-09-25T12:05:49Z
- Verdict: Pass. No blocker, major, or minor findings.

## Target

Reviewed exactly one maintained YAML record:
`data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml`.

PR metadata was verified with GitHub:

- PR: #121, `Add trans,trans-farnesyl diphosphate GO-CAM record`
- State: open, non-draft
- Base: `main`
- Head branch: `add-gocam-farnesyl-diphosphate-biosynthesis`
- Head OID: `c881932c11cd07cd79a5d81829f4283113cc097c`
- Files: added the target YAML, added `pages/records/gomodel_YeastPathways_PWY-5123.html`, and modified `pages/browse.html`

Local checkout verification:

- Current branch: `add-gocam-farnesyl-diphosphate-biosynthesis`
- Local `HEAD`: `c881932c11cd07cd79a5d81829f4283113cc097c`

Maintained YAML identity:

- `id`: `gomodel:YeastPathways_PWY-5123`
- `label`: `trans, trans-farnesyl diphosphate biosynthesis`
- `pathway_type`: `lipid-biosynthesis`
- `taxa`: 1
- `participants`: 7
- `reactions`: 3
- `mechanistic_edges`: 15
- `references`: 1

## Validation

All requested read-only gates passed at local `HEAD`:

- `just validate`: passed; validated 5 Claude skills, 104 pathway records, 4,682 evidence blocks, 12 source records, 6 documentation files, and the deep-research report contract.
- `just test`: passed; 34 tests passed.
- `just lint`: passed; `ruff check .` reported `All checks passed!`.
- `git diff --check`: passed with no whitespace errors.

## Identity and Grounding

The maintained record denotes the requested SGD GO-CAM pathway.

- `/private/tmp/gocam-noctua/YeastPathways_PWY-5123.json` is the full GO-CAM export. It has `id` `gomodel:YeastPathways_PWY-5123`, 39 `individuals`, and 21 raw `facts`.
- `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-5123.json` is the compact SGD projection. It has `id` `gomodel:YeastPathways_PWY-5123`, title `<i>trans, trans</i>-farnesyl diphosphate biosynthesis - imported from: Saccharomyces Genome Database`, taxon `NCBITaxon:559292`, 3 `activities`, and 13 `objects`.
- The two raw files are not byte-identical and not structurally identical: the full Noctua export contains `individuals` and `facts`, while the compact SGD file contains `activities` and `objects`. Both identify the same `gomodel:YeastPathways_PWY-5123` model.
- The three local reactions match the raw activity identifiers `gomodel:GPPSYN-RXN`, `gomodel:FPPSYN-RXN`, and `gomodel:IPPISOM-RXN`.
- The seven local participants match the compact SGD object CURIEs and the class types on the full Noctua instance nodes used by the raw facts: `SGD:S000003703`, `SGD:S000006038`, `CHEBI:128769`, `CHEBI:175763`, `CHEBI:29888`, `CHEBI:57623`, and `CHEBI:58057`.

Hidden-and-ignored duplicate searches used `rg --no-ignore --hidden` across
the repository with `.git` and `.venv` excluded.

- `YeastPathways_PWY-5123`: only the target YAML and `pages/browse.html` mention this exact text; `pages/records/gomodel_YeastPathways_PWY-5123.html` was also present by filename.
- `PWY-5123`: only the target YAML and `pages/browse.html` mention this exact text.
- `trans, trans-farnesyl diphosphate biosynthesis`: only the target YAML, generated record page, and browse row mention the exact label.
- `GPPSYN-RXN`: exact token hits are limited to this pathway plus the neighboring hexaprenyl-diphosphate GO-CAM record/page, where the same upstream geranyl-diphosphate synthase step is reused.
- `FPPSYN-RXN`: exact token hits are limited to this pathway plus the neighboring hexaprenyl-diphosphate GO-CAM record/page, where the same farnesyl-diphosphate synthase step is reused.
- `IPPISOM-RXN`: exact token hits are limited to this pathway plus the neighboring mevalonate-pathway record and IPPSYN generated page, where the same isopentenyl-diphosphate isomerase step is reused.

## Graph and Local References

The local graph is internally closed.

- Every `mechanistic_edges` subject and object resolves to the record id or a node declared in `taxa`, `participants`, or `reactions`.
- Every edge predicate is in `ALLOWED_EDGE_PREDICATES`.
- Every evidence `reference_id` resolves to the sole local reference, `gomodel:YeastPathways_PWY-5123`.
- Edge IDs are unique.

Generated artifact consistency:

- `pages/records/gomodel_YeastPathways_PWY-5123.html` renders the same label, description, and 15 edge statements in the same order as the YAML.
- `pages/browse.html` contains the expected row: `gomodel:YeastPathways_PWY-5123 - 15 mechanistic edges`.

Hidden-and-ignored leak searches for `BFO:0000050`, `BFO:0000066`,
`GO:0045337`, `GO:0005829`, `lociGO`, and `reaction_` were run against the
target YAML and generated record page. None of those raw GO-CAM part-of or
location terms leaked into either file.

## Edge Evidence

Every raw GO-CAM relation requested for projection is present in the YAML, with
no extra YAML mechanistic edges.

Full Noctua export, `/private/tmp/gocam-noctua/YeastPathways_PWY-5123.json`:

- 3 raw `RO:0002333` enabled-by facts all map to YAML `enables` edges.
- 6 raw `RO:0002233` input facts all map to YAML `consumes` edges.
- 4 raw `RO:0002234` output facts all map to YAML `produces` edges.
- 2 raw `RO:0002413` causal facts all map to YAML `precedes` edges.
- Total relevant raw RO facts: 15.
- Total YAML mechanistic edges: 15.
- Full export facts missing from YAML: none.
- YAML edges missing from the full export: none.

Compact SGD export, `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-5123.json`:

- `enabled_by` coverage: all 3 compact gene-product associations are in YAML.
- `has_input` coverage: all 6 compact input associations are in YAML.
- `has_output` coverage: all 4 compact output associations are in YAML.
- `causal_associations` coverage: both compact `RO:0002413` associations are in YAML.
- Total compact associations: 15.
- Compact associations missing from YAML: none.
- YAML edges missing from compact SGD: none.

Exact quote coverage:

- The 15 YAML edges contain 28 evidence quote snippets.
- All 28 snippets occur exactly in a minified serialization of
  `/private/tmp/gocam-noctua/YeastPathways_PWY-5123.json`.

## Completeness

None found.

The full Noctua file also carries three raw `BFO:0000050` part-of facts to the
pathway process and three raw `BFO:0000066` occurs-in facts to `GO:0005829`.
The compact file represents the same biological-process and cellular-component
associations as `part_of` and `occurs_in` on each of the three activities. Those
relations are outside PathwayMech's allowed mechanistic-edge predicates and
were correctly omitted from this record.

## Findings

None found.

- Blocker: 0
- Major: 0
- Minor: 0

## Recommended Edits

None.

## Follow-up Checks

Before merge, rerun the same full-corpus read-only gates:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

No generated page refresh is required for the reviewed commit; the generated
record page and browse row already match the maintained YAML.

## Additional Notes

No GitHub issue should be filed.
