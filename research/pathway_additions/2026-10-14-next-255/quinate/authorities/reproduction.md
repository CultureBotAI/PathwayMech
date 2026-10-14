# Additive next255 authority union

Baseline commit: `bfa3f5ed0e843472c0fd173ce91df2a90dd4ddb2`.
Worktree: `/private/tmp/pathwaymech-next-255-20261014`.
External cache: `/private/tmp/pathwaymech-next-255-authorities/originals`.

Both production builders passed without modification. Their exact argument
arrays, environment, working directory, SHA256 hashes, selector binding and
manifest digest are in `canonical-build-commands.json`. Command receipts and
lossless UTF-8 log wrappers are retained separately. These builds used all
251 baseline record files copied from exact Git blobs and an ID-only selector
retaining all 4,891 prior authority identifiers plus 25 planned pathway-node
identifiers. The selector supplies no labels or biological assertions.

To reproduce in the same evidence environment, read those argument arrays,
change only their `--output` destinations to fresh external paths, and run each
with the recorded working directory and environment. Compare the resulting
whole-file hashes to the following promoted outputs:

| Artifact | SHA256 |
| --- | --- |
| `data/identifier_authorities/sources.json` | `32fdd091eb94869fa437cc8cbafaf2ae69458ef55f72031586dbc69561cfe8fb` |
| `data/identifier_authorities/ontology.json` | `1115c53b4bc1e1104a03e612cd1f2b08ae1d72e3d6538eb864bd6c084c90f7bf` |
| `conf/identifier_sources.json` | `5021eff782c83cee42c848aeeb339724f700c3dd874707e3ea75a76cb56128f7` |

`prepare_union.py` records the exact staging procedure. It expects a fresh
baseline checkout and refuses concurrent authority changes. `run_builds.py`
preserves existing receipts rather than overwriting an earlier attempt.
`promote.py` verifies the complete baseline objects and raw-source hashes before
writing only the two snapshots and source manifest. It must not be rerun over
an already promoted checkout without reviewing its guards.

## Preservation result

- All 4,891 baseline terms and all 821 baseline source owners remain unchanged.
- Source terms: 2,813 to 2,824; source owners: 816 to 827.
- Ontology terms: 2,078 to 2,083; the five ontology source owners are unchanged.
- Total final terms: 4,907, adding exactly sixteen identifiers.
- Source manifest: 997 to 1,008 entries; the entire old entry prefix is exact.
- All 1,023 top-level/companion hash descriptors verified, covering 1,007 distinct
  original cache paths, including the separate Rhea-update provenance manifest.
- Existing GO localization authorities were retained; no policy/schema change
  or new parser branch was needed.

The native initial quinate reaction remains an independently verified typed
MetaCyc reaction with contextual display naming. Native `Quinones` and
`Reduced-Quinones` retain their exact source HTML names, `a quinone` and `a quinol`.
This authority work does not assert equivalence to the narrower Rhea first-step
family, assay-material sequence identity, or scientific review approval.

Keep full HTML/XML/JSON/SQLite/RDF originals external. The retained authority
snapshots, compact manifest, acquisition/verification receipts, and helper text
files suffice to identify and replay the original-byte selections.
