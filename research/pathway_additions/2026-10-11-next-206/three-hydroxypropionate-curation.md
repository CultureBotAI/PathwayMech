# Pathway mechanism research: carbon fixation by 3-hydroxypropionate cycle

The selected identity is **GO:0043427**, the complete first cycle that produces glyoxylate while regenerating acetyl-CoA in *Chloroflexus aurantiacus*. The original QuickGO definition and pinned GO definition were inspected. This is an exact biological boundary, rather than a label-only equivalence to MetaCyc. The current author target is [carbon-fixation-by-3-hydroxypropionate-cycle.yaml](../../../data/pathways/carbon-fixation-by-3-hydroxypropionate-cycle.yaml).

## Pathway scope

Native PWY-5743 lists 13 reaction objects. The record retains all 13 and adds succinate oxidation and fumarate hydration, both directly present in the first-cycle diagram and extract assays of the 2001 primary study (PMID:11418572). Those regeneration reactions were omitted from the captured native list; they are not a different variant or optional shortcuts. The closed chemical cycle has 15 reaction nodes. It produces one glyoxylate and regenerates the acetyl-CoA acceptor.

The separate PWY-5744 glyoxylate-assimilation cycle produces pyruvate. It shares the acetyl-CoA-to-propionyl-CoA branch and multifunctional Mcl but has its own independently defined biological boundary. Its dedicated methylmalyl/mesaconyl/citramalyl chemistry is outside this record. The broader bicycle is not claimed as fully represented by either individual child.

CO2/bicarbonate equilibration is explicit, without an invented carbonic anhydrase. Carboxylation uses the two protein-bound biotin half-reactions. No additional overall acetyl-CoA carboxylation is added. One turnover of each displayed reaction leaves one CO2 and one bicarbonate as inputs; two carbon-hydration turnovers express the same biological carbon input as two CO2. Displaying one reaction node does not impose its flux multiplicity.

## Original sources and identity decisions

The [source manifest](three-hydroxypropionate-source-manifest.json) identifies complete original response bodies separately from transformed web excerpts, pinned SemanticSQL authorities and unsuccessful access attempts. No session, cookie or authorization headers are maintained. The [source projection](three-hydroxypropionate-source-projection.json) preserves every native reaction's sides, direction and controller links; the selected Rhea side occurrences; current protein identities; and both source-to-graph and explicit exclusion dispositions. The [identifier ledger](three-hydroxypropionate-identifiers.json) distinguishes named graph nodes from reference-only accessions.

The primary whole-cycle, MCR, PCS, Smt and Mcl studies used OK-70-fl/DSM 636. The 2024 ACC work instead used J-10-fl material. The declared taxon is the species, with these strain distinctions retained at each applicable protein/assay edge. No taxon `occurs_in` relation is invented: that predicate is reserved for cellular compartments.

| Component | Selected representation and evidence limit |
| --- | --- |
| BC1 | A9W9X0, J-10-fl Caur_1378, enables the protein-biotin carboxylation activity. The 2024 original main paper (PMID:38572988) establishes the fused BCCP domain, biotinylation, functional reconstruction and solution tetramer. A full holo-ACC stoichiometry is not inferred. |
| CT alpha/beta | A9WBQ8 and A9WBQ9 enable the jointly required carboxyl-transfer function using their exact current HAMAP/ARBA evidence tiers. The 2024 Methods reverses current alpha/beta locus assignments and gives inconsistent construct lengths. It is not treated as direct exact-accession construct proof. |
| MCR | Species-level CPLX-7550 with independently grounded OK-70-fl Q6QQP7. The purified dimer and two partial reductions are supported by PMID:11948153. Q6QQP7 is a separately submitted 1220-residue OK-70-fl sequence; native A9WIU3 is a distinct 1219-residue J-10-fl entry. They are not equated. |
| PCS | Exact OK-70-fl Q8VRG6 enables the three native partial activities. The author-updated AF445079.2/AAL47820.2 sequence equals Q8VRG6. Native MONOMER-13612 links both Q8VRG6 and J-10-fl A9WEU4; their two residue differences remain explicit. Native coefficient four conflicts with its own three-or-four-subunit prose, so no unique complex stoichiometry is asserted. |
| Smt | CPLX-7546 contains six CPLX-7548 alpha/beta heterodimers. Exact OK-70-fl Q1KLK1/Q1KLK0 derive from primary-linked sequence submissions. PMID:16547052 establishes joint coexpression, native function and an approximately 550-kDa recombinant assembly. The native current J-10-fl chains are not silently substituted for those experimental sequences. |
| Mcl | CPLX-7549 contains six S5N020 chains. Its sequence exactly equals the separately retained native-linked A9WC35 sequence; this is a sequence comparison, not a claim of strain identity. PMID:24206647 directly studies the OK-70-fl construct and supplies solution/structural hexamer evidence. |
| SDH | A9WDT7 is a current J-10-fl, ARBA-inferred catalytic component of generic quinone-dependent succinate oxidation, with inferred FAD. It is not a fully isolated OK-70-fl holoenzyme or an experimentally fixed physiological acceptor assignment. |
| PCC, epimerase, mutase, fumarase | Chemistry remains complete. Exact organism-specific protein selection is unresolved and not invented. In particular the genome-paper fumarase locus Caur_1443 is currently annotated as aspartase. The archaeal native CPLX-7545 and MONOMER-13611 are not transferred into this bacterium. |

