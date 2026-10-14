Historical authority acquisition/staging note. The final completed canonical union build, retained identifiers and zero-old-owner-change comparison are documented in `canonical-build-receipt.json`, `retained-authority-identifiers.json`, `canonical-build-commands.json` and `canonical-union-comparison.json`. Complete raw originals remain external; this repository keeps bounded projections and provenance receipts.

Authority preparation for MetaCyc PWY0-301, local 2026-10-13 / UTC 2026-10-14

All 68 acquired response bodies remain unmodified in `raw/`, including HTTP
failures and native JavaScript redirect pages. `provenance-manifest.json` records
actual request/final URLs, UTC times, whole-byte hashes, versions where supplied,
and native object identities. Every retained body was freshly checked against its
acquisition hash. Projections are derivative inspection aids, not replacement
source objects. No maintained repository file was changed by this preparation.

The selected whole MetaCyc 27.0 PWY0-301 XML proves a five-member pathway:
RXN0-2461 -> RXN0-5214 -> RXN0-705 -> LXULRU5P-RXN -> RIBULPEPIM-RXN.
LXULRU5P-RXN runs right-to-left relative to its printed native equation; the
other pathway layouts run left-to-right. The older SGD-hosted MetaCyc 22.5
original has four members and an incoming PTS link. Retain this release
difference; do not substitute the shorter old boundary for the selected source.

The author's choice of native MetaCyc RXN0-2461 aggregate transport preserves
HPr protein-bound histidine residue classes. Native Rhea 33303 is obsolete;
its replacement comment points at Rhea 42436, whose permease phosphohistidine
donor is not the same aggregate donor. Current UniProt UlaB Cys9 annotation
also warrants documenting that conflict. Neither obsolete reaction 33303 nor
the residue ChEBI cross-reference should be promoted as a current whole reaction
or whole HPr protein identity.

Canonical source builder feasibility:

- `metacyc-html` accepts exact issuing ID/title originals for PWY0-301,
  RXN0-2461, Hpr-Histidine, and Hpr-pi-phospho-L-histidines. This proves only
  identity/name; complete native XML separately supports all biological scope.
- Exact HTML title for RXN0-2461 is `EC 2.7.1.194`; HPr class titles are
  `an [HPr]-L-histidine` and `an [HPr protein]-Npi-phospho-L-histidine`.
  A descriptive graph display label must follow current record label policy.
- Current typed pathway/reaction/carrier adapters reject the unmodified full
  XML profiles. Rejected probes remain in `adapter-probes.json` and
  `carrier-adapter-probes.json`. Do not claim typed-pathway or transport parsing.
- Three exact MetaCyc assembly XMLs already pass `metacyc-protein-xml`:
  CPLX0-7848 (UlaG hexamer), CPLX0-7744 (UlaD dimer), EIISGA (UlaABC PTS).
  All native subunit coefficients and taxon context are retained in originals.
  EcoCyc alternative probes also exist, but the author must select actual IDs.
- All eight individually requested MG1655 Gene originals pass the existing
  `ncbi-entrezgene-xml` adapter and emit the `Entrez:` namespace.
- Existing source `uniprot-ecoli-reviewed-cofactors`, release 2026_03, already
  emits every Ula protein, UlaR, PtsH, PtsI, CRP, and both IHF subunits. Retain
  this first owner and use newly fetched complete UniProt objects as scientific
  evidence. No new UniProt issuing-source entry is needed.

`proposed-source-additions.json` contains at most 15 source-object entries, all
backed by successful originals. The preparation script filters these to IDs
selected by the real corpus and the actual author draft. It never invents labels.

Run after the author finishes, substituting the actual draft path:

```bash
PYTHONDONTWRITEBYTECODE=1 /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-ascorbate-authority-20261013/prepare_snapshot_staging.py --draft /actual/author/draft.yaml --output /private/tmp/pathwaymech-next-244-canonical-staging
```

This creates external aliases to every prior manifest original under
`/private/tmp/pathwaymech-next-243-canonical-build-20261012/originals`, then
selected new originals, with the real old corpus plus the copied author draft.
The shared `pathwaymech-curation-authorities/sources` cache is incomplete for
the existing manifest and must not be used as the whole prior source cache.

Run the unchanged source builder against the external staged paths:

```bash
PYTHONDONTWRITEBYTECODE=1 /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/build_source_identifier_snapshot.py --manifest /private/tmp/pathwaymech-next-244-canonical-staging/identifier_sources.json --cache-dir /private/tmp/pathwaymech-next-244-canonical-staging/originals --records /private/tmp/pathwaymech-next-244-canonical-staging/records --output /private/tmp/pathwaymech-next-244-canonical-staging/sources.json
```

The builder performs full hash/typed consistency checks and preserves first
owner semantics. A generated output must be compared against the maintained
snapshot: preserve every old term and owner unless a separately reviewed source
change is required. The source preparation script was run successfully against the author draft, selecting nine new issuing-source objects. The source builder was then started against that external staging directory; see the separate build verification receipt for completion status.

Pinned ontology projection finds CHEBI:61698, CHEBI:58774, RHEA:28804, and
RHEA:14354 in the retained SQL sources. Additional author-selected chemical or
taxon IDs must be extracted from those same authorities, never authored labels.
The complete CHEBI, GO, NCBITaxon, and Rhea SQL originals are in
`/private/tmp/pathwaymech-curation-authorities`. Preserve existing Rhea142
overrides and direction metadata; RHEA:18499 is already owned by that source.
The exact SQL term projection is `ontology-term-projection.json`; its projection
does not claim freshly recomputed whole-database hashes. The canonical ontology
builder must include current `conf/rhea_identifier_updates.json` and its actual
retained original cache, as in the previous canonical build.

Required final checks: record-specific identifier resolution; all five reaction
steps and complete sides; carrier residue class versus whole protein distinction;
transport membrane sides; UlaG/UlaD/UlaABC assembly coefficients; UlaR/CRP/IHF
evidence-qualified regulation; version and Rhea conflict statements; and unchanged
old authority owners. Scientific appraisal belongs to the author/root reviewers.
