# Independent scientific review of adenosylcobalamin nucleotide-loop assembly

- Review: 20261011T002023Z-nucleotide-loop-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T00:11:48Z
- Finished UTC: 2026-10-11T00:20:23Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact three-reaction PWY-5509 route is supported across all 22 named nodes,25 edges,45 evidence blocks and21 references. One minor edge-local source-attribution defect was found before freeze, filed as issue329 and corrected with separate native MetaCyc and Rhea evidence. Independent source replay confirms the correction; no open corrective finding remains. Similarity-qualified annotations, cross-species terminal-step physiology and the engineered scope of the 2023 MG1655 study remain explicit.

## Scope And Provenance

Full independent scientific assessment of one maintained target, its entire local graph and references.

Selection: Exact assigned MetaCyc:PWY-5509 maintained YAML.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 83c2c597b300b8c716a32b96b6cbe8fb2a6ccb0a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5509 | data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml | maintained | adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial governed capture | passed | False | MetaCyc:PWY-5509 | Actual exit0 captured initial target6ffc41e8827aab8bd22242b568233e1c0361e18104e31469188ec68d5937afec before assessment. The temporary target kind was initially pathway; inspect accepted it, and it was corrected to governed maintained for final capture before any bundle validation/save. |
| Independent issuing-source replay | passed | False | MetaCyc:PWY-5509 | Actual exit0:14 exact chemical-side occurrences, coefficients1, three master-relative directions, three elemental/charge balances from Rhea compound fields,21 non-pathway issuing identities plus exact pathway identity, native assembly membership and21 reference digest/access dispositions. |
| Independent raw-body and target freeze verification | passed | False | MetaCyc:PWY-5509 | All 27 preserved manifest source bodies independently rehashed. Current frozen target is byte-identical to the first post-fix8453146 snapshot. |
| Ignored-inclusive prior review search | passed | False | MetaCyc:PWY-5509 | Actual rg no-match status1 was treated as an ordinary successful bounded absence search by the reviewer wrapper, which exited0. Both hidden and ignored review/report files were included; no prior exact-target bundle found. |
| Independent preserved-authority comparison | passed | False | MetaCyc:PWY-5509 | All 121 prior manifest inputs,1331 ontology terms/4 source-metadata entries and1633 source terms/105 metadata entries retain identical values. Final141 inputs,1367 ontology terms and1658 source terms/112 metadata entries. |
| Final governed changed-input capture | passed | False | MetaCyc:PWY-5509 | Actual exit0 captures the final target, re-inspected receipts, authority snapshots and rendered page. The initial source-attribution observation is retained in evidence rather than silently replaced. |
| Integrated just render-pages | passed | False | MetaCyc:PWY-5509 | 172 records rendered. Log /private/tmp/pathwaymech-salvage-render.log; SHA256 f1ab92d786152e153465f8768b42742e6ce38d0f78a137f6156960079ea21337. |
| Integrated just validate | passed | True | MetaCyc:PWY-5509 | 172 native and closed-schema records; exact identities;9047 evidence blocks;30sources;255history records;6documentation files and current pages passed. Log /private/tmp/pathwaymech-salvage-validate.log; SHA256 21db8649e8785667ca778d3c461b3af075d79129d2ba8ed759607bdb06a302cd. |
| Integrated just test | passed | True | MetaCyc:PWY-5509 | 1048 passed,3 skipped,3 upstream warnings in215.42seconds. Log /private/tmp/pathwaymech-salvage-test.log; SHA256 1b74817e756745dc202a910358835c45b2bcd02ee31db0b9a99d3b3f6d24165c. |
| Integrated just lint | passed | True | MetaCyc:PWY-5509 | All Ruff checks passed after helper formatting and exact four-column zip. Log /private/tmp/pathwaymech-salvage-lint-final.log; SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41. |
| Integrated just check-identifiers | passed | False | MetaCyc:PWY-5509 | All172 records resolve against authority snapshots. Log /private/tmp/pathwaymech-salvage-identifiers.log; SHA256 a0122812a006451b9885112bb7fd0ca7b653f43a1df2ee99361e04c7e33c30e2. |
| Integrated just vendored-check | passed | False | MetaCyc:PWY-5509 | All22 governed artifacts match pinned CLAW revision. Log /private/tmp/pathwaymech-salvage-vendored-final.log; SHA256 b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6. |
| Integrated just kgx-export --output-dir /private/tmp/pathwaymech-salvage-kgx | passed | False | MetaCyc:PWY-5509 | Actual CLI KGX exported172 records to separate external directory; complete target artifacts independently rechecked. Log /private/tmp/pathwaymech-salvage-kgx-audit-cli.log; SHA256 c68c4197fec68cfa2ffeeea741327be17fa1426b83485e5d6f50357b3710088a. |
| Superseded initial just lint | failed | False | MetaCyc:PWY-5509 | Style errors in new research replay helper; formatting/imports/strict four-column zip/unused variable corrected; actual replay and full lint rerun passed. Actual initial log /private/tmp/pathwaymech-salvage-lint.log SHA256 f3af228a25159ca258fa5c88925631af40947eed0a6e813d2af06226c4e5b254. Final successful run recorded separately. |
| Superseded initial just vendored-check | failed | False | MetaCyc:PWY-5509 | network unavailable on first sandbox attempt; authorized retry passed Actual initial log /private/tmp/pathwaymech-salvage-vendored.log SHA256 5c0bc23f897952690d071dc55631ff5e55cb0c369902d174847de4600bf1b6a2. Final successful run recorded separately. |
| Reviewer whitespace checks | passed | True | MetaCyc:PWY-5509 | Both separately executed reviewer checks returned0 on frozen source and generated bytes. |
| Initial scratch export selector | failed | False | MetaCyc:PWY-5509 | The scratch selector incorrectly treated source_records as the owning pathway; actual exporter stores evidence source IDs there. Selection was corrected to target-prefixed edge IDs; no repository change. |
| Independent final export recheck | passed | False | MetaCyc:PWY-5509 | All25 exported target edges retain45exact evidence objects,descriptions and reference metadata. Separate Rhea family assertion for329 is present in HTML and KGX; page and separate CLI file hashes match final audit. |
| Initial governed draft validation | failed | False | MetaCyc:PWY-5509 | Initial draft validation exited1 because search evidence lacked the mandatory separate search_scope field. The already described bounded search was copied into that governed field; no target or scientific input changed. |

## Scientific And Domain Assessments

### Exact native boundary and taxa

identity: supported. Targets: MetaCyc:PWY-5509.

The exact PWY-5509 title,membership and activated-corrinoid starting boundary are correct. K-12 accessions and bounded genetics support local taxon83333; MG1655 engineered evidence and BL21 construct evidence are not conflated. No native multi-species list is automatically inherited.

