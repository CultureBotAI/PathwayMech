# Complete independent menaquinol-8 review after all provenance corrections

- Review: 20261011T064102Z-menaquinol-completed-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T06:40:32Z
- Finished UTC: 2026-10-11T06:41:02Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete ten-reaction pathway is supported within its stated E. coli and assay scopes. All three minor provenance findings are independently resolved with exact predecessor lineage. All 56 node identities, 85 edges and 181 evidence items were assessed; reaction chemistry and biological assertions are unchanged by the final three-pointer cleanup. MenE assembly and other source-specific scientific limits remain explicit.

## Scope And Provenance

Full independent review of one complete native pathway, all 56 nodes, 85 edges and 181 evidence items.

Selection: Frozen final target SHA 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492; all changed record, author, authority and gate inputs were reinspected before this completed successor.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d776b82c9c598bb79885ad01514b07900a678de0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5838 | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml | maintained | superpathway of menaquinol-8 biosynthesis I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical final inspection | passed | True | MetaCyc:PWY-5838 | Exact current target and all listed source inputs canonically reinspected after final corrections and gate seal. |
| Fresh post-pointer render | passed | True | MetaCyc:PWY-5838 | Root coordinated command completed after the final three-pointer correction; complete log hash independently verified. |
| Fresh post-pointer validate | passed | True | MetaCyc:PWY-5838 | Root coordinated command completed after the final three-pointer correction; complete log hash independently verified. |
| Fresh post-pointer lint | passed | True | MetaCyc:PWY-5838 | Root coordinated command completed after the final three-pointer correction; complete log hash independently verified. |
| Fresh post-pointer identifiers | passed | True | MetaCyc:PWY-5838 | Root coordinated command completed after the final three-pointer correction; complete log hash independently verified. |
| Fresh post-pointer kgx | passed | True | MetaCyc:PWY-5838 | Root coordinated command completed after the final three-pointer correction; complete log hash independently verified. |
| Fresh post-pointer diff | passed | True | MetaCyc:PWY-5838 | Root coordinated command completed after the final three-pointer correction; complete log hash independently verified. |
| Retained complete suite before three locator removals | passed | True | MetaCyc:PWY-5838 | 1050 passed, 3 skipped, 3 warnings in 291.11s (0:04:51). This completed run preceded only removal of three redundant absent pointers. No chemistry or code changed; all six affected non-test gates and graph/KGX checks were freshly rerun. No repeated full-suite claim. |
| Superseded pre-fix suite | failed | False | MetaCyc:PWY-5838 | Deliberately interrupted after 1022 passed and 3 skipped before source-attribution corrections; not treated as a completed pass. |
| Independent strict original pointers and actual KGX replay | passed | False | MetaCyc:PWY-5838 | Exactly three parsed locator changes; all 59 remaining UniProt pointers resolve with no optional-field exception. Actual isolated KGX preserves all 56 nodes, 85 edges and 181 evidence items. Prior ten-reaction original chemistry replay is retained and the full scientific content is unchanged. |

## Scientific And Domain Assessments

### Exact native pathway and completeness

identity: supported. Targets: MetaCyc:PWY-5838.

PWY-5838 is the complete ten-step parent across its four children. Precursors supplied by that boundary are not recursively expanded, and the broader PathBank respiratory object is explicitly dispositioned rather than silently dropped.

### All local identities and source bridges

grounding: supported. Targets: MetaCyc:PWY-5838.

All 56 identities match final authorities. Ten protein entries, five named assemblies, native catalytic links and two exact chain-specific Rhea subclass bridges were independently inspected.

### Reaction sides, orientation, charge and chain length

consistency: supported. Targets: MetaCyc:PWY-5838.

All ten directed Rhea IDs are left-to-right relative to their masters. Forty-three chemical sides with source coefficients balance by atoms and charge. IspB consumes five IPP plus one FPP, yielding the eight-isoprene donor. Current quinol endpoints are preserved without an invented oxidation step.

### Catalysts, assemblies and cofactors

representation: supported. Targets: MetaCyc:PWY-5838.

Source-defined MenF/MenD/MenB/MenI/IspB assemblies are retained with their source scope. MenE function uses enables without selecting among tetramer, homodimer-by-similarity and inhibitor-bound monomer. Alternative metals, bicarbonate activation and similarity-level Mg annotations remain qualified.

### Evidence tier, strain and source attribution

evidence: supported. Targets: MetaCyc:PWY-5838.

Primary abstracts and inspected full articles are distinguished. K-12/MG1655 identity, BW25113 deletions, XL1 Blue MenB and heterologous/recombinant assays do not become universal native flux claims. Each of the 181 evidence items was reviewed in its narrow edge context.

### Both independent review findings resolved

provenance: supported. Targets: MetaCyc:PWY-5838.

All three provenance findings are now independently resolved. Eight article locators match original headings; RCSB assembly and primary structural context are separated; three nonexistent optional note pointers are removed.

### Expression context

scope: supported. Targets: MetaCyc:PWY-5838.

The canonical-client offline replay reproduces the retained context. It supplies neither mechanistic proof nor absence evidence.

### Redundant nonexistent optional JSON pointers

provenance: supported. Targets: MetaCyc:PWY-5838.

The three absent note paths were removed without scientific changes; all remaining 59 UniProt JSON pointers resolve exactly. Valid cofactor/evidence-code support is unchanged.

### Final applicable validation and generated evidence

schema: supported. Targets: MetaCyc:PWY-5838.

Current native/closed schemas, identity policies, evidence checks and generated pages pass. Actual final graph/KGX audit preserves all 85 edges and 181 evidence items. The complete suite passed before the final three source-locator removals and is not falsely described as rerun afterward.

## Findings

### f-primary-locators: Eight primary citations name inaccurate article sections

minor / resolved / confirmed; issue key: menaquinol-primary-section-locators.

Edges 047, 054, 059, 061, 063, 065, 066 and 072 contain absent or inaccurate section headings. Exact original and replacement locations plus raw body digests are in menaquinol-independent-review-audit.json. The source assertions themselves are supported by the corrected locations.

Disposition: All eight source_locator substitutions were independently compared with original HTML/XML headings, paragraphs and anchors; their assertions and all graph chemistry remain unchanged. Final target retains every verified correction.

### f-mene-context: MenE assembly payloads do not supply protein and ligand context

minor / resolved / confirmed; issue key: menaquinol-mene-structure-context-attribution.

