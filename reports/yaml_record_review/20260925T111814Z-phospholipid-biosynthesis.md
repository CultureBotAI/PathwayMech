# YAML Record Review: phospholipid biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/phospholipid-biosynthesis.yaml
- Started UTC: 2026-09-25T11:18:14Z
- Finished UTC: 2026-09-25T11:18:18Z
- Verdict: Pass; no blocker, major, or minor findings.

## Target

Reviewed PR #113, "Add phospholipid biosynthesis GO-CAM".

- PR metadata: open, not draft, `CLEAN`, `add-gocam-phospholipid-biosynthesis` into `main`.
- PR head: `17a1a6c9df911654bcc9aa6d519460b5dd4389a3`.
- PR base: `42c40a9d45233c85dc1cc7a5445c4da5e425d758`.
- PR diff: 647 insertions and 0 deletions across exactly 3 files.
- Maintained YAML added: `data/pathways/phospholipid-biosynthesis.yaml`, 576 lines.
- Generated pages changed: `pages/browse.html` and `pages/records/gomodel_YeastPathways_PHOSLIPSYN2-PWY-1.html`.

Resolved exactly one target under `data/pathways/`:

- `id`: `gomodel:YeastPathways_PHOSLIPSYN2-PWY-1`
- `label`: `phospholipid biosynthesis`
- `pathway_type`: `lipid-biosynthesis`
- taxa: 1, `NCBITaxon:559292` / `Saccharomyces cerevisiae S288C`
- participants: 27
- reactions: 9
- mechanistic edges: 56
- references: 1, `gomodel:YeastPathways_PHOSLIPSYN2-PWY-1`

The source files checked were:

- `/private/tmp/gocam-noctua/YeastPathways_PHOSLIPSYN2-PWY-1.json`
- `/private/tmp/sgd-yeast-gocams/YeastPathways_PHOSLIPSYN2-PWY-1.json`

The source JSONs were not byte-identical, as expected for raw Noctua versus normalized SGD GO-CAM exports:

- raw Noctua SHA-256: `44b6b02246f073f531ddcd7292c755c75a10e3fef7622a4fe3f670a101282ecc`
- SGD normalized SHA-256: `649bb6ddd5fb0ec4b2fe5683f86be6ce0dc4805dd0ca527070bc0f23d18e64c6`

## Validation

All requested read-only validation passed.

- `just validate`
  - validated 5 Claude skills
  - validated 96 pathway records
  - checked 4,181 evidence blocks
  - validated 12 source records
  - checked 6 documentation files
  - checked deep-research report contract
- `just test`
  - 34 tests passed
- `just lint`
  - Ruff passed with no findings
- `git diff --check`
  - passed with no whitespace errors

## Identity and Grounding

No identity defect found.

- The YAML record id is the raw GO-CAM model id: `gomodel:YeastPathways_PHOSLIPSYN2-PWY-1`.
- The raw Noctua title is `phospholipid biosynthesis - imported from: Saccharomyces Genome Database`.
- The raw Noctua metadata points back to the SGD pathway import URL for `PHOSLIPSYN2-PWY-1`.
- Both source forms scope the model to `NCBITaxon:559292`.
- The maintained YAML declares all 9 activity nodes from the normalized SGD `activities` list as `gomodel:` reactions.
- The maintained YAML declares the 27 local CHEBI/SGD class ids reached through `RO:0002233`, `RO:0002234`, and `RO:0002333` raw fact objects as participants.

The hidden-and-ignored duplicate search included ignored and hidden files and excluded only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.

- `YeastPathways_PHOSLIPSYN2-PWY-1`: only the target YAML and its generated HTML page/browse references were found.
- `PHOSLIPSYN2-PWY`: only the target YAML and its generated HTML page/browse references were found.
- `phospholipid biosynthesis`: only the target YAML and its generated HTML page/browse references were found.
- `gomodel_YeastPathways_PHOSLIPSYN2-PWY-1`: only `pages/browse.html` links to the generated record page.
- `phospholipid-biosynthesis`: no repository matches.
- `SGD_PWY:PHOSLIPSYN2-PWY-1`: no repository matches.
- `CARDIOLIPSYN-RXN`: only the target YAML and its generated record page were found.
- `phosphatidylserine decarboxylase`: the target YAML and generated page were found; the only other maintained hit was `data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml`, which shares a PSD reaction label but denotes the narrower phosphatidylethanolamine biosynthesis pathway.

