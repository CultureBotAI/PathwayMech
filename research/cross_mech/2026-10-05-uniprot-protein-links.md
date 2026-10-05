# Cross-Mech UniProt Proteins and PathwayMech Links

Checked: 2026-10-05.

## Scope and decision

Which UniProtKB proteins do the sibling Mechs hold? How do those proteins
relate to PathwayMech pathways? Do the sibling records link back to PathwayMech?
Where could PathwayMech proteins serve as sibling examples?

This note records what was measured and what each sibling allows. It ends
with the follow-up it supports. Nothing here edits a sibling repository or
adds a PathwayMech pathway record. Those changes need their own pull requests
in each repository, under that repository's rules.

Sibling checkouts read (working trees on their default branch unless noted):

| Mech | Commit |
|---|---|
| TraitMech | `9dea24521a32e92c3425449321fc36b1dbc621f1` |
| ProteinTraitsMech | `316a8005e69bb3f2ee5d53bb0c6bd41beb018421` (checkout on branch `cross-mech-protein-ledger`, same commit as `origin/main`, only an untracked script added) |
| NaturalProductMech | `aa0e38c4ac899ca5534b4ce02318c019fc44db29` |
| AntibioticMech | `f1604be2ab31232faf63ad6a9bc4b1441af0ac1d` |
| CellStructureMech | `6f9c21f864a0ec71523dda358491e96263934d21` |
| PathwayMech | `d8ec2b69f7a4c615aecddff80498fef1e1fab0ce` |

TaxonMech, DUFMech, MediaIngredientMech, CommunityMech, CultureMech and
HabitatMech hold no curated UniProtKB protein. Each was checked with an
ignore-independent `grep -r`. DUFMech's accessions appear only as InterPro
description text in its worklists. MediaIngredientMech's appear only in
literature notes under `research/`. CommunityMech and HabitatMech do model
pathway-level processes, so they appear in the gap ranking below. No PathwayMech record links were detected on the configured record surfaces
of the five inventoried siblings at the listed revisions. This is not an
assertion about every file or every Mech repository.

## Method

```bash
uv run python research/cross_mech/2026-10-05/reproduce.py \
  --mechs-root <dir holding the Mech checkouts>
```

This reads the exact sibling commits listed above using git objects, even if
the checkouts have since moved. It uses the committed SGD/UniProt inputs and
Rhea quartet projection.

The `just cross-mech-proteins` command reads the protein slots listed in
`conf/sibling_mechs.yaml`, and only those. Each slot's meaning was read from that
Mech's LinkML schema and validators. An accession cited as evidence or named in
prose does not count.

PathwayMech names proteins in two ways. There are 47 UniProtKB participants in 5
records. There are also 338 SGD gene ids in 90 records. The SGD ids map to 330
reviewed S. cerevisiae S288C UniProtKB entries through UniProtKB's own SGD
cross-references (`inputs/sgd_uniprot.json`, queried anonymously). The other 8
SGD ids are Complex Portal complexes with no single accession: S000217821,
S000217863, S000217933, S000217934, S000218025, S000218096, S000218158 and
S000218211. Together PathwayMech names 377 UniProtKB proteins.

`inputs/uniprot_annotations.json` holds UniProtKB Rhea, EC and pathway
annotations for 1,338 sibling and PathwayMech accessions. It lets a sibling
protein match a pathway by reaction even when the pathway record states no
Rhea reaction. That is the case for the 86 GO-CAM yeast records.

## Results

| Mech | Protein slot values | Distinct accessions | In a PathwayMech pathway | Record-pathway pairs |
|---|---:|---:|---:|---:|
| TraitMech | 143 | 112 | 0 | 0 |
| ProteinTraitsMech (records naming a PathwayMech protein) | 10,056 | 3,256 | 351 | 2,468 |
| NaturalProductMech | 1,093 | 445 | 1 | 1 |
| AntibioticMech | 278 | 88 | 0 | 0 |
| CellStructureMech | 413 | 329 | 0 | 0 |

