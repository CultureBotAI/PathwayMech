# Partial menaquinol successor: cofactor locator cleanup

- Review: 20261011T063334Z-menaquinol-optional-locator-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T06:31:00Z
- Finished UTC: 2026-10-11T06:33:34Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Both earlier provenance findings are resolved and the complete scientific assessment supports the route within its stated limits. Three remaining minor locator fields include a nonexistent optional note path alongside a valid cofactors array. No cofactor assertion or evidence grade is unsupported; remove only the redundant absent paths.

## Scope And Provenance

Complete source assessment with a partial final disposition pending three bounded locator corrections.

Selection: Frozen final target SHA a9a1d571791078e1286e57ad686df30579254adf9ab0f5590d93e09757190f42; canonical inspect precedes assessment and changed inputs are explicitly reinspected.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d776b82c9c598bb79885ad01514b07900a678de0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5838 | data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml | maintained | superpathway of menaquinol-8 biosynthesis I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical inspection of final scientific and gate inputs | passed | True | MetaCyc:PWY-5838 | Actual canonical inspect exited0; current input attestations are retained in source. |
| Coordinated render | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. Exact frozen record/gate surface. |
| Coordinated validate | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. Exact frozen record/gate surface. |
| Coordinated test | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. 1050 passed, 3 skipped, 3 warnings in 291.11s (0:04:51) |
| Coordinated lint | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. Exact frozen record/gate surface. |
| Coordinated identifiers | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. Exact frozen record/gate surface. |
| Coordinated kgx | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. Exact frozen record/gate surface. |
| Coordinated diff | passed | True | MetaCyc:PWY-5838 | Root coordinated command; actual terminal receipt and complete log SHA verified. Exact frozen record/gate surface. |
| Superseded pre-fix suite | failed | False | MetaCyc:PWY-5838 | Deliberately interrupted after1022passed/3skipped before citation corrections; not treated as a completed pass. Final separate suite passed. |

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

The eight inaccurate headings now match original article sections. RCSB assembly facts and primary protein/variant/ligand facts are separated at edge059. Independent source and semantic comparison verifies both changes without chemistry drift.

### Expression context

scope: supported. Targets: MetaCyc:PWY-5838.

The canonical-client offline replay reproduces the retained context. It supplies neither mechanistic proof nor absence evidence.

### Redundant nonexistent optional JSON pointers

provenance: concern. Targets: MetaCyc:PWY-5838.

Three evidence locators name a nonexistent note member. Each cofactor/ECO assertion is fully supported by the valid cofactors array in the same cited object, so only locator hygiene is affected.

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

minor / open / confirmed; issue key: menaquinol-absent-optional-cofactor-locators.

Edges050/051 cite UniProt P17109 and edge057 cites P29208 with /comments/2/cofactors; /comments/2/note. The original complete COFACTOR objects have no note member. The valid cofactors array fully supports the chemical identities and evidence grades; remove only the redundant absent paths.

## Recommended Actions And Acceptance Checks

### a-remove-optional-paths

Remove exactly the three absent /comments/2/note paths, preserving valid cofactors pointers and all assertions. Reinspect correction and refresh affected generated artifacts and applicable validation before completed successor.

