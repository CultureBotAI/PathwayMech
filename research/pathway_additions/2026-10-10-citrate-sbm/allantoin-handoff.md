# Allantoin oxamate-branch follow-up

The **E. coli anaerobic allantoin-to-oxamate route is biologically supported, but is not yet ready for a complete curated record**. This bounded follow-up did not verify an external identifier for the AllFGH oxamate carbamoyltransferase assembly. It does not block other pathway additions, and does not establish that the wider source landscape is exhausted.

Candidate identities remain PathBank:SMP0002064 (`PW002050.owl`) and MetaCyc:PWY0-41. The prior [candidate handoff](../2026-10-10-cyanate-monapterin/next-handoff.md) distinguishes this route from the maintained yeast allantoicase pathways. This follow-up creates research artifacts only: no record, authority, policy, history or generated-page changes.

## AllFGH: the remaining identity blocker

[PMID38888336](https://pmc.ncbi.nlm.nih.gov/articles/PMC11326118/) identifies AllF/Q47208, AllG/P77129 and AllH/P0AAS5 through purified coexpressed protein and genetic experiments. The experimental deletion/complementation background is **K-12 MG1655**; BL21(DE3) is the recombinant expression host. These are distinct from the later MC4100 regulatory paper mentioned in the prior handoff.

Purified reaction measurements ran **oxamate + carbamoyl phosphate → oxalurate**, because an oxalurate standard was unavailable. The physiological pathway uses the opposite direction, RHEA:22986. Current UniProt preserves that distinction: experimental catalytic evidence is separate from the inferred physiological-direction annotation. Tables 1–3 also require care: complete `allFGH` complementation restores near-wild-type oxamate, whereas single-gene and partial combinations do not provide an equally clean rescue. They do not justify treating each subunit as an independent catalyst.

The paper explicitly **assumes** a 139-kDa, 1:1:1 assembly for kinetic calculations. Its Discussion says the quaternary stoichiometry remains unresolved. Predicted or isolated subunit dimers do not determine the whole-complex copy counts. Future membership edges should leave those counts unspecified unless a later inspected experiment resolves them.

The supported EBI Search interface for ComplexPortal returned zero hits for each of `Q47208`, `P77129`, `P0AAS5`, `allF` and `oxamate`; a ribosome positive control returned 135 hits. Current EcoCyc AllF XML, OXTCase reaction XML and reaction HTML redirected to an account-required page. Those HTTP-200 HTML responses are **not** native authority records. The public MetaCyc22.5 mirror returned 404 for the AllF monomer and its pathway still carries the older hypothetical-reaction annotation. These are bounded search/access outcomes, not proof that no registry accession exists.

Next concrete action: obtain an authorized current EcoCyc export for `G6287-MONOMER`, `G6288-MONOMER`, `G6289-MONOMER` and their `component-of` assembly, then verify the assembly's independently declared identifier and all three UniProt crosswalks. If no registry has such a record, upstream registry curation is a separate action. Do not invent a local complex ID, use an EC/reaction identifier as an assembly identity, or substitute one subunit for the complex.

## AllD: reject the archived NADP alternative

[PMID23284870](https://pmc.ncbi.nlm.nih.gov/articles/PMC3527362/) and its [Figure S2 PDF](https://journals.plos.org/plosone/article/file?type=supplementary&id=10.1371/journal.pone.0052066.s002) were inspected, including the plotted supplement. At 0.3 mM NAD or NADP, with AllD added after enzymatic preparation of ureidoglycolate, the NAD trace rises strongly while the NADP trace remains near baseline. This supports selecting RHEA:15330 and excluding the archived NADP branch. It is not a universal detection-limit claim for every possible condition.

The NADPH used in Figure S9 is part of a glutamate-dehydrogenase-coupled ammonia assay upstream of AllD; it does not support NADP-dependent AllD chemistry. AllD is a supported homodimer: primary crystallography and size exclusion agree with native PathBank:SMP0002064/ProteinComplex/4022, coefficient 2.

## Assemblies and metal scope

| Enzyme | Verified native representation | Evidence disposition |
| --- | --- | --- |
| AllB/P77671 | MetaCyc:CPLX-64; PathBank:SMP0002064/ProteinComplex/1588; four copies of G6281-MONOMER | Native stoichiometry agrees with [primary gel filtration and crosslinking](https://pmc.ncbi.nlm.nih.gov/articles/PMC94829/). |
| AllC/P77425 | MetaCyc:CPLX-7524; PathBank:SMP0002064/ProteinComplex/1589; two copies of G6285-MONOMER | Native dimer agrees with reviewed and primary structural evidence. Use the current reaction to ureidoglycine, not the older direct net assignment to ureidoglycolate. |
| AllE/P75713 | MetaCyc:G6284-MONOMER; protein node | Current reviewed annotation and [RCSB 1RC6 biological assembly 1](https://data.rcsb.org/rest/v1/core/assembly/1RC6/1) are monomeric. The 2024 docking discussion's description of an AllE dimer does not establish a physiological complex. |

[AllB metal experiments](https://pmc.ncbi.nlm.nih.gov/articles/PMC141845/) used differently loaded recombinant preparations. Zinc, cobalt and nickel preparations differ in measured occupancy, activity and stereospecificity; cobalt broadens the observed stereochemical preference. The earlier AllB paper supports manganese-dependent activity enhancement as well. These are alternative conditions, not four simultaneous obligatory cofactors. The reviewed two-zinc-site annotation must not become a claim that exactly two zinc ions were measured in every preparation or that zinc is the exclusive in-vivo metal. The zinc-loaded enzyme supports the selected S-allantoin reaction.

AllC has a two-metal active site. The older native account explicitly says zinc was assigned by structural analogy; current UniProt lists zinc and manganese binding, while [PMID20038185](https://pubmed.ncbi.nlm.nih.gov/20038185/) describes manganese-dependent AAH chemistry. Preserve those provenance and metal-scope distinctions. That paper and the 2014 structural paper were inspected as primary abstracts here, not full articles. AllE's reviewed manganese cofactor and cobalt-substitution annotation should likewise remain qualified by its actual source coverage.

For AllFGH, Figure 4C varies MgCl2 in crude lysates, and purified kinetics use 10 mM magnesium. Current UniProt explicitly annotates magnesium as cofactor. This supports the reported activation/assay and reviewed annotation; it does not measure bound-metal stoichiometry or establish a universal physiological metal requirement.

## AllK: represent components or the net reaction once

Independent parsing of official Rhea142 recovered eight relevant directed reactions and their exact chemical-side coefficients. The AllK component vectors satisfy:

`RHEA:30757 + RHEA:57718 = RHEA:10154`

The first is enzyme-mediated carbamoyl-phosphate/ADP phosphotransfer; the second is spontaneous carbamate decay. If the intermediate is represented explicitly, use those two component steps and do not add the net reaction as a third serial transformation. Do not assign spontaneous decay to AllK or call it a gene-product molecular activity. The alternative net representation needs an explicit scope explanation. The prior AllK primary abstract and current reviewed comments support ATP formation; they are not a reason to double-count chemistry.

## Receipts and limits

- [Assessment and exact Rhea side projection](allantoin-assessment.json) preserves the decisions, source locators and concrete next actions.
- [Source manifest](allantoin-source-manifest.json) binds 36 successful bodies, including access-block HTML explicitly classified as such, plus every acquisition attempt. Raw files remain external under `/private/tmp/pathwaymech-citrate-sbm-evidence/allantoin`.
- [Search receipt](allantoin-search-receipt.json) records bounded registry queries and hidden/ignored-inclusive local searches in both repositories. It retains failed DNS/obsolete-endpoint attempts and successful retries.
- [Validation receipt](allantoin-validation.json) records digest, native identity/stoichiometry, supplement, registry-control and AllK vector checks. These are research checks, not corpus validation or a saved scientific review.

No full gates, full-record atom-balance audit or regulatory graph expansion were performed. Exact AllFGH identity remains the specific blocker; evidence must not be forced into an unsupported assembly representation to clear it.
