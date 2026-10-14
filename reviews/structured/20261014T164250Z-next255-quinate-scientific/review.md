# Independent scientific review of quinate degradation I

- Review: 20261014T164250Z-next255-quinate-scientific
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T16:23:07Z
- Finished UTC: 2026-10-14T16:42:50Z
- Reviewer: codex:/root/next255_science_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Independently assessed the entire frozen quinate degradation I record: all 37 edges and all 51 bounded native biological source objects. Concrete molecular identities, reaction direction and class scope, six catalyst preparations, taxon contexts and edge-level evidence are supported. The pending author attribution correction tracked by issue 540 is reflected in final evidence; no erroneous maintained record or structured predecessor is invented. All required gates pass on the reviewed bytes. No open scientific findings remain.

## Scope And Provenance

One maintained pathway, all 37 mechanistic edges, three reactions, 17 participants, two taxa, 31 references and all 51 objects in the declared native biological neighborhood; independent primary reading with explicit access bounds.

Selection: Exact MetaCyc:QUINATEDEG-PWY target selected for complete independent review; no edge or source-neighborhood sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base bfa3f5ed0e843472c0fd173ce91df2a90dd4ddb2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:QUINATEDEG-PWY | data/pathways/quinate-degradation-i.yaml | maintained | quinate degradation I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Final frozen input inspection | passed | True | MetaCyc:QUINATEDEG-PWY | Initial target was inspected before judgement; complete final record was reread after changes. Final inspect binds the exact target and retained context inputs. |
| All-edge and reference audit | passed | True | MetaCyc:QUINATEDEG-PWY | All 37 unique triples, 29 source hashes and seven literal quote occurrences pass. |
| Independent native/ChEBI/Rhea verification | passed | True | MetaCyc:QUINATEDEG-PWY | Six concrete molecular identities, three native reaction side/direction declarations and 35 raw-RDF node comparisons pass. |
| Complete bounded native biological neighborhood | passed | True | MetaCyc:QUINATEDEG-PWY | Independent original-slot traversal produces all 51 reviewed objects and agrees with 13 retained/38 excluded dispositions. |
| Structured iModulonDB applicability | passed | False | MetaCyc:QUINATEDEG-PWY | Catalog acquisition succeeded; no matching target organism/dataset, so gene/module queries are not applicable. Absence does not weaken biological evidence. |
| just render-pages | passed | True | MetaCyc:QUINATEDEG-PWY | Root executed this full-repository gate; reviewer independently verified original output hash, exit status and unchanged tested inputs. Generated all maintained pages/graph data successfully. |
| just validate | passed | True | MetaCyc:QUINATEDEG-PWY | Root executed this full-repository gate; reviewer independently verified original output hash, exit status and unchanged tested inputs. Full closed-schema, identifier/label, evidence and history/review validation passed. |
| just test | passed | True | MetaCyc:QUINATEDEG-PWY | Root executed this full-repository gate; reviewer independently verified original output hash, exit status and unchanged tested inputs. Full pytest suite passed; complete terminal summary retained in original log. |
| just lint | passed | True | MetaCyc:QUINATEDEG-PWY | Root executed this full-repository gate; reviewer independently verified original output hash, exit status and unchanged tested inputs. Full Ruff lint passed. |
| just vendored-check | passed | True | MetaCyc:QUINATEDEG-PWY | Root executed this full-repository gate; reviewer independently verified original output hash, exit status and unchanged tested inputs. Canonical vendored helper check passed. |
| git diff --check | passed | True | MetaCyc:QUINATEDEG-PWY | Root executed this full-repository gate; reviewer independently verified original output hash, exit status and unchanged tested inputs. Whitespace check passed. |

## Scientific And Domain Assessments

### Exact native three-step quinate degradation I boundary

identity: supported. Targets: MetaCyc:QUINATEDEG-PWY.

The target preserves the complete native three-step route and its specific taxon contexts. It excludes NAD-dependent sibling pathways, aromatic biosynthesis, AsbF petrobactin biology and the same protein's neighboring shikimate activity. Shared downstream reactions do not merge these pathways.

### Molecular identities, quinone class scope and reversibility

grounding: supported. Targets: MetaCyc:QUINATEDEG-PWY.

Quinate/DHQ/DHS/protocatechuate/water/PQQ identities agree at full InChI and InChIKey level. Native broad quinones/quinols and initial reaction remain native because narrower Rhea classes are not exact scope matches. PQQ is an enzyme cofactor, not the net quinone acceptor. Middle RHEA21099 remains reversible while graph edges select catabolic flux; final RHEA24849 and the six contains1 side locators agree with original RDF.

### Taxon, assay and construct scope for all six catalysts

evidence: supported. Targets: MetaCyc:QUINATEDEG-PWY.

ADP1 QuiA/QuiB/QuiC functions have genetic/extract or recombinant support, with current exact protein identities and explicit old-start/construct limits. IFO3244 QDH, pDQD complex and DHSase retain preparation identities and evidence tiers. Native erroneous citation/prose content is not converted into direct ADP1 purified evidence or a wrong substrate claim.

### Molecular state, component role and localization

representation: supported. Targets: MetaCyc:QUINATEDEG-PWY.

MONOMER-0 is represented as a complex with MONOMER-15328 membership, not isolated-subunit catalysis. A suggested twelve-subunit state is qualified, and the short 621H sequence comparison is not exact identity. Broad membrane association is supported; precise periplasmic topology and direct QDH-pDQD interaction are not promoted. Cytoplasmic recovery is preparation context rather than exclusive localization.

### Every local edge and complete bounded source neighborhood

completeness: supported. Targets: MetaCyc:QUINATEDEG-PWY.

