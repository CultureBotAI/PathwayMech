# Pathway mechanism research: fructoselysine catabolic process

## Pathway scope

- Maintained record: `GO:1901281`, `data/pathways/fructoselysine-catabolic-process.yaml`.
- Selected proteins: reviewed `UniProtKB:P45543` (FrlD/YhfQ) and
  `UniProtKB:P0AC00` (FrlB/YhfN), both assigned to `NCBITaxon:83333`,
  Escherichia coli K-12. The primary abstract describes E. coli biochemical
  experiments; the exact K-12 protein scope comes from the inspected UniProt
  entries, rather than an assumed experimental substrain.
- Scope: the two-enzyme ATP-dependent route from fructoselysine to glucose
  6-phosphate and lysine. Transport, upstream psicoselysine epimerization,
  transcriptional regulation and other-organism routes are contextual evidence.
- QuickGO defines the exact catabolic process and cites UniPathway `UPA00784`.
  Both proteins independently carry that same UniPathway accession, with native
  reaction accessions `UER00769` and `UER00770`, and explicit steps 1/2 and 2/2.
  These native cross-references bridge the GO identity to the selected route;
  no UniPathway CURIE was invented as a maintained node.

## Mechanistic summary

The original primary study characterizes purified YhfQ and YhfN after expression
in E. coli. FrlD phosphorylates fructoselysine, and NMR identifies the product as
fructoselysine 6-phosphate. FrlB then converts that intermediate and water to
lysine and glucose 6-phosphate. The FrlB reaction is experimentally reversible;
`RHEA:28383` selects the catabolic orientation without claiming irreversibility.
The kinase is represented by `RHEA:28379`.

All nine chemical sides of the two directed Rhea equations are retained,
including ATP, ADP, hydron and water. Each native coefficient is 1, read from
reaction-side `rh:contains1`; coefficients are source facts, not duplicated
graph edges. The intermediate is the ionic species `CHEBI:61392`, rather than
an assumed neutral form. Glucose 6-phosphate is the exact Rhea-linked
`CHEBI:61548`, and the lysine product is `CHEBI:32551`. Canonical authority labels
are used for every node, including the full Rhea equations and exact UniProt
recommended protein names.

## Evidence table

| Maintained edges | Mechanism | Inspected support |
| --- | --- | --- |
| 001–005 | FrlD reaction substrates and products | Rhea 142 directed reaction 28379, native sides, compounds and `contains1` coefficients |
| 006–009 | FrlB reaction substrates and products | Rhea 142 directed reaction 28383 with the same exact native locators |
| 010 | FrlD catalysis | P45543 catalytic annotation, ECO:0000269/PMID:12147680; Rhea master/directional bridge; exact short primary excerpt |
| 011 | FrlB catalysis | P0AC00 catalytic annotation, ECO:0000269/PMID:12147680; Rhea bridge; primary reversibility excerpt |
| 012–013 | Both reactions belong to fructoselysine catabolism | UniProt pathway/UniPathway assignments, explicit GO definition cross-reference, independently cited Rhea reaction identities |
| 014 | Kinase precedes deglycase | UniProt native steps 1/2 and 2/2, shared chemical intermediate and primary observation of delayed glucose 6-phosphate formation |

The protein pathway evidence is not uniformly experimental: FrlD's PATHWAY
annotation uses `ECO:0000305`; FrlB's uses `ECO:0000269` and `ECO:0000305`.
Both catalytic annotations use `ECO:0000269`. Monomeric FrlD and homododecameric
FrlB annotations have explicit SUBUNIT locators and experimental evidence codes
in their catalyst edges. No unsupported protein-complex accession is minted.

Three short excerpts from PMID:12147680 were checked against the actual abstract;
their combined length is 17 whitespace-delimited words. Structured database assertions are never
presented as quotations from the papers cited by those databases.

## Gaps and source-fact dispositions

- Neither selected UniProt entry has a COFACTOR or SUBCELLULAR LOCATION comment.
  This is an annotation omission, not evidence of cofactor independence or
  compartment absence. No generic kinase metal or guessed compartment was added.
  The original full article was not obtained: both legacy and current JBC PDF
  endpoints returned HTTP 403; the public Elsevier API supplied bibliographic
  metadata without article text. Mechanistic conclusions above use the inspected
  original abstract and exact reviewed database statements, not inaccessible text.
