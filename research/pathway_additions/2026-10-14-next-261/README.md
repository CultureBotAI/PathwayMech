# Pathway mechanism research: catechol degradation I

## Pathway scope

The candidate is **MetaCyc:PWY-5415 — catechol degradation I (meta-cleavage pathway)**. It comprises one connected five-step hydrolytic route, joining the native P183-PWY entry module to PWY-5162 and ending in formate, pyruvate and acetyl-CoA. Its child modules are not counted as separate additions. GO:0019616 is broader than this exact route; the oxidative sibling PWY-5420 remains separate.

The [current duplicate assessment](root-verification/dedup/final-disposition.json) binds the search to merged commit `62b8798b0044f422a59f1527b0801ff09a27d368`. The search included ignored and hidden files, with explicit exclusions for root Git metadata and the root dependency environment. All 257 maintained record hashes and all 329 matched file hashes across the isolated worktree and original checkout match the prior reviewed inventories. No exact maintained pathway or complete defining reaction set was found within that scope. Existing mentions concern research leads, source inventories, authority coverage, or distinct routes sharing a terminal module.

Whole-route organism annotations, enzyme-source organisms, reference strains and expression hosts require separate evidence. Combining experiments from several preparations does not demonstrate the complete pathway in each organism.

## Mechanistic summary

The formal route contains catechol 2,3-dioxygenation, semialdehyde hydrolysis, dienol hydration, aldol cleavage and CoA-acylating acetaldehyde oxidation. The [formal chemistry proof](source-evidence/formal-chemistry/HANDOFF.md) selects RHEA:17338, MetaCyc:3.7.1.9-RXN, RHEA:22582, RHEA:22625 and RHEA:23289. RHEA:22582 is the right-to-left member of its issuing family; the other selected Rhea members are left-to-right. Native reversible annotations for the terminal reactions remain distinct from the selected pathway traversal.

The native hydrolase produces the formal 2Z enol, whereas its linked Rhea hydrolase family describes the keto compound. The native reaction identifier preserves that difference. Parent-pathway narrative also mentions a distinct 2E enol. Exact source structures distinguish these entities; historical assay names and unassigned stereochemistry do not establish interchangeability. All 21 formal material-side facts and five equations balance. The calculated net equation is bookkeeping evidence, not a newly measured elementary reaction or flux.

## Evidence table

| Package | Verified source scope | Interpretation boundary |
| --- | --- | --- |
| [Discovery](source-evidence/discovery/HANDOFF.md) | Exact pathway boundary, five-step connectivity, corpus inventory and prior-mention dispositions | Discovery is not a maintained addition or a claim that all sources are exhausted. |
| [Native closure](source-evidence/native/HANDOFF.md) | 217 complete META 27.0 objects; 399 required follows; 45 activities and 2,986 direct slots | Formal and adjacent activities remain distinct; extracted assertion candidates are not automatically graph claims. |
| [Formal chemistry](source-evidence/formal-chemistry/HANDOFF.md) | 16 complete native compounds, all 20 Rhea family members, 21 material-side facts and net balance | Formal structures do not determine the stereochemistry or initial tautomer in a historical assay preparation. |
| [Primary evidence](source-evidence/primary/HANDOFF.md) | 50 located claims from 12 sources, including three complete publisher-transformed main texts | Abstract-only, partial-text and metadata-only readings retain their explicit limits. |
| [Biological identities](source-evidence/biological-identities/HANDOFF.md) | 96 native biological objects, issuing protein/gene/taxon counterparts and version comparisons | Sequence or identifier correspondence alone does not identify an experimental construct or establish whole-route occurrence. |
| [Chemical participants](source-evidence/chemical-participants/HANDOFF.md) | 22 native endpoints, 37 roles, all 50 primary-claim dispositions and 11 assay contexts | Adjacent-enzyme inhibitors, analytical reagents and alternative substrates do not become formal route inputs or outputs. |

## Gaps

The frozen primary dossier distinguishes full transformed text from raw PDF bytes and visual figure inspection. Its structural paper is partial, several sources are abstract-only, and one historical paper is metadata-only. Later successful acquisitions belong in explicitly identified successor packages. A failed or challenged web response is not article evidence.

The native NADH inhibition annotation conflicts with the inspected CF600 primary preparation, which supports stimulation of complex-associated aldolase. The primary result does not establish direct nucleotide binding or an allosteric transmission mechanism. Mn2+ stimulation, Zn2+ inhibition, negative Mg2+/Ca2+ tests and EDTA controls remain preparation-specific. Biological DmpFG tetramer composition is distinct from a catalytic heterodimer and the crystal asymmetric unit.

