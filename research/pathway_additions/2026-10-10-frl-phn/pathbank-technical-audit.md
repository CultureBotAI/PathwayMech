# Independent PathBank technical audit

Reviewed 2026-10-10 at 21:25:54 UTC against base `d83a2f0` and the working
implementation. Reviewer: a separate agent that authored neither the PathBank
authority implementation nor the archive-screening script. This is a technical
audit, **not a structured scientific review of either new pathway record**.

**Result: no actionable technical defect found in the inspected scope.** Full
repository gates and scientific reviews remain separate requirements.

## Evidence inspected

- Read the source-builder change, production identifier policy, source-manifest
  additions, relevant identifier-gate implementation, parser/gate tests,
  `docs/IDENTIFIERS.md`, source-inventory change, authority notes, screening
  script, TSV, JSON and batch README.
- Independently read `PW002065.owl` from the original ZIP. Its 45,470 bytes match
  both external extracted copies and SHA-256
  `66e835939e82188e3c976f0eda7ab68fa3d6fd8064bb18b1c4df439abec4cc62`.
  The archive digest matches
  `b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44`.
- Direct production extraction returns 24 unique native terms: one pathway,
  four biochemical reactions, eleven chemicals, seven proteins and one complex.
  The linked SMPDB accession and pathway URI establish `PathBank:SMP0002077`,
  with title `Methylphosphonate Degradation I`; the complex resolves to
  `PathBank:SMP0002077/ProteinComplex/4049`.
- Every extracted authority term is in the scoped PathBank namespace. The real
  member's external chemical and protein cross-references do not generate
  ChEBI or UniProt authority terms.

## Identity and label boundaries

The parser fails on ambiguous or absent SMPDB unification identity, disagreement
with the supported identifiers.org pathway URI, duplicate normalized subjects,
conflicting subject attributes, nested XML bases and unsupported local graph
identities. It does not derive an SMP accession from a PathWhiz filename or
manufacture referenced-but-undeclared local entities. Malformed or unresolved
inputs raise before the command replaces an existing snapshot.

The pathway title remains independently canonical. Declared local graph objects
are `source_context`, and cannot satisfy canonical-only slots merely by matching
text. Contextual rules are limited to the documented record prefixes and slots;
missing identities still fail before label relaxation. Graph existence is
explicitly distinguished from membership, composition and catalytic evidence.

Executed `UV_CACHE_DIR=/private/tmp/pathwaymech-frl-phn-uv-cache UV_NO_SYNC=1 uv run
pytest tests/test_pathbank_identifier_authority.py -q`: **26 passed in 0.79 s**.
The malformed-input, contextual-policy and no-snapshot-replacement cases were
read individually. No broad test suite was run by this reviewer.

## Screening reproducibility and preserved authority

Re-ran `screen_pathbank_archive.py` on the preserved ZIP and the baseline corpus
under `/private/tmp/pathwaymech-pathbank-authority-regression/data/pathways`.
All 159 baseline YAML files were separately compared byte-for-byte with
`git show d83a2f0:<path>` before accepting that corpus comparison.

The regenerated TSV and JSON are byte-identical to the maintained artifacts:

| Output | SHA-256 |
| --- | --- |
| `pathbank-screening.tsv` | `8b63deb0ee48d3d3a010d90fba94fce095aed61c5cb6a550dff4858912b0fd11` |
| `pathbank-screening.json` | `9b567ea92e1b260d267ce168d27e22b71a49e11a00e60042158d5a97f7b8e93d` |

This reproduces 2,687 OWL members, 528 files with the selected explicit microbial
names, and screening classes of 205 single-pathway files with at least two
document reactions, 265 multiple-pathway files and 58 smaller single-pathway
files. The script and prose retain the limits: a named-organism screen,
document-level counts, exact-match hints, no automatic semantic deduplication,
no addition approval and no exhaustion claim. Reproduced output remains under
`/private/tmp/pathwaymech-pathbank-independent-audit/screening/`.

