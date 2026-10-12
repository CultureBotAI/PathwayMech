# Reference-only Handle support

This external candidate lets a declared bibliographic reference use `hdl:1993/32279`. Its evidence links still require a declared reference. It does not make Handle identifiers valid biological nodes or authority terms.

The accepted EG runtime is the complete baseline recorded in `baseline.json`. All 222 baseline files were copied. Exactly three existing files change and one test file is added; 219 files remain byte-identical. `copy-plan.json` binds each original and candidate file; `delta.patch` is the complete proposed patch. Adoption and independent review remain root-owned and have not happened in this package.

## Grammar and boundaries

The supported reference-only subset is:

```text
hdl:[0-9]+(?:\.[0-9]+)*/[A-Za-z0-9][A-Za-z0-9._-]*
```

The lowercase prefix is followed by numeric, optionally dot-separated prefix segments, one slash, and a suffix beginning with an ASCII letter or digit. Subsequent suffix characters may also include dots, underscores and hyphens. This intentionally bounded subset is not a definition of all Handle-system syntax. Whitespace, empty components, a URL in place of a CURIE, extra slashes and unsupported punctuation fail. A declared reference may carry an explicit issuing HTTPS URL, which the existing renderer already prefers.

The only production changes are native `_validate_references` and the LinkML `Reference.id` pattern/description. `ALLOWED_CURIE_PREFIXES`, all biological ID patterns, source and ontology loaders, source and ontology collectors, resolver, page renderer and KGX exporter are unchanged. The existing prefix parity test now explicitly compares the two biological classes; the new tests separately exercise every pre-existing reference prefix and the narrow reference exception.

Native validation still owns local evidence and endpoint resolution, as before. LinkML validates the reference ID syntax; it does not gain a local cross-reference engine. An undeclared Handle evidence link and a declared Handle reference used as an edge endpoint both fail the native local-resolution checks.

## Actual checks

- Final focused run: **97 passed**, including the new reference boundary tests, existing graph-context regressions and biological-prefix parity. Ruff passes for all changed Python files. Exact commands, environment and outputs are in `receipts/focused-*-2.*`.
- The first run had **95 passed, 2 failed** because the new endpoint tests expected the word `declared`; the native validator correctly said `does not resolve locally`. Only those assertions were corrected. First-run logs remain in `receipts/focused-*-1.*`.
- The frozen observed author draft `a0f144cf3191ff3f02daf7cd7c4c0e5ef1d96fa7cc72fa16e132e5819e35f2b0` has 51 edges and 51 references. Its copied bytes pass native and LinkML validation with this candidate. The issuing URL and complete Handle reference metadata survive page rendering and the two relevant KGX edges; no Handle biological node appears. This is an evolving, unsealed author draft, not a final scientific acceptance.
- The same frozen draft fails the unchanged baseline precisely at `references[45].id` in both validators. The compact receipt is `receipts/baseline-rejection.json`; the first overly verbose receipt is retained separately.
- `receipts/delta-preservation.json` rehashes every accepted baseline file and verifies the exact candidate inventory with hidden, ignored and followed paths included. It proves identical global biological prefixes and that only LinkML `Reference.id` changes.
- `git diff --no-index --check` produced no whitespace diagnostics; its exit status was 1 because the directories differ. It did not touch a Git index or repository state.

Negative cases cover malformed references, undeclared evidence, Handle record/taxon/participant/reaction IDs, both edge endpoints, source/ontology authority terms and configured authority namespaces. Collector probes select the exact expected biological IDs without adding the Handle citation. These are focused implementation checks, not a full maintained suite or a canonical build.

## Reproduction and remaining work

Use the pinned Python with `-B`, `PYTHONDONTWRITEBYTECODE=1` and `UV_NO_SYNC=1`. `run-focused.py`, `check-baseline-rejection.py`, `check-observed-draft.py` and `verify-delta.py` record the bounded checks. The observed-draft script explicitly refuses to overwrite its frozen copy if the author draft changes. Reproduction should use a fresh external copy of this sealed package so receipts remain immutable.

Root must independently review the four-file patch and tests, bridge to any later author draft, adopt the accepted delta into the intended maintained baseline, and run the maintained gates. No maintained files, shared caches, Git/GitHub state, source snapshots, dependencies or author drafts were written by this task. No scientific scope, source identity, thesis-date conflict or assay interpretation is changed by this implementation.
