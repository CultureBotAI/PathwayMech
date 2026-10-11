# Pseudouridine degradation: complete native route

The new record is `MetaCyc:PWY-6019`, **pseudouridine degradation**, in
`data/pathways/pseudouridine-degradation.yaml`. It contains both native reactions:
ATP-dependent pseudouridine phosphorylation and cleavage of pseudouridine
5'-phosphate to uracil and ribose 5-phosphate. This is a complete two-step pathway,
not a single-enzyme record or an expansion of the existing purine/pyrimidine
nucleoside pathways. The K-12 protein assignments are supported, with the strain
and assay limits below.

## Identity, novelty and source boundary

The frozen PathBank archive member `PW001887.owl` identifies
`PathBank:SMP0001901` but calls it **Purine Degradation**. Its entire native graph
contains only reactions 5150 and 5151, with P30235 and P33025, respectively. These
are the pseudouridine route; the title is not a defensible umbrella identity for
the record. Independent MetaCyc 22.5 XML supplies the exact pathway `PWY-6019`,
two reaction-list entries, their directions and their order. A full local GO
Semantic SQL search of labels and synonym predicates found enzyme activities and
RNA pseudouridylation terms, but no exact biological-process term for this route.

Eighteen fresh exact-identity and semantic searches used `rg --no-ignore --hidden`
over the accessible Git worktree, excluding only Git metadata and the virtual
environment. They covered pathway IDs, title/synonyms, proteins/genes, defining
Rhea/native reaction IDs and primary PMIDs. Earlier mentions are archive-screening
rows and native subpathway links, not an existing maintained record or a scientific
rejection. Expected matches in the new author's own files are disclosed in
`pseudouridine-search-ledger.json`. The separate original Documents checkout could
not be searched because the OS denied access; its attempted ignored-inclusive
command and error are retained. No whole-computer absence is claimed.

RNA pseudouridylation, import, uracil salvage and downstream pyrimidine-ring
catabolism are outside this exact native boundary. The record does not claim to
cover those processes. Other organisms named by MetaCyc are not transferred to
the K-12 protein core.

## Reaction chemistry and direction

| Native reaction | Native cross-reference | Selected Rhea member | Selection |
| --- | --- | --- | --- |
| PSEUDOURIDINE-KINASE-RXN | 22449, unification | RHEA:22449 | Left to right phosphorylation |
| RXN0-5398 | 18340, unification | RHEA:18339 | Right to left cleavage |

The second native cross-reference is **bidirectional**, not a master reaction.
The complete Rhea 142 RDF explicitly links master 18337 to bidirectional 18340
and directional 18339. Native pathway layout independently selects cleavage.
Master 22448 links the directional kinase 22449. All nine chemical side
occurrences have coefficient one, read from the side-level `rh:contains1`
predicate. Each record edge cites its actual side and participant URI.

Rhea selects the charged species pseudouridine, ATP(4-), pseudouridine
5'-phosphate(2-), ADP(3-), hydron, water, D-ribofuranose 5-phosphate(2-) and uracil.
The ribose product `CHEBI:78346` is a furanose with unspecified anomer; neither
the broader native ribose-phosphate class nor an aldehydo form is asserted to be
an exact match. Native neutral/charged chemical differences are retained in the
full original graph and source dispositions. Both equations balance atoms and
charge when the full ChEBI 255 formula/charge statements are replayed.

The shared intermediate is exactly `CHEBI:58380` in both selected Rhea equations.
MetaCyc additionally makes the kinase an explicit predecessor of RXN0-5398.
Reversible PsuG chemistry is preserved. The biological cleavage direction does
not mean reverse synthesis is impossible: the 2012 steady-state kinetic
measurements actually measured PsiMP synthesis, and the equilibrium favors that
direction. Those rates are not represented as forward physiological flux.

## Proteins, assemblies and organism limits

The selected taxon is `NCBITaxon:83333`, E. coli K-12. Both current reviewed
UniProt entries have that taxon. PsuK is `P30235` (`psuK`, `pscK`, `yeiC`, b2166);
PsuG is `P33025` (`psuG`, `pscG`, `yeiN`, b2165). Current UniProt 2026_03 supplies
their exact names and Rhea master annotations. Experimental evidence codes and
the PsuG HAMAP inference are stated rather than flattening them into a single
experimental claim.

