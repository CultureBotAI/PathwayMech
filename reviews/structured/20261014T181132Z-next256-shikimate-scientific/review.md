# Independent scientific review of shikimate degradation I

- Review: 20261014T181132Z-next256-shikimate-scientific
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T17:36:57Z
- Finished UTC: 2026-10-14T18:11:32Z
- Reviewer: codex:/root/next256_scientific_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 31 edges of the frozen shikimate degradation I record and all 17 bounded native biological objects plus 9 supplemental contexts independently assessed. Exact chemical identities and reaction class scope, four catalysts, PQQ roles, taxa, qualifiers and four transcription-regulation edges are supported within stated limits. Minor issue 542 attribution was corrected and exactly rechecked. All required gates pass on final bytes; no open scientific findings remain.

## Scope And Provenance

One maintained pathway, all 31 edges, 16 participants, two reactions, three taxa, 27 references and full declared native neighborhood, with independent primary reading bounds.

Selection: Exact MetaCyc:SHIKIMATEDEG-PWY selected for complete record and bounded native-neighborhood review; no edge sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b645cc4c0afd75f3eff521376b75602a3c2ad679.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:SHIKIMATEDEG-PWY | data/pathways/shikimate-degradation-i.yaml | maintained | shikimate degradation I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Final frozen input inspection | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Formal initial target inspection binds draft hash; final complete target and corrected sentence rechecked before final input inspection. |
| All 31 edges and original-reference audit | passed | True | MetaCyc:SHIKIMATEDEG-PWY | 31 unique triples, 26 reference hashes and 9 literal quote occurrences checked; all per-source quote totals within 25 words. |
| Independent chemical/native/Rhea audit | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Five concrete InChI/key mappings and 25 original RDF nodes agree; source-class scope retained. |
| Complete bounded native neighborhood | passed | True | MetaCyc:SHIKIMATEDEG-PWY | 17 independently derived biological objects and 9 supplemental contexts assessed. |
| Structured iModulonDB applicability | passed | False | MetaCyc:SHIKIMATEDEG-PWY | Catalog returned successfully; no matching target dataset, downstream queries inapplicable. |
| Superseded attempt: just render-pages | passed | False | MetaCyc:SHIKIMATEDEG-PWY | Actual archived result retained. The first full suite reported 1 failed, 4,959 passed and 3 skipped; only the page reflecting the appended history correction was stale. The complete final rerun supersedes this attempt. |
| Superseded attempt: just validate | passed | False | MetaCyc:SHIKIMATEDEG-PWY | Actual archived result retained. The first full suite reported 1 failed, 4,959 passed and 3 skipped; only the page reflecting the appended history correction was stale. The complete final rerun supersedes this attempt. |
| Superseded attempt: just test | failed | False | MetaCyc:SHIKIMATEDEG-PWY | Actual archived result retained. The first full suite reported 1 failed, 4,959 passed and 3 skipped; only the page reflecting the appended history correction was stale. The complete final rerun supersedes this attempt. |
| Superseded vendored-check DNS failure | failed | False | MetaCyc:SHIKIMATEDEG-PWY | The actual failed invocation could not fetch the pinned canonical GitHub artifact (DNS Errno 8). An identical bounded retry passed on unchanged inputs. |
| History actor correction validation | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Actual root validate-history receipt and log verified: 443 valid history records. Final full-run inputs also include history. |
| just render-pages | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Root executed the final run; reviewer checked actual log hash, successful exit and all unchanged tested inputs. Generated all maintained pages/graph data successfully. |
| just validate | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Root executed the final run; reviewer checked actual log hash, successful exit and all unchanged tested inputs. Full closed-schema, identifier/label, evidence and history validation passed. |
| just test | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Root executed the final run; reviewer checked actual log hash, successful exit and all unchanged tested inputs. Final full pytest suite: 4960 passed, 3 skipped. Complete terminal summary retained in original log. |
| just lint | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Root executed the final run; reviewer checked actual log hash, successful exit and all unchanged tested inputs. Full Ruff lint passed. |
| just vendored-check | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Root executed the final run; reviewer checked actual log hash, successful exit and all unchanged tested inputs. Canonical vendored helper check passed. |
| git diff --check | passed | True | MetaCyc:SHIKIMATEDEG-PWY | Root executed the final run; reviewer checked actual log hash, successful exit and all unchanged tested inputs. Whitespace check passed. |

## Scientific And Domain Assessments

### Exact complete two-step shikimate I route

identity: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

The target preserves both native reactions in selected forward order and ends at protocatechuate. Quinate-specific QuiB, NAD-dependent sibling variants, petrobactin AsbF and downstream mineralization remain distinct. Similar names or shared DHS chemistry do not establish pathway equivalence.

### Exact molecule and reaction scope

grounding: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

Shikimate, DHS, PCA, water and PQQ identities match complete native/pinned ChEBI InChI and stereochemistry/protonation. First reaction and quinone/quinol classes remain native; narrower Rhea 47049 is not used as an exact replacement. RHEA 24849 sides and contains1 locators agree. PQQ cofactor is distinct from the consumed acceptor.

### All four catalyst identities and preparations

evidence: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

ADP1 QuiA has native/genetic support and current protein identity; SA1/AC3 purified kinetics are excluded. ADP1 QuiC carries its heterologous crude-extract qualification. Gox DHSase retains partial cytoplasmic preparation and Gox QDH possible proteolysis. Shikimate activity of the latter is attributed to inspected native comment, not unread 2004 body.

### Gene expression regulation and physical component roles

graph: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

PcaU and PCA regulation targets are exact native quiA/quiC genes. The original 2005 Northern experiments support transcript-level influence; the shared quiC–quiX probe and constitutive quiAp limits are explicit. No direct binding/promoter sequence/enzymatic activation is invented. Gene targets are physical entities and cytoplasm/membrane remain cellular components.

### Historical taxa and location limits

scope: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

ADP1, historical LMD 79.41 and Gox enzyme preparations remain separate. LMD 79.41 Table 1 growth/PQQ rescue is valid context without modern retyping. Gox edges assert oxidative enzyme evidence rather than growth/mineralization. Broad membrane evidence does not prove precise topology; DHSase cytoplasmic recovery is preparation context.

### Full local graph and declared source-neighborhood coverage

completeness: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

All 31 edges and 17 bounded native biological objects have evidence-backed dispositions; nine supplemental native contexts are assessed. No duplicate genus-level MONOMER1521 catalyst is invented. Outside-variant proteins/regulation and adjacent QuiA quinate activity are explicitly excluded. This is not a claim that literature or pathways are exhausted.

### Applied issue 542 correction and source traceability

provenance: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