All 37 maintained edges and all 51 native biological neighborhood objects were reviewed. Exclusions are explicit and biologically justified; no available native regulatory object is silently promoted onto the retained pathway. Structured iModulonDB coverage is not applicable. This is complete coverage of the declared record/native neighborhood, not exhaustion of literature or all organisms.

### Source assertions, quotes and already-applied author correction

provenance: supported. Targets: MetaCyc:QUINATEDEG-PWY.

Original hashes, structured locators and literal quote checks support traceability. The SA1/AC3 genus mistake was in a pending session attribution; corrected author evidence now states Acinetobacter and no erroneous maintained pathway had been written. This clean record review reports the applied correction without inventing a resolved structured predecessor.

### Full-repository required checks on reviewed bytes

schema: supported. Targets: MetaCyc:QUINATEDEG-PWY.

Documented validation, test, lint and whitespace checks pass, alongside rendering and vendored checks. Reviewer verified actual root receipts and final unchanged tested-core hashes; these deterministic results supplement independent scientific evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/quinate-degradation-i.yaml | supports | Read the entire final frozen record and independently assessed all 37 edges, three reactions, 17 participants, two taxa and 31 references. Final SHA a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb; initial inspected draft was reread after spacing and six Rhea contains1 locator corrections. |
| e-edge | research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/all-edge-and-reference-audit.json | supports | All 37 exact triples reproduce from inspected native assertions and independently adjudicated primary support; 29 hash-bearing references match actual originals; all seven quote occurrences literally match inspected text with whitespace normalization only. Deterministic checks complement scientific reading. |
| e-neighborhood | research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/native-neighborhood-audit.json | supports | Independently traversed original native reaction/activity/enzyme/component/auxiliary-activity/regulation slots: 16 direct activities, 16 enzymes, five subunits, seven auxiliary activities and seven regulations. All 51 original objects have explicit reviewer dispositions: 13 retained with scope, 38 excluded. Exact set and decisions agree with the author ledger, without treating it as approval. |
| e-chemical | research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/independent-source-checks.json | supports | Six native/ChEBI full InChI and InChIKey identities independently agree. Reparsed original Rhea 142 RDF and matched all 35 projected nodes. Exact native three-step side/direction semantics retained; broad native quinone classes are not equated to narrower Rhea 23673 participants. |
| e-pathway | https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:QUINATEDEG-PWY; /ptools-xml/Pathway[@frameid="QUINATEDEG-PWY"] | supports | Inspected full MetaCyc 27.0 native pathway, reaction-list, layout, predecessor ordering, comments and evidence. Exact boundary is quinate through DHQ/DHS to protocatechuate; source taxa are ADP1 and G. oxydans, not every isolate or a purified one-strain reconstruction. |
| e-1994 | https://pmc.ncbi.nlm.nih.gov/articles/PMC197224/; PMID8002591; DOI10.1128/jb.176.24.7659-7666.1994; original scan hashes in retained primary/reading-ledger.json | supports | Independently read all eight official page scans, pp. 7659–7666, including methods, results, discussion, references, figures and Table 1. ADP1 genetic/complementation and extract evidence supports QuiA; 809-aa sequence and membrane predictions do not constitute direct topology measurement. Standard QDH assay in recombinant DH5alpha(pZR504) was undetectable even with PQQ. Protocatechuate induction and quinate metabolism dependence do not establish direct regulator-ligand binding. |
| e-1995 | https://www.researchgate.net/publication/15607491_Unusual_ancestry_of_dehydratases_associated_with_quinate_catabolism_in_Acinetobacter_calcoaceticus; PMID7592351; DOI10.1128/jb.177.20.5971-5978.1995; methods, Table 1, cloned enzyme results and discussion | supports | Independently read author-rendered complete main body, Table 1 and figure captions, pp. 5971–5978, with original figure images unavailable. Native thermolabile catabolic QuiB evidence is distinct from biosynthetic AroD and the old 290-aa recombinant start annotation. QuiC pZR564 is the 2.0-kb HindIII ADP1 insert in E. coli DH5alpha; no tag or expressed termini measured. Text/Table 1 pBSK/pBKS conflict retained. QuiC is DHS-dehydrating; native DHQ and numeric-unit prose errors are not copied. No demonstrated QuiX transporter edge. |
| e-2003-qdh | https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2115/_pdf; PMID14586098; DOI10.1271/bbb.67.2115; pp. 2116–2122, Tables 1/2 and purification/acceptor sections | supports | Independently read all nine text pages, pp. 2115–2123, and visually verified decisive pp. 2118/2120 Tables 1/2 and adjacent purification explanation. SA1 is Acinetobacter sp.; AC3 is A. calcoaceticus. Gluconobacter purification was abandoned because of co-purifying ADH. PQQ/calcium reconstitution, ferricyanide/PMS-DCIP/DCIP/ubiquinone-2 and membrane oxygen-uptake evidence concern those Acinetobacter preparations, not ADP1 or IFO3244; neither universal quinone specificity nor full respiratory-chain reconstitution follows. |
| e-2003-dhs | https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2124/_pdf; PMID14586099; DOI10.1271/bbb.67.2124; methods and cytoplasmic enzyme fractionation/results | supports | Independently read all eight text pages, pp. 2124–2131, and visually inspected p. 2129 Figure 5 and fractionation text. IFO3244 partially purified cytoplasmic DHSase is separated from DQD and supports qualitative protocatechuate formation. No homogeneous enzyme, complete sequence or full same-strain three-enzyme reconstitution is asserted. NADP/shikimate-dehydrogenase coupling is not assigned as a DHSase cofactor. |
| e-2008 | https://www.jstage.jst.go.jp/article/bbb/72/6/72_70778/_pdf; PMID18540103; DOI10.1271/bbb.70778; fractionation/purification, molecular properties, N-terminal alignment and equilibrium experiments | supports | Independently read all eight text pages, pp. 1475–1482, and visually inspected pp. 1476/1479 Figure 1, Figure 2 and Table 2. Native IFO3244 detergent-purified pDQD is membrane associated; no RSO/ISO topology test was performed. 191-kDa native versus 16-kDa subunit mass suggests twelve subunits; 189 kDa belongs to the other sDQD preparation. Figure 2C/prose disagree at one N-terminal residue. The short 621H GOX0437 comparison does not prove complete IFO3244 sequence identity. Reverse chemistry is measured; QDH interaction remains a hypothesis. |
| e-2004 | https://pubmed.ncbi.nlm.nih.gov/15598527/; PMID15598527; DOI10.1016/j.femsle.2004.10.014; abstractText in original Europe PMC capture | supports | Independently read abstract/metadata only. IFO3244 membrane QDH holoenzyme and prosthetic PQQ are supported; 65/21-kDa bands may reflect one-polypeptide proteolysis. No exact cleavage, sequence-equivalent construct, obligate heteromer or unread full-body acceptor panel is claimed. |
| e-1988 | https://pubmed.ncbi.nlm.nih.gov/3044290/; PMID3044290; DOI10.1007/BF00409714; abstractText in original Europe PMC capture | context_only | Independently read abstract/metadata only. PQQ-deficient Acinetobacter strain evidence is contextual, not direct ADP1 purified-enzyme evidence. The purported PDF acquisition is HTML and was not treated as a read full paper. |
| e-q59086 | https://rest.uniprot.org/uniprotkb/Q59086.json; Current original JSON: organism, sequence, comments, references and cross-references | supports | Reviewed ADP1 QuiA, 809 aa: PQQ ChEBI58442 cofactor annotation and membrane annotation with ECO0000305. Native cross-reference agrees; measured topology and cross-strain purified conditions are not inferred. |
| e-q59087 | https://rest.uniprot.org/uniprotkb/Q59087.json; Current original JSON: organism, sequence, comments, references and cross-references | supports | Reviewed ADP1 catabolic QuiB, current 272 aa, explicit erroneous extended-start cautions for AAC37158.1/CAG68555.1. Old 290-aa construct and proposed leader localization are not treated as the canonical molecule. |
| e-q43922 | https://rest.uniprot.org/uniprotkb/Q43922.json; Current original JSON: organism, sequence, comments, references and cross-references | supports | Reviewed ADP1 QuiC, 486 aa, DHS dehydration; gene/native identity agrees while original recombinant assay context remains edge-qualified. |
| e-q5fts6 | https://rest.uniprot.org/uniprotkb/Q5FTS6.json; Current original JSON: organism, sequence, comments, references and cross-references | context_only | Unreviewed G. oxydans 621H/NCBITaxon290633 GOX0437, 160 aa; automatic biosynthetic/assembly annotations and a short N-terminal comparison do not establish identity of the IFO3244 pDQD preparation. |
| e-reading | research/pathway_additions/2026-10-14-next-255/quinate/primary/reading-ledger.json | supports | Verified original-file hashes and compared the author reading ledger against independently inspected materials. Its broader figure coverage is author evidence; this reviewer claims only the independent bounds recorded in each evidence entry. |
| e-scope-correction | research/pathway_additions/2026-10-14-next-255/quinate/primary/claims-and-dispositions.json | supports | Final sa1-ac3 row explicitly identifies Acinetobacter sp. SA1 and A. calcoaceticus AC3 and excludes transfer to ADP1. This corrects a pending author-session attribution before erroneous maintained YAML existed. Issue 540 is tracked as a provenance/scope correction, without invented structured finding lineage. |
| e-imodulon | research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/imodulondb-datasets.md | context_only | The structured iModulonDB runner returned 28 dataset entries. None covers A. baylyi ADP1 or G. oxydans. A. baumannii is not the target; E. coli recombinant-host assays do not imply native pathway/module context. No downstream gene search was applicable. |
| e-lineage | reviews/structured/ | context_only | An ignored/hidden-inclusive search for issue540, SA1, AC3, the exact pathway identifier and slug found only unrelated PSA1 substring occurrences in an older legacy review. No structured predecessor for this target or the pending attribution correction was found within the complete local structured-review tree. |
| e-gates | research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/gate-acceptance.json | supports | Independently verified root-executed full-repository gate receipts, original log hashes and final tested-core file hashes. These are shared actual executions, not a second reviewer full-suite run. |

