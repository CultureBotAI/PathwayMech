# Pathway mechanism research: benzoate degradation I (aerobic)

## Pathway scope

The candidate is **MetaCyc:PWY-2503 — benzoate degradation I (aerobic)**,
the two-step conversion of benzoate through its cis-dihydrodiol to catechol.
The three maintained catechol degradation routes begin at its endpoint and
remain separate records. Broader benzoate/methylbenzoate modules and aromatic
superpathways do not define this candidate's exact substrate boundary.

The [postmerge duplicate assessment](root-verification/postmerge-rebind/HANDOFF.md)
binds the decision to merge commit `3bd67d7cc30513e6b3cddc9b3696af0ef785fbdb`.
All 260 current records and 258 records in the preserved original checkout were
parsed completely. Their bytes, identities and reactions match the frozen
discovery comparison. Neither defining reaction family occurs in the declared
reactions, and the selected whole-pathway identity is absent. The repeated
91-pattern searches included ignored and hidden files and dispositioned every
match: 22 current files/42 lines and 10 original-checkout files/27 lines.
Git/environment exclusions, normal binary handling, archive interiors and
directory symlinks bound that search. This does not establish global source
exhaustion.

Native organism annotations, purified preparations, expression hosts and modern
sequence identities have different scopes. In particular, JMP222, historical
335, B9, C-1, mt-2, H16, ADP1, RW1, KT2440 and B1 must not be merged by similar
enzyme names. Native whole-pathway annotations do not demonstrate the complete
route experimentally in every listed organism.

## Mechanistic summary

The first selected equation, RHEA:12634, converts benzoate, NADH, a hydron and
oxygen to the stereospecified cis-dihydrodiol CHEBI:60129 and NAD. RHEA:11561
then oxidatively decarboxylates that intermediate to catechol and carbon dioxide
while reducing NAD to NADH. Both selected equations run left to right in the
native pathway. The substrate is oxidized in the second step; conflicting native
prose calling it reduced is retained as a source error.

The complete formal route contains 11 material-side entries, eight core chemical
identities and one primary-material join. NAD/NADH cancels in the sum:
benzoate + hydron + oxygen → catechol + carbon dioxide. Both net sides have
C7H6O4 and zero charge. This is stoichiometric bookkeeping, not a third elementary
reaction or measured flux. Issuing chemical structures establish the selected
absolute stereochemistry; historical cis-dihydrodiol observations alone do not.

The finite native design accounts for five activity contexts, 13 protein/complex
contexts, nine component links, eight genes, four cofactor annotations and one
location annotation. Components do not individually inherit whole-complex
catalysis. Two XylL activity objects share an enzyme/reaction pair but retain
their different source identities and evidence availability. Gene/product
context does not justify inventing an encoding predicate.

The protein-ligated cluster class retains MetaCyc:CPD-6; it is not equated with
the neutral Fe2S2 core CHEBI:33739. Native cofactor and assembly annotations
retain their preparation conflicts. Historical C-1 and 335 measurements are not
direct measurements of the source's JMP222 protein frames.

## Evidence table

| Evidence | Completed scope | Interpretation boundary |
| --- | --- | --- |
| [Discovery](source-evidence/discovery/HANDOFF.md) | Exact native boundary, alternatives and prior mentions | Initial unmerged comparison is superseded by the postmerge rebind. |
| [Native closure](source-evidence/native/HANDOFF.md) | 47 complete objects, 511 direct slots, 72 assertion proposals and 116 typed cross-references | Native annotation and its cited evidence code are distinct from primary experimental proof. |
| [Chemistry](source-evidence/chemistry/HANDOFF.md) and [independent assessment](independent-chemistry/HANDOFF.md) | Complete selected reaction families, all material entries, chemical identities and net balance | The original broad comparison defect is corrected separately below. |
| [Primary evidence](source-evidence/primary/HANDOFF.md) | 13 papers, 17 finite claim groups and explicit access/preparation limits | The 1971 and 2025 originals were inspected fully; the 1972 full text is transformed text plus an original first-page preview. |
| [Biological identity](source-evidence/biological-identity/HANDOFF.md) | 25 complete coding-region translations and 17 printed primary accession/locus pairs | Identity does not prove an assay construct, catalytic function or strain equivalence. |
| [A1501 primary follow-up](source-evidence/a1501-primary/HANDOFF.md) | Complete article, figures and supplement; 25 claim/disposition rows and 47 source-unit dispositions | Authored evidence requiring independent acceptance; benA is the measured transcript proxy. |
| [A1501 issuing identities](source-evidence/a1501-identity/HANDOFF.md) | Five exact coding-region translations, four KEGG gene crosswalks and the exact A1501 taxon | The 186 bp benA assay matches; four optional junction lengths disagree with the paper. |
| [Independent A1501 acceptance](independent-a1501-acceptance/HANDOFF.md) | Full original paper/supplement reading and an independently written identity/primer replay | Accepts the bounded source interpretations; final whole-record review remains separate. |
| [Independent primary review](independent-primary/HANDOFF.md) | All 17 claims, exact preparation limits, original figures/tables and identity checks | This is source preparation, not acceptance of a maintained draft. |
| [Assembly title](source-evidence/assembly-title/HANDOFF.md) | Exact CPLX-2541 native title through the unchanged HTML adapter | Whole-assembly identity is preserved; a software footer is not a database release. |
| [Record design](record-design/HANDOFF.md) | Full finite source-to-record dispositions | Final realization is assessed by the completed scientific and technical reviews below. |
| [Final record authoring](record-authoring/HANDOFF.md) | All 54 edges, 101 reference owners, native source dispositions and 17 + 25 primary claim groups | Author checks and exact reproduction do not replace independent scientific review. |
| [Authority integration](authority-integration/HANDOFF.md) | 45 selected source identifiers and 22 ontology identifiers; complete 261-record identifier check | Selected source reproduction preserves every historical authority value; it does not rebuild every historical source cache. |
| [Technical preparation](independent-technical-source-preparation/HANDOFF.md) | Source inventories, native slots, issuing originals and storage integrity | Final maintained-record, generated-output and gate acceptance remains separate. |

