# Pathway mechanism research: benzoyl-CoA degradation II (anaerobic)

## Pathway scope

**MetaCyc:CENTBENZCOA-PWY** is the complete seven-reaction anaerobic route
from benzoyl-CoA to glutaryl-CoA and acetyl-CoA. Benzoate activation is upstream
and subsequent glutaryl-CoA degradation is downstream. The distinct nine-step
P321 route is not substituted for this pathway.

The four organism contexts are Thauera aromatica (NCBITaxon:59405), its K172
strain (NCBITaxon:44139), Syntrophus aciditrophicus SB (NCBITaxon:56780), and
Rhodopseudomonas palustris CGA009 (NCBITaxon:258594). These are supported source
and enzyme contexts, not evidence that every listed organism experimentally
completes all seven reactions. Species, strain, experimental construct and
expression host remain distinct.

The actual merged-baseline duplicate assessment binds commit
`dd780ef273323efd638eacd63625963062e0b105` and its 262 complete maintained records,
plus 258 complete records in the preserved original checkout. Its 391-pattern
search includes hidden and ignored eligible text and decoded gzip contents,
with explicit Git/environment, binary and archive-interior limits. The two
scans retain 983 matching file occurrences, 553 distinct originals, 436 complete
content bodies and 9,956 literal offsets. No exact CENTBENZCOA-PWY or complete
selected seven-reaction route was found in that bounded assessment. This is
not a global pathway-source exhaustion claim.

## Mechanistic summary

The selected sequence is MetaCyc:1.3.99.15-RXN, MetaCyc:4.2.1.100-RXN,
MetaCyc:HADTHAUERA-RXN, MetaCyc:RXN-15012, MetaCyc:RXN-15013,
MetaCyc:1.1.1.259-RXN and MetaCyc:RXN-8032. All 32 material occurrences,
19 native material frames, six joins and seven pathway memberships are
represented. Reaction direction records the native equation orientation;
material edges follow the selected pathway traversal. The first two equations
are traversed right to left, and the remaining five left to right.

The graph contains 43 participants, four taxa, eight declared reaction nodes,
76 edges, 25 references and 117 evidence items including endpoint qualifiers.
The eighth reaction node, MetaCyc:OAHTHAUERA-RXN, is an auxiliary composite.
Its two formal constituents cancel CPD-15900 and produce the two-water net
hydrolysis. It is not an eighth pathway step or evidence for a freely released
intermediate or two separately characterized constituent catalysts.

The complete formal net is:

`benzoyl-CoA + CoA + 2 ATP + 2 NAD + 2 reduced ferredoxin cluster units + 5 water -> glutaryl-CoA + acetyl-CoA + 2 ADP + 2 NADH + 2 oxidized ferredoxin cluster units + 3 protons + 2 phosphate`.

The two generic ferredoxin coefficients count one-electron cluster redox units,
not two whole two-cluster polypeptides. The small-molecule elemental balance is
exact, while the carrier classes are not assigned fixed molecular formulas.
The retired Rhea 19097–19100 chain and its whole-carrier successors are not
exact replacements for the native equation. Formal joins do not establish
physical channeling or measured whole-pathway flux.

Thauera BcrABCD, Dch, Had and Oah retain their exact native enzyme and component
claims. Individual subunits are not assigned the complex's overall catalysis.
BamR and BamA retain the inspected tagged recombinant preparation on every
affected catalytic and composition endpoint. BamQ's exact SYN_RS14210/CDS and
NCBIProtein:WP_011418919.1 identity supports cyclic hydroxy-CoA oxidation,
with its E. coli BL21/pET101 preparation qualified. It is not the lower C7
dehydrogenase. BadDEFG has a genetic/sequence-supported `enables` edge rather
than a claim of purified intact-complex turnover.

Magnesium and generic protein-associated iron-sulfur CPD-7 preserve their source
cofactor scope. The existing CPD-7 identifier owner is unchanged. Intrinsic BCR
clusters, natural donor assays and the 1RGV donor structure are distinct
evidence. No FAD occupancy, fixed cluster ligation or whole-donor coefficient
is inferred. Historical Had zinc annotation remains separate from the measured
two-zinc-per-monomer result for a modern Strep-tagged, zinc-supplemented
recombinant preparation.

## Evidence table

The retained source and review packages preserve complete original bodies,
source locators, structure/sequence comparisons, explicit rejected mappings,
access failures and prior observations. Independent reviews retain their actual
reading scope and do not relabel an author's checks as independent evidence.