- The FrlB entry reports strong ZnCl2 inhibition (ECO:0000269/PMID:12147680).
  This is retained as an in vitro context fact; no concentration or physiological
  metal-regulation claim is inferred from the annotation. A dedicated inhibitor
  edge is outside the selected core conversion. ATP remains a consumed substrate,
  not an inferred permanently bound cofactor.
- UniProt also reports substrate-dependent induction, FrlB deletion phenotypes,
  and kinetic parameters. These support the contextual pathway assignment but
  are not converted into ungrounded transcriptional or phenotype nodes.
- PMID:14641112/DOI:10.1042/BJ20031527 directly establishes a reversible
  fructoselysine/psicoselysine epimerase and FrlA/FrlB mutant growth phenotypes.
  FrlC supplies an upstream route into the fructoselysine substrate pool; it is
  not necessary to represent the selected two-step breakdown of fructoselysine.
  The slower FrlD activity on psicoselysine is likewise not promoted into a
  second complete catabolic branch. Its abstract was inspected; NCBI BioC access
  returned 429, and an institutional PDF request timed out.
- PMID:32979851/DOI:10.1111/mmi.14608 establishes substrate-specific FrlR
  repression and CRP/RpoH activation of frl transcription. Its inspected abstract
  is evidence that regulatory physiology exists. No promoter-specific graph is
  added without resolving the exact DNA and regulator context.
- PMID:16153181/DOI:10.1042/BJ20051183 distinguishes Enterococcus faecium GfrF
  fructoselysine-phosphate cleavage from GfrE glucoselysine-phosphate cleavage.
  The putative PTS in that work is proposed to provide phosphorylated substrates;
  the inspected abstract does not establish it as the ATP-dependent E. coli
  FrlD route. Neither the other taxon nor its PTS/GfrE mechanism is merged here.
- P0AC00 also has computational IBA GO annotations for glucosamine-related
  function/UDP-N-acetylglucosamine biosynthesis. They are not used to redefine
  the directly supported fructoselysine mechanism or establish extra substrates.
- The canonical iModulonDB adapter search for `frl` in `e_coli/precise_mg1655`
  returned five gene keys (b3374 FrlD, b3371 FrlB, b3370 FrlA, b4474 FrlC,
  b3375 FrlR) and zero iModulon hits. These are expression-dataset context, not
  proof of catalysis, regulation or biological absence. The parent ran the
  adapter; its result at `/private/tmp/pathwaymech-frl-phn-imodulondb-frl.md`
  was inspected for this curation.

## Duplicate search and provenance

Searches included hidden and ignored files across the original checkout and the
new worktree, excluding Git internals, virtual environments and Python caches.
They covered the GO ID, label/synonyms, exact Rhea/UniProt/UniPathway identifiers,
primary PMID/DOI, and PathBank `SMP0002063`/`PW002049`. Matches were the previous
candidate ledger, current planning files, a broader PathBank screening candidate,
and the ignored SEED menu. None was an existing exact maintained pathway.
Bare reaction-number searches also hit unrelated hash substrings; exact CURIE
follow-up distinguished those from pathway evidence.

`fructoselysine-source-manifest.json` records actual URLs, retrieval timestamps,
artifact digests and failed source-access attempts. PMID reference digests cover
explicit two-entry Europe PMC responses, not the PubMed webpage bytes. Raw
response headers remain in the external cache; no cookies or session headers
are copied into maintained provenance. The raw Rhea digest covers compressed
RDF bytes, while the direction-table digest covers the uncompressed TSV.
`fructoselysine-source-projection.json` records all source-to-edge dispositions,
canonical reaction chemistry and evidence codes. Raw artifacts remain under
`/private/tmp/pathwaymech-frl-phn-evidence/fructoselysine`.

## Verification

Bounded native/closed-schema, chemical coverage, exact excerpt and export checks
are reported in `fructoselysine-validation.json`. Shared authority refresh,
curation history, pages, full-corpus gates and independent review are owned by
the parent integration task and remain required before publication.
