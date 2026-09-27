# Current open-source ingest triage

Updated: 2026-09-27

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

The low-edge Escherichia coli Pathway Tools maps are not usable with the
current prefix set. `WP2484`, `WP2486`, `WP2487`, `WP2488`, and `WP2886`
collapse to HMDB, CAS, PubChem, and Ensembl nodes. `WP3538` is a cell-division
protein-state map, `WP3641` overlaps peptidoglycan and
UDP-<i>N</i>-acetylglucosamine records while depending on Ensembl and
Wikidata nodes, and `WP3583`, `WP5070`, and `WP2472` are broad
central-carbon, Salmonella regulatory, and E. coli K-12 peripherome diagrams
rather than bounded pathway definitions.

The Mycobacterium and Plasmodium maps are mostly KEGG or TubercuList exports.
`WP1567`, `WP1581`, `WP1622`, `WP1631`, `WP1642`, `WP1652`, `WP1667`, `WP2563`,
`WP2566`, `WP2638`, and `WP2918` currently reduce to catalyst-only stubs or
ChemSpider-only compound lists. `WP4198` keeps a few UniProtKB and mycolic acid
nodes but loses the PubChem/Entrez/Pks13 chemistry needed to represent mycolic
acid biosynthesis. `WP2564` is a sigma-factor transcription map, not a
biochemical pathway.

The remaining Bacillus, Caulobacter, and Gibberella GPML files are blocked for
similar reasons. `WP1466` is a response-regulator protein interaction diagram,
`WP2360` overlaps existing folate and tetrahydrofolate curation while using
HMDB and KEGG compounds, `WP5271` depends on unsupported lipid identifiers, and
`WP2258` loses the DON mycotoxin chemistry needed to make the record
meaningful.

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

## Unlocks

The next likely pathway records need harmonization rather than more manual
triage:

- LIPID MAPS to ChEBI or native LIPID MAPS support would reopen bacterial
  ceramide, ergosterol, sphingolipid, and fatty-acid candidates.
- KEGG Compound to ChEBI mapping would reopen most Mycobacterium and
  Plasmodium GPML maps.
- HMDB, CAS, ChemSpider, PubChem, Ensembl, Entrez, TubercuList, and NCBI
  Protein mappings would be needed before the E. coli Pathway Tools GPML
  exports can produce anything beyond empty or catalyst-only graphs.
- BGC-shaped fields are still needed before MIBiG can be more than a source of
  seed rows for secondary-metabolite clusters.

Candidate absence and duplicate checks used `rg --no-ignore --hidden` before
new records were written. No further GO-CAM or WikiPathways pathway from the
current caches should be curated until one of the unlocks above lands.
