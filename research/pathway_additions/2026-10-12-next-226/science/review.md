# Independent scientific review: ribose phosphorylation

Verdict: **scientifically acceptable with the draft’s explicit source and access limits**. No new blocker, major, or minor scientific findings. Target SHA-256 `385101d166c9150936d81bb0f1c6c0d134b6ac1e6a6454d86e238ac0576e3d71`.

This is an external review of one unadopted candidate, not a maintained gate or merge approval. The exact unnamed RXN-14904 authority-adapter integration, canonical review saver and root-owned corpus/lifecycle checks remain pending.

Reviewed 2026-10-12T01:09:43.963761+00:00 to 2026-10-12T01:15:24.377897+00:00; independent reviewer `/root/ribose_science`; Git base `6b6747ae6e14a9904efd7da9cbcca16398855582`.

## Findings and prior dispositions

All five prior source-locality findings, RIBOSE-AUDIT-01 through RIBOSE-AUDIT-05, are resolved in this exact target. I independently checked their corrections against the original sources. No participant, reaction, or edge triple was changed by this review.

## Scientific assessment

**Identity and boundary.** Exact MetaCyc RIBOKIN-PWY, not a single kinase reaction or a PathBank collage. Two native enzymatic members plus the narrative-required exact spontaneous event remain. Incoming uptake and two opaque downstream interfaces preserve boundary context. Fucose mutarotase chemistry, methylglyoxal-overproduction phenotype, chemotaxis, and the historical PathBank attached lysine interface do not enlarge the core.

**Chemistry and orientation.** Original authority structures separate beta-pyranose, beta-furanose, alpha-furanose, generic furanose and aldehydo ribose. All four equations balance atoms and charge. Native spontaneous alpha-left/beta-right reversible reaction is correctly used right-to-left. Native kinase formal generic sides and Rhea13698 remain distinct from the explicitly declared alpha pathway refinement.

**Transport.** Native uptake moves generic D-ribopyranose from outside to inside with all seven ATP-hydrolysis sides. Rhea29904 uses furanose and is not an exact alias. RbsB beta-pyranose binding supports presumed beta transport only, not an unqualified beta-exclusive transport equation.

**Enzymes and assemblies.** Native RbsD10/FucU10/RbsK2 and A1C2B1 component counts are exact original slots. They are not direct assertions about Ryu tagged/untagged chromatographic mixtures. RbsA contains tandem ABC domains in one chain; frozen PathBank A2C2B1 conflict is retained. Transport-cycle states are conditional.

**Cofactors and locations.** Native kinase Mg2+/K+ and reviewed alternative Mn2+/NH4+ roles agree. Probable metal-nucleotide substrate and likely potassium/magnesium in vivo are not measurements of intracellular occupancy. Pi activation is separate from phosphate incorporation; no invented arsenate/vanadate identities. Localization annotations preserve source or curator inference; construct topology is not imported as native protein measurement.

**Gene regulation.** Native promoter regulation, full TU00206 gene membership and six exact MG1655 NCBI gene mappings agree. RbsR and CRP-cAMP target transcription. Native YidZ RNA-seq and Gao primary rbsD deletion response support a negative sign under stated M9-glucose conditions; tagged ChIP-exo and supplement limits remain explicit. Unnumbered RbsR-ribose and CRP-cAMP ligand slots do not imply counts.

**Source-locality remediation.** RIBOSE-AUDIT-01 through -05 remedies preserve biology while moving each claim to its actual source. Exact cofactor/localization/native gene/primary-condition/CRP identity assertions are now separate and supported.

**Computational context and discovery.** Original iModulon tables match RbsD/RbsA in e_coli/precise_mg1655/1 Crp and FucU in /73 Fucose. No causal edges derive from membership; operon metadata disagreement does not split native TU00206. Root-preflight dedup is inherited, not claimed independently repeated over the full corpus. No source exhaustion claim.

## Verification

- All 51 reference hashes match their originals and the record. All 203 sealed author artifacts match.
- All 95 XPath evidence entries resolve, including every union arm. Claim support was assessed separately from locator resolution.
- 139 independent probes passed: native and closed schemas; original ontology labels/structures; original Rhea orientation and complete linked participants; four complete atom/charge balances; native assembly coefficients; six gene identities/taxa; and regulatory signs/targets.
- Four same-type or same-formula chemistry mutations were rejected, including the wrong anomer bridge endpoint, wrong spontaneous direction, wrong kinase anomer, and omitted ATP. These controls do not substitute for review.
- Thirteen supplemental probes passed, including exact native ChEBI mappings, seven transport compartment roles, iModulon source identities, author seal, and META PRPP page identity.
- No whole-corpus, render/export, GitHub, or canonical saver result is claimed. The exact terminal receipt is in `probe-receipt-1.json`.