The unsupported attribution of previous Gox observations to 1988 experiments was removed. Exact byte reconstruction confirms the only record change. Original references, literal quotes and scientific scoping pass. No unresolved defect remains, and no structured predecessor finding is fabricated.

### Full corpus checks on final bytes

schema: supported. Targets: MetaCyc:SHIKIMATEDEG-PWY.

Required validate, test, lint, whitespace and supporting rendering/vendored checks succeeded on unchanged final core inputs. Original receipts independently verified; deterministic checks supplement primary scientific review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/shikimate-degradation-i.yaml | supports | Entire final record inspected: 31 edges, 16 participants, two reactions, three taxa and 27 references. Final SHA ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808. Initial inspected record differed by one removed unsupported historical-attribution sentence; correction reconstructed and verified exactly. |
| e-edge | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/all-edge-and-reference-audit.json | supports | All 31 exact triples reproduce from native slots and independently adjudicated primary support. All 26 hash-bearing references match actual originals; nine quote occurrences literally match inspected text with whitespace normalization. Per-source verbatim totals remain 6, 12, 17 and 20 words. This replay complements scientific reading. |
| e-neighborhood | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/native-neighborhood-audit.json | supports | Independent native traversal finds seven direct activities, seven proteins, one recursive subunit, one auxiliary activity and one regulation: 17 objects, six retained with scope and 11 excluded. Nine supplemental native objects are separately assessed. No source-neighborhood sampling. |
| e-chemistry | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent-source-checks.json | supports | Five concrete native/ChEBI full InChI and InChIKey mappings match independently read pinned ChEBI 255 SQL. All 25 projected Rhea nodes match original Rhea 142 RDF. Native broad quinones/quinols are not exactly equated to Rhea 47049 narrower 1,4-benzoquinone/hydroquinone participants; RHEA 24849 exact sides match. |
| e-primary | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent-primary-reading.json | supports | Independent reading bounds and original hashes for seven primary sources: all 1994 scans; relevant 1995 author text/captions; 1988 author-reprint chapter; decisive 2003 strain/fractionation passages and images; 2004 abstract; 2005 original transcription methods/results/discussion and Figures 6–7. Broader author reading is not adopted as independent coverage. |
| e-pathway | https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:SHIKIMATEDEG-PWY; /ptools-xml/Pathway[@frameid="SHIKIMATEDEG-PWY"] | supports | Full MetaCyc 27.0 object establishes exactly SHIKIMATE-PQQ-RXN then DHSHIKIMATE-DEHYDRO-RXN, shikimate through DHS to PCA. Pathway membership, selected directions, predecessor ordering and three source-listed taxon contexts agree. Native generalizations and citation transfer are independently bounded. |
| e-1994 | https://pmc.ncbi.nlm.nih.gov/articles/PMC197224/; PMID 8002591; DOI 10.1128/jb.176.24.7659-7666.1994; pp. 7659–7666, Table 1, Figures 1–5 and results | supports | All eight official page scans visually read. ADP1/BD413 qui deletion/complementation and route diagram support two-step shikimate catabolism and QuiA. The 809-aa sequence and membrane-family predictions do not prove topology or purified ADP1 kinetics. Heterologous QuiA assay was undetectable even with PQQ. |
| e-1995 | https://www.researchgate.net/publication/15607491_Unusual_ancestry_of_dehydratases_associated_with_quinate_catabolism_in_Acinetobacter_calcoaceticus; PMID 7592351; DOI 10.1128/jb.177.20.5971-5978.1995; methods and cloned quiC results | supports | Author-rendered methods, cloned-enzyme results, Table 1 and relevant captions inspected; original figure images unavailable. QuiC pZR564 E. coli crude extracts catalyze DHS dehydration, with a truncated negative control. Native MONOMER37 DHQ wording and suspect numeric units are not copied. Vector pBSK/pBKS disagreement remains qualified. |
| e-1988 | https://repository.tudelft.nl/file/File_568d007a-a882-4759-b342-9d21fd7d69bc?preview=1; PMID 3044290; DOI 10.1007/BF00409714; author-thesis reprint PDF 90–102, identification PDF 9 | supports | Chapter V text independently read; decisive original pages 85, 87, 89 visually checked. LMD 79.41 historical API 20NE assignment and Table 1 PQQ-mutant rescue support separate species context. QDH was not purified and periplasm location was assumed. Discussion summarizes earlier Gox observations rather than reporting new Gox tests. |
| e-2003-qdh | https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2115/_pdf; PMID 14586098; DOI 10.1271/bbb.67.2115; strain Table 1 and purification selection, substrate/product results | supports | Original-derived pages 1, 2, 4, 7, 8 text and original rendered page 4 read. SA1 and AC3 are Acinetobacter purified preparations, not Gox or ADP1. Their 74% shikimate rate, kinetic constants and electron-acceptor assays must not be attributed to Q59086. Native ENZRXN11861 citation transfer is explicitly excluded. |
| e-2003-dhs | https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2124/_pdf; PMID 14586099; DOI 10.1271/bbb.67.2124; pp. 2124–2126, 2129–2130 | supports | Relevant methods and fractionation text independently read, with original journal page 2129 image inspected. IFO 3244 DHSase is a partially purified cytoplasmic fraction separated from DQD, with qualitative protocatechuate detection. This is not a sequence-defined purified enzyme or demonstration of whole-route growth. |
| e-2004 | https://pubmed.ncbi.nlm.nih.gov/15598527/; PMID 15598527; DOI 10.1016/j.femsle.2004.10.014; abstractText in original EuropePMC payload | supports | Actual EuropePMC abstract and metadata inspected. IFO 3244 QDH is membrane-associated, PQQ-containing and possibly proteolyzed. The abstract does not directly report a shikimate assay; the corresponding catalytic edge is explicitly attributed to native ENZRXN68 commentary, not unread primary full-body evidence. |
| e-2005 | https://pmc.ncbi.nlm.nih.gov/articles/PMC546756/; PMID 15691962; DOI 10.1128/AEM.71.2.1025-1034.2005; #sec6,#sec11–17 and Tables 1–2 | supports | Original methods/results/discussion, tables and decisive Figures 6–7 independently read. ADP331 pcaU deletion reduces qui transcripts and removes inducer dependence; protocatechuate induction follows 2 mM addition to pyruvate-grown cells. QuiA probe is specific; quiC–quiX probe is shared. Constitutive quiAp persists. No direct PcaU binding to quiA/quiC promoters, direct ligand binding, complete 14.4 kb transcript detection or enzyme activation is inferred. |
| e-q59086 | https://rest.uniprot.org/uniprotkb/Q59086.json; Original JSON organism, genes, proteinDescription, comments and sequence | supports | ADP1 quiA/ACIAD1716, 809 aa, explicit PQQ cofactor and membrane ECO:0000305 inference; native cross-reference agrees. |
| e-q43922 | https://rest.uniprot.org/uniprotkb/Q43922.json; Original JSON organism, genes, proteinDescription, comments and sequence | supports | ADP1 quiC/ACIAD1714, 486 aa, explicit DHS-to-PCA catalytic annotation; original recombinant preparation remains qualified. |
| e-o83046 | https://rest.uniprot.org/uniprotkb/O83046.json; Original JSON organism, genes, proteinDescription, comments and sequence | supports | ADP1 pcaU/ACIAD1702 regulator, 278 aa, Met1/Met5 initiation uncertainty; no invented exact tested N terminus. |
| e-gene-retirement | research/pathway_additions/2026-10-14-next-256/shikimate/native/gene-retirement-assessment.json | supports | Independently inspected NCBI Gene originals 2879574/2879469, both discontinued, and native G27/G36 gene/product links. Native physical genes remain exact regulation targets; no active Entrez successor or nucleotide accession was fabricated. |
| e-correction | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/issue-542-correction-verification.json | supports | Issue 542 corrected the one unsupported historical sentence in edge 003. Re-inserting that exact removed line reconstructs the initial inspect SHA; all other record bytes are unchanged. No previous governed finding existed, so final clean review uses an applied-correction assessment rather than invented resolved-finding lineage. |
| e-imodulon | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/imodulondb-applicability.md | context_only | Actual structured runner returned 28 dataset rows; none matches ADP1, historical LMD 79.41 or Gox IFO 3244. A. baumannii is not the same organism. No downstream module/gene query applicable; no negative biological inference. |
| e-lineage | reviews/structured/ | context_only | The pre-save lineage search covered the exact target identifier and slug throughout the structured-review tree, including hidden/ignored files, and found no previous target observation at that time. A contemporaneous integration review is separate; this is not a claim about remote discussions. |
| e-gates | research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/gate-acceptance.json | supports | Final root-executed full-repository gate receipts, original logs and all tested-core hashes independently verified unchanged, including history. The first full run failed only the stale-page check after the history correction; its archived failed receipt is preserved and superseded by the full successful rerun. The separate history validation also passed. A temporary DNS failure of the vendored checker is preserved separately; its unchanged bounded retry passed. The retained helper phrase history/review validation is too broad: just validate runs repository QC and history validation, while the final structured-review archive check is a separate post-save operation. The check summaries here use that precise scope. These checks are not scientific proof. |

