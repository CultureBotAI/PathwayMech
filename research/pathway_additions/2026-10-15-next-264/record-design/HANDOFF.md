# Next264 source-to-record design

This is a finite source-author design for **MetaCyc:PWY-2503, benzoate degradation I (aerobic)**. It is not a YAML draft, maintained graph, independent scientific review, authority promotion, or postmerge absence conclusion. No source package was changed. The old263 worktree is released and is not an active dependency.

The latest reviewed contracts and nearest record shape were captured by read-only `git show` from commit **68cab54ba4d43c095c8e5e644a3cf8fbbc5b420a**, not from the older original checkout's working files. `contract-bindings.json` records those exact bytes. The add-pathway skill, closed schema, graph/evidence contract, identifier contracts and source configuration govern the proposed representation.

`merged-contract-comparison.json` subsequently verifies that all 12 captured contract/example blobs are unchanged at the actual merged baseline **3bd67d7cc30513e6b3cddc9b3696af0ef785fbdb**. This bounded git-object comparison is not the separate full corpus/source duplicate rebind, which another reviewer owns. Record generation remains pending root confirmation of that rebind and the locator repair's independent acceptance.

## Complete route and evidence selection

`core-route-design.json` preserves the complete two-step boundary:

1. RHEA:12634, left to right: benzoate + NADH + proton + oxygen → CPD-290 + NAD.
2. RHEA:11561, left to right: CPD-290 + NAD → catechol + carbon dioxide + NADH.

All **11 material-side entries**, eight exact core chemical identities, two pathway-membership relations, the explicit predecessor order and the **CPD-290 primary-material join** are accounted for. The `consumes` relations point from chemical to reaction; `produces` points from reaction to chemical. Native coefficient slots are omitted, while the exact selected Rhea sides establish formal coefficient one. NAD/NADH cycling is retained without inventing a reverse causal or regulatory edge. The calculated net equation is bookkeeping, not a third elementary reaction.

Exact native structures and selected Rhea family descriptions own formal identity and orientation. The primary evidence identifies cis-DHB; no historical experiment is claimed to establish the issuing absolute configuration. The copied chemistry package's **37,216-equation symbolic comparison and exclusion-completeness claim are explicitly quarantined**. Issue572 correction is separate. No family-uniqueness or exhaustion claim in this design depends on that comparison.

## Native contexts

`native-context-design.json` specifies all **five distinct activity contexts, 13 protein/complex contexts, nine component links, and eight genes**. Both XylL activity objects ENZRXN-3125 and ENZRXN-12384 remain visible. Their common enzyme/reaction pair may have one formal catalysis edge with both source owners, while their separate activity identities and different evidence availability remain intact. No extra XylL protein or experiment is inferred.

The four verified Xyl monomers may normalize to P23099/P23100/P23101/P23102 with exact native unification and issuing/CDS evidence. The other proteins and all five whole complexes keep native identities. All component coefficients remain in source evidence/description; they are not unsupported new schema fields. No component membership becomes independent overall catalysis. All eight native genes remain declared context nodes with reciprocal product descriptions; the closed schema has no `encodes` predicate, and this design does not misuse `enables` for gene→protein encoding.

The CPLX-2541 title question is resolved by the frozen assembly-title supplement: the complete native page's exact `TITLE` and `typeObjectPage` yield **MetaCyc:CPLX-2541 — benzoate 1,2-dioxygenase** through the existing `metacyc-html` reader. The complete assembly is preserved. This is not a synthetic label from its activity or a change to the unnamed-homomer XML fallback. Its version is the retrieval date, not a release inferred from the software footer.

Four source-reported cofactor relations and one native location relation are proposed with their source limits. FAD uses CHEBI:57692; the protein-ligated cluster class keeps MetaCyc:CPD-6. CHEBI:33739 is explicitly rejected as its exact identity, and CHEBI:49601 establishes only a broader generic cluster class. No Rieske ligands, oxidation state or preparation-specific microstate is inferred. GO:0005829 still needs the final accepted issuing owner before promotion.

The native JMP222 enzyme assignments, component annotations and cofactors remain **database assertions with visible conflicts**, not experimentally verified JMP222 findings. C-1 component/cofactor studies and the purified historical335 preparation cannot be used as direct proof of native JMP222 identities, masses, kinetic constants, or measured assembly. Primary observations belong in narrowly scoped reaction/evidence narrative. This is a proposed treatment of conflicting source claims; independent review must assess the final scientific interpretation, not merely its schema validity.

## Primary evidence and preparation limits

`primary-claim-design.json` dispositions every one of the **17 primary claim groups**, with original owners and locators. `primary-protein-selection.json` covers all **17 printed2025 accession/locus identities**; `complete-publication-dispositions.json` covers the union of **20 publication leads**. The full reading/access levels remain those of the primary source package. This design additionally inspected the exact2025 methods/result and figure-caption passages relevant to construct roles; it does not claim to repeat the independent full visual reading.

