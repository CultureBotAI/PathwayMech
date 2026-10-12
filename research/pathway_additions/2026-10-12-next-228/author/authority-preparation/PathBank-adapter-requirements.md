# Bounded PathBank interface identity extension required for MG

The reviewed archive-aware adapter rejects the actual frozen MG member with `ValueError: PathBank additional pathways must be attached native interface stubs`. This is an identity-adapter coverage gap, not evidence that the source objects are absent. No source or implementation edits were made by this helper.

## Exact issuing artifacts

- Official archive URL: `https://pathbank.org/downloads/pathbank_primary_biopax.zip`.
- Retained ZIP: `/private/tmp/pathwaymech-pathbank-dbcan-evidence/pathbank/pathbank_primary_biopax.zip`; 27,782,843 bytes; SHA256 `b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44`.
- Exact member: `PW002096.owl`; 42,234 bytes; SHA256 `473c3b61e69910e3ff52bbfff79daf3e9d1939f4ccf9c2cb8bb8ea96e08b2bb8`.
- Unmodified extracted member: `/private/tmp/pathwaymech-next-228-preflight-20261012/raw/PW002096.owl`.
- Requested primary accession: `SMP0002108`, with native URI `http://identifiers.org/smpdb/SMP0002108` and matching `UnificationXref` (`db=SMPDB`, `id=SMP0002108`). Its direct displayName is `2-O-alpha-Mannosyl-D-glycerate Degradation`.
- Attached interface accession: `SMP0000839`, native URI `http://identifiers.org/smpdb/SMP0000839`, matching independent SMPDB `UnificationXref`; direct displayName `Gluconeogenesis from L-Malic Acid`.

`unresolved-pathbank-source-manifest.json` supplies the exact typed ZIP manifest entry. `unresolved-pathbank-copy-plan.json` binds both original levels. The ZIP is the same one already used by the lyxose proposal; no new attribution to a live per-pathway download is justified.

## Exact native attachment graph

All objects and predicates below are BioPAX level 3. Fragment IDs are native RDF subjects, not invented PathBank accessions.

1. The primary Pathway has `pathwayComponent -> #SubPathwayControls/109883`.
2. Independently, it has `pathwayOrder -> #PathwaySubPathway/109883`; that object is a `PathwayStep` with `stepProcess -> #SubPathwayControls/109883`.
3. `#SubPathwayControls/109883` is an **Interaction**, not a BioPAX Control or Inhibition. Its direct displayName is `SubPathwayControl109883`; its two direct names are `SubPathway109883Control` and `InhibitorySubPathwayControl`.
4. The Interaction has exactly two direct `participant` pointers: `#Compound/PW_C001870` and `http://identifiers.org/smpdb/SMP0000839`.
5. The local participant is a resolved `SmallMolecule` with displayName `2-Phospho-D-glyceric acid`, name `SubPathwayInhibitor`, and `entityReference -> #CompoundReference/PW_C001870`. Its source-local existence is distinct from any exact external chemical identity.
6. The interface is a `Pathway` with one direct displayName and the direct marker name `InhibitorySubPathway`. It has its PathWhiz and SMPDB xrefs, but **no pathwayComponent/pathwayOrder or expanded biochemical content**.
7. The primary pathway also contains its actual reaction/transport and catalysis objects; it is not merely an interface stub.

The current adapter accepts a different shape: an attached `SubPathway` Pathway whose own members resolve to Interaction objects. It neither follows this primary-owned Interaction participant bridge nor permits this empty `InhibitorySubPathway` interface shape.

## Required closed behavior

Extend only the issuing identity-selection behavior. Preserve the existing direct/ordered `SubPathway` mode and its outputs. Add a distinct bounded branch for this original-backed `InhibitorySubPathway` shape:

- Resolve a primary-owned process through the existing validated direct-component or ordered-step path. Do not scan arbitrary document interactions or global descendants for a child URI. The two actual attachment paths are redundant; retaining either intact native path can be a positive case, while removing both must fail.
- Require an exact BioPAX Interaction with the observed source marker, exactly one resolved local SmallMolecule participant and exactly one different native Pathway participant; reject absent, duplicate, dangling, extra or unrelated participants.
- Require the referenced Pathway's matching native SMPDB accession/URI, one nonempty direct biological displayName, the exact native interface marker, and no expansion into its own chemistry. Keep generic marker names out of biological name synonyms.
- Keep subject uniqueness, native namespace, XML-base, parent-root selection and original provenance guards. Do not hardcode SMP0002108, SMP0000839, PW002096 or the numeric local IDs into the parser.
- Use the structural/source markers only to recognize the documented issuing format. They do **not** authorize a biological inhibition predicate, inhibitor mechanism, directed pathway dependency, exact chemical identity, or expanded child membership. The schema/source snapshot remains an identity authority, not a scientific causal assertion.
- Preserve the whole-ZIP SHA/byte count and selected-member SHA/byte count as separate typed provenance. Snapshot `pathway_accessions` should remain root-first and include only the actually proven interface accession. Consumer scope must accept the additional validated accession without broadening to arbitrary archive contents.

## Original-backed tests and remaining adoption gates

A positive bounded build should resolve the two direct native titles above from the original complete ZIP and selected member; labels must not be copied from the draft or handcrafted tables. Test direct-only, ordered-only and both-path attachment, provided each retained path still resolves the exact original Interaction shape.

Negative derivatives should reject: both attachment paths removed; attachment to a different process/step; wrong step type; unowned same-marker Interaction elsewhere; unresolved/duplicated Interaction or child; wrong process type; missing/incorrect source markers; no child participant; two child participants; extra/dangling/duplicate participants; wrong local participant type; conflicting SMPDB xref/URI; unrelated extra Pathway; empty or generic displayName; expanded child chemistry; wrong namespaces or nested XML base; altered archive/member hash/count/root or duplicate member names. A marker alone must never turn an unattached pathway into an authorized identity.

Replay every previously supported PathBank original, the lyxose `PW002100.owl` archive selection, its direct/ordered attachment regression cases, and the full focused authority/consumer tests. Scientific regression must preserve the MG author's explicit source-conflict disposition: no inhibition is inferred from these labels. No whole-corpus or full canonical gate is claimed here; implementation/review, full original-backed build, final scientific review and adoption remain root-owned.
