Pre-merge scientific review of `MetaCyc:PWY0-1300`, intended owner `data/pathways/mannosylglycerate-degradation.yaml`. Reviewed draft SHA-256: `08fe9a6f3f0da2f66c4dc6cd68fc33fbe51a38770b6eeee743751f05f019d088`.

Stable review key: `mg-cdar-assay-endpoint-scope`. Severity: **major**.

The graph/export endpoint is the exact modern reference protein. Assay-specific reference numbering, preparations and loss/rescue interpretation must travel with the affected claim, rather than remaining only in an external dossier. The signs and gene endpoints are supported; this is a scope defect, not evidence that P297S or Tn5 mutants activate transcription.

Affected locations:

- `mechanistic_edges[id=mg-gark-reg-cdar].subject`
- `mechanistic_edges[id=mg-cdar-auto].subject`

Evidence:

- PMID:10762278: The study uses MC4100 loss/rescue and reporter systems; its reference describes 391 residues, paper-numbered P297S in JA176 and a near-terminal Tn5 insertion in JA177. pRM1 carries MC4100 sdaR in pBluescript. Positive autoregulation is inferred from reporter responses and loss of functional sdaR. Source SHA-256 `558ddd8487022da44e22f533f49a4f2d8d9c433fd2cdfa3bd6613449c702c391`; /html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[5]/p[1]; same section p[2]; section[6]/p[1] and p[2].
- UniProtKB:P37047: The current issuing reference is P37047 with 385 residues. The author dossier retains this mismatch, but it is not on either regulatory subject endpoint in the YAML/page/export claim. Source SHA-256 `510779d935c3ec17cf2702a2be40300f544d6cea4a25924e72e31232dbaf1789`; primaryAccession; sequence.length; genes.

Required correction:

Qualify the subject of both affected edges as experimental_construct with exact source-limited MC4100 reporter/loss/rescue context and the 391-aa paper/current-385-aa reference distinction. Preserve paper residue numbering without silently mapping it to the modern chain. Distinguish active reference or rescued regulator from loss-of-function mutants used to infer its role; do not mint a new protein ID or label mutant proteins as active.

Acceptance:

- Both affected CdaR subject endpoints retain evidence-backed qualification in YAML, graph and KGX.
- Current P37047 identity and both existing positive expression signs/gene targets remain unchanged.
- No asserted sequence equivalence, direct ligand binding or active P297S/Tn5 phenotype is introduced.

Provenance: independent scientific review handoff SHA-256 `36cbadc214456c366a4d579909daedd128458b398eac594f0670fbdc839e5b7a`; findings SHA-256 `51d37e63e7402def8ed72b2ebe6686c92aad4b94efe655da5f6205b6611ddb88`. Full original author and review packets remain immutable. Close after the corrected record and preserved review dispositions merge.

Primary sources: [Sampaio et al.](https://doi.org/10.1074/jbc.M310980200), [CdaR study](https://pmc.ncbi.nlm.nih.gov/articles/PMC111340/), [PtsI](https://www.uniprot.org/uniprotkb/P08839/entry), [H-NS](https://www.uniprot.org/uniprotkb/P0ACF8/entry), [Rhea](https://www.rhea-db.org/rhea/27378).
