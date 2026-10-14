# Quinate degradation II: native source and biological identity handoff

Scope: MetaCyc PWY-6416, version 27.0. All work is external; no maintained record, schema, adapter, or authority configuration was edited.

## Files to retain compactly

- `native-coverage.json`: all 73 retrieved native objects, dispositions, 18 activities, and 30 recursively closed protein/component/gene references.
- `native-fact-dispositions-compact.json`: every one of 998 direct native object slots, with exact locator, disposition, reason, and deterministic projection digest.
- `source-projection-compact.json`: substantive biological slots and chemical identity slots, with explicitly listed omitted slots. Full source objects remain hash-bound externally.
- `authority-candidates.json`: 30 independently retrieved identifier candidates; select only nodes actually used. Three UniProt unknown-function cluster proteins are context only; ANU32720.1 is accepted as the source gene after exact strain, CDS and published primer reconciliation, with the complete assayed internal sequence unavailable.
- `native-graph-proposal.json`: eight source-backed graph additions and their local references, nodes, construct qualifications, and exact locators. Root owns final chemistry mappings and merges these with the primary paper proposals.
- `protein-identity-candidates.json` and `supplemental-biological-context.json`: all 20 queried individual UniProt records, including the deleted R-strain QsuB entry and unknown-function qa/qut cluster components.
- `QsuD-construct-identity.json`: exact PDB 2NLO sequence comparison against Q9X5C9.
- `QsuB-ATCC13869-primer-check.json`: exact genomic CDS translation and P3/P4/P5 primer matching for candidate ANU32720.1.
- `artifact-manifest.json`, `original-bindings.json`, acquisition receipts, and reproducible helper sources.

Do **not** commit `originals/`, `native-fact-dispositions.json`, or `source-projection.json`. Those include complete upstream payloads and large water/proton reverse indexes. The compact ledger covers every slot without copying those payloads.

## Native pathway closure

The three formal members are QUINATE-5-DEHYDROGENASE-RXN, 3-DEHYDROQUINATE-DEHYDRATASE-RXN and DHSHIKIMATE-DEHYDRO-RXN, each selected L2R by PWY-6416. The middle reaction is natively reversible. The first reaction uses generic NAD(P) classes; it is not exactly the NAD-specific Rhea reaction. The five native species assertions are Corynebacterium glutamicum (species and strain R separately), Amycolatopsis methanolica, Aspergillus nidulans and Neurospora crassa. The broad fungal/phylum taxonomic range does not establish universal phenotypes.

Of the 16 activities directly linked to the formal reactions, relevant native enzyme contexts include A. nidulans QutB, A. methanolica AroQ, N. crassa Qa4, and the inferred R-strain QsuB/QsuC activities. E. coli YdiB is explicitly nonphysiological. E. coli AroD, Bacillus subtilis AroC, archaeal and yeast enzymes, and Arabidopsis DHQ-SDH belong biosynthetic or nonmicrobial contexts. Gluconobacter and Acinetobacter enzymes belong the PQQ route already curated separately. Bacillus anthracis AsbF is a petrobactin precursor enzyme. Their components and regulatory annotations were inspected and explicitly excluded rather than inherited through a shared reaction.

QsuD is mentioned in the pathway narrative but its native activity is linked to the more specific RXN-20483. Its sibling RXN-20484 is shikimate oxidation and remains an alternative-substrate boundary. CPLX-7981 contains two MONOMER-15330/Q9X5C9 subunits. CPLX-7980 contains twelve MONOMER-15327/P46380 subunits. Catalysis belongs to the respective complex; subunit membership alone is not independent catalysis.

## Identity and evidence cautions

1. The native pathway's direct PMID 8002591 and 14586099 evidence belongs to the PQQ alternative. It must not support the NAD-dependent route.
2. Q9X5C9 is ATCC 13032, while A4QB65 is strain R. Native species-level enzyme labels and the 99% identity reported in the literature do not make these proteins interchangeable.
3. UniProt A4QB63 is deleted, without a redirect. Native gene G-11737 identifies cgR_0493; issuing protein BAF53460.1 identifies that exact R-strain locus. QsuC A4QB64 remains active but its enzyme and assembly annotations are by HAMAP/inference.
4. R-strain regulator QsuR is NCBIProtein BAF53458.1 (cgR_0491); QsuA is BAF53459.1 (cgR_0492). Their retired Entrez Gene objects are useful history, not asserted current active genes.
5. Fungal qa/qut enzymes, regulators and transporters are meaningful pathway components even where omitted from the native activity list. Their issuing records and the primary agent's papers provide the necessary extension. Unknown-function QaX, QutG and QutH remain context only.
6. P11636's canonical protein label says qa-x, but its gene name is qa-y, ORF NCU06026 and GeneID 3875775. P11634 is the distinct qa-x/NCU06021 protein. Preserve canonical authority bytes and explain the contextual gene-based transporter label; do not merge these identities.
7. The QutB paper's Methods/Results describe an N-terminal metal-chelating fusion from pRSETB/pRF2, while its Table 2 and native prose use GST wording. The preparation discrepancy must remain explicit.
8. The 2NLO structural sample is an N-tagged wild-type ATCC 13032 Cgl0424 protein from pETNHis in BL21(DE3). Its 302-residue sequence is exactly the 19-residue prefix MSGHHHHHHGSEQLYFQGA plus the full 283-residue Q9X5C9 sequence. This does not independently establish every kinetic preparation's cleavage state.
9. The 2020 QsuB experiments used strain 2256/ATCC 13869, not R or ATCC 13032. Candidate ANU32720.1 has exact ATCC 13869 source metadata and a misleading historical dioxygenase label. Its CDS translates exactly; all three published primers match, including Phe297 truncation and C-terminal His6 tags. The primary agent inspected the figures and found no printed full sequence: Figure 1 is pathway chemistry and Figure 2 is the structure model. The exact source gene is accepted, with the undeclared internal assay sequence retained as a limitation.
10. Some UniProt annotations state a biosynthetic role for QsuD; the specific catabolic knockout/auxotrophy evidence must control the final pathway scope. Do not turn generic annotations into additional biosynthetic edges.

The root agent owns final record creation, authority union selection, validation, independent reviews, and publication. No claim of exhaustive pathway-source exhaustion is made here.