## Limits And Additional Notes

- PMID7592351 was read as author-rendered full main body, Table 1 and captions, with original figure rasters/raw PDF unavailable; no claim of a complete contiguous reference-list capture. PMID15598527 and PMID3044290 are abstract-only. Native database assertions remain separately attributed and are not disguised as quotations from unread bodies.
- For PMID14586098/14586099/18540103 the reviewer read full text and the decisive images described in individual evidence entries; broader author figure-reading claims are not adopted as independent coverage.
- Generic native quinone classes do not establish every class member as a substrate or the physiological acceptor in each strain. PQQ versus quinone roles remain distinct; complete same-strain purified pathway/respiratory reconstitution is not asserted.
- Precise pDQD periplasmic topology, direct QDH interaction, whole IFO3244 protein sequences/cleavage states and the exact 621H correspondence remain unresolved. Canonical native labels containing periplasmic are preserved as authority labels while edge assertions explicitly restrict localization.
- All 51 source-neighborhood dispositions concern a bounded native traversal, not all enzymes in nature or exhaustive primary-literature coverage. Excluded source objects can remain valid in their own pathways.
- Full-repository gates were executed once by the root curator and independently verified through original logs and unchanged tested-core hashes; they were not duplicated by this reviewer. Shared validation is not scientific proof.
- This working-tree review binds exact file bytes and available external-original hashes; it does not prove Git commit membership or lasting availability of external scratch payloads. Commit/blob retention must be checked before publication.
- Initial formal input inspection used the first maintained target hash; the final record was reread in full and all-edge checks repeated after source-locator/spacing changes. The final inspect binds final bytes rather than silently refreshing hashes.
- Issue 540 concerns an author-session attribution corrected before erroneous maintained YAML existed. No earlier structured finding was saved for it, so this observation uses evidence-linked assessment rather than fabricated previous_occurrences.
- The initial iModulonDB request failed under restricted DNS; the authorized public catalog retry succeeded. The dataset mismatch is not negative biological evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T164250Z-next255-quinate-scientific
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of quinate degradation I
started_at: '2026-10-14T16:23:07Z'
finished_at: '2026-10-14T16:42:50Z'
reviewer:
  identity: codex:/root/next255_science_review
  kind: agent
  independence: independent
  independence_basis: Did not author or edit maintained pathway, authorities, history,
    pages or author research. Independently read original source payloads and primary
    material, identified the pending SA1/AC3 attribution correction, and owns only
    reviewer scratch receipts and this immutable review bundle.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: Exact three-step native route supported within stated assay, molecular-state
  and source-access bounds