## Graph and Local References

No graph or local-reference defect found.

- `just validate` accepted every local endpoint, predicate, evidence block, evidence quote length, reference id, and CURIE prefix.
- All 56 edge ids are unique.
- Every `mechanistic_edges` endpoint is the pathway id or one of the declared local taxon, participant, or reaction ids.
- All 56 edges use the allowed local predicates generated from raw RO facts:
  - `RO:0002233` -> `consumes`
  - `RO:0002234` -> `produces`
  - `RO:0002333` -> `enables`
  - `RO:0002413` -> `precedes`
  - `RO:0002411` -> `regulates`; not present in this source model
- The single declared reference, `gomodel:YeastPathways_PHOSLIPSYN2-PWY-1`, is cited by all 56 mechanistic edges.

## Edge Evidence

No edge-evidence defect found.

The exact raw Noctua fact projection was checked for all projectable predicates.

- Raw Noctua fact counts:
  - `BFO:0000050`: 9
  - `BFO:0000066`: 9
  - `RO:0002233`: 17
  - `RO:0002234`: 22
  - `RO:0002333`: 9
  - `RO:0002413`: 8
  - `RO:0002411`: 0
- The raw Noctua export has 74 total facts.
- The 56 raw facts with `RO:0002233`, `RO:0002234`, `RO:0002333`, `RO:0002413`, or `RO:0002411` project to exactly the same 56 `(subject, predicate, object)` triples in the YAML.
- Every YAML edge includes an exact raw fact quote present in `/private/tmp/gocam-noctua/YeastPathways_PHOSLIPSYN2-PWY-1.json`.
- Every raw projectable fact is quoted exactly once as the first evidence quote for one YAML edge.
- Every `RO:0002233`, `RO:0002234`, and `RO:0002333` edge also includes an exact raw individual-type quote whose individual id is the fact object and whose type class is the CHEBI or SGD participant id projected into YAML.
- Each `RO:0002413` causal edge has exactly one raw fact quote and no extra type quote.
- The normalized SGD source also projects to the same 56 YAML triples:
  - `enabled_by`: 9
  - `has_input`: 17
  - `has_output`: 22
  - `RO:0002413` causal associations: 8

Only placement facts are intentionally omitted from YAML:

- `BFO:0000050`: 9 `part_of` facts linking each activity to `GO:0008654`.
- `BFO:0000066`: 9 `occurs_in` facts linking each activity to a cellular component.
- There were no other raw Noctua predicates absent from the YAML projection.

## Completeness

No completeness defect found for a raw Noctua GO-CAM projection.

- The maintained YAML covers all 9 activities in the normalized SGD source.
- The maintained YAML covers all 56 RO input, output, enabler, and causal facts in the raw Noctua source.
- The 18 omitted BFO placement facts are outside the current PathwayMech edge vocabulary and are intentional omissions rather than lost reactions, metabolites, enzymes, or causal steps.

Generated-page completeness also checked out.

- `pages/browse.html` links to `records/gomodel_YeastPathways_PHOSLIPSYN2-PWY-1.html` and reports `gomodel:YeastPathways_PHOSLIPSYN2-PWY-1 - 56 mechanistic edges`.
- `pages/records/gomodel_YeastPathways_PHOSLIPSYN2-PWY-1.html` renders exactly 56 edge list items.
- The rendered record-page edge list matches the YAML `mechanistic_edges` list in count, order, subject, predicate, and object.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None required for this PR.

If future edits touch this record or the GO-CAM source projection, rerun:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

## Additional Notes

- I did not edit `data/pathways/phospholipid-biosynthesis.yaml`.
- I did not regenerate or hand-edit `pages/browse.html` or `pages/records/gomodel_YeastPathways_PHOSLIPSYN2-PWY-1.html`.
- I did not create or mutate any GitHub issues, PR comments, labels, or settings.
- No GitHub issues should be filed from this review.