For ProteinTraitsMech, only records whose text names one of the 377 PathwayMech
accessions were parsed, out of 429,293 trait records. Its 351 shared proteins
appear as canonical examples on 1,879 distinct trait records, yielding 2,468
record–pathway pairs. Most of those records are
domain, family and structure traits, which should not link to a pathway.

`pairs.tsv` lists every record and pathway sharing a protein.
`reaction_matches.tsv` lists protein-slot–pathway matches that share a Rhea
chemical transformation or a complete EC number. A slot can match multiple
pathways, so its row count is not a count of distinct slots. The original
237 rows represented 202 slots and 117 record–pathway pairs; the corrected
Rhea normalization and retaining chemistry leads for other records even when
a protein directly overlaps one record yield 854 rows: 587 distinct slots
and 640 record–pathway pairs. Of these, 323 use `record_rhea`.
They remain unreviewed curation leads, including known rejected examples. `example_candidates.tsv` lists PathwayMech
proteins of overlapping pathways that a sibling does not hold.
`proteintraitsmech_pathway_trait_links.tsv` gives the exact
ProteinTraitsMech joins described below. `link_checks.tsv` is empty: no sibling
links PathwayMech yet.

## Pathways PathwayMech already has

These correspondences survived review of the leads. Each needs the relation
and evidence that the sibling's own rules require before it is written there.

### ProteinTraitsMech

There are 73 exact cross-reference joins (not assertions of pathway equivalence): 67 GO biological-process traits carry a MetaCyc
xref equal to a PathwayMech record id. The xref matches either a `MetaCyc:` id
directly, or the frame inside `gomodel:YeastPathways_<frame>`. In 30 pairs,
PathwayMech names proteins that are not yet examples of the trait. In 14
pairs (12 distinct traits), the trait has no microbial example at all, only human, mouse, plant,
fly or worm proteins. Examples:

- removal of superoxide radicals (GO:0019430) ↔ superoxide radicals degradation
- zymosterol biosynthetic process (GO:0036197) ↔ zymosterol biosynthesis
- very long-chain fatty acid biosynthetic process (GO:0042761) ↔ very long
  chain fatty acid biosynthesis I
- farnesyl diphosphate biosynthetic process (GO:0045337) ↔ trans,
  trans-farnesyl diphosphate biosynthesis

All 179 PathwayMech EC numbers exist as ProteinTraitsMech EC trait records.
183 of PathwayMech's 382 Rhea ids are ProteinTraitsMech Rhea master records.

### NaturalProductMech

- linearmycin A, B and C ↔ `MIBiG:BGC0002072`, joined on the same MIBiG
  accession
- ectoine ↔ `MetaCyc:P101-PWY`, joined because the pathway's terminal product
  CHEBI:58515 has the record's InChIKey
- feglymycin's target MurA (P0A749) is a participant of `WikiPathways:WP5060`
- citrulline ↔ the yeast `gomodel:YeastPathways_CITRUL-BIO2-PWY` is weak, since
  the producer taxa differ

### AntibioticMech

- **Peptidoglycan synthesis** (`WikiPathways:WP5060`): fosfomycin (MurA),
  D-cycloserine (Alr/Ddl), β-lactams (PBPs), bacitracin, teixobactin and the
  glycopeptides.
- **Ergosterol synthesis**:
  - azole CYP51/ERG11 determinants (fluconazole, itraconazole, voriconazole,
    posaconazole, difenoconazole, prochloraz, pyrifenox, triflumizole) →
    `gomodel:YeastPathways_PWY-6074-1`
  - ERG3 alleles → `gomodel:YeastPathways_PWY-6075-1`
  - terbinafine's squalene epoxidase → `gomodel:YeastPathways_PWY-5670-1`
  - 53 of 55 ERGOSTEROL_PATHWAY_INHIBITION records carry no target at all
- **Succinate dehydrogenase** (`WikiPathways:WP296`): carboxin determinants.
- **Folate** (`gomodel:YeastPathways_PWY-6614`, `PWY3O-697`): DHFR targets of
  trimethoprim. These are bacterial, so a yeast pathway link overclaims unless
  it is marked as a related, different-organism pathway.

### CellStructureMech