scientific_review: true
summary: 'Independently assessed the entire frozen quinate degradation I record: all
  37 edges and all 51 bounded native biological source objects. Concrete molecular
  identities, reaction direction and class scope, six catalyst preparations, taxon
  contexts and edge-level evidence are supported. The pending author attribution correction
  tracked by issue 540 is reflected in final evidence; no erroneous maintained record
  or structured predecessor is invented. All required gates pass on the reviewed bytes.
  No open scientific findings remain.'
source:
  git_revision: bfa3f5ed0e843472c0fd173ce91df2a90dd4ddb2
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: f0d394f29cad1a1cd6a004abceb5f59f8e567d6b885cd6c4ff07c629c4d6db7a
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/identifier_sources.json
    sha256: 5021eff782c83cee42c848aeeb339724f700c3dd874707e3ea75a76cb56128f7
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 1115c53b4bc1e1104a03e612cd1f2b08ae1d72e3d6538eb864bd6c084c90f7bf
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 32fdd091eb94869fa437cc8cbafaf2ae69458ef55f72031586dbc69561cfe8fb
    role: context
  - path: data/pathways/quinate-degradation-i.yaml
    sha256: a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 072884773d626ea909bd1e4f275901f0a6053f660d5e68a294ee54149b6496b0
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/all-edge-and-reference-audit.json
    sha256: cbd342e9378f06642e3cb481a411157be0c6badc1fbb399da901a7459d10bef3
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/edge_audit.py.txt
    sha256: 83af002c0e63e4f489be0c59c48628ad8eec8a9f7f30d7e2f37ab042eb0a9b53
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/gate-acceptance.json
    sha256: 73be041be2b35bba5da3db3756ef64143f3e60ce8b82728e45fc844667f0fa42
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/gate_acceptance.py.txt
    sha256: d9879f1d057dac49d3b06208f3b8c9211f4263e7223448130d34fabfcd990f0a
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/imodulondb-datasets.md
    sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/independent-source-checks.json
    sha256: 977110c4e1fca87485ef4f9e050c26ff3c503da8bebd9070d5a19832eb1c707e
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/independent_sources.py.txt
    sha256: 509e43c330c2c90979e919506b23d92c19d783a133cc3b0349b6137c644b724a
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/native-neighborhood-audit.json
    sha256: 1b374333e3248ca485f161d183ad2058412fce2e558e58db4dd36db0cab76ebe
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/native_neighborhood_audit.py.txt
    sha256: c2ff91ccca76c5064136703a4e90bff87aebfd9f12c205187dfe915f0ca782d4
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/native/biological-coverage.json
    sha256: bf18e55e39e72860951aa7d96e6d1c593ed2aaecb65ab7f781b3b4cc011894de
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/primary/HANDOFF.md
    sha256: 79cf599000c1107072c888daa5461ff0faced3192d80248a8ee97ee04a5d9ac2
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/primary/claims-and-dispositions.json
    sha256: 954248ea29be6c0a82519c8bdc041eabcd22c84c47762d7d5d7637b3a1c51b64
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/primary/constructs-ledger.json
    sha256: 860f2fb588f692294287e94c1160654b7e548fdf978ed0acbc103e1e4340dbf6
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/primary/reading-ledger.json
    sha256: e08670c0d0843e7a59d963799a691c6907cd3765cdd9bd0bd2b30c9fe651908f
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/validation/final-input-preservation.json
    sha256: 37e31421c35a590b6155aa56cbfcda9638361a8c050ea269d0c609f43cd1142c
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/validation/receipts.json
    sha256: 4eb455068b37a25f9ccc2be3537a55f143e04c5a82d04bf0a318d1f42658235a
    role: context
  - path: research/pathway_additions/2026-10-14-next-255/quinate/validation/tested-core-input-hashes.json
    sha256: 2d47bd9d7ef6557f34fdca62559a0ea3d0436ee2e742b44102cdf50b6b167397
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
scope:
  description: One maintained pathway, all 37 mechanistic edges, three reactions,
    17 participants, two taxa, 31 references and all 51 objects in the declared native
    biological neighborhood; independent primary reading with explicit access bounds.
  selection: Exact MetaCyc:QUINATEDEG-PWY target selected for complete independent
    review; no edge or source-neighborhood sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:QUINATEDEG-PWY
  exclusions:
  - target: Other 251 maintained pathways
    reason: Not scientifically rereviewed; included only in shared full-corpus deterministic
      gates.
  - target: Additional organisms, routes, 2010/2021/2022 expression leads and unread
      full papers
    reason: Outside exact target/native-neighborhood scope; no literature-exhaustion
      or broader route claim.