The [retention map](root-verification/initial-source-retention.json) accounts for
all 3,348 declared artifacts across 15 frozen packages. It maps original bytes to
their lossless maintained storage and preserves the frozen external manifests.
Those manifests describe the original packages; the retention map describes the
compact layout in this repository. No original finding or source body was
rewritten during integration.

An explicit [storage successor](root-verification/native-xml-storage-successor.json)
stores two native XML bodies as lossless gzip because their original curator
biographies contain trailing whitespace. It supersedes only their two retained
paths in the initial map. The original bytes and frozen external manifests remain
unchanged; the subsequent whole-directory whitespace check passes.

Separate retention maps preserve the later
[A1501 primary package](root-verification/a1501-primary-retention.json)
(315 declared artifacts, 157 lossless pairs) and
[issuing identity package](root-verification/a1501-identity-retention.json)
(81 artifacts, 40 pairs). The root replay reproduces the identity author's
bounded checks against the unchanged originals. Byte preservation and replay
do not substitute for scientific review. The independent A1501 source assessment
has since accepted the bounded primary interpretations and exact identities.
Completed whole-record scientific acceptance is linked below.

The author and authority packages have separate
[record-author retention](root-verification/record-author-retention.json) and
[authority retention](root-verification/authority-retention.json) maps. The
selected authority union adds 45 source terms and six ontology terms, plus 31
source-manifest entries. All prior terms, owners and 1,275 manifest entries remain
unchanged. The final totals are 3,136 source terms, 2,164 ontology terms and 1,306
manifest entries. Some earlier external cache symlinks have missing targets;
this addition neither repairs that cache nor claims a complete historical rebuild.

## Gaps

