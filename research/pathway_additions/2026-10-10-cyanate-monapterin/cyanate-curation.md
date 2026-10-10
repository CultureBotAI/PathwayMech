# Cyanate degradation curation — 2026-10-10

Record: `data/pathways/cyanate-degradation.yaml`, `MetaCyc:CYANCAT-PWY`, **cyanate degradation**. This is the explicit CynS/CynT bicarbonate-recycling pathway, bounded to the native MG1655 annotation. The raw comparison lead was PathBank `SMP0002111`, archive member `PW002099.owl`. It is not the net cyanase reaction alone.

## Novelty and identity

Fresh `rg -uu` searches included hidden and ignored files in both the original PathwayMech checkout and this worktree; only `.git`, `.venv`, and `__pycache__` implementation directories were excluded. Exact pathway/reaction/protein/paper identifiers, labels and synonyms were checked before drafting. The two initial scans each returned 130 matching lines; expanded scans returned 21 in the worktree and 3 in the original. Current root authority acquisitions explain additional expanded worktree matches. Commands, output digests, matching files, and bounds are in `cyanate-duplicate-searches.json`.

Prior committed triage was read and its unresolved chemistry/assembly questions addressed. No maintained record denotes this complete recycling route. Existing arginine degradation V shares spontaneous carbamate decomposition (`RHEA:15650`), not the full cyanate mechanism. Earlier inventory/screening references and the Pseudomonas same-label source are discovery context. `GO:0009440` is generic cyanate catabolism; `MetaCyc:CYANCAT-PWY` more exactly defines the three-step cycle represented here.

## Explicit chemistry

All reaction sides come from full pinned Rhea RDF release 142, independently bridged through the full native MetaCyc reaction objects:

| Graph reaction | Native MetaCyc reaction | Selected conversion |
| --- | --- | --- |
| RHEA:18490 | R524-RXN | cyanate + bicarbonate + H+ → carbamate + CO2 |
| RHEA:15650 | RXN0-5222 | carbamate + 2 H+ → ammonium + CO2 |
| RHEA:10750 | RXN0-5224 | CO2 + water → bicarbonate + H+ |

The 13 chemical side occurrences preserve exact `rh:containsN` coefficients and participant URIs. Each equation independently balances atoms and charge. Carbamate is the anion `CHEBI:13941`; neutral native PathBank carbamic acid `CHEBI:28616` is not silently treated as the same charged species. One pass through the three reactions sums to cyanate + 2 H+ + water → ammonium + CO2. This arithmetic is a consistency check, not a measured flux ratio or claim that every CO2 molecule is captured.

