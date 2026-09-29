# Current open-source ingest triage

Updated: 2026-09-29

This note records the terminal sweep of the currently enabled open pathway
sources after the first GO-CAM and WikiPathways records were ingested into
PathwayMech. The goal was to find another hand-reviewable record whose
pathway identifier, pathway elements, and mechanistic edges are all grounded in
prefixes accepted by the local schema.

The sweep covered:

- the cached SGD GO-CAM JSON models under `/private/tmp/sgd-yeast-gocams`
- the September 10, 2026 WikiPathways GPML archives cached as
  `/private/tmp/wikipathways-20260910-gpml-*.zip` for Acetobacterium woodii,
  Bacillus subtilis, Caulobacter vibrioides, Escherichia coli, Gibberella
  zeae, Mycobacterium tuberculosis, Plasmodium falciparum, and Saccharomyces
  cerevisiae

GPML candidates were converted through `src/pathwaymech/wikipathways.py` and
inspected with `/private/tmp/inspect_wikipathways_gpml.py`, so rejected
records reflect the same local Xref whitelist used by the production importer.
SGD GO-CAM candidates were scored with `/private/tmp/score_gocam_candidates.py`
for duplicate labels, broad superpathways, missing nodes, unlabeled ChEBI
nodes, and generic placeholders before the least-bad models were inspected
manually.

## Result

No additional record in those caches is commit-ready under the current
`PathwayRecord` schema.

The current useful remainder falls into four buckets:

1. exact duplicates of already curated records
2. superpathways or overview maps that mix several curated routes
3. protein, transcription, signaling, or cell-cycle diagrams rather than
   biochemical pathways
4. reaction maps whose defining compounds or genes are not grounded in an
   accepted prefix

Do not re-attempt the rejected GPML and SGD GO-CAM rows below unless the schema
or import layer gains a new identifier mapping step.

## WikiPathways state

The following WikiPathways records are already represented exactly:

- `WikiPathways:WP71` - phospholipids degradation
- `WikiPathways:WP171` - NAD salvage pathway V
- `WikiPathways:WP178` - isoleucine degradation
- `WikiPathways:WP266` - triglyceride biosynthesis
- `WikiPathways:WP287` - ubiquinol-6 biosynthesis from 4-hydroxybenzoate
- `WikiPathways:WP296` - TCA cycle - detailed
- `WikiPathways:WP392` - glutathione-glutaredoxin redox reaction
- `WikiPathways:WP478` - glycogen catabolism
- `WikiPathways:WP556` - glutamate degradation I
- `WikiPathways:WP5019` - acetogenesis
- `WikiPathways:WP5060` - peptidoglycan cytoplasmic synthesis and recycling
  pathways
- `WikiPathways:WP5587` - 2-phenylethanol biosynthesis

The low-edge Escherichia coli Pathway Tools maps are no longer blocked by
HMDB, CAS, PubChem, or Ensembl prefix support. After native GPML xref support,
`WP2484` imports as a 33-edge NAD de novo draft but duplicates the curated
MetaCyc/Rhea `PYRIDNUCSYN-PWY` record; `WP2486` and `WP2488` overlap existing
NAD salvage curation; and `WP2487` and `WP2886` are still weak Pathway Tools
exports rather than better evidence sources. `WP3538` is a cell-division
protein-state map, `WP3641` still overlaps peptidoglycan and
UDP-<i>N</i>-acetylglucosamine records while failing strict validation through
unresolved chained GPML anchors, and `WP3583`, `WP5070`, and `WP2472` remain
broad central-carbon, Salmonella regulatory, and E. coli K-12 peripherome
diagrams rather than bounded pathway definitions.

The Mycobacterium and Plasmodium maps are also richer after KEGG, PubChem,
ChemSpider, TubercuList, Entrez, and NCBI Protein support, but they are not
commit-ready. `WP1567`, `WP2563`, `WP2566`, and `WP2638` are KEGG-style
overview maps that mix glycolysis/gluconeogenesis, the TCA cycle, glyoxylate
cycle, and GAS branches. `WP1581`, `WP1622`, `WP1631`, `WP1642`, `WP1652`, and
`WP1667` need source-specific review before their KEGG/TubercuList projections
can be split into bounded records. `WP4198` now preserves PubChem and Entrez
nodes but still lacks catalyst edges for a reviewable mycolic-acid pathway.
`WP2918` imports as a 31-edge apicoplast isoprenoid draft, but it also includes
inhibitor and transporter diagram lines that the GPML importer cannot yet
separate from biochemical conversions. `WP2564` is a sigma-factor transcription
map, not a biochemical pathway.

The remaining Bacillus, Caulobacter, and Gibberella GPML files are blocked for
similar reasons. `WP1466` is a response-regulator protein interaction diagram,
`WP2360` overlaps existing folate and tetrahydrofolate curation, `WP5271` now
preserves the ceramide lipids but still needs lipid normalization to produce a
reviewable biochemical graph, and `WP2258` preserves the DON mycotoxin
chemistry but still fails strict validation through an unresolved GPML anchor.

