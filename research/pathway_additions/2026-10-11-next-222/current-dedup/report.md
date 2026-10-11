# Current-corpus duplicate and adoption-scope audit

**No duplicate of the complete PathBank:SMP0002083 candidate was found.** The audit covers reviewed PR421 commit0227eb43e306d989240369c083b717230ef2ede1, tree929b9b0578a280aed04e20cf33d412b13ba0d822, at the explicitly named221worktree. All222 maintained records were parsed and their actual bytes independently checked against the Git tree's blob IDs. All1216 reaction instances were compared through actual consumes/produces and has_input/has_output material endpoints, not names alone. None consumes inosine plusATP to produceIMP. Exact target SHA11ceb3fe99f2ed2966bb8a68faf8fa836a6a4a9e94b2bc0c499bb1119fd3cddd remained unchanged.

The target remains all three chemical reactions, AdeP transport and the native opaque Aspartate Metabolism input interface. This audit does not reduce it to the related three-reaction MetaCyc core and does not substitute current author assertions for independent scientific review. Root subsequently reported a minor PWML evidence-locator finding, issue422; that is a separate successor provenance correction, not a duplicate or changed native pathway boundary.

## Mechanistic distinctions

| Existing record | Overlap | Why it is not this pathway |
|---|---|---|
| MetaCyc:P121-PWY, salvageI | DeoD, adenine/adenosine, shared primary genetics | RHEA27643 uses the opposite phosphorylase direction; Apt producesAMP. It lacks the Add/Gsk inosine-toIMP branch. |
| MetaCyc:PWY-6609, salvageIII | Exact first two directed steps27644 and24409, Add/DeoD, some evidence | Its terminal route is inosine phosphorolysis27647 then hypoxanthine phosphoribosyltransfer17975. It does not contain inosine kinase21141 or this complete transport/interface boundary. |
| MetaCyc:PWY-6579, guanine/guanosine salvage | Gsk, DeoD and shared2020 regulation study | Gsk phosphorylates guanosine toGMP (27711), not inosine toIMP. The other branch also endsGMP. |
| PathBank:SMP0002089, purine deoxyribonucleoside degradation | Add/DeoD and primary assembly sources | Its six steps act on deoxyribonucleosides and end in free bases, acetaldehyde and glyceraldehyde3P; no ATP-dependent inosine salvage. |
| MetaCyc:PWY-6123/PWY-6124, IMP biosynthesis | IMP endpoint | De novo ring construction through AICAR/FAICAR differs from nucleoside salvage. |
| Yeast AMP/GMP de novo records | IMP as input and downstream nucleotide chemistry | These consumeIMP or modify nucleotide phosphates; they do not produceIMP from inosine. |

Rhea master-family and exact directional IDs were searched separately; the opposite27643 is not silently equated with27644. The exact candidateIDs SMP0002083/PWY-6611 and native IDs/labels, primary referenceIDs/DOIs, protein/gene/complex IDs, transport and downstream interface references were included. Broad GO salvage labels do not establish exact variant coverage.

## Prior mentions and search completeness

The search inventoried5371 files with ignored and hidden files included and symlinks followed. Lexical searches explicitly enabled binary-content search. Only Git administrative internals and the installed .venv environment were excluded, with their rationale recorded; no research, source, generated, cache, history or application directory was excluded. The only symlink was the explicitly excluded195 runtime environment. Four maintained record files matched the exact mechanism/reference queries; other hits were authorities, generated exports, reviews, history, prior research or implementation text. All match paths/hashes and bounded identity/terminal contexts are retained.

All nonmaintained YAML was also parsed:14 record-shaped historical/withheld/review specimens were examined for terminal chemistry, and none contains it. There were no YAML parse failures. These are not counted as current pathway owners, but they were not ignored.

Prior189 salvageIII and192 salvageI dossiers were read, including the earlier independent/resolved review context. They explicitly distinguish the kinase route. The201 scout calls PWY-6611/SMP0002083 a strong followup, not an already authored record. Frozen PathBank inventory and source-projection mentions are provenance/lead records; they are not proof that this complete current definition is already curated. Shared Gsk/DeoD/Add proteins or a shared paper are likewise not pathway equivalence.

## Authority and adoption boundary

The exact reviewed authority baseline is bound to bothSHA256 and Git blobs:

- conf/identifier_sources.json:624 entries; SHA8986e0aa609719692dbb07dfd78cadc3acf99dded0ce0f3641665d77ea5f7e26.
- ontology.json:1871 terms; SHA505d40e7422ddc43aea7e0dd934d8ba8d448815a160a56d78663b4f3051e8da9.
- sources.json:2251 terms; SHAbb462c5cc88cce38a85a557b190c01a96b3a6b113f4d18333d360192714fea6a.

Of47 candidate named IDs,31 already have the exact same canonical label and16 need new authority selection: the candidate and downstream pathway IDs, Transport505, six compartment-specific chemical instances, RHEA21141, copper(2+) CHEBI29036, AdeP P31466, PurR P0ACP7/PC00033, and the two Entrez genes. No existing label differs. This is an adoption inventory, not approval of a new production adapter, policy, authority snapshot, or scientific claim.

Root can ground this audit after merge by an exact tree bridge. Root reported actual merge d8e3888528088e7bba468df57056f9f0e588b463 with the same tree929b at21:55:55Z; this report records that as a root-provided bridge, not an independently performed publication verification. Before adoption, the correction target and final approved authority output must be bound explicitly. No maintained files, shared cache, Git state or GitHub state were mutated. Only read-only rev-parse and ls-tree were used.

This is a bounded duplicate/adoption audit, not a claim that PathBank, DRAM, SEED or other source queues are exhausted. Optional next-lead selection was not part of the completed audit; existing queues remain available without a new viability claim.