The source-native protein labels are retained even when automated naming is broader or misleading, notably the PCS acetate-CoA-ligase name. Biochemical function is independently supported; canonical labels do not substitute for function evidence.

## Chemistry, carriers and conditions

All selected reaction sides are re-extracted from the complete original Rhea release 142 RDF and official direction table. Named directional labels already match the configured pinned Rhea canonical labels. Current physiological orientation is distinct from the native reaction's reversible or opposite stored orientation. The projection retains both.

RHEA-COMP:10505 and RHEA-COMP:10506 denote **whole generic protein-bearing biotin states**. Their linked reactive-residue formulas permit atom/charge accounting only because the unchanged protein scaffold cancels. They are not substituted with free CHEBI:83144 or CHEBI:83145 residues. The carrier returns to its original state across the two carboxylation half-reactions.

The original Rhea/ChEBI equations preserve malonyl-, propionyl-, methylmalonyl-, succinyl- and (S)-malyl-CoA charge and stereochemical states. The epimerase direction converts the selected S-methylmalonyl state to R-methylmalonyl-CoA before rearrangement. NADPH consumption is explicit in the two MCR activities and the PCS reductase activity; no NADH alternative is invented.

The original 2001 SDH assay used artificial DCIP/PMS. The 2002 cycle figure calls the electron acceptor unknown, while the 2006 paper's introductory cycle accounting explicitly produces reduced quinone. Current Rhea:40524 and A9WDT7's inferred catalytic annotation separately support the generic quinone/quinol reaction class. No specific quinone species or direct natural-acceptor measurement is claimed. The generic R substituents cancel in the class-level balance.

Mcl magnesium/manganese alternatives preserve preparation-specific support and do not require simultaneous binding. Smt itself did not require magnesium in the 2006 experiment; magnesium in the coupled assay served the lyase. MCR metal stimulation and EDTA inhibition did not establish an obligatory physiological metal identity, so no exact MCR metal edge is added. Current CT zinc and SDH FAD retain their computational evidence tiers.

The 2002 PCS paper was independently inspected through its original-paper web rendering. Its potassium and magnesium dependencies are retained with their assay scope. The magnesium relation does not assert a separately isolated metal-binding site. The paper's intermediate X was a proposed assignment; native/current curated partial reactions are not presented as a fully resolved standard comparison from that experiment. Publisher/PDF byte retrieval failed, so the reference has no fabricated original-body hash. Saved tool excerpts are explicitly transformations, and offline replay cannot establish full original-paper byte integrity.

A late follow-up, PMID:39019246 (2024), was inspected in original PMC12786355 HTML. Methods S5/Table 1 specifies a His-tagged A9WIU3 C-terminal fragment, residues 550–1219. This is compatible with the selected partial chemistry but is not an exact Q6QQP7 whole-enzyme preparation. Its kinetic order and product inhibition remain construct-specific context, without new graph relations. The original body and exact access/hash metadata are retained.

## Coverage and exclusions

Every native reaction member has a disposition. Controller links embedded in generic native reaction objects often include unrelated taxa; only separately supported Chloroflexus proteins are selected. The native Smt nested assembly is retained, rather than flattening 12 polypeptide chains into six identical subunits. Functional `enables` edges preserve joint requirements and uncertain oligomerization without claiming monomer sufficiency or formal Boolean AND semantics.

Other Mcl activities, alternative Smt acceptors, artificial assay dyes, off-pathway inhibitor screens, upstream biotin biosynthesis, nucleotide recycling, respiratory quinone regeneration and the second assimilation cycle are outside this exact record. Their omission is not a claim of biological absence. Current computational cytoplasmic/membrane location annotations were considered; they are not transferred into a whole-pathway compartment claim. The inspected papers do not identify a causal regulatory protein for this record. No such node is invented from induction/growth observations.

The current shared iModulonDB inventory has no Chloroflexus dataset. That is a resource-applicability result, not a biological absence result. Parent-owned applicability receipts remain separate from mechanistic evidence.

## Deduplication and verification

The [deduplication receipt](three-hydroxypropionate-dedup.json) records fresh `rg -uu` searches in both this worktree and the original Documents checkout, including ignored and hidden content. Only Git internals and the environment directory were excluded. Prior carbon-fixation scouts and the cross-Mech PWY-5743 lead were read. Existing Rut chemistry overlaps one reduction but is a different complete mechanism. Current authored files and the distinct concurrently curated second cycle are not mistaken for pre-existing duplicates.

The [author replay](three-hydroxypropionate-replay.py) re-parses original RDF, official directions, native XML, current protein JSON, exact sequences and primary HTML anchors. It checks 15 atom/charge balances, whole-cycle net accounting, every chemical-side edge, all material-continuity relations, native and closed schemas, and actual KGX evidence/reference metadata. It rehashes original bodies and streams the ChEBI cache hash. This is an author check, not the later independent scientific review. Its [validation receipt](three-hydroxypropionate-validation.json) records actual execution and limitations.

An early author scaffold used the wrong `edges` key, an undeclared `evidence_code` field and a taxon `occurs_in` relation. These were corrected before freeze; source evidence tiers remain in allowed assertion prose. The first replay was intentionally interrupted while an additional sequence-comparison citation was being attached. The final replay checks its target hash before and after execution to prevent a mixed-input receipt. Parent-owned full-corpus gates and independent review occur after author freeze.
