# Bounded native EcoCyc complex adapter preparation

This is an external implementation candidate for independent review. It was based on all 223 exact runtime files from the accepted next231 canonical build, including its Handle changes. It does not adopt anything into a maintained worktree, run a full canonical build, or accept the next232 pathway record. No actual ATP/PPi merge state is claimed.

## Supported representations

The new `ecocyc-complex-xml` kind handles two typed shapes without changing the old named-complex adapter:

| Native object | Honest display | Native naming status | Preserved assembly |
| --- | --- | --- | --- |
| `EcoCyc:CPLX0-682` | `unnamed protein complex CPLX0-682` | `unnamed`, no direct common-name or synonym | `MONOMER0-541` × 6 |
| `EcoCyc:PYRNUTRANSHYDROGEN-CPLX` | `PntAB` | `synonym_only`, no direct common-name | `PNTB-MONOMER` × 2 then `PNTA-MONOMER` × 2 |

The unnamed term uses `label_kind: source_context`; the PntAB term uses `label_kind: source_synonym`. Both use `entity_type: protein_complex`, empty term aliases, and complete typed native metadata under their source. The display for the unnamed complex explicitly reports missing native name and frame identity. “NadK hexamer” remains supported scientific context for the record description; nested activity names are never promoted to protein names. PntAB's direct synonym stays a synonym in the metadata. Existing policy has no EcoCyc contextual display exception, so these terms require their exact normalized honest display and placement in `participants` with `category: complex`. A canonical-only namespace policy cannot use the synonym-only term. No broad contextual-label bypass was added.

The new kind is deliberately bounded by structural shape, not these two accession constants. An unnamed homomer must have exactly the `Protein-Complexes` parent, one protein component with integer coefficient at least two, no direct names, and no class companion. A synonym-only heteromer must have exactly the `PC-1` and `Protein-Complexes` parents, one simple direct synonym, at least two distinct protein components, and a separate issuing PC-1 class original that declares the exact complex instance. Parent and component order are preserved. Closed direct slots reject unsupported state/chain/class structures even if an allowed parent is also present.

The request host, HTTPS request, frame, full top-level entity, ECOLI PGDB, release, species, strain and taxon all bind to the original bytes. The service's literal HTTP-on-443 serialization remains accepted within its XML metadata, as in the existing adapter. XML DOCTYPEs, unresolved entities, duplicate/conflicting parent assertions, unsupported parent classes, modified-state slots, chain/class nodes, ambiguous names, missing/fractional coefficients, contradictory duplicate source assertions and forged typed snapshot metadata fail closed. Native metadata validation checks internal consistency; agreement with the original XML is the builder's responsibility.

## Manifest and original coverage

See `receipts/originals-1791790019833385000/bounded-manifest.json` for the exact working two-entry manifest and `bounded-native-snapshot.json` for actual builder output. Primary entries use the existing key/kind/path/url/version/license/sha256 fields. The PntAB entry additionally requires closed `class_source` provenance containing `path`, `url`, `version`, `license`, and `sha256`. Both paths are relative to the original cache directory; each original is freshly SHA-256 checked during the build. The class companion is not a biological selected term.

**Future preparation/capture/integration helpers must explicitly inventory and copy `class_source.path` as an original**, in addition to top-level manifest paths and existing sidecars. The builder itself reads and hashes it. Its SHA-256 is `e36fbeb82a86b02acd1494807251805a45aa63f7b60b83e109453d096c3ac835`. Merely copying the top-level manifest paths would omit a required original. The native source is ECOLI 27.0; the licensing marker preserves the accepted explicit upstream-terms/deferred-public-release provenance.

Use the normal `build_snapshot` manifest workflow. The older low-level `source_terms` API does not handle this new kind because it cannot supply a closed companion manifest entry. No network requests or label injection are part of the build.

## Integration files and preservation

`copy-plan.json` binds exactly four eventual integration files: changed `scripts/build_source_identifier_snapshot.py` and `src/pathwaymech/identifiers.py`, plus new `src/pathwaymech/ecocyc_complex.py` and `tests/test_ecocyc_complex_authority.py`. `delta.patch` shows the complete delta. The other 221 existing runtime files remain exact, including schema, identifier policy, Handle files, rendering, history and KGX code. Do not copy the entire baseline/candidate tree into a current worktree: independently bridge the accepted runtime and the actual integration base, then apply only the reviewed four-file delta. Authority configuration/output changes belong to the later original-driven full build.

Five legacy parser/helper function bodies are byte-exact. Whole-original ALKAPHOSPHA-CPLX and UDHA-CPLX outputs remain equal to baseline. Existing EcoCyc, MetaCyc unnamed reaction, MetaCyc complex naming, identifier and Handle tests passed with the new tests.

## Actual validation and limits

Final focused run: **785 passed**; final Ruff F checks passed. The final whole-original replay rebuilt both new terms and class proof, checked two existing named complexes for exact equality, rejected the original PHOSPHO-ARCA/PHOSPHO-PHOB modified proteins, PNTA monomer and PC-1 class as biological complexes, compared five old parser bodies and rehashed all nine copied originals. Final checks used pinned Python with `-B`, no install/sync, external pytest temporary files and an external Ruff cache. Every check retains its exact four-file code snapshot, command, environment, stdout, stderr and exit receipt.

The initial 732- and 773-test passes remain retained. Additional controls and the final unsupported-direct-slot guard led to the 785-test pass; there were no failed test runs. A first capture-script invocation failed on the preflight manifest's bare-list shape before copying inputs; its receipt is retained in `initial-capture-attempt.json`, and the corrected capture succeeded. Read-only `diff` commands returned their ordinary exit 1 because changes exist; they were inspections, not test failures.

This package does not establish a full-corpus canonical build, selected-ID completeness for an unfinished author draft, scientific acceptance, maintained integration, whole repository tests, PR review or merge. Those remain parent-owned next steps. Original preflight files and accepted next231 runtime files were verified unchanged; no maintained repository, shared source cache or Git writes were made.
