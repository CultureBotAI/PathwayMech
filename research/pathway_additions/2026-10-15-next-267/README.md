# Pathway mechanism research: benzoyl-CoA degradation III (anaerobic)

## Pathway scope

**MetaCyc:P321-PWY** describes the nine-reaction anaerobic route from
benzoyl-CoA to glutaryl-CoA and acetyl-CoA through saturated cyclic
intermediates. Benzoate activation is upstream and glutaryl-CoA degradation
is downstream. The seven-reaction CENTBENZCOA route is a distinct pathway;
only the first and final two selected reactions are shared.

The record has 62 participants, seven taxa, nine native reactions and one
separate auxiliary reaction: 80 declared identities, 100 edges, 64 references
and 196 evidence items including endpoint qualifiers. The source taxa are
Rhodopseudomonas palustris (NCBITaxon:1076), CGA009 (258594), Thauera aromatica
(59405), K172 (44139), Syntrophus aciditrophicus SB (56780),
Paramagnetospirillum magneticum AMB-1 (342108), and Geobacter metallireducens
GS-15 (269799). These are source and experimental contexts; the record does
not establish that all seven organisms complete the whole pathway. The final
two taxa identify separately assayed BadL homologs. Species, strain,
expression host and experimental construct remain distinct.

The duplicate assessment binds actual merge
`02bc234143d40e0e825737f27dfdcb5fd358322f`, tree
`08c04c1808980164ab90512f83e6e1c9bb5f16af`, and all 263 preceding records.
All 29,606 tracked baseline files were rebound to their immutable Git blobs.
The finite source-context assessment includes hidden and ignored files,
decoded archive contents, reconstruction of all three actual multipart source
archives, and explicit dispositions for 57 standalone archive errors.
Fifty-four are synthetic fixture objects, including six intentional corruption
controls. Their failures are not source-access failures. Compressed PDF/image
semantic interiors were not freshly OCRed. These checks support addition of
the distinct P321 record, not global source or literature exhaustion.

## Mechanistic summary

The selected sequence is MetaCyc:1.3.99.15-RXN, MetaCyc:R265-RXN,
MetaCyc:R266-RXN, MetaCyc:R267-RXN, MetaCyc:R268-RXN,
MetaCyc:1.3.1.62-RXN, MetaCyc:RXN-8031, MetaCyc:1.1.1.259-RXN and
MetaCyc:RXN-8032. All 42 material occurrences, 23 native material frames and
eight primary-material joins are retained. The first two equations are
traversed right to left and the remaining seven left to right. Native
reversibility annotations remain separate from the selected traversal.

The formal net is:

`benzoyl-CoA + 2 reduced ferredoxin cluster units + 2 ATP + 5 water + reduced ETF + 3 NAD + CoA -> 2 oxidized ferredoxin cluster units + 2 ADP + 2 phosphate + oxidized ETF + 5 protons + 3 NADH + glutaryl-CoA + acetyl-CoA`.

This is symbolic accounting under the native generic-carrier convention.
Two ferredoxin cluster units are not two whole two-cluster polypeptides.
Intrinsic BCR clusters, natural donors and complete donor proteins remain
separate. The net does not demonstrate complete physiological carrier
coupling, physical channeling or measured whole-pathway flux. Nineteen core
molecular identities and four native carrier-state classes preserve the
accepted structures, charges and unspecified stereochemistry. The lower
enoyl intermediate is specifically E; a broader E/Z-unspecified chemical
identifier is not substituted.

BadDEFG has a genetics-supported `enables` relation; the separate purified
Thauera BCR has a qualified `catalyzes` relation. The Syntrophus reverse assay
used artificial reductants, so it does not establish physiological ETF
turnover. BadK's crude extract, tagged BadH, purified BadI and all affected
construct endpoints retain their actual preparation scope. BadI's
approximately 90%-pure protein obtained by the shorter purification and
approximately 5% intended substrate in a chemical mixture describe different
quantities.
The four-stage preparation reached apparent protein homogeneity.

Lower-pathway PimCD, PimF and PimB assignments remain predictions.
The eighth reaction is present with its native putative status and all
materials, without an assigned catalyst. The 772-nt pimE pseudogene is not
converted into an active protein. Whole-operon evidence supports contextual
interpretation without demonstrating each isolated C7 activity or a unique
route; residual growth and the authors' caprylate-growth description remain
explicit.

Regulatory relations retain BadM repression of badD, BadR repression of
badH, cyclic keto-CoA effects on BadR binding, AadR-dependent expression,
and the genetic BadL/BadM relationship. No direct BadL–BadM binding,
BadM acetylation, AadR promoter binding or unmeasured physiological affinity
is inferred. Historical sequence variants and experimental deletion effects
are not silently assigned to a different allele or construct.

