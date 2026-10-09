# YAML Record Review: glycolysis I (from glucose 6-phosphate)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech`
- Record: `data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml`
- Started UTC: 2026-09-25T11:00:15Z
- Finished UTC: 2026-09-25T11:00:15Z
- Verdict: Pass; 0 blockers, 0 majors, 0 minors.

## Target

- Pull request: #110, `Add glycolysis GO-CAM`
- Maintained YAML: `data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml`
- Generated page: `pages/records/gomodel_YeastPathways_GLYCOLYSIS.html`
- Browse index: `pages/browse.html`
- Source id: `gomodel:YeastPathways_GLYCOLYSIS`
- Raw Noctua JSON: `/private/tmp/gocam-noctua/YeastPathways_GLYCOLYSIS.json`
- Compact SGD GO-CAM JSON: `/private/tmp/sgd-yeast-gocams/YeastPathways_GLYCOLYSIS.json`

## Validation

All requested validators passed.

- `just validate`: passed.
  - `validated 5 Claude skills`
  - `validated 93 pathway records`
  - `checked 3885 evidence blocks`
  - `validated 12 source records`
  - `checked 6 documentation files`
  - `checked deep-research report contract`
- `just test`: passed, 34 tests.
- `just lint`: passed, Ruff found no issues.
- `git diff --check`: passed.

Skipped validators: none.

## Identity and Grounding

The YAML record denotes the same production SGD GO-CAM model supplied in both source artifacts.

- YAML `id`: `gomodel:YeastPathways_GLYCOLYSIS`
- YAML `label`: `glycolysis I (from glucose 6-phosphate)`
- Raw Noctua `id`: `gomodel:YeastPathways_GLYCOLYSIS`
- Raw Noctua `title`: `glycolysis I (from glucose 6-phosphate) - imported from: Saccharomyces Genome Database`
- Compact `id`: `gomodel:YeastPathways_GLYCOLYSIS`
- Compact `title`: `glycolysis I (from glucose 6-phosphate) - imported from: Saccharomyces Genome Database`
- Compact `status`: `production`
- Compact `taxon`: `NCBITaxon:559292`
- YAML taxon: `NCBITaxon:559292` / `Saccharomyces cerevisiae S288C`