## Limits And Additional Notes

- PMID 15598527 remains abstract-only; Gox shikimate assay is explicitly supported by inspected native commentary. PMID 7592351 original figure images were unavailable; relevant author-rendered text and captions were read.
- The reviewer independently read all 1994 scans, the 1988 chapter and decisive 2005 methods/results/discussion; 2003 reading was bounded to the passages/images listed in independent-primary-reading.json, not a fresh complete-paper/figure claim.
- Source-listed species context does not assert every strain expresses a complete route or grows on shikimate. LMD 79.41 historical species assignment is not modern retyping. SA1/AC3, ADP1 and IFO 3244 remain distinct.
- Generic quinone classes do not establish every member as a substrate or identify a physiological acceptor. Broad membrane/cytoplasmic recovery does not establish exact topology or exclusive localization; molecular cleavage states and unnamed Gox protein sequences remain unresolved.
- The quiC–quiX shared probe limits target resolution to operon context; regulation edges do not claim direct PcaU promoter binding, metabolite binding or protein activation. Constitutive quiAp remains independent of PcaU.
- Bounded source-neighborhood coverage is complete but not exhaustive knowledge of all enzymes/organisms. Root reran the full corpus gates after refreshing the page for the history correction. Both attempts and the successful final receipts were independently verified; this reviewer did not rerun them.
- This working-tree observation attests to exact input bytes and original-source hashes; actual committed Git blob membership and external scratch longevity require separate integration/publication checks.
- Independent source reading and the provisional attribution finding preceded the first inspect invocation. The entire assembled target and final correction were subsequently audited against captured inputs. Review start records target availability; initial inspect captured 5d9924235a404618b4192d4562199635f6e4bc8cf05f80379e4a7162508ab6e8, and the exact one-sentence correction produced final ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808.
- Issue 542 was corrected before any governed finding snapshot was saved. Its disposition appears in evidence-linked assessment without fabricated previous_occurrences.
- The first full suite reported 1 failed, 4,959 passed and 3 skipped because appended history made the generated shikimate page stale. Its actual failed receipt remains visible; the root refreshed the page and completed a full successful rerun with history included in the hashed inputs.
- The vendored checker initially failed with a DNS fetch error. The preserved failed receipt is superseded by a successful identical retry with authorized network access and unchanged source, checker, pin and tested inputs.
- iModulonDB returned 28 datasets successfully; no matching organism makes further gene/module queries inapplicable. This absence is not negative biological evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T181132Z-next256-shikimate-scientific
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of shikimate degradation I
started_at: '2026-10-14T17:36:57Z'
finished_at: '2026-10-14T18:11:32Z'
reviewer:
  identity: codex:/root/next256_scientific_review
  kind: agent
  independence: independent
  independence_basis: No authorship or edits to maintained pathway, authority snapshots,
    pages, history or author dossier. Independently read original payloads and primary
    material, identified issue 542, checked the author correction, and owns only reviewer
    scratch audits and this immutable review bundle.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: Complete two-step native route supported with explicit strain, assay,
  regulatory and source-access bounds
scientific_review: true
summary: All 31 edges of the frozen shikimate degradation I record and all 17 bounded
  native biological objects plus 9 supplemental contexts independently assessed. Exact
  chemical identities and reaction class scope, four catalysts, PQQ roles, taxa, qualifiers
  and four transcription-regulation edges are supported within stated limits. Minor
  issue 542 attribution was corrected and exactly rechecked. All required gates pass
  on final bytes; no open scientific findings remain.