### All 14 chemical side edges and three direction fields

graph: supported. Targets: MetaCyc:PWY-5509.

All exact charged species,stoichiometric coefficients,locators and selected directions match issuing Rhea142; all three equations balance. Supplemental chemical-name mistakes are explicitly rejected instead of copied into graph chemistry.

### CobT source assembly and CobS/CobC functional roles

representation: supported. Targets: MetaCyc:PWY-5509.

CobT has a native external assembly identity,component coefficient2 and controlled reaction. Similarity evidence is retained. CobS/CobC enables assignments avoid inferring a physical monomer from frame names; 6E4B assigneddimer is distinguished from direct solution-assembly proof.

### Edges015–018 claim-specific evidence grades

evidence: supported. Targets: MetaCyc:PWY-5509.

Reviewed K-12 reactions,primary salvage genetics and later MG1655 cascade evidence support the selected gene functions at their stated scopes. The record distinguishes isolated enzymology,cross-species homology,engineered fusion constructs and multienzyme production. No physiological exclusivity or universal essentiality claim is made.

### Mg2+ and plasma-membrane location

evidence: supported. Targets: MetaCyc:PWY-5509.

Both exact auxiliary edges reproduce scoped reviewed annotations. Mg2+ remains ECO0000250 rather than buffer-based binding proof. GO0005886 derives from explicit experimental annotation; abstract-only source access precludes detailed topology claims.

### Native reaction membership and sequential transfer

scope: supported. Targets: MetaCyc:PWY-5509.

All three native memberships and two material-transfer edges agree with native XML and correct Rhea sides. The 1999 reconstitution alone did not establish physiological phosphate-removal timing; the 2007 terminal-step evidence remains Salmonella-specific.

### Pre-save minor issue329 correction verified

provenance: supported. Targets: MetaCyc:PWY-5509.

The initial edge023 chemical interpretation was correct but its sole native source citation did not establish the Rhea family relationship. Separate exact Rhea evidence now supports that bridge. No corrective finding remains in the frozen target; the original observation and final correction are retained without fabricated review lineage.

### Evidence limitations that constrain the qualified pass

completeness: unknown. Targets: MetaCyc:PWY-5509.

Direct native K-12 terminal-step physiology and isolated MG1655 CobC kinetic/assembly experiments are not established by inspected sources. Similarity-qualified annotations and engineered system evidence remain supported as such; these limits do not justify inflating the evidence tier.

### Source integrity and integrated publication consistency

provenance: supported. Targets: MetaCyc:PWY-5509.