targets:
- target_id: MetaCyc:QUINATEDEG-PWY
  path: data/pathways/quinate-degradation-i.yaml
  label: quinate degradation I
  kind: maintained
  record_class: PathwayRecord
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-i.yaml
    role: maintained_record
checks:
- check_id: inspect
  name: Final frozen input inspection
  status: passed
  required: true
  summary: Initial target was inspected before judgement; complete final record was
    reread after changes. Final inspect binds the exact target and retained context
    inputs.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: python -B scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-255-science-review/targets.yaml
    --input <declared context inputs>
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-record
- check_id: all-edges
  name: All-edge and reference audit
  status: passed
  required: true
  summary: All 37 unique triples, 29 source hashes and seven literal quote occurrences
    pass.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: python -B /private/tmp/pathwaymech-next-255-science-review/edge_audit.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-edge
- check_id: source-identities
  name: Independent native/ChEBI/Rhea verification
  status: passed
  required: true
  summary: Six concrete molecular identities, three native reaction side/direction
    declarations and 35 raw-RDF node comparisons pass.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: python3 /private/tmp/pathwaymech-next-255-science-review/independent_sources.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-chemical
- check_id: neighborhood
  name: Complete bounded native biological neighborhood
  status: passed
  required: true
  summary: Independent original-slot traversal produces all 51 reviewed objects and
    agrees with 13 retained/38 excluded dispositions.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: python3 /private/tmp/pathwaymech-next-255-science-review/native_neighborhood_audit.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-neighborhood
- check_id: imodulon
  name: Structured iModulonDB applicability
  status: passed
  required: false
  summary: Catalog acquisition succeeded; no matching target organism/dataset, so
    gene/module queries are not applicable. Absence does not weaken biological evidence.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-imodulon
- check_id: gate-1
  name: just render-pages
  status: passed
  required: true
  summary: Root executed this full-repository gate; reviewer independently verified
    original output hash, exit status and unchanged tested inputs. Generated all maintained
    pages/graph data successfully.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: just render-pages
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-2
  name: just validate
  status: passed
  required: true
  summary: Root executed this full-repository gate; reviewer independently verified
    original output hash, exit status and unchanged tested inputs. Full closed-schema,
    identifier/label, evidence and history/review validation passed.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: just validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-3
  name: just test
  status: passed
  required: true
  summary: Root executed this full-repository gate; reviewer independently verified
    original output hash, exit status and unchanged tested inputs. Full pytest suite
    passed; complete terminal summary retained in original log.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: just test
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-4
  name: just lint
  status: passed
  required: true
  summary: Root executed this full-repository gate; reviewer independently verified
    original output hash, exit status and unchanged tested inputs. Full Ruff lint
    passed.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: just lint
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-5
  name: just vendored-check
  status: passed
  required: true
  summary: Root executed this full-repository gate; reviewer independently verified
    original output hash, exit status and unchanged tested inputs. Canonical vendored
    helper check passed.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-6
  name: git diff --check
  status: passed
  required: true
  summary: Root executed this full-repository gate; reviewer independently verified
    original output hash, exit status and unchanged tested inputs. Whitespace check
    passed.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/quinate-degradation-i.yaml
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Read the entire final frozen record and independently assessed all 37 edges,
    three reactions, 17 participants, two taxa and 31 references. Final SHA a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb;
    initial inspected draft was reread after spacing and six Rhea contains1 locator
    corrections.
  snapshot_sha256: a0c21af8e01b7a2653b226656b405fc197b0376b2d9ea4a6dbb6d003a3cc36cb
- evidence_id: e-edge
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/all-edge-and-reference-audit.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: All 37 exact triples reproduce from inspected native assertions and independently
    adjudicated primary support; 29 hash-bearing references match actual originals;
    all seven quote occurrences literally match inspected text with whitespace normalization
    only. Deterministic checks complement scientific reading.
  snapshot_sha256: cbd342e9378f06642e3cb481a411157be0c6badc1fbb399da901a7459d10bef3
- evidence_id: e-neighborhood
  kind: database
  reference: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/native-neighborhood-audit.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: 'Independently traversed original native reaction/activity/enzyme/component/auxiliary-activity/regulation
    slots: 16 direct activities, 16 enzymes, five subunits, seven auxiliary activities
    and seven regulations. All 51 original objects have explicit reviewer dispositions:
    13 retained with scope, 38 excluded. Exact set and decisions agree with the author
    ledger, without treating it as approval.'
  snapshot_sha256: 1b374333e3248ca485f161d183ad2058412fce2e558e58db4dd36db0cab76ebe
- evidence_id: e-chemical
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/independent-source-checks.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Six native/ChEBI full InChI and InChIKey identities independently agree.
    Reparsed original Rhea 142 RDF and matched all 35 projected nodes. Exact native
    three-step side/direction semantics retained; broad native quinone classes are
    not equated to narrower Rhea 23673 participants.
  snapshot_sha256: 977110c4e1fca87485ef4f9e050c26ff3c503da8bebd9070d5a19832eb1c707e
- evidence_id: e-pathway
  kind: database
  reference: https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:QUINATEDEG-PWY
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Inspected full MetaCyc 27.0 native pathway, reaction-list, layout, predecessor
    ordering, comments and evidence. Exact boundary is quinate through DHQ/DHS to
    protocatechuate; source taxa are ADP1 and G. oxydans, not every isolate or a purified
    one-strain reconstruction.
  locator: /ptools-xml/Pathway[@frameid="QUINATEDEG-PWY"]
  snapshot_sha256: 51d1f25faf0545dfdf14baf69f8f3647ab33ed564ef4e6117146c06f98e5153b
