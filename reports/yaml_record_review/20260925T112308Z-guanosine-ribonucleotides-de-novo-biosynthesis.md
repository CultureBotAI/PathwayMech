# YAML Record Review: guanosine ribonucleotides de novo biosynthesis

- Repository: CultureBotAI/PathwayMech
- Record: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
- Started UTC: 2026-09-25T11:20:46Z
- Finished UTC: 2026-09-25T11:23:08Z
- Verdict: Pass; no blocker, major, or minor findings.

## Target

Reviewed PR #114, "Add guanosine ribonucleotides GO-CAM".

- PR metadata: open, not draft, `CLEAN`, `add-gocam-guanosine-ribonucleotides` into `main`.
- PR head: `0bd65e80cdef34f22987c4df59765ef207998732`.
- PR base: `a0c4768ed58b5546d077bd84a1373e2b9442b932`.
- PR diff: 494 insertions and 0 deletions across exactly 3 files.
- Maintained YAML added: `data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml`, 438 lines.
- Generated pages changed: `pages/browse.html` and `pages/records/gomodel_YeastPathways_PWY-7221.html`.

Resolved exactly one target under `data/pathways/`:

- `id`: `gomodel:YeastPathways_PWY-7221`
- `label`: `guanosine ribonucleotides de novo biosynthesis`
- `pathway_type`: `nucleotide-biosynthesis`
- taxa: 1, `NCBITaxon:559292` / `Saccharomyces cerevisiae S288C`
- participants: 21
- reactions: 6
- mechanistic edges: 41
- references: 1, `gomodel:YeastPathways_PWY-7221`

The source files checked were:

- `/private/tmp/gocam-noctua/YeastPathways_PWY-7221.json`
- `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-7221.json`

The two source JSONs were not byte-identical, as expected for raw Noctua versus compact SGD GO-CAM exports:

- raw Noctua SHA-256: `89c3d8feff8b65367fc13521f285bfefde8c838e234a363b321f4342bc1c0ef9`
- compact SGD SHA-256: `3a6bb798292508021169c5f9e3bd85e1920ac0e5806b1f1ed17a51f1ff8fce04`

## Validation

All requested read-only validation passed.

- `just validate`
  - validated 5 Claude skills
  - validated 97 pathway records
  - checked 4,263 evidence blocks
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

- The YAML record id is the raw GO-CAM model id: `gomodel:YeastPathways_PWY-7221`.
- The raw Noctua title annotation is `guanosine ribonucleotides <i>de novo</i> biosynthesis - imported from: Saccharomyces Genome Database`.
- The compact SGD title is the same pathway title.
- The raw Noctua metadata points back to the SGD pathway import URL for `PWY-7221`.
- Both source forms scope the model to `NCBITaxon:559292`.
- The maintained YAML declares all 6 activity nodes from the compact SGD `activities` list as `gomodel:` reactions.
- The maintained YAML declares all 21 local `CHEBI`/`SGD` class ids reached through `RO:0002233`, `RO:0002234`, and `RO:0002333` raw fact objects as participants.

The hidden-and-ignored duplicate search included ignored and hidden files and excluded only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.

- `gomodel:YeastPathways_PWY-7221`: only the target YAML and its generated HTML page/browse references were found.
- `YeastPathways_PWY-7221`: only the target YAML and its generated HTML page/browse references were found.
- `PWY-7221`: only the target YAML and its generated HTML page/browse references were found.
- `guanosine ribonucleotides de novo biosynthesis`: only the target YAML and its generated HTML page/browse references were found.
- `guanosine-ribonucleotides-de-novo-biosynthesis` and `YeastPathways_PWY-7221` filename globs found only the target YAML and generated record page.
- `SGD:S000004830`, `SGD:S000002862`, `SGD:S000004424`, and `SGD:S000004520`: each appeared only in the target YAML and its generated record page.
- `GMP-SYN-GLUT-RXN` and `GUANYL-KIN-RXN`: each appeared only in the target YAML and its generated record page.
- `GDPKIN-RXN`: appeared in the target YAML and generated record page plus `data/pathways/ppgpp-metabolism.yaml`, where it is a legitimate reused reaction id rather than a duplicate `PWY-7221` record.

## Graph and Local References

No graph or local-reference defect found.