## Every edge disposition

All entries are supported within the recorded scope. The JSON preserves every individual evidence item, original source path/hash, and locator.

| Edge | Assessment |
|---|---|
| ribose-001 | Native META reaction-list contains RXN0-5304; independently read Rhea directional 25433 and native beta-pyranose/beta-furanose sides establish the representation. |
| ribose-002 | Exact RIBOKIN-RXN is the other member of the native reaction-list; its sugar refinement is explicitly declared in the record. |
| ribose-003 | Pathway narrative explicitly supplies spontaneous alpha/beta furanose exchange; exact RXN-14904 has alpha-left/beta-right, reversible, spontaneous and physiologically-relevant flags plus orphan YES-PUTATIVE. Source-context direction is right-to-left. |
| ribose-004 | Native left CPD0-1110 maps to CHEBI:27476. Original Rhea 25433 left substrate is the same beta-pyranose, coefficient one. |
| ribose-005 | Native right CPD0-1108 maps to CHEBI:47002. Original Rhea 25433 product is beta-furanose, coefficient one; its short ChEBI label does not erase ring identity. |
| ribose-006 | Exact RXN-14904 right participant CPD0-1108 is consumed by the selected right-to-left route. No catalyst or unrelated ring-opening reaction is substituted. |
| ribose-007 | Exact RXN-14904 left CPD-10330 is the selected alpha-furanose output, independently mapped to CHEBI:45506. |
| ribose-008 | Formal RIBOKIN-RXN generic D-Ribofuranose is deliberately refined to narrative CPD-10330/alpha-furanose. This is not an exact Rhea 13698 alias; primary NMR supports preference, not exclusivity. |
| ribose-009 | Native kinase ATP input retained; alpha-sugar refinement does not change nucleotide stoichiometry. |
| ribose-010 | Native generic CPD-15317 product is deliberately refined by the pathway narrative to CPD-15318/alpha-furanose-5-phosphate, CHEBI:140679. Ring and protonation identity checked independently. |
| ribose-011 | Native kinase ADP product retained as ADP(3-). |
| ribose-012 | Native kinase hydron product retained; original ChEBI formula/charge balancing closes the equation. |
| ribose-013 | Native ABC uptake consumes one internal ATP; original side compartment CCO-IN is explicit. |
| ribose-014 | Native ABC uptake consumes D-ribopyranose from CCO-OUT. Rhea transport uses furanose and is not substituted; beta-only transport remains presumptive. |
| ribose-015 | Native ABC uptake consumes one internal water, retained in complete ATP-hydrolysis chemistry. |
| ribose-016 | Native ABC uptake produces one internal ADP; transport roles are separately retained. |
| ribose-017 | Native ABC uptake produces internal Pi mapped to hydrogenphosphate; this role is distinct from kinase activation. |
| ribose-018 | Native ABC uptake produces the D-ribopyranose class in CCO-IN; same chemical ID has distinct external/internal roles in evidence, not a global free-sugar location. |
| ribose-019 | Native ABC uptake produces internal hydron. Seven formal sides balance atoms and charge. |
| ribose-020 | Native narrative and exact beta-furanose intermediate establish pyranase supply to the spontaneous anomer event. |
| ribose-021 | Exact alpha-furanose product of the spontaneous event supplies the narrative-refined kinase substrate. |
| ribose-022 | Native pathway incoming-link and narrative establish uptake before pyranase. Formal transported class remains broader than the beta-pyranose substrate and presumed beta selectivity is disclosed. |
| ribose-023 | META pathway-link connects generic furanose-5-phosphate to NONOXIPENT-PWY. Accepted only as opaque material-supply context, without asserting immediate cyclic/open-chain chemical identity. |
| ribose-024 | Exact META pathway-link connects the phosphate class to PWY0-662; META issuing page independently establishes PRPP biosynthesis. No claim that ECOLI also supplies this link. |
| ribose-025 | Native ENZRXN0-6479 assigns CPLX0-7646 to RXN0-5304. Accepted as the source-defined RbsD complex annotation, not as proof that a particular unmodified decamer was directly assayed by Ryu. |
| ribose-026 | Native ENZRXN0-8627 assigns CPLX0-7645 to the same pyranase chemistry. Ryu scientific body independently reports FucU pyranase activity. Alternative enzyme, not obligatory RbsD partner. |
| ribose-027 | Native RIBOKIN-ENZRXN assigns CPLX0-7647 to RIBOKIN-RXN. Explicit pathway-specific alpha refinement is supported separately by the native narrative. |
| ribose-028 | Native ABC complex comment reports active reconstructed transporter and proposes cofactor-dependent cycle states; accepted as curated source annotation without inventing uninspected preparation details. |
| ribose-029 | Native complex component is exactly ten EG10817-MONOMER chains; monomer original provides UniProt P04982. Source-defined decamer is distinguished from C-His gel-filtration estimates. |
| ribose-030 | Native complex component is exactly ten EG10355-MONOMER chains; monomer original maps P0AEN8. Native decamer is distinguished from inactive N-His monomer and other preparation estimates. |
| ribose-031 | Native complex has two RIBOKIN-MONOMER chains; source maps P0A9J6. Ryu C-His approximate 1.9 estimate is not treated as an exact native assembly observation. |
| ribose-032 | Current inspected native snapshot has one RbsA chain with tandem ABC domains. Original frozen PathBank Complex4095 gives two chains; exact stoichiometry/xref objects confirm this disclosed conflict. |
| ribose-033 | Native ABC component coefficient is two RbsC chains; exact source-local P0AGI1 link checked. |
| ribose-034 | Native ABC component coefficient is one RbsB chain; exact source-local P02925 link checked. Binding subunit is not assigned independent transporter catalysis. |
| ribose-035 | Native comment proposes Mg-ATP-loaded RbsA association in the transport cycle. Cofactor edge preserves this conditional state and does not imply permanent occupancy. |
| ribose-036 | Native kinase cofactor slot contains K+. This role does not imply simultaneous use of every alternative ion. |
| ribose-037 | Native kinase Mg2+ slot and separate reviewed COFACTOR inference support the split assertion. Likely intracellular magnesium and probable metal-nucleotide substrate remain inference. |
| ribose-038 | Reviewed COFACTOR explicitly names manganese as an active alternative. No simultaneous Mg/Mn requirement is asserted. |
| ribose-039 | Reviewed ACTIVITY REGULATION explicitly names ammonium activation, likely potassium occupancy, and a probable conformational/affinity mechanism. |
| ribose-040 | Native REG0-9220 connects Pi and positive regulation to RIBOKIN-ENZRXN; separate enzyme comment supplies pH/pentavalent-ion context. No invented arsenate/vanadate species or phosphate incorporation. |
| ribose-041 | Exact RbsD native location slot gives Gram-negative cytosol. Claim remains source annotation. |
| ribose-042 | Exact RbsK native location slot gives Gram-negative cytosol. Claim remains source annotation. |
| ribose-043 | Exact RbsR native location slot gives Gram-negative cytosol. P0ACQ0 mapping independently checked in reviewed original. |
| ribose-044 | FucU reviewed SUBCELLULAR LOCATION says cytoplasm with ECO:0000305; inferential status preserved. |
| ribose-045 | RbsA reviewed location is peripheral cell-inner-membrane protein with HAMAP/curator inference. Tandem-domain claim is sourced elsewhere, not attributed to location field. |
| ribose-046 | RbsC reviewed field supports inner membrane and multipass annotation. Separate ten-helix primary used His10 C227A single-cysteine constructs; the edge is not an unmodified-chain topology assay. |
| ribose-047 | RbsB reviewed entry supports periplasm; no transmembrane-permease role is inferred. |
| ribose-048 | RbsR negative REG0-5371 acts on rbsDp PM00290. Exact TU00206 includes EG10817; original NCBI Gene 948267 independently identifies rbsD, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-049 | CRP-cAMP positive REG0-5370 acts on rbsDp PM00290. Exact TU00206 includes EG10817; original NCBI Gene 948267 independently identifies rbsD, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-050 | RbsR negative REG0-5371 acts on rbsDp PM00290. Exact TU00206 includes EG10814; original NCBI Gene 948264 independently identifies rbsA, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-051 | CRP-cAMP positive REG0-5370 acts on rbsDp PM00290. Exact TU00206 includes EG10814; original NCBI Gene 948264 independently identifies rbsA, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-052 | RbsR negative REG0-5371 acts on rbsDp PM00290. Exact TU00206 includes EG10816; original NCBI Gene 948262 independently identifies rbsC, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-053 | CRP-cAMP positive REG0-5370 acts on rbsDp PM00290. Exact TU00206 includes EG10816; original NCBI Gene 948262 independently identifies rbsC, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-054 | RbsR negative REG0-5371 acts on rbsDp PM00290. Exact TU00206 includes EG10815; original NCBI Gene 948261 independently identifies rbsB, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-055 | CRP-cAMP positive REG0-5370 acts on rbsDp PM00290. Exact TU00206 includes EG10815; original NCBI Gene 948261 independently identifies rbsB, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-056 | RbsR negative REG0-5371 acts on rbsDp PM00290. Exact TU00206 includes EG10818; original NCBI Gene 948260 independently identifies rbsK, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-057 | CRP-cAMP positive REG0-5370 acts on rbsDp PM00290. Exact TU00206 includes EG10818; original NCBI Gene 948260 independently identifies rbsK, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-058 | RbsR negative REG0-5371 acts on rbsDp PM00290. Exact TU00206 includes EG10819; original NCBI Gene 948266 independently identifies rbsR, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-059 | CRP-cAMP positive REG0-5370 acts on rbsDp PM00290. Exact TU00206 includes EG10819; original NCBI Gene 948266 independently identifies rbsR, its b-locus, MG1655 taxon and EcoCyc xref. Gene-target edge concerns transcription, not encoded enzyme catalysis. Expression-based regulation is not promoted to direct binding. |
| ribose-060 | REG0-15980 is negative RNA-seq-backed regulation of EG10817 by EG11721-MONOMER. Original reviewed P31463 maps that frame. Gao passage 31118 identifies rbsD upregulation in the deletion; Methods 5640, 9154, 14498 distinguish MG1655-derived RNA-seq and C-terminal 8-myc ChIP-exo. No direct unmodified-binding or exact fold-change claim. |
| ribose-061 | MONOMER-60 includes PD03867 without a coefficient. Reviewed P0ACQ0 identity is checked; no RbsR oligomer count inferred. |
| ribose-062 | MONOMER-60 includes uppercase RIBOSE, independently mapped to CHEBI:16988, without a ligand coefficient. |
| ribose-063 | Native RbsR comment supports ribose-dependent reduction of DNA-binding affinity and derepression. Edge targets repressor function, not direct pathway catalysis. |
| ribose-064 | Native CRP-cAMP assembly contains PC00004; component slot has no coefficient. No ligand copy number is inferred. |
| ribose-065 | Native CRP-cAMP assembly contains CAMP mapped to CHEBI:58165; no cAMP copy count is supplied or invented. |
| ribose-066 | Native PC00004 has two PD00257 chains; separately cited reviewed P0ACJ8 BioCyc cross-reference binds the protein identity. This resolves prior source-locality defect. |