- evidence_id: e-1994
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC197224/
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently read all eight official page scans, pp. 7659–7666, including
    methods, results, discussion, references, figures and Table 1. ADP1 genetic/complementation
    and extract evidence supports QuiA; 809-aa sequence and membrane predictions do
    not constitute direct topology measurement. Standard QDH assay in recombinant
    DH5alpha(pZR504) was undetectable even with PQQ. Protocatechuate induction and
    quinate metabolism dependence do not establish direct regulator-ligand binding.
  locator: PMID8002591; DOI10.1128/jb.176.24.7659-7666.1994; original scan hashes
    in retained primary/reading-ledger.json
- evidence_id: e-1995
  kind: primary_source
  reference: https://www.researchgate.net/publication/15607491_Unusual_ancestry_of_dehydratases_associated_with_quinate_catabolism_in_Acinetobacter_calcoaceticus
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently read author-rendered complete main body, Table 1 and figure
    captions, pp. 5971–5978, with original figure images unavailable. Native thermolabile
    catabolic QuiB evidence is distinct from biosynthetic AroD and the old 290-aa
    recombinant start annotation. QuiC pZR564 is the 2.0-kb HindIII ADP1 insert in
    E. coli DH5alpha; no tag or expressed termini measured. Text/Table 1 pBSK/pBKS
    conflict retained. QuiC is DHS-dehydrating; native DHQ and numeric-unit prose
    errors are not copied. No demonstrated QuiX transporter edge.
  locator: PMID7592351; DOI10.1128/jb.177.20.5971-5978.1995; methods, Table 1, cloned
    enzyme results and discussion
- evidence_id: e-2003-qdh
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2115/_pdf
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently read all nine text pages, pp. 2115–2123, and visually verified
    decisive pp. 2118/2120 Tables 1/2 and adjacent purification explanation. SA1 is
    Acinetobacter sp.; AC3 is A. calcoaceticus. Gluconobacter purification was abandoned
    because of co-purifying ADH. PQQ/calcium reconstitution, ferricyanide/PMS-DCIP/DCIP/ubiquinone-2
    and membrane oxygen-uptake evidence concern those Acinetobacter preparations,
    not ADP1 or IFO3244; neither universal quinone specificity nor full respiratory-chain
    reconstitution follows.
  locator: PMID14586098; DOI10.1271/bbb.67.2115; pp. 2116–2122, Tables 1/2 and purification/acceptor
    sections
  snapshot_sha256: 618dd246b5755894346615c09f71bdfb5165115469f4014895cb9f10647e1937
- evidence_id: e-2003-dhs
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2124/_pdf
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently read all eight text pages, pp. 2124–2131, and visually inspected
    p. 2129 Figure 5 and fractionation text. IFO3244 partially purified cytoplasmic
    DHSase is separated from DQD and supports qualitative protocatechuate formation.
    No homogeneous enzyme, complete sequence or full same-strain three-enzyme reconstitution
    is asserted. NADP/shikimate-dehydrogenase coupling is not assigned as a DHSase
    cofactor.
  locator: PMID14586099; DOI10.1271/bbb.67.2124; methods and cytoplasmic enzyme fractionation/results
  snapshot_sha256: fe0a94a47666acfe3a85aed78521589dd0e251b352f3dbfb8bba93df76351f6c
- evidence_id: e-2008
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/72/6/72_70778/_pdf
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently read all eight text pages, pp. 1475–1482, and visually inspected
    pp. 1476/1479 Figure 1, Figure 2 and Table 2. Native IFO3244 detergent-purified
    pDQD is membrane associated; no RSO/ISO topology test was performed. 191-kDa native
    versus 16-kDa subunit mass suggests twelve subunits; 189 kDa belongs to the other
    sDQD preparation. Figure 2C/prose disagree at one N-terminal residue. The short
    621H GOX0437 comparison does not prove complete IFO3244 sequence identity. Reverse
    chemistry is measured; QDH interaction remains a hypothesis.
  locator: PMID18540103; DOI10.1271/bbb.70778; fractionation/purification, molecular
    properties, N-terminal alignment and equilibrium experiments
  snapshot_sha256: b5dd24d357efdd77f5977528a0056085f069bfdfc927cf4a602abae1c905ca76
- evidence_id: e-2004
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15598527/
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently read abstract/metadata only. IFO3244 membrane QDH holoenzyme
    and prosthetic PQQ are supported; 65/21-kDa bands may reflect one-polypeptide
    proteolysis. No exact cleavage, sequence-equivalent construct, obligate heteromer
    or unread full-body acceptor panel is claimed.
  locator: PMID15598527; DOI10.1016/j.femsle.2004.10.014; abstractText in original
    Europe PMC capture
  snapshot_sha256: 787511b9e5396984ebb44ee38cbb4584352ab5959511bf8639c25d3f8ddaa5c0
- evidence_id: e-1988
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/3044290/
  accessed_at: '2026-10-14T16:42:50Z'
  support: context_only
  summary: Independently read abstract/metadata only. PQQ-deficient Acinetobacter
    strain evidence is contextual, not direct ADP1 purified-enzyme evidence. The purported
    PDF acquisition is HTML and was not treated as a read full paper.
  locator: PMID3044290; DOI10.1007/BF00409714; abstractText in original Europe PMC
    capture
  snapshot_sha256: 787511b9e5396984ebb44ee38cbb4584352ab5959511bf8639c25d3f8ddaa5c0