Reference hashes,authority identities,unchanged baseline inputs,scoped context lookup and final generated artifacts are consistent. Required corpus gates pass; those checks do not constitute scientific assessment of other targets.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml; Complete target:17 participants,1 taxon,3 reactions,25 edges,45 evidence blocks,21 references | supports | Read the complete initial and frozen target; every edge and material qualifier was assessed. Final bytes were rechecked after the source-attribution correction. |
| e-native | https://pathway.yeastgenome.org/getxml?META:PWY-5509; PWY-5509 common-name,reaction-list,order and L2R layouts; separate DMBPPRIBOSYLTRANS-RXN,COBALAMIN5PSYN-RXN,RXN-8770 XML sides/dblinks | supports | The exact native route has three members and two sequential transfers. First two native reactions directly cross-reference11197 and23561; RXN-8770 instead cross-references bidirectional30370, requiring separate Rhea family evidence for30368. Native taxon and protein comments retain their versioned scope. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Release142 masters11196,23560,30367; directions11197,23561,30368; bidirectional30370; substrates/products,contains1,compound/chebi; official directions TSV | supports | Independent full-RDF extraction confirms all 14 chemical side occurrences with coefficient1, all three left-to-right selections and exact edge locators. Each equation balances in elements and charge. Exact ChEBI,GO,taxon andRhea labels were independently queried from issuing SemanticSQL caches. |
| e-proteins | https://rest.uniprot.org/uniprotkb/P36562.json; Reviewed UniProt2026_03 P36562,P36561,P52086 JSON: accession,organism83333,recommended name,FUNCTION,CAT,SUBUNIT,COFACTOR,SUBCELLULAR and GO cross-reference32 | supports | All three K-12 accessions and exact reactions agree. CobT homodimer and CobS function/Mg2+ retain ECO0000250. CobC terminal hydrolysis explicitly cites similarity to SalmonellaP39701. CobS GO0005886 location has IDA/ECO0000314; absence of a subunit statement is not monomer proof. Actual response-body hashes match all reference digests. |
| e-assembly | https://pathbank.org/pathways/SMP0001898; PW001884.owl: ProteinComplex/3870;Protein/6552;Stoichiometry/2.0;ProteinReference/6552;Reference/UniProt_P36562;ReactionCatalysis/5115;Reactions/5142 | supports | The native dimer contains two P36562 components and controls the exact DMB phosphoribosyltransferase reaction. This supplies an externally identified source assembly; current homodimer evidence is separately similarity-qualified, not a new physical-assembly experiment. |
| e-k12-primary | https://europepmc.org/articles/PMC177486?pdf=render; PMID7592411: complete extracted PDF,Materials and Methods,Results Localization of mutations,Tables2–3 printedp6375 | supports | K-12 cobS mutant growth defects support salvage function; DMB rescue and differing CobT phenotypes prevent universal enzyme-essentiality claims. These genetic assays do not directly assay each modern charged Rhea species. |
| e-salmonella-reconstitution | https://pmc.ncbi.nlm.nih.gov/articles/PMC18366/; PMID10518530: Methods,Results CobS cobalamin synthase and CobC dephosphorylation,Figures3C,4,6,Discussion | supports | The reconstitution uses Salmonella enzymes. CobT product feeds CobS; CobC-containing extract hydrolyzes formed cobalamin phosphate with vector-only control. Cyanation before HPLC and uncertain physiological phosphate-removal timing are preserved. |
| e-terminal-physiology | https://pmc.ncbi.nlm.nih.gov/articles/PMC1899380/; PMID17209023: Methods,Results cobC accumulation and preferred Alpha-RP substrate,Figures5–8,Discussion opening | supports | Salmonella mutant accumulation and substrate-preference experiments support terminal CobC dephosphorylation. The authors explicitly limit the demonstrated physiological conclusion to Salmonella; the target does not claim equivalent direct K-12 timing proof. |
| e-bl21 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8407341/; PMID34031037: Figure4A control,Table1,Materials and Methods in-vitro production; linked PMID31609521 Experimental procedures Strain cultivation and cloning | supports | The EcCobS control uses Salmonella CobU and Vibrio CobC, so it does not directly assay EcCobC. The linked publisher full-text cloning section confirms a BL21-derived EcCobS construct; no exact P36561 sequence equivalence or E.coli remodeling activity is inferred. |
| e-bl21-origin | https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.14402; PMID31609521: Experimental procedures,Strain cultivation and cloning,second paragraph,pET16bEcCobS | supports | Actual live publisher section was inspected independently through the web tool and identifies BL21 as the cloning source. Direct download403 does not negate the inspected web section; no downloaded full-text digest is claimed. |
| e-2023 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10449867/; PMID37620358 DOI10.1038/s41467-023-40932-4: Results promoting transmembrane reactions,Methods cloning/purification; actual31-pageSI Tables1–2,Figure9d | supports | The later system uses MG1655 enzymes, including engineered SIMPLEx-CobS, in a larger cell-free cascade and engineered complementation. It provides bounded additional function support, not isolated CobC kinetics, native assembly or native terminal-step flux. |
| e-2023-si | https://doi.org/10.1038/s41467-023-40932-4; Actual Supplementary Information PDF,Tables1–2 pages2,4–8;Figure9d page23; independently visually inspected pages4,5,7,8,23 | supports | Tables identify MG1655 CobT/CobS/CobC and include CobC[4] in the cascade. Misabbreviated nicotinate-ribonucleotide, cobinamide/cobalamin-phosphate name errors and the CobC[4] synthase footnote are real source conflicts. The target retains independent Rhea chemistry. Calculated K-prime-equilibrium values are not measured catalytic rates. |
| e-structure | https://data.rcsb.org/rest/v1/core/assembly/6E4B/1; RCSB6E4B assembly1 auth evidence,oligomeric details;entity1 SIFTS P52086 alignment and source strain | supports | Tagged 6E4B maps the complete P52086 sequence to K-12 source despite BL21 expression. Its dimer is author/PISA-assigned and experimental_support is explicitly none; no solution-assembly experiment is inferred. |
| e-location-primary | https://pubmed.ncbi.nlm.nih.gov/15919996/; Complete indexed abstract; separate P36561 location comment and GO0005886 IDA assertion | supports | The primary abstract describes systematic inner-membrane topology tagging. Detailed CobS topology was not independently read; the edge is correctly a bounded reviewed location assertion, not a new full-text primary result. |
| e-correction | https://github.com/CultureBotAI/PathwayMech/issues/329; nla-edge-023: initial governed target6ffc41e8827aab8bd22242b568233e1c0361e18104e31469188ec68d5937afec;final8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184;RXN-8770 body SHAfcbdc14cb69887cc5b3c3f8edd25861e7ba453492b4781d2304acd92b395dadb | supports | Reviewer found a minor provenance gap: the initial native-only assertion attributed the30367family→30368selection to MetaCyc although native XML provides30370 and physiologicalLTR only. Parent filed329; author separated native assertions and added explicit Rhea master/bidirectional/directional/side evidence. Independent raw replay verifies the final correction. No defective immutable predecessor was saved; this is pre-save observation history, not invented structured finding lineage. |
| e-replay | /private/tmp/pathwaymech-salvage-nucleotide-loop-review/replay.json; Independent scratch replay.py plus raw-input-recheck.json | supports | Reviewer executed a separate direct-source replay and rehashed27 raw bodies. Exact named identities,side triples,directions,balances,assembly links,native membership/order and all 21 reference digest/access dispositions match the final target. |
| e-authority | research/pathway_additions/2026-10-10-salvage/authority-integration.json; Canonical refreshed snapshots and manifest; independent reviewer comparison to83c2c597b300b8c716a32b96b6cbe8fb2a6ccb0a | supports | Every prior manifest/term/metadata value is retained; target IDs independently resolve. Rhea139 issuing-label cache and separately versioned Rhea142 chemistry are distinguished. Source-defined PathBank assembly context is a scoped participant label policy; ID existence and scientific role evidence remain mandatory. |
| e-context | research/pathway_additions/2026-10-10-salvage/imodulondb-context.json; Original adapter class fallback;datasets and e_coli/precise_mg1655 queries cobT,cobS,cobC | context_only | Installed console runner failed OS permission and external CLI lackeddotenv; root used unchanged ImodulonDBClient with recorded HTTP bodies. Each selected gene matched b1991,b1992,b0638 respectively and no module-name hits; no summarize applies. These are computational context hits, not catalytic proof or absence of module membership. |
| e-prior | reviews/ and reports/; Exact target ID,label,slug searched with rg -n -uu | supports | No prior exact-target review/report occurrence was returned. Search includes hidden and ignored files in these two review surfaces only; it is not a repository-wide scientific coverage claim. |
| e-generated | research/pathway_additions/2026-10-10-salvage/generated-graph-kgx-audit.json; Final actual CLI KGX,rendered HTML/SVG and metadata audit; target-specific reviewer recheck | supports | All 25 target edges/45 evidence and exact local source contexts remain in generated publication artifacts, including the separate Rhea30368 family evidence added for329. Structural programmatic verification does not imply visual browser QA. |
| e-gates | /private/tmp/pathwaymech-salvage-nucleotide-loop-review/gate-receipt.json; Actual root terminal results and rehashed validate/test/lint/render/vendored logs; reviewer whitespace/finalinput checks | supports | All required integrated gates reached terminal success on frozen inputs. Reviewer read the real logs and recorded delegated execution rather than rerunning broad corpus gates. Deterministic validation does not replace scientific assessment. |

## Limits And Additional Notes

