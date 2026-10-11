# Independent scientific review of lipoate biosynthesis and incorporation I

- Review: 20261011T024322Z-lipoate-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T02:30:20Z
- Finished UTC: 2026-10-11T02:43:22.914657Z
- Reviewer: Codex /root/pathway_authority_cache (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 26 edges and 40 evidence blocks support the complete native LipB–LipA route with explicit strain, annotation and formal-redox limits. One minor evidence-placement finding was filed as issue #344 and independently verified corrected before this first immutable review. No open finding remains; final required gates pass.

## Scope And Provenance

Full single-target review of all local nodes, 26 edges, 40 evidence blocks and 17 references.

Selection: Explicit parent assignment to a reviewer who did not author or edit target; governed inspect before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e3bceba7613eb0525af3ff76ef32520201ae9f33.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-501 | data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml | maintained | lipoate biosynthesis and incorporation I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed inspect before scientific assessment | passed | True | MetaCyc:PWY0-501 | Actual initial inspect captured 901a9ba9… before full-record assessment. Changed evidence later re-inspected explicitly. |
| Independent complete raw source replay | passed | True | MetaCyc:PWY0-501 | Fresh full RDF, all 17 sides/coefficient locators and two complete balances, including both reactive parts of carrier 14568; native identity/order/assembly and all 17 record reference digests passed. |
| Independent retained iModulonDB body rehash | passed | False | MetaCyc:PWY0-501 | All 45 exact retained API bodies match manifest; dataset coverage and relevant six query projections inspected. This is rehash/review of root acquisition, not a fresh network call or independent parser replay. |
| just validate | failed | False | MetaCyc:PWY0-501 | Superseded initial validation failed on stale pages after wording corrections; final2 validation below checks rerendered frozen inputs. |
| just render-pages | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. |
| just lint | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. |
| git diff --check | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. |
| just check-identifiers | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. |
| just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. |
| just validate | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. 184 records, 9977 evidence blocks, 272 history records, identifiers, strict schemas, documentation, sources and current pages pass. |
| just test | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. 1048 passed, 3 skipped, 3 warnings in 594.56 seconds. Full suite started before final nicotine/lipoate evidence wording fixes and completed after them; implementation and tests did not change. Final2 full corpus QC separately checks frozen data and regenerated pages. |
| UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | True | MetaCyc:PWY0-501 | Root executed command; actual terminal receipt and log bytes independently inspected. |
| Initial reviewer page-anchor spot check | failed | False | MetaCyc:PWY0-501 | The exact corrected assertion passed, but this ad hoc check incorrectly expected YAML edge IDs to be literal HTML IDs. The renderer uses documented ordinal mechanism-edge-N anchors; no record or page change was needed. Superseded by the corrected check below. |
| Corrected reviewer page-anchor and assertion spot check | passed | True | MetaCyc:PWY0-501 | All 26 rendered mechanism-edge-N anchors are present. Exact corrected LipB source assertion is present and the copied LipA clause is absent. Full graph evidence matching is independently covered by the root artifact audit. |

## Scientific And Domain Assessments

### Exact complete two-step boundary

identity: supported. Targets: MetaCyc:PWY0-501.

MetaCyc PWY0-501 explicitly consists of native RXN0-947→RXN0-949, octanoyl-ACP transfer then protein-bound sulfur insertion. Broader lipoate biosynthesis/lipoylation GO terms and LplA salvage are not substituted. The PathBank acetyl-ACP label is an inspected source error.

### Chemical sides, stereochemistry, whole carrier states and source conflict

grounding: supported. Targets: MetaCyc:PWY0-501.

All 17 source sides/coefficient locators and both equations independently verified. Carrier 14568 contributes both native reactive parts. Rhea Fe(III), oxidized-to-reduced ferredoxin and four protons differ from native Fe(II), reduced-to-oxidized ferredoxin and six protons; the record explicitly preserves the disagreement rather than claiming measured physiology. Protein-bound (R)-dihydrolipoyl endpoint and shared octanoyl state are exact native boundary, not free lipoate.

### Catalysis, monomer/complex roles and primary evidence limits

evidence: supported. Targets: MetaCyc:PWY0-501.

K-12 LipB FUNCTION has direct experimental citations, catalytic Rhea annotation is HAMAP-only. Three inspected primary abstracts support octanoyl-ACP transfer, true initiation and C169 acyl-enzyme mechanism; reverse transfer is preserved. Active monomer/homotrimer remains UniProt experimental annotation, not claimed visible in abstract. Native LipA dimer catalyst and exact Rhea family agree on core protein-bound sulfur insertion. Three inspected primary abstracts support target-bound substrate, two SAM cleavage and same-polypeptide sulfur origin. Later result qualifies the earlier two-polypeptide interpretation. No physiological proof is claimed for formal Fe/ferredoxin bookkeeping.

### Assembly, Fe-S cofactor and inferred cytoplasm

evidence: supported. Targets: MetaCyc:PWY0-501.

Native complex has two EG11306 monomers, explicitly cross-referenced to P60716/MG1655. UniProt allows monomer or dimer without an explicit subunit evidence code, preserved as alternative rather than unique active state. Current cofactor annotation and PMID15362861 abstract independently support two distinct Fe-S clusters per polypeptide. Broad ChEBI class and precise formal Rhea carrier states remain separate. LipB cytoplasm is HAMAP ECO0000255; direct UniProt GO0005737 cross-reference also verified. No experimental localization claim. LipA cytoplasm is HAMAP ECO0000255; direct UniProt GO0005737 cross-reference also verified. No experimental localization claim.

### Exact native membership, corrected evidence placement and order

evidence: supported. Targets: MetaCyc:PWY0-501.

Native first route member RXN0-947 unifies17666; irrelevant LipA clause was removed under344 and correction independently checked. Native second member RXN0-949 unifies16586 at core chemistry level; formal redox discrepancy is not concealed. Explicit native reaction ordering plus exact shared RHEA-COMP9928 support LipB output feeding LipA. No extra free-lipoate or salvage step is appended.

### K-12 annotation versus experimental strain detail

scope: supported. Targets: MetaCyc:PWY0-501.

Both reviewed protein entries identify K-12. Native subunit taxonomy is MG1655. Primary abstracts generally say E. coli and do not independently establish every substrain. LipB experimental function/active-oligomer annotation is distinct from HAMAP catalytic annotation. LipA monomer/dimer alternative has no explicit evidence code.

### Structured expression context

evidence: supported. Targets: MetaCyc:PWY0-501.

Exact lipA/b0628 and lipB/b0630 matches are bounded computational context. Substring lipase hits and missing protein-accession matches are not biological conclusions. No useful module-name hit required component summarization.

### Final authorities, gates and generated artifacts

schema: supported. Targets: MetaCyc:PWY0-501.

Final source input hashes were rechecked after explicit changed-input review. Full required gates and structural publication audit pass; they do not replace the scientific source assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml; Entire YAML, all 26 edges and 40 evidence blocks | supports | Exact complete LipB–LipA route, with source-version chemistry and evidence limits retained. |
| independent-audit | research/pathway_additions/2026-10-11-nicotine-next/lipoate-independent-review-audit.json; Full independent raw-RDF replay, every edge scientific assessment and genuine before/after fix evidence | supports | Independent full source replay session 6049 exited 0 on corrected target: 17 sides, 2 balances, 17 reference hashes, exact native boundary/order/assembly. Deterministic checks supplement source reading. |
| identity-search | Accessible current worktree and retained prior dispositions; Exact MetaCyc/PathBank/Rhea identifiers, labels and related GO definitions | supports | No baseline exact pathway found; current generated/authority surfaces and frozen prior leads are not duplicates. |
| source-1 | https://pathway.yeastgenome.org/getxml?META:PWY0-501; Pathway[@frameid="PWY0-501"]/reaction-list; reaction-layout; Pathway[@frameid="PWY0-501"]/reaction-ordering; reaction-layout | supports | lipoate biosynthesis and incorporation I. Inspected source scope: MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-024, lipoate-edge-025, lipoate-edge-026. |
| source-2 | https://pathway.yeastgenome.org/getxml?META:RXN0-947; Reaction[@frameid="RXN0-947"]/dblink[dblink-db="RHEA"] | supports | octanoyl transfer. Inspected source scope: MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-024. |
| source-3 | https://pathway.yeastgenome.org/getxml?META:RXN0-949; Reaction[@frameid="RXN0-949"]/enzymatic-reaction; dblink[dblink-db="RHEA"]; left; right; Reaction[@frameid="RXN0-949"]/dblink[dblink-db="RHEA"] | supports | lipoyl synthase reaction; native redox convention. Inspected source scope: MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-019, lipoate-edge-025. |
| source-4 | https://pathway.yeastgenome.org/getxml?META:CPLX0-782; Protein[@frameid="CPLX0-782"]/component/Protein; component/coefficient | supports | lipoyl synthase native dimer. Inspected source scope: MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-020. |
| source-5 | https://pathway.yeastgenome.org/getxml?META:EG11306-MONOMER; Protein[@frameid="EG11306-MONOMER"]/dblink[dblink-db="UNIPROT"]; species/Organism | supports | LipA native subunit. Inspected source scope: MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-020. |
| source-6 | https://pathway.yeastgenome.org/getxml?META:EG11591-MONOMER; Native protein identity context, full source object | supports | LipB native protein. Inspected source scope: MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on . |
| source-7 | https://rest.uniprot.org/uniprotkb/P60720.json; /organism/taxonId; /comments/0; /comments/1; /comments/4; /comments/5/subcellularLocations | supports | Octanoyltransferase. Inspected source scope: UniProt 2026_03; full current entry retrieved 2026-10-11 UTC. Used on lipoate-edge-018, lipoate-edge-022. |
| source-8 | https://rest.uniprot.org/uniprotkb/P60716.json; /organism/taxonId; /comments/0; /comments/1; /comments/5; /comments/2/cofactors; /comments/2/note; /comments/6/subcellularLocations | supports | Lipoyl synthase. Inspected source scope: UniProt 2026_03; full current entry retrieved 2026-10-11 UTC. Used on lipoate-edge-019, lipoate-edge-020, lipoate-edge-021, lipoate-edge-023. |
| source-9 | https://pubmed.ncbi.nlm.nih.gov/12591875/; /resultList/result[id="12591875"]/abstractText | supports | The Escherichia coli lipB gene encodes lipoyl (octanoyl)-acyl carrier protein:protein transferase.. Inspected source scope: 2003; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-018. |
| source-10 | https://pubmed.ncbi.nlm.nih.gov/14700636/; /resultList/result[id="14700636"]/abstractText | supports | Assembly of the covalent linkage between lipoic acid and its cognate enzymes.. Inspected source scope: 2003; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-019. |
| source-11 | https://pubmed.ncbi.nlm.nih.gov/15157071/; /resultList/result[id="15157071"]/abstractText | supports | Lipoyl synthase requires two equivalents of S-adenosyl-L-methionine to synthesize one equivalent of lipoic acid.. Inspected source scope: 2004; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-019. |
| source-12 | https://pubmed.ncbi.nlm.nih.gov/15362861/; /resultList/result[id="15362861"]/abstractText | supports | Escherichia coli lipoyl synthase binds two distinct [4Fe-4S] clusters per polypeptide.. Inspected source scope: 2004; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-021. |
| source-13 | https://pubmed.ncbi.nlm.nih.gov/15642479/; /resultList/result[id="15642479"]/abstractText | supports | Expression, purification, and physical characterization of Escherichia coli lipoyl(octanoyl)transferase.. Inspected source scope: 2005; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-018. |
| source-14 | https://pubmed.ncbi.nlm.nih.gov/15740115/; /resultList/result[id="15740115"]/abstractText | supports | Mechanistic investigations of lipoic acid biosynthesis in Escherichia coli: both sulfur atoms in lipoic acid are contributed by the same lipoyl synthase polypeptide.. Inspected source scope: 2005; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-019. |
| source-15 | https://pubmed.ncbi.nlm.nih.gov/16342964/; /resultList/result[id="16342964"]/abstractText | supports | The reaction of LipB, the octanoyl-[acyl carrier protein]:protein N-octanoyltransferase of lipoic acid synthesis, proceeds through an acyl-enzyme intermediate.. Inspected source scope: 2005; primary indexed abstract inspected via Europe PMC core JSON, not full article; digest covers retained response. Used on lipoate-edge-018. |
| source-16 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/17666 rh:substrates; http://rdf.rhea-db.org/17665_L rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9636; rh:compound http://rdf.rhea-db.org/Compound_9636; http://rdf.rhea-db.org/17666 rh:substrates; http://rdf.rhea-db.org/17665_L rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9752; rh:compound http://rdf.rhea-db.org/Compound_9752; http://rdf.rhea-db.org/17666 rh:products; http://rdf.rhea-db.org/17665_R rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9928; rh:compound http://rdf.rhea-db.org/Compound_9928; http://rdf.rhea-db.org/17666 rh:products; http://rdf.rhea-db.org/17665_R rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9685; rh:compound http://rdf.rhea-db.org/Compound_9685; http://rdf.rhea-db.org/17666 rh:products; http://rdf.rhea-db.org/17665_R rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_3249; rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/17665 rh:directionalReaction http://rdf.rhea-db.org/17666; http://rdf.rhea-db.org/17665_R rh:contains1; http://rdf.rhea-db.org/16585_L rh:contains1; rh:compound http://rdf.rhea-db.org/Compound_9928 | supports | Rhea directional reaction 17666. Inspected source scope: Rhea 142, 2026-09-02; digest covers complete compressed RDF; exact triples identified in edge locators. Used on lipoate-edge-001, lipoate-edge-002, lipoate-edge-003, lipoate-edge-004, lipoate-edge-005, lipoate-edge-018, lipoate-edge-026. |
| source-17 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/16586 rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_14568; rh:compound http://rdf.rhea-db.org/Compound_14568; http://rdf.rhea-db.org/16586 rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_9928; rh:compound http://rdf.rhea-db.org/Compound_9928; http://rdf.rhea-db.org/16586 rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_10000; rh:compound http://rdf.rhea-db.org/Compound_10000; http://rdf.rhea-db.org/16586 rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_6127; rh:compound http://rdf.rhea-db.org/Compound_6127; http://rdf.rhea-db.org/16586 rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains4 http://rdf.rhea-db.org/Participant_16585_compound_3249; rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_14569; rh:compound http://rdf.rhea-db.org/Compound_14569; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_10475; rh:compound http://rdf.rhea-db.org/Compound_10475; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains4 http://rdf.rhea-db.org/Participant_16585_compound_4615; rh:compound http://rdf.rhea-db.org/Compound_4615; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_3841; rh:compound http://rdf.rhea-db.org/Compound_3841; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_2028; rh:compound http://rdf.rhea-db.org/Compound_2028; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_2530; rh:compound http://rdf.rhea-db.org/Compound_2530; http://rdf.rhea-db.org/16586 rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_10001; rh:compound http://rdf.rhea-db.org/Compound_10001 | supports | Rhea directional reaction 16586. Inspected source scope: Rhea 142, 2026-09-02; digest covers complete compressed RDF; exact triples identified in edge locators. Used on lipoate-edge-006, lipoate-edge-007, lipoate-edge-008, lipoate-edge-009, lipoate-edge-010, lipoate-edge-011, lipoate-edge-012, lipoate-edge-013, lipoate-edge-014, lipoate-edge-015, lipoate-edge-016, lipoate-edge-017. |
| expression-context | research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json; e_coli/precise_mg1655; lipA/b0628 and lipB/b0630 searches and dataset response | supports | Direct unchanged canonical client was used after console dependency failure. Exact gene hits only; lipase substrings are false positives, zero module-name hits imply neither membership nor absence. All 45 retained bodies independently rehashed. |
| correction-344 | research/pathway_additions/2026-10-11-nicotine-next/lipoate-evidence-placement-fix.json; edge 024 RXN0-947 source assertion; before 901a9ba9… and after 917b7a97… | supports | Independent review found a copied LipA-only redox caveat on LipB evidence. Author removed it under GitHub issue #344; exact raw RXN0-947/RHEA:17666 bridge and unchanged LipA edge 025 were rechecked. |
| final-gates | research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json; Final actual command receipts and retained log hashes | supports | Final required repository gates delegated to root; actual terminal receipts and log bytes inspected separately from scientific source assessment. |
| authority-final | research/pathway_additions/2026-10-11-nicotine-next/authority-integration.json; New authority entries, source bodies, labels and baseline preservation | supports | All 24 target identifiers and labels independently resolve under current canonical authorities. Independent base-to-current JSON comparison confirms every baseline term and source metadata entry is preserved unchanged. |
| generated-audit | research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json; Lipoate SVG endpoints/evidence and published/CLI KGX projections | supports | Programmatic graph and evidence-preservation checks passed, with no interactive browser claim. |

## Limits And Additional Notes

- Rhea and native MetaCyc formal Fe/ferredoxin/hydron conventions disagree; no measured physiological electron balance is claimed.
- Primary sources were inspected as indexed abstracts, not full articles; source metadata and claims preserve that limit.
- LipB monomer/trimer annotation is experimentally referenced by UniProt; the abstract does not independently describe that comparison. LipA monomer/dimer alternatives remain unresolved.
- Both cytoplasm annotations are HAMAP-inferred, not inspected fractionation experiments.
- Reviewed protein taxon K-12 and native MG1655 identity are distinguished from more general E. coli wording in primary abstracts.
- Expression context is computational; absent module-name or accession hits are not biological absence.
- Ignored/hidden search covers accessible worktree; original Documents checkout is OS-inaccessible.
- The inspected generated page pages/records/MetaCyc_PWY0-501.html is owned by the maintained target YAML and rendered by src/pathwaymech/cli.py render_site; any correction belongs in those maintained owners, not the page.
- Issue #344 was identified and fixed before any immutable review bundle existed. Its actual original/fixed hashes and source evidence are retained in the audit and assessments; no terminal resolved finding with fabricated predecessor is created.
- Full gate commands were executed by root and actual receipts/logs were inspected by this reviewer. No broad tests were duplicated.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T024322Z-lipoate-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of lipoate biosynthesis and incorporation I
started_at: '2026-10-11T02:30:20Z'
finished_at: '2026-10-11T02:43:22.914657Z'
reviewer:
  identity: Codex /root/pathway_authority_cache
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Did not author or edit lipoate YAML or author dossiers. Authored
    separate Moco record; root authored lipoate and integrates shared authorities/gates.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'All 26 edges and 40 evidence blocks support the complete native LipB–LipA
  route with explicit strain, annotation and formal-redox limits. One minor evidence-placement
  finding was filed as issue #344 and independently verified corrected before this
  first immutable review. No open finding remains; final required gates pass.'
source:
  git_revision: e3bceba7613eb0525af3ff76ef32520201ae9f33
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 296ab1a206afa3aa9b487eae7f5f8d836c09001a4ce9ee8016c36abe198cdc0d
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: 563ace71ecbab2ccdf71e353813afe89988024b9f46288611cbfb97db726c67f
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 88dfc909cc4efc39e0c4c05a7c4d721ec6f2e68d4d4f431df1f1d4c4307d80fe
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: c5efa10d14da146c39262662f330c6a39be9be71c5072dd619d644bc2724be6c
    role: context
  - path: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
    sha256: 917b7a976e9fad4d84e43e5497105ac58670ccd419f09dc147aa8ebd93fc2e2e
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 3af37b2e92b0103da74bc462bedda1021c6bd262d3da13c030eb47344d08b61f
    role: context
  - path: docs/record-review-profile.md
    sha256: a3d4b48de5f227515f9b5de12dd172cd1eb626068235b2b2e58bc4f6a5ee567d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: pages/records/MetaCyc_PWY0-501.html
    sha256: 01c772d8cbe12dde6eedd2da746fb9df2dacfa74d3176cf000ed30b31fd75501
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-integration.json
    sha256: 508115133210b4b274705562e606b38ce33b774d0b26f9779dc1cd539eff34f1
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-protein-crosscheck.json
    sha256: 7865b01494836dd3e6b104bc804cc013cdefd424f6ee2fcbcdbd3661fcb571eb
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-source-inspection.json
    sha256: 6819051b3cde54f86e72f75c4ddcf7a576a5d56334b32a338125fa211fb4b216
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/baseline-preservation.json
    sha256: 1759ef38d27e253e1f35206ac7a5d0269ff0d8e1325ceb710b58676624229492
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/browser-availability.json
    sha256: 7dd0d8c23add2134ecf6331ccd914d32bcc071e731387a7b76548cf72bce2242
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json
    sha256: 2012413903397cabd2554fcd7a80841f8db8e3e6c059dc2d2d4f390860d7720a
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
    sha256: 44fe95b9cef24af8f4ba69d7b845142d40e63e1ed42ac29db6e8a26361c0c0a9
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-parser-replay.json
    sha256: e0615d4d3eade07658e352e572426479dac155c525c1cf460daaa6846f601f91
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-runner-availability.json
    sha256: f996c636a02f9e017b5831003fa27d0577576dfe355fa9a5097f59644c880698
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-source-manifest.json
    sha256: 4ae60106c78976dcf8396ec0646e69f74d70ea70c018659430223d37e66a9af6
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
    sha256: 33ca08ff4c31d5f2c03c0b3732b731e2b9d64ad583066f4360cfcddcf5797975
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-curation.md
    sha256: aca6eecfcd348a355d6eb32429b9d65903f181306cc037ad8d0a44ee7767c47c
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-dedup.json
    sha256: 23459102a9a2aa183c47bbf74c1a72f37383f05e42075c7c6b02691ec46d5b8d
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-evidence-placement-fix.json
    sha256: f1110e8fdaffa16a1d236a5c69f4a91b80832a3800fe856acd1a6ddaa9a91ec9
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-go-candidates.json
    sha256: 058804b2f7028a6db68a94c4d7d3bb364bd32e24d23e1ff06cb28ffae3201b8a
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-independent-review-audit.json
    sha256: 6e4d19c92849ee0d492073454c183b9e49d81564552c8d0c1c4a29c5432675b6
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-pathbank-projection.json
    sha256: c67c2e8ae5dc7cf3cd8e8295ef2bcd0d5f38a0c61908694df721dade98aba189
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-replay.py
    sha256: 76229c80c968a44d46cfe05d3f9b270e2f9e35b687e0f5e92b33ab7c03b53230
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-rhea-projection.json
    sha256: a5aa1e1b1a75df00be7a3b92c7451dd0e8b20819071ea7377951cc0b5be8877e
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-source-manifest.json
    sha256: be384adef84b3a46b1f51806521a01f16a6b8f4b6b71530f61ae371f31e6471d
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/lipoate-validation.json
    sha256: 2fdcfbf6ced4db93aae4089cde8aea621d49dd58660e58f05f66e710c1e3af94
    role: context
  - path: src/pathwaymech/cli.py
    sha256: ab045fb947cfb93323886079abc2e7632d292679b2866fa7a0e39719310cc738
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
targets:
- target_id: MetaCyc:PWY0-501
  path: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
  label: lipoate biosynthesis and incorporation I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
    role: maintained_yaml
  record_class: Pathway
scope:
  description: Full single-target review of all local nodes, 26 edges, 40 evidence
    blocks and 17 references.
  selection: Explicit parent assignment to a reviewer who did not author or edit target;
    governed inspect before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-501
  exclusions:
  - target: Other cohort or baseline pathways
    reason: Outside this independent scientific target; adjacent routes read only
      to establish boundary.
  - target: Wet-lab and interactive browser validation
    reason: Neither performed nor claimed; publication audit is programmatic.
checks:
- check_id: inspect-initial
  name: Governed inspect before scientific assessment
  status: passed
  required: true
  summary: Actual initial inspect captured 901a9ba9… before full-record assessment.
    Changed evidence later re-inspected explicitly.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - target
  - correction-344
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-nicotine-next-evidence/lipoate-review-targets.yaml
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input docs/CAUSAL_GRAPHS.md --input conf/identifier_policy.yaml --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json
  exit_code: 0
  expected_exit_code: 0
- check_id: independent-source-replay
  name: Independent complete raw source replay
  status: passed
  required: true
  summary: Fresh full RDF, all 17 sides/coefficient locators and two complete balances,
    including both reactive parts of carrier 14568; native identity/order/assembly
    and all 17 record reference digests passed.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - independent-audit
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache .venv/bin/python
    /private/tmp/pathwaymech-nicotine-next-evidence/lipoate-independent-replay.py
  exit_code: 0
  expected_exit_code: 0
- check_id: context-body-check
  name: Independent retained iModulonDB body rehash
  status: passed
  required: false
  summary: All 45 exact retained API bodies match manifest; dataset coverage and relevant
    six query projections inspected. This is rehash/review of root acquisition, not
    a fresh network call or independent parser replay.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - expression-context
  - independent-audit
  command: .venv/bin/python - (read canonical retained context and SHA-256 all 45
    preserved API bodies)
  exit_code: 0
  expected_exit_code: 0
- check_id: superseded-1
  name: just validate
  status: failed
  required: false
  summary: Superseded initial validation failed on stale pages after wording corrections;
    final2 validation below checks rerendered frozen inputs.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-2
  name: just render-pages
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-3
  name: just lint
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-4
  name: git diff --check
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected.
  target_ids:
  - MetaCyc:PWY0-501
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-5
  name: just check-identifiers
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-6
  name: just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-7
  name: just validate
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected. 184 records, 9977 evidence blocks, 272 history records, identifiers,
    strict schemas, documentation, sources and current pages pass.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-8
  name: just test
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected. 1048 passed, 3 skipped, 3 warnings in 594.56 seconds. Full suite started
    before final nicotine/lipoate evidence wording fixes and completed after them;
    implementation and tests did not change. Final2 full corpus QC separately checks
    frozen data and regenerated pages.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: final-9
  name: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  status: passed
  required: true
  summary: Root executed command; actual terminal receipt and log bytes independently
    inspected.
  target_ids:
  - MetaCyc:PWY0-501
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - final-gates
- check_id: reviewer-page-initial
  name: Initial reviewer page-anchor spot check
  status: failed
  required: false
  summary: The exact corrected assertion passed, but this ad hoc check incorrectly
    expected YAML edge IDs to be literal HTML IDs. The renderer uses documented ordinal
    mechanism-edge-N anchors; no record or page change was needed. Superseded by the
    corrected check below.
  target_ids:
  - MetaCyc:PWY0-501
  command: .venv/bin/python - (assert every YAML edge ID is a substring of rendered
    HTML)
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - generated-audit
- check_id: reviewer-page-final
  name: Corrected reviewer page-anchor and assertion spot check
  status: passed
  required: true
  summary: All 26 rendered mechanism-edge-N anchors are present. Exact corrected LipB
    source assertion is present and the copied LipA clause is absent. Full graph evidence
    matching is independently covered by the root artifact audit.
  target_ids:
  - MetaCyc:PWY0-501
  command: .venv/bin/python - (check mechanism-edge-1 through mechanism-edge-26 and
    exact corrected assertion)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - generated-audit
  - correction-344
evidence:
- evidence_id: target
  kind: record_content
  reference: data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml
  locator: Entire YAML, all 26 edges and 40 evidence blocks
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: Exact complete LipB–LipA route, with source-version chemistry and evidence
    limits retained.
  snapshot_sha256: 917b7a976e9fad4d84e43e5497105ac58670ccd419f09dc147aa8ebd93fc2e2e
- evidence_id: independent-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/lipoate-independent-review-audit.json
  locator: Full independent raw-RDF replay, every edge scientific assessment and genuine
    before/after fix evidence
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Independent full source replay session 6049 exited 0 on corrected target:
    17 sides, 2 balances, 17 reference hashes, exact native boundary/order/assembly.
    Deterministic checks supplement source reading.'
  snapshot_sha256: 6e4d19c92849ee0d492073454c183b9e49d81564552c8d0c1c4a29c5432675b6
- evidence_id: identity-search
  kind: search
  reference: Accessible current worktree and retained prior dispositions
  locator: Exact MetaCyc/PathBank/Rhea identifiers, labels and related GO definitions
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: No baseline exact pathway found; current generated/authority surfaces and
    frozen prior leads are not duplicates.
  search_scope: Entire accessible worktree including hidden/ignored files except Git
    internals and venv; original Documents checkout remains OS-inaccessible.
  snapshot_sha256: 91ce7cd31a18857f7de2e7266a62877cecd39f5206ee36fc333fe00929536f73
- evidence_id: source-1
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-501
  locator: Pathway[@frameid="PWY0-501"]/reaction-list; reaction-layout; Pathway[@frameid="PWY0-501"]/reaction-ordering;
    reaction-layout
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'lipoate biosynthesis and incorporation I. Inspected source scope: MetaCyc
    22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-024,
    lipoate-edge-025, lipoate-edge-026.'
  snapshot_sha256: a94cb0070944764fa0d8140597ce9c8f9cfa2bd4667772ed95d47e1dfa18343b
- evidence_id: source-2
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:RXN0-947
  locator: Reaction[@frameid="RXN0-947"]/dblink[dblink-db="RHEA"]
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'octanoyl transfer. Inspected source scope: MetaCyc 22.5; complete native
    XML retrieved 2026-10-11 UTC. Used on lipoate-edge-024.'
  snapshot_sha256: 5771ba18461be457ae5d89f0ef60e651c2fc7a49a4b94c9baaae88fcfe6ebd7b
- evidence_id: source-3
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:RXN0-949
  locator: Reaction[@frameid="RXN0-949"]/enzymatic-reaction; dblink[dblink-db="RHEA"];
    left; right; Reaction[@frameid="RXN0-949"]/dblink[dblink-db="RHEA"]
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'lipoyl synthase reaction; native redox convention. Inspected source scope:
    MetaCyc 22.5; complete native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-019,
    lipoate-edge-025.'
  snapshot_sha256: 6cf86334548c16e9c79ce3baac56d57b97826812a1f9c450b4bcb289df1ee383
- evidence_id: source-4
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:CPLX0-782
  locator: Protein[@frameid="CPLX0-782"]/component/Protein; component/coefficient
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'lipoyl synthase native dimer. Inspected source scope: MetaCyc 22.5; complete
    native XML retrieved 2026-10-11 UTC. Used on lipoate-edge-020.'
  snapshot_sha256: c518f4e6a9c35e933d20bea27eee5c9f8c07bb0165d81b8383f0e9e2b25f8e0f
- evidence_id: source-5
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:EG11306-MONOMER
  locator: Protein[@frameid="EG11306-MONOMER"]/dblink[dblink-db="UNIPROT"]; species/Organism
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'LipA native subunit. Inspected source scope: MetaCyc 22.5; complete native
    XML retrieved 2026-10-11 UTC. Used on lipoate-edge-020.'
  snapshot_sha256: 9c6f8441af500be9320be4a4c7c579157f8ebf3f37853a8c8e8025dc8080b634
- evidence_id: source-6
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:EG11591-MONOMER
  locator: Native protein identity context, full source object
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'LipB native protein. Inspected source scope: MetaCyc 22.5; complete native
    XML retrieved 2026-10-11 UTC. Used on .'
  snapshot_sha256: 6aa4842a5e144cf99e5e883cfdd8f6228f1ec81474347fa1e188e8da4857f24c
- evidence_id: source-7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P60720.json
  locator: /organism/taxonId; /comments/0; /comments/1; /comments/4; /comments/5/subcellularLocations
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Octanoyltransferase. Inspected source scope: UniProt 2026_03; full current
    entry retrieved 2026-10-11 UTC. Used on lipoate-edge-018, lipoate-edge-022.'
  snapshot_sha256: ad34e89fdedc2381f53895fbb1f7c2eaee6a3ca20e1899f97eab0a5bdc3012ca
- evidence_id: source-8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P60716.json
  locator: /organism/taxonId; /comments/0; /comments/1; /comments/5; /comments/2/cofactors;
    /comments/2/note; /comments/6/subcellularLocations
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Lipoyl synthase. Inspected source scope: UniProt 2026_03; full current
    entry retrieved 2026-10-11 UTC. Used on lipoate-edge-019, lipoate-edge-020, lipoate-edge-021,
    lipoate-edge-023.'
  snapshot_sha256: c50683fac74d9e13ccfb51dd3e8b5c8e5e80752e3efa3287a921b27561473905
- evidence_id: source-9
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/12591875/
  locator: /resultList/result[id="12591875"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'The Escherichia coli lipB gene encodes lipoyl (octanoyl)-acyl carrier
    protein:protein transferase.. Inspected source scope: 2003; primary indexed abstract
    inspected via Europe PMC core JSON, not full article; digest covers retained response.
    Used on lipoate-edge-018.'
  snapshot_sha256: a472b6d22088bb8303fa27ab19f3d4e4c8a1e3030a21e8b36f1fba0d7e702da7
- evidence_id: source-10
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/14700636/
  locator: /resultList/result[id="14700636"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Assembly of the covalent linkage between lipoic acid and its cognate enzymes..
    Inspected source scope: 2003; primary indexed abstract inspected via Europe PMC
    core JSON, not full article; digest covers retained response. Used on lipoate-edge-019.'
  snapshot_sha256: e11ccc42fbf832f87e65fb77cbd34056dfc7a35de461fc14910ee27be68aac6b
- evidence_id: source-11
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15157071/
  locator: /resultList/result[id="15157071"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Lipoyl synthase requires two equivalents of S-adenosyl-L-methionine to
    synthesize one equivalent of lipoic acid.. Inspected source scope: 2004; primary
    indexed abstract inspected via Europe PMC core JSON, not full article; digest
    covers retained response. Used on lipoate-edge-019.'
  snapshot_sha256: 1b3e264d65e394390d51627c27424f8a262d4e854e106d8e09fa420766a5a536
- evidence_id: source-12
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15362861/
  locator: /resultList/result[id="15362861"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Escherichia coli lipoyl synthase binds two distinct [4Fe-4S] clusters
    per polypeptide.. Inspected source scope: 2004; primary indexed abstract inspected
    via Europe PMC core JSON, not full article; digest covers retained response. Used
    on lipoate-edge-021.'
  snapshot_sha256: a67a361c544956852f079e4ed3471c9ebce25db4cc65002efe94d2cdf090da3c
- evidence_id: source-13
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15642479/
  locator: /resultList/result[id="15642479"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Expression, purification, and physical characterization of Escherichia
    coli lipoyl(octanoyl)transferase.. Inspected source scope: 2005; primary indexed
    abstract inspected via Europe PMC core JSON, not full article; digest covers retained
    response. Used on lipoate-edge-018.'
  snapshot_sha256: feeb415dc45af7e45640ef7f025ac748d60d8d925c37538fcb81a5d502fa15dd
- evidence_id: source-14
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15740115/
  locator: /resultList/result[id="15740115"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Mechanistic investigations of lipoic acid biosynthesis in Escherichia
    coli: both sulfur atoms in lipoic acid are contributed by the same lipoyl synthase
    polypeptide.. Inspected source scope: 2005; primary indexed abstract inspected
    via Europe PMC core JSON, not full article; digest covers retained response. Used
    on lipoate-edge-019.'
  snapshot_sha256: 47015d23a8fc45f71d702a6e14814045ff4301c9a0bc8c1bbe2906406a12d735
- evidence_id: source-15
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/16342964/
  locator: /resultList/result[id="16342964"]/abstractText
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'The reaction of LipB, the octanoyl-[acyl carrier protein]:protein N-octanoyltransferase
    of lipoic acid synthesis, proceeds through an acyl-enzyme intermediate.. Inspected
    source scope: 2005; primary indexed abstract inspected via Europe PMC core JSON,
    not full article; digest covers retained response. Used on lipoate-edge-018.'
  snapshot_sha256: b33094913a12253642bb60d6ace6773250732e89ef69285b05e18b17c4f8335c
- evidence_id: source-16
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/17666 rh:substrates; http://rdf.rhea-db.org/17665_L
    rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9636; rh:compound
    http://rdf.rhea-db.org/Compound_9636; http://rdf.rhea-db.org/17666 rh:substrates;
    http://rdf.rhea-db.org/17665_L rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9752;
    rh:compound http://rdf.rhea-db.org/Compound_9752; http://rdf.rhea-db.org/17666
    rh:products; http://rdf.rhea-db.org/17665_R rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9928;
    rh:compound http://rdf.rhea-db.org/Compound_9928; http://rdf.rhea-db.org/17666
    rh:products; http://rdf.rhea-db.org/17665_R rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_9685;
    rh:compound http://rdf.rhea-db.org/Compound_9685; http://rdf.rhea-db.org/17666
    rh:products; http://rdf.rhea-db.org/17665_R rh:contains1 http://rdf.rhea-db.org/Participant_17665_compound_3249;
    rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/17665
    rh:directionalReaction http://rdf.rhea-db.org/17666; http://rdf.rhea-db.org/17665_R
    rh:contains1; http://rdf.rhea-db.org/16585_L rh:contains1; rh:compound http://rdf.rhea-db.org/Compound_9928
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Rhea directional reaction 17666. Inspected source scope: Rhea 142, 2026-09-02;
    digest covers complete compressed RDF; exact triples identified in edge locators.
    Used on lipoate-edge-001, lipoate-edge-002, lipoate-edge-003, lipoate-edge-004,
    lipoate-edge-005, lipoate-edge-018, lipoate-edge-026.'
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-17
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/16586 rh:substrates; http://rdf.rhea-db.org/16585_L
    rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_14568; rh:compound
    http://rdf.rhea-db.org/Compound_14568; http://rdf.rhea-db.org/16586 rh:substrates;
    http://rdf.rhea-db.org/16585_L rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_9928;
    rh:compound http://rdf.rhea-db.org/Compound_9928; http://rdf.rhea-db.org/16586
    rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_10000;
    rh:compound http://rdf.rhea-db.org/Compound_10000; http://rdf.rhea-db.org/16586
    rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_6127;
    rh:compound http://rdf.rhea-db.org/Compound_6127; http://rdf.rhea-db.org/16586
    rh:substrates; http://rdf.rhea-db.org/16585_L rh:contains4 http://rdf.rhea-db.org/Participant_16585_compound_3249;
    rh:compound http://rdf.rhea-db.org/Compound_3249; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_14569;
    rh:compound http://rdf.rhea-db.org/Compound_14569; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains1 http://rdf.rhea-db.org/Participant_16585_compound_10475;
    rh:compound http://rdf.rhea-db.org/Compound_10475; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains4 http://rdf.rhea-db.org/Participant_16585_compound_4615;
    rh:compound http://rdf.rhea-db.org/Compound_4615; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_3841;
    rh:compound http://rdf.rhea-db.org/Compound_3841; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_2028;
    rh:compound http://rdf.rhea-db.org/Compound_2028; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_2530;
    rh:compound http://rdf.rhea-db.org/Compound_2530; http://rdf.rhea-db.org/16586
    rh:products; http://rdf.rhea-db.org/16585_R rh:contains2 http://rdf.rhea-db.org/Participant_16585_compound_10001;
    rh:compound http://rdf.rhea-db.org/Compound_10001
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Rhea directional reaction 16586. Inspected source scope: Rhea 142, 2026-09-02;
    digest covers complete compressed RDF; exact triples identified in edge locators.
    Used on lipoate-edge-006, lipoate-edge-007, lipoate-edge-008, lipoate-edge-009,
    lipoate-edge-010, lipoate-edge-011, lipoate-edge-012, lipoate-edge-013, lipoate-edge-014,
    lipoate-edge-015, lipoate-edge-016, lipoate-edge-017.'
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: expression-context
  kind: database
  reference: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
  locator: e_coli/precise_mg1655; lipA/b0628 and lipB/b0630 searches and dataset response
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: Direct unchanged canonical client was used after console dependency failure.
    Exact gene hits only; lipase substrings are false positives, zero module-name
    hits imply neither membership nor absence. All 45 retained bodies independently
    rehashed.
  snapshot_sha256: 44fe95b9cef24af8f4ba69d7b845142d40e63e1ed42ac29db6e8a26361c0c0a9
- evidence_id: correction-344
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/lipoate-evidence-placement-fix.json
  locator: edge 024 RXN0-947 source assertion; before 901a9ba9… and after 917b7a97…
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: 'Independent review found a copied LipA-only redox caveat on LipB evidence.
    Author removed it under GitHub issue #344; exact raw RXN0-947/RHEA:17666 bridge
    and unchanged LipA edge 025 were rechecked.'
  snapshot_sha256: f1110e8fdaffa16a1d236a5c69f4a91b80832a3800fe856acd1a6ddaa9a91ec9
- evidence_id: final-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
  locator: Final actual command receipts and retained log hashes
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: Final required repository gates delegated to root; actual terminal receipts
    and log bytes inspected separately from scientific source assessment.
  snapshot_sha256: 33ca08ff4c31d5f2c03c0b3732b731e2b9d64ad583066f4360cfcddcf5797975
- evidence_id: authority-final
  kind: authority
  reference: research/pathway_additions/2026-10-11-nicotine-next/authority-integration.json
  locator: New authority entries, source bodies, labels and baseline preservation
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: All 24 target identifiers and labels independently resolve under current
    canonical authorities. Independent base-to-current JSON comparison confirms every
    baseline term and source metadata entry is preserved unchanged.
  snapshot_sha256: 508115133210b4b274705562e606b38ce33b774d0b26f9779dc1cd539eff34f1
- evidence_id: generated-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json
  locator: Lipoate SVG endpoints/evidence and published/CLI KGX projections
  accessed_at: '2026-10-11T02:43:22.914657Z'
  support: supports
  summary: Programmatic graph and evidence-preservation checks passed, with no interactive
    browser claim.
  snapshot_sha256: 2012413903397cabd2554fcd7a80841f8db8e3e6c059dc2d2d4f390860d7720a
assessments:
- assessment_id: identity
  area: identity
  topic: Exact complete two-step boundary
  outcome: supported
  summary: MetaCyc PWY0-501 explicitly consists of native RXN0-947→RXN0-949, octanoyl-ACP
    transfer then protein-bound sulfur insertion. Broader lipoate biosynthesis/lipoylation
    GO terms and LplA salvage are not substituted. The PathBank acetyl-ACP label is
    an inspected source error.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - target
  - identity-search
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
- assessment_id: edges-1
  area: grounding
  topic: Chemical sides, stereochemistry, whole carrier states and source conflict
  outcome: supported
  summary: All 17 source sides/coefficient locators and both equations independently
    verified. Carrier 14568 contributes both native reactive parts. Rhea Fe(III),
    oxidized-to-reduced ferredoxin and four protons differ from native Fe(II), reduced-to-oxidized
    ferredoxin and six protons; the record explicitly preserves the disagreement rather
    than claiming measured physiology. Protein-bound (R)-dihydrolipoyl endpoint and
    shared octanoyl state are exact native boundary, not free lipoate.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - source-9
  - source-10
  - source-11
  - source-12
  - source-13
  - source-14
  - source-15
  - source-16
  - source-17
  dimensions:
  - name: source-object
    value: RHEA:17666 and RHEA:16586, full Rhea release 142; MetaCyc RXN0-947 and
      RXN0-949, release 22.5
    definition: Exact chemical projection and explicit versioned redox disagreement,
      with every native Rhea side retained.
    evidence_ids:
    - independent-audit
    - source-1
    - source-2
    - source-3
    - source-4
    - source-5
    - source-6
    - source-7
    - source-8
    - source-9
    - source-10
    - source-11
    - source-12
    - source-13
    - source-14
    - source-15
    - source-16
    - source-17
- assessment_id: edges-2
  area: evidence
  topic: Catalysis, monomer/complex roles and primary evidence limits
  outcome: supported
  summary: K-12 LipB FUNCTION has direct experimental citations, catalytic Rhea annotation
    is HAMAP-only. Three inspected primary abstracts support octanoyl-ACP transfer,
    true initiation and C169 acyl-enzyme mechanism; reverse transfer is preserved.
    Active monomer/homotrimer remains UniProt experimental annotation, not claimed
    visible in abstract. Native LipA dimer catalyst and exact Rhea family agree on
    core protein-bound sulfur insertion. Three inspected primary abstracts support
    target-bound substrate, two SAM cleavage and same-polypeptide sulfur origin. Later
    result qualifies the earlier two-polypeptide interpretation. No physiological
    proof is claimed for formal Fe/ferredoxin bookkeeping.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - source-9
  - source-10
  - source-11
  - source-12
  - source-13
  - source-14
  - source-15
  - source-16
  - source-17
- assessment_id: edges-3
  area: evidence
  topic: Assembly, Fe-S cofactor and inferred cytoplasm
  outcome: supported
  summary: Native complex has two EG11306 monomers, explicitly cross-referenced to
    P60716/MG1655. UniProt allows monomer or dimer without an explicit subunit evidence
    code, preserved as alternative rather than unique active state. Current cofactor
    annotation and PMID15362861 abstract independently support two distinct Fe-S clusters
    per polypeptide. Broad ChEBI class and precise formal Rhea carrier states remain
    separate. LipB cytoplasm is HAMAP ECO0000255; direct UniProt GO0005737 cross-reference
    also verified. No experimental localization claim. LipA cytoplasm is HAMAP ECO0000255;
    direct UniProt GO0005737 cross-reference also verified. No experimental localization
    claim.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - source-9
  - source-10
  - source-11
  - source-12
  - source-13
  - source-14
  - source-15
  - source-16
  - source-17
  dimensions:
  - name: component-role
    value: LipB active monomer role; native LipA dimer with monomer/dimer annotation
      alternatives; whole carrier states distinct from bound Fe-S cofactor class
    definition: Protein activity, assembly membership, cofactor binding and reaction
      carrier chemistry are separately supported assertions.
    evidence_ids:
    - independent-audit
    - source-1
    - source-2
    - source-3
    - source-4
    - source-5
    - source-6
    - source-7
    - source-8
    - source-9
    - source-10
    - source-11
    - source-12
    - source-13
    - source-14
    - source-15
    - source-16
    - source-17
- assessment_id: edges-4
  area: evidence
  topic: Exact native membership, corrected evidence placement and order
  outcome: supported
  summary: Native first route member RXN0-947 unifies17666; irrelevant LipA clause
    was removed under344 and correction independently checked. Native second member
    RXN0-949 unifies16586 at core chemistry level; formal redox discrepancy is not
    concealed. Explicit native reaction ordering plus exact shared RHEA-COMP9928 support
    LipB output feeding LipA. No extra free-lipoate or salvage step is appended.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - source-9
  - source-10
  - source-11
  - source-12
  - source-13
  - source-14
  - source-15
  - source-16
  - source-17
  - correction-344
- assessment_id: scope
  area: scope
  topic: K-12 annotation versus experimental strain detail
  outcome: supported
  summary: Both reviewed protein entries identify K-12. Native subunit taxonomy is
    MG1655. Primary abstracts generally say E. coli and do not independently establish
    every substrain. LipB experimental function/active-oligomer annotation is distinct
    from HAMAP catalytic annotation. LipA monomer/dimer alternative has no explicit
    evidence code.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - independent-audit
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - source-9
  - source-10
  - source-11
  - source-12
  - source-13
  - source-14
  - source-15
  - source-16
  - source-17
  dimensions:
  - name: taxon
    value: NCBITaxon:83333 (E. coli K-12); native assembly context NCBITaxon:511145
      (MG1655)
    definition: Reviewed protein identity and narrower native subunit source are distinct
      from unspecified E. coli primary assays.
    evidence_ids:
    - independent-audit
    - source-1
    - source-2
    - source-3
    - source-4
    - source-5
    - source-6
    - source-7
    - source-8
    - source-9
    - source-10
    - source-11
    - source-12
    - source-13
    - source-14
    - source-15
    - source-16
    - source-17
  - name: evidence-tier
    value: Primary abstracts; reviewed direct and HAMAP-inferred annotations; native
      curated assembly objects
    definition: Experimental function, database assembly assertions and inferred localization
      retain their separate evidence grades.
    evidence_ids:
    - independent-audit
    - source-1
    - source-2
    - source-3
    - source-4
    - source-5
    - source-6
    - source-7
    - source-8
    - source-9
    - source-10
    - source-11
    - source-12
    - source-13
    - source-14
    - source-15
    - source-16
    - source-17
- assessment_id: expression
  area: evidence
  topic: Structured expression context
  outcome: supported
  summary: Exact lipA/b0628 and lipB/b0630 matches are bounded computational context.
    Substring lipase hits and missing protein-accession matches are not biological
    conclusions. No useful module-name hit required component summarization.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - expression-context
  - independent-audit
- assessment_id: gates
  area: schema
  topic: Final authorities, gates and generated artifacts
  outcome: supported
  summary: Final source input hashes were rechecked after explicit changed-input review.
    Full required gates and structural publication audit pass; they do not replace
    the scientific source assessment.
  target_ids:
  - MetaCyc:PWY0-501
  evidence_ids:
  - final-gates
  - authority-final
  - generated-audit
findings: []
actions: []
limitations:
- Rhea and native MetaCyc formal Fe/ferredoxin/hydron conventions disagree; no measured
  physiological electron balance is claimed.
- Primary sources were inspected as indexed abstracts, not full articles; source metadata
  and claims preserve that limit.
- LipB monomer/trimer annotation is experimentally referenced by UniProt; the abstract
  does not independently describe that comparison. LipA monomer/dimer alternatives
  remain unresolved.
- Both cytoplasm annotations are HAMAP-inferred, not inspected fractionation experiments.
- Reviewed protein taxon K-12 and native MG1655 identity are distinguished from more
  general E. coli wording in primary abstracts.
- Expression context is computational; absent module-name or accession hits are not
  biological absence.
- Ignored/hidden search covers accessible worktree; original Documents checkout is
  OS-inaccessible.
notes:
- The inspected generated page pages/records/MetaCyc_PWY0-501.html is owned by the
  maintained target YAML and rendered by src/pathwaymech/cli.py render_site; any correction
  belongs in those maintained owners, not the page.
- 'Issue #344 was identified and fixed before any immutable review bundle existed.
  Its actual original/fixed hashes and source evidence are retained in the audit and
  assessments; no terminal resolved finding with fabricated predecessor is created.'
- Full gate commands were executed by root and actual receipts/logs were inspected
  by this reviewer. No broad tests were duplicated.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/344
```