[Issue 572](https://github.com/CultureBotAI/PathwayMech/issues/572) tracks the
original chemistry comparison helper's omission of symbolic material terms.
The [append-only correction](source-evidence/chemistry-symbolic-successor/CORRECTIONS.md)
and [independent acceptance](independent-chemistry-successor-acceptance/HANDOFF.md)
replace that comparison with 37,068 complete fixed equations and 154 whole
exclusions, including the 148 formerly truncated cases. All selected chemistry
is unchanged. Parsed RDF closures are structural extracts, not original lexical
byte slices. The original defective result and failed successor attempt remain
preserved.

[Issue 573](https://github.com/CultureBotAI/PathwayMech/issues/573) tracks a
biological-metadata locator typo. The accession paragraph belongs to Methods 2.1,
DNA Techniques and Alignments, rather than Methods 2.3. Its
[one-field successor](source-evidence/biological-locator-successor/HANDOFF.md)
and [independent acceptance](independent-bio-locator-acceptance/HANDOFF.md)
preserve all other bytes, including all 17 identity rows. Both issues remain open
until the accepted corrections are published with the completed record.

[Issue 574](https://github.com/CultureBotAI/PathwayMech/issues/574) records a
minor field-locator error in the frozen reference-owner inventory: KEGG's
`benA` symbol belongs to `SYMBOL`, not `NAME`. The
[one-leaf successor](source-evidence/kegg-locator-successor/HANDOFF.md) and
[independent acceptance](root-verification/issue-574-independent-acceptance.json)
preserve all other inventory bytes and the unchanged pathway YAML. The original
finding and inventory remain retained; closure awaits publication.

JMP222 lineage, TW3 taxonomy, native NT4 versus published 4NT, the historical
testosteroni collection conflict, deleted UniProt entries and differing sequence
versions remain explicit. The 2025 helper-host, assay/control wording and
sampling inconsistencies are not silently resolved. RW1 BenD remains putative;
the first-step experiments do not demonstrate a unique physiological ferredoxin.
Negative growth/activity observations are not automatically inhibitory edges.
The proposed beta-ketoacid is not an observed pathway intermediate.

The completed source-author follow-up of PMID:20137101 supports A1501 BenR-dependent
benA expression, benzoate induction, glucose/acetate expression effects and a
separately qualified genetic rescue. It does not establish direct BenR binding,
a Crc mechanism, or direct enzyme activation by 4-hydroxybenzoate. The latter
compound's concentration-specific whole-cell growth/depletion observations remain
narrative context, distinct from downstream catechol and pca regulation.

The paper's HPLC material is filtered culture supernatant despite its
"intracellular" wording. Methods reverses the catechol/muconate retention-time
assignments printed in Figure 4 and the supplement, so those peaks do not provide
independent formal chemical identification. Figure 7 contains the expression
experiment despite an erroneous Figure 8 pointer. The exact benA primer product
matches 186 bp, while four optional junction-primer products differ from printed
lengths. These limits remain explicit in the record and source dispositions.
Independent A1501 source acceptance is complete, with these limits preserved.
The completed whole-record scientific review accepts these bounds. Public-release
licensing review remains deferred as instructed.

## Candidate YAML

The [maintained record](../../../data/pathways/benzoate-degradation-i-aerobic.yaml)
contains 67 named identifiers, 54 mechanistic edges, 12 endpoint qualifiers and
101 references. It is the exact author-validated successor with SHA256
`3f8bbb8eceaa4420fa822e87ce01cca6b9d1967908dc117628aba71f54030696`.
All 260 prior pathway records remain byte-identical. The complete author package
and verified selected authority union are integrated. Independent whole-record
science and technical integration reviews both pass with explicit limitations
and no open findings. Source-to-graph and graph-to-source coverage, exact
identifier consumption, generated diagrams and KGX are accepted. Additional
pathway candidates remain; no global exhaustion claim is made.


## Completed verification and reviews

The [scientific review](../../../reviews/structured/20261015T101855Z-next264-independent-scientific/review.md)
and [authoritative YAML](../../../reviews/structured/20261015T101855Z-next264-independent-scientific/review.yaml)
assess the entire maintained record. The
[technical review](../../../reviews/structured/20261015T101912Z-next264-independent-technical/review.md)
and [authoritative YAML](../../../reviews/structured/20261015T101912Z-next264-independent-technical/review.yaml)
cover authority integration, preservation and output fidelity, with scientific
self-review explicitly excluded. Both are completed observations with
`pass_with_limitations` and zero findings in their declared scopes.

The immutable [scientific proof](independent-scientific-review/HANDOFF.md) and
[technical production proof](independent-technical-production/HANDOFF.md) retain
original-source assessments, all 54 relationships, 12 qualifiers, 101 references,
71 graph display nodes and exact exported contexts for all 67 named identifiers.
Native KGX equals the published downloads. All 13,492 prior edges remain intact.
Desktop and mobile browser checks exercised zoom and node selection with no
runtime errors; screenshots cover finite viewports of the tall graph.

[Initial gate receipts](verification/initial-gates/receipts.json) record passed
`just render-pages`, `just validate`, `just test`, `just lint`,
`just vendored-check`, `git diff --check` and `git diff --cached --check`.
The full suite reported **5,255 passed, three skipped and seven warnings**.
The [preservation check](verification/initial-gates/final-input-preservation.json)
binds 4,403 unchanged tested files, including ignored and hidden files within
the declared scope. Later review, evidence and history additions receive
separate documentation checks; the pathway, authority and generated bytes
remain the tested bytes.

The [identifier and reference register](verification/identifier-and-reference-register.tsv)
lists every named node and reference declaration from the accepted YAML, with
[derivation provenance](verification/identifier-register-format-successor.json). Source
conflicts and deliberately excluded assertions are described above and in the
complete scientific review. This report records pre-publication acceptance;
PR merge state, landed-tree identity and owned-branch cleanup are verified
separately after publication.

Final canonical inspection and validation receipts are retained in the
[scientific completion package](independent-scientific-completion/HANDOFF.md)
and [technical completion package](independent-technical-completion/HANDOFF.md).
These preserve failed preparatory attempts and their corrections separately
from the successful final validations. No earlier review or source package
was overwritten.