- The exact route is an annotated K-12 pathway. Current CobC terminal chemistry and CobT/CobS auxiliary statements retain stated similarity evidence; direct Salmonella physiology is not K-12 physiological proof.
- The 2023 study supplies stronger MG1655 function support in an engineered multienzyme system and SIMPLEx-CobS fusion. It does not establish isolated CobC kinetics,native quaternary structure or terminal-step flux.
- The 2021 EcCobS construct is BL21-derived and uses heterologous accessory enzymes; no exact P36561 sequence identity is claimed. Cyanation constrains upper-ligand conclusions from the final peak.
- PMID15919996 was inspected at abstract level. The 2019/2020 EcCobS cloning section was inspected through live publisher web output; no downloaded full-text digest is claimed for that access.
- A source-defined CobT dimer and author/PISA-assigned CobC structure do not by themselves establish solution-assembly experiments. Functional enables edges do not assert isolated-monomer catalysis.
- The original Documents checkout was OS-inaccessible for author deduplication. The fresh author search and reviewer prior-review search cover the accessible worktree and explicitly included hidden/ignored files within their declared scopes.
- The iModulon console entry point was unavailable; the unchanged adapter-class fallback is recorded. Search results are computational context and no membership absence or mechanistic proof is inferred.
- Programmatic HTML/SVG/KGX checks do not constitute visual browser inspection. No claim of exhaustive literature coverage or scientific review of the other batch records is made.
- Generated page owner: the maintained target YAML, src/pathwaymech/cli.py and src/pathwaymech/graph_view.py via just render-pages. Generated authority snapshots are owned by the independent pinned inputs, conf/identifier_sources.json and canonical snapshot builders; future fixes belong to maintained inputs and generators.
- Initial governed capture at00:11:48UTC supplies the actual review start. Final changed inputs were explicitly reassessed before capture. Issue329 was fixed before the first immutable bundle; empty findings describes the frozen target and does not fabricate a resolved predecessor.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T002023Z-nucleotide-loop-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of adenosylcobalamin nucleotide-loop assembly
started_at: '2026-10-11T00:11:48Z'
finished_at: '2026-10-11T00:20:23Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored this target and its research. This
    reviewer inspected all target bytes and source bodies without editing the target.
    The reviewer authored the separate allantoin record and separately reviewed the
    contextual-label policy; independence is claimed for the present nucleotide-loop
    scientific target, not for the allantoin target.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact three-reaction PWY-5509 route is supported across all 22 named
  nodes,25 edges,45 evidence blocks and21 references. One minor edge-local source-attribution
  defect was found before freeze, filed as issue329 and corrected with separate native
  MetaCyc and Rhea evidence. Independent source replay confirms the correction; no
  open corrective finding remains. Similarity-qualified annotations, cross-species
  terminal-step physiology and the engineered scope of the 2023 MG1655 study remain
  explicit.
source:
  git_revision: 83c2c597b300b8c716a32b96b6cbe8fb2a6ccb0a
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: 3ec96c0a41020aa6a55443800ea6c26477187db6541d9365fe850d7492b9cb1c
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: e29efd42ce259b42e69f2633975e62ffbfd1f8ade0b7d56be98ae106a961a540
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 51ae7ed90bd02b7ed76d40b04627c3108d6621e23f9d110e10cdc0546907c24a
    role: context
  - path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
    sha256: 8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: docs/IDENTIFIERS.md
    sha256: dba50be9c2a6cf7a166790f3bab4d86fd89dbc3bea042a0f8e013e9586624328
    role: context
  - path: pages/records/MetaCyc_PWY-5509.html
    sha256: e876c984fb8ec681e7f30c18fcf9a7a0fcd4888651609d87370177ccd5400a8b
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/authority-integration.json
    sha256: fc5f1a8df62cf2f12077b55b0da1b351f2d989e3a1429fb9c1f5cae6c64e9b6c
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/baseline-preservation.json
    sha256: f54354956c7cf3bc8ebcc837686152147891ce6131adced2ebd0388fb3a098b0
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/generated-graph-kgx-audit.json
    sha256: e52b29a4496b04274ba41cd89fd02bab60106aef46bffe3db10e34a21bfe2cd7
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/imodulondb-context.json
    sha256: 1fbc82646b456ff90ef6742c010f3b919340ccb1f38c097833fd63bcc469e6b1
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/imodulondb-independent-replay.json
    sha256: cb14ac0855305712ae96b386bc4f58b625b5af0d68cde23695af65b82624a6e1
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/imodulondb-source-manifest.json
    sha256: ea561bd79b95d99c1d6309b8f2ab03f75147007b884a3b8fe681be055ff57d35
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/integration-validation.json
    sha256: ffbc8e6231d085154fda26a01a8521632e78e8d066754d00f2eea7bb0b432fdf
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/nucleotide-loop-curation.md
    sha256: ccca9f37daf57829acc28f1272f2d97683ba2c5ef335dcd6ed810769d084127e
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/nucleotide-loop-replay.py
    sha256: 068f036b2c5bde75c67b76048e428d2ba93f9fadb98c9f5f155e082baa27fe48
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/nucleotide-loop-source-manifest.json
    sha256: 5d2982119e46a24bcf127ceef1c92b393fd1214d2143bfb4e4e01e162e3bbd9c
    role: context
  - path: research/pathway_additions/2026-10-10-salvage/nucleotide-loop-validation.json
    sha256: 85b3faf73b1c80aef03472e619fc41b17e2e441396fe828d1cfc02d3490fcf58
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Full independent scientific assessment of one maintained target, its
    entire local graph and references.
  selection: Exact assigned MetaCyc:PWY-5509 maintained YAML.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5509
  exclusions:
  - target: All other pathway records, including the separately authored allantoin
      route
    reason: Shared corpus validation is not independent scientific assessment of other
      records.
  - target: Upstream cobinamide transport, reduction, adenosylation, GDP activation
      and de novo corrin synthesis
    reason: Outside the native three-reaction pathway boundary; supplied activated
      corrinoid is the input.
  - target: Unphosphorylated-ribazole alternative and cobamide remodeling
    reason: Different routes or activities, not assigned to this exact pathway.
targets:
- target_id: MetaCyc:PWY-5509
  path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
  label: adenosylcobalamin biosynthesis from adenosylcobinamide-GDP I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
    role: maintained pathway record
checks:
- check_id: c-initial-inspect
  name: Initial governed capture
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-salvage-nucleotide-loop-review/targets.yaml
    --input docs/CAUSAL_GRAPHS.md --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
    --input conf/identifier_policy.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit0 captured initial target6ffc41e8827aab8bd22242b568233e1c0361e18104e31469188ec68d5937afec
    before assessment. The temporary target kind was initially pathway; inspect accepted
    it, and it was corrected to governed maintained for final capture before any bundle
    validation/save.
  evidence_ids:
  - e-record
  - e-correction
- check_id: c-replay
  name: Independent issuing-source replay
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-salvage-nucleotide-loop-review/replay.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit0:14 exact chemical-side occurrences, coefficients1, three master-relative
    directions, three elemental/charge balances from Rhea compound fields,21 non-pathway
    issuing identities plus exact pathway identity, native assembly membership and21
    reference digest/access dispositions.
  evidence_ids:
  - e-rhea
  - e-native
  - e-proteins
  - e-replay
- check_id: c-body-hashes
  name: Independent raw-body and target freeze verification
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: .venv/bin/python reviewer raw-input recheck
  exit_code: 0
  expected_exit_code: 0
  summary: All 27 preserved manifest source bodies independently rehashed. Current
    frozen target is byte-identical to the first post-fix8453146 snapshot.
  evidence_ids:
  - e-replay
  - e-record
  - e-correction
- check_id: c-prior
  name: Ignored-inclusive prior review search
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: rg -n -uu 'MetaCyc:PWY-5509|adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i|adenosylcobalamin
    biosynthesis from adenosylcobinamide-GDP I' reviews reports
  exit_code: 0
  expected_exit_code: 0
  summary: Actual rg no-match status1 was treated as an ordinary successful bounded
    absence search by the reviewer wrapper, which exited0. Both hidden and ignored
    review/report files were included; no prior exact-target bundle found.
  evidence_ids:
  - e-prior