Edge059 assigns protein/mutation and inhibitor context to two RCSB assembly-only JSON payloads. Those payloads support monomeric author/PISA assemblies, while exact context is supported by separate retained original primary paragraphs. Restrict assembly assertions to their fields and attach the explicit primary bridges.

Disposition: Final edge059 restricts both RCSB statements to actual author/PISA monomeric assembly fields. Separate primary blocks cite original PMC6653581 P17/P32 and PMC4624480 P11/P23 for exact protein, mutation, ligand and PDB context; all four original paragraphs were independently reread.

### f-optional-cofactor-locators: Three cofactor locators include an absent optional note field

minor / resolved / confirmed; issue key: menaquinol-absent-optional-cofactor-locators.

Edges050/051 cite UniProt P17109 and edge057 cites P29208 with /comments/2/cofactors; /comments/2/note. The original complete COFACTOR objects have no note member. The valid cofactors array fully supports the chemical identities and evidence grades; remove only the redundant absent paths.

Disposition: The final record removes exactly the three absent /comments/2/note strings. Independent complete JSON-pointer enumeration resolves all 59 remaining pointers; exact semantic comparison and actual KGX replay confirm no other record or evidence assertion changed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-initial-target | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml; Entire record; eight primary evidence source_locator fields | refutes | All 85 edges and 67 references read. Eight source_locator fields contain section-heading mismatches documented in the independent audit. |
| e-PMC107237 | https://pmc.ncbi.nlm.nih.gov/articles/PMC107237/; Original article body; exact observed locations listed in menaquinol-independent-review-audit.json | supports | Independently read relevant original Methods/Results and assembly/assay passages; supports the associated assertion at the corrected location, while the named heading is absent or inaccurate. |
| e-PMC2943303 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2943303/; Original article body; exact observed locations listed in menaquinol-independent-review-audit.json | supports | Independently read relevant original Methods/Results and assembly/assay passages; supports the associated assertion at the corrected location, while the named heading is absent or inaccurate. |
| e-PMC3630204 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3630204/; Original article body; exact observed locations listed in menaquinol-independent-review-audit.json | supports | Independently read relevant original Methods/Results and assembly/assay passages; supports the associated assertion at the corrected location, while the named heading is absent or inaccurate. |
| e-PMC3697248 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3697248/; Original article body; exact observed locations listed in menaquinol-independent-review-audit.json | supports | Independently read relevant original Methods/Results and assembly/assay passages; supports the associated assertion at the corrected location, while the named heading is absent or inaccurate. |
| e-PMC4116151 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4116151/fullTextXML; Original article body; exact observed locations listed in menaquinol-independent-review-audit.json | supports | Independently read relevant original Methods/Results and assembly/assay passages; supports the associated assertion at the corrected location, while the named heading is absent or inaccurate. |
| e-PMC4624480 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4624480/; Original article body; exact observed locations listed in menaquinol-independent-review-audit.json | supports | Independently read relevant original Methods/Results and assembly/assay passages; supports the associated assertion at the corrected location, while the named heading is absent or inaccurate. |
| e-current-target | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml; Entire structural diff; edge059 two RCSB assertions | refutes | Exactly eight prior locator changes are present. The two assembly JSON assertions additionally identify protein/mutant/ligand contexts that are absent from those payloads. |
| e-rcsb6 | https://data.rcsb.org/rest/v1/core/assembly/6NJ0/1; Entire original payload; pdbx_struct_assembly; rcsb_struct_symmetry | supports | Monomeric author/PISA assembly is explicit. Protein identity, wild-type status and inhibitor identity fields are not in this assembly payload. |
| e-rcsb5 | https://data.rcsb.org/rest/v1/core/assembly/5C5H/1; Entire original payload; pdbx_struct_assembly; rcsb_struct_symmetry | supports | Monomeric author/PISA assembly is explicit. R195K protein and OSB-AMS identities are not fields in this payload. |
| e-mene2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6653581/; Methods paragraph P17; Results paragraph P32; P8 and P18 | supports | Original Methods P17 explicitly identifies wild-type E. coli MenE plus analogue 5 and coordinates 6NJ0; P8/P18 identify OSB-AMS in 5C5H. |
| e-mene2015 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4624480/; Methods P11; Results P23 | supports | Original source explicitly identifies the R195K E. coli MenE and OSB-AMS co-crystal as 5C5H. |
| e-final-target | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml; Entire final record, all fields and semantic differences from initial/intermediate captures | supports | Final change is confined to exact primary retrieval locators and MenE source attribution; all nodes and reaction chemistry are unchanged. |
| e-original-replay | research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json; independent_chemistry_replay; edge_coverage; execution_receipts | supports | Independent original RDF, direct native XML, full UniProt and ChEBI replay passes all 43 side occurrences, ten atom/charge balances, ten native members, fixed-chain subclass bridges and 68 exact reference-body hashes. |
| e-native-boundary | https://pathway.yeastgenome.org/getxml?META:PWY-5838; Pathway[@frameid="PWY-5838"]/reaction-list; original child objects PWY-5837, PWY-5783, PWY-5852 and MENAQUINONESYN-PWY | supports | Direct native hierarchy contains ten reactions, including the IspB donor branch. The original PathBank eleven-object map has duplicate MenA projections and a respiratory overlay; no complete-map equivalence is asserted. |
| e-protein-evidence | research/pathway_additions/2026-10-11-next-195/menaquinol-protein-projection.json; All ten full UniProt entry bodies; FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT and CAUTION comments with exact pointers | supports | Each projection was compared with the original JSON. Experimental, HAMAP and similarity assignments are distinguished; identities are K-12 and component role does not imply universal single-protein sufficiency. |
| e-current-identities | data/identifier_authorities/ontology.json and data/identifier_authorities/sources.json; All 56 declared node IDs and exact labels | supports | Every declared identity resolves with an exact matching label in final pinned snapshots. Original ontology/native/protein sources were inspected; label resolution alone is not used as mechanism proof. |
| e-primary-scope | research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json; scientific_limits; source_fix_verification; all cited primary abstract bodies and full article Methods/Results sections | supports | Independent original-source reading preserves MenF versus EntC, corrected MenD/MenH products, conditional MenE assembly, MenB bicarbonate and tag effects, MenI residual knockout flux, IspB chain-length scope, and older MenA donor/redox limits. |
| e-context | research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json; imodulondb_independent_replay | context_only | All 37 retained bodies and 35 searches replay through unchanged canonical client. Ten named genes have dataset contexts; returned component52 has no exact queried members. No exhaustive membership or biological absence inference. |
| e-optional-P17109 | https://rest.uniprot.org/uniprotkb/P17109.json; Entire original JSON; /comments/2 keys and /comments/2/cofactors | supports | The complete COFACTOR object contains cofactors with the cited ChEBI and ECO facts, but no note member. Explicit original-object enumeration establishes only this bounded absent pointer. |
| e-optional-P29208 | https://rest.uniprot.org/uniprotkb/P29208.json; Entire original JSON; /comments/2 keys and /comments/2/cofactors | supports | The complete COFACTOR object contains cofactors with the cited ChEBI and ECO facts, but no note member. Explicit original-object enumeration establishes only this bounded absent pointer. |
| e-final-gates | research/pathway_additions/2026-10-11-next-195/integration-receipt.json; final_gates; test_summary; generated graph supporting receipt | supports | All seven final coordinated commands passed; 1050 tests passed,3skipped,3warnings. This validates the current exact record before optional-pointer cleanup; no future check is implied. |
| e-completed-target | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml; Entire final record and exact semantic comparison against pre-pointer record | supports | Only three redundant note paths differ from the previously assessed record; every scientific assertion, chemical side, coefficient, node and reference remains identical. |
| e-completed-audit | research/pathway_additions/2026-10-11-next-195/menaquinol-independent-completed-audit.json; changes; strict_original_UniProt_pointers_resolved; source_hashes; kgx; resolved_findings | supports | Independent exact-delta check, strict pointer enumeration of original JSON bodies and actual KGX evidence replay all pass. The previous independent ten-reaction chemistry/source audit is linked by digest. |
| e-completed-gates | research/pathway_additions/2026-10-11-next-195/integration-receipt.json; final_gates; full_suite_before_pointer_cleanup; test_scope; supporting_receipts | supports | All six fresh final gates and graph/KGX/baseline checks pass; the prior complete 1050/3/3 suite is explicitly distinguished from those post-pointer commands. All log and supporting-receipt digests were independently verified. |

