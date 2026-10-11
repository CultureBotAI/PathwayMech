# Glutathione Metabolism III source disposition

PathBank:SMP0002032, exact archive member `PW002018.owl`, is not promoted as a new maintained pathway. Its complete native boundary mixes biosynthesis, redox recycling, amino-acid uptake and unrelated xenobiotic conjugations. A useful map is not automatically one bounded molecular pathway. No new record or authority addition was made; no smaller subset is presented as the whole map.

The archive SHA-256 was independently streamed and matched `b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44`; member SHA-256 is `379a5eccfe939bb7025308b094a3af5e515eba643d1676a16d64a741466850f2`. The source projection retains all seven biochemical reactions, four transport conversions, their explicit pathway membership, controllers, assemblies, and exact conflicting compound objects. The frozen inventory's seven-reaction count excludes its transport conversion classes; it was an initial screening count, not the complete native boundary.

| Native conversion | Exact native content | Disposition |
| --- | --- | --- |
| Reactions/3052 | ATP-dependent glutamate + cysteine ligation | Already covered in MetaCyc:GLUTATHIONESYN-PWY (RHEA:13286). |
| Reactions/3053 | ATP-dependent gamma-glutamylcysteine + glycine ligation | Already covered in MetaCyc:GLUTATHIONESYN-PWY (RHEA:13558). |
| Reactions/3054 | Two GSH reduce generic oxidized glutaredoxin, producing GSSG | Separate recycling chemistry; generic protein states are not a specific experimentally resolved E. coli complex. Native source marks spontaneous. No catalyst inferred. |
| Reactions/3055 | NADPH-dependent glutathione disulfide reduction | Separate recycling chemistry; connected to 3054 but not an identity for the entire map. |
| Reactions/5816 | GSH conjugation of 2-(S-glutathionyl)acetyl chloride | Separate xenobiotic conjugation branch, not a step from GSH biosynthesis through the other xenobiotics. |
| Reactions/5900 | Bromobenzene-3,4-oxide/GSH conjugate, native right-to-left | Separate xenobiotic conjugation branch; native reverse direction is preserved in the projection, not silently corrected. |
| Reactions/5928 | Benzo[a]pyrene-4,5-oxide + GSH, native reversible | Conflicting product metadata; not promoted or repaired by guessing an identity. |
| Transports/352 | Glycine/proton periplasm-to-cytosol transport | Explicit native pathway member; not silently omitted from the map boundary. |
| Transports/369 | Glutamate/sodium periplasm-to-cytosol transport | Explicit native pathway member. |
| Transports/371 | Glutamate/proton periplasm-to-cytosol transport | Explicit native pathway member. |
| ReactionCoupledTransports/102 | Glutamate ABC transport coupled to ATP hydrolysis | Explicit native pathway member; native inner-membrane physical identities and duplicate glutamate sides remain in the projection. |

The specific chemical conflict is within `SmallMoleculeReference[@rdf:ID='CompoundReference/PW_C007696']`: display name “1-Amino-propan-2-ol”, CAS 78-96-6, PubChem compound 4, ChemSpider 3 and ChEBI 291706 accompany formula **C30H29N3O7S**, mass **575.1726** and KEGG C05771. `Reactions/5928` uses this exact object as the conjugation product. Those statements do not establish one consistent identity; the formula is not the formula of the named three-carbon amino alcohol. The source's full original structure and cross-references are retained so a future curator can investigate without trusting a selected field. No atom/charge-balanced curated reaction is claimed, and no corrected product CURIE was invented.

Dedup searched hidden and ignored files in both the current worktree and original Documents checkout, excluding Git internals, virtual-environment dependencies and generated page copies. Exact command, heads, matched files and maintained record hashes are recorded in `glutathione-dedup.json`. The existing biosynthesis record is direct two-step overlap. The yeast WP392 redox map and yeast ECM38/DUG1 degradation route have different source/taxon boundaries and are contextual overlap, not proof of an E. coli duplicate. The glutathione-dependent methylglyoxal route is also distinct. The candidate's original BioPAX contains no PublicationXref objects, so source graph annotations must not be described as directly inspected primary evidence.

The current MetaCyc glutathione biosynthesis and glutathione/glutaredoxin recycling identities describe separate portions, not an independently verified exact equivalent of this entire PathBank map. No exact current MetaCyc whole-map equivalence is asserted. This bounded rejection does not establish exhaustion of glutathione pathways or remaining source inventory.

Per root assignment, the separate next lead is **MetaCyc:P121-PWY, adenine and adenosine salvage I**, to be inspected afresh against the current salvage III record and the legacy PathBank I/II/III labels. It is not a replacement subset of this glutathione map.