- check_id: c-authority
  name: Independent preserved-authority comparison
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: .venv/bin/python reviewer comparison of git83c2c597 baseline and current
    JSON values
  exit_code: 0
  expected_exit_code: 0
  summary: All 121 prior manifest inputs,1331 ontology terms/4 source-metadata entries
    and1633 source terms/105 metadata entries retain identical values. Final141 inputs,1367
    ontology terms and1658 source terms/112 metadata entries.
  evidence_ids:
  - e-authority
- check_id: c-final-inspect
  name: Final governed changed-input capture
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-salvage-nucleotide-loop-review/targets.yaml
    --input docs/CAUSAL_GRAPHS.md --input docs/IDENTIFIERS.md --input src/pathwaymech/schema.py
    --input src/pathwaymech/schema/pathwaymech.yaml --input conf/identifier_policy.yaml
    --input conf/identifier_sources.json --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input pages/records/MetaCyc_PWY-5509.html
    --input research/pathway_additions/2026-10-10-salvage/nucleotide-loop-curation.md
    --input research/pathway_additions/2026-10-10-salvage/nucleotide-loop-source-manifest.json
    --input research/pathway_additions/2026-10-10-salvage/nucleotide-loop-validation.json
    --input research/pathway_additions/2026-10-10-salvage/nucleotide-loop-replay.py
    --input research/pathway_additions/2026-10-10-salvage/authority-integration.json
    --input research/pathway_additions/2026-10-10-salvage/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-10-salvage/baseline-preservation.json
    --input research/pathway_additions/2026-10-10-salvage/integration-validation.json
    --input research/pathway_additions/2026-10-10-salvage/imodulondb-context.json
    --input research/pathway_additions/2026-10-10-salvage/imodulondb-source-manifest.json
    --input research/pathway_additions/2026-10-10-salvage/imodulondb-independent-replay.json
  exit_code: 0
  expected_exit_code: 0
  summary: Actual exit0 captures the final target, re-inspected receipts, authority
    snapshots and rendered page. The initial source-attribution observation is retained
    in evidence rather than silently replaced.
  evidence_ids:
  - e-record
  - e-correction
  - e-generated
- check_id: c-gate-render-pages
  name: Integrated just render-pages
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  summary: 172 records rendered. Log /private/tmp/pathwaymech-salvage-render.log;
    SHA256 f1ab92d786152e153465f8768b42742e6ce38d0f78a137f6156960079ea21337.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-gate-validate
  name: Integrated just validate
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  summary: 172 native and closed-schema records; exact identities;9047 evidence blocks;30sources;255history
    records;6documentation files and current pages passed. Log /private/tmp/pathwaymech-salvage-validate.log;
    SHA256 21db8649e8785667ca778d3c461b3af075d79129d2ba8ed759607bdb06a302cd.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-gate-test
  name: Integrated just test
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  summary: 1048 passed,3 skipped,3 upstream warnings in215.42seconds. Log /private/tmp/pathwaymech-salvage-test.log;
    SHA256 1b74817e756745dc202a910358835c45b2bcd02ee31db0b9a99d3b3f6d24165c.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-gate-lint
  name: Integrated just lint
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  summary: All Ruff checks passed after helper formatting and exact four-column zip.
    Log /private/tmp/pathwaymech-salvage-lint-final.log; SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-gate-check-identifiers
  name: Integrated just check-identifiers
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  exit_code: 0
  expected_exit_code: 0
  summary: All172 records resolve against authority snapshots. Log /private/tmp/pathwaymech-salvage-identifiers.log;
    SHA256 a0122812a006451b9885112bb7fd0ca7b653f43a1df2ee99361e04c7e33c30e2.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-gate-vendored-check
  name: Integrated just vendored-check
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  summary: All22 governed artifacts match pinned CLAW revision. Log /private/tmp/pathwaymech-salvage-vendored-final.log;
    SHA256 b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-gate-kgx-export
  name: Integrated just kgx-export --output-dir /private/tmp/pathwaymech-salvage-kgx
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-salvage-kgx
  exit_code: 0
  expected_exit_code: 0
  summary: Actual CLI KGX exported172 records to separate external directory; complete
    target artifacts independently rechecked. Log /private/tmp/pathwaymech-salvage-kgx-audit-cli.log;
    SHA256 c68c4197fec68cfa2ffeeea741327be17fa1426b83485e5d6f50357b3710088a.
  evidence_ids:
  - e-gates
  scope_note: Executed by integration agent /root on frozen inputs; this reviewer
    inspected actual log bytes and parent terminal outcome. No duplicate broad-gate
    execution or scientific review of other records is implied.
- check_id: c-prior-gate-0
  name: Superseded initial just lint
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 1
  expected_exit_code: 0
  summary: Style errors in new research replay helper; formatting/imports/strict four-column
    zip/unused variable corrected; actual replay and full lint rerun passed. Actual
    initial log /private/tmp/pathwaymech-salvage-lint.log SHA256 f3af228a25159ca258fa5c88925631af40947eed0a6e813d2af06226c4e5b254.
    Final successful run recorded separately.
  evidence_ids:
  - e-gates
- check_id: c-prior-gate-1
  name: Superseded initial just vendored-check
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    vendored-check
  exit_code: 1
  expected_exit_code: 0
  summary: network unavailable on first sandbox attempt; authorized retry passed Actual
    initial log /private/tmp/pathwaymech-salvage-vendored.log SHA256 5c0bc23f897952690d071dc55631ff5e55cb0c369902d174847de4600bf1b6a2.
    Final successful run recorded separately.
  evidence_ids:
  - e-gates
- check_id: c-diff
  name: Reviewer whitespace checks
  status: passed
  required: true
  target_ids:
  - MetaCyc:PWY-5509
  command: git diff --check; git diff --cached --check
  exit_code: 0
  expected_exit_code: 0
  summary: Both separately executed reviewer checks returned0 on frozen source and
    generated bytes.
  evidence_ids:
  - e-record
- check_id: c-generated-initial
  name: Initial scratch export selector
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: .venv/bin/python reviewer KGX source_records selector
  exit_code: 1
  expected_exit_code: 0
  summary: The scratch selector incorrectly treated source_records as the owning pathway;
    actual exporter stores evidence source IDs there. Selection was corrected to target-prefixed
    edge IDs; no repository change.
  evidence_ids:
  - e-generated
- check_id: c-generated
  name: Independent final export recheck
  status: passed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: .venv/bin/python reviewer target-prefixed KGX and HTML check
  exit_code: 0
  expected_exit_code: 0
  summary: All25 exported target edges retain45exact evidence objects,descriptions
    and reference metadata. Separate Rhea family assertion for329 is present in HTML
    and KGX; page and separate CLI file hashes match final audit.
  evidence_ids:
  - e-generated
  - e-correction
