# Reactome sulfur-pathway curation, 2026-10-07

This bounded ingestion adds three *Mycobacterium tuberculosis* pathways from
official Reactome release 97 BioPAX exports. All 13 source reactions and all 177
extracted edges were reviewed. The resulting records contain 11 reactions and
169 edges. The CysM–CysO and CysK1 routes remain separate. This is a review of
these source definitions, not a complete reconstruction of sulfur metabolism.

## Artifacts and reproduction

- [source-projection.json](source-projection.json) freezes the complete importer
  projection of each export, its retrieval manifest, source pathway-order XML
  fragments, and the relevant indexed UniProt comments. This is a derived
  projection, not a claim that it contains every BioPAX field.
- [curation-plan.json](curation-plan.json) pins the source-projection SHA256 and
  records the reviewed reaction exclusions, edge changes, labels, categories,
  evidence, and additional material-flow edges.
- [curate.py](curate.py) applies that plan without network access. It validates
  the full cohort with the native and closed LinkML validators before writing;
  it refuses to overwrite any differing destination. A repeated run against
  identical artifacts is a no-op.
- [edge-dispositions.json](edge-dispositions.json) accounts for every original
  edge, including the original evidence and the final form of each retained or
  corrected edge. Added edges, removed participants, and final record hashes
  are separate fields. No excluded edge silently disappears from the ledger.

From the repository root, validate the frozen projection without writes:

```sh
uv run python research/source_discovery/2026-10-07-reactome/curate.py
```

Reproduce the records and ledger into a fresh directory:

```sh
uv run python research/source_discovery/2026-10-07-reactome/curate.py \
  --output-dir /tmp/reactome-2026-10-07-replay/pathways \
  --ledger /tmp/reactome-2026-10-07-replay/edge-dispositions.json
```

This replays the reviewed source projection; re-fetching the unversioned export
URLs is not assumed to reproduce release 97 indefinitely. The importer's
state-preserving policy and deterministic context-edge ordering are required
when comparing a fresh import against the frozen projection.

| Source pathway | Maintained record | Reactions, source → curated | Raw edges: retained / corrected / excluded | Added flow edges | Final edges |
|---|---|---:|---:|---:|---:|
| R-MTU-936654 | [O-phosphoserine route](../../../data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml) | 3 → 2 | 27 / 0 / 7 | 1 | 28 |
| R-MTU-936721 | [O-acetylserine route](../../../data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml) | 5 → 4 | 62 / 4 / 8 | 3 | 69 |
| R-MTU-936635 | [Sulfate assimilation](../../../data/pathways/mycobacterium-sulfate-assimilation.yaml) | 5 → 5 | 63 / 6 / 0 | 3 | 72 |

Here, “corrected” includes an evidence or scope clarification even when the
triple remains unchanged. Sulfate's six corrected edges comprise four moved
GTP-hydrolysis endpoints, the bounded kinase hydron assertion, and a CysQ
evidence clarification. Native validation, closed-schema validation, script
lint, deterministic replay, and complete edge accounting passed for this
cohort. Corpus-wide authority and generated-artifact checks are reported by
the encompassing ingestion change.

## Reaction decisions

The identifiers in this table have the `Reactome:` prefix in the records.