Current UniProt CynS uses the net master reaction `RHEA:11120`. Rhea explicitly describes 18489 and 15649 as parts of this net reaction. The graph therefore uses the explicit intermediate step and decay, without a redundant net `RHEA:11121` node. The isotope study [PMID:3110153](https://pubmed.ncbi.nlm.nih.gov/3110153/) distinguishes bicarbonate substrate use from activation and water-dependent hydrolysis; the omitted formula in its indexed abstract was not reconstructed as a quotation.

MetaCyc explicitly sets RXN0-5222 `spontaneous=true`, and Rhea independently states the reaction can occur spontaneously. These support the nonenzymatic step despite PathBank's contradictory `spontaneous=false`. There is no catalyst edge to this reaction. Draft adversarial review [issue #322](https://github.com/CultureBotAI/PathwayMech/issues/322) identified that a `molecular_activity` override would incorrectly imply gene-product activity. The optional override was removed; actual KGX must retain `biolink:BiochemicalReaction`. The two enzyme-mediated steps retain their supported activity categories.

RXN0-5224 is reversible; CYANCAT-PWY selects R2L hydration. Thus `RHEA:10750` has `direction: right_to_left`, without a claim of intrinsic irreversibility. Three native predecessor links define the cycle. An additional initial-step CO2 → hydration input link is explicitly labeled an inference from shared chemical input and the documented recycling role, not an extra native ordering assertion.

## Assemblies and scope

`MetaCyc:CYANLY-CPLX` is the native cyanase assembly. Its component coefficient is ten, and CYANLY-MONOMER explicitly unifies with reviewed `UniProtKB:P00816`. Reviewed annotation and the primary structure abstract [PMID:10801492](https://pubmed.ncbi.nlm.nih.gov/10801492/) support the functional homodecamer. Catalysis is assigned to the assembly, with CynS as its subunit.

`MetaCyc:CARBODEHYDRAT-CPLX` is the CynT-only assembly; its native monomer unifies with `UniProtKB:P0ABE9`. The complex coefficient two is qualified in the same source as “probably a dimer”; monomer commentary describes two or four subunits depending on bicarbonate. Current UniProt and the purification abstract [PMID:1740425](https://pubmed.ncbi.nlm.nih.gov/1740425/) support an oligomer. The graph preserves membership without asserting a universally fixed dimer. Zinc is supported at one ion per CynT subunit and attached to P0ABE9. Its cytoplasmic localization uses the explicit GO annotation and experimental evidence code, not a guessed location mapping.

PathBank's `ProteinComplex/1171` mixes CynT/P0ABE9 and Can/P61517. This assembly is rejected. MetaCyc's `enzymes-not-used` object CPLX0-7521 resolves through EG12319-MONOMER to P61517, rather than being identified by its display name alone. Can is a separate enzyme; its native tetramer/current UniProt dimer discrepancy is retained as context, not imported or silently resolved. Primary compensation experiments do not imply a mixed Can/CynT complex.

Both selected native complexes and the native pathway explicitly name `NCBITaxon:511145`, MG1655. Reviewed UniProt entries have broader K-12 scope (`83333`). The original physiology experiments used K-12 derivatives, including HfrR5-derived mutants, and are not claimed to be new direct experiments on MG1655. Pathway taxon scope is represented in `taxa` and source evidence on the relevant pathway/catalysis edges; `occurs_in` is reserved by the schema for cellular components.

The recycling interpretation is conditional. The 1993 study examined 0.03% versus 3% CO2, found defective cyanate use in cynT deletion mutants at the lower concentration, and tested rescue at the higher concentration. The publisher PDF was inspected for strain provenance, activity controls and growth/degradation results. This supports the record's conditional description, not an absolute CynT requirement in every environment. [PMID:8444806](https://pubmed.ncbi.nlm.nih.gov/8444806/)

## Exclusions and access limits

CynX is retained in the research comparison only. Current reviewed P17583 calls it a cyanate importer but supplies no inline experimental code for that function; PathBank assigns a transport reaction. The 1993 experiments left its physiological role unresolved. The graph does not convert the annotation into demonstrated transport, and the older negative phenotype does not establish that transport is impossible.

The boundary also excludes induced expression as direct protein activation, broader nitrogen assimilation, cyanate generation, slow background cyanate decay, growth toxicity, assay inhibitor networks, Can-dependent growth, and plant/Pseudomonas alternatives. These dispositions are enumerated in `cyanate-source-projection.json`. Computational free energies were not promoted into measured kinetics or physiological direction evidence.

The raw directory is `/private/tmp/pathwaymech-cyanate-monapterin-evidence/cyanate`. Full MetaCyc objects are freshly retrieved official-mirror version 22.5; reviewed UniProt release 2026_03 and indexed primary abstracts were preserved unchanged from same-day triage. `cyanate-sources.json` gives exact response-body/member/compressed-file digest scopes and retrieval lineage. Abstracts of 1740425, 3110153 and 10801492 were inspected completely; no inaccessible full texts are claimed read. Publisher PDF text for 8444806 was browsable, although the local download returned403, so no PDF-body digest is claimed. Europe PMC XML failures and the NCBI HTML response are recorded as unusable full-text retrievals. Authority identity release and Rhea142 mechanism evidence remain distinct.

## Verification

`cyanate-validation.json` records actual narrow author checks: native and closed schema, independent elemental/charge balance, all side coefficients and locators, native source-to-UniProt bridges and ordering, exact short excerpts, canonical ontology labels, source digests, and actual target KGX evidence/category preservation. These checks do not replace independent scientific review or the parent's integrated render/validate/test/lint gates. Initial native validation rejected an attempted taxon `occurs_in` edge; it was removed and its taxon evidence retained with the corresponding existing pathway/catalysis claims before the successful final author run.
