# Pathway mechanism research: catechol degradation II

## Pathway scope

The candidate is **MetaCyc:PWY-5420 — catechol degradation II (meta-cleavage pathway)**, one connected seven-step oxidative route from catechol to carbon dioxide, pyruvate and acetyl-CoA. Its four-step PWY-5419 module joins the three-step PWY-5162 module. These children belong inside the full parent boundary and are not counted as additional pathway records.

The hydrolytic catechol degradation I route, the ortho-cleavage route and broader KEGG/GO entries remain distinct. A shared enzyme, intermediate or terminal module does not establish an exact pathway duplicate. The discovery assessment is preserved in the [source handoff](source-evidence/discovery/HANDOFF.md); the [merged-baseline successor](root-verification/dedup/HANDOFF.md) binds the addition decision to commit `fbccbdc027f2a86ad4919e9dbbb16a736cc0746a`. Both roots preserve all 258 expected record hashes, and all 872 matching-file instances have dispositions. No exact maintained whole-route duplicate was found within that scope. Searches include ignored and hidden files, subject to their explicit Git/environment, binary, archive and symlink bounds.

Native whole-pathway annotations, enzyme-source organisms, expression hosts and reference strains retain their separate scopes. The four grounded parent taxon annotations do not represent four new experimental demonstrations of the complete route. Historical mt-2 remains named context without a guessed NCBI Taxonomy identifier.

## Mechanistic summary

The formal sequence comprises catechol 2,3-dioxygenation, hydroxymuconate-semialdehyde oxidation, hydroxymuconate tautomerization, oxohexenedioate decarboxylation, dienol hydration, aldol cleavage and CoA-acylating acetaldehyde oxidation. The selected reaction identities are RHEA:17338, RHEA:34220, RHEA:33432, MetaCyc:4.1.1.77-RXN, RHEA:22582, RHEA:22625 and RHEA:23289. RHEA:22582 retains its right-to-left source orientation. Native reversible annotations remain distinct from the route traversal and from directional Rhea entities.

The [chemistry dossier](source-evidence/chemistry/HANDOFF.md) accounts for all 28 material-side entries, seven balanced equations and six exact intermediate joins. The calculated net equation has C69H94N21O50P7S and charge −6 on each side. This cancellation is chemical bookkeeping, not a measured elementary reaction or flux.

Native decarboxylation produces the 2Z enol, whereas its linked Rhea family produces a keto compound. The native reaction identifier preserves that difference. The rejected tautomerase cross-reference also has a different stereochemical scope. Formal structures, historical assay names and spontaneous conversions are therefore not treated as interchangeable. Root separately replayed the native XML, issuing structures and complete pinned Rhea directional equation search; these checks remain distinct from biological interpretation.

## Evidence table

| Package | Verified scope | Interpretation boundary |
| --- | --- | --- |
| [Discovery](source-evidence/discovery/HANDOFF.md) | Complete parent and child boundaries, seven reaction families and prior research mentions | A discovery proposal is not a maintained record or a source-exhaustion claim. |
| [Native closure](source-evidence/native/HANDOFF.md) | 343 complete META 27.0 originals, 5,148 direct slots and 629 required relation follows; 41 formal and 15 adjacent activities | Neighboring activities, database evidence codes and literature links do not automatically become experimentally established route edges. |
| [Chemistry](source-evidence/chemistry/HANDOFF.md) | Complete finite reaction equations, exact structures, 28 material facts and six joins | A formal entity match does not determine an unresolved historical preparation's initial tautomer or stereochemistry. |
| [Primary evidence](source-evidence/primary/HANDOFF.md) | 148 new claim/limitation rows, 50 predecessor dispositions and 19 targeted references | Full text, transformed publisher text, abstracts, inaccessible errata and figure inspection retain separate coverage limits. |
| [Biological identity](source-evidence/biological-identity/compact/HANDOFF.md) | 125 native biological objects, issuing counterparts and nine independently translated deposited CDSs | Exact sequence identity does not itself establish an assay, native assembly or physiological role. |
| [Additional chemicals](source-evidence/additional-chemistry/verification.json) | 21 requested endpoints: 13 exact source reuses and eight issuing comparisons | Chemical identity does not establish the sign of an enzyme effect or make assay reagents formal route participants. |

## Gaps

AP3 gene-name assignments disagree across the native database, deposited sequence, UniProt and primary papers, including an internal 2006 naming conflict. Exact accession and coordinate identities are retained; a convenient gene-name swap would obscure those differences. The modern 8IH6 engineered assembly has five hydratase and five decarboxylase chains with expression tags. It does not establish the exact stoichiometry of a historical native preparation.