## Limits And Additional Notes

- MenE physiological assembly remains unresolved: native tetramer, UniProt homodimer by similarity, inhibitor-bound monomeric PISA/author assemblies; enables does not assert monomer sufficiency.
- MenD functional dimer is supported; later structural/solution work also observes a smaller tetramer population. A universal solution-only dimer is not inferred.
- MenA original assay used farnesyl donor and older extraction studies measure quinones; exact octaprenyl/quinol chemistry is independently grounded by current native/Rhea, without invented respiratory oxidation.
- MenB bicarbonate activation is distinct from a consumed chemical substrate; Salmonella structural comparison and E. coli XL1 Blue/BW25113/MG1655 assay contexts remain explicit.
- Some protein evidence is HAMAP or similarity; all primary abstracts are distinguished from inspected full articles. No uniform direct-experimental grade is inferred.
- All eleven PathBank reaction objects have dispositions; duplicate MenA projections and hydrogenase respiratory overlay are not claimed as additional biosynthetic reactions.
- iModulon context does not prove catalysis, mechanism or biological absence.
- The superseded pre-fix full suite was deliberately interrupted at 1022 passed/3 skipped, exit2. It is not reported as a passing suite; final coordinated results are separately inspected.
- Deterministic source/export replay and full-corpus gates complement rather than replace manual scientific review.
- The full 1,050 passed / 3 skipped suite ran before the final three redundant locator removals. Six fresh applicable gates and graph/KGX audits cover the final byte state; no post-cleanup repeated full suite is claimed.
- Independent reviewer did not author the target or its source projections. Reviewer-authored methylcitrate is excluded.
- Initial and intermediate target/source inputs remain archived; both immutable partial reports and both exact finding lineages are retained.
- Local read-only helper attempts encountered an unavailable optional bs4 import and whitespace across inline HTML tags. Installed lxml and normalized-whitespace heading comparison resolved those method errors without changing scientific assertions.
- The optional-pointer observation was separately persisted before correction. Its original source inputs and successful pre-cleanup full-suite seal are archived, preserving the exact discovery and remediation sequence.
- The first completed-draft validation rejected an ID/finish-timestamp mismatch before saving. The draft timestamp prefix was corrected; no scientific input changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T064102Z-menaquinol-completed-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Complete independent menaquinol-8 review after all provenance corrections
started_at: '2026-10-11T06:40:32Z'
finished_at: '2026-10-11T06:41:02Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author menaquinol or its source dossiers. Full
    target and original source sections were read independently. Reviewer-authored
    methylcitrate is excluded.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete ten-reaction pathway is supported within its stated E. coli
  and assay scopes. All three minor provenance findings are independently resolved
  with exact predecessor lineage. All 56 node identities, 85 edges and 181 evidence
  items were assessed; reaction chemistry and biological assertions are unchanged
  by the final three-pointer cleanup. MenE assembly and other source-specific scientific
  limits remain explicit.