Duplicate pathway identity was checked with ignored-file-inclusive searches that covered the workspace, including ignored and hidden files, excluding only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`:

```bash
rg --no-ignore --hidden -n -F "gomodel:YeastPathways_GLYCOLYSIS" . -g '!/.git/**' -g '!/.venv/**' -g '!/.pytest_cache/**' -g '!/.ruff_cache/**'
rg --no-ignore --hidden -n -F "glycolysis I (from glucose 6-phosphate)" . -g '!/.git/**' -g '!/.venv/**' -g '!/.pytest_cache/**' -g '!/.ruff_cache/**'
rg --no-ignore --hidden -n -F "YeastPathways_GLYCOLYSIS" . -g '!/.git/**' -g '!/.venv/**' -g '!/.pytest_cache/**' -g '!/.ruff_cache/**'
rg --no-ignore --hidden -n -F -e "gomodel:YeastPathways_GLYCOLYSIS" -e "YeastPathways_GLYCOLYSIS" -e "glycolysis I (from glucose 6-phosphate)" -e "GLYCOLYSIS" data/pathways -g '!/.git/**' -g '!/.venv/**' -g '!/.pytest_cache/**' -g '!/.ruff_cache/**'
rg --files --no-ignore --hidden -g '*glycolysis*' -g '*GLYCOLYSIS*' -g '*YeastPathways_GLYCOLYSIS*' -g '!/.git/**' -g '!/.venv/**' -g '!/.pytest_cache/**' -g '!/.ruff_cache/**'
```

Those searches found the maintained identity only in the target YAML under `data/pathways/`; the workspace hits outside `data/pathways/` were the generated `pages/records/gomodel_YeastPathways_GLYCOLYSIS.html` page, its `pages/browse.html` link, and GO-CAM importer fixture references in `tests/`. The gitignore-independent filename search found only `data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml` and `pages/records/gomodel_YeastPathways_GLYCOLYSIS.html`, so no sibling maintained YAML, generated page, or filename duplicate exists for this exact pathway slug or GO-CAM id.

The compact source has 14 activities and 44 term objects. The YAML keeps the 31 concrete local participants in scope for the current PathwayMech schema: 17 `CHEBI` metabolite/cofactor objects and 14 `SGD` gene-product or complex objects.

## Graph and Local References

The local graph is schema-clean.

- Declared taxa: 1
- Declared participants: 31
- Declared reactions: 14
- Maintained `mechanistic_edges`: 91
- Distinct maintained triples: 91
- Declared references: 1
- Dangling edge endpoints: none
- Duplicate maintained edge ids: none
- Duplicate maintained edge triples: none
- Duplicate participant ids: none
- Duplicate reaction ids: none
- Duplicate reference ids: none
- Unsupported predicates: none; `just validate` enforced `ALLOWED_EDGE_PREDICATES`.
- Undeclared `reference_id` values: none; `just validate` checked all 3885 corpus evidence blocks.
- Evidence quotes longer than 400 characters: none; `just validate` enforced the limit.

Every maintained edge endpoint resolves to the record id, the local `NCBITaxon:559292` taxon, one of the declared participants, or one of the declared reactions.

## Edge Evidence

The raw Noctua file contains 119 facts:

- `RO:0002233`: 27
- `RO:0002234`: 29
- `RO:0002333`: 14
- `RO:0002413`: 21
- `RO:0002411`: 0
- `BFO:0000050`: 14
- `BFO:0000066`: 14

I compared every raw `RO:0002333`, `RO:0002233`, `RO:0002234`, `RO:0002413`, and `RO:0002411` fact against the YAML after projecting local Noctua controller and chemical individuals to their `SGD` or `CHEBI` classes:

- `RO:0002333`: inverted to `SGD:* enables gomodel:*`.
- `RO:0002233`: inverted to `CHEBI:* consumes gomodel:*`.
- `RO:0002234`: retained as `gomodel:* produces CHEBI:*`.
- `RO:0002413`: retained as `gomodel:* precedes gomodel:*`.
- `RO:0002411`: none present in raw.

The raw projection produced 91 expected edges and 91 distinct expected triples. The YAML has exactly those 91 triples:

- Missing raw projected edges: none
- Extra YAML edges: none
- Duplicate YAML edges: none

Every YAML evidence quote is an exact substring of `/private/tmp/gocam-noctua/YeastPathways_GLYCOLYSIS.json`. The first quote on every edge matches the raw fact tuple, for example:

```text
"subject":"gomodel:6PFRUCTPHOS-RXN","property":"RO:0002333","property-label":"RO:0002333","object":"gomodel:YeastPathways_GLYCOLYSIS/6690711d00000315"
```

For every `RO:0002333`, `RO:0002233`, and `RO:0002234` edge whose raw endpoint is a local Noctua individual, the second quote exactly captures the raw `type` record that grounds the local individual to the normalized `SGD` or `CHEBI` class, for example:

```text
"id":"gomodel:YeastPathways_GLYCOLYSIS/6690711d00000315","type":[{"type":"class","id":"SGD:S000218025"
```

The compact SGD GO-CAM source projects to the same normalized multiset as the raw Noctua facts:

- Raw-minus-compact projected edges: none
- Compact-minus-raw projected edges: none

## Completeness

No material raw GO-CAM fact in the current mechanistic edge predicate set is missing:

- All 27 raw `RO:0002233` input facts are represented as `consumes`.
- All 29 raw `RO:0002234` output facts are represented as `produces`.
- All 14 raw `RO:0002333` controller/enabler facts are represented as `enables`.
- All 21 raw `RO:0002413` ordering facts are represented as `precedes`.
- The raw model has no `RO:0002411` facts to curate as `regulates`.

The 28 omitted raw facts are exactly out-of-scope structural or location assertions:

- All 14 `BFO:0000050` facts are pathway membership assertions from GO-CAM activity nodes to the GO-CAM model individual.
- All 14 `BFO:0000066` facts are `occurs_in` assertions to cytosol local individuals.

`src/pathwaymech/schema.py` has no concrete local schema path for `BFO:0000050`, `BFO:0000066`, location nodes, or GO cellular-component participants. Its `ALLOWED_EDGE_PREDICATES` set contains only `activates`, `catalyzes`, `consumes`, `enables`, `inhibits`, `precedes`, `produces`, and `regulates`.

I also searched for accidental BFO leakage in the maintained YAML and generated record page with ignored and hidden files enabled:

```bash
rg --no-ignore --hidden -n -F -e "BFO:0000050" -e "BFO:0000066" data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml pages/records/gomodel_YeastPathways_GLYCOLYSIS.html -g '!/.git/**' -g '!/.venv/**' -g '!/.pytest_cache/**' -g '!/.ruff_cache/**'
```

That search found no `BFO:0000050` or `BFO:0000066` strings in the maintained YAML or generated record page.

## Findings

None found.

## Recommended Edits

None.

The maintained record already represents every in-scope raw mechanistic fact, has no extras or duplicate local assertions, and keeps only the out-of-scope BFO pathway-membership and location assertions omitted.

## Follow-up Checks

None required for PR #110.

For any future edit, rerun:

```bash
just validate
just test
just lint
git diff --check
```

If any YAML edge changes, also rerun a raw projection comparison against `/private/tmp/gocam-noctua/YeastPathways_GLYCOLYSIS.json` and `/private/tmp/sgd-yeast-gocams/YeastPathways_GLYCOLYSIS.json`.

## Additional Notes

The generated page matches the YAML. I rendered the expected `pages/records/gomodel_YeastPathways_GLYCOLYSIS.html` content in memory through `pathwaymech.cli._record_page` and compared it byte-for-byte to the committed HTML.

`pages/browse.html` also matches the YAML. I rendered the expected browse index in memory from all 93 validated records and compared it byte-for-byte to the committed index; its glycolysis row links to `records/gomodel_YeastPathways_GLYCOLYSIS.html` and reports `gomodel:YeastPathways_GLYCOLYSIS - 91 mechanistic edges`.

The only GitHub issue follow-up would be for a real finding in this review. No blockers, majors, or minors were found, so no GitHub issues should be filed.