- evidence_id: e-q59086
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q59086.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: 'Reviewed ADP1 QuiA, 809 aa: PQQ ChEBI58442 cofactor annotation and membrane
    annotation with ECO0000305. Native cross-reference agrees; measured topology and
    cross-strain purified conditions are not inferred.'
  locator: 'Current original JSON: organism, sequence, comments, references and cross-references'
  snapshot_sha256: 25d86e8505af8ac4923f508fa03b7fd2aadfeaf1dd1dea924faeec64c532eafe
- evidence_id: e-q59087
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q59087.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Reviewed ADP1 catabolic QuiB, current 272 aa, explicit erroneous extended-start
    cautions for AAC37158.1/CAG68555.1. Old 290-aa construct and proposed leader localization
    are not treated as the canonical molecule.
  locator: 'Current original JSON: organism, sequence, comments, references and cross-references'
  snapshot_sha256: aae8268077f8c3115197025dd96e62bbf3abc0071be8d9f4b5419fea3eab9ce8
- evidence_id: e-q43922
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q43922.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Reviewed ADP1 QuiC, 486 aa, DHS dehydration; gene/native identity agrees
    while original recombinant assay context remains edge-qualified.
  locator: 'Current original JSON: organism, sequence, comments, references and cross-references'
  snapshot_sha256: 7b18529d44b49af1f01be42a2734ef35a8e4f4f814328a166f29273ac8e261c1
- evidence_id: e-q5fts6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q5FTS6.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: context_only
  summary: Unreviewed G. oxydans 621H/NCBITaxon290633 GOX0437, 160 aa; automatic biosynthetic/assembly
    annotations and a short N-terminal comparison do not establish identity of the
    IFO3244 pDQD preparation.
  locator: 'Current original JSON: organism, sequence, comments, references and cross-references'
  snapshot_sha256: cf4a7dadd5a115bf9e5a700eaee7d5d7e01af12930d3d2047ff16d503530b10a
- evidence_id: e-reading
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-255/quinate/primary/reading-ledger.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Verified original-file hashes and compared the author reading ledger against
    independently inspected materials. Its broader figure coverage is author evidence;
    this reviewer claims only the independent bounds recorded in each evidence entry.
  snapshot_sha256: e08670c0d0843e7a59d963799a691c6907cd3765cdd9bd0bd2b30c9fe651908f
- evidence_id: e-scope-correction
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-255/quinate/primary/claims-and-dispositions.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Final sa1-ac3 row explicitly identifies Acinetobacter sp. SA1 and A. calcoaceticus
    AC3 and excludes transfer to ADP1. This corrects a pending author-session attribution
    before erroneous maintained YAML existed. Issue 540 is tracked as a provenance/scope
    correction, without invented structured finding lineage.
  snapshot_sha256: 954248ea29be6c0a82519c8bdc041eabcd22c84c47762d7d5d7637b3a1c51b64
- evidence_id: e-imodulon
  kind: search
  reference: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/imodulondb-datasets.md
  accessed_at: '2026-10-14T16:42:50Z'
  support: context_only
  summary: The structured iModulonDB runner returned 28 dataset entries. None covers
    A. baylyi ADP1 or G. oxydans. A. baumannii is not the target; E. coli recombinant-host
    assays do not imply native pathway/module context. No downstream gene search was
    applicable.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  search_scope: Complete returned public datasets catalog, queried through kg-microbe-sources
    imodulondb datasets; no assertion about every possible transcriptomic resource.
    Not a filesystem absence claim and not negative biological evidence.
- evidence_id: e-lineage
  kind: search
  reference: reviews/structured/
  accessed_at: '2026-10-14T16:42:50Z'
  support: context_only
  summary: An ignored/hidden-inclusive search for issue540, SA1, AC3, the exact pathway
    identifier and slug found only unrelated PSA1 substring occurrences in an older
    legacy review. No structured predecessor for this target or the pending attribution
    correction was found within the complete local structured-review tree.
  search_scope: 'Actual command: rg --no-ignore --hidden -n issues/540|SA1|AC3|QUINATEDEG-PWY|quinate-degradation-i
    reviews/structured; all local structured bundles including ignored/hidden files.
    Search expression was passed as one quoted shell argument. External repositories
    and GitHub discussions are outside this lineage search.'
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-255/quinate/independent-scientific/gate-acceptance.json
  accessed_at: '2026-10-14T16:42:50Z'
  support: supports
  summary: Independently verified root-executed full-repository gate receipts, original
    log hashes and final tested-core file hashes. These are shared actual executions,
    not a second reviewer full-suite run.
  snapshot_sha256: 73be041be2b35bba5da3db3756ef64143f3e60ce8b82728e45fc844667f0fa42
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact native three-step quinate degradation I boundary
  outcome: supported
  summary: The target preserves the complete native three-step route and its specific
    taxon contexts. It excludes NAD-dependent sibling pathways, aromatic biosynthesis,
    AsbF petrobactin biology and the same protein's neighboring shikimate activity.
    Shared downstream reactions do not merge these pathways.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-record
  - e-pathway
  - e-neighborhood
  - e-1994
  - e-1995
- assessment_id: a-chemistry
  area: grounding
  topic: Molecular identities, quinone class scope and reversibility
  outcome: supported
  summary: Quinate/DHQ/DHS/protocatechuate/water/PQQ identities agree at full InChI
    and InChIKey level. Native broad quinones/quinols and initial reaction remain
    native because narrower Rhea classes are not exact scope matches. PQQ is an enzyme
    cofactor, not the net quinone acceptor. Middle RHEA21099 remains reversible while
    graph edges select catabolic flux; final RHEA24849 and the six contains1 side
    locators agree with original RDF.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-chemical
  - e-edge
  - e-pathway
  - e-2008
  - e-q59086
  - e-2004