source:
  git_revision: d776b82c9c598bb79885ad01514b07900a678de0
  state: working_tree
  inputs:
  - path: conf/identifier_sources.json
    sha256: 552a5c3065ba911a2273bb78920c55ea2d52d76743d778bd50607cab29dbc656
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 51eee8026be46917276ac3047b36e1f3905fa9a3cfaee1a84e6a385baaab09ac
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 56d26c06b72b5de61bb690d1e7b0e8b6e2410b1741ff5c7537f8c4c0506ba8f8
    role: context
  - path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    sha256: 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: c635a91493a53b519ed2c8e0f825adcca320e1c8d96ef87a69459c8a2cb14937
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/authority-integration.json
    sha256: 64875d2a7007fb6a8f9bc471dfd910b5246f8ff932678dd7a324071a869f4ba8
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/authority-source-inspection.json
    sha256: 7dbaa26ddd89ae0ef1c75ed78ae663b3359a988d70ffa88a5df71ad9dc4c1c1e
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/generated-graph-kgx-audit.json
    sha256: 3c6f9c3c705fd85eb8656ecc19f49807bc40604f110d198a34fc0d4eaacdfb2d
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-context.json
    sha256: b68015a40f63072b8595b1dba8a173dfa9adc757e0aa60c5c9c4b9a5914eadd1
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-parser-replay.json
    sha256: 5e1a3aae8d47c568a3ca74a851a90edb287b3362016bfeed99d42d6e51450eeb
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-runner-availability.json
    sha256: 7996cefbe69cc800c1b560de79e17a0ac65e18147fb847311ecd87513058766a
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-source-manifest.json
    sha256: 069e566c3b897c7b824c27da2f3a5026898c6e6e5963522fbc00f66cb80e6bd7
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/integration-receipt.json
    sha256: fb1865b0f2cd7e1adee4cb326d4692c4e34f0002167257a304f14678a26d7a5b
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-authority-delta.json
    sha256: 52e0bf0fd7cf3c019f12016e62734c00eaa7bb9e7b441ccf64427d1f06da5c14
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-curation.md
    sha256: 570d7482804c5f12c5df2853c41514a08031fcd8bd8933ad934b902586a821ec
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-dedup.json
    sha256: c73332869d1a8b07827011010259166d44cdf55b8b7d43a387e45df0182665ff
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-focused-replay.py
    sha256: d8910db1b76580bf73511e80d721c212cf5f1cd02fd1bcf123b30832d5cde54c
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-identifiers.json
    sha256: c1a94635f73e85fe8614c45b4abd10aea32a083d898facf498e0d6023e7a4a05
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-completed-audit.json
    sha256: c648c6978443a54d42ac7a9b7cab7dbb56566c8ba715b0db3d1a8e753baf93d6
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json
    sha256: f4b32af5bcfbd1331e51a9df5c7960fc6a51ba19805d7576a015f9e4b53f4162
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-review-audit.json
    sha256: 32bd0ccf2f18034b6997ae13e096b85de5c7d33a365942195e95ebe73e296be8
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-pointer-fix.json
    sha256: b2b3553bee8e6b81c296a1c408751b4a1f5898450678e9b6be736742bd6cb721
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-pointer-replay.py
    sha256: 6ed8aab7daa571d368e3cef1c19408a3a09a0f8f56a8e0cfade15706b3dcd10f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-protein-projection.json
    sha256: 0797be8718f83b13701abdc185f9352b650998158ce851ec5e025b3a330f0bad
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-provenance-fix.json
    sha256: 76159be648583507a0b5d7b409de7aeab440c086f3334c8bf90fc30449c66f11
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-replay.py
    sha256: 793f75e0126444933c4177430caaa8476f1d8d9b75e3bd174373ffe0ab2c227c
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-source-manifest.json
    sha256: 059482990d2828a003244e2eef5db04570a2e4c1610a5c00173df47c38b18835
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-source-projection.json
    sha256: dbe22e015ee03cba8a6f8f817ba6c6ad297a6726b19b59cdcc476dcbf7ec9a28
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-structure-context-fix.json
    sha256: 073770bb5491179bb3c12db844f9b2439b138020fee0ef9c396ec5f36a25cc7f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-validation.json
    sha256: d1efdad49331bfcf5cc7d0b0c1d9a7b917f74787f235c21f487480fe215ce7f0
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/pre-pointer-review-inputs/manifest.json
    sha256: 93c0f9b9d001628db2d024ad2fe0e98a9d268ee337d34b42ef79aa4959c6ccef
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY-5838
  path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
  label: superpathway of menaquinol-8 biosynthesis I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    role: maintained record
scope:
  description: Full independent review of one complete native pathway, all 56 nodes,
    85 edges and 181 evidence items.
  selection: Frozen final target SHA 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492;
    all changed record, author, authority and gate inputs were reinspected before
    this completed successor.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5838
  exclusions:
  - target: Reviewer-authored methylcitrate and all other records
    reason: Outside this independent one-record scientific scope.
  - target: All possible microbial menaquinone routes and physiological conditions
    reason: The exact selected E. coli implementation does not establish universal
      route or assembly behavior.
checks:
- check_id: inspect-completed
  name: Canonical final inspection
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-195-menaquinol-review/targets.yaml
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-authority-delta.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-curation.md
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-dedup.json --input
    research/pathway_additions/2026-10-11-next-195/menaquinol-focused-replay.py --input
    research/pathway_additions/2026-10-11-next-195/menaquinol-identifiers.json --input
    research/pathway_additions/2026-10-11-next-195/menaquinol-independent-completed-audit.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-pointer-fix.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-pointer-replay.py
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-protein-projection.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-provenance-fix.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-replay.py --input
    research/pathway_additions/2026-10-11-next-195/menaquinol-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-source-projection.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-structure-context-fix.json
    --input research/pathway_additions/2026-10-11-next-195/menaquinol-validation.json
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input conf/identifier_sources.json --input src/pathwaymech/schema.py --input
    src/pathwaymech/schema/pathwaymech.yaml --input docs/CAUSAL_GRAPHS.md --input
    research/pathway_additions/2026-10-11-next-195/integration-receipt.json --input
    research/pathway_additions/2026-10-11-next-195/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-195/authority-integration.json
    --input research/pathway_additions/2026-10-11-next-195/authority-source-inspection.json
    --input research/pathway_additions/2026-10-11-next-195/pre-pointer-review-inputs/manifest.json
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-source-manifest.json
  status: passed
  required: true
  exit_code: 0
  summary: Exact current target and all listed source inputs canonically reinspected
    after final corrections and gate seal.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-render
  name: Fresh post-pointer render
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command completed after the final three-pointer correction;
    complete log hash independently verified.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-validate
  name: Fresh post-pointer validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command completed after the final three-pointer correction;
    complete log hash independently verified.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-lint
  name: Fresh post-pointer lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command completed after the final three-pointer correction;
    complete log hash independently verified.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-identifiers
  name: Fresh post-pointer identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command completed after the final three-pointer correction;
    complete log hash independently verified.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-kgx
  name: Fresh post-pointer kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-195-kgx
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command completed after the final three-pointer correction;
    complete log hash independently verified.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-diff
  name: Fresh post-pointer diff
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 git
    diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command completed after the final three-pointer correction;
    complete log hash independently verified.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: full-suite-before-pointer-cleanup
  name: Retained complete suite before three locator removals
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: passed
  required: true
  exit_code: 0
  summary: 1050 passed, 3 skipped, 3 warnings in 291.11s (0:04:51). This completed
    run preceded only removal of three redundant absent pointers. No chemistry or
    code changed; all six affected non-test gates and graph/KGX checks were freshly
    rerun. No repeated full-suite claim.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: initial-interrupted-test
  name: Superseded pre-fix suite
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: failed
  required: false
  exit_code: 2
  summary: Deliberately interrupted after 1022 passed and 3 skipped before source-attribution
    corrections; not treated as a completed pass.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: independent-strict-pointers-kgx
  name: Independent strict original pointers and actual KGX replay
  command: .venv/bin/python /private/tmp/pathwaymech-next-195-menaquinol-review/strict-final-pointers.py
  status: passed
  required: false
  exit_code: 0
  summary: Exactly three parsed locator changes; all 59 remaining UniProt pointers
    resolve with no optional-field exception. Actual isolated KGX preserves all 56
    nodes, 85 edges and 181 evidence items. Prior ten-reaction original chemistry
    replay is retained and the full scientific content is unchanged.
  target_ids:
  - MetaCyc:PWY-5838