## Source access and limits

- **PMID:15060078:** Read retained author-uploaded full scientific body observations read1/read2, including Methods, NMR results, Table I and discussion. Not a publisher PDF; supplementary figures unavailable.
- **PMID:34428301:** Original full BioC artifact hash verified; independently read YidZ results and all relevant culture, RNA-seq, ChIP-exo, differential-expression and structural-model methods. Critical-section review rather than claim to reread unrelated TF results; no supplement values or figure-pixel claim.
- **PMID:12923096:** Original full PMC HTML artifact hash verified; independently inspected Abstract, introduction, construct/mutagenesis, multiplex labeling, Fig2 description and topology discussion. Critical-section textual review; no original figure-pixel claim.
- **Other cited primary work:** Native database evidence annotations/metadata inspected where relevant. This review does not claim full-paper retrieval/reading of every underlying paper cited by databases.

- Known exact unnamed RXN-14904 still fails the existing identifier gate; separate typed source-context adapter must pass before integration. It is not an uncertain chemical identity.
- Native database snapshot/version and primary access boundaries are retained; this review does not establish all annotations and alternatives operate concurrently in wild-type MG1655.
- Fresh web attempts to PMC8464067 and PMC181013 returned browser challenges; retained original BioC/HTML bodies were inspected instead.
- No fresh full-corpus absence claim. Gitignored/hidden/followed searches were used for external artifact discovery; completeness of pathway absence comes from sealed preflight/root acceptance.
- Canonical review saver, maintained pages/KGX, whole-corpus gates, history/GitHub lifecycle and licensing are root/user workstreams, not performed here.

## Next steps

Root should finish the typed RXN-14904 authority integration, preserve this external review beside the canonical lifecycle record, and run required maintained gates on the integrated exact target. Any later scientific delta needs a successor review. No source-exhaustion conclusion is made.

Root subsequently reported a separate adapter metadata-consistency defect involving altered source URL/frame metadata. The authentic source and builder output remain correct; this does not change the scientific verdict. Adapter repair/adoption and the final accepted threonine predecessor bridge remain pending.