- glycine cleavage complex ↔ glycine cleavage
- peroxisome and peroxisomal matrix ↔ fatty acid oxidation pathway (yeast)
- chitosome ↔ chitin biosynthesis
- peptidoglycan cell wall, divisome and elongasome ↔ `WikiPathways:WP5060`
- lipid droplet ↔ triglyceride biosynthesis
- succinate dehydrogenase complex II ↔ TCA cycle
- cytoophidium (CTP synthase filaments) ↔ UTP and CTP de novo biosynthesis

### TraitMech

The links are causal-graph nodes to records:

- glyoxylate cycle ↔ `MetaCyc:GLYOXYLATE-BYPASS`
- TCA cycle ↔ `WikiPathways:WP296`
- glycolysis ↔ `gomodel:YeastPathways_GLYCOLYSIS`
- pentose phosphate ↔ `MetaCyc:OXIDATIVEPENT-PWY` and `MetaCyc:NONOXIPENT-PWY`
- AckA-Pta ↔ `MetaCyc:PWY0-1312`
- carbamate kinase (arginine deiminase route) ↔ `MetaCyc:ARGDEGRAD-PWY`
- Wood-Ljungdahl nodes in five traits ↔ `WikiPathways:WP5019`
- ectoine nodes ↔ `MetaCyc:P101-PWY`
- proline ↔ `MetaCyc:PROSYN-PWY`
- trehalose ↔ `MetaCyc:TRESYN-PWY`
- shikimate ↔ `MetaCyc:ARO-PWY`
- mevalonate ↔ `gomodel:YeastPathways_IPPSYN-PWY`
- heme ↔ `gomodel:YeastPathways_HEME-BIOSYNTHESIS-II`
- peptidoglycan nodes in four shape traits ↔ `WikiPathways:WP5060`

Do not link these look-alikes:

- urease activity ↔ urea degradation I, which is yeast urea amidolyase, not
  urease
- dissimilatory ↔ assimilatory sulfate reduction
- brown-pigment tyrosine catabolism ↔ the yeast Ehrlich tyrosine degradation
- methanotroph formaldehyde assimilation ↔ glutathione-dependent formaldehyde
  oxidation

## Pathways PathwayMech lacks

These are ranked by sibling demand. Each MetaCyc 22.5 frame was confirmed on
the SGD Pathway Tools mirror that PathwayMech already uses for MetaCyc
identity (HTTP 200 with the name shown; an unknown frame returns 404).