evidence:
- evidence_id: e-initial-target
  kind: record_content
  reference: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
  locator: Entire record; eight primary evidence source_locator fields
  accessed_at: '2026-10-11T06:17:04Z'
  support: refutes
  summary: All 85 edges and 67 references read. Eight source_locator fields contain
    section-heading mismatches documented in the independent audit.
  snapshot_sha256: ce7ca7155a12be396ea94b0b83c5b6ca72285c1cf53188fb1916e559c7e15e81
- evidence_id: e-PMC107237
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC107237/
  locator: Original article body; exact observed locations listed in menaquinol-independent-review-audit.json
  accessed_at: '2026-10-11T06:17:04Z'
  support: supports
  summary: Independently read relevant original Methods/Results and assembly/assay
    passages; supports the associated assertion at the corrected location, while the
    named heading is absent or inaccurate.
  snapshot_sha256: 7783345d801962b37134f7772ef6f79bb177a3574b65b60ef54e90086de571b9
- evidence_id: e-PMC2943303
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2943303/
  locator: Original article body; exact observed locations listed in menaquinol-independent-review-audit.json
  accessed_at: '2026-10-11T06:17:04Z'
  support: supports
  summary: Independently read relevant original Methods/Results and assembly/assay
    passages; supports the associated assertion at the corrected location, while the
    named heading is absent or inaccurate.
  snapshot_sha256: 17b89c4f0fbf1f02265c257edfa7780233bea713fe4b6cfbdcacda489e8b44fb
- evidence_id: e-PMC3630204
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3630204/
  locator: Original article body; exact observed locations listed in menaquinol-independent-review-audit.json
  accessed_at: '2026-10-11T06:17:04Z'
  support: supports
  summary: Independently read relevant original Methods/Results and assembly/assay
    passages; supports the associated assertion at the corrected location, while the
    named heading is absent or inaccurate.
  snapshot_sha256: 3a09918deee6b20b79a67c4687b6e904d3fc2f4ac109aa76f66f5545ff93c169
- evidence_id: e-PMC3697248
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3697248/
  locator: Original article body; exact observed locations listed in menaquinol-independent-review-audit.json
  accessed_at: '2026-10-11T06:17:04Z'
  support: supports
  summary: Independently read relevant original Methods/Results and assembly/assay
    passages; supports the associated assertion at the corrected location, while the
    named heading is absent or inaccurate.
  snapshot_sha256: 44af8e69c22e4cca4b7bb80de3064852d7a3d5d03408072bab08875248a6861d
- evidence_id: e-PMC4116151
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4116151/fullTextXML
  locator: Original article body; exact observed locations listed in menaquinol-independent-review-audit.json
  accessed_at: '2026-10-11T06:17:04Z'
  support: supports
  summary: Independently read relevant original Methods/Results and assembly/assay
    passages; supports the associated assertion at the corrected location, while the
    named heading is absent or inaccurate.
  snapshot_sha256: dc6f06a5e9076d94e0016621bd0e57bfc78aeb423d4462079f0d666cca2f47e3
- evidence_id: e-PMC4624480
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4624480/
  locator: Original article body; exact observed locations listed in menaquinol-independent-review-audit.json
  accessed_at: '2026-10-11T06:17:04Z'
  support: supports
  summary: Independently read relevant original Methods/Results and assembly/assay
    passages; supports the associated assertion at the corrected location, while the
    named heading is absent or inaccurate.
  snapshot_sha256: f4a8d851344a536bc7d5dead20245d0ce5bf0d52ebfad038cc407c5c3ef07756
- evidence_id: e-current-target
  kind: record_content
  reference: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
  locator: Entire structural diff; edge059 two RCSB assertions
  accessed_at: '2026-10-11T06:21:38Z'
  support: refutes
  summary: Exactly eight prior locator changes are present. The two assembly JSON
    assertions additionally identify protein/mutant/ligand contexts that are absent
    from those payloads.
  snapshot_sha256: 11ebb55f4c8150b09ed35eac0960515b9e7f6225bea05086d9a7a3fc918e2586
- evidence_id: e-rcsb6
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6NJ0/1
  locator: Entire original payload; pdbx_struct_assembly; rcsb_struct_symmetry
  accessed_at: '2026-10-11T06:21:38Z'
  support: supports
  summary: Monomeric author/PISA assembly is explicit. Protein identity, wild-type
    status and inhibitor identity fields are not in this assembly payload.
  snapshot_sha256: 711cc1b8b27497be201e99fc7dc3c078648f1764d538449329b9c020cd8d292c
- evidence_id: e-rcsb5
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/5C5H/1
  locator: Entire original payload; pdbx_struct_assembly; rcsb_struct_symmetry
  accessed_at: '2026-10-11T06:21:38Z'
  support: supports
  summary: Monomeric author/PISA assembly is explicit. R195K protein and OSB-AMS identities
    are not fields in this payload.
  snapshot_sha256: de5a814d338a1656e19f702f2fc3d161eca3c7631548778124b57dd1aa65a308
- evidence_id: e-mene2019
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6653581/
  locator: Methods paragraph P17; Results paragraph P32; P8 and P18
  accessed_at: '2026-10-11T06:21:38Z'
  support: supports
  summary: Original Methods P17 explicitly identifies wild-type E. coli MenE plus
    analogue 5 and coordinates 6NJ0; P8/P18 identify OSB-AMS in 5C5H.
  snapshot_sha256: 7780cf50173d5f570480f707c0b912a00a900f3a16675cba7190dceea2accef4
- evidence_id: e-mene2015
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4624480/
  locator: Methods P11; Results P23
  accessed_at: '2026-10-11T06:21:38Z'
  support: supports
  summary: Original source explicitly identifies the R195K E. coli MenE and OSB-AMS
    co-crystal as 5C5H.
  snapshot_sha256: f4a8d851344a536bc7d5dead20245d0ce5bf0d52ebfad038cc407c5c3ef07756
