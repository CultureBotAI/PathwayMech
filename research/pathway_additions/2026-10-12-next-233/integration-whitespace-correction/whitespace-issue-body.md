## Finding

Stable issue key: `thio-integration-raw-source-whitespace` (P2 / bounded packaging).

The prepared THIO dossier includes raw whole-source XML/HTML copies under
`research/pathway_additions/2026-10-12-next-233/new-source-originals/`.
Ten of the 23 original files contain upstream trailing whitespace. A read-only
`git diff --no-index --check /dev/null` against the proposed whole THIO pathway
HTML reports the whitespace errors and exits nonzero. The required maintained
`git diff --check` gate would therefore fail after staging these new files.

The scientific originals must remain byte-exact. Trimming the source bodies
would invalidate their accepted source hashes. The bounded correction stores
all 23 bodies using deterministic gzip, records repository-relative maintained
owners and serialization, and verifies that decoded bytes recover each exact
original size/hash. The accepted source snapshots, record and runtime are unchanged.

This was found before maintained adoption. The sealed first preparation remains
unchanged and is superseded by a separately reviewed integration successor.

## Acceptance checks

- All 23 decoded source originals recover their accepted exact bytes.
- All 116 references remain resolvable from the proposed repository payload alone.
- Every new maintained text file passes a whitespace preflight.
- Actual full maintained gates and final staged whitespace check pass after adoption.

Evidence: external `whitespace-finding.json`, its retained actual command streams,
the sealed predecessor, and the successor's lossless-conversion/portable replay proofs.
