# Complete external author draft: Adenine and Adenosine Salvage II

This successor implements the full current PathBank:SMP0002083 boundary accepted in the sealed preflight: three biochemical reactions, AdeP-mediated adenine/proton transport, and the named non-elementary Aspartate Metabolism interface. No maintained record, production parser, policy or source cache is changed. It remains an external author proposal until independent review and production gates.

## Representation decisions

RHEA:27644, RHEA:24409 and RHEA:21141 carry all14 charge- and stereochemistry-specific material sides. The first is right_to_left relative to Rhea master27642, while the other two are left_to_right. Native PathBank LEFT_TO_RIGHT is diagram-relative and is not substituted for Rhea master orientation. Each coefficient is explicitly one. Transport505 has four compartment-specific material roles (two inputs, two outputs), also native coefficient1. Its exact proton ratio is attributed to the database; the inspected E. coli uptake experiments and abstract-only PMF paper do not establish that ratio.

SMP0000809 is a biological_process node representing the explicitly named opaque native interface. PathBank's real pathwayComponent and participant/input predicates are preserved. Its input molecule retains the native SMP0002083-scoped identifier Compound/PW_C000114_Cytoplasm. The terminal kinase also retains its different native output instance, Compound/PW_C000114_Cytosol. These are neutral inosinic-acid source views; balanced Rhea uses IMP(2-). The source-view has_output is not an additional stoichiometric product. No conversion between charged/generic forms, cytosol/cytoplasm transfer, or whole connected pathway expansion is asserted. Both native instances are retained rather than silently collapsed.

The current predicate vocabulary has no encodes predicate. Exact NCBI Gene identities are therefore retained for the two experimentally supported transcriptional effects, with gene-to-protein correspondence in source evidence, without fabricating an encoding or catalytic edge. PurR inhibits adeP/yieG transcription. Adenine activates add transcription as a measured culture response; this is neither direct ligand binding nor direct Add enzyme activation. The primary study explicitly finds add and deoD not directly PurR-regulated.

Native DeoD hexamer, Gsk dimer and PurR dimer are distinct complex nodes, with subunit copy numbers in edge evidence. The measured Gsk conditional tetramer has no established issuing assembly identifier in this bounded assessment; its ligand-dependent state and lower activity remain explicit in the record/evidence. No fake CURIE or physiological octamer is added. PurR is activated for DNA binding by hypoxanthine OR guanine, not an obligatory joint pair.

## Biological scope and evidence tiers

The primary 2020 Gsk results directly establish inosine phosphorylation, GDP/ppGpp inhibition, dimer-interface dependence and concentration-dependent tetramerization. Biochemical proteins were released tracelessly from SUMO; crystallographic proteins retained a Gly-Ser-His scar. The reviewed434-residue P0AEW6 entry is the sequence authority, not a claim that every construct had those exact terminal residues. Older database GTP inhibition conflicts with the newer GDP-not-GTP result and is preserved as a conflict in the description, not a uniformly asserted inhibitory edge.

K+ stimulation and Cu2+/Zn2+ inhibition are additionally retained as reviewed experimental-literature annotations (UniProt ECO:0000269). The cited1995 original was only accessible as an abstract, so the graph does not invent quantitative ion conditions or physiological exposure. Crystallographic K+ occupancy is distinct from a required catalytic cofactor. Add's one-Zn-per-subunit annotation is explicitly HAMAP ECO:0000255 inference. Gsk Mg2+ is retained with the probable additional free-Mg requirement and actual ATP-Mg/MgCl2 assay conditions distinguished.

Nonphysiological experimental reagents such as coformycin, p-chloromercuribenzoate, formycin analogs and crystallization calcium are not added as endogenous pathway components. Alternative substrates/phosphate donors, whole PurR regulon targets, upstream SgrS/Hfq regulation, and recursive aspartate/TCA/NAD pathways are outside this exact native pathway boundary; their source mentions are preserved in originals/preflight. Internal-adenine feedback on AdeP remains a kinetic-model hypothesis/"may" annotation rather than a measured inhibition edge.

The reviewed DeoD protein is239 residues, while the primary structural report describes238-residue chains. No initiator processing is inferred. Transport constructs came from T184 and assays used named mutants; source genes, expression hosts and functional assay hosts are not conflated. Native PathBank BioSource5649 labels K-12 while its taxon679895 points to BW25113, UniProt proteins are83333 and the selected NCBI genes/MetaCyc complexes are511145. These scopes are kept distinct.

## Source/version and citation limitations

The frozen2019 archive is not the current definition. Current export adds the opaque interface and compartment-specific nodes. The intact current PWML fails strict XML parsing at an unbound option prefix; a bounded raw-text interface section is used with independent valid BioPAX support, not a silently cleaned substitute. Exact acquisition successes/failures and hashes are retained in the sealed preflight and this successor.

MetaCyc PWY-6611 is the three-reaction chemical core, not an exact alias for the complete PathBank definition. Its native PMID7551735 citation concerns Aspergillus hydrolysis and is not presented as primary evidence for the E. coli Gsk route. The older1975 primary paper supports the specified mutant kinase comparison, not a measured complete adenine-to-IMP flux. The old1983/1994 transport and1995 kinase full-text requests failed; claims based on their abstracts remain labeled accordingly.

## Production work deliberately separate

The author authority proposal freshly derives exact selected names from issuing originals/retained original ontology SQL, with no contextual-label exemptions in its external gate. That does not make it an approved production snapshot.

1. Current canonical PathBank parsing selects a single Pathway and omits Transport. This original legitimately contains the selected primary pathway plus a downstream stub. Production support needs exact accession/xref root selection and native Transport/compartment entity coverage without importing arbitrary connected pathways. SMP0000809's canonical name is independently grounded by its own original definition.
2. Entrez is schema-allowed but not currently a configured production authority namespace. Gene948224 and945851 require a bounded NCBI Entrezgene XML kind and policy support; HTML attempts were reCAPTCHA despiteHTTP200 and are rejected. Original XML omits Gene-track_status; no explicit status was fabricated.
3. PurR PC00033 requires the native MetaCyc protein XML authority kind addressed independently in221; no unapproved authority output is adopted by this author task.

Full maintained build/history/corpus preservation, canonical production authority rebuild and independent review remain root-owned integration work. The sealed preflight includes exhaustive ignored/hidden/symlink-following dedup against both221-record baselines plus the accepted ethylmalonyl candidate, and semantic terminal-chemistry checks across2404 reaction instances. This is one viable next candidate, not a claim that remaining sources are exhausted.