- `just validate` accepted every local endpoint, predicate, evidence block, evidence quote length, reference id, and CURIE prefix.
- All 41 edge ids are unique.
- Every `mechanistic_edges` endpoint is the pathway id or a declared local taxon, participant, or reaction id.
- All 41 edges use allowed local predicates projected from raw RO facts:
  - `RO:0002233` -> `consumes`
  - `RO:0002234` -> `produces`
  - `RO:0002333` -> `enables`
  - `RO:0002413` -> `precedes`; not present in this source model
  - `RO:0002411` -> `regulates`; not present in this source model
- The single declared reference, `gomodel:YeastPathways_PWY-7221`, is cited by all 41 mechanistic edges.

## Edge Evidence

No edge-evidence defect found.

The exact raw Noctua fact projection was checked for every requested relation.

- Raw Noctua fact counts:
  - `BFO:0000050`: 6
  - `BFO:0000066`: 6
  - `RO:0002233`: 17
  - `RO:0002234`: 18
  - `RO:0002333`: 6
  - `RO:0002413`: 0
  - `RO:0002411`: 0
- The raw Noctua export has 53 total facts.
- The 41 raw facts with `RO:0002233`, `RO:0002234`, `RO:0002333`, `RO:0002413`, or `RO:0002411` project to exactly the same 41 `(subject, predicate, object)` triples in the YAML.
- `RO:0002233`: all 17 activity-input facts are retained as `CHEBI:* consumes gomodel:*` edges.
- `RO:0002234`: all 18 activity-output facts are retained as `gomodel:* produces CHEBI:*` edges.
- `RO:0002333`: all 6 enabled-by facts are retained as `SGD:* enables gomodel:*` edges.
- `RO:0002413`: no raw precedes facts are present, and no `precedes` edge is maintained.
- `RO:0002411`: no raw regulates facts are present, and no `regulates` edge is maintained.
- Every raw projectable fact is quoted exactly once as the first evidence quote for one YAML edge.
- Every YAML edge quote is an exact substring of `/private/tmp/gocam-noctua/YeastPathways_PWY-7221.json`.
- Every YAML edge includes an exact raw fact quote present in the raw Noctua source.
- Every `RO:0002233`, `RO:0002234`, and `RO:0002333` edge also includes an exact raw individual-type quote whose individual id is the fact object and whose type class is the `CHEBI` or `SGD` participant id projected into YAML.
- The compact SGD source projects to the same 41 non-causal input/output/enabler facts:
  - `activities`: 6
  - `has_input`: 17
  - `has_output`: 18
  - `enabled_by`: 6
  - causal associations: 0

Only BFO placement and membership facts are intentionally omitted from YAML:

- `BFO:0000050`: 6 `part_of` facts linking each activity to `GO:0106387`, `'de novo' GMP biosynthetic process`.
- `BFO:0000066`: 6 `occurs_in` facts linking each activity to `GO:0005829`, cytosol.
- There were no other raw Noctua predicates absent from the YAML projection.
- A hidden-and-ignored leak search over `data/` and `pages/`, excluding `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`, found no `BFO:0000050` or `BFO:0000066` strings in maintained YAML or generated pages.

## Completeness

No completeness defect found for a raw Noctua GO-CAM projection.

- The maintained YAML covers all 6 activities in the compact SGD source.
- The maintained YAML covers all 41 RO input, output, and enabler facts in the raw Noctua source.
- The raw source has no `RO:0002413` or `RO:0002411` facts to curate as causal edges.
- The 12 omitted BFO facts are outside the current PathwayMech edge vocabulary and are intentional omissions rather than lost reactions, metabolites, enzymes, or causal steps.

Generated-page completeness also checked out.

- `pages/browse.html` links to `records/gomodel_YeastPathways_PWY-7221.html` and reports `gomodel:YeastPathways_PWY-7221 - 41 mechanistic edges`.
- `pages/records/gomodel_YeastPathways_PWY-7221.html` renders exactly 41 edge list items.
- The generated record-page edge list matches the YAML `mechanistic_edges` list in count, order, subject, predicate, and object.

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

- I did not edit `data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml`.
- I did not regenerate or hand-edit `pages/browse.html` or `pages/records/gomodel_YeastPathways_PWY-7221.html`.
- I did not create or mutate any GitHub issues, PR comments, labels, or settings.
- No GitHub issues should be filed from this review.
