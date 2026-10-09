# YAML Record Review: gluconeogenesis I

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech`
- Record: `data/pathways/gluconeogenesis-i.yaml`
- Started UTC: 2026-09-25T10:52:22Z
- Finished UTC: 2026-09-25T10:52:22Z
- Verdict: Pass; 0 blockers, 0 majors, 0 minors.

## Target

- Maintained YAML: `data/pathways/gluconeogenesis-i.yaml`
- Generated page: `pages/records/gomodel_YeastPathways_GLUCONEO-PWY-1.html`
- Browse index entry: `pages/browse.html`
- Source id: `gomodel:YeastPathways_GLUCONEO-PWY-1`
- Raw Noctua JSON: `/private/tmp/gocam-noctua/YeastPathways_GLUCONEO-PWY-1.json`
- Compact SGD GO-CAM JSON: `/private/tmp/sgd-yeast-gocams/YeastPathways_GLUCONEO-PWY-1.json`

## Validation

All requested validators passed.

- `just validate`: passed.
  - `validated 5 Claude skills`
  - `validated 92 pathway records`
  - `checked 3724 evidence blocks`
  - `validated 12 source records`
  - `checked 6 documentation files`
  - `checked deep-research report contract`
- `just test`: passed, 34 tests.
- `just lint`: passed, Ruff found no issues.
- `git diff --check`: passed.

Skipped validators: none.

## Identity and Grounding

The record identity matches both supplied GO-CAM artifacts.

- YAML `id`: `gomodel:YeastPathways_GLUCONEO-PWY-1`
- YAML `label`: `gluconeogenesis I`
- Raw Noctua `id`: `gomodel:YeastPathways_GLUCONEO-PWY-1`
- Compact `id`: `gomodel:YeastPathways_GLUCONEO-PWY-1`
- Compact `title`: `gluconeogenesis I - imported from: Saccharomyces Genome Database`
- Compact `taxon`: `NCBITaxon:559292`
- YAML taxon: `NCBITaxon:559292` / `Saccharomyces cerevisiae S288C`

Duplicate pathway identity was checked with an ignored-file-inclusive search:

```bash
rg --no-ignore --hidden -n -F -e 'gomodel:YeastPathways_GLUCONEO-PWY-1' -e 'YeastPathways_GLUCONEO-PWY-1' -e 'GLUCONEO-PWY' -e 'gluconeogenesis I' . -g '!**/.git/**' -g '!**/.venv/**' -g '!**/.pytest_cache/**' -g '!**/.ruff_cache/**'
```

That search covered the workspace, including ignored and hidden files, excluding only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`. The only hits were the target YAML, `pages/records/gomodel_YeastPathways_GLUCONEO-PWY-1.html`, and the `pages/browse.html` link to that page. No sibling maintained YAML record for the GO-CAM source id, source slug, `GLUCONEO-PWY` pathway fragment, or exact label was found.

The 36 YAML participant CURIEs are exactly the 36 compact `objects` whose prefix is `SGD` or `CHEBI`. The 16 YAML reaction ids are exactly the 16 compact `activities` and exactly the 16 raw activity individuals used by the raw mechanistic relations. The YAML reaction labels match the raw Noctua `type` labels, including the duplicate-class local activities for:

- TDH2/TDH3 glyceraldehyde-3-phosphate dehydrogenase activities.
- PYC1/PYC2 pyruvate carboxylase activities.
- MDH2/MAE1 malate or malic enzyme activities.
- ENO1/ENO2 phosphopyruvate hydratase activities.

## Graph and Local References

The local graph is schema-clean.

- Declared participants: 36
- Declared reactions: 16
- Maintained `mechanistic_edges`: 108
- Distinct maintained triples: 108
- Dangling edge endpoints: none
- Duplicate maintained edge triples: none
- Unsupported predicates: none; `just validate` enforced `ALLOWED_EDGE_PREDICATES`.
- Undeclared `reference_id` values: none; `just validate` checked all 3724 corpus evidence blocks.
- Evidence quotes longer than 400 characters: none; `just validate` enforced the limit.

Every maintained edge endpoint resolves to the record id, the one local taxon, one of the declared participants, or one of the declared reactions.

## Edge Evidence