- evidence_id: e-final-target
  kind: record_content
  reference: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
  locator: Entire final record, all fields and semantic differences from initial/intermediate
    captures
  accessed_at: '2026-10-11T06:28:03Z'
  support: supports
  summary: Final change is confined to exact primary retrieval locators and MenE source
    attribution; all nodes and reaction chemistry are unchanged.
  snapshot_sha256: a9a1d571791078e1286e57ad686df30579254adf9ab0f5590d93e09757190f42
- evidence_id: e-original-replay
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json
  locator: independent_chemistry_replay; edge_coverage; execution_receipts
  accessed_at: '2026-10-11T06:28:03Z'
  support: supports
  summary: Independent original RDF, direct native XML, full UniProt and ChEBI replay
    passes all 43 side occurrences, ten atom/charge balances, ten native members,
    fixed-chain subclass bridges and 68 exact reference-body hashes.
  snapshot_sha256: f4b32af5bcfbd1331e51a9df5c7960fc6a51ba19805d7576a015f9e4b53f4162
- evidence_id: e-native-boundary
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-5838
  locator: Pathway[@frameid="PWY-5838"]/reaction-list; original child objects PWY-5837,
    PWY-5783, PWY-5852 and MENAQUINONESYN-PWY
  accessed_at: '2026-10-11T06:28:03Z'
  support: supports
  summary: Direct native hierarchy contains ten reactions, including the IspB donor
    branch. The original PathBank eleven-object map has duplicate MenA projections
    and a respiratory overlay; no complete-map equivalence is asserted.
  snapshot_sha256: d64dee995187648e7d1be403e38ef9824e68a729c1264d23af32f575973b78b8
- evidence_id: e-protein-evidence
  kind: database
  reference: research/pathway_additions/2026-10-11-next-195/menaquinol-protein-projection.json
  locator: All ten full UniProt entry bodies; FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
    SUBUNIT and CAUTION comments with exact pointers
  accessed_at: '2026-10-11T06:28:03Z'
  support: supports
  summary: Each projection was compared with the original JSON. Experimental, HAMAP
    and similarity assignments are distinguished; identities are K-12 and component
    role does not imply universal single-protein sufficiency.
  snapshot_sha256: 8032e47d707737018c057b36db71c0b8e2fc5aeb58c50ee833f4f4397baaca89
- evidence_id: e-current-identities
  kind: authority
  reference: data/identifier_authorities/ontology.json and data/identifier_authorities/sources.json
  locator: All 56 declared node IDs and exact labels
  accessed_at: '2026-10-11T06:28:03Z'
  support: supports
  summary: Every declared identity resolves with an exact matching label in final
    pinned snapshots. Original ontology/native/protein sources were inspected; label
    resolution alone is not used as mechanism proof.
- evidence_id: e-primary-scope
  kind: primary_source
  reference: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json
  locator: scientific_limits; source_fix_verification; all cited primary abstract
    bodies and full article Methods/Results sections
  accessed_at: '2026-10-11T06:28:03Z'
  support: supports
  summary: Independent original-source reading preserves MenF versus EntC, corrected
    MenD/MenH products, conditional MenE assembly, MenB bicarbonate and tag effects,
    MenI residual knockout flux, IspB chain-length scope, and older MenA donor/redox
    limits.
  snapshot_sha256: f4b32af5bcfbd1331e51a9df5c7960fc6a51ba19805d7576a015f9e4b53f4162
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json
  locator: imodulondb_independent_replay
  accessed_at: '2026-10-11T06:28:03Z'
  support: context_only
  summary: All 37 retained bodies and 35 searches replay through unchanged canonical
    client. Ten named genes have dataset contexts; returned component52 has no exact
    queried members. No exhaustive membership or biological absence inference.
  snapshot_sha256: f4b32af5bcfbd1331e51a9df5c7960fc6a51ba19805d7576a015f9e4b53f4162
- evidence_id: e-optional-P17109
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P17109.json
  locator: Entire original JSON; /comments/2 keys and /comments/2/cofactors
  accessed_at: '2026-10-11T06:33:34Z'
  support: supports
  summary: The complete COFACTOR object contains cofactors with the cited ChEBI and
    ECO facts, but no note member. Explicit original-object enumeration establishes
    only this bounded absent pointer.
  snapshot_sha256: a02406319564da0ea256fa19e90d3ad0e7db04c99b7a71c25ecc8c3d4ceaad5e
- evidence_id: e-optional-P29208
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P29208.json
  locator: Entire original JSON; /comments/2 keys and /comments/2/cofactors
  accessed_at: '2026-10-11T06:33:34Z'
  support: supports
  summary: The complete COFACTOR object contains cofactors with the cited ChEBI and
    ECO facts, but no note member. Explicit original-object enumeration establishes
    only this bounded absent pointer.
  snapshot_sha256: 6d7677f59ed90cebf877f362aed5f4f4a151fe69f48c1b4299fd8995928ce23e
- evidence_id: e-final-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-195/integration-receipt.json
  locator: final_gates; test_summary; generated graph supporting receipt
  accessed_at: '2026-10-11T06:33:34Z'
  support: supports
  summary: All seven final coordinated commands passed; 1050 tests passed,3skipped,3warnings.
    This validates the current exact record before optional-pointer cleanup; no future
    check is implied.
  snapshot_sha256: 1d9098c0ce1286cee43d296db7ad74a6d47a5023ed54d9ed65eb87ea452614ef
- evidence_id: e-completed-target
  kind: record_content
  reference: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
  locator: Entire final record and exact semantic comparison against pre-pointer record
  accessed_at: '2026-10-11T06:40:32Z'
  support: supports
  summary: Only three redundant note paths differ from the previously assessed record;
    every scientific assertion, chemical side, coefficient, node and reference remains
    identical.
  snapshot_sha256: 8d24e6ff858759aa4eaecd04b456ffa1b79c992bc090637f5cc8805a5ecbf492
- evidence_id: e-completed-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-completed-audit.json
  locator: changes; strict_original_UniProt_pointers_resolved; source_hashes; kgx;
    resolved_findings
  accessed_at: '2026-10-11T06:40:32Z'
  support: supports
  summary: Independent exact-delta check, strict pointer enumeration of original JSON
    bodies and actual KGX evidence replay all pass. The previous independent ten-reaction
    chemistry/source audit is linked by digest.
  snapshot_sha256: c648c6978443a54d42ac7a9b7cab7dbb56566c8ba715b0db3d1a8e753baf93d6