- check_id: c-draft-format
  name: Initial governed draft validation
  status: failed
  required: false
  target_ids:
  - MetaCyc:PWY-5509
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py validate /private/tmp/pathwaymech-salvage-nucleotide-loop-review/completed-review.yaml
  exit_code: 1
  expected_exit_code: 0
  summary: Initial draft validation exited1 because search evidence lacked the mandatory
    separate search_scope field. The already described bounded search was copied into
    that governed field; no target or scientific input changed.
  evidence_ids:
  - e-prior
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/adenosylcobalamin-biosynthesis-from-adenosylcobinamide-gdp-i.yaml
  locator: Complete target:17 participants,1 taxon,3 reactions,25 edges,45 evidence
    blocks,21 references
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Read the complete initial and frozen target; every edge and material qualifier
    was assessed. Final bytes were rechecked after the source-attribution correction.
  snapshot_sha256: 8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-5509
  locator: PWY-5509 common-name,reaction-list,order and L2R layouts; separate DMBPPRIBOSYLTRANS-RXN,COBALAMIN5PSYN-RXN,RXN-8770
    XML sides/dblinks
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: The exact native route has three members and two sequential transfers.
    First two native reactions directly cross-reference11197 and23561; RXN-8770 instead
    cross-references bidirectional30370, requiring separate Rhea family evidence for30368.
    Native taxon and protein comments retain their versioned scope.
  snapshot_sha256: de4e4e21ac728af6ed447d0d42e2b018b1fdeab29cc1062604108bfb3d2e7244
- evidence_id: e-rhea
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Release142 masters11196,23560,30367; directions11197,23561,30368; bidirectional30370;
    substrates/products,contains1,compound/chebi; official directions TSV
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Independent full-RDF extraction confirms all 14 chemical side occurrences
    with coefficient1, all three left-to-right selections and exact edge locators.
    Each equation balances in elements and charge. Exact ChEBI,GO,taxon andRhea labels
    were independently queried from issuing SemanticSQL caches.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36562.json
  locator: 'Reviewed UniProt2026_03 P36562,P36561,P52086 JSON: accession,organism83333,recommended
    name,FUNCTION,CAT,SUBUNIT,COFACTOR,SUBCELLULAR and GO cross-reference32'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: All three K-12 accessions and exact reactions agree. CobT homodimer and
    CobS function/Mg2+ retain ECO0000250. CobC terminal hydrolysis explicitly cites
    similarity to SalmonellaP39701. CobS GO0005886 location has IDA/ECO0000314; absence
    of a subunit statement is not monomer proof. Actual response-body hashes match
    all reference digests.
- evidence_id: e-assembly
  kind: database
  reference: https://pathbank.org/pathways/SMP0001898
  locator: 'PW001884.owl: ProteinComplex/3870;Protein/6552;Stoichiometry/2.0;ProteinReference/6552;Reference/UniProt_P36562;ReactionCatalysis/5115;Reactions/5142'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: The native dimer contains two P36562 components and controls the exact
    DMB phosphoribosyltransferase reaction. This supplies an externally identified
    source assembly; current homodimer evidence is separately similarity-qualified,
    not a new physical-assembly experiment.
  snapshot_sha256: 4b4233814e281b298cf718f03ae89c2c0af8e70a278ccd0ea0664d8575499612
- evidence_id: e-k12-primary
  kind: primary_source
  reference: https://europepmc.org/articles/PMC177486?pdf=render
  locator: 'PMID7592411: complete extracted PDF,Materials and Methods,Results Localization
    of mutations,Tables2–3 printedp6375'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: K-12 cobS mutant growth defects support salvage function; DMB rescue and
    differing CobT phenotypes prevent universal enzyme-essentiality claims. These
    genetic assays do not directly assay each modern charged Rhea species.
  snapshot_sha256: 42da7e9bae0a77458a857218fe302469602a6e9247cb4e5092af60c362ad122b
- evidence_id: e-salmonella-reconstitution
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC18366/
  locator: 'PMID10518530: Methods,Results CobS cobalamin synthase and CobC dephosphorylation,Figures3C,4,6,Discussion'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: The reconstitution uses Salmonella enzymes. CobT product feeds CobS; CobC-containing
    extract hydrolyzes formed cobalamin phosphate with vector-only control. Cyanation
    before HPLC and uncertain physiological phosphate-removal timing are preserved.
  snapshot_sha256: e1879357ff7b981378c747cd9b687afa618f4cc71ab9d0d9982ae4b37c1339dd
- evidence_id: e-terminal-physiology
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1899380/
  locator: 'PMID17209023: Methods,Results cobC accumulation and preferred Alpha-RP
    substrate,Figures5–8,Discussion opening'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Salmonella mutant accumulation and substrate-preference experiments support
    terminal CobC dephosphorylation. The authors explicitly limit the demonstrated
    physiological conclusion to Salmonella; the target does not claim equivalent direct
    K-12 timing proof.
  snapshot_sha256: 9799f9e02b3cb36da51360533d3a8ef651693c3e1cdd232b32d50ecf16d83bdf
- evidence_id: e-bl21
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8407341/
  locator: 'PMID34031037: Figure4A control,Table1,Materials and Methods in-vitro production;
    linked PMID31609521 Experimental procedures Strain cultivation and cloning'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: The EcCobS control uses Salmonella CobU and Vibrio CobC, so it does not
    directly assay EcCobC. The linked publisher full-text cloning section confirms
    a BL21-derived EcCobS construct; no exact P36561 sequence equivalence or E.coli
    remodeling activity is inferred.
  snapshot_sha256: c030fdc34f5fb84c0543d327c8ee0050cf288dfcc915a2f9305239bd1392d77d
- evidence_id: e-bl21-origin
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.14402
  locator: 'PMID31609521: Experimental procedures,Strain cultivation and cloning,second
    paragraph,pET16bEcCobS'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Actual live publisher section was inspected independently through the web
    tool and identifies BL21 as the cloning source. Direct download403 does not negate
    the inspected web section; no downloaded full-text digest is claimed.
- evidence_id: e-2023
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10449867/
  locator: 'PMID37620358 DOI10.1038/s41467-023-40932-4: Results promoting transmembrane
    reactions,Methods cloning/purification; actual31-pageSI Tables1–2,Figure9d'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: The later system uses MG1655 enzymes, including engineered SIMPLEx-CobS,
    in a larger cell-free cascade and engineered complementation. It provides bounded
    additional function support, not isolated CobC kinetics, native assembly or native
    terminal-step flux.
  snapshot_sha256: b672d2fa009658762fc8f41ccbd17fcbe943440b40353f7570c87651cee90f82