| Rank | Pathway (MetaCyc frame) | Sibling demand |
|---:|---|---|
| 1 | Calvin-Benson-Bassham cycle (`CALVIN-PWY`) | RbcL examples on 8 TraitMech traits (CBB cycle, carbon fixation, autotrophic and four chemo/photo-autotrophy traits); CellStructureMech carboxysome and shell; CommunityMech carbon-fixation records |
| 2 | methanogenesis from H2 and CO2 (`METHANOGENESIS-PWY`) | TraitMech methanogenesis and anaerobic oxidation of methane (McrA); CellStructureMech methyl-coenzyme M reductase; CommunityMech and HabitatMech methanogenesis |
| 3 | nitrogen fixation I (ferredoxin) (`N2FIX-PWY`) | TraitMech nitrogen fixation and nitrogen-fixing symbiosis (NifH); CellStructureMech nitrogenase; CommunityMech |
| 4 | nitrate reduction I (denitrification) (`DENITRIFICATION-PWY`) | TraitMech denitrification and anaerobic respiration (NosZ); CommunityMech |
| 5 | dissimilatory sulfate reduction I (`DISSULFRED-PWY`) | TraitMech dissimilatory sulfate reduction and cable-bacteria metabolism (DsrAB); CommunityMech |
| 6 | bacterial type II fatty acid synthesis (`FASYN-ELONG-PWY`, `PWY-6282`) | TraitMech homeoviscous adaptation (FabB, FabI); AntibioticMech triclosan (FabI) and α-mangostin (FabZ); NaturalProductMech emodin target (FabZ) |
| 7 | (S)-propane-1,2-diol degradation (`PWY-7013`) and ethanolamine utilization (`PWY0-1477`) | CellStructureMech Pdu and Eut microcompartments (13 shell proteins) |
| 8 | urea degradation II (`PWY-5704`) | TraitMech urease activity (UreA, UreB, UreC) |
| 9 | methylerythritol phosphate pathway I (`NONMEVIPP-PWY`) | CellStructureMech Dxr complex; AntibioticMech fosmidomycin (DXR) |
| 10 | 1,3-β-D-glucan biosynthesis (`PWY-6773`) | AntibioticMech echinocandins (FKS1); CellStructureMech glucan synthase complex |
| 11 | superpathway of mycolate biosynthesis (`PWY-6113`) | AntibioticMech isoniazid (InhA, KasA) |
| 12 | fermentations: lactate (`PWY-5481`), mixed acid (`FERMENTATION-PWY`), propanoate (`P108-PWY`), ethanol (`PWY-5486`) | TraitMech lactic, mixed-acid, propionic and ethanol fermentation traits; CellStructureMech formate hydrogenlyase |
| 13 | polyhydroxybutanoate biosynthesis (`PWY1-3`) | TraitMech PHA granule (PhaC); CellStructureMech PHA granule |
| 14 | ammonia oxidation I (`AMMOXID-PWY`) and methane oxidation to methanol I (`PWY-1641`) | TraitMech chemolithotrophy and nitrification traits (AmoA) and methanotrophy (pMMO) |
| 15 | phenylacetate degradation I (aerobic) (`PWY0-321`) | CellStructureMech PaaABCE complex |
| 16 | carbon-fixation cycles: reductive TCA (`P23-PWY`), 3-hydroxypropanoate (`PWY-5743`), 3-hydroxypropanoate/4-hydroxybutanoate (`PWY-5789`) | one TraitMech trait each |
| 17 | enterobactin biosynthesis (`ENTBACSYN-PWY`) | NaturalProductMech siderophores; TraitMech siderophore production |

NaturalProductMech also curates biosynthesis for 175 compounds on 191 MIBiG
clusters. PathwayMech covers one of those clusters. The existing MIBiG
importer is the route for those, rather than MetaCyc.

## Example candidates

- **AntibioticMech:** E. coli MurA (UniProtKB:P0A749, a `WikiPathways:WP5060`
  participant) on fosfomycin's curator-owned MurA target. That target cites a
  fosfomycin cocrystal paper and has no protein example.
- **CellStructureMech:** FtsW (P0ABG4) and FtsI (P0AD68), both `WP5060`
  participants, on the divisome's septal peptidoglycan synthase component. That
  component has no example. It needs one example per subunit, with membership
  evidence such as UniProt localisation PMIDs. Pathway membership is not
  evidence. Yeast Ura7 and Ura8 on the cytoophidium, and yeast Gcv1, Gcv2 and
  Lpd1 on the glycine cleavage complex, would first need S. cerevisiae added to
  those records' taxa. That is a curation decision.
- **TraitMech:** the catalase activity trait has a monofunctional heme catalase
  node (InterPro:IPR018028) with no protein example; only the PerR regulator
  has one. Yeast catalase T (Ctt1, P06115) from
  `gomodel:YeastPathways_DETOX1-PWY` would fill it. Yeast pyruvate decarboxylase
  Pdc1 (P06169) and alcohol dehydrogenase Adh1 (P00330) suit the ethanol
  fermentation trait. Each needs a primary paper with a verbatim snippet and
  the UniProt strain taxon.
- **ProteinTraitsMech:** the 30 trait-pathway pairs above where PathwayMech names
  proteins that are not yet examples. They are candidates for that repository's
  release-pinned grounding workflow. They cannot be hand-added, and no
  evidence provider qualifies GO-BP or EC examples there today.
- **NaturalProductMech:** none that fit. The compounds whose targets are
  PathwayMech proteins (fosfomycin, cycloserine, tunicamycin) have
  AntibioticMech records, where their targets belong. The 34
  `example_candidates.tsv` rows for NaturalProductMech are therefore rejected.

## Rejected leads and data issues

The rejected reaction-level leads fall into four groups:

- mammalian bioactivity targets matched to yeast pathways, such as human
  glutathione peroxidases on ochratoxin A, antimycin A and beauvericin;
