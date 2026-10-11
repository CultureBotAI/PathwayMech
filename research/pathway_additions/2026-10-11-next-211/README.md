# Complete desferrioxamine B addition

This cohort prepares the complete five-transformation **MetaCyc:PWY-6376** pathway
for *Streptomyces coelicolor* A3(2)/M145, with 25 participants, 50 mechanistic
edges, 130 evidence blocks and 44 references. The maintained owner is
`data/pathways/desferrioxamine-b-biosynthesis.yaml`.

The source boundary contains lysine decarboxylation, the proposed native
cadaverine hydroxylation, both succinylation and acetylation branches, and the
complete iterative DesD assembly of two HSC units and one HAC into desferrioxamine
B. Desferrioxamine E, uptake, iron loading and hydrolysis are separate processes.
The full source and identifier inventories are retained in the author dossier.

## Evidence and qualifications

The strongest primary support includes the original DesA abstract
(PMID:22906379), the 2018 DesC article and official supplementary document
(PMID:29685972), and the original 2023 DesD manuscript and supplement
(PMID:37207292). The complete 595-residue DesD construct bridge to Q9L069 is
independently supported by the 2022 supplementary sequences (PMID:35750210).
The source-native pathway, five reactions, proteins, complex and chemicals were
resolved from 17 original MetaCyc HTML bodies.

The native terminal reaction has the correct organic transformation but conflicts
with the primary-supported two-adenylation mechanism. The selected complete net
uses two ATP, two AMP and two diphosphate, with no net water. Both the original
one-ATP equation and the corrected equation balance; balance does not demonstrate
energetic coupling. The selected coefficient is a mechanistic derivation, not a
measured ATP/product ratio or an assertion of exact native-equation equivalence.

The coelicolor DesB activity remains a proposed native assignment, with generic
donor/acceptor classes and unresolved physiological donor specificity. Automatic
PLP/FAD annotations remain explicitly inferred. Cross-species donor kinetics,
assemblies, mismatched 2023 DesABC sequences and incomplete DesC construct
identity are not transferred to exact native proteins. Four equations have
concrete atom/charge checks; hydroxylation has only conditional generic-redox
bookkeeping. The author curation dossier retains all these distinctions.

The original iModulon responses place all four exact coelicolor loci in modules
35 and 57. This is computational expression context. Two original search queries
fail the unchanged canonical parser because their regulator field is null;
that failure is preserved, alongside successful native gene/table parsing.
Neither membership nor regulator labels become direct mechanistic edges.

## Initial review and correction

The initial independent canonical review is
`20261011T121520Z-desferrioxamine-b-initial-independent-review`. It is explicitly
partial and does not grant final scientific approval. Its one minor finding,
[issue #381](https://github.com/CultureBotAI/PathwayMech/issues/381), concerns two
DesC assay locators that cited Figures 2–3 instead of Figure 4(a)/(b).

Only the two `source_locator` strings on edges 029/030 were corrected. The exact
original target remains in `initial-review-inputs/`, and the author observations,
initial review and independent preflight remain unchanged. The correction receipt
and original-source replay prove that all other parsed record content is
identical. `verify-desc-locators.py` accepts an explicit original article path,
maintained record path and fresh output path; it checks the original source hash,
figure captions and the complete bounded record delta.

The copied author replay and validation are historical observations of the
external author draft. The author replay expects its original companion draft
files and writes its validation receipt; it must not be run in this maintained
dossier to overwrite that historical receipt. Original response bodies remain
external, with selected projections, source hashes and replay evidence retained
here.

## Integration sequence

Preparation began on aerobactin head `6647fd6`, before its unrelated page-history
correction. The canonical authority builders retained all baseline terms and
metadata while adding 17 native terms and two ontology terms. The manifest grew
from 459 to 476 inputs. The subsequent move to independently audited corrected
head `506c7ef` preserved every prepared file; the only intervening changes are
the aerobactin page-history item and its technical review evidence.

Those preparation steps do not claim that either head had already merged.
The actual merged-baseline equivalence, complete corpus gates, generated graph
audit, final linked independent review and publication are separate checks.
All record history events for creation and the locator correction precede the
planned final rendering.

Duplicate searches included hidden and ignored files in the current and original
checkouts, excluding Git object stores and dependency environments. The only
current exact-protein hit was an older cross-Mech Q9L069 annotation inventory,
which describes an unreviewed siderophore umbrella annotation rather than this
complete pathway. These bounded searches do not establish source exhaustion.

## Completed integration checks

The reviewed preparation baseline and actual aerobactin merge `75b6c586be91719f5d5d8db1183581403c36a485` have identical whole trees; all prepared files were preserved on the new branch. All seven canonical gates completed successfully, including **1131 passed, 3 skipped, 3 warnings in 371.65s (0:06:11)**. The vendored check passed all 22 governed artifacts. The independent graph audit verified 32 nodes, 50 edges, 130 evidence blocks and preservation of all 211 prior records. `integration-receipt.json` and lossless `console-transcripts.json` bind the exact observations. Final scientific successor review, PR checks and publication are separate steps. No record-history entry was added after the render.