The saved baseline rebuild equals the base source snapshot as parsed JSON.
The current source snapshot preserves all 1,572 baseline terms and all 88
baseline provenance blocks unchanged; it has 1,583 terms and 89 selected
sources. This audit checks preservation and the added PathBank authority; it
does not substitute for the parent task's complete source-build receipt.

## Reviewed implementation digests

| File | SHA-256 |
| --- | --- |
| `scripts/build_source_identifier_snapshot.py` | `b65cc2b7fe4d7234d5d3925918b3cc8ad2be01c67dfaaf8423e8d6935186fdd4` |
| `conf/identifier_policy.yaml` | `b5831e481fb7551858de5de9e4765c560d1f1d5531eecf871205cbe26041bc19` |
| `tests/test_pathbank_identifier_authority.py` | `fbef9055615c28164ca354bc4ca785ee474f97e7a653b469e5b2594cece134ea` |
| `screen_pathbank_archive.py` | `f229efe5d5b1908a88f7792c9a82739246a7457007bdfaee06aaeb51999539fd` |

## Source-status test correction: issue #318

Independently reviewed the one-line correction in `tests/test_sources.py:68`
for [issue #318](https://github.com/CultureBotAI/PathwayMech/issues/318).
Changing the expected seed-row status from `support` to `active` matches the
authorized source-inventory promotion: PathBank now has a maintained
`PathBank:SMP0002077` record backed by the independently verified native
authority. The inventory still requires individual review of remaining archive
members and preserves the deferred public-release terms review. The correction
does not broaden adoption or remove an assertion; it updates the obsolete
expected status while retaining the source's priority, identifier and enabled
flag check. No further defect was found in this change.

Executed `UV_CACHE_DIR=/private/tmp/pathwaymech-frl-phn-uv-cache UV_NO_SYNC=1 uv run
pytest tests/test_sources.py -q`: **7 passed in 0.22 s**, exit 0. The parent task
owns the complete suite rerun; this addendum reports only the focused result.

## Final LF serialization verification

The final staged whitespace check exposed the new screening TSV's default CSV
CRLF endings. Reviewed the sole generator change: `csv.DictWriter` now explicitly
uses `lineterminator="\n"`. The earlier screening/script digests above remain
historical receipts for the original CRLF serialization.

Independently re-ran the complete 2,687-member scan against the same preserved
archive and verified 159-record base corpus, with output under
`/private/tmp/pathwaymech-pathbank-independent-audit/screening-lf/`. The command
used `UV_CACHE_DIR=/private/tmp/pathwaymech-frl-phn-uv-cache UV_NO_SYNC=1 uv run
python research/pathway_additions/2026-10-10-frl-phn/screen_pathbank_archive.py`,
the archive and baseline paths documented above, and that new `--output` path.
It exited 0 and reproduced the same 528 selected files and 205/265/58 classes.
Both regenerated TSV and JSON match the final repository files byte-for-byte.

Compared the final TSV with the preserved original
`/private/tmp/pathwaymech-frl-phn-screening-original-crlf.tsv`: exactly 529 CRLF
sequences became LF, with all 529 rows including the header and all 5,819 cells
unchanged. No carriage returns remain. No target-record or scientific-evidence
content changed, and no additional defect was found.

| Final artifact | SHA-256 |
| --- | --- |
| `screen_pathbank_archive.py` | `c961933df7dbf980fe56ca1f19071a748bd58fa9f0595840ee6c13d5e0137cdc` |
| `pathbank-screening.tsv` | `d33dfe644a47172b0d58ed857b66d3574bfa03c63e2d72af402701cac3a8d547` |
| `pathbank-screening.json` (unchanged) | `9b567ea92e1b260d267ce168d27e22b71a49e11a00e60042158d5a97f7b8e93d` |
