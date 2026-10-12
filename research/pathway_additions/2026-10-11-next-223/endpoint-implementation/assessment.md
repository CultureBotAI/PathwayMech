This external implementation preserves endpoint qualifications as part of the
complete edge claim across the native validator, closed LinkML schema, record
text, interactive/static graph and KGX export. It contains 12 proposed files;
`implementation-files.json` records their exact before/after hashes. The separate
complex naming implementation is not overlaid or modified here.

The optional list accepts zero, one or two qualifiers. Roles are `subject` and
`object`, each at most once; kinds are `experimental_construct` and
`molecular_state`. Descriptions must contain text and be at most 400 characters.
Evidence uses the existing grammar and locally declared references. Native
validation permits only explicitly typed protein/complex participant endpoints;
ambiguous declarations across record/taxon/reaction roles are rejected. The
closed schema checks structure, enums, length, cardinality and Evidence fields;
record-local endpoint typing, role uniqueness and reference resolution remain
native-validator responsibilities, as the schema documentation explains.

An existing Evidence reference-type check is made explicit so malformed
unhashable references produce a ValidationError rather than a TypeError. No
reference, identifier or label-policy exception is introduced. Qualifier objects
have no biological-ID slot. Curation guidance prefers exact issuing state IDs
and explains the experimental sequence and occupancy limits.

Record pages render each qualification and its full evidence beside the correct
subject or object. A native HTML details disclosure contains the evidence, so
it remains available without JavaScript. Graphs keep declared base nodes and
create scoped display instances only for qualified incident edges. Those
instances display a construct/state label and a description preview; complete
description, support and locators remain in accessible graph details and the
linked endpoint cell. Display keys are not biological CURIEs and never appear
as KGX endpoints or nodes. The node picker displays the native ID. The existing
JavaScript uses the scoped display keys, preventing selection of the base node
from highlighting a qualified claim as if it were unqualified.

KGX appends a non-lossy `endpoint_qualifiers` JSON column and includes
qualification-only citations in source/reference metadata. Qualified edge IDs
include the complete payload. Subject/object list order is normalized for
identity but preserved in exported JSON. Empty/absent lists retain previous
edge IDs and values. The reusable WikiPathways dedup helper shares the same
qualification key; source extraction itself is unchanged. The provenance
command counts qualifier Evidence blocks as well as primary edge Evidence.

The baseline is actual pending working bytes from
`/private/tmp/pathwaymech-next-222-20261011` at HEAD
`d8e3888528088e7bba468df57056f9f0e588b463`, including accepted Salvage II work.
It is not a claim about HEAD bytes or the eventual merged baseline. Preparation
copied and bound 1042 original inputs, including the current 223 records,
history, generated pages, and the author's proposal/examples. No shared cache
was needed or written. A later actual merged-baseline bridge and combined
candidate scientific/canonical replay remain required.

The first focused run passed 239 tests. Initial lint attempts identified line
length only; exact code, hashes and receipts are retained under
`initial-attempt/` and `cli-test-lint-attempt/`. A rejected apply_patch transaction
made no edits and its cause is recorded. The final runner records complete
subprocess stdout/stderr and actual exit codes under `validation-run-1/`.
Its `result.json`, focused-test receipt and legacy output accounting establish
the completed result; an intermediate log is not success evidence.
The final nine-suite run passed 286 tests in 293.84 seconds, Ruff passed, and
all 2895 validation input bindings were rehashed unchanged. The runner exited
0 in session 54458, terminal chunk f455d9; the terminal receipt records this
separately from subprocess receipts.

The final focused coverage includes native/closed schema controls, qualifier
role/type/Evidence rules, non-JavaScript placement and escaping, graph instance
identity and interactions, JSON roundtrip, qualifier-aware identity/dedup,
qualifier-only citation metadata, and real CLI failures before output mutation.
The author's exact four-edge/seven-endpoint examples are separately bound and
replayed. Ten negative mutations cover qualifier loss, valid-but-wrong role
swaps, Met1 restoration, lost Evidence, lost tags/state, duplicate roles, bad
kinds/references and flattened input. Generic schema validation deliberately
does not pretend to infer the missing scientific qualifier or reject plausible
but wrong wording; those controls use the source-specific accepted example
contract. The examples are not acceptance of the author's complete pathway.

The external whole-corpus renderer checks all 223 existing records. Existing
record pages and nodes.tsv remain byte-identical. Every previous edge cell and
ID remains equal after removing the new empty column. The edge TSV bytes,
download manifest and homepage export fingerprint change, as required by the
new column; the report accounts for those changes rather than claiming all
legacy output bytes are unchanged. No current-worktree gates are rerun.

Visual inspection of the generated example SVG confirmed distinct construct
and state instances, readable labels, directed edges and retained base nodes.
The standalone PNG is a layout diagnostic; the full page supplies the maintained
site's styles and accessible evidence links. Long qualification descriptions
are previewed in node labels and available completely in details and text.

Limits: the native grammar cannot determine biological truth. Downstream KGX
consumers must retain the qualification JSON or explicitly reject/omit the
qualified claim. Historical one-off curation migrations are not generally
retrofitted: the MetaCyc reconstruction is pinned to a 50-record reviewed Git
baseline, the diagram migration has fixed 16-record/baseline guards, and the
GO-CAM review scripts select gomodel records. Their private transformation
functions are not supported generic qualification-preserving consumers. Reuse
on qualified records needs separate review; they are not invoked here.

No maintained records, snapshots, pages, cache, native history, Git metadata or
GitHub state are written. Parent-owned independent review and adoption remain
separate from this external implementation.