The native terminal module explicitly excludes E. coli ADHE-CPLX as a route catalyst; this exclusion does not apply to every unrelated protein called AdhE. Bordetella decarboxylase inhibitors must not be assigned to its associated hydratase. Historical PKO1 regulatory names, plasmid constructs and host measurements require their own identity and preparation dispositions. Named but ungrounded regulators cannot acquire invented CURIEs.

## Candidate YAML

The integrated [maintained draft](../../../data/pathways/catechol-degradation-i.yaml) contains 8 source-annotated taxa, 60 participants, 37 reaction/activity/module nodes, 128 edges and 79 references. The [integration receipt](integration/record-integration.json) binds its initial SHA-256 `38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255`, preserves all 112 native and 16 primary edges, checks all 58 primary claim dispositions, and verifies the 21 formal material facts and five-step membership/order against their originals. Python and closed-schema checks passed at integration. These author checks do not establish an independent scientific verdict or full repository validation.

The [native author package](authoring/native/HANDOFF.md) accounts for all 3,139 source slots, 132 mechanism candidates, 165 prose paragraphs and 80 features. The [primary author package](authoring/primary/HANDOFF.md) adds the complete transformed 1996 TbuE paper and preserves the distinct 1991 crude-extract and 1996 partially purified preparations. The [taxon selection](root-verification/taxon-integration-selection.json) preserves eight exact issuing identities from parent-pathway species annotations without treating them as eight independent whole-route experimental confirmations. Historical mt-2 has no supplied taxon cross-reference and is retained as named context.

The [final 106 named identifiers](identifier-selection-final.json) are verified against the promoted authority union. The [root promotion receipt](root-verification/authority-promotion.json) verifies all 716 author-package files and all 70 new source originals. The union adds 70 source terms and 10 ontology terms, preserving all 5,023 previous terms, all existing owners and the complete 1,072-entry configuration prefix. The unchanged identifier consumer passed on all 258 actual records; independent technical replay also checked every new source parser and ontology label.

Two immutable initial reviews found [a minor AdhE scope ambiguity](../../../reviews/structured/20261015T024904Z-next261-technical-initial/review.md) and [a major primary-evidence representation defect](../../../reviews/structured/20261015T025017Z-pwy5415-independent-science-initial/review.md), tracked as [issue 561](https://github.com/CultureBotAI/PathwayMech/issues/561) and [issue 562](https://github.com/CultureBotAI/PathwayMech/issues/562). The [repair integration](integration/review-repair-integration.json) binds successor SHA-256 `29b073a0a5aca884b9decf6b86a41c2a018c62dc0818c7e33ec17065152d781c`. It replaces all 35 faulty evidence occurrences through 23 array replacements with source-checked excerpts or precise original table facts, narrows the exclusion to E. coli ADHE-CPLX, and distinguishes the native DmpF pH-optimum annotation from the primary tested range. All 128 graph triples, 54 primary context blocks, named nodes and reference declarations remain intact.

The [repair package](authoring/primary-evidence-repair/HANDOFF.md) includes exact original byte spans and all old-item dispositions. Its passing author checks and the independent candidate repair check do not by themselves close the issues. Generated page/KGX inspection and all full repository gates have passed; the [verification report](verification.md) binds the results and successor review locations. Canonical review persistence, publication and issue closure remain separate recorded steps.

## Retained artifacts

The [root integrity check](root-verification/frozen-source-integrity.json) verifies 1,223 files across six frozen source packages, including hidden and ignored files. The [retention receipt](root-verification/source-retention-receipt.json) maps 206 retained files to their exact external bytes. Six complete biological accounting ledgers and the current duplicate-search logs are retained with verified lossless compression. The chemical package separately binds its two compressed broad or failed probes.

Full papers, large source bodies, sequence archives and pinned ontology databases remain external. The chemical participant package also retains six small original chemical counterpart responses; therefore the initial source-history description of all raw downloads remaining external was too broad. Full package manifests preserve the external locations and hashes, and compact projections preserve the scientific decisions. Handoffs describe their original external layouts.

The [primary author retention receipt](root-verification/primary-author-retention.json) verifies all 72 package files and maps 29 retained files. The [native author retention receipt](root-verification/native-author-retention.json) verifies all 257 package files and maps 67 retained files; its 126 new original responses and redundant runtime/cache copies remain external. Large native JSON ledgers use verified lossless compression. Retained Python helpers are inert text. All integration and retention checks are author checks, separate from independent review.

The [independent evidence retention receipt](root-verification/initial-review-evidence-retention.json) preserves 33 reviewer artifacts, including the initial record bytes, complete native-slot replay, primary item audit, formal chemistry checks, and selected-authority replay. The [authority handoff](authoring/authority/HANDOFF.md) retains 56 compact artifacts plus its manifests. Initial source/author drafts and review observations remain immutable; the repair receipt identifies the current maintained successor.