| Evidence | Completed scope | Interpretation boundary |
| --- | --- | --- |
| [Discovery](evidence-retention/packages/discovery/README.md) and [merged-baseline assessment](evidence-retention/packages/merged-discovery/README.md) | Exact seven-step route, alternatives and complete bounded match contexts | Shared substrates or reaction families do not make an adjacent route a duplicate. |
| [Chemistry](evidence-retention/packages/chemistry/README.md) and [independent review](evidence-retention/packages/independent-chemistry-review/README.md) | All selected equations, 17 exact molecular structures, two generic carrier classes and six joins | Unspecified stereochemistry and generic carrier scope remain explicit. |
| [Primary evidence](evidence-retention/packages/primary/README.md) and [independent review](evidence-retention/packages/independent-primary-review/README.md) | Source-specific biochemical, construct and taxon claims | Unavailable full texts and supplements are not called read. |
| [Native closure](evidence-retention/packages/native/README.md) and [independent review](evidence-retention/packages/independent-native-review/README.md) | Full activity/component context, exact issuing protein and CDS identity, structure interpretation | Sequence identity alone does not establish the assayed construct or reaction. |
| [Scientific design](evidence-retention/packages/design/README.md) and [independent review](evidence-retention/packages/independent-design-review/README.md) | All 76 edges, 117 evidence locators and four exact quotations | Acceptance covers the exact design and its explicit limitations. |
| [Authority preparation](evidence-retention/packages/authority/README.md) and [independent review](evidence-retention/packages/independent-authority-review/README.md) | All 56 named nodes; exact source/SQL projections and additive registry union | Identifier consistency does not establish biological catalysis. |

The authority union preserves all 3,153 prior source terms, 1,141 prior source
owners, 2,179 prior ontology terms and five ontology owners. It adds 32 source
terms and owners, 11 ontology terms and 32 manifest rows. The previous 1,322
manifest rows remain an exact ordered prefix. The complete external corpus of
262 baseline records plus this proposal passes the identifier consumer on
the final implementation. Independent implementation testing passed 2,077
regression tests and 66 additional adversarial probes. These are bounded
implementation checks; the full production gates are reported separately.

The maintained registry serialization preserves the previous key order and
Unicode formatting. A separate formatting successor proves strict whole-object
equality with the independently accepted proposals, exact preservation of every
prior owner/value and the ordered manifest prefix. It reduces the three-file
registry diff to 1,927 additions with no deletions. The original sorted proposals
remain immutable evidence.

## Gaps

The sixth reaction remains explicitly YES-PUTATIVE without a catalyst. C4
extract assays, BadH, Hcd1 structures and name similarity do not establish a
Thauera enzyme for this C7 reaction.

The seventh reaction does have a native PimB assignment:
RXN-8032 → ENZRXN-26773 → MONOMER-20679/G-58826 → UniProtKB:Q6N3H9.
The native protein comment describes a predicted R. palustris C7 function
without biochemical characterization. Operon-level evidence does not isolate
PimB activity. Both a categorical `catalyzes` edge and a single-protein `enables`
edge are therefore omitted, with the full native chain and reasons retained.
This is an evidence-scope decision, not a claim that the annotation is absent.

Full texts for PMID:10406950 and PMID:18312395 and specified supplementary
materials remain unavailable in the accepted source scope. The Oah inactive
GST construct wording remains unresolved. BcrA's contradictory deposited gene
qualifier is preserved beside its exact product/sequence identity. Thauera
K172 is distinct from Azoarcus KB740; R. palustris CGA009 is not silently
equated with CGA604. BadDEFG feeding uses the primary benzoate experiment,
rather than the erroneous copied native wording about supplied benzoyl-CoA.
Crystal sequence versions, partial entities and mutations remain distinct
from whole native proteins and biochemical preparations.

