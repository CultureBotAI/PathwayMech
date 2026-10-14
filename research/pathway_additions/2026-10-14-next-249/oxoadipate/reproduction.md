# Reproducing the oxoadipate curation inputs

The authored record and all 18 original reference-byte bindings are identified in
`identifiers.json` and `reference-bindings.json`. The latter hashes distinguish
whole native objects, the full Rhea RDF archive, individual paper scans and an
author abstract HTML page. They do not treat failed PDF downloads as papers.

## Baseline and duplicate search

Start from baseline commit `40b878b91af87a41295bfa90c6bf72fd9efefecb`.
`preflight/baseline-record-bindings.json` enumerates every one of its 246 pathway
YAMLs, IDs, labels and hashes. `preflight/search-summary.json` retains all 42
exact ripgrep commands, statuses, match counts and file/line hits, including
hidden and ignored files. Replaying against a later checkout will also find
this newly added record/dossier, so interpret differences against the baseline.
The stated exclusions, binary handling and archive/symlink limits still apply.

## Original-source replay

Reacquire objects using the URLs in native, chemistry and primary source
manifests, then require their recorded SHA256 before interpreting the retained
locators. Source access and version changes may prevent byte-identical replay;
those changes need a new acquisition assessment rather than silently accepting
new bytes. Temporary absolute paths locate this session's originals and are not
a durable source archive. No source bodies, paper images, raw HTTP responses or
session cookies are committed in this dossier.

The native projection preserves exact membership, coefficients, activity links
and source directions. The chemistry assessment retains full structures,
charges, formula checks, reaction-side identities and representation caveats;
the Rhea projection retains the selected directional subjects and connected
RDF nodes. Chemical computations are evidence about deposited structures, not
new experimental metabolite identification. The adipate projection distinguishes
the chosen dianion from neutral adipic acid and does not identify an assay
stock's unmeasured protonation state.

Primary reading coverage, ten scoped claim dispositions, and access failures
remain in `primary/`. Literal source quotations occur only in the maintained
YAML. The ledger and allocation file store exact UTF8 text hashes, character
and whitespace-word counts, and YAML/source locators. Recompute these from the
actual record before accepting any later quote edit. Source-only papers in the
reading ledger are not thereby declared direct evidence for every graph edge.

## Canonical authorities

The unchanged repository builders and exact original invocations are recorded
in `authorities/canonical-build-commands.json` and the append-only
`ontology-v2-build-command.json`. For a relocated cache, substitute only the
external cache/output paths and preserve all source manifest hashes.

Reconstruct the ID-only selection from baseline snapshot keys in
`data/identifier_authorities/{sources,ontology}.json` at the baseline commit,
unioned with `authorities/planned-identifiers-v2.json`. Copy the 246 baseline
YAML files to a temporary corpus directory and add a selector with record ID
MetaCyc:PWY-2361 plus sorted `{id: identifier}` participant mappings. The
selector supplies no labels or biological assertions. Canonical builders obtain
labels only from their independently pinned originals.

The first source build and first ontology build used the same planned set
without CHEBI:17128. The second ontology build adds that adipate ID and preserves
the earlier output/receipt. `canonical-union-comparison-v2.json` establishes
that all 4776 baseline term objects, 752 source-owner objects and 928 ordered manifest
entries are unchanged; six new source owners and ten terms are added. The
integrated outputs are compared against the canonical bytes in
`actual-selection-reconciliation.json`; its seventeen actual named IDs exactly
match the final planned set. Source-only reference IDs are kept separate.

Build logs, raw source caches and environment-bound acquisition helpers remain
external; their receipt hashes are retained. Re-running builders requires the
original manifest inputs and pinned ontology databases, not just the small
output snapshots. The final enforcing identifier gate, complete validation,
rendering, tests and independent scientific review are separate root-owned
steps, recorded only after their execution. This dossier does not claim those
steps passed.