- evidence_id: e-2023-si
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-023-40932-4
  locator: Actual Supplementary Information PDF,Tables1–2 pages2,4–8;Figure9d page23;
    independently visually inspected pages4,5,7,8,23
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Tables identify MG1655 CobT/CobS/CobC and include CobC[4] in the cascade.
    Misabbreviated nicotinate-ribonucleotide, cobinamide/cobalamin-phosphate name
    errors and the CobC[4] synthase footnote are real source conflicts. The target
    retains independent Rhea chemistry. Calculated K-prime-equilibrium values are
    not measured catalytic rates.
  snapshot_sha256: b847c84fe5bf0b7de306cba3cb3c0ee8278053381a8dafaa35789dfcfa57dce7
- evidence_id: e-structure
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/6E4B/1
  locator: RCSB6E4B assembly1 auth evidence,oligomeric details;entity1 SIFTS P52086
    alignment and source strain
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Tagged 6E4B maps the complete P52086 sequence to K-12 source despite BL21
    expression. Its dimer is author/PISA-assigned and experimental_support is explicitly
    none; no solution-assembly experiment is inferred.
  snapshot_sha256: 53d35b7f80a5302e9d99389ff4196dceb0bbbe4d6e30c2f5ca91ca500515d5fd
- evidence_id: e-location-primary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15919996/
  locator: Complete indexed abstract; separate P36561 location comment and GO0005886
    IDA assertion
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: The primary abstract describes systematic inner-membrane topology tagging.
    Detailed CobS topology was not independently read; the edge is correctly a bounded
    reviewed location assertion, not a new full-text primary result.
- evidence_id: e-correction
  kind: validation
  reference: https://github.com/CultureBotAI/PathwayMech/issues/329
  locator: 'nla-edge-023: initial governed target6ffc41e8827aab8bd22242b568233e1c0361e18104e31469188ec68d5937afec;final8453146fc5cc438fd95be5acc623ba0f6fbe52e647ad21f1fa2dc535ee619184;RXN-8770
    body SHAfcbdc14cb69887cc5b3c3f8edd25861e7ba453492b4781d2304acd92b395dadb'
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: 'Reviewer found a minor provenance gap: the initial native-only assertion
    attributed the30367family→30368selection to MetaCyc although native XML provides30370
    and physiologicalLTR only. Parent filed329; author separated native assertions
    and added explicit Rhea master/bidirectional/directional/side evidence. Independent
    raw replay verifies the final correction. No defective immutable predecessor was
    saved; this is pre-save observation history, not invented structured finding lineage.'
- evidence_id: e-replay
  kind: validation
  reference: /private/tmp/pathwaymech-salvage-nucleotide-loop-review/replay.json
  locator: Independent scratch replay.py plus raw-input-recheck.json
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Reviewer executed a separate direct-source replay and rehashed27 raw bodies.
    Exact named identities,side triples,directions,balances,assembly links,native
    membership/order and all 21 reference digest/access dispositions match the final
    target.
  snapshot_sha256: 7b67e71cd29a35ccb7751b6740a0ec974f464e0b1738ad5a960de4e238571622
- evidence_id: e-authority
  kind: authority
  reference: research/pathway_additions/2026-10-10-salvage/authority-integration.json
  locator: Canonical refreshed snapshots and manifest; independent reviewer comparison
    to83c2c597b300b8c716a32b96b6cbe8fb2a6ccb0a
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: Every prior manifest/term/metadata value is retained; target IDs independently
    resolve. Rhea139 issuing-label cache and separately versioned Rhea142 chemistry
    are distinguished. Source-defined PathBank assembly context is a scoped participant
    label policy; ID existence and scientific role evidence remain mandatory.
  snapshot_sha256: fc5f1a8df62cf2f12077b55b0da1b351f2d989e3a1429fb9c1f5cae6c64e9b6c
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-10-salvage/imodulondb-context.json
  locator: Original adapter class fallback;datasets and e_coli/precise_mg1655 queries
    cobT,cobS,cobC
  accessed_at: '2026-10-11T00:20:23Z'
  support: context_only
  summary: Installed console runner failed OS permission and external CLI lackeddotenv;
    root used unchanged ImodulonDBClient with recorded HTTP bodies. Each selected
    gene matched b1991,b1992,b0638 respectively and no module-name hits; no summarize
    applies. These are computational context hits, not catalytic proof or absence
    of module membership.
  snapshot_sha256: 1fbc82646b456ff90ef6742c010f3b919340ccb1f38c097833fd63bcc469e6b1
- evidence_id: e-prior
  kind: search
  reference: reviews/ and reports/
  locator: Exact target ID,label,slug searched with rg -n -uu
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: No prior exact-target review/report occurrence was returned. Search includes
    hidden and ignored files in these two review surfaces only; it is not a repository-wide
    scientific coverage claim.
  search_scope: Accessible worktree reviews/ and reports/ recursively, including hidden
    and ignored files via rg -uu; exact MetaCyc:PWY-5509, complete pathway label and
    stable slug. No broader absence claim.
- evidence_id: e-generated
  kind: validation
  reference: research/pathway_additions/2026-10-10-salvage/generated-graph-kgx-audit.json
  locator: Final actual CLI KGX,rendered HTML/SVG and metadata audit; target-specific
    reviewer recheck
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: All 25 target edges/45 evidence and exact local source contexts remain
    in generated publication artifacts, including the separate Rhea30368 family evidence
    added for329. Structural programmatic verification does not imply visual browser
    QA.
  snapshot_sha256: e52b29a4496b04274ba41cd89fd02bab60106aef46bffe3db10e34a21bfe2cd7
- evidence_id: e-gates
  kind: validation
  reference: /private/tmp/pathwaymech-salvage-nucleotide-loop-review/gate-receipt.json
  locator: Actual root terminal results and rehashed validate/test/lint/render/vendored
    logs; reviewer whitespace/finalinput checks
  accessed_at: '2026-10-11T00:20:23Z'
  support: supports
  summary: All required integrated gates reached terminal success on frozen inputs.
    Reviewer read the real logs and recorded delegated execution rather than rerunning
    broad corpus gates. Deterministic validation does not replace scientific assessment.
  snapshot_sha256: 5ba99f01b55784f1c854e98e9fa99880395663776fd2fcc844180bc258d07855
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact native boundary and taxa
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-record
  - e-native
  - e-proteins
  - e-k12-primary
  - e-bl21
  - e-2023
  summary: The exact PWY-5509 title,membership and activated-corrinoid starting boundary
    are correct. K-12 accessions and bounded genetics support local taxon83333; MG1655
    engineered evidence and BL21 construct evidence are not conflated. No native multi-species
    list is automatically inherited.
  dimensions:
  - name: target_taxon
    value: NCBITaxon:83333 Escherichia coli K-12
    definition: Local annotated taxon; MG1655 engineered-system evidence and BL21
      construct evidence retain distinct conditions.
    evidence_ids:
    - e-proteins
    - e-k12-primary
    - e-bl21
    - e-2023