[Issue 590](https://github.com/CultureBotAI/PathwayMech/issues/590) records the
merged-discovery report's selection of superseded independent-native review
controls. The corrected scope is 12 complexes plus two monomer catalysts.
The native final identity replay differs only in completion timestamp, and
the two structure replay files are byte-identical. The original report remains
immutable; correction and independent acceptance are separate successors.
This finding does not alter the selected route or scientific conclusions.

[Issue 591](https://github.com/CultureBotAI/PathwayMech/issues/591) records an
independent evidence-retention finding. In the original proposal, 586 content
mappings across 301 inherited paths name the current merged commit while
retaining its predecessor's tree hash. Independent comparison recovered all
source bytes correctly; the defect is inconsistent machine-readable provenance.
The separate successor corrects exactly those 586 fields and the generator,
while preserving all other map values and the 250 optional-tree omissions.
Independent successor review accepted the fix with no new finding. The exact
3,343-file corrected payload is now integrated and its actual maintained
physical, compact and provenance checks pass. The complete 3,357-file original
preparation remains reconstructible. The [retention verification package](verification/retention/README.md)
preserves both independent reviews, author controls, root adoption results and
the original failures. Issues remain open until publication is verified.

## Candidate YAML

The complete maintained record is
[`benzoyl-coa-degradation-ii-anaerobic.yaml`](../../../data/pathways/benzoyl-coa-degradation-ii-anaerobic.yaml).
Its YAML SHA256 is
`e43e6ad5563c38af738e8f1c7b733510072b531196ce435395896b62951c6ab9`.
Serialization preserves the exact accepted design object, including every
node, edge, qualifier, reference, coefficient and source locator. No scientific
field was changed during YAML formatting.

## Verification and publication

The exact record and additive authority files are integrated in the owned
worktree. All 262 preceding YAML files are byte-identical to the merged
baseline; the corpus now has 263 records. Native history records document the
record and authority implementation. The exact YAML also passed the separate
closed-schema preflight before integration.

`just render-pages` passed for all 263 records. The native KGX export matches
the generated download files byte for byte. Complete direct comparison verifies
all 76 new edges, their evidence, references and qualifiers, plus all 56 local
node contexts. Every one of the previous 13,613 exported edge rows is unchanged.
Export fidelity establishes data preservation, not scientific acceptance.

The generated graph displays 60 nodes and 76 relationships: 50 mechanism and
26 context relationships. An isolated Chrome retry passed desktop/mobile
rendering, zoom and node selection with no runtime errors. Selecting the first
reaction highlights its 12 connected relationships at 100 percent while keeping
all graph relationships. The initial sandboxed launch failed before loading a
page; that failure is retained separately. Visual inspection found a dense
overview with small labels at 21 percent and legible focused labels at
100 percent. The viewport scrolls to the surrounding graph. This is a visual
smoke check, not an accessibility or cross-browser audit.

The complete retention source cutoff covers 17 frozen source/review packages
and 28 selected root snapshots: 7,337 physical source occurrences, 1,334
compact-only logical originals, and 4,339 compact rows across 11 explicitly
bound map versions. Independent byte recovery and the issue 591 successor
acceptance passed. The exact corrected payload has been copied into the
maintained worktree; all 7,337 physical occurrences, 4,339 compact declarations
and 502 inherited Git storage owners pass the actual retained readers. All
262 previous YAML records remain unchanged after adoption.
Later integration, gates and final reviews form a separate verification scope;
they are not retroactively claimed inside the earlier frozen source cutoff.

This report and the [integration verification archive](verification/root-integration/README.md)
are present in the maintained worktree, alongside the corrected source
retention and complete technical retention-review evidence. The native
`just vendored-check` passed all 22 artifacts selected by the pinned canonical
manifest.

As of this report's final gate update at **2026-10-15T17:49:55Z**, the complete
`just render-pages`, `just validate`, `just test`, `just lint` and
`git diff --check` run has passed. The [full gate evidence](verification/final-gates/README.md)
retains every complete command log, receipt and exact tested-input inventory.
All declared inputs remained unchanged through that run and archive adoption.
The earlier wrapper prerequisite error occurred before any gate ran and is
preserved separately. Actual staged-index checks are a later publication step.

Both independent reviewers found no new actionable defect in their completed
preparation scopes. Their [complete maintained-record preparations](verification/maintained-review-preparation/README.md)
preserve all 92 technical and 131 scientific files, including current retained
source ownership, report, history and generated-output checks. Their original
pending statements remain historical. Canonical scientific and technical review
persistence, PR publication and verified merge are subsequent steps; this dated
report does not claim they have occurred. No global pathway-source exhaustion
is claimed.


As of **2026-10-15T18:28:59Z**, the canonical [scientific review](../../../reviews/structured/20261015T175945Z-centbenzcoa-pwy-scientific/review.md)
and [technical review](../../../reviews/structured/20261015T180105Z-next266-independent-technical/review.md)
have been saved. Both completed with qualified passing verdicts and no findings
in their declared scopes. Their full construction and later documentation checks
are preserved in the corresponding verification archives; the earlier dated
pending statements above remain historical.

The first actual staged whitespace check then rejected six upstream contributor
biography lines in the new raw XML fixtures. [Issue 593](https://github.com/CultureBotAI/PathwayMech/issues/593)
records this publication defect. All eight fixtures now use deterministic gzip
storage, with all 106,540 original bytes recovered exactly. The existing manifest
and acquisition receipts are unchanged. The test loader verifies compressed and
decoded sizes and hashes before materializing temporary XML inputs.

The complete affected module passed all 234 tests and repository lint passed.
Independent review accepted the correction after 153 checks and 66 loader
rejection probes, including direct comparison to the staged and native originals.
The [complete fixture correction evidence](verification/fixture-storage/README.md)
preserves both packets, the original failed staging observation and their exact
before/after bytes. The original 5,489-pass full-suite run predates the loader
change; it is not represented as a new run of the corrected loader. All other
initial gate inputs are unchanged except this dated report and the fixture README.
The pathway, production code, authority snapshots and generated pages are unchanged.

A new canonical partial technical observation, final current validation, actual
successor staging, PR publication and protected merge remain subsequent steps.
Issues 590, 591 and 593 remain open pending verified publication. The following
nine-step pathway is being prepared separately; source exhaustion remains unproven.