- evidence_id: e-completed-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-195/integration-receipt.json
  locator: final_gates; full_suite_before_pointer_cleanup; test_scope; supporting_receipts
  accessed_at: '2026-10-11T06:40:32Z'
  support: supports
  summary: All six fresh final gates and graph/KGX/baseline checks pass; the prior
    complete 1050/3/3 suite is explicitly distinguished from those post-pointer commands.
    All log and supporting-receipt digests were independently verified.
  snapshot_sha256: fb1865b0f2cd7e1adee4cb326d4692c4e34f0002167257a304f14678a26d7a5b
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact native pathway and completeness
  outcome: supported
  summary: PWY-5838 is the complete ten-step parent across its four children. Precursors
    supplied by that boundary are not recursively expanded, and the broader PathBank
    respiratory object is explicitly dispositioned rather than silently dropped.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-native-boundary
  - e-original-replay
- assessment_id: a-grounding
  area: grounding
  topic: All local identities and source bridges
  outcome: supported
  summary: All 56 identities match final authorities. Ten protein entries, five named
    assemblies, native catalytic links and two exact chain-specific Rhea subclass
    bridges were independently inspected.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-current-identities
  - e-original-replay
  - e-protein-evidence
- assessment_id: a-chemistry
  area: consistency
  topic: Reaction sides, orientation, charge and chain length
  outcome: supported
  summary: All ten directed Rhea IDs are left-to-right relative to their masters.
    Forty-three chemical sides with source coefficients balance by atoms and charge.
    IspB consumes five IPP plus one FPP, yielding the eight-isoprene donor. Current
    quinol endpoints are preserved without an invented oxidation step.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-original-replay
  - e-primary-scope
- assessment_id: a-components
  area: representation
  topic: Catalysts, assemblies and cofactors
  outcome: supported
  summary: Source-defined MenF/MenD/MenB/MenI/IspB assemblies are retained with their
    source scope. MenE function uses enables without selecting among tetramer, homodimer-by-similarity
    and inhibitor-bound monomer. Alternative metals, bicarbonate activation and similarity-level
    Mg annotations remain qualified.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-protein-evidence
  - e-primary-scope
  - e-mene2019
  - e-mene2015
  - e-rcsb6
  - e-rcsb5
- assessment_id: a-primary
  area: evidence
  topic: Evidence tier, strain and source attribution
  outcome: supported
  summary: Primary abstracts and inspected full articles are distinguished. K-12/MG1655
    identity, BW25113 deletions, XL1 Blue MenB and heterologous/recombinant assays
    do not become universal native flux claims. Each of the 181 evidence items was
    reviewed in its narrow edge context.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-primary-scope
  - e-protein-evidence
  - e-final-target
- assessment_id: a-fixes
  area: provenance
  topic: Both independent review findings resolved
  outcome: supported
  summary: All three provenance findings are now independently resolved. Eight article
    locators match original headings; RCSB assembly and primary structural context
    are separated; three nonexistent optional note pointers are removed.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-final-target
  - e-original-replay
  - e-mene2019
  - e-mene2015
  - e-rcsb6
  - e-rcsb5
  - e-completed-target
  - e-completed-audit
- assessment_id: a-context
  area: scope
  topic: Expression context
  outcome: supported
  summary: The canonical-client offline replay reproduces the retained context. It
    supplies neither mechanistic proof nor absence evidence.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-context
- assessment_id: a-optional-locators
  area: provenance
  topic: Redundant nonexistent optional JSON pointers
  outcome: supported
  summary: The three absent note paths were removed without scientific changes; all
    remaining 59 UniProt JSON pointers resolve exactly. Valid cofactor/evidence-code
    support is unchanged.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-optional-P17109
  - e-optional-P29208
  - e-final-target
  - e-completed-target
  - e-completed-audit
- assessment_id: a-final-gates
  area: schema
  topic: Final applicable validation and generated evidence
  outcome: supported
  summary: Current native/closed schemas, identity policies, evidence checks and generated
    pages pass. Actual final graph/KGX audit preserves all 85 edges and 181 evidence
    items. The complete suite passed before the final three source-locator removals
    and is not falsely described as rerun afterward.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-completed-audit
  - e-completed-gates
findings:
- finding_id: f-primary-locators
  issue_key: menaquinol-primary-section-locators
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Eight primary citations name inaccurate article sections
  description: Edges 047, 054, 059, 061, 063, 065, 066 and 072 contain absent or inaccurate
    section headings. Exact original and replacement locations plus raw body digests
    are in menaquinol-independent-review-audit.json. The source assertions themselves
    are supported by the corrected locations.
  target_ids:
  - MetaCyc:PWY-5838
  field_paths:
  - mechanistic_edges[id=menaquinol-edge-047]/evidence[reference_id=PMID:23564174]/source_locator
  - mechanistic_edges[id=menaquinol-edge-054]/evidence[reference_id=PMID:23637813]/source_locator
  - mechanistic_edges[id=menaquinol-edge-059]/evidence[reference_id=PMID:26394156]/source_locator
  - mechanistic_edges[id=menaquinol-edge-061]/evidence[reference_id=PMID:20643650]/source_locator
  - mechanistic_edges[id=menaquinol-edge-063]/evidence[reference_id=PMID:20643650]/source_locator
  - mechanistic_edges[id=menaquinol-edge-065]/evidence[reference_id=PMID:23564174]/source_locator
  - mechanistic_edges[id=menaquinol-edge-066]/evidence[reference_id=PMID:25010423]/source_locator
  - mechanistic_edges[id=menaquinol-edge-072]/evidence[reference_id=PMID:9573170]/source_locator
  evidence_ids:
  - e-initial-target
  - e-PMC107237
  - e-PMC2943303
  - e-PMC3630204
  - e-PMC3697248
  - e-PMC4116151
  - e-PMC4624480
  - e-final-target
  - e-original-replay
  - e-completed-target
  - e-completed-audit
  rule_id: review-yaml-record Evidence Rules; docs/CAUSAL_GRAPHS.md precise source
    locators
  native_severity: minor
  normalization_reason: Bounded provenance gap; no unsupported chemistry or wrong
    enzyme identity is established by this finding.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    role: maintained_record
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T063334Z-menaquinol-optional-locator-review
    finding_id: f-primary-locators
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T062138Z-menaquinol-structure-context-review
    finding_id: f-primary-locators
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T061704Z-menaquinol-initial-independent-review
    finding_id: f-primary-locators
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/357
  disposition_reason: All eight source_locator substitutions were independently compared
    with original HTML/XML headings, paragraphs and anchors; their assertions and
    all graph chemistry remain unchanged. Final target retains every verified correction.