- assessment_id: a-chemistry
  area: graph
  topic: All 14 chemical side edges and three direction fields
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-rhea
  - e-replay
  - e-2023-si
  summary: All exact charged species,stoichiometric coefficients,locators and selected
    directions match issuing Rhea142; all three equations balance. Supplemental chemical-name
    mistakes are explicitly rejected instead of copied into graph chemistry.
- assessment_id: a-assembly
  area: representation
  topic: CobT source assembly and CobS/CobC functional roles
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-assembly
  - e-proteins
  - e-structure
  summary: CobT has a native external assembly identity,component coefficient2 and
    controlled reaction. Similarity evidence is retained. CobS/CobC enables assignments
    avoid inferring a physical monomer from frame names; 6E4B assigneddimer is distinguished
    from direct solution-assembly proof.
  dimensions:
  - name: assembly_evidence
    value: Native PathBank CobT dimer; reviewed similarity; RCSB CobC author/PISA
      assignment without experimental assembly support
    definition: Source-defined participant identity and physical evidence tier are
      distinct; enables does not specify physical monomer.
    evidence_ids:
    - e-assembly
    - e-proteins
    - e-structure
- assessment_id: a-functions
  area: evidence
  topic: Edges015–018 claim-specific evidence grades
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-proteins
  - e-k12-primary
  - e-salmonella-reconstitution
  - e-terminal-physiology
  - e-bl21
  - e-2023
  - e-2023-si
  summary: Reviewed K-12 reactions,primary salvage genetics and later MG1655 cascade
    evidence support the selected gene functions at their stated scopes. The record
    distinguishes isolated enzymology,cross-species homology,engineered fusion constructs
    and multienzyme production. No physiological exclusivity or universal essentiality
    claim is made.
  dimensions:
  - name: experimental_scope
    value: K-12 salvage genetics; Salmonella terminal-step physiology; MG1655 engineered
      multienzyme system; BL21-derived CobS construct
    definition: The exact taxon and experimental system that bounds each support class.
    evidence_ids:
    - e-k12-primary
    - e-terminal-physiology
    - e-bl21
    - e-2023
- assessment_id: a-auxiliary
  area: evidence
  topic: Mg2+ and plasma-membrane location
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-proteins
  - e-location-primary
  summary: Both exact auxiliary edges reproduce scoped reviewed annotations. Mg2+
    remains ECO0000250 rather than buffer-based binding proof. GO0005886 derives from
    explicit experimental annotation; abstract-only source access precludes detailed
    topology claims.
- assessment_id: a-order
  area: scope
  topic: Native reaction membership and sequential transfer
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-native
  - e-rhea
  - e-salmonella-reconstitution
  - e-terminal-physiology
  summary: All three native memberships and two material-transfer edges agree with
    native XML and correct Rhea sides. The 1999 reconstitution alone did not establish
    physiological phosphate-removal timing; the 2007 terminal-step evidence remains
    Salmonella-specific.
- assessment_id: a-correction
  area: provenance
  topic: Pre-save minor issue329 correction verified
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-correction
  - e-native
  - e-rhea
  - e-replay
  - e-generated
  summary: The initial edge023 chemical interpretation was correct but its sole native
    source citation did not establish the Rhea family relationship. Separate exact
    Rhea evidence now supports that bridge. No corrective finding remains in the frozen
    target; the original observation and final correction are retained without fabricated
    review lineage.
- assessment_id: a-limits
  area: completeness
  topic: Evidence limitations that constrain the qualified pass
  outcome: unknown
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-proteins
  - e-terminal-physiology
  - e-2023
  - e-2023-si
  - e-structure
  summary: Direct native K-12 terminal-step physiology and isolated MG1655 CobC kinetic/assembly
    experiments are not established by inspected sources. Similarity-qualified annotations
    and engineered system evidence remain supported as such; these limits do not justify
    inflating the evidence tier.
- assessment_id: a-integrity
  area: provenance
  topic: Source integrity and integrated publication consistency
  outcome: supported
  target_ids:
  - MetaCyc:PWY-5509
  evidence_ids:
  - e-replay
  - e-authority
  - e-context
  - e-generated
  - e-gates
  summary: Reference hashes,authority identities,unchanged baseline inputs,scoped
    context lookup and final generated artifacts are consistent. Required corpus gates
    pass; those checks do not constitute scientific assessment of other targets.
findings: []
actions: []
limitations:
- The exact route is an annotated K-12 pathway. Current CobC terminal chemistry and
  CobT/CobS auxiliary statements retain stated similarity evidence; direct Salmonella
  physiology is not K-12 physiological proof.
- The 2023 study supplies stronger MG1655 function support in an engineered multienzyme
  system and SIMPLEx-CobS fusion. It does not establish isolated CobC kinetics,native
  quaternary structure or terminal-step flux.
- The 2021 EcCobS construct is BL21-derived and uses heterologous accessory enzymes;
  no exact P36561 sequence identity is claimed. Cyanation constrains upper-ligand
  conclusions from the final peak.
- PMID15919996 was inspected at abstract level. The 2019/2020 EcCobS cloning section
  was inspected through live publisher web output; no downloaded full-text digest
  is claimed for that access.
- A source-defined CobT dimer and author/PISA-assigned CobC structure do not by themselves
  establish solution-assembly experiments. Functional enables edges do not assert
  isolated-monomer catalysis.
- The original Documents checkout was OS-inaccessible for author deduplication. The
  fresh author search and reviewer prior-review search cover the accessible worktree
  and explicitly included hidden/ignored files within their declared scopes.
- The iModulon console entry point was unavailable; the unchanged adapter-class fallback
  is recorded. Search results are computational context and no membership absence
  or mechanistic proof is inferred.
- Programmatic HTML/SVG/KGX checks do not constitute visual browser inspection. No
  claim of exhaustive literature coverage or scientific review of the other batch
  records is made.
notes:
- 'Generated page owner: the maintained target YAML, src/pathwaymech/cli.py and src/pathwaymech/graph_view.py
  via just render-pages. Generated authority snapshots are owned by the independent
  pinned inputs, conf/identifier_sources.json and canonical snapshot builders; future
  fixes belong to maintained inputs and generators.'
- Initial governed capture at00:11:48UTC supplies the actual review start. Final changed
  inputs were explicitly reassessed before capture. Issue329 was fixed before the
  first immutable bundle; empty findings describes the frozen target and does not
  fabricate a resolved predecessor.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/329
```