| Pathway | Reaction | Decision and boundary |
|---|---|---|
| OPS | R-MTU-936590, sulfur transfer to CysO | Excluded. Reactome states that the donor is unknown while drawing free sulfide as a placeholder. The maintained graph starts at CysO-COSH; exclusion does not deny MoeZ involvement. |
| OPS | R-MTU-936665, OPS addition | Retained. CysM uses OPS and thiocarboxylated CysO to form a carrier-bound cysteine adduct and phosphate. |
| OPS | R-MTU-936747, cysteine release | Retained. Mec hydrolyzes the adduct with water, releasing cysteine and regenerating CysO. Preserve the source zinc complex and cleaved protein state. |
| OAS | R-MTU-936655, APS reduction | Retained. CysH produces the source sulfite-family chemical and AMP, with thioredoxin oxidation. The substrate is APS even though a source GO activity label mentions phosphoadenylyl sulfate. |
| OAS | R-MTU-936703, sulfite reduction | Retained with evidence bounds. Sir activity is supported; the specific ferredoxin-pair assignment remains a Reactome assertion. |
| OAS | R-MTU-936615, serine acetylation | Retained, with direct 2013 CysE biochemical evidence added. The source's historical absence-of-assay statement is outdated. |
| OAS | R-MTU-936642, CysK1 sulfhydrylation | Retained. Keep the OAS route and PLP-containing CysK1 dimer; no CysE:CysK1 assembly is inferred. |
| OAS | R-MTU-936745, CysK2 OAS reaction | Excluded. Direct substrate experiments contradict the OAS assignment. CysK2's OPS/thiosulfate route is distinct from both maintained cysteine pathways. |
| Sulfate | R-MTU-936667, SubI sulfate binding | Retained. Keep free and bound extracellular sulfate; a binding event does not require an enzyme catalyst. |
| Sulfate | R-MTU-936631, sulfate uptake | Retained. The CysTWA transporter assembly catalyzes ATP-dependent uptake; its components are not each independently asserted to catalyze transport. |
| Sulfate | R-MTU-936729, APS synthesis | Corrected. Add the GTP, water, GDP, and phosphate endpoint edges moved from the kinase event. GTP hydrolysis is coupled to APS production. |
| Sulfate | R-MTU-936583, APS kinase | Corrected. Remove those four GTP-hydrolysis endpoints; retain ATP-dependent APS phosphorylation and a qualitative hydron product. |
| Sulfate | R-MTU-936659, PAPS dephosphorylation | Retained with evidence bounds. CysQ PAPS activity was demonstrated qualitatively; PAP was the quantitatively characterized substrate. |

## Evidence behind the corrections