PsuG has an independently named native physical complex,
`MetaCyc:CPLX0-8233`, with three copies of `EG12033-MONOMER`. The monomer has an
explicit UniProt P33025 unification and MG1655 native taxonomy. The complex
catalyzes RXN0-5398 through ENZRXN0-6547. The complete primary article
[PMID:23066817](https://pubmed.ncbi.nlm.nih.gov/23066817/) confirms that the DNA
was amplified from K-12, expressed in BL21, and yielded a homotrimer. Expression
host and biological protein origin are distinguished. P33025 is a component of
the complex; it is not independently asserted to be a sufficient catalytic
monomer.

PsuK's reviewed K-12 assignment cites
[PMID:18591240](https://pubmed.ncbi.nlm.nih.gov/18591240/), whose indexed primary
abstract describes UTI89 whole-cell pseudouridine utilization. The
MetaCyc kinase controller MONOMER-14165 is likewise a UTI89 entity, explicitly
cross-referenced to Q1R9Q6; it is not an exact identity for P30235. An ECOLI-only
EG11646-MONOMER frame cross-references P30235, but the corresponding META request
returned 404 and cannot justify manufacturing a MetaCyc identity.

The full structural study
[PMID:35783380](https://pubmed.ncbi.nlm.nih.gov/35783380/) used BL21-derived
A0A140N873 and demonstrated a dimer by solution chromatography and
crystallography. The separately inspected abstract for PMID:35346685 also
explicitly concerns strain B. These do not directly establish a K-12 assembly.
Accordingly, the record uses the supported functional `enables` relation for
P30235 and explicitly limits the strain/assembly claim. It does not assert
monomer sufficiency, invent a complex ID, or omit either pathway reaction.

## Metals and mechanistic scope

The K-12 PsuG trimer retains the three supported alternative cofactor relations
for Mn(2+), Fe(2+) and Co(2+). Primary structure shows one Mn per subunit with
one Asp ligand and five water ligands. The paper reports high activity with the
three alternatives and inhibition with Zn and, more weakly, Ni. UniProt's
cofactor statements agree. These edges do not assert simultaneous occupancy or
identify the dominant in vivo metal. Inhibition is a source limitation, not an
excuse to expand this pathway into a generic metal-regulation network.

PsuK assays in the 2022 paper used MgCl2 and KCl, but the putative Mg sites were
not modeled. No separate K-12 free-Mg or K binding/cofactor edge is justified by
those assay ingredients. This omission does not mean that the kinase is
cofactor-independent. No compartment assertion is inferred from a soluble
purification or from a pathway drawing. PsuG ring opening and the covalent lysine
intermediate are supported mechanistic context, not additional independently
identified pathway reactions.

## Evidence access and reproducibility

The source manifest records exact URLs, retrieval times, releases and complete
body hashes. Only allowlisted response metadata is retained. Native XML is
MetaCyc/EcoCyc 22.5, independently obtained HTML authority pages are also 22.5,
and the reviewed UniProt bodies report 2026_03. Rhea reference digests cover the
complete official compressed RDF 142 download; the locators identify the exact
triples used. The original PathBank member and its complete object graph are
retained even though its pathway title is rejected.

The 2008 article was available as an indexed abstract; the attempted full PDF
returned 403. No statement is presented as an inspected full-text result from
that paper. Europe PMC's initial 2012 full-text endpoint failed, but the complete
PMC BioC article succeeded and was read, including methods, structural results,
kinetics and discussion. The complete 2022 PMC9247573 JATS body was read for
construct identity, dimer results, assay conditions and structural limitations.
A guessed PMID:35814684 resolved to an unrelated whitefly paper and is explicitly
rejected in the receipt; it is not a record reference. These access and lookup
failures remain visible rather than being replaced by fabricated successful
retrievals.

The replay script reads the raw bodies rather than treating the curation
projection as authority. It checks the native and closed schemas, every record
reference digest, retained body digests, all nine side/coefficient assertions,
both atom/charge balances, family bridges, native membership/order, physical
trimer crosswalks, current UniProt assignments, literal primary quotes and actual
KGX export preservation. `pseudouridine-validation.json` records the actual final
run. Shared identifier snapshots, histories, rendered pages and full gates are
delegated to the integrating root agent; this author replay is not a saved
independent scientific review.

Root-managed iModulonDB context searches found the psuK/b2166 and psuG/b2165 gene
names and no module-name hits. That is expression-database context, not proof of
catalysis or biological absence. Source and context receipts are maintained by
their respective owners.