source:
  git_revision: b645cc4c0afd75f3eff521376b75602a3c2ad679
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
    sha256: 3ce7f3ed376451d625be862b8f56f45771f57dbaf0ffd7203ac011ebdc189e59
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: cc16a3703d5ee7d07b141d33b0f5ed9943caf885ecd791e9565800bbfad5df64
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 4a1963c5b61ea7906ce5e5ad09f8f6865fc7e18a86e9f5a5a0f2c85bde62cc45
    role: context
  - path: data/pathways/shikimate-degradation-i.yaml
    sha256: ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808
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
  - path: history/records/shikimate-degradation-i/2026-10-14T173756Z-claude-code-70bb5a.yaml
    sha256: ae468b221e70aecd4bf6bdecd8b6af1d8766cb8e70a291f9ef75219da68462b9
    role: context
  - path: history/records/shikimate-degradation-i/2026-10-14T174930Z-codex-a826f9.yaml
    sha256: 8643ff819c2c007722dbc14adc5639922610bea833c32aeb142caa5d98799b99
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/authorities/pathway-authority-profile-assessment.json
    sha256: 8fcd3d3ac7f708f3eb906c6f0ad8b45a2420334371f21fa8ac8a4c8222e24f9b
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/chemistry/assembly-ledger.json
    sha256: 0c530b6bb01e98cf743dceea9184611c0e9cd3aab7ef1208a21e836c5cfd3552
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/chemistry/chemical-identity-and-reaction-audit.json
    sha256: 05971c436d951bc9713e58d09db378204947af08024b2a3c4c118dfad7efaa99
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/all-edge-and-reference-audit.json
    sha256: ce102a9f356a36e0f2280970fda838b9e8140c17c8c9bc1b635bc3cc889546c7
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/edge_audit.py.txt
    sha256: 4a0c534188f7acc37623cb81329c12eef5b448a23eea6ca3bccb0b2835ec250a
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/gate-acceptance.json
    sha256: c3138ad80f76ad75d41ea7dccfc6dff6b9f2ced894e5f962ea6878de5821ff30
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/gate_acceptance.py.txt
    sha256: 395a6ec07c29459418a1d7a05f9f53b0cba31034bb7b0a8e53576a9c0f183f0a
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/imodulondb-applicability.md
    sha256: b8c285c94304371d844e29bbf1f787d0751554e445db63cac54223de3bf26c93
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent-primary-reading.json
    sha256: 1c2408617d188c31bd4db7b24cc2d3ab2f4b4ebdfc6eebb00555fa705a297b88
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent-source-checks.json
    sha256: 90c3deefcd54a55e106f11a6ad35dc73332d93cb9d5a6c763591a0626f97d401
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent_sources.py.txt
    sha256: d2861fa3057da136a44299c41495104b04a60e1df27887b0c230ab597878bd16
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/issue-542-correction-verification.json
    sha256: 58981d801e9888c66325461c6eb134ec664e26a94b075dfb28bb7042fb860c01
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/native-neighborhood-audit.json
    sha256: 2be2be2878c5418ec3536c05c8833b51d47118718ff89a3ac42772f8df310b30
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/native_neighborhood_audit.py.txt
    sha256: 632dc92bbae56ba0cf21bdaac6e07eb452a562593228b8615139d4666b06b4f2
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/retention.json
    sha256: 18f95cdffe0708db9260a767fb3a1d872d7455d7fc50fa541a922b0e260f0225
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/native/biological-coverage.json
    sha256: 1cf0088e4b4dc749604390eb8d5cc3f84d9be7511c356a14713eee1966b85fad
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/native/gene-retirement-assessment.json
    sha256: 1eacca4f1d488e21ef6233e71b47b3d93370ce1793a4d42cea8e81afb1e73427
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/native/supplemental-context.json
    sha256: f1893f0f94b61d52baddb6140b4c2e8f5f6e6bae738a55b11caae565b7ec071d
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/primary/claims-and-dispositions.json
    sha256: a5790801fd7f26277ee3de0c08b0ec1d2f07898cbd07caac3f74d8bf92f60a83
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/primary/constructs-ledger.json
    sha256: 2d1b19505a31768122583d5e23e3a26e787f11f00dd034ad38d1b49db5af22ac
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/primary/original-bindings.json
    sha256: 2af53a95caa1cb79fc630f371a743450ff16ea6eb976ee42c73e479b54b92b80
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/primary/reading-ledger.json
    sha256: 6b9ed4aa4021f41b577c71eb084539f35d298b7658006429b6421e6cc9de61b2
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-network-retry/just-vendored-check.log.json
    sha256: e056c499943770973096ae09315fd3ac23ec05e29bcb35a18da302d0671a4eaa
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-network-retry/receipts.json
    sha256: 50310261b8fd0fdc6396487722e9410a875500e895f1ff6795e7af6cbdf8f010
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-network-retry/relocation.json
    sha256: 7edb15a2f4d4ad095d5f168de9a387801dd4e4bf16d7f27ab0668ad7d855a153
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-network-retry/retention.json
    sha256: bfa538f3f191a1ed7ed186fc90cf81a907f9fcd65dc8338d4e3955c7512a37f9
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/archive-bindings.json
    sha256: 95825a91bbdc2e83bc67e70016a9d2710c0839c640b18799a471b8e0129cfe60
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/environment.json
    sha256: 7aae12e69dda412d74568df8ffc3c1694d5d3695d92694fc2d605e57c73a635c
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/just-render-pages.log.json
    sha256: a3c9672b83a2f6efd484190edb87ca0c0b2ef7c9e0c1ba03f4407dd9755b2bc1
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/just-test.log.json
    sha256: adf7c55c2d9a8664773eb0f51eb831f0f2c264a613b11e74f1c48e2e284827aa
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/just-validate.log.json
    sha256: a73965c2c35b4efa32db3b66ffb384162c32ce8a25b38798220fca575d79c415
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/receipts.json
    sha256: 9cb1635d038ce9c5003687f708085b3e62e33c1d51af565fdaff8703abe968c8
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/run_checks.py.txt
    sha256: fd8b9c714cbb51af19ccc0da8e3f4b912b09b3f3aeebfde26851cf84e8d062de
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/attempt-before-history-render/tested-core-input-hashes.json
    sha256: 0881b8c30326267796c4dab05a8eb09bad27928abd2fb468b3549b9956578ab6
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/history-correction-receipt.json
    sha256: e8e3f0736f0eff618f1e607df8d8934c2dd33bb9f090c4136b38165636cda19c
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/history-correction.log.json
    sha256: a4be88387ca35d01a1a4926b8697a51a1085ce29a7c59c0f463f956a19e9e3e2
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation-observations/retention.json
    sha256: 6c2364b935abf3bfc78044b55714a0f43850f3cb193e497134c31d0c3b5e2bc8
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/environment.json
    sha256: 7aae12e69dda412d74568df8ffc3c1694d5d3695d92694fc2d605e57c73a635c
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/final-input-preservation.json
    sha256: ad2f67e8d8cbb1af5bfdc4bf95a799118c8846abe36bd4d4441af5762b4c8570
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/git-diff-check.log.json
    sha256: af739331ac883bb3493c20de861f72a2cd747c187471be2949ea9b56b3d255cb
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/just-lint.log.json
    sha256: 4d6301ca2c9020de480582d2f8f67582be0ebf8eba8312ca54ab1bf91838e09c
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/just-render-pages.log.json
    sha256: 51282bed1cb626077fd06e0c161f7cdae66e34b88ee9e31768208d191f617e2d
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/just-test.log.json
    sha256: d7ece460f753303928c8164b70b1933768c9324c293875fcd20fd0a17e15738a
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/just-validate.log.json
    sha256: bd594a130b00a1d2b342075c5bd11124fa84fe29961535e7fb480bd2c5e4ad3f
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/just-vendored-check.log.json
    sha256: 4d6f5845d12ddd54fcff59187a37311e76887c455fd3ec0cfe4bb69e85e6e9b1
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/receipts.json
    sha256: c38e27df6b097fbc157c39a5ff8158487bd5ca4f477c9339d2f5ccf432992df5
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/resume_checks.py.txt
    sha256: dd4bd34c01497ff16b99818e0815e3cd23fab572b4d8acc0ed7d952c37768255
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/retention.json
    sha256: 5752b1339531b402024444a100b864d86b137cebf6a4b47255cf9f8a3dc69b51
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/run_checks.py.txt
    sha256: 56e483a6e1596cd88eaac827017ad96a37fe87bb69ecf7b2bfe15a8baa8f17e1
    role: context
  - path: research/pathway_additions/2026-10-14-next-256/shikimate/validation/tested-core-input-hashes.json
    sha256: fd85039b22cd87bf71a6174eda7b2a835ddace81e4f837fb626c4d469d9f9db2
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/cli.py
    sha256: a170e60e3c398755a21e1304e3bec9e2af743af46ca62de3bbb47ea878ca0b7e
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
scope:
  description: One maintained pathway, all 31 edges, 16 participants, two reactions,
    three taxa, 27 references and full declared native neighborhood, with independent
    primary reading bounds.
  selection: Exact MetaCyc:SHIKIMATEDEG-PWY selected for complete record and bounded
    native-neighborhood review; no edge sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  exclusions:
  - target: Other 252 maintained pathways
    reason: Not scientifically rereviewed; covered by shared corpus deterministic
      gates only.
  - target: Other pathway variants, additional organisms and unread primary full bodies
    reason: Outside exact selected scope; no literature-exhaustion or universal organism
      claim.