Saccharomyces cerevisiae has the largest GPML set, but after the exact
WikiPathways records above it divides into curation-blocking buckets. These are
first blockers rather than mutually exclusive claims: several overview maps
also contain unsupported compounds, and several unsupported maps are also near
duplicates.

- already covered by exact or near-exact records:
  `WP2`, `WP67`, `WP84`, `WP91`, `WP128`, `WP1518`, `WP165`, `WP180`,
  `WP194`, `WP196`, `WP214`, `WP224`, `WP250`, `WP287`, `WP345`, `WP354`,
  `WP379`, `WP381`, `WP432`, `WP459`, `WP479`, `WP514`, `WP538`, and `WP555`
- broader duplicates of existing routes:
  `WP7`, `WP9`, `WP27`, `WP92`, `WP95`, `WP102`, `WP112`, `WP156`, `WP191`,
  `WP198`, `WP203`, `WP218`, `WP220`, `WP253`, `WP290`, `WP321`, `WP331`,
  `WP398`, `WP416`, `WP4173`, `WP423`, `WP462`, `WP472`, `WP490`, `WP515`,
  `WP5201`, and `WP5354`
- unsupported or misleading chemistry:
  `WP14`, `WP36`, `WP46`, `WP54`, `WP70`, `WP109`, `WP121`, `WP132`, `WP137`,
  `WP159`, `WP256`, `WP257`, `WP260`, `WP261`, `WP275`, `WP301`, `WP328`,
  `WP332`, `WP369`, `WP370`, `WP380`, `WP440`, `WP452`, `WP463`, `WP503`,
  `WP533`, `WP541`, `WP546`, `WP563`, `WP573`, `WP579`, and `WP4162`
- non-pathway or protein/regulatory maps:
  `WP13`, `WP32`, `WP62`, `WP158`, `WP210`, `WP219`, `WP346`, `WP377`,
  `WP414`, `WP425`, `WP510`, `WP2838`, `WP2869`, and `WP3636`

## SGD GO-CAM state

The current SGD GO-CAM cache has also been drained of low-risk records.

Exact or near-exact duplicates include cysteine, homoserine, threonine,
glutathione, allantoin, serine, sulfate assimilation, riboflavin, triglyceride,
glutathione-glutaredoxin, tryptophan degradation, and p-aminobenzoate routes
that are already covered by existing MetaCyc, WikiPathways, or earlier GO-CAM
records.

Superpathway GO-CAMs should stay out of `data/pathways/` because PathwayMech
stores one bounded route per YAML. The rejected superpathways cover aromatic
amino acids, branched-chain amino acids, glucose fermentation, polyamine
biosynthesis, histidine/purine/pyrimidine biosynthesis, threonine/methionine
biosynthesis, sulfur amino acid biosynthesis, glutathione metabolism,
glutamate biosynthesis, fatty acid biosynthesis, phosphatidate biosynthesis,
phospholipid biosynthesis, ubiquinone biosynthesis, and heme/siroheme
biosynthesis.

The remaining narrow-looking GO-CAMs are blocked by placeholders or by
ambiguous chemistry:

- `YeastPathways_PWY-5084` - generic oxoglutarate decarboxylation
  sub-reactions
- `YeastPathways_PWY-5177` - omits the defining glutaryl-CoA steps
- `YeastPathways_PWY-6482-1` - begins with generic `CHEBI:24431` protein
  complex activity and an unlabeled `CHEBI:80681`
- `YeastPathways_PWY3O-20` - duplicates folate interconversions and uses a
  cyclic dihydrofolate/polyglutamate representation rather than a single
  bounded route
- `YeastPathways_GLUCOSE-MANNOSYL-CHITO-DOLICHOL` - contains unlabeled
  oligosaccharide ChEBI nodes and `CHEBI:24431`

## Revisited unlocks

The first harmonization blockers have landed in the importer layer:

- Native LIPIDMAPS support preserves lipids that have no checked ChEBI mapping.
- Local ChEBI OBO xrefs can normalize KEGG Compound, HMDB, CAS, ChemSpider, and
  PubChem GPML chemistry to ChEBI when an exact xref exists.
- Ensembl, Entrez, TubercuList, and NCBI Protein GPML nodes can be preserved as
  native gene or protein participants.
- MIBiG JSON can emit draft records with `gene_clusters` for BGC accessions,
  products, biosynthetic classes, local genes, GenBank loci, taxa, and PubMed
  references.

These unlocks make the formerly empty or catalyst-only GPML candidates
inspectable, but they do not by themselves make any rejected record
commit-ready. Candidate absence and duplicate checks used `rg --no-ignore
--hidden` before new records were written. Further GPML curation should now
focus on narrower maps with native chemistry that can be normalized to ChEBI
and Rhea, or on improving MIM inhibition and chained-anchor handling before
revisiting `WP2918` and `WP3641`.
