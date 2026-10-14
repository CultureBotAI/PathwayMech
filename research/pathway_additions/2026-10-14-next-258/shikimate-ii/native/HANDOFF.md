# Shikimate degradation II native closure and identity handoff

All author work is external under `/private/tmp/pathwaymech-next-258-native`. No maintained record, source adapter, authority snapshot, policy or generated page was edited. Root owns final assembly, authority selection, tests, independent review and publication.

`native-coverage.json` closes 53 complete native objects, 853 direct XML slots, all six activities attached to the two formal reactions, and 22 protein/component/gene references. `native-fact-dispositions-compact.json` indexes every direct slot with a complete recursive semantic-projection hash and serialized XML slot hash. `source-projection-compact.json` retains biological/identity details; administrative slots and global chemical reverse indexes remain exactly reconstructable from hash-bound complete originals. `narrative-claims.json` splits 27 pathway/included-enzyme narrative claims plus eight current ShiA/ShiR UniProt annotations. No completeness claim beyond these explicit sources is made.

The formal route is **RXN-20484 then DHSHIKIMATE-DEHYDRO-RXN**, both selected L2R. RXN-20484 is explicitly NAD dependent and maps to RHEA:17742 only after root's molecular audit. Its EC label differs from Rhea's and is not enzyme equivalence. Newly fetched **RXN-11174** uses generic NAD(P)/NAD(P)H classes despite its RHEA:17742 unification link: it is not an exact whole-reaction mapping. Its E. coli YdiB activity, kinetics and assembly are boundary context. DHQ dehydration is bypassed in shikimate II. Protocatechuate ortho cleavage is only a downstream pathway interface.

The native PWY-6419 narrative incorrectly identifies **qutB/G-11736** as the second bacterial operon enzyme. Complete G-11736/MONOMER-15333 objects show fungal A. nidulans QutB. Correct second-step identity is **ENZRXN-17385 → MONOMER-15334 → G-11737/qsuB/cgR_0493**, matching the R-strain primary context. Its native 2009 evidence remains inference from operon, similarity and induction, rather than a purified R-QsuB assay. The later ATCC13869 QsuB assay is separate.

Native **CPLX-7981** contains two MONOMER-15330/Q9X5C9 subunits. Its accession Cgl0424 and issuing UniProt object identify **ATCC13032**, unlike R QsuD **A4QB65/cgR_0495**. Native activity evidence mixes a purified heterologous protein source (18566515) with R genetics (19376919); the proposals keep these claims separate. The native shikimate Km is **46600 micromolar (46.6 mM)**. Native NAD preference and >300-fold lower NADP turnover are scoped database assertions, not absolute absence of NADP activity. `QsuD-construct-replay.json` freshly confirms the 302-aa 2NLO structural sample equals the 19-aa extension MSGHHHHHHGSEQLYFQGA plus all 283 Q9X5C9 residues; cleavage state of every kinetic preparation remains unverified.

`native-graph-proposal.json` supplies five edges: native QsuD homodimer composition; qualified ATCC13032 shikimate catalysis; inferred R QsuB enables; ShiA location at GO:0005886 plasma membrane; and RHEA:24849 `provides_input_for` the downstream ortho-cleavage pathway. The downstream node is explicitly `category: pathway` in the proposal's `reactions` list, not a third formal member. Canonical MetaCyc HTML was acquired for its new authority candidate. References bind exact raw payloads. Root should integrate primary claims rather than duplicate them. The plasma-membrane annotation is experimental in current UniProt; multipass topology is an inference. UniProt's H+-symport RHEA:28973 annotation is ECO:0000305 and must not become direct experimental proton stoichiometry. Primary PMID25406451 establishes uptake and transcription effects; its accessible abstract alone does not establish ShiR binding-construct details or direct shikimate ligand binding.

## New ShiA/ShiR and exact regulatory gene endpoints

The primary agent found PMID25406451: **ShiA/cgR_2523** is the actual R-strain shikimate uptake protein, distinct from inferred **QsuA/cgR_0492**. Exact current proteins are **UniProtKB:A4QH18 / NCBIProtein:BAF55534.1** (ShiA) and **UniProtKB:A4QH19 / NCBIProtein:BAF55535.1** (ShiR). Individual issuing objects and complete KEGG CDS objects were fetched.

`transport-gene-identity-reconciliation.json` proves four KEGG CDS translations match exact R-strain NCBI proteins; the QsuD, ShiA and ShiR proteins also match their full UniProt sequences. ShiR begins GTG; NCBI declares translation table 11 and bacterial initiator methionine handling is explicit. An initial naive start-codon comparison failure was retained, then corrected scientifically.

| Gene endpoint | Native locus | Protein | Protein/CDS length |
| --- | --- | --- | --- |
| KEGG:cgt:cgR_0492 | qsuA | BAF53459.1 | 467 aa / 1404 nt |
| KEGG:cgt:cgR_0495 | qsuD | BAF53462.1 / A4QB65 | 283 aa / 852 nt |
| KEGG:cgt:cgR_2523 | shiA | BAF55534.1 / A4QH18 | 450 aa / 1353 nt |
| KEGG:cgt:cgR_2524 | shiR | BAF55535.1 / A4QH19 | 295 aa / 888 nt |

All four KEGG `ENTRY` records explicitly say CDS/T00501, `ORGANISM` is cgt/Corynebacterium glutamicum R, and native positions match NCBI `coded_by`. The separately retrieved issuing T00501 genome record explicitly gives ORG_CODE cgt, NAME Corynebacterium glutamicum R, TAXONOMY TAX:340322 and chromosome AP009044; `genome-gene-consistency.json` audits all four gene/genome pairs. Preserve `NAME (GenBank) hypothetical protein` as annotation metadata; exact native locus is available for canonical gene identity. Root is implementing the needed strict KEGG gene authority capability, because current module/reaction/compound parsers do not cover CDS genes. Select only gene nodes actually used; the shiR gene need not be added merely because its protein regulates shiA.

Fresh NCBI exact locus queries found only discontinued GeneIDs: qsuA4994327, qsuD4994338, shiA4991808, shiR4993621. Complete fresh gene objects all have discontinued status and no current-id successor. Current WP entries are nonredundant multi-genome protein identities without GeneID, not alternate exact regulatory gene endpoints. These rejected alternatives are retained.

## Boundaries, provenance and retention

N. crassa Qa4, A. nidulans QutB and Amycolatopsis quinate facts do not establish whole-route shikimate-II occurrence; AsbF is petrobactin context; Gluconobacter and Acinetobacter shared dehydratases are PQQ-route context. Broad Bacillota/Actinomycetota ranges are not universal phenotypes. QsuA transporter inference, QsuC coexpression and HPPD domain similarity are not promoted to new measured pathway steps.

`original-bindings.json`, `source-reuse-verification.json`, acquisition receipts, reproducible helpers and `helper-checks.json` preserve source reproducibility. Initial sandbox DNS failures and the initial translation-check failure are retained. Complete originals stay external; retain JSON/Markdown plus byte-identical helper `.py.txt` copies and an exact retention map. `artifact-manifest.json` enumerates those artifacts. No source exhaustion, final record acceptance, independent scientific review or repository gate success is claimed by this author package.