targets:
- target_id: MetaCyc:SHIKIMATEDEG-PWY
  path: data/pathways/shikimate-degradation-i.yaml
  label: shikimate degradation I
  kind: maintained
  record_class: PathwayRecord
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-i.yaml
    role: maintained_record
checks:
- check_id: inspect
  name: Final frozen input inspection
  status: passed
  required: true
  summary: Formal initial target inspection binds draft hash; final complete target
    and corrected sentence rechecked before final input inspection.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: python -B scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-256-science-review/targets.yaml
    --input <declared context inputs>
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-record
- check_id: edge-audit
  name: All 31 edges and original-reference audit
  status: passed
  required: true
  summary: 31 unique triples, 26 reference hashes and 9 literal quote occurrences
    checked; all per-source quote totals within 25 words.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: python -B /private/tmp/pathwaymech-next-256-science-review/edge_audit.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-edge
- check_id: source-audit
  name: Independent chemical/native/Rhea audit
  status: passed
  required: true
  summary: Five concrete InChI/key mappings and 25 original RDF nodes agree; source-class
    scope retained.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: python3 /private/tmp/pathwaymech-next-256-science-review/independent_sources.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-chemistry
- check_id: neighborhood
  name: Complete bounded native neighborhood
  status: passed
  required: true
  summary: 17 independently derived biological objects and 9 supplemental contexts
    assessed.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: python3 /private/tmp/pathwaymech-next-256-science-review/native_neighborhood_audit.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-neighborhood
- check_id: imodulon
  name: Structured iModulonDB applicability
  status: passed
  required: false
  summary: Catalog returned successfully; no matching target dataset, downstream queries
    inapplicable.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: uv run --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw
    kg-microbe-sources imodulondb datasets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-imodulon
- check_id: superseded-gate-1
  name: 'Superseded attempt: just render-pages'
  status: passed
  required: false
  summary: Actual archived result retained. The first full suite reported 1 failed,
    4,959 passed and 3 skipped; only the page reflecting the appended history correction
    was stale. The complete final rerun supersedes this attempt.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just render-pages
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
  scope_note: Historical attempt on superseded rendered bytes; the separate final
    gate entries are the required acceptance checks.
- check_id: superseded-gate-2
  name: 'Superseded attempt: just validate'
  status: passed
  required: false
  summary: Actual archived result retained. The first full suite reported 1 failed,
    4,959 passed and 3 skipped; only the page reflecting the appended history correction
    was stale. The complete final rerun supersedes this attempt.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
  scope_note: Historical attempt on superseded rendered bytes; the separate final
    gate entries are the required acceptance checks.
- check_id: superseded-gate-3
  name: 'Superseded attempt: just test'
  status: failed
  required: false
  summary: Actual archived result retained. The first full suite reported 1 failed,
    4,959 passed and 3 skipped; only the page reflecting the appended history correction
    was stale. The complete final rerun supersedes this attempt.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just test
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - e-gates
  scope_note: Historical attempt on superseded rendered bytes; the separate final
    gate entries are the required acceptance checks.
- check_id: superseded-network
  name: Superseded vendored-check DNS failure
  status: failed
  required: false
  summary: The actual failed invocation could not fetch the pinned canonical GitHub
    artifact (DNS Errno 8). An identical bounded retry passed on unchanged inputs.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just vendored-check
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - e-gates
  scope_note: Historical network-unavailable attempt; final gate-5 is the required
    successful vendored check.
- check_id: history-correction
  name: History actor correction validation
  status: passed
  required: true
  summary: 'Actual root validate-history receipt and log verified: 443 valid history
    records. Final full-run inputs also include history.'
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-1
  name: just render-pages
  status: passed
  required: true
  summary: Root executed the final run; reviewer checked actual log hash, successful
    exit and all unchanged tested inputs. Generated all maintained pages/graph data
    successfully.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just render-pages
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-2
  name: just validate
  status: passed
  required: true
  summary: Root executed the final run; reviewer checked actual log hash, successful
    exit and all unchanged tested inputs. Full closed-schema, identifier/label, evidence
    and history validation passed.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-3
  name: just test
  status: passed
  required: true
  summary: 'Root executed the final run; reviewer checked actual log hash, successful
    exit and all unchanged tested inputs. Final full pytest suite: 4960 passed, 3
    skipped. Complete terminal summary retained in original log.'
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just test
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-4
  name: just lint
  status: passed
  required: true
  summary: Root executed the final run; reviewer checked actual log hash, successful
    exit and all unchanged tested inputs. Full Ruff lint passed.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just lint
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-5
  name: just vendored-check
  status: passed
  required: true
  summary: Root executed the final run; reviewer checked actual log hash, successful
    exit and all unchanged tested inputs. Canonical vendored helper check passed.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: just vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