**Unknown carrier sulfur donor.** Reactome's
[R-MTU-936590 description](https://reactome.org/content/detail/R-MTU-936590)
identifies the uncertainty. [Burns et al. 2005, PMID16104727](https://pmc.ncbi.nlm.nih.gov/articles/PMC2536522/),
reaction-reconstitution text, reports carrier-adduct cleavage and recycling,
while the charging experiment used crude lysate with an unidentified sulfur
source. [Voss et al. 2011](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0028170),
electrospray-mass-spectrometry results and Discussion, supports MoeZR-dependent
CysO thiocarboxylation while leaving the physiological donor unresolved. Its
separate thiosulfate:cyanide assay does not establish free sulfide as the
carrier-charging substrate.

**CysK2 is not an OAS branch.** [Steiner et al. 2014, PMID25022854](https://pmc.ncbi.nlm.nih.gov/articles/PMC4187678/),
substrate experiments and first Discussion paragraph, shows lack of OAS
reaction, preferential use of OPS with thiosulfate to produce S-sulfocysteine,
and lower-efficiency sulfide-dependent cysteine production. CysK2 also does
not accept thiocarboxylated CysO. Conversely,
[O'Leary et al. 2008, PMID18842002](https://pubmed.ncbi.nlm.nih.gov/18842002/) and
[Agren et al. 2008, PMID18799456](https://pubmed.ncbi.nlm.nih.gov/18799456/)
support the OPS/CysO donor specificity of CysM. These findings justify
excluding the obsolete reaction, not substituting a new CysK2 route into an
unrelated source pathway.

**Direct CysE support.** [Qiu et al. 2013, PMID23483228](https://www.spandidos-publications.com/10.3892/ijmm.2013.1298?text=fulltext),
Results subsection on serine acetyltransferase activity, characterizes
recombinant H37Rv Rv2335 using serine and acetyl-CoA. A short exact excerpt
supports the CysE catalysis edge. No narrative-paper paraphrase is represented
as a structured `source_assertion`.

**GTP coupling belongs to APS synthesis.** [Sun et al. 2005, PMID15615729](https://pubmed.ncbi.nlm.nih.gov/15615729/),
Abstract and biochemical characterization, couples GTP hydrolysis to APS
synthesis at 1:1 stoichiometry. A single short excerpt is attached to the GTP
input edge. The other corrected endpoints use the structured FUNCTION
annotation of [UniProt P9WNM5](https://www.uniprot.org/uniprotkb/P9WNM5/entry),
preserving its `ECO:0000250` inference status. Original BioPAX endpoint
identities and placements remain visible in the edge ledger. The supporting
UniProt batch URL, hash, exact JSON indices, and comment objects are preserved
in the projection.

The same UniProt record's RHEA:18133 sulfurylase reaction consumes a hydron;
GTP hydrolysis produces one, so these cancel in the coupled APS-synthesis
description. RHEA:24152 APS kinase produces a hydron. The retained kinase edge
does not retain BioPAX's multiplicity of two. These qualitative graphs have
no stoichiometric coefficients and do not claim full elemental/charge
balance. The four endpoint corrections alone must not be interpreted as an
independently balanced reaction model.

**Sir evidence scope.** [Pinto et al. 2007, PMID17644602](https://pmc.ncbi.nlm.nih.gov/articles/PMC2045171/),
“SirA—the enzyme” and Figure 5, used purified *M. tuberculosis* SirA with
methyl viologen as the kinetic-assay donor. Deletion physiology was studied
in *M. smegmatis*. The maintained specific Fdx donor pairing is therefore
attributed to Reactome rather than to that direct assay.

**CysQ and transport evidence scope.** [Hatzios et al. 2008, PMID18454554](https://pubs.acs.org/doi/10.1021/bi702453s)
quantitatively characterizes PAP hydrolysis, with qualitative PAPS activity
because PAPS instability limited kinetic characterization. Reactome membrane
and oligomer context is retained as database context. [Wooff et al. 2002,
PMID11929522](https://pubmed.ncbi.nlm.nih.gov/11929522/) studies *M. bovis* BCG
mutants and complementation by *M. tuberculosis cysA*; those organisms are not
described as interchangeable direct physiological experiments.

**No blanket sulfate exclusivity.** [Wheeler et al. 2005, PMID15576367](https://www.sciencedirect.com/science/article/pii/S0021925819305782)
demonstrates methionine use as the sole sulfur source through reverse
transsulfuration in the *M. tuberculosis* complex. Accordingly, the source's
claims of exclusively sulfate-dependent sulfur uptake and universal enzyme
essentiality were not copied into the maintained description.

## Molecular identity and context

The curation retains native source protein states when BioPAX explicitly
describes features. In particular, CysO (`R-MTU-936619`), CysO-COSH
(`R-MTU-936718`), and CysO-cysteine adduct (`R-MTU-936690`) remain distinct;
their shared P9WP33 sequence reference is not an exact identity assertion for
all three states. The same applies to reduced/oxidized thioredoxin
(`R-MTU-936674` / `R-MTU-1222293`, sequence P9WG67), PLP-bearing CysM
(`R-MTU-936710`), and PLP-bearing CysK1 (`R-MTU-936587`). Mec's source fragment
spans residues 26–146 (`R-MTU-936660`); it is not replaced by a whole-sequence
UniProt identity. Complex composition and compartment assertions retain their
own source evidence.

The Fdx composition discrepancy requires a narrower decision than removing
every cluster edge:

| Native source edge | BioPAX component/stoichiometry | Decision |
|---|---|---|
| `R-MTU-937263 has_part CHEBI:33723` | Reduced `Complex2`, `SmallMolecule5`, `Stoichiometry6` coefficient 2 | Retain partial membership only, without coefficient. |
| `R-MTU-937267 has_part CHEBI:33722` | Oxidized `Complex3`, `SmallMolecule8`, `Stoichiometry10` coefficient 1 | Retain partial membership only. |
| `R-MTU-937267 has_part CHEBI:33723` | Oxidized `Complex3`, `SmallMolecule5`, `Stoichiometry11` coefficient 1 | Exclude the extra reduced [4Fe-4S] component. |

Both complexes contain Fdx Protein4/P9WNE7 at coefficient 1. [UniProt
P9WNE7](https://www.uniprot.org/uniprotkb/P9WNE7/entry), COFACTOR annotations,
lists one [4Fe-4S] cluster and one [3Fe-4S] cluster, each supported by similarity
(`ECO:0000250`). The graph's `has_part` relation does not claim complete
composition, so a single bounded [4Fe-4S] membership can remain. The source's
explicit two-[4Fe-4S] composition conflicts with that annotation; the extra
oxidized-complex component is excluded with that inference-level limitation
recorded. No charge state for a replacement [3Fe-4S] cluster is invented.

Chemical labels use the existing exact ChEBI identities. `CHEBI:33384` is
L-serine zwitterion; the source short label `Ser` was merely underspecified.
`CHEBI:48854` is neutral sulfurous acid, `CHEBI:15138` is sulfide(2-), and
`CHEBI:15366` is acetic acid, despite the source's acetate-style display label.
These were not silently replaced by different protonation states. Both
compartment-specific sulfate instances (`R-ALL-427648` outside and
`R-ALL-174375` inside) remain native and distinct.

Older BioPAX sequence references sometimes use species-level organism labels,
while P9 accessions often name H37Rv. No strain transfer correction was inferred
from this historical label difference alone. The records retain the source
species-level scope; identifier authority validation is a separate gate.

The seven added `provides_input_for` edges require both an explicit BioPAX
`PathwayStep/nextStep` ordering and matching produced/consumed physical
entities. Each has both locators. Shared ATP, water, or cofactor pools alone
never establish a causal link. No additional CysQ cycle/order was inferred
when the source lacked that pathway-order assertion. Excluded-reaction
context is pruned by following composition/location outward from accepted
reactions, preventing shared cytosol nodes from retaining excluded enzymes.

## Source provenance and access limits

The full manifest fields, URLs, byte lengths, hashes, retrieval timestamps,
and release identifiers are in the source projection. Official BioPAX
payloads use Reactome's CC0-1.0 terms; the UniProt projection uses CC-BY-4.0.

| Official release-97 export | SHA256 |
|---|---|
| [936654](https://reactome.org/ReactomeRESTfulAPI/RESTfulWS/biopaxExporter/Level3/936654) | `81265e1ab996bdf4c4126a380f285189dd7cd41e6e68e228fa56d2d09c40ff56` |
| [936721](https://reactome.org/ReactomeRESTfulAPI/RESTfulWS/biopaxExporter/Level3/936721) | `810756282671ad39c8be2ddf04e500fb53b33fe6a5f5ad51ecb955b263efe5e4` |
| [936635](https://reactome.org/ReactomeRESTfulAPI/RESTfulWS/biopaxExporter/Level3/936635) | `3064b8669aaddd154b89541727131af9f24bdc1980c9bc737c3e56d4533d0b71` |

The UniProt batch SHA256 is
`9d5fc21a10f70ef21cf95ffb126f8e850f11441b59f377c0311d11cd3012ab54`;
retrieval was 2026-10-07, with no release exposed by the response. The
successful CysE publisher HTML retrieval had SHA256
`97e00c0aec96dd72808582420e5c68f8227c47df88a94564291c901f5bc74c02`.
Primary-paper text was inspected through publisher, PMC, or PubMed web
extraction. Several direct local PMC/PubMed downloads returned access
challenges and Europe PMC XML requests returned HTTP 503. Those responses
are not article artifacts and their hashes are not used as article evidence.
Only the bounded successful CysE payload is assigned an article hash here;
the scientific citations do not imply archival possession of every paper.
