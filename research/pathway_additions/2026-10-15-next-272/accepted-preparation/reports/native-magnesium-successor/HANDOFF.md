# EutP/Q magnesium interpretation successor

This bounded supplementary correction confirms independent finding `next272-preparation-eutpq-divalent-cation-scope`. It supersedes only the affected scientific interpretations in the frozen native preparation. All parent packets and raw database assertions remain immutable. The successor is authored by the original native preparer after direct targeted reading of the retained primary original; independent acceptance belongs to the reviewer/root.

**Corrected conclusion:** PMID26448059 reports no observed loss of EutP/Q activity after EDTA dialysis. The documented coupled kinetic assay adds 6.6 mM MgCl2; HPLC reactions add 1 mM MgCl2. The EutQ NMR reaction additionally contains 5 mM MgCl2. These results support reported EDTA-treatment resistance under the study's documented magnesium-containing assay conditions, not magnesium-independent catalysis. The EutQ EDTA comparison is explicitly data not shown, and the paper specifies no separate magnesium-free assay for that comparison. This distinction also prevents inferring a bound-magnesium cofactor or physiological magnesium requirement merely because magnesium was added to the reaction mixture.

## Exact evidence

The self-contained original `originals/PMC4857615-efetch.xml` is byte-identical to the frozen primary packet (SHA256 `44360d646bf5b6b3f123b0655788eb27a8a9ce470ba493ba4e6fc4c4ab725d26`). `results/primary-reading.json` provides six original XML locators, element hashes, short snippets totaling 22 words and targeted paraphrases:

- Results P13: EutQ dialysis in 2 mM EDTA, three buffer changes at 4 C for two hours each; unchanged activity, data not shown.
- Results P14: unchanged EutP specific activity after EDTA dialysis.
- Discussion P20: the authors' stronger no-divalent-metal/nonmetalloprotein interpretation, retained as interpretation rather than independently proved metal-free catalysis.
- Methods P39: coupled kinetic assay with 6.6 mM MgCl2.
- Methods P40: both HPLC reaction arrangements contain 1 mM MgCl2.
- Figure F8 caption: EutQ NMR reaction with 5 mM MgCl2; nucleotide chemical shifts attributed to magnesium complexation.

Both LT2 UniProt originals, P0A208 and Q9ZFV5, assert “Does not need divalent cations.” at `/comments/3/note/texts/0/value`, citing PMID26448059. Those exact original annotations remain preserved, with issuing receipts. The K12 originals P76556 and P76555 contain no equivalent COFACTOR absence assertion; the original shared role text had improperly carried the broad interpretation into their derived protein/comment dispositions. K12 scope is now explicitly separate from the LT2 experiment.

## Affected interpretation inventory

`results/successor-dispositions.json` supplies 25 exact old/new interpretation fields with parent file hashes and JSON pointers. It covers four P/Q protein dispositions, twenty role-based P/Q comment dispositions and the grouped P/Q conflict disposition. Eleven contain the direct overstatement (two protein rows and nine EutP comment rows). The additional fields receive consistent qualification, including the EutQ COFACTOR row whose preserved raw statement otherwise lacks the necessary assay-method caveat. No source statement field is rewritten.

`results/occurrence-inventory.json` records a physical scan of all 621 native-parent files, including hidden and ignored files. Ten files match the specified exact claim strings. It distinguishes raw issuer/search assertions, source projections, three current interpretation ledgers, two generators and one historical failed helper. The frozen generators' EutP role text and grouped P/Q conflict text must not be replayed into a future accepted record without this successor. Their exact copied source and affected line numbers are included. Historical failed-helper text remains historical. This is an exact-string search plus a semantic audit of all four P/Q protein rows and all P/Q comment rows, not a claim to discover every imaginable paraphrase.

Full copies of the three affected interpretation ledgers and two generator sources are included under `inputs/native/`, permitting offline pointer verification. The preserved exact native and primary manifests/freeze proofs establish parent bindings. There is no change to the support for reversible acetate-kinase activity, the five-member pathway boundary, taxon identity or protein identity.

## Future record and graph limits

A future record may describe EutP/Q acetate-kinase activity with organism, recombinant preparation, conditions and evidence scope. If the EDTA result is relevant, it must retain the magnesium-containing assay qualification. Magnesium can be recorded as an assay constituent where the existing schema permits it.

The source does not justify magnesium-independent, divalent-cation-independent, metal-free or cofactor-free catalytic claims. It also does not justify a new enzyme-bound Mg edge, a fixed metal stoichiometry, an established physiological Mg requirement, or direct transfer of LT2 observations to K12. Added Mg could contribute to nucleotide/coupled-assay chemistry; its presence alone does not resolve the enzyme's own metal mechanism. No new schema slot or maintained graph is introduced.

## Parent bindings, validation and freeze

Native parent manifest: `d7fe7fedf9315c241782ce9b26729804461dda646ba903da312fba0996054d13`.
Primary parent manifest: `86974c5ce2562d549755f18b30fa27a14ac6c6d5007b476aaeefe105eaa36ada`.
The native parent's bound core packet remains untouched; no core identity conclusion is changed by this assay interpretation.

`results/parent-bindings.json` provides each copied source path, size and SHA256. `scripts/verify.py` verifies all local copies against these bindings and parent manifests, resolves all old interpretation pointers, checks the six XML elements and confirms the source-annotation/interpretation separation. No network, installs, maintained files, runtime, Git or GitHub changes occurred. All jobs are terminal. One initial helper assertion expected exactly 25 quoted words instead of an upper bound; the 22-word excerpt set was unchanged, the failed receipt preserved, and the corrected check passed.

`artifact-manifest.json` inventories every physical file except itself and `freeze-proof.json`; the freeze proof binds that inventory and this handoff. Any later amendment requires a new packet. Independent acceptance is not asserted here.

## Additional requested metadata/context corrections

The original front matter of PMID27063436 / PMC4827028 / DOI10.1038/srep24359 lists Mark Held, Alexander Kolb, Sarah Perdue, Szu-Yi Hsu, Sarah E. Bloch, Maureen B. Quin and Claudia Schmidt-Dannert in that order. Therefore frozen primary reading-ledger S24 `/sources/23/citation` should read **Held, Kolb, Perdue et al.2016**, replacing its Quin et al.2016 label. `results/citation-successor.json` binds the original author list, exact old field and replacement. The complete original XML and receipt are copied; this is targeted metadata inspection and does not change any biological interpretation.

The frozen root iModulonDB context packet (manifest `faeb80b7709f36e6544b059f10700f22e545aa87e58b2cfc371a0be474a2e4dd`) contains historical EutH/P76552 prose at `raw-e_coli-modulome-76-genes.body.json`, `/genes/4/uniprot_function`, describing protonated ethanolamine. That exact field is preserved and bound in `results/contextual-euth-disposition.json`, with its full contextual source copy and parent manifest/proof. It inherits the existing neutral-versus-protonated EutH conflict; expression-context text does not establish a transport microstate or mechanistic edge. The previously prepared native/primary EutH conflict is referenced, without claiming a new independent EutH paper review.