- check_id: gate-6
  name: git diff --check
  status: passed
  required: true
  summary: Root executed the final run; reviewer checked actual log hash, successful
    exit and all unchanged tested inputs. Whitespace check passed.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - e-gates
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/shikimate-degradation-i.yaml
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: 'Entire final record inspected: 31 edges, 16 participants, two reactions,
    three taxa and 27 references. Final SHA ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808.
    Initial inspected record differed by one removed unsupported historical-attribution
    sentence; correction reconstructed and verified exactly.'
  snapshot_sha256: ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808
- evidence_id: e-edge
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/all-edge-and-reference-audit.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: All 31 exact triples reproduce from native slots and independently adjudicated
    primary support. All 26 hash-bearing references match actual originals; nine quote
    occurrences literally match inspected text with whitespace normalization. Per-source
    verbatim totals remain 6, 12, 17 and 20 words. This replay complements scientific
    reading.
  snapshot_sha256: ce102a9f356a36e0f2280970fda838b9e8140c17c8c9bc1b635bc3cc889546c7
- evidence_id: e-neighborhood
  kind: database
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/native-neighborhood-audit.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: 'Independent native traversal finds seven direct activities, seven proteins,
    one recursive subunit, one auxiliary activity and one regulation: 17 objects,
    six retained with scope and 11 excluded. Nine supplemental native objects are
    separately assessed. No source-neighborhood sampling.'
  snapshot_sha256: 2be2be2878c5418ec3536c05c8833b51d47118718ff89a3ac42772f8df310b30
- evidence_id: e-chemistry
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent-source-checks.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Five concrete native/ChEBI full InChI and InChIKey mappings match independently
    read pinned ChEBI 255 SQL. All 25 projected Rhea nodes match original Rhea 142
    RDF. Native broad quinones/quinols are not exactly equated to Rhea 47049 narrower
    1,4-benzoquinone/hydroquinone participants; RHEA 24849 exact sides match.
  snapshot_sha256: 90c3deefcd54a55e106f11a6ad35dc73332d93cb9d5a6c763591a0626f97d401
- evidence_id: e-primary
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/independent-primary-reading.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: 'Independent reading bounds and original hashes for seven primary sources:
    all 1994 scans; relevant 1995 author text/captions; 1988 author-reprint chapter;
    decisive 2003 strain/fractionation passages and images; 2004 abstract; 2005 original
    transcription methods/results/discussion and Figures 6–7. Broader author reading
    is not adopted as independent coverage.'
  snapshot_sha256: 1c2408617d188c31bd4db7b24cc2d3ab2f4b4ebdfc6eebb00555fa705a297b88
- evidence_id: e-pathway
  kind: database
  reference: https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:SHIKIMATEDEG-PWY
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Full MetaCyc 27.0 object establishes exactly SHIKIMATE-PQQ-RXN then DHSHIKIMATE-DEHYDRO-RXN,
    shikimate through DHS to PCA. Pathway membership, selected directions, predecessor
    ordering and three source-listed taxon contexts agree. Native generalizations
    and citation transfer are independently bounded.
  locator: /ptools-xml/Pathway[@frameid="SHIKIMATEDEG-PWY"]
  snapshot_sha256: 9153c7962f156d28786f875f73aee72b4ad67cd07d3e03e6adb5254b3d0d66a3
- evidence_id: e-1994
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC197224/
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: All eight official page scans visually read. ADP1/BD413 qui deletion/complementation
    and route diagram support two-step shikimate catabolism and QuiA. The 809-aa sequence
    and membrane-family predictions do not prove topology or purified ADP1 kinetics.
    Heterologous QuiA assay was undetectable even with PQQ.
  locator: PMID 8002591; DOI 10.1128/jb.176.24.7659-7666.1994; pp. 7659–7666, Table
    1, Figures 1–5 and results
- evidence_id: e-1995
  kind: primary_source
  reference: https://www.researchgate.net/publication/15607491_Unusual_ancestry_of_dehydratases_associated_with_quinate_catabolism_in_Acinetobacter_calcoaceticus
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Author-rendered methods, cloned-enzyme results, Table 1 and relevant captions
    inspected; original figure images unavailable. QuiC pZR564 E. coli crude extracts
    catalyze DHS dehydration, with a truncated negative control. Native MONOMER37
    DHQ wording and suspect numeric units are not copied. Vector pBSK/pBKS disagreement
    remains qualified.
  locator: PMID 7592351; DOI 10.1128/jb.177.20.5971-5978.1995; methods and cloned
    quiC results
- evidence_id: e-1988
  kind: primary_source
  reference: https://repository.tudelft.nl/file/File_568d007a-a882-4759-b342-9d21fd7d69bc?preview=1
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Chapter V text independently read; decisive original pages 85, 87, 89 visually
    checked. LMD 79.41 historical API 20NE assignment and Table 1 PQQ-mutant rescue
    support separate species context. QDH was not purified and periplasm location
    was assumed. Discussion summarizes earlier Gox observations rather than reporting
    new Gox tests.
  locator: PMID 3044290; DOI 10.1007/BF00409714; author-thesis reprint PDF 90–102,
    identification PDF 9
  snapshot_sha256: 9059bfeef93bb35ecadf868c689cc1ed208cd7bac677c3849bdd63852b1b8c97
- evidence_id: e-2003-qdh
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2115/_pdf
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Original-derived pages 1, 2, 4, 7, 8 text and original rendered page 4
    read. SA1 and AC3 are Acinetobacter purified preparations, not Gox or ADP1. Their
    74% shikimate rate, kinetic constants and electron-acceptor assays must not be
    attributed to Q59086. Native ENZRXN11861 citation transfer is explicitly excluded.
  locator: PMID 14586098; DOI 10.1271/bbb.67.2115; strain Table 1 and purification
    selection, substrate/product results
  snapshot_sha256: 618dd246b5755894346615c09f71bdfb5165115469f4014895cb9f10647e1937
- evidence_id: e-2003-dhs
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/bbb/67/10/67_10_2124/_pdf
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Relevant methods and fractionation text independently read, with original
    journal page 2129 image inspected. IFO 3244 DHSase is a partially purified cytoplasmic
    fraction separated from DQD, with qualitative protocatechuate detection. This
    is not a sequence-defined purified enzyme or demonstration of whole-route growth.
  locator: PMID 14586099; DOI 10.1271/bbb.67.2124; pp. 2124–2126, 2129–2130
  snapshot_sha256: fe0a94a47666acfe3a85aed78521589dd0e251b352f3dbfb8bba93df76351f6c
