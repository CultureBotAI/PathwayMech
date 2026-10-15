# PWY-5417 biological issuing-identity source handoff

This is a bounded source-author package for MetaCyc:PWY-5417 (catechol degradation III). It is not an independent scientific review, a maintained record, or a current-corpus deduplication decision. No maintained files, Git state, or GitHub objects were changed. Repository integration must use the verified post-262 merge baseline supplied by root; this package does not depend on the removed 262 worktree.

The exact native package manifest is `302c4e494f3bfc92f4062e223f5bf7316451e29bc1e4ca52e97b32d70671abcc`. Its 394 files were hash-checked with an inventory that includes hidden and ignored files. The exact primary package is separately frozen with manifest `87fdb4ab693eda355d2f16070721a776e4468f905b4f0abdcfaa111ce2fd5cd2`. These are source-owner dependencies, not substitutes for their issuing originals.

## Finite coverage

- All 59 native protein/gene objects: the 51-object formal catalyst closure plus eight explicit adjacent conflict/preparation objects.
- All 20 formal activities, their 19 distinct catalysts, exact gene/products and component coefficients, including absent coefficients.
- All 11 parent-organism annotations: nine direct issuing taxon joins; mt-2 and Rm2011 remain ungrounded native strain contexts.
- 98 exact issuing originals: 21 UniProt (19 direct native, two explicitly separate context accessions), 24 NCBI protein records, nine nucleotide records, 16 taxonomy records, four Gene XML files covering five GeneIDs, and 24 files for six PDB preparations.
- All 45 deposited nucleotide CDS translations independently reproduced. Eighteen native active UniProt/first-deposit protein comparisons comprise 16 exact matches and two completely reconstructed from issuer sequence-conflict annotations. Six additional NCBI protein views match their exact counterparts. Twelve cloned-CDS comparisons include the separately scoped PcaR context.

`biological-identity-decision-ledger.json` gives every object, activity and parent row a disposition and binds all 21 catalyst/adjacent preparation decisions. `native-conflict-identity-dispositions.json` accounts for all 18 native conflicts, including explicit primary/chemistry handoffs. `issuing-original-provenance-index.json` and `issuing-original-usage-ledger.json` provide the complete original-to-receipt and original-to-assessment paths. New acquisition failures (DNS and one rate-limit response) and subsequent successful retries are preserved separately; no failure was overwritten as success.

## Material identity limits for integration

1. PcaD's historical 30–33 kDa oligomer, approximately 11 kDa dissociated subunits and inferred trimer belong to the PRS2260-from-2178 preparation. Q88N36 is a separate 263-residue/28656-Da KT2440 sequence. The historical paper's transformed text was read in bounded relevant sections; figures were not viewed. No historical-to-modern accession or strain equivalence is established.
2. Q9AEQ0 is deleted with no replacement accession in its issuing response. Native-linked AY029000/AAK33066.1 and C-1 PDB2AZQ/Q51433 are distinct exact sequences and contexts. Current Q51433 itself differs from the deposited 2AZQ chain at two positions. Never replace the deleted pointer with that structure mapping.
3. CatB P08310 and CatC P00948 differ from their native-linked M19460 deposit sequences; the issuing sequence-conflict features exactly reconstruct both deposits. PDB1MUC, F329I 2MUC and I54V/truncated 3MUC retain their own source sequence numbering and octameric biological assemblies. `src_method: nat` does not erase the explicit mutants. PDB1MLI has a distinct engineered 96-residue sequence and biological decamer; its expression host is not supplied.
4. The five historical cloned MT1 SalD/SalC/CatA/CatB/CatC sequences exactly match their current UniProt sequences. This closes sequence identity, not assay attribution. CatC remains uncharacterized/homology-based; its current ARBA homodecamer annotation is inferred. The native contradictory CatA assay tail is not repaired by sequence equality.
5. Q845J8 is exactly AJ000330/CAD76924.1, deposited as `paaE`, while native uses the later `paaJ` name. AJ000330's actual deposited `paaJ`/CAD76935.1 is a different ring-oxidation complex protein. Accessible PaaK-only text and partial thiolase primary access leave preparation gaps intact.
6. H16 direct pcaI/pcaJ/pcaF products and Q0K4S5/Q0K4S4/Q0K4S3 sequences agree with CAJ94999.1/CAJ95000.1/CAJ95001.1. Conflicting native prose does not reverse these direct bindings. Adjacent adipate activation remains separate from the formal 3-oxoadipate CoA-transfer step. All four native NCBI Gene pointers are explicitly discontinued. Q88N36's different current GeneID points to P. alloputida and is not an automatic KT2440 replacement.
7. Historical PcaIJ 2+2 coefficients remain separate from current UniProt heterodimer annotations. PcaF's cloned sequence is not an oligomer measurement. P. knackmussii components without sequence pointers and PS12's unknown gene/absent coefficient stay explicit; no homolog or monomeric assembly is guessed.
8. Taxon384 and taxon386 are distinct; 386 currently has the name R. leguminosarum bv. trifolii and rank `no rank`, unlike the native strain rank. JMP134 is currently C. pinatubonensis. E. coli MG1655, broader K12, Thermobifida B6, YX donor and E. coli BL21 expression contexts are not merged. PDB7VTR exactly matches Q47RK4 and is a biological tetramer, but this preparation does not establish a whole catechol route in any host.
9. Separate PcaR Q52154 exactly matches the deposited L33795/AAA57136.1 sequence. Its issuer explicitly leaves the initiator uncertain among Met-1, Met-23 and Met-45. This does not supply a native PcaR frame, a measured N terminus or a direct ligand-activation edge. Primary author retains PRS2000 lineage and the Methods/Fig6 pHS104 host discrepancy.

## Verification and retention

The read-only source-author replay is:

```text
python3 -B /private/tmp/pathwaymech-next-263-biological-identity/helpers/verify_identity.py.txt
```

It reads exact originals without network requests or writes and checks cohort completeness, native direct relations, parent joins, all deposited translations, protein sequence conflicts, six PDB sequences/assemblies/mmCIF contexts, and inactive/discontinued identifiers. `receipts/identity-verification.json` is the successful receipt. This self-check does not replace later independent scientific review.

`compact-retention-manifest.json` is the sole finite copy contract for `compact-retained/`. Every row uniformly includes actual `original_path`, `original_bytes`, `original_sha256`, relative stored `path`, `bytes`, `sha256`, and `encoding`. Gzip uses mtime zero and is verified lossless. All helper source is inert `.py.txt`. Raw originals are retained losslessly compressed; there are no active `.py` files or raw diff/log whitespace hazards in the compact package. The complete external package also preserves intermediate projections and parser attempts; the compact package deliberately retains the final assessments, required original evidence, acquisition receipts, and relevant helpers.

Native/primary originals remain in their separately frozen owner packages; `external-frozen-source-dependencies.json` gives the exact finite required files. Issuing originals reused from earlier packages have their own byte-identical copies here. The PcaD text is retained by its primary owner with exact transformation-to-original web receipts; this package retains those bindings and the reading limit, not a second full article copy. Original absolute paths in assessments identify the bytes actually inspected. Consumers must use the compact manifest's original-to-stored map and the native/primary owner manifests rather than rewriting a stored gzip hash as an original XML/JSON hash.