- side activities, such as RebD catalase activity and promiscuous homocitrate
  synthase annotation;
- partial EC classes;
- a fungal nucleoside diphosphate kinase on the hydrogen peroxide record.

Data issues found:

- `WikiPathways:WP5060` names MrdA as UniProtKB:Q2TL65, an unreviewed
  species-level E. coli entry. The reviewed K-12 entry is P0AD65, which
  CellStructureMech uses. This is a reconciliation candidate, not an established
  error: an unreviewed species-level entry is not inherently invalid.
- AntibioticMech nevirapine lists UniProtKB:P06633 (S. cerevisiae
  imidazoleglycerol-phosphate dehydratase, His3) as a target example labelled
  HIV-1. This is a BindingDB artifact. It is the only route by which nevirapine
  matched `MetaCyc:HISTSYN-PWY`.
- Four distinct accessions were unresolved by the audit lookup in six
  AntibioticMech BindingDB target-example slots (a failed lookup alone does
  not establish deletion): Q9WJQ1 on etravirine and nevirapine, R4ML78 on mafenide
  and sulfanilamide, A0A045J7I4 on sulfanilamide, and A0A0E3A638 on α-mangostin.
  The 99 unresolved historical accessions in TraitMech occur only in curation-history text,
  and the one in NaturalProductMech (P24247, formycin A) only in notes.

## Gaps

1. **New PathwayMech records are blocked by the identifier gate's snapshot
   refresh.**
   - `scripts/build_source_identifier_snapshot.py` rebuilds all 71 manifest
     sources at once. The original session did not locate a complete cache.
   - The Reactome BioPAX exporter failed during the original audit; the GO-CAM tarball is a
     moving file.
   - The ontology snapshot needs pinned ChEBI 255, GO 2026-07-26 and Rhea 139
     databases. The local ChEBI and GO databases are different releases, and no
     matching Rhea database was found in that session.
   - The user chose to wait for a complete refresh of all 71 sources. No
     partial-refresh implementation or identifier-gate exception is included.
2. **At the audit baseline, only NaturalProductMech had a cross-corpus link slot.**
   - NaturalProductMech's `related_records` is computed by its seeder from a
     pinned sibling inventory and must not be hand-edited.
   - TraitMech, AntibioticMech and CellStructureMech need a schema change. The
     fleet precedent is NaturalProductMech's `CrossCorpusLink`.
   - ProteinTraitsMech can use `trait_relations` through a registered editor,
     on records not bound by grounding receipts.
   - A shared shape would belong in claw's `mech_shared.yaml`.
3. **Concurrent work.**
   - A ProteinTraitsMech session is building a cross-Mech protein ledger on
     branch `cross-mech-protein-ledger`.
   - A DUFMech session has an uncommitted cross-Mech scanner.
   - Their sibling readers and this inventory should agree on slot channels.

Sibling checks can verify a PathwayMech link against
`pages/pathway_index.json`, published with the PathwayMech pages from this
change on. It lists each record's id, label, page, taxa, protein participants
and reactions.

## Review corrections and remaining work

Rhea reactions are grouped using the independently downloaded upstream
`rhea-directions.tsv`, projected into `conf/rhea_directions.json` with the
complete input SHA-256 and retrieval timestamp. Directional and master IDs
can now join on their common chemical transformation; this does not assert
a physiological reaction direction. See the [Rhea direction contract](https://www.rhea-db.org/help/reaction-side-direction).

ProteinTraitsMech remains a prefiltered inventory: its counts are lower
bounds for the whole corpus, and annotation coverage is separate from parsed
record coverage. No sibling link asserts equivalence solely from a shared
protein, EC number, or MetaCyc cross-reference. In particular, antibacterial
DHFR claims and antifungal target claims may concern different organisms from
the linked yeast pathway and must retain that qualification.

The selected continuation is a governed CrossCorpusLink class in claw, fleet
repins, and local changes in AntibioticMech, TraitMech, CellStructureMech, and
NaturalProductMech. ProteinTraitsMech domain changes stay with its concurrent
session. The user selected a full authority refresh before new PathwayMech
records; the 17 ranked gaps remain deferred.