All three measured acetamidobenzoic-acid effects on BadM DNA binding are
represented: PubChem:6971, PubChem:48847 and PubChem:19266. Their neutral
reagent identities remain distinct from formal anions and depicted
zwitterions. The nominal 10 mM EMSA conditions, 72 nM BadM, 12 nM 212-bp
probe, ortho 5 mM negative result, and meta/para solubility limitations
remain explicit. These experiments do not identify a physiological ligand
or establish an affinity ranking.

The separate RHEA:28551 auxiliary activity has four material edges and two
homolog-specific catalyst edges:

`anthranilate + acetyl-CoA(4−) -> N-acetylanthranilate + coenzyme A(4−)`.

All coefficients are one and the formal elemental and charge balances are
zero. Q2W1S9 from AMB-1 and Q39TU9 from GS-15 retain their actual
preparations. This activity has no P321 membership or precedence relation;
it is not a tenth native step. Both homologs' meta/para acetylation evidence
is retained with unresolved exact activity identifiers. Only the MmBadL
meta product had the reported direct HPLC/MS comparison. Below-background
kinetic signals do not support substrate preference or kinetic constants.
Inconsistent native RpBadL activity does not support a purified native
catalysis edge.

## Evidence table

The [retained evidence package](evidence-retention/README.md) preserves the
original source bodies, authors' analyses, independent reviews, explicit
correction successors and bounded root preparation receipts. Its
[source-package inventory](evidence-retention/source-package-inventory.json)
and [role ledger](evidence-retention/owner-roles.json) keep authorship,
independent acceptance, historical observations and reused inputs separate.
Four original ontology databases are explicitly outside the retention cutoff;
their pinned identities, derived outputs and build receipts are preserved.
A complete ontology rebuild still requires those external originals.

| Evidence family | Accepted scope | Interpretation boundary |
| --- | --- | --- |
| Discovery and actual merged-baseline assessment | Exact nine-step route, adjacent routes, all 263 prior records and finite hidden/ignored archive context | Shared components do not establish pathway equivalence; no global absence claim. |
| Chemistry and native identity | Every selected equation, molecular structure, carrier convention, exact sequence/CDS and source component context | Native classes, unspecified stereochemistry, constructs and variants are preserved. |
| Primary evidence and corrected claim placement | All 28 primary claims, 76 source leads, eight explicit prior-claim reuses and 15 design obligations | Unavailable full texts and supplements are not presented as read. |
| Regulatory chemistry and independent review | Three BadM ligand effects, two homologs, exact ortho activity and qualified meta/para evidence | Nominal concentrations, physiological uncertainty and unresolved exact activity identifiers remain explicit. |
| Complete design and accepted correction successor | All 100 edges, 64 references and four full-design review corrections | The original needs-curation verdict remains immutable; acceptance applies to the corrected successor. |
| Authority implementation and full union review | Complete source/ontology builds, all 80 identities and additive ordered registry integration | Identifier consistency does not itself establish biological catalysis. |

The full authority union preserves all 3,185 prior source terms and 1,173
source owners, adding 36 of each. It preserves all 2,190 prior ontology terms
and five owners, adding six terms. The previous 1,354 manifest rows remain
an exact ordered prefix of 1,390 rows. Complete source and ontology rebuilds
and independently reconstructed outputs agree. Permutation checks apply to
new source additions while preserving prior first-owner order. The corrected
264-record identifier-consumer replay reports no errors.

The implementation correction also preserves ordinary legacy protein
products when a new native gene points to them. Exact companion provenance
and the narrowly permitted legacy metadata shape are verified; wrong
source kinds, identifiers, release metadata, hashes and extra fields remain
rejected. Independent correction review passed 254 dedicated adversarial
cases and 697 selected tests. Those are bounded checks, separate from the
full maintained-repository gates.

## Gaps

The eighth catalyst, direct lower C7 Pim activities, physiological ETF
coupling and BadM's physiological ligand remain unresolved. Exact meta/para
homolog-acetylation activity identifiers are not closed by the finite pinned
Rhea 142 search. No local identifiers or mismatched ortho activity are used
to fill those gaps. Exact missing tag/linker details remain unknown.

PMID:15186151 has indexed abstract scope; PMID:10903310 supplies the exact
abstract spectroscopy statement rather than a three-paper chronology.
ThnL context was retained as rendered main text, not a complete raw paper
and supplement. The specified 2013, 2018, 2024 and ThnL supplements were
unavailable within the accepted preparation. Eight prior claims are explicit
reuse rather than new complete readings. Public-release licensing remains
the separate later decision requested by the user.

Review findings are tracked in issues 587–589, 592, 594–596, 598–605.
Accepted successors correct source scope, protein/chemical distinctions,
claim locators, allele attribution, ordered-owner testing, legacy product
handling, four bibliography titles, displayed prose and six synthetic
fixture-member receipts. Original observations remain retained. No issue
closure is implied before verified publication.