- evidence_id: e-2004
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/15598527/
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Actual EuropePMC abstract and metadata inspected. IFO 3244 QDH is membrane-associated,
    PQQ-containing and possibly proteolyzed. The abstract does not directly report
    a shikimate assay; the corresponding catalytic edge is explicitly attributed to
    native ENZRXN68 commentary, not unread primary full-body evidence.
  locator: PMID 15598527; DOI 10.1016/j.femsle.2004.10.014; abstractText in original
    EuropePMC payload
  snapshot_sha256: 787511b9e5396984ebb44ee38cbb4584352ab5959511bf8639c25d3f8ddaa5c0
- evidence_id: e-2005
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC546756/
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Original methods/results/discussion, tables and decisive Figures 6–7 independently
    read. ADP331 pcaU deletion reduces qui transcripts and removes inducer dependence;
    protocatechuate induction follows 2 mM addition to pyruvate-grown cells. QuiA
    probe is specific; quiC–quiX probe is shared. Constitutive quiAp persists. No
    direct PcaU binding to quiA/quiC promoters, direct ligand binding, complete 14.4
    kb transcript detection or enzyme activation is inferred.
  locator: 'PMID 15691962; DOI 10.1128/AEM.71.2.1025-1034.2005; #sec6,#sec11–17 and
    Tables 1–2'
  snapshot_sha256: a6ce5986eb9687d2acca79fbccdb1882ed2e715bbd9c1f746a32bd7fc3d71a23
- evidence_id: e-q59086
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q59086.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: ADP1 quiA/ACIAD1716, 809 aa, explicit PQQ cofactor and membrane ECO:0000305
    inference; native cross-reference agrees.
  locator: Original JSON organism, genes, proteinDescription, comments and sequence
  snapshot_sha256: 25d86e8505af8ac4923f508fa03b7fd2aadfeaf1dd1dea924faeec64c532eafe
- evidence_id: e-q43922
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q43922.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: ADP1 quiC/ACIAD1714, 486 aa, explicit DHS-to-PCA catalytic annotation;
    original recombinant preparation remains qualified.
  locator: Original JSON organism, genes, proteinDescription, comments and sequence
  snapshot_sha256: 7b18529d44b49af1f01be42a2734ef35a8e4f4f814328a166f29273ac8e261c1
- evidence_id: e-o83046
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O83046.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: ADP1 pcaU/ACIAD1702 regulator, 278 aa, Met1/Met5 initiation uncertainty;
    no invented exact tested N terminus.
  locator: Original JSON organism, genes, proteinDescription, comments and sequence
  snapshot_sha256: 4fc6acac931fcb47fcecd0508b54c36c3a7c932c13420580ba8ed61c36aba81c
- evidence_id: e-gene-retirement
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/native/gene-retirement-assessment.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Independently inspected NCBI Gene originals 2879574/2879469, both discontinued,
    and native G27/G36 gene/product links. Native physical genes remain exact regulation
    targets; no active Entrez successor or nucleotide accession was fabricated.
  snapshot_sha256: 1eacca4f1d488e21ef6233e71b47b3d93370ce1793a4d42cea8e81afb1e73427
- evidence_id: e-correction
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/issue-542-correction-verification.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: Issue 542 corrected the one unsupported historical sentence in edge 003.
    Re-inserting that exact removed line reconstructs the initial inspect SHA; all
    other record bytes are unchanged. No previous governed finding existed, so final
    clean review uses an applied-correction assessment rather than invented resolved-finding
    lineage.
  snapshot_sha256: 58981d801e9888c66325461c6eb134ec664e26a94b075dfb28bb7042fb860c01
- evidence_id: e-imodulon
  kind: search
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/imodulondb-applicability.md
  accessed_at: '2026-10-14T18:11:32Z'
  support: context_only
  summary: Actual structured runner returned 28 dataset rows; none matches ADP1, historical
    LMD 79.41 or Gox IFO 3244. A. baumannii is not the same organism. No downstream
    module/gene query applicable; no negative biological inference.
  snapshot_sha256: b8c285c94304371d844e29bbf1f787d0751554e445db63cac54223de3bf26c93
  search_scope: Complete returned public dataset catalog from kg-microbe-sources imodulondb
    datasets, process 41412 exit 0; not an exhaustive transcriptomic-resource search.
- evidence_id: e-lineage
  kind: search
  reference: reviews/structured/
  accessed_at: '2026-10-14T18:11:32Z'
  support: context_only
  summary: The pre-save lineage search covered the exact target identifier and slug
    throughout the structured-review tree, including hidden/ignored files, and found
    no previous target observation at that time. A contemporaneous integration review
    is separate; this is not a claim about remote discussions.
  search_scope: rg --no-ignore --hidden -n SHIKIMATEDEG-PWY|shikimate-degradation-i
    reviews/structured, pattern passed as one quoted argument, completed with no matches.
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-256/shikimate/independent-scientific/gate-acceptance.json
  accessed_at: '2026-10-14T18:11:32Z'
  support: supports
  summary: 'Final root-executed full-repository gate receipts, original logs and all
    tested-core hashes independently verified unchanged, including history. The first
    full run failed only the stale-page check after the history correction; its archived
    failed receipt is preserved and superseded by the full successful rerun. The separate
    history validation also passed. A temporary DNS failure of the vendored checker
    is preserved separately; its unchanged bounded retry passed. The retained helper
    phrase history/review validation is too broad: just validate runs repository QC
    and history validation, while the final structured-review archive check is a separate
    post-save operation. The check summaries here use that precise scope. These checks
    are not scientific proof.'
  snapshot_sha256: c3138ad80f76ad75d41ea7dccfc6dff6b9f2ced894e5f962ea6878de5821ff30
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact complete two-step shikimate I route
  outcome: supported
  summary: The target preserves both native reactions in selected forward order and
    ends at protocatechuate. Quinate-specific QuiB, NAD-dependent sibling variants,
    petrobactin AsbF and downstream mineralization remain distinct. Similar names
    or shared DHS chemistry do not establish pathway equivalence.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-record
  - e-pathway
  - e-1994
  - e-neighborhood
- assessment_id: a-chemistry
  area: grounding
  topic: Exact molecule and reaction scope
  outcome: supported
  summary: Shikimate, DHS, PCA, water and PQQ identities match complete native/pinned
    ChEBI InChI and stereochemistry/protonation. First reaction and quinone/quinol
    classes remain native; narrower Rhea 47049 is not used as an exact replacement.
    RHEA 24849 sides and contains1 locators agree. PQQ cofactor is distinct from the
    consumed acceptor.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-chemistry
  - e-edge
  - e-pathway
