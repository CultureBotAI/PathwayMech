# GalA2005 successor author handoff

Author research only for PMID16030014 / DOI10.1074/jbc.M502585200. No maintained files were edited, no authority snapshot was promoted, and this package supplies no approval verdict. Frozen `gal2005`, `gal2014`, `gal2016` and the independent chemistry package remain untouched.

The package contains 31 source-located research facts, three evidence-shaped proposals (catalysis, Fe2+ cofactor and native complex composition), and nine additional explicit research proposals for the three inhibitory treatments, four metal rescues, ascorbate rescue and experimental assembly. The latter are intentionally not insertion-ready: their relevant results are primary prose, not native structured slots or table cells. They remain covered research rather than being dropped or relabeled as structured assertions.

## Exact preparation and identity

The source-native enzyme is `MetaCyc:CPLX-8177`, containing `MetaCyc:G1G01-2702-MONOMER`, with activity `MetaCyc:ENZRXN-18371`. Do not substitute the GalC aldolase objects CPLX1G01-155 / ENZRXN1G01-1112.

The current ENA AE015451.2 CDS at complement(2865514..2866776), locus PP_2518, supplies AAN68130.2 with 420 residues beginning MARIIGG. I independently re-read that actual feature and counted its translation. The paper's Edman observation corresponds to ARIIGG and apparent initiator-Met removal, yielding a 419-residue chain. Q88JX5 is a different 340-residue record; it is not the tested full-length protein. The old sequence begins with M where residue 81 of the full chain is V; only its remaining 339 residues match full-chain positions 82–420.

The paper's construct is pETGalA, made in pET-29a(+), expressed in E. coli BL21(DE3). The Figure 1 caption explicitly supplies BL21(DE3); the methods and Table 1 transcript instead spell BLB21(DE3), which is retained as a transcription discrepancy. The reverse primer is described beyond the native stop, but no complete pETGalA sequence is available here. Do not assert a fully verified tag-free recombinant sequence or unmeasured terminal modifications.

## Treatment and assembly findings

All chemical pretreatments used purified enzyme at 1 mg/ml, 100 mM Tris-HCl pH 7, 30 minutes at 4 C, followed by 250 microM gallate. EDTA at 1 mM left less than 1% activity; 2 mM 2,2-prime-dipyridyl abolished activity; 1 mM peroxide left 15%. Metal reactivation used 2 mM salts and another 30 minutes at 4 C. Fe2+ alone fully rescued activity; Mn2+, Cu2+ and Co2+ restored 8%, 9% and 5%, respectively. Results were not separated by the two chelator preparations. Fe3+, Mg2+, Zn2+ and Ni2+ lack individual numeric results; do not convert that omission to zero rescue.

Sodium ascorbate at 10 mM after peroxide treatment restored 50% of untreated activity after the further incubation. This is partial rescue of a treated preparation, not activation of untreated enzyme. Preserve salt/ion distinctions when issuing chemical identifiers. The native identity agent has been told which GalA treatment endpoints this package has not independently issued.

The predominant sedimenting species was about 75% of loading protein, 7.29 +/- 0.10 S and 132 +/- 12 kDa. With the calculated 47.644-kDa monomer, the data support a predominant homotrimer under those preparation conditions, not a uniform trimer population. The native component slot itself has no numeric coefficient.

## Product and negative evidence limits

The paper's OMA assignment includes keto/enol alternatives and a D2O NMR ambiguity. Figure 3 was visually inspected and explicitly shows those alternatives. This paper alone does not establish an immediate keto-only product. The parent 2011 and independent chemistry work must supply that reconciliation. PDC and decarboxylated ions were attributed to mass-spectrometric conditions; do not promote them to physiological GalA products.

All tested alternative-substrate negatives, the unquantified protocatechuate non-inhibition result, spectral non-observation, induction panel, insertional-mutant experiment and model-only active-site predictions are separately covered in `research-facts.json`. Negative activity is not inhibition, a transcriptional response is not direct ligand binding, and predicted residues are not experimental causal contacts.

## Evidence grammar and quotation budget

Only actual Table 1 cells, native XML slots and the issuing ENA feature become `source_assertion` in `edge-proposals.json`. Paper prose paraphrases occur only in the research ledger and staged proposals. The three evidence-shaped proposals are author candidates, not approved graph changes.

The two exact construct qualifiers use **22 of 25 primary quoted words in total**, counting both occurrences of each quote. Three words remain. The budget file counts placements without copying quotation text. Copying those qualifiers into further edges would increase the budget; do not silently do so. This budget/grammar constraint is the remaining reason the treatment proposals are not fully materialized as maintained Evidence objects, in addition to any unresolved chemical identity. The sibling identity agent now owns supplemental endpoint acquisition.

## Coverage and files

Scientific main text through the conclusions, Table 1's three rows and all six figure captions were read. Figure 3 alone was visually read. Figure 2's normal public page was available, but its linked image failed with 404 in this successor; the parent's normal direct request had returned 403. No further probes were made. Other figure pixels and a complete raw publisher/author PDF remain unavailable here. A retained web transcript is not a raw publisher PDF. Supplement absence is not asserted globally.

- `research-facts.json`: all 31 source-specific observations and limitations.
- `edge-proposals.json`: three proposals with actual Evidence-shaped objects and qualified experimental endpoints where used.
- `research-edge-proposals.json`: nine condition-preserving staged candidates, each with an explicit evidence and identity disposition.
- `source-coverage.json`: complete read, visual and access accounting.
- `projections/table1.json`, `projections/sequence-check.json`, `projections/native-slot-check.json`: independently inspected structured inputs.
- `reuse-receipts.json`: 20 copied source artifacts rehashed against their original bytes.
- `references.json`, `quotation-budget.json`, `verification.json`, `manifest.json`: provenance and verification.

The source originals remain external. `manifest.json` binds every package file except itself. This handoff is bounded to GalA2005; the new GalB 244-versus-258-residue issue is acknowledged but not resolved or edited here.