The raw Noctua file contains 140 facts:

- `RO:0002233`: 35
- `RO:0002234`: 38
- `RO:0002333`: 16
- `RO:0002413`: 19
- `RO:0002411`: 0
- `BFO:0000050`: 16
- `BFO:0000066`: 16

I compared every raw `RO:0002333`, `RO:0002233`, `RO:0002234`, `RO:0002413`, and `RO:0002411` fact against the YAML after projecting typed local Noctua controller and chemical individuals to their `SGD` or `CHEBI` classes:

- `RO:0002333`: inverted to `SGD:* enables gomodel:*`.
- `RO:0002233`: inverted to `CHEBI:* consumes gomodel:*`.
- `RO:0002234`: retained as `gomodel:* produces CHEBI:*`.
- `RO:0002413`: retained as `gomodel:* precedes gomodel:*`.
- `RO:0002411`: none present in raw.

The raw projection produced 108 expected edges and 108 distinct expected triples. The YAML has exactly those 108 triples:

- Missing raw projected edges: none
- Extra YAML edges: none
- Duplicate YAML edges: none

Every YAML evidence quote is an exact substring of the minified raw Noctua JSON. This checked the fact snippets such as:

- `"subject":"gomodel:RXN-15513","property":"RO:0002333","property-label":"RO:0002333","object":"gomodel:YKL152C-MONOMER_RXN-15513_controller"`
- `"id":"gomodel:YKL152C-MONOMER_RXN-15513_controller","type":[{"type":"class","id":"SGD:S000001635"`

## Completeness

No material raw GO-CAM fact in the current mechanistic edge predicate set is missing:

- All 35 raw `RO:0002233` input facts are represented as `consumes`.
- All 38 raw `RO:0002234` output facts are represented as `produces`.
- All 16 raw `RO:0002333` controller/enabler facts are represented as `enables`.
- All 19 raw `RO:0002413` ordering facts are represented as `precedes`.
- The raw model has no `RO:0002411` facts to curate as `regulates`.

The omitted structural/location assertions are appropriate for the current local schema:

- All 16 `BFO:0000050` facts are pathway membership assertions from GO-CAM activity nodes to the GO-CAM model individual.
- All 16 `BFO:0000066` facts are `occurs_in` location assertions to cytosol or mitochondrion local individuals.
- `src/pathwaymech/schema.py` has no concrete local schema path for `BFO:0000050`, `BFO:0000066`, location nodes, or GO cellular component participants, and its `ALLOWED_EDGE_PREDICATES` set contains only `activates`, `catalyzes`, `consumes`, `enables`, `inhibits`, `precedes`, `produces`, and `regulates`.

I searched for accidental BFO leakage with ignored and hidden files enabled:

```bash
rg --no-ignore --hidden -n -F -e 'BFO:0000050' -e 'BFO:0000066' data/pathways/gluconeogenesis-i.yaml pages/records/gomodel_YeastPathways_GLUCONEO-PWY-1.html -g '!**/.git/**' -g '!**/.venv/**' -g '!**/.pytest_cache/**' -g '!**/.ruff_cache/**'
```

The search found no `BFO:0000050` or `BFO:0000066` assertions in the maintained YAML or generated record page.

## Findings

None found.

## Recommended Edits

None.

The maintained record already represents every in-scope raw mechanistic fact, has no extras, and keeps the out-of-scope BFO pathway-membership and location assertions omitted.

## Follow-up Checks

None required for PR #109.

For any future edit, rerun:

```bash
just validate
just test
just lint
git diff --check
```

If any YAML edge changes, also rerun a raw projection comparison against `/private/tmp/gocam-noctua/YeastPathways_GLUCONEO-PWY-1.json`.

## Additional Notes

Generated page drift was checked by parsing `pages/records/gomodel_YeastPathways_GLUCONEO-PWY-1.html` and comparing every `<li>` edge string to the YAML `mechanistic_edges` list. The page has no missing YAML edges and no extra edge strings.

`pages/browse.html` links to `records/gomodel_YeastPathways_GLUCONEO-PWY-1.html` and reports `gomodel:YeastPathways_GLUCONEO-PWY-1 - 108 mechanistic edges`, matching the YAML and record page.