- finding_id: f-mene-context
  issue_key: menaquinol-mene-structure-context-attribution
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: MenE assembly payloads do not supply protein and ligand context
  description: Edge059 assigns protein/mutation and inhibitor context to two RCSB
    assembly-only JSON payloads. Those payloads support monomeric author/PISA assemblies,
    while exact context is supported by separate retained original primary paragraphs.
    Restrict assembly assertions to their fields and attach the explicit primary bridges.
  target_ids:
  - MetaCyc:PWY-5838
  field_paths:
  - mechanistic_edges[id=menaquinol-edge-059]/evidence[reference_id=DOI:10.2210/pdb6NJ0/pdb]/source_assertion
  - mechanistic_edges[id=menaquinol-edge-059]/evidence[reference_id=DOI:10.2210/pdb5C5H/pdb]/source_assertion
  evidence_ids:
  - e-current-target
  - e-rcsb6
  - e-rcsb5
  - e-mene2019
  - e-mene2015
  - e-final-target
  - e-original-replay
  - e-completed-target
  - e-completed-audit
  rule_id: review-yaml-record Evidence Rules; docs/CAUSAL_GRAPHS.md precise source
    locators
  native_severity: minor
  normalization_reason: Bounded provenance gap; no unsupported chemistry or wrong
    enzyme identity is established by this finding.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    role: maintained_record
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/360
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T063334Z-menaquinol-optional-locator-review
    finding_id: f-mene-context
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T062138Z-menaquinol-structure-context-review
    finding_id: f-mene-context
  disposition_reason: Final edge059 restricts both RCSB statements to actual author/PISA
    monomeric assembly fields. Separate primary blocks cite original PMC6653581 P17/P32
    and PMC4624480 P11/P23 for exact protein, mutation, ligand and PDB context; all
    four original paragraphs were independently reread.
- finding_id: f-optional-cofactor-locators
  issue_key: menaquinol-absent-optional-cofactor-locators
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Three cofactor locators include an absent optional note field
  description: Edges050/051 cite UniProt P17109 and edge057 cites P29208 with /comments/2/cofactors;
    /comments/2/note. The original complete COFACTOR objects have no note member.
    The valid cofactors array fully supports the chemical identities and evidence
    grades; remove only the redundant absent paths.
  target_ids:
  - MetaCyc:PWY-5838
  field_paths:
  - mechanistic_edges[id=menaquinol-edge-050]/evidence[reference_id=UniProtKB:P17109]/source_locator
  - mechanistic_edges[id=menaquinol-edge-051]/evidence[reference_id=UniProtKB:P17109]/source_locator
  - mechanistic_edges[id=menaquinol-edge-057]/evidence[reference_id=UniProtKB:P29208]/source_locator
  evidence_ids:
  - e-optional-P17109
  - e-optional-P29208
  - e-final-target
  - e-completed-target
  - e-completed-audit
  rule_id: review-yaml-record Evidence Rules; exact native source locators
  native_severity: minor
  normalization_reason: Valid adjacent cofactor pointers support every assertion;
    this is a small retrievability defect, not an unsupported biochemical or cofactor
    claim.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    role: maintained_record
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/361
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T063334Z-menaquinol-optional-locator-review
    finding_id: f-optional-cofactor-locators
  disposition_reason: The final record removes exactly the three absent /comments/2/note
    strings. Independent complete JSON-pointer enumeration resolves all 59 remaining
    pointers; exact semantic comparison and actual KGX replay confirm no other record
    or evidence assertion changed.
actions: []
limitations:
- 'MenE physiological assembly remains unresolved: native tetramer, UniProt homodimer
  by similarity, inhibitor-bound monomeric PISA/author assemblies; enables does not
  assert monomer sufficiency.'
- MenD functional dimer is supported; later structural/solution work also observes
  a smaller tetramer population. A universal solution-only dimer is not inferred.
- MenA original assay used farnesyl donor and older extraction studies measure quinones;
  exact octaprenyl/quinol chemistry is independently grounded by current native/Rhea,
  without invented respiratory oxidation.
- MenB bicarbonate activation is distinct from a consumed chemical substrate; Salmonella
  structural comparison and E. coli XL1 Blue/BW25113/MG1655 assay contexts remain
  explicit.
- Some protein evidence is HAMAP or similarity; all primary abstracts are distinguished
  from inspected full articles. No uniform direct-experimental grade is inferred.
- All eleven PathBank reaction objects have dispositions; duplicate MenA projections
  and hydrogenase respiratory overlay are not claimed as additional biosynthetic reactions.
- iModulon context does not prove catalysis, mechanism or biological absence.
- The superseded pre-fix full suite was deliberately interrupted at 1022 passed/3
  skipped, exit2. It is not reported as a passing suite; final coordinated results
  are separately inspected.
- Deterministic source/export replay and full-corpus gates complement rather than
  replace manual scientific review.
- The full 1,050 passed / 3 skipped suite ran before the final three redundant locator
  removals. Six fresh applicable gates and graph/KGX audits cover the final byte state;
  no post-cleanup repeated full suite is claimed.
notes:
- Independent reviewer did not author the target or its source projections. Reviewer-authored
  methylcitrate is excluded.
- Initial and intermediate target/source inputs remain archived; both immutable partial
  reports and both exact finding lineages are retained.
- Local read-only helper attempts encountered an unavailable optional bs4 import and
  whitespace across inline HTML tags. Installed lxml and normalized-whitespace heading
  comparison resolved those method errors without changing scientific assertions.
- The optional-pointer observation was separately persisted before correction. Its
  original source inputs and successful pre-cleanup full-suite seal are archived,
  preserving the exact discovery and remediation sequence.
- The first completed-draft validation rejected an ID/finish-timestamp mismatch before
  saving. The draft timestamp prefix was corrected; no scientific input changed.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/357
- https://github.com/CultureBotAI/PathwayMech/issues/360
- https://github.com/CultureBotAI/PathwayMech/issues/361
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261011T061704Z-menaquinol-initial-independent-review
  relationship: Resolves the original eight-locator finding with exact lineage.
- repository: CultureBotAI/PathwayMech
  review_id: 20261011T062138Z-menaquinol-structure-context-review
  relationship: Supersedes partial review, preserving its resolved locator finding
    and resolving its MenE source-attribution finding after independent verification.
- repository: CultureBotAI/PathwayMech
  review_id: 20261011T063334Z-menaquinol-optional-locator-review
  relationship: Completes the whole-record assessment and resolves the remaining optional-pointer
    finding, retaining all three exact finding lineages.
```