- assessment_id: a-catalysis
  area: evidence
  topic: All four catalyst identities and preparations
  outcome: supported
  summary: ADP1 QuiA has native/genetic support and current protein identity; SA1/AC3
    purified kinetics are excluded. ADP1 QuiC carries its heterologous crude-extract
    qualification. Gox DHSase retains partial cytoplasmic preparation and Gox QDH
    possible proteolysis. Shikimate activity of the latter is attributed to inspected
    native comment, not unread 2004 body.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-1994
  - e-1995
  - e-2003-qdh
  - e-2003-dhs
  - e-2004
  - e-q59086
  - e-q43922
  - e-edge
- assessment_id: a-regulation
  area: graph
  topic: Gene expression regulation and physical component roles
  outcome: supported
  summary: PcaU and PCA regulation targets are exact native quiA/quiC genes. The original
    2005 Northern experiments support transcript-level influence; the shared quiC–quiX
    probe and constitutive quiAp limits are explicit. No direct binding/promoter sequence/enzymatic
    activation is invented. Gene targets are physical entities and cytoplasm/membrane
    remain cellular components.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-2005
  - e-o83046
  - e-gene-retirement
  - e-record
  dimensions:
  - name: evidence_tier
    value: Genetic perturbation and transcript induction, with shared probe limits
    definition: Regulation concerns expression; it does not assert direct regulator-target
      binding.
    evidence_ids:
    - e-2005
  - name: taxon_scope
    value: Acinetobacter baylyi ADP1
    definition: Transcription experiments do not generalize to LMD 79.41 or Gox IFO
      3244.
    evidence_ids:
    - e-2005
    - e-o83046
- assessment_id: a-context
  area: scope
  topic: Historical taxa and location limits
  outcome: supported
  summary: ADP1, historical LMD 79.41 and Gox enzyme preparations remain separate.
    LMD 79.41 Table 1 growth/PQQ rescue is valid context without modern retyping.
    Gox edges assert oxidative enzyme evidence rather than growth/mineralization.
    Broad membrane evidence does not prove precise topology; DHSase cytoplasmic recovery
    is preparation context.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-1988
  - e-2003-dhs
  - e-2004
  - e-q59086
  - e-record
- assessment_id: a-coverage
  area: completeness
  topic: Full local graph and declared source-neighborhood coverage
  outcome: supported
  summary: All 31 edges and 17 bounded native biological objects have evidence-backed
    dispositions; nine supplemental native contexts are assessed. No duplicate genus-level
    MONOMER1521 catalyst is invented. Outside-variant proteins/regulation and adjacent
    QuiA quinate activity are explicitly excluded. This is not a claim that literature
    or pathways are exhausted.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-neighborhood
  - e-edge
  - e-imodulon
- assessment_id: a-correction
  area: provenance
  topic: Applied issue 542 correction and source traceability
  outcome: supported
  summary: The unsupported attribution of previous Gox observations to 1988 experiments
    was removed. Exact byte reconstruction confirms the only record change. Original
    references, literal quotes and scientific scoping pass. No unresolved defect remains,
    and no structured predecessor finding is fabricated.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-correction
  - e-1988
  - e-edge
  - e-lineage
- assessment_id: a-gates
  area: schema
  topic: Full corpus checks on final bytes
  outcome: supported
  summary: Required validate, test, lint, whitespace and supporting rendering/vendored
    checks succeeded on unchanged final core inputs. Original receipts independently
    verified; deterministic checks supplement primary scientific review.
  target_ids:
  - MetaCyc:SHIKIMATEDEG-PWY
  evidence_ids:
  - e-gates
  - e-record
findings: []
actions: []
limitations:
- PMID 15598527 remains abstract-only; Gox shikimate assay is explicitly supported
  by inspected native commentary. PMID 7592351 original figure images were unavailable;
  relevant author-rendered text and captions were read.
- The reviewer independently read all 1994 scans, the 1988 chapter and decisive 2005
  methods/results/discussion; 2003 reading was bounded to the passages/images listed
  in independent-primary-reading.json, not a fresh complete-paper/figure claim.
- Source-listed species context does not assert every strain expresses a complete
  route or grows on shikimate. LMD 79.41 historical species assignment is not modern
  retyping. SA1/AC3, ADP1 and IFO 3244 remain distinct.
- Generic quinone classes do not establish every member as a substrate or identify
  a physiological acceptor. Broad membrane/cytoplasmic recovery does not establish
  exact topology or exclusive localization; molecular cleavage states and unnamed
  Gox protein sequences remain unresolved.
- The quiC–quiX shared probe limits target resolution to operon context; regulation
  edges do not claim direct PcaU promoter binding, metabolite binding or protein activation.
  Constitutive quiAp remains independent of PcaU.
- Bounded source-neighborhood coverage is complete but not exhaustive knowledge of
  all enzymes/organisms. Root reran the full corpus gates after refreshing the page
  for the history correction. Both attempts and the successful final receipts were
  independently verified; this reviewer did not rerun them.
- This working-tree observation attests to exact input bytes and original-source hashes;
  actual committed Git blob membership and external scratch longevity require separate
  integration/publication checks.
notes:
- Independent source reading and the provisional attribution finding preceded the
  first inspect invocation. The entire assembled target and final correction were
  subsequently audited against captured inputs. Review start records target availability;
  initial inspect captured 5d9924235a404618b4192d4562199635f6e4bc8cf05f80379e4a7162508ab6e8,
  and the exact one-sentence correction produced final ae4b0f56055956fcfe86d0d887fa4d1654efaad87a77d46bb2922335e66e4808.
- Issue 542 was corrected before any governed finding snapshot was saved. Its disposition
  appears in evidence-linked assessment without fabricated previous_occurrences.
- The first full suite reported 1 failed, 4,959 passed and 3 skipped because appended
  history made the generated shikimate page stale. Its actual failed receipt remains
  visible; the root refreshed the page and completed a full successful rerun with
  history included in the hashed inputs.
- The vendored checker initially failed with a DNS fetch error. The preserved failed
  receipt is superseded by a successful identical retry with authorized network access
  and unchanged source, checker, pin and tested inputs.
- iModulonDB returned 28 datasets successfully; no matching organism makes further
  gene/module queries inapplicable. This absence is not negative biological evidence.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/542
- https://github.com/CultureBotAI/PathwayMech/issues/543
tags:
- next256
- shikimate
- scientific
- independent
- metacyc
- full-edge-review
```