- Every remaining UniProt pointer resolves in the original payload.
- Semantic comparison shows only three redundant locator removals and no scientific changes.
- Updated successor retains all three exact finding lineages.

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
- This partial disposition leaves only issue361 open; the earlier independent replay tolerated absent optional note paths when the valid cofactors array supported the complete claim. A later exhaustive pointer pass identified the redundant locators.
- Independent reviewer did not author the target or its source projections. Reviewer-authored methylcitrate is excluded.
- Initial and intermediate target/source inputs remain archived; both immutable partial reports and both exact finding lineages are retained.
- Local read-only helper attempts encountered an unavailable optional bs4 import and whitespace across inline HTML tags. Installed lxml and normalized-whitespace heading comparison resolved those method errors without changing scientific assertions.
- This finding was identified after the separately retained independent scientific/source audit; the completed all-pass shared suite is real but does not erase the locator observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T063334Z-menaquinol-optional-locator-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Partial menaquinol successor: cofactor locator cleanup'
started_at: '2026-10-11T06:31:00Z'
finished_at: '2026-10-11T06:33:34Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author menaquinol or its source dossiers. Full
    target and original source sections were read independently. Reviewer-authored
    methylcitrate is excluded.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: Both earlier provenance findings are resolved and the complete scientific
  assessment supports the route within its stated limits. Three remaining minor locator
  fields include a nonexistent optional note path alongside a valid cofactors array.
  No cofactor assertion or evidence grade is unsupported; remove only the redundant
  absent paths.
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
    sha256: a9a1d571791078e1286e57ad686df30579254adf9ab0f5590d93e09757190f42
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
    sha256: c73dd059339471c15e615ae413537df27b67b03734cd1b2c987e398db7a7aebc
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
    sha256: 1d9098c0ce1286cee43d296db7ad74a6d47a5023ed54d9ed65eb87ea452614ef
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-authority-delta.json
    sha256: ae14a32ace36a913c3ff8283b83924d73036b699040d3067136d7a2674f6e46c
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-curation.md
    sha256: 41fb6cf95c7acac027e2605ea5e7f48ef0e23a994cf88783d39c413f3d746371
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-dedup.json
    sha256: c73332869d1a8b07827011010259166d44cdf55b8b7d43a387e45df0182665ff
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-focused-replay.py
    sha256: d8910db1b76580bf73511e80d721c212cf5f1cd02fd1bcf123b30832d5cde54c
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-identifiers.json
    sha256: 198af50111d380931c88ff837c89ffc9eeb6ce3b98c05c146fe921c8ce466bd3
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-final-audit.json
    sha256: f4b32af5bcfbd1331e51a9df5c7960fc6a51ba19805d7576a015f9e4b53f4162
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-independent-review-audit.json
    sha256: 32bd0ccf2f18034b6997ae13e096b85de5c7d33a365942195e95ebe73e296be8
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-protein-projection.json
    sha256: 8032e47d707737018c057b36db71c0b8e2fc5aeb58c50ee833f4f4397baaca89
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-provenance-fix.json
    sha256: 76159be648583507a0b5d7b409de7aeab440c086f3334c8bf90fc30449c66f11
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-replay.py
    sha256: 793f75e0126444933c4177430caaa8476f1d8d9b75e3bd174373ffe0ab2c227c
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-source-manifest.json
    sha256: 3d549eb371e3f85629b2b2d45e42c2b253e09085336860e0ab629b0964e825e6
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-source-projection.json
    sha256: bf9f7b1b700c7465110d4af5e23d93701a1a26af41618f82c1d562aa059732c0
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-structure-context-fix.json
    sha256: 073770bb5491179bb3c12db844f9b2439b138020fee0ef9c396ec5f36a25cc7f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/menaquinol-validation.json
    sha256: 2b7f1cb6f6217c1ab0ac2868227b1895b1f98b19432e0cddfa371734ee45bfee
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
  description: Complete source assessment with a partial final disposition pending
    three bounded locator corrections.
  selection: Frozen final target SHA a9a1d571791078e1286e57ad686df30579254adf9ab0f5590d93e09757190f42;
    canonical inspect precedes assessment and changed inputs are explicitly reinspected.
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
- check_id: inspect
  name: Canonical inspection of final scientific and gate inputs
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-195-menaquinol-review/targets.yaml
    --input <30 captured inputs>
  status: passed
  required: true
  exit_code: 0
  summary: Actual canonical inspect exited0; current input attestations are retained
    in source.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-render
  name: Coordinated render
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. Exact frozen record/gate surface.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-validate
  name: Coordinated validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. Exact frozen record/gate surface.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-test
  name: Coordinated test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. 1050 passed, 3 skipped, 3 warnings in 291.11s (0:04:51)
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-lint
  name: Coordinated lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. Exact frozen record/gate surface.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-identifiers
  name: Coordinated identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. Exact frozen record/gate surface.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-kgx
  name: Coordinated kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-195-kgx
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. Exact frozen record/gate surface.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: final-diff
  name: Coordinated diff
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 git
    diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Root coordinated command; actual terminal receipt and complete log SHA
    verified. Exact frozen record/gate surface.
  target_ids:
  - MetaCyc:PWY-5838
- check_id: initial-interrupted-test
  name: Superseded pre-fix suite
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: failed
  required: false
  exit_code: 2
  summary: Deliberately interrupted after1022passed/3skipped before citation corrections;
    not treated as a completed pass. Final separate suite passed.
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
  summary: The eight inaccurate headings now match original article sections. RCSB
    assembly facts and primary protein/variant/ligand facts are separated at edge059.
    Independent source and semantic comparison verifies both changes without chemistry
    drift.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-final-target
  - e-original-replay
  - e-mene2019
  - e-mene2015
  - e-rcsb6
  - e-rcsb5
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
  outcome: concern
  summary: Three evidence locators name a nonexistent note member. Each cofactor/ECO
    assertion is fully supported by the valid cofactors array in the same cited object,
    so only locator hygiene is affected.
  target_ids:
  - MetaCyc:PWY-5838
  evidence_ids:
  - e-optional-P17109
  - e-optional-P29208
  - e-final-target
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
  status: open
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
actions:
- action_id: a-remove-optional-paths
  description: Remove exactly the three absent /comments/2/note paths, preserving
    valid cofactors pointers and all assertions. Reinspect correction and refresh
    affected generated artifacts and applicable validation before completed successor.
  finding_ids:
  - f-optional-cofactor-locators
  target_ids:
  - MetaCyc:PWY-5838
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/superpathway-of-menaquinol-8-biosynthesis-i.yaml
    role: maintained_record
  acceptance_checks:
  - Every remaining UniProt pointer resolves in the original payload.
  - Semantic comparison shows only three redundant locator removals and no scientific
    changes.
  - Updated successor retains all three exact finding lineages.
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
- This partial disposition leaves only issue361 open; the earlier independent replay
  tolerated absent optional note paths when the valid cofactors array supported the
  complete claim. A later exhaustive pointer pass identified the redundant locators.
notes:
- Independent reviewer did not author the target or its source projections. Reviewer-authored
  methylcitrate is excluded.
- Initial and intermediate target/source inputs remain archived; both immutable partial
  reports and both exact finding lineages are retained.
- Local read-only helper attempts encountered an unavailable optional bs4 import and
  whitespace across inline HTML tags. Installed lxml and normalized-whitespace heading
  comparison resolved those method errors without changing scientific assertions.
- This finding was identified after the separately retained independent scientific/source
  audit; the completed all-pass shared suite is real but does not erase the locator
  observation.
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
```