- assessment_id: a-enzymes
  area: evidence
  topic: Taxon, assay and construct scope for all six catalysts
  outcome: supported
  summary: ADP1 QuiA/QuiB/QuiC functions have genetic/extract or recombinant support,
    with current exact protein identities and explicit old-start/construct limits.
    IFO3244 QDH, pDQD complex and DHSase retain preparation identities and evidence
    tiers. Native erroneous citation/prose content is not converted into direct ADP1
    purified evidence or a wrong substrate claim.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-1994
  - e-1995
  - e-2003-qdh
  - e-2003-dhs
  - e-2008
  - e-2004
  - e-q59086
  - e-q59087
  - e-q43922
  dimensions:
  - name: taxon_scope
    value: ADP1/NCBITaxon62977 and IFO3244 preparations within G. oxydans/NCBITaxon442
    definition: Native context does not assert every isolate expresses the whole route.
      SA1/AC3 and 621H remain distinct.
    evidence_ids:
    - e-pathway
    - e-2003-qdh
    - e-2008
    - e-q5fts6
  - name: evidence_tier
    value: Native database assertions plus inspected genetic/extract/partial-purification/purification
      primary support; 2004 abstract-only
    definition: Evidence type is retained per edge and does not imply a purified three-enzyme
      reconstitution in one strain.
    evidence_ids:
    - e-edge
    - e-1994
    - e-1995
    - e-2003-dhs
    - e-2008
    - e-2004
- assessment_id: a-assembly
  area: representation
  topic: Molecular state, component role and localization
  outcome: supported
  summary: MONOMER-0 is represented as a complex with MONOMER-15328 membership, not
    isolated-subunit catalysis. A suggested twelve-subunit state is qualified, and
    the short 621H sequence comparison is not exact identity. Broad membrane association
    is supported; precise periplasmic topology and direct QDH-pDQD interaction are
    not promoted. Cytoplasmic recovery is preparation context rather than exclusive
    localization.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-2008
  - e-2003-dhs
  - e-2004
  - e-q59086
  - e-q5fts6
  - e-neighborhood
  - e-record
- assessment_id: a-completeness
  area: completeness
  topic: Every local edge and complete bounded source neighborhood
  outcome: supported
  summary: All 37 maintained edges and all 51 native biological neighborhood objects
    were reviewed. Exclusions are explicit and biologically justified; no available
    native regulatory object is silently promoted onto the retained pathway. Structured
    iModulonDB coverage is not applicable. This is complete coverage of the declared
    record/native neighborhood, not exhaustion of literature or all organisms.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-edge
  - e-neighborhood
  - e-imodulon
  - e-record
- assessment_id: a-provenance
  area: provenance
  topic: Source assertions, quotes and already-applied author correction
  outcome: supported
  summary: Original hashes, structured locators and literal quote checks support traceability.
    The SA1/AC3 genus mistake was in a pending session attribution; corrected author
    evidence now states Acinetobacter and no erroneous maintained pathway had been
    written. This clean record review reports the applied correction without inventing
    a resolved structured predecessor.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-edge
  - e-reading
  - e-scope-correction
  - e-2003-qdh
  - e-lineage
- assessment_id: a-gates
  area: schema
  topic: Full-repository required checks on reviewed bytes
  outcome: supported
  summary: Documented validation, test, lint and whitespace checks pass, alongside
    rendering and vendored checks. Reviewer verified actual root receipts and final
    unchanged tested-core hashes; these deterministic results supplement independent
    scientific evidence.
  target_ids:
  - MetaCyc:QUINATEDEG-PWY
  evidence_ids:
  - e-gates
  - e-record
findings: []
actions: []
limitations:
- PMID7592351 was read as author-rendered full main body, Table 1 and captions, with
  original figure rasters/raw PDF unavailable; no claim of a complete contiguous reference-list
  capture. PMID15598527 and PMID3044290 are abstract-only. Native database assertions
  remain separately attributed and are not disguised as quotations from unread bodies.
- For PMID14586098/14586099/18540103 the reviewer read full text and the decisive
  images described in individual evidence entries; broader author figure-reading claims
  are not adopted as independent coverage.
- Generic native quinone classes do not establish every class member as a substrate
  or the physiological acceptor in each strain. PQQ versus quinone roles remain distinct;
  complete same-strain purified pathway/respiratory reconstitution is not asserted.
- Precise pDQD periplasmic topology, direct QDH interaction, whole IFO3244 protein
  sequences/cleavage states and the exact 621H correspondence remain unresolved. Canonical
  native labels containing periplasmic are preserved as authority labels while edge
  assertions explicitly restrict localization.
- All 51 source-neighborhood dispositions concern a bounded native traversal, not
  all enzymes in nature or exhaustive primary-literature coverage. Excluded source
  objects can remain valid in their own pathways.
- Full-repository gates were executed once by the root curator and independently verified
  through original logs and unchanged tested-core hashes; they were not duplicated
  by this reviewer. Shared validation is not scientific proof.
- This working-tree review binds exact file bytes and available external-original
  hashes; it does not prove Git commit membership or lasting availability of external
  scratch payloads. Commit/blob retention must be checked before publication.
notes:
- Initial formal input inspection used the first maintained target hash; the final
  record was reread in full and all-edge checks repeated after source-locator/spacing
  changes. The final inspect binds final bytes rather than silently refreshing hashes.
- Issue 540 concerns an author-session attribution corrected before erroneous maintained
  YAML existed. No earlier structured finding was saved for it, so this observation
  uses evidence-linked assessment rather than fabricated previous_occurrences.
- The initial iModulonDB request failed under restricted DNS; the authorized public
  catalog retry succeeded. The dataset mismatch is not negative biological evidence.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/540
tags:
- next255
- quinate
- scientific
- independent
- metacyc
- full-edge-review
```