CnbE/F chlorinated coupled-assay evidence is distinct from unchlorinated formal activities. NbaG remains a predicted homolog where an isolated assay was not found, despite a native experimental evidence code. Recombinant PraB/C/D assays do not independently demonstrate PraE/F/G activities. Historical XylH oligomer estimates, crystallographic assemblies and asymmetric-unit chain counts remain distinct.

The shared terminal module retains the primary NADH stimulation result for complex-associated DmpG, its preparation-specific metal effects and the explicit E. coli ADHE-CPLX exclusion. These observations do not establish direct nucleotide binding, universal metal dependence or exclusion of every protein called AdhE. Component donors and heterologous expression hosts do not acquire whole-route occurrence edges.

The 1971 Azotobacter study ends at pyruvate and acetaldehyde, not the final CoA-acylating step; unresolved coupled steps and synthetic-substrate stereochemistry retain their limits. An identified 2000 erratum remains inaccessible in full. Ambiguous historical numeric OCR and unavailable figures are not promoted into precise kinetics or structural claims.

## Candidate YAML

The initial [maintained draft](../../../data/pathways/catechol-degradation-ii.yaml) contains four source-annotated taxa, 123 participants, 49 reaction/activity/module nodes, 214 edges and 210 references. The [root integration receipt](integration/record-integration.json) binds SHA-256 `021069187297588d42fc144e192f572beeb2e9c7415196c9ebd79550c688dd3e`: it reconstructs the frozen primary preview exactly before six explicit issuing references, three accession/structure context paragraphs and two issuing-source evidence additions. All 185 native graph triples and their edge-level evidence arrays remain present after 33 explicit primary patches; 29 primary edges are added. Eight endpoint-qualifier evidence occurrences were replaced by primary-source construct qualifications, as accounted individually in the [scoped successor](integration/record-integration-scope-successor.json). The initial receipt remains an unchanged historical observation. All 198 primary claim dispositions and 26 narrative paragraphs are preserved. Shape and closed-schema checks passed; all 258 prior records remain byte-identical.

The [native author handoff](authoring/native/HANDOFF.md) and [primary author handoff](authoring/primary/HANDOFF.md) retain their source-to-record decisions. The [issuing structure context](integration/issuing-structure-context.json) distinguishes entry-reference hashes from separately bound polymer, assembly and mmCIF originals. The PraB alternative NADP coenzyme uses an existing exact ChEBI authority with explicit conjugate-base normalization; its protonation was not measured in that assay.

Independent review identified two minor provenance defects. [Issue 564](https://github.com/CultureBotAI/PathwayMech/issues/564) corrects ten printed-page locators for PMID:7868591; the [repair receipt](review-repairs/SCI-F01-repair.json) binds the current record SHA-256 `4931e9a8cc5ae9f55c434d942c70fc65c75ad73a49e878bd34fbcfc4250df110`. [Issue 565](https://github.com/CultureBotAI/PathwayMech/issues/565) clarifies edge-level evidence preservation and records eight intentionally replaced qualifier occurrences. Scientific claims, graph triples and identifiers are unchanged by these repairs. Independent acceptance, generated pages/KGX, full repository gates and publication remain pending. An initial draft is not counted as a completed addition.

The [selected authority handoff](authority-integration/HANDOFF.md) and [root promotion receipt](authority-integration/root-promotion-receipt.json) bind three exact promoted files. Both canonical builders passed. The proposal adds 63 source terms and six ontology terms selected by this record, preserving all 5,103 existing terms, 961 source owners, five ontology owners and the complete 1,142-entry configuration prefix. Root verified all 694 owned package files and 39 compact/original pairs. The initial real offline consumer passed on all 259 records; its original record observation remains immutable, and the ten-locator repair requires a separately bound successor check. Authority validation establishes identifier coverage and identity, not scientific approval.

## Retained artifacts

The [retention receipt](root-verification/source-retention-receipt.json) binds 290 retained artifacts to their external bytes. Root verified 1,183 manifest-bound files across the five frozen source packages, including hidden and ignored files, and checked every compact compressed entry against its original bytes before retention. The supplemental chemical result and root verification helpers are retained separately in the same receipt. Helpers are inert text.

Large downloads, full paper bodies and pinned SQL/RDF datasets remain external and hash-bound by the source manifests and source-specific receipts. Small originals selected by the compact manifests are retained as specified. Historical absolute paths identify acquisition context; retained relative paths identify repository copies. Author integrity checks and scientific judgments are not independent review verdicts. Licensing assessment for public release remains deferred.

The [author and duplicate-assessment retention receipt](root-verification/author-and-dedup-retention.json) verifies another 199 frozen package files and maps 134 retained artifacts, including 33 exact native patches, all primary claim/assay details, the complete merged-baseline duplicate dispositions and the root NADP issuing-original reuse. These preserve initial author observations without silently rewriting them.
