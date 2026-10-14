This handoff was written in the external author workspace. Complete raw source bodies remain external per `docs/CAUSAL_GRAPHS.md`. Maintained `README.md` and `evidence/external-archive-manifest.json` bind public URLs, versions, whole-original hashes, archive filenames and members; historical external paths are not the sole evidence identity.

# Complete external author handoff

Candidate: `candidate.yaml`, exact identity `MetaCyc:PWY0-301`, proposed maintained filename `data/pathways/l-ascorbate-degradation-i.yaml`. This external candidate has35 participants, five core molecular activities plus the downstream pentose-phosphate interface,55 mechanistic edges,36 source references, and passes `validate_record` (see `validation.json`). Parent owns integration, native review, generated pages, curation history, gates and publication. No maintained repository or GitHub mutation was performed by this author.

The selected boundary is the full native MetaCyc 27.0 five-event route: RXN0-2461 → RXN0-5214 → RXN0-705 → LXULRU5P-RXN → RIBULPEPIM-RXN. Four non-transport events are represented by exact formal directional Rhea IDs28804,14354,18499 and22369, preserving water, hydron and CO2 as well as carbon-bearing substrates. UlaE is right-to-left relative to its native equation. The old22.5 four-event boundary is retained as a release difference, not silently preferred.

Evidence dossier:
- `reading/SCIENTIFIC-READING.md`: full primary reading, figure/table inspection, experimental contexts, negative findings, source conflicts and access limits.
- `edge-source-matrix.json`: every edge and qualifier, its claim-level source locator, exact original path/hash/URL.
- `reference-original-bindings.json`: exact whole-original binding for all reference nodes; abstracts are explicitly distinguished from full bodies.
- `node-identity-matrix.json`: every record node, issuing-source provenance/owner or ontology original, scientific bindings and semantic cautions.
- `source-original-request-hash-manifest.json`: whole original and figure hashes with actual request receipts; binds the separate authority manifest.
- `dedup-receipt.json`, `dedup-matches.txt`, `dedup-record-identity.json`: fresh gitignore-independent search and maintained exact-ID enumeration.

Authority handoff is `/private/tmp/pathwaymech-ascorbate-authority-20261013/INTEGRATION.md`, its `provenance-manifest.json`, and `proposed-source-additions.json`. The authority agent is preparing canonical staging and owns copying the stable candidate into the isolated worktree. Existing source owners are preserved. No new source adapter is needed: native HTML establishes exact identity/title for the unusual transport and HPr classes, with complete XML independently supporting chemistry; native protein XML supports the assemblies; NCBI Gene supports two promoter-bearing genes.

Canonical label corrections already applied: CHEBI:58774 is `3-dehydro-L-gulonate 6-phosphate` (formal charge remains in the chemical original); native phospho-HPr class uses literal `Npi`; MetaCyc:RXN0-2461 uses its accepted native title `EC 2.7.1.194` and explains its complete aggregate transport in the description and edges. UniProt UlaG retains the canonical `Probable...` label despite newer direct activity evidence.

Material scientific limits retained in the candidate:
1. PMID20359483 (UlaG2010) and PMID18844374 (UlaR2008) were inspected as complete primary abstracts, with independent native source support; full body methods/figures were unavailable. Only their explicit activity/assembly/effector results are used. No unavailable experimental construct, kinetics or binding constant is inferred.
2. Native RXN0-2461 is a net HPr-fed aggregate. HPr-bound residue classes are not free histidine or whole PtsH sequence identities. Obsolete Rhea33303 is not used; replacement42436 is not asserted identical to the net aggregate. Its generic immediate histidyl donor conflicts with the separate UlaB Cys9 relay annotation. The candidate makes no direct HPr-to-sugar transfer or UlaB phosphohistidine claim.
3. UlaG Mn2+ and Co2+ are alternatives, not a simultaneous metal requirement. UlaD Mg2+ has curated structural support. UlaF Zn2+ is explicitly a similarity/HAMAP annotation, not a direct UlaF metal experiment; Mg in a coupled assay is not generalized to every enzyme.
4. Reporter regulation in JA134 derivatives is not whole-route flux in MG1655. CRP activates the ulaA promoter, not ulaG; IHF helps basal repression. Free ascorbate does not directly displace UlaR; the 6-phosphate effector has separate 2008 evidence. FNR growth effects do not become a direct transcriptional edge. Proposed DNA looping and inducer exclusion remain proposed.
5. UlaG hexamer, UlaD dimer and UlaABC2:1:1 source assemblies are represented explicitly. UlaD/E/F primary assay constructs are qualified as MG1655-derived, BL21-expressed, His10-tagged then thrombin-cleaved; residual sequence is unspecified. UlaR tag-cleaved binding material is distinguished from the native chromosomal protein in reporter cells.
6. UlaE/UlaF are not substitutes for the SgbU/SgbE/AraD catalyst choices of the existing L-lyxose route. PWY0-301 enzymes-not-used and the retained227 corrective dispositions exclude those alternatives. The aerobic yia route and hypothetical2002 preparative chemistry are outside this record.

No further candidate discovery or scope expansion is part of this handoff. Root should apply the authorized publication cycle to this record only.
