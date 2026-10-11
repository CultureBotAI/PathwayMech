# Independent external scientific review: PathBank:SMP0002083

The complete pathway is scientifically supported. One minor evidence-provenance correction remains open: [issue422](https://github.com/CultureBotAI/PathwayMech/issues/422), `salvage-ii-pwml-interface-evidence-locator`. No major or blocker finding was identified. This judgment applies to original draft SHA256 `11ceb3fe99f2ed2966bb8a68faf8fa836a6a4a9e94b2bc0c499bb1119fd3cddd`.

All57 edges,81 evidence items,47 named identifiers and23 references were reviewed. The complete native boundary is three biochemical reactions, one transport and an opaque Aspartate Metabolism input interface.

## Required correction

Original lines 24–38 contain id 581268, reference-pathway-id 551 and Compound 114 input, with no Aspartate Metabolism name. Lines 8627–8645 contain sub-pathway-visualization/sub_pathway_compound_visualizations/sub-pathway-compound-visualization/side = Left, not visual-element/connector-type. In an immutable successor, change only the PWML source_assertion and source_locator to the observed native IDs, input and side path. Retain the independently named Aspartate Metabolism interface and all biological scope.

## identity and boundary

Current selected SMP0002083 is four elementary events plus one opaque SMP0000809 input interface. Original membership has three BiochemicalReaction, one Transport, four Catalysis and one Pathway object; it is not the three-reaction MetaCyc PWY-6611 salvage V core. Independent SMP0000809 export supplies canonical Aspartate Metabolism name. Full connected pathway is deliberately not expanded.

## chemical sides and direction

Independent complete-original XML scans recovered reverse master links and native substrate/product resources. RHEA27644 is right_to_left relative to 27642; 24409 and 21141 are left_to_right. All 14 balanced material sides and coefficients agree. Three direction mutations and a coefficient mutation were rejected.

## transport and compartments

Native transport has adenine and proton as periplasmic inputs and cytosolic outputs, coefficient 1 each. Exact coupling ratio remains database-only. All six compartment instances are preserved. Native GO0005620 has issuing replacement GO0042597. Neutral PathBank IMP_Cytosol and IMP_Cytoplasm are distinct from Rhea IMP2-; no connecting transport/protonation reaction is asserted. aas2-032 PWML text/locator needs finding422 correction.

## proteins and assemblies

Five reviewed UniProt identities, sequence versions, lengths and K12 taxonomy agree. Native DeoD hexamer and Gsk/PurR dimers agree with MetaCyc components; Gsk and PurR have explicit monomer UniProt bridges. DeoD 238-residue crystallographic chains are not silently equated to 239-residue current sequence. Gsk 434-residue sequence is distinguished from assay/crystal constructs. Conditional tetramer remains evidence because no exact issuing assembly ID was established.

## cofactors and regulation

Add zinc is explicitly HAMAP inference. Gsk Mg2+ retains probable additional free Mg and actual ATP-Mg/MgCl2 assay conditions. K+ stimulation and Cu2+/Zn2+ inhibition remain database annotations whose cited 1995 primary was abstract-only. GDP/ppGpp inhibition, concentration-dependent tetramers and lower ppGpp-tetramer activity agree with 2020 Results S3-S5. Crystallographic octamer is not physiological; older GTP annotation conflict remains visible.

## taxa and transcription

PurR direct repression of yieG/adeP is supported by combined MG1655 ChIP-chip/transcription evidence. add induction 17.61-fold is an adenine supplementation response, not direct PurR-add regulation or direct enzyme activation. Exact NCBI Gene948224/945851 agree with adeP/add, loci, MG1655 taxon511145 and Swiss-Prot bridges. PathBank K12 name/BW25113 taxon mismatch remains explicit; uptake constructs from T184 and JW3692/JW4025 assay hosts are not generalized to MG1655.

## primary sources and limits

Read original 2020 Gsk sections S3-S5/S45/S48, 2013 transport methods/results/table1, 2011 PurR sec9/sec12/sec13/sec14, and 2018 DeoD BioC passages40-52/63. Independently extracted all seven 1975 PDF pages and rendered pp87/89: SO312 vs SO445 has guanosine0.70 to<0.01, inosine0.05 to0.02 and adenosine0.11 unchanged. No full-route flux inferred. 1983/1994/1995 abstracts are labeled; kinetic internal-adenine feedback is appropriately omitted as a model/may annotation.

## identifiers and evidence

All47 declared named IDs checked through originals/issuing SQL and independent 76-input positive replay;25 ontology names separately queried by reviewer. All57 edges and81 evidence items read, with23 reference bindings. Stable external IDs retained; no invented tetramer or encoding predicate. PWML failure is preserved, not silently repaired. Source-version labels distinguish current export acquisition, older archive and specific database releases.

## helper and fail closed controls

Read full author replay implementation. It resolves native directions from original RDF, binds source/projection/runtime/reference hashes before use and rechecks before publishing accepted outputs, checks imported PathwayMech runtime files and outputs. Reviewer-executed positive run passed76inputs/17outputs; all17 output hashes independently checked. Reviewer-seeded reversed RHEA27644 failed with NATIVE_DIRECTION_MISMATCH and no accepted result. Reviewer-owned seven semantic controls passed. Native-helper checks are not a substitute for source reading; they did not detect finding422.

## Validation and limits

Reviewer-executed author replay passed with76 bound inputs and17 output artifacts. Independent native traversal checked3 Rhea directions and14 sides, and rejected7 scientific mutations. An independently seeded author-replay mutation was rejected with no accepted output. Full author150/preflight104 artifact seals were checked twice.

- One open minor finding422; no major or blocker findings. Original target is not approved for maintained adoption until this is corrected.
- Current review is external and independent of authorship; production PathBank/Entrez authority implementation is separately reviewed.
- Canonical authority regeneration, current merged-corpus dedup, history, native saved review, complete rendering/validation/tests/lint/KGX and PR workflow are integration requirements, not outcomes of this external review.
- Whole-ontology SQL files were fully hash-bound before use and before publication in reviewer-executed author replay; reviewer subsequently rechecked small originals/runtime and upstream artifacts. Filesystem checks are bounded and do not claim an atomic snapshot.
- No newly retrieved broad literature search or iModulon adapter run; exact retained primary/native sources were inspected. No negative biological conclusion from missing expression-module data.
- Programmatic SVG/KGX checks passed through replay; no browser visual inspection claimed.
- No public-release licensing disposition or global source-exhaustion claim.

The immutable JSON contains per-edge assessments, exact source/runtime bindings, actual terminal receipts and failed harness attempts. This external assessment is not a native maintained review bundle.