**Issue 573 / NEXT264-BIO-LOC-01:** the frozen biological identity package's single `$.primary_locator` field incorrectly said Methods2.3. The actual accession paragraph is Methods2.1, “DNA Techniques and Alignments,” JATS `/article/body/sec[@id="jobm70061-sec-0020"]/sec[@id="jobm70061-sec-0030"]/p[1]`. The append-only package at `corrections/identity-locator-successor/` retains the original and an exact one-string successor; all 17 identity rows and all other bytes are unchanged. Its proof does not repeat sequence checks. The primary package P264-16 already had the correct locator. The design's corresponding 17 locator leaves and its generator literal are corrected, with predecessor bytes and `author-plan-replay.json` preserved. `design-locator-successor-receipt.json` records that bounded change; `author-plan-replay-final.json` binds the corrected design. Independent acceptance is separate.

The1971 observations support the two-step material route, intermediate trapping, second-step extract activity, and preparation-specific donor use. Positive extract measurements, below-detection controls, blank cells, and unrelated-substrate controls remain distinct. Blank cells and failed NADPH substitution are not inhibition measurements. The1972 masses, Km values, NAD requirement, observed excess-NADP inhibition, tested reverse-reaction non-detection and pH-dependent salt effects remain scoped to purified335 FractionV. Original ambiguous salt-table values stay withheld. The unobserved proposed beta-ketoacid does not become a third reaction or measured participant.

The2025 positive coexpression assays support qualified `enables` claims for the tested RW1 BenAB/RedA2/ferredoxin ensembles and the separate KT2440 BenABC control. These are not claims that every isolated subunit independently catalyzes the full reaction. SWIT0053 and SWIT0363 retain their separate low-conversion constructs; SWIT0285,0998 and1843 non-detection does not become `inhibits`. RedA1/RedA2 complementation can support a separately qualified pathway-enabling observation, with no purified electron-transfer claim. Fdx1/Fdx3 double-knockout growth establishes no unique physiological partner. BenD remains putative, and the benA insertion's possible polar effect prevents attributing the multi-gene rescue to an individually demonstrated BenD activity.

Construct qualifiers belong on the actual protein endpoint and require their own narrow evidence. They cannot repair a different-strain identity or turn a guessed complex into a verified assembly. The helper HB101/JM109 discrepancy and the assay/control wording/sampling limits remain visible. Every historical335/B9/C-1/73/mt-2 and modernJMP222/H16/ADP1/RW1/KT2440/B1 preparation remains distinct. Native NT4 versus paper4NT, TW3 taxonomy, and the two testosteroni/deposit inconsistencies are preserved.

## Complete accounting and omissions

The machine-readable plan contains:

| Surface | Disposition count |
| --- | ---: |
| Native direct slots across47 full objects | 511 |
| Native assertion proposals | 72 |
| Typed native database cross-references | 116 |
| Native organism contexts | 13 |
| Historical/modern preparation groups | 14 |
| Unrelated regulation backlinks | 21 |
| Out-of-boundary chlorinated activities | 4 |
| Adjacent pathway interfaces | 6 |

`complete-native-slot-dispositions.json`, `native-proposal-dispositions.json`, `xref-selection-dispositions.json`, `taxon-and-preparation-design.json`, and `explicit-omission-ledger.json` provide one disposition per item. This is a finite source denominator, not a global completeness claim. All five umbrella backlinks and the six upstream/downstream interfaces remain context; no extra pathway or cross-boundary transfer is inferred. Family membership, orthology, taxonomy, calculated energies, administrative metadata and unrelated compound backlinks never become catalytic edges merely because they appear in the source.

`evidence-owner-catalog.json` identifies exact original/derived owners, hashes and locators. It distinguishes native assertions from primary evidence and marks the1972 artifact as transformed text rather than a raw full PDF. Repeated catalog entries for one biological ID are evidence/authority roles, not permission to create duplicate final reference IDs. Each final evidence item must be at most400 characters, have the correct local reference, and use either an exact short quotation or a faithful located structured statement. The accompanying source manifests retain all additional artifact bindings.

## Before authoring and acceptance

`next-author-decisions.json` gives ten grounded decisions/questions. The remaining mandatory work is the post263 merged-baseline duplicate rebind, final selected-only authority integration, exact preparation/construct realization, independent scientific and technical review, and normal rendering/KGX/full gates with current-byte binding. The design does not run those gates on a nonexistent record.

Default handling of observed NADP/salt effects is explicit narrative/evidence with preparation and access limits. A signed reagent edge requires the actual tested chemical's exact issuing identity and an unambiguous target; no new chemical identifier is guessed. Unread full articles or figures only need further retrieval to support claims currently withheld. No permission request or artificial zero-baseline causal inference is introduced.

The frozen package retains exact selected source copies, the tiny assembly-title supplement, current contract bytes, all plan tables and inert reproduction helpers. The isolated final author replay reproduces all 11 plan tables (normalizing only the run timestamp), reconstructs 511 slot locators, and checks 279 exact copied source files, 12 exact contract blobs, 39 structural proposals and 38 distinct structural relations. This is not final record validation or independent review. The compact manifest preserves original/stored hashes and byte counts, and the artifact manifest freezes the complete owned package. Historical predecessor proofs are explicitly retained, including the initial replay helper's pre-execution syntax failure. No maintained, Git or GitHub writes occurred.
