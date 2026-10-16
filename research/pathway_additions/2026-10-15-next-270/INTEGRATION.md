# Maintained H2/CO2 methanogenesis integration

The new record `MetaCyc:METHANOGENESIS-PWY` represents the native six-reaction
route from H2/CO2 to methyl-CoM. Its 125 evidence-bearing edges connect 101
biochemical nodes; three direct taxon associations bring the KGX node count to
104. The generated diagram has 101 nodes and 125 links. The three unconnected
taxa remain in the ordinary record page and KGX export.

The record preserves the source's directions, cofactor conflicts, reaction and
material occurrence details, and the reviewed limits on chemical, taxonomic,
strain and primary-literature interpretation. It does not add adjacent methane
formation or regeneration reactions to this six-member source definition.
Top-level triples have no typed occurrence coefficient or compartment fields;
the complete incident descriptions, evidence and retained ledgers carry those
source details. Catalog associations are explicitly qualified where independent
experimental support is unavailable.

A guarded native-XML authority adapter adds 92 verified native identifiers and
three taxon authorities. All previous authority entries retain their values and
ordering. All 266 earlier pathway records and their individual record pages are
unchanged; generated aggregate pages and downloads include the new record.

The [canonical maintained scientific review](../../../reviews/structured/20261016T025354Z-methanogenesis-maintained-record-review/review.md)
records `pass_with_limitations` with zero findings. It binds 792 direct source
inputs and separately documents the exact indirectly bound percent-named receipt.
Its YAML and Markdown were saved by the governed review tool. The final check
validated all 195 saved reviews within their declared scopes.

The [terminal gate receipts](final-verification/gates.json) record passing
`just render-pages`, `just validate`, `just test`, `just lint`,
`git diff --check`, `just vendored-check` and the corrected staged whitespace
check. The full suite passed **7,149 tests**, with **3 skipped** and **7 warnings**.
All 704 integrated owners were hashed again after the gates. Final evidence
packaging and this integration note follow those checks; the publication receipt
will bind the complete staged tree. No full-suite rerun is claimed for packaging.

The original source bytes are preserved. Issue
[#626](https://github.com/CultureBotAI/PathwayMech/issues/626) is corrected in the
record's root and incident paper locators. Issue
[#628](https://github.com/CultureBotAI/PathwayMech/issues/628) is corrected by a
narrow directory-local attribute for exact upstream XML end-of-line spaces.
Both fixes have independent acceptance. Original failed attempts and their
passing successors remain in the evidence; the issues stay open until the
actual merged tree is verified.

The preparation [README](README.md) keeps its original cutoff and scope.
Later page/export and source-byte reviews are retained in
[maintained-review-preparation](maintained-review-preparation/README.md), with
canonical review execution in [canonical-review-preparation](canonical-review-preparation/README.md).
Archive inventories cover every physical outer file, including hidden and
ignored files; nested containers are opaque unless a particular review declares
otherwise. These finite checks do not establish source exhaustion. Page QA
covers generated structure, complete no-JS text and exports; no browser or pixel
readability audit is claimed. Public-release licensing review remains deferred.
