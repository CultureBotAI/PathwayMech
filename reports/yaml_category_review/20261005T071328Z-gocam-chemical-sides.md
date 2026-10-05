# YAML Category Review: Yeast GO-CAM chemical sides

- Repository: CultureBotAI/PathwayMech
- Category: All maintained yeast GO-CAM pathway records
- Selection Rule: Recursively enumerate `data/pathways/**/*.yaml`; select top-level `gomodel:` records with taxon `NCBITaxon:559292`.
- Started UTC: 2026-10-05T06:42:27Z (independent catalytic-source retrieval)
- Finished UTC: 2026-10-05T07:13:28Z
- Verdict: All 85 records and all 475 original activity occurrences assessed. Source-backed repairs applied; retained abstractions, authority conflicts and unspecified enzyme assignments are explicit.

## Target Category

This is the chemical-side supplement to the native GO-CAM, function, complex,
cofactor and compartment reviews. The user explicitly authorized editing all
causal graphs; that authorization supersedes the review skill's read-only default.
The work preserves each record's intended yeast pathway scope.

## Selection and Membership

The [complete disposition ledger](../causal_graph_review/gocam-chemical-dispositions.json)
contains one row for every original activity, with its record path and ID, original
comparison, final disposition, source pointers and amendment ledgers. The
[initial comparison](../causal_graph_review/gocam-chemical-review.json) contains
475 activities in 85 records. The
[final comparison](../causal_graph_review/gocam-chemical-final.json) contains
470 activities in the same 85 records: 440 original activities retained, 29 with
changed labels, chemical sides or enablers, six excluded, and one supported Vip1
activity added. These counts describe activity changes, not all evidence,
compartment, cofactor or material-flow edits. Filesystem recursion includes
ignored files; no sampled subset was used.

## Validation

Seven focused biochemical regressions pass in
`tests/test_gocam_chemical_identities.py`, covering FOX2/DCI1/ECI1 identity,
MAE1 versus MDH2, ARO8 transamination sides, PSA1 donor chemistry, ARG2/ARG7
labels, yeast dATP scope and COQ1 product length. Every changed record was
validated before publication. Seven new history files were created by the
repository scaffolder and corresponding curation-history entries appended.
Ruff passes the chemical audit and curation scripts/tests. The coordinator
reports final `just validate` passing all 152 records, 8,075 evidence blocks and
176 history records; the final full test/render checks are recorded in the
repository-wide handoff rather than claimed by this report.

## Lump and Split Review

No pathway records are merged. Enzyme-specific branches remain distinct where
independent chemistry requires it: DCI1 dienoyl isomerization is distinct from
ECI1 monoene isomerization, and MAE1 decarboxylating malate oxidation is distinct
from MDH2 oxaloacetate formation. Supported isoenzyme contexts are retained;
unsupported branches are excluded with their original assertions preserved.

## Identity and Grounding

The audit maps exact SGD cross-references to reviewed S288C UniProt entries,
expands represented complex components, and compares every chemical input/output
with all annotated Rhea catalytic families in both side orders. Exact ChEBI
identity, conjugate acid/base, protonation and broader/narrower class matches
remain separate. A low mismatch score is a review aid, not an equation rewrite.
The final report records source-byte hashes for UniProt, Rhea RDF, directional
correspondence and the ChEBI Semantic SQL authority. It does not derive
independent chemical labels from the corpus.

## Graph and Evidence Patterns

Confirmed errors include the PSA1 GDP/Pi versus GTP/diphosphate donor pair,
FOX2 S/R stereochemistry, DCI1/ECI1 conflation, ARO8 donor/acceptor sides,
MAE1 misassignment, wrong ARG2/ARG7 and COQ1 labels, folate methenyl/methylene
collapse, MET13 reductant specificity, inositol positions, yeast CRD1 chemistry,
THI13/THI4 single-turnover chemistry, ADK2 nucleotide donor specificity and
BNA3/LYS4 assignments. The linked amendment ledgers contain original assertions,
exact source locators and the bounded changes.

The imported unenabled formate-dependent ATP-to-dATP branch was excluded from
the yeast record. Direct characterization of yeast ribonucleotide reductase
supports diphosphate reduction (PMID:6370695); the formate reaction is class III
anaerobic chemistry and its appearance in a source model does not establish a
yeast enzyme. Qualified conflicts remain visible for STR2, FAS1 reductant
catalogs, URK1 nucleotide donor coverage and disputed URA6 CMP phosphorylation.

## Completeness Patterns

Every initial non-compatible or unannotated comparison has an explicit curator
disposition. Five retained source activities have unspecified exact enablers;
no enzyme identity is invented for them. Spontaneous steps do not require a
UniProt catalytic annotation. Protein-bound and polymer reactants remain
abstractions when the source does not resolve their exact state/length.

Seven retained native substrate-specificity contexts lack an independently
complete catalytic catalog; the ledger distinguishes broad FUNCTION support
from an exact substrate assay. Five tyrosol ADH branches specifically retain
native context with related-substrate support: the inspected PMID:12499363
abstract directly covers phenylalanine/tryptophan, not a tyrosine assay.
Two retained coupled redox contexts use NADPH
at pathway-system level while Rhea describes cytochrome/reductase partners.
These are RO `has_input`/`has_output` assertions, not balanced
`consumes`/`produces` equations or proof of direct enzyme contact. This review
therefore completes the bounded assessment without claiming complete
stoichiometry, physiological flux or specificity for every member of a broad
chemical class.

## Findings

The final ledger accounts for all 475 original activities and all 470 current
activities. Six original activities were excluded, 29 changed, and one added;
other changes qualify evidence and material flow without changing activity
identity. Remaining source limitations are explicitly scoped above and in each
row. No demonstrated chemical-identity contradiction is knowingly hidden by an
automatic class match or by a green schema result.

## Recommended Edits

The supported record edits are applied. Preserve the linked source exclusions,
reviewed cofactor overrides and distinction between literal quotations and
structured-source assertions. Do not restore discarded branches from the raw
model merely to reproduce its original edge count.

## Follow-up Checks

The coordinator regenerates pages/exports and runs the full suite after all
cohorts settle. Reproduce the numerical chemical comparison with
`scripts/audit_gocam_chemical_sides.py`, supplying explicit `--root`,
`--uniprot-json`, `--uniprot-provenance`, `--rhea-rdf`, `--directions`,
`--chebi-db` and `--output` paths. Source releases are UniProt 2026_03,
Rhea 139 and ChEBI 255. The JSON disposition ledger is the curator assessment,
not an automatic inference from comparison scores.

## Additional Notes

Amendment ledgers: `gocam-chemical-corrections.json`,
`gocam-chemical-final-supplement.json`, `gocam-function-review.json`,
`gocam-function-dispositions.json`, `gocam-assignment-conflicts.json`, and
`folate-inositol-chemistry-review.json`, all under
`reports/causal_graph_review/`. The five-record chemistry migration and
its two-record supplement preserve exact source hashes and preconditions;
they are bounded migrations, not general source importers.

Not checked: iModulonDB expression modules. This supplement establishes chemical
identity and enzyme scope; expression membership is not evidence for reaction
sides. No GitHub mutation or paid research call was performed. Reports live
under an ignored directory and require explicit inclusion in the final change.