[Issue 604](https://github.com/CultureBotAI/PathwayMech/issues/604) identified
acceptance of missing or incomplete historical declarations and altered
ownership metadata in the proposed standalone decoder.
[Issue 605](https://github.com/CultureBotAI/PathwayMech/issues/605) identified
scratch-path escapes through traversal or symlink ancestry. The accepted
correction derives the complete 477 historical declarations and 926 paths from
pinned Git records and both original copied manifests, preserving their owner
roles. Destination checks reject unsafe paths before creation. All 78 independent
rejection controls and complete corrected reconstruction passed; unsafe probes
made no outside-scratch writes. Every source byte and storage mapping remains
unchanged. The [independent correction review](verification/retention-successor-review/README.md)
retains both explicit resolved dispositions and the original needs-curation
observation. Issue closure remains tied to verified publication.

## Candidate YAML

The maintained record is
[`benzoyl-coa-degradation-iii-anaerobic.yaml`](../../../data/pathways/benzoyl-coa-degradation-iii-anaerobic.yaml),
SHA256 `40fa37e63c5be6ec6c9d33bf67f4bf06e597fc4c9b12514d34401379b124ad51`.
Its exact bytes match the independently accepted correction successor.
All 263 prior record files remain byte-for-byte unchanged. Native history
records document the new pathway and authority profiles.

## Verification and publication

The actual maintained site rendered all 264 records. Native KGX exports
match the generated downloads byte for byte. Direct comparisons cover all
100 new edges, every evidence/reference/qualifier payload and all 80 local
node contexts; all 13,689 prior exported edge rows remain unchanged.

The generated graph displays 92 nodes: 73 base pathway, participant and
reaction nodes plus 19 qualified endpoint occurrences. The seven taxa remain
component-table context. Its 100 relationships comprise 73 mechanism and 27
context relations. Isolated Chrome
checks passed on desktop and mobile with no runtime errors. Zoom and node
selection work; selecting the first reaction highlights its 12 connected
relationships at 100% while retaining the whole graph. Visual inspection
found the 15% overview dense and focused labels readable. The graph scrolls
within the viewport. This is a visual smoke check, not an accessibility or
cross-browser audit. An unused declaration-class counter in the helper was
explicitly corrected in the assessment to the actual context-class count.

The native vendored-file gate passed all 22 artifacts against canonical
revision `a5d562962c75a2ad9efd8160b548df5944315422`.
Full maintained `just validate`, `just test`, `just lint` and `git diff --check`
passed. The test run finished with 5,965 passed, three skipped and seven warnings.
All 29,580 declared tested inputs remained unchanged, including hidden and ignored
files within the recorded scope. The complete terminal receipts and input
inventories are retained in [native gate evidence](verification/initial-gates/README.md).
[Integration evidence](verification/root-integration/README.md) preserves the
actual graph/export observations and their limitations. The
[scientific review preparation](verification/scientific-preparation/README.md)
retains its original partial observation; it is not the final canonical review.

The accepted evidence package was adopted exactly: 5,969 files with payload
manifest SHA256 `11a6f52cfa2d6afd5ed51d641d4b33eb59220422e5dc251536bb817891a7a1ce`.
The subsequent native lint gate identified one overlong decoder string literal
([issue 606](https://github.com/CultureBotAI/PathwayMech/issues/606)). The explicit
[formatting correction](verification/decoder-lint-correction/README.md) preserves
the entire module AST and all 5,967 other payload files. Only the literal layout
and its manifest binding changed. That formatting successor had payload manifest
SHA256 `e99337264ef70fd72555b4e10928584909e5830c00e41d5566c6b7c5b90f5a4a`.
The later staged whitespace check found required blank-context spaces in a
retained unified diff ([issue 607](https://github.com/CultureBotAI/PathwayMech/issues/607)). The explicit
[lossless storage successor](verification/publication-storage-successor/README.md)
stores that exact diff as deterministic gzip and updates its physical-manifest
entry. All 5,967 other payload files, including the decoder and all source maps,
remain unchanged; all 5,969 predecessor files can be recovered exactly.
The current physical payload manifest SHA256 is `919fa2b0315177894ba222761f671c55fcc9b5e6e4498a8d9fcbf43a610b8e74`.
The earlier canonical reviews retain their original working-tree cutoffs; a
separate bounded technical review assesses this storage transition.
The predecessor maintained decoder independently passed complete offline verification
of all 13,577 original physical occurrences, 6,175 current compact declarations,
477 historical pairs and 926 historical paths. The
[technical preparation](verification/technical-preparation/README.md) preserves
its earlier partial assessment and declared cutoff.

Source packaging, maintained integration, final documentation checks and
canonical scientific/technical reviews have distinct recorded cutoffs.
Commit, PR, protected merge and issue closure require their subsequent verified
observations; this source report does not claim those publication outcomes.
