# Final independent DHB scientific review and issue359 disposition

- Review: 20261011T063128Z-dhb-final-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T06:14:11Z
- Finished UTC: 2026-10-11T06:31:28Z
- Reviewer: Codex independent reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact full three-reaction PWY-5901 is supported for the qualified K-12 implementation. Independently checked primary/native/UniProt sources and original Rhea sides support all 23 edges/55 evidence. Issue359 is resolved by the sole supplementary page locator change from797 to796. Holo-EntB state, EntA assembly conflict, abstract-only sources and annotation-level magnesium limits are explicit; final coordinated gates passed.

## Scope And Provenance

One complete frozen DHB record: full native boundary, every local node/edge/reference, primary scope, native assembly state, chemistry and final deterministic gates.

Selection: Exact MetaCyc:PWY-5901 at final bdb60326e2ffa5db8e15939ce29bf57a12b992c1f2e56899c1cec3ecf01e2859
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d776b82c9c598bb79885ad01514b07900a678de0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5901 | data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml | maintained | 2,3-dihydroxybenzoate biosynthesis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| inspect | passed | True | MetaCyc:PWY-5901 | Canonical inspect ran before assessment and captured exact target/source inputs. |
| Final coordinated render | passed | False | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-render.log SHA256 ef7dbcc0be2b3270944edd90e5951c29b83bc76658603f0119132d50cb820956 |
| Final coordinated validate | passed | True | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-validate.log SHA256 7957d06519835efb547f4defb83a3043f6ed2107f9337b01a12cec71473fa6f1 |
| Final coordinated test | passed | True | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-test.log SHA256 839e1447ccca9bf8f461d2ff81b9d4a576e600d3a91055a99698cce5550cf3e9 |
| Final coordinated lint | passed | True | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-lint.log SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41 |
| Final coordinated identifiers | passed | False | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-identifiers.log SHA256 6410b6b35834a1c72c636fb95510a85d0b50254252e552b3e606465cdc0f9d5e |
| Final coordinated kgx | passed | False | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-kgx.log SHA256 f5d2ef75b25ad170ae60547de4a3dc42302ca2c6b5b81970d7efe2d1b2191902 |
| Final coordinated diff | passed | True | MetaCyc:PWY-5901 | Delegated root execution; reviewer inspected actual terminal receipt and log content/hash. /private/tmp/pathwaymech-next-195-verification-diff.log SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| Independent original-source and graph replay | passed | False | MetaCyc:PWY-5901 | Actual terminal95491 exit0 on initial target:51 original body digests,23 reference bodies,11 Rhea sides,3 balances, exact native three-step membership/modified assembly/protein bridges, and actual 23-edge/55-evidence KGX. Exact final parsed-object comparison proves only the p797→796 locator changed. |
| Independent exact final source delta | passed | False | MetaCyc:PWY-5901 | Actual terminal0: sole changed parsed field is supplementary Discussion page. Reassessed the corrected locator against independently rendered original p796. Structured context all 37 body hashes independently rechecked. |
| Initial full-suite observation | failed | False | MetaCyc:PWY-5901 | Initial pre-fix suite was deliberately interrupted by root after 1022 passed/3 skipped to apply confirmed review corrections. Driver130 and KeyboardInterrupt2 retained in initial receipt; no complete initial pass claimed. The final post-fix full run is recorded separately above. |

## Scientific And Domain Assessments

### Exact complete native pathway

identity: supported. Targets: MetaCyc:PWY-5901.

PWY5901 denotes all three chorismate→DHB transformations, independent from mixed PathBank map. Upstream chorismate, downstream siderophore maturation and CueO overlay have explicit exclusions.

### Exact chemistry, direction and continuity

graph: supported. Targets: MetaCyc:PWY-5901.

Independently parsed originalRhea142:11 side occurrences and all 3 atom/charge balances. Exact2S,3S intermediate retained, complete NAD/NADH/hydron chemistry. Master/directed/bidirectional bridges grounded separately; reversible EntC given native pathway direction. No separate aromatization doublecount.

### Protein role, modified state and assembly

grounding: supported. Targets: MetaCyc:PWY-5901.

Active monomer EntC supported. Exact native holo-EntB dimer retains two modified HOLO-ENTB components, without claiming carrier modification required for N-terminal lyase. EntA tetramer selected with historical octamer and concentration-dependent dimer/tetramer disagreement explicit; no obligatory channeling or fixed multienzyme complex.

### Taxon, cofactor and evidence tiers

scope: supported. Targets: MetaCyc:PWY-5901.

K12-derived primary experiments are distinguished from native MG1655 annotation; taxon83333 verified directly. EntC Mg two-ion annotation and EntB Mg without occupancy are explicit reviewed statements, not inflated abstract conclusions. NAD is reaction cosubstrate.

### Issue359 exact source location

provenance: supported. Targets: MetaCyc:PWY-5901.

Final p796 Discussion is the original octamer paragraph, visually verified alongside correct Results p795. Exact one-field delta resolves initial finding while preserving all prior bytes and lineage.

### Deterministic and generated integrity

schema: supported. Targets: MetaCyc:PWY-5901.

Final coordinated native/closed schema, identifiers, tests, lint, export and whitespace checks passed, with actual logs independently inspected and hashed. Source replay and source science assessed separately.

## Findings

### f-enta-discussion-page: Historical EntA octamer Discussion page is 796, not 797

minor / resolved / confirmed; issue key: dhb-enta-octamer-discussion-page.

dhb-edge-015 PMID:2521622 evidence locates Discussion on printed p797. Original PDF places that octamer discussion at printed p796. Correctly cited Results p795 already supports the assertion; no chemistry or assembly change requested. Matching projected evidence in dhb-source-projection.json should follow the correction.

Disposition: Exact supplementary locator changed to printed p796; independently rendered original p796 confirms the octamer discussion, and the semantic diff contains no other record changes.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-ref-0 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/18986 rh:substrates; http://rdf.rhea-db.org/18985_L rh:contains1 http://rdf.rhea-db.org/Participant_18985_compound_3304; http://rdf.rhea-db.org/Participant_18985_compound_3304 rh:compound http://rdf.rhea-db.org/Compound_3304; rh:chebi; http://rdf.rhea-db.org/18986 rh:products; http://rdf.rhea-db.org/18985_R rh:contains1 http://rdf.rhea-db.org/Participant_18985_compound_3577; http://rdf.rhea-db.org/Participant_18985_compound_3577 rh:compound http://rdf.rhea-db.org/Compound_3577; rh:chebi; http://rdf.rhea-db.org/18985 rh:directionalReaction http://rdf.rhea-db.org/18986; http://rdf.rhea-db.org/18985 rh:directionalReaction http://rdf.rhea-db.org/18986; rh:bidirectionalReaction http://rdf.rhea-db.org/18988; http://rdf.rhea-db.org/18986 rh:products http://rdf.rhea-db.org/18985_R; http://rdf.rhea-db.org/18985_R rh:contains1 http://rdf.rhea-db.org/Participant_18985_compound_3577; rh:compound http://rdf.rhea-db.org/Compound_3577; rh:chebi | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-1 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/11113 rh:substrates; http://rdf.rhea-db.org/11112_L rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_3577; http://rdf.rhea-db.org/Participant_11112_compound_3577 rh:compound http://rdf.rhea-db.org/Compound_3577; rh:chebi; http://rdf.rhea-db.org/11113 rh:substrates; http://rdf.rhea-db.org/11112_L rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_1283; http://rdf.rhea-db.org/Participant_11112_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283; rh:chebi; http://rdf.rhea-db.org/11113 rh:products; http://rdf.rhea-db.org/11112_R rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_5459; http://rdf.rhea-db.org/Participant_11112_compound_5459 rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi; http://rdf.rhea-db.org/11113 rh:products; http://rdf.rhea-db.org/11112_R rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_3719; http://rdf.rhea-db.org/Participant_11112_compound_3719 rh:compound http://rdf.rhea-db.org/Compound_3719; rh:chebi; http://rdf.rhea-db.org/11112 rh:directionalReaction http://rdf.rhea-db.org/11113; http://rdf.rhea-db.org/11113 rh:substrates http://rdf.rhea-db.org/11112_L; http://rdf.rhea-db.org/11112_L rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_3577; rh:compound http://rdf.rhea-db.org/Compound_3577; rh:chebi; http://rdf.rhea-db.org/11113 rh:products http://rdf.rhea-db.org/11112_R; http://rdf.rhea-db.org/11112_R rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_5459; rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-2 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; http://rdf.rhea-db.org/23825 rh:substrates; http://rdf.rhea-db.org/23824_L rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_5459; http://rdf.rhea-db.org/Participant_23824_compound_5459 rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi; http://rdf.rhea-db.org/23825 rh:substrates; http://rdf.rhea-db.org/23824_L rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_3484; http://rdf.rhea-db.org/Participant_23824_compound_3484 rh:compound http://rdf.rhea-db.org/Compound_3484; rh:chebi; http://rdf.rhea-db.org/23825 rh:products; http://rdf.rhea-db.org/23824_R rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_3751; http://rdf.rhea-db.org/Participant_23824_compound_3751 rh:compound http://rdf.rhea-db.org/Compound_3751; rh:chebi; http://rdf.rhea-db.org/23825 rh:products; http://rdf.rhea-db.org/23824_R rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_1650; http://rdf.rhea-db.org/Participant_23824_compound_1650 rh:compound http://rdf.rhea-db.org/Compound_1650; rh:chebi; http://rdf.rhea-db.org/23825 rh:products; http://rdf.rhea-db.org/23824_R rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_3249; http://rdf.rhea-db.org/Participant_23824_compound_3249 rh:compound http://rdf.rhea-db.org/Compound_3249; rh:chebi; http://rdf.rhea-db.org/23824 rh:directionalReaction http://rdf.rhea-db.org/23825; http://rdf.rhea-db.org/23825 rh:substrates http://rdf.rhea-db.org/23824_L; http://rdf.rhea-db.org/23824_L rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_5459; rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-3 | https://rest.uniprot.org/uniprotkb/P0AEJ2.json; /organism/taxonId; /comments/1/reaction; /comments/5; /comments/2/cofactors; /comments/2/note | supports | Exact reviewed K12 EntC native JSON: reversible isochorismate reaction, monomer and experimental Mg annotation. |
| e-ref-4 | https://pathway.yeastgenome.org/getxml?META:ENTC-MONOMER; Protein[@frameid="ENTC-MONOMER"]/catalyzes/Enzymatic-Reaction[@frameid="ENTC-ENZRXN"]/reaction; dblink[dblink-db="UNIPROT"] | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-5 | https://pubmed.ncbi.nlm.nih.gov/2139795/; /resultList/result[id="2139795"]/abstractText | supports | Inspected retained indexed primary abstract only; claim kept within its stated experimental and evidence scope. |
| e-ref-6 | https://pathway.yeastgenome.org/getxml?META:ENTB-CPLX; Protein[@frameid="ENTB-CPLX"]/catalyzes/Enzymatic-Reaction[@frameid="ISOCHORMAT-ENZRXN"]/reaction; comment; Protein[@frameid="ENTB-CPLX"]/component/Protein[@frameid="HOLO-ENTB"]; component/coefficient; comment; Protein[@frameid="ENTB-CPLX"]/catalyzes/Enzymatic-Reaction[@frameid="ISOCHORMAT-ENZRXN"]; component | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-7 | https://rest.uniprot.org/uniprotkb/P0ADI4.json; /organism/taxonId; /comments/2/reaction; /comments/7; /comments/3/cofactors | supports | Exact reviewed K12 native JSON: N-terminal isochorismatase, homodimer and magnesium annotation; C-terminal carrier modification/loading distinguished. |
| e-ref-8 | https://pubmed.ncbi.nlm.nih.gov/2139796/; /resultList/result[id="2139796"]/abstractText | supports | Inspected retained indexed primary abstract only; claim kept within its stated experimental and evidence scope. |
| e-ref-9 | https://pathway.yeastgenome.org/getxml?META:ENTA-CPLX; Protein[@frameid="ENTA-CPLX"]/catalyzes/Enzymatic-Reaction[@frameid="DHBDEHYD-ENZRXN"]/reaction; comment; Protein[@frameid="ENTA-CPLX"]/component/Protein; component/coefficient; comment | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-10 | https://rest.uniprot.org/uniprotkb/P15047.json; /organism/taxonId; /comments/1/reaction; /comments/5 | supports | Exact reviewed K12 EntA native JSON: net NAD reaction and homotetramer annotation; conflicts retained. |
| e-ref-11 | https://pubmed.ncbi.nlm.nih.gov/2144454/; /resultList/result[id="2144454"]/abstractText | supports | Inspected retained indexed primary abstract only; claim kept within its stated experimental and evidence scope. |
| e-ref-12 | https://pathway.yeastgenome.org/getxml?META:ENTA-MONOMER; Protein[@frameid="ENTA-MONOMER"]/dblink[dblink-db="UNIPROT"]; species/Organism | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-13 | https://pubmed.ncbi.nlm.nih.gov/21166461/; /resultList/result[id="21166461"]/abstractText | supports | Inspected retained indexed primary abstract only; claim kept within its stated experimental and evidence scope. |
| e-ref-14 | https://europepmc.org/articles/PMC209666?pdf=render; PMC209666 full PDF p.795, Results/Purification of diDHB-DH; p.796 Discussion | supports | Full original scanned PDF independently extracted/rendered; purified EntA Results p795 and octamer Discussion p796 support historical conflict. p797 inspected and corrected as locator. |
| e-ref-15 | https://pathway.yeastgenome.org/getxml?META:HOLO-ENTB; Protein[@frameid="HOLO-ENTB"]/unmodified-form; component-of; Protein[@frameid="HOLO-ENTB"]/unmodified-form | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-16 | https://pathway.yeastgenome.org/getxml?META:ENTB-MONOMER; Protein[@frameid="ENTB-MONOMER"]/dblink[dblink-db="UNIPROT"]; comment; Protein[@frameid="ENTB-MONOMER"]/dblink[dblink-db="UNIPROT"] | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-17 | https://pubmed.ncbi.nlm.nih.gov/20079748/; /resultList/result[id="20079748"]/abstractText | supports | Inspected retained indexed primary abstract only; claim kept within its stated experimental and evidence scope. |
| e-ref-18 | https://pathway.yeastgenome.org/getxml?META:PWY-5901; Pathway[@frameid="PWY-5901"]/reaction-list; reaction-layout; Pathway[@frameid="PWY-5901"]/reaction-ordering | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-19 | https://pathway.yeastgenome.org/getxml?META:ISOCHORSYN-RXN; Reaction[@frameid="ISOCHORSYN-RXN"]/dblink[dblink-db="RHEA"]; reaction-direction; left; right | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-20 | https://pathway.yeastgenome.org/getxml?META:ISOCHORMAT-RXN; Reaction[@frameid="ISOCHORMAT-RXN"]/dblink[dblink-db="RHEA"]; reaction-direction; left; right | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-21 | https://pathway.yeastgenome.org/getxml?META:DHBDEHYD-RXN; Reaction[@frameid="DHBDEHYD-RXN"]/dblink[dblink-db="RHEA"]; reaction-direction; left; right | supports | Inspected original source object and exact cited locators; structured assignments replayed independently. |
| e-ref-22 | https://europepmc.org/articles/PMC248643?pdf=render; PMC248643 full PDF pp.54-55, Identification of enzyme deficiency; Tables 2 and 3 | supports | Full original scanned PDF independently extracted/rendered. K12-derived mutant Table1/Methods and Results/Tables2–3 directly resolve EntC→EntB→EntA sequence and intermediate accumulation. |
| e-current | data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml; Entire final target and exact parsed delta against archived initial target | supports | Only p797→p796 supplementary locator changed; all other parsed record content unchanged. |
| e-prior | reviews/structured/20261011T061848Z-dhb-initial-independent-review/review.yaml; f-enta-discussion-page | context_only | Immutable confirmed initial issue359 finding retained as predecessor. |
| e-audit | research/pathway_additions/2026-10-11-next-195/dhb-independent-final-review-audit.json; Full independent initial replay, exact final delta and raw structured context hashes | supports | Independent technical/source work, not a substitute for primary scientific interpretation. |
| e-context | research/pathway_additions/2026-10-11-next-195/imodulondb-context.json; e_coli/precise_mg1655 queries entC/entB/entA; component52/FHL table | context_only | Direct unchanged canonical-client fallback after unavailable console. Exact gene hits b0593,b0595,b0596; FHL substring module hit has no exact selected member. No negative biology, reaction or regulatory conclusion. All37body hashes independently rechecked. |
| e-gates | research/pathway_additions/2026-10-11-next-195/integration-receipt.json; Final shared gates and graph/baseline receipt hashes | supports | Actual final coordinated checks passed; original interrupted test observation remains explicitly distinct. |

## Limits And Additional Notes

- Several primary mechanistic sources were inspected as indexed abstracts only; full PDFs were independently read for1971mutant pathway evidence and1989EntA assembly conflict. Database-assigned details are attributed to databases.
- Native holo-EntB is a supported catalyst state, not proof its carrier modification is necessary for the independently active N-terminal domain.
- EntA physical state varies by concentration/experiment; retained historical octamer conflicts with selected tetramer and dimer/tetramer equilibrium. No unique physiological assembly asserted.
- Mg cofactor evidence includes reviewed annotation limits; no occupancy/metal dependence inferred merely from crystal or assay Mg.
- No browser visual inspection; generated graph validation is programmatic.
- Full gates were executed by root; reviewer independently inspected exact results/logs rather than claiming personal execution.
- Final changed inputs were explicitly re-inspected and reassessed. Initial target/dossiers remain archived with exact hashes; immutable initial review preserved.
- Canonical final inspect ran on frozen final target, author receipts, shared authority/gate inputs and independent audit before this save.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T063128Z-dhb-final-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Final independent DHB scientific review and issue359 disposition
started_at: '2026-10-11T06:14:11Z'
finished_at: '2026-10-11T06:31:28Z'
reviewer:
  identity: Codex independent reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Did not author DHB or its dossiers; authored menaquinol in the
    same cohort, excluded from this review. Read complete DHB target and original
    primary/database evidence independently.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact full three-reaction PWY-5901 is supported for the qualified K-12
  implementation. Independently checked primary/native/UniProt sources and original
  Rhea sides support all 23 edges/55 evidence. Issue359 is resolved by the sole supplementary
  page locator change from797 to796. Holo-EntB state, EntA assembly conflict, abstract-only
  sources and annotation-level magnesium limits are explicit; final coordinated gates
  passed.
source:
  git_revision: d776b82c9c598bb79885ad01514b07900a678de0
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: 552a5c3065ba911a2273bb78920c55ea2d52d76743d778bd50607cab29dbc656
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 51eee8026be46917276ac3047b36e1f3905fa9a3cfaee1a84e6a385baaab09ac
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 56d26c06b72b5de61bb690d1e7b0e8b6e2410b1741ff5c7537f8c4c0506ba8f8
    role: context
  - path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    sha256: bdb60326e2ffa5db8e15939ce29bf57a12b992c1f2e56899c1cec3ecf01e2859
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: c635a91493a53b519ed2c8e0f825adcca320e1c8d96ef87a69459c8a2cb14937
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 3af37b2e92b0103da74bc462bedda1021c6bd262d3da13c030eb47344d08b61f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/authority-integration.json
    sha256: 64875d2a7007fb6a8f9bc471dfd910b5246f8ff932678dd7a324071a869f4ba8
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/baseline-preservation.json
    sha256: 27cd424f6c70786a31372a835be0b351db3c29fe90b6b01b2aeada5779c60af6
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-authority-inputs.json
    sha256: 401dec19b375edaf3ecf214d56e90625ef96fd5328edc2e1833d1872aaefd1ca
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-curation.md
    sha256: 3d74f64f9345fb5acd2c1702eb685e320935710646607d1bb306dc5fa887ffdc
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-dedup.json
    sha256: f594e1c6570f0c71272678fb5f9c733d2f36b131d948aeb3e4d27c03478d2fea
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-identifiers.json
    sha256: 0a3effc56559c3967c1c28831b6c2c69c5fdef1c79e6553901320a42dcd12574
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-independent-final-review-audit.json
    sha256: 88ad172df0905d6f20c7bfd8822fe2f1b9d706abbba945533b37ae02dd052069
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-independent-initial-review-audit.json
    sha256: 661d2c5268ea49cfbf6a79b69ca047a6d28712fe41bccbaa28563adba40bc245
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-replay.py
    sha256: 652d9d5d4fc7715ec5b206bc61c4d1ef1c91a4b04c2ba843073bef980b58884a
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-source-manifest.json
    sha256: e58c7ed818efe5df313016f6c80a831ccdd75715fe777ac252cf1a109b6fd7ac
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-source-projection.json
    sha256: 744ce6df76fb5c531c1c50ddb4e958830c67a885273e2b1d3621515d76c6fa28
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/dhb-validation.json
    sha256: 7f48b12d10b4da2e19ebe5faa9571d78d9677d48a3c3ce07a3385f12430d3546
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
  - path: reviews/structured/20261011T061848Z-dhb-initial-independent-review/review.yaml
    sha256: d5cfc8248bba60f525dcaa5ac1434d01f2c14584fe9e8d9657a71beed9910bdb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
targets:
- target_id: MetaCyc:PWY-5901
  path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
  label: 2,3-dihydroxybenzoate biosynthesis
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    role: maintained pathway record
scope:
  description: 'One complete frozen DHB record: full native boundary, every local
    node/edge/reference, primary scope, native assembly state, chemistry and final
    deterministic gates.'
  selection: Exact MetaCyc:PWY-5901 at final bdb60326e2ffa5db8e15939ce29bf57a12b992c1f2e56899c1cec3ecf01e2859
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5901
  exclusions:
  - target: Other cohort records
    reason: Reviewed separately; this reviewer authored menaquinol and does not independently
      certify that authored science.
  - target: Upstream chorismate and downstream enterobactin synthesis, CueO oxidation
    reason: Outside independently verified exact PWY5901 native boundary.
checks:
- check_id: inspect
  name: inspect
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-195-dhb-review-targets.yaml
    --input research/pathway_additions/2026-10-11-next-195/dhb-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-195/dhb-source-projection.json
    --input research/pathway_additions/2026-10-11-next-195/dhb-curation.md --input
    research/pathway_additions/2026-10-11-next-195/dhb-identifiers.json --input research/pathway_additions/2026-10-11-next-195/dhb-dedup.json
    --input research/pathway_additions/2026-10-11-next-195/dhb-validation.json --input
    src/pathwaymech/schema.py --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/CAUSAL_GRAPHS.md
  status: passed
  required: true
  summary: Canonical inspect ran before assessment and captured exact target/source
    inputs.
  target_ids:
  - MetaCyc:PWY-5901
  exit_code: 0
- check_id: final-render
  name: Final coordinated render
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  status: passed
  required: false
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-render.log SHA256
    ef7dbcc0be2b3270944edd90e5951c29b83bc76658603f0119132d50cb820956
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-validate
  name: Final coordinated validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: passed
  required: true
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-validate.log
    SHA256 7957d06519835efb547f4defb83a3043f6ed2107f9337b01a12cec71473fa6f1
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-test
  name: Final coordinated test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: passed
  required: true
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-test.log SHA256
    839e1447ccca9bf8f461d2ff81b9d4a576e600d3a91055a99698cce5550cf3e9
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-lint
  name: Final coordinated lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: passed
  required: true
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-lint.log SHA256
    df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-identifiers
  name: Final coordinated identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  status: passed
  required: false
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-identifiers.log
    SHA256 6410b6b35834a1c72c636fb95510a85d0b50254252e552b3e606465cdc0f9d5e
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-kgx
  name: Final coordinated kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-195-kgx
  status: passed
  required: false
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-kgx.log SHA256
    f5d2ef75b25ad170ae60547de4a3dc42302ca2c6b5b81970d7efe2d1b2191902
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-diff
  name: Final coordinated diff
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Delegated root execution; reviewer inspected actual terminal receipt and
    log content/hash. /private/tmp/pathwaymech-next-195-verification-diff.log SHA256
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  target_ids:
  - MetaCyc:PWY-5901
- check_id: independent-source-replay
  name: Independent original-source and graph replay
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-next-195-dhb-independent-audit.py
  status: passed
  required: false
  exit_code: 0
  summary: Actual terminal95491 exit0 on initial target:51 original body digests,23
    reference bodies,11 Rhea sides,3 balances, exact native three-step membership/modified
    assembly/protein bridges, and actual 23-edge/55-evidence KGX. Exact final parsed-object
    comparison proves only the p797→796 locator changed.
  target_ids:
  - MetaCyc:PWY-5901
- check_id: final-source-delta
  name: Independent exact final source delta
  command: .venv/bin/python /private/tmp/pathwaymech-next-195-dhb-final-recheck.py
  status: passed
  required: false
  exit_code: 0
  summary: 'Actual terminal0: sole changed parsed field is supplementary Discussion
    page. Reassessed the corrected locator against independently rendered original
    p796. Structured context all 37 body hashes independently rechecked.'
  target_ids:
  - MetaCyc:PWY-5901
- check_id: initial-test-interrupted
  name: Initial full-suite observation
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: failed
  required: false
  exit_code: 2
  summary: Initial pre-fix suite was deliberately interrupted by root after 1022 passed/3
    skipped to apply confirmed review corrections. Driver130 and KeyboardInterrupt2
    retained in initial receipt; no complete initial pass claimed. The final post-fix
    full run is recorded separately above.
  target_ids:
  - MetaCyc:PWY-5901
evidence:
- evidence_id: e-ref-0
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/18986 rh:substrates; http://rdf.rhea-db.org/18985_L
    rh:contains1 http://rdf.rhea-db.org/Participant_18985_compound_3304; http://rdf.rhea-db.org/Participant_18985_compound_3304
    rh:compound http://rdf.rhea-db.org/Compound_3304; rh:chebi; http://rdf.rhea-db.org/18986
    rh:products; http://rdf.rhea-db.org/18985_R rh:contains1 http://rdf.rhea-db.org/Participant_18985_compound_3577;
    http://rdf.rhea-db.org/Participant_18985_compound_3577 rh:compound http://rdf.rhea-db.org/Compound_3577;
    rh:chebi; http://rdf.rhea-db.org/18985 rh:directionalReaction http://rdf.rhea-db.org/18986;
    http://rdf.rhea-db.org/18985 rh:directionalReaction http://rdf.rhea-db.org/18986;
    rh:bidirectionalReaction http://rdf.rhea-db.org/18988; http://rdf.rhea-db.org/18986
    rh:products http://rdf.rhea-db.org/18985_R; http://rdf.rhea-db.org/18985_R rh:contains1
    http://rdf.rhea-db.org/Participant_18985_compound_3577; rh:compound http://rdf.rhea-db.org/Compound_3577;
    rh:chebi
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-ref-1
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/11113 rh:substrates; http://rdf.rhea-db.org/11112_L
    rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_3577; http://rdf.rhea-db.org/Participant_11112_compound_3577
    rh:compound http://rdf.rhea-db.org/Compound_3577; rh:chebi; http://rdf.rhea-db.org/11113
    rh:substrates; http://rdf.rhea-db.org/11112_L rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_1283;
    http://rdf.rhea-db.org/Participant_11112_compound_1283 rh:compound http://rdf.rhea-db.org/Compound_1283;
    rh:chebi; http://rdf.rhea-db.org/11113 rh:products; http://rdf.rhea-db.org/11112_R
    rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_5459; http://rdf.rhea-db.org/Participant_11112_compound_5459
    rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi; http://rdf.rhea-db.org/11113
    rh:products; http://rdf.rhea-db.org/11112_R rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_3719;
    http://rdf.rhea-db.org/Participant_11112_compound_3719 rh:compound http://rdf.rhea-db.org/Compound_3719;
    rh:chebi; http://rdf.rhea-db.org/11112 rh:directionalReaction http://rdf.rhea-db.org/11113;
    http://rdf.rhea-db.org/11113 rh:substrates http://rdf.rhea-db.org/11112_L; http://rdf.rhea-db.org/11112_L
    rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_3577; rh:compound
    http://rdf.rhea-db.org/Compound_3577; rh:chebi; http://rdf.rhea-db.org/11113 rh:products
    http://rdf.rhea-db.org/11112_R; http://rdf.rhea-db.org/11112_R rh:contains1 http://rdf.rhea-db.org/Participant_11112_compound_5459;
    rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-ref-2
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: http://rdf.rhea-db.org/23825 rh:substrates; http://rdf.rhea-db.org/23824_L
    rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_5459; http://rdf.rhea-db.org/Participant_23824_compound_5459
    rh:compound http://rdf.rhea-db.org/Compound_5459; rh:chebi; http://rdf.rhea-db.org/23825
    rh:substrates; http://rdf.rhea-db.org/23824_L rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_3484;
    http://rdf.rhea-db.org/Participant_23824_compound_3484 rh:compound http://rdf.rhea-db.org/Compound_3484;
    rh:chebi; http://rdf.rhea-db.org/23825 rh:products; http://rdf.rhea-db.org/23824_R
    rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_3751; http://rdf.rhea-db.org/Participant_23824_compound_3751
    rh:compound http://rdf.rhea-db.org/Compound_3751; rh:chebi; http://rdf.rhea-db.org/23825
    rh:products; http://rdf.rhea-db.org/23824_R rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_1650;
    http://rdf.rhea-db.org/Participant_23824_compound_1650 rh:compound http://rdf.rhea-db.org/Compound_1650;
    rh:chebi; http://rdf.rhea-db.org/23825 rh:products; http://rdf.rhea-db.org/23824_R
    rh:contains1 http://rdf.rhea-db.org/Participant_23824_compound_3249; http://rdf.rhea-db.org/Participant_23824_compound_3249
    rh:compound http://rdf.rhea-db.org/Compound_3249; rh:chebi; http://rdf.rhea-db.org/23824
    rh:directionalReaction http://rdf.rhea-db.org/23825; http://rdf.rhea-db.org/23825
    rh:substrates http://rdf.rhea-db.org/23824_L; http://rdf.rhea-db.org/23824_L rh:contains1
    http://rdf.rhea-db.org/Participant_23824_compound_5459; rh:compound http://rdf.rhea-db.org/Compound_5459;
    rh:chebi
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-ref-3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEJ2.json
  locator: /organism/taxonId; /comments/1/reaction; /comments/5; /comments/2/cofactors;
    /comments/2/note
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: 'Exact reviewed K12 EntC native JSON: reversible isochorismate reaction,
    monomer and experimental Mg annotation.'
  snapshot_sha256: 15c91f10c971c01fd6293782a86575c7f4543ea292b9bc741ec7f35ef8b9a4b6
- evidence_id: e-ref-4
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ENTC-MONOMER
  locator: Protein[@frameid="ENTC-MONOMER"]/catalyzes/Enzymatic-Reaction[@frameid="ENTC-ENZRXN"]/reaction;
    dblink[dblink-db="UNIPROT"]
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 52e0e6b20a111e2a648b47d8fe063fcd038a2de1553138bfdacba1d561836e91
- evidence_id: e-ref-5
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2139795/
  locator: /resultList/result[id="2139795"]/abstractText
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected retained indexed primary abstract only; claim kept within its
    stated experimental and evidence scope.
  snapshot_sha256: 85cfb55849c394ca17e80f980e7285886619c6f65f820e3d6d374ef9d079b46f
- evidence_id: e-ref-6
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ENTB-CPLX
  locator: Protein[@frameid="ENTB-CPLX"]/catalyzes/Enzymatic-Reaction[@frameid="ISOCHORMAT-ENZRXN"]/reaction;
    comment; Protein[@frameid="ENTB-CPLX"]/component/Protein[@frameid="HOLO-ENTB"];
    component/coefficient; comment; Protein[@frameid="ENTB-CPLX"]/catalyzes/Enzymatic-Reaction[@frameid="ISOCHORMAT-ENZRXN"];
    component
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 6de80c7a21186f5fd510252cbecf992748d13d421b996ff0b1169118b71f43d0
- evidence_id: e-ref-7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ADI4.json
  locator: /organism/taxonId; /comments/2/reaction; /comments/7; /comments/3/cofactors
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: 'Exact reviewed K12 native JSON: N-terminal isochorismatase, homodimer
    and magnesium annotation; C-terminal carrier modification/loading distinguished.'
  snapshot_sha256: 4bb0083a3305cf700583822edbc55244ac3ade3cf47b49847ee10495dd8464d1
- evidence_id: e-ref-8
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2139796/
  locator: /resultList/result[id="2139796"]/abstractText
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected retained indexed primary abstract only; claim kept within its
    stated experimental and evidence scope.
  snapshot_sha256: 715986c5918c80d590e79f0aac6c3f149d81bfbd791994232b410fc2e3312965
- evidence_id: e-ref-9
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ENTA-CPLX
  locator: Protein[@frameid="ENTA-CPLX"]/catalyzes/Enzymatic-Reaction[@frameid="DHBDEHYD-ENZRXN"]/reaction;
    comment; Protein[@frameid="ENTA-CPLX"]/component/Protein; component/coefficient;
    comment
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 94bfacaa03b3f3339833839470b382fdc28f7384fa92b70fcc535d1c18e6de88
- evidence_id: e-ref-10
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P15047.json
  locator: /organism/taxonId; /comments/1/reaction; /comments/5
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: 'Exact reviewed K12 EntA native JSON: net NAD reaction and homotetramer
    annotation; conflicts retained.'
  snapshot_sha256: b00850662da8517045c70ff9519dd5411795a6da50549184d13067eec86211a1
- evidence_id: e-ref-11
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/2144454/
  locator: /resultList/result[id="2144454"]/abstractText
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected retained indexed primary abstract only; claim kept within its
    stated experimental and evidence scope.
  snapshot_sha256: 04794f0f8e2ce8236604656840bf1503f51f3d4a10341098cc19029e9991c21e
- evidence_id: e-ref-12
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ENTA-MONOMER
  locator: Protein[@frameid="ENTA-MONOMER"]/dblink[dblink-db="UNIPROT"]; species/Organism
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: c7ef86c457fb2f332f054fcc6866e36f8b9ef591804d1ac6d302f1bdb608dfa2
- evidence_id: e-ref-13
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/21166461/
  locator: /resultList/result[id="21166461"]/abstractText
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected retained indexed primary abstract only; claim kept within its
    stated experimental and evidence scope.
  snapshot_sha256: 201f74cd1a680d18b48e939605ab3dbb7bd557e449079f558c59242da32d59a4
- evidence_id: e-ref-14
  kind: primary_source
  reference: https://europepmc.org/articles/PMC209666?pdf=render
  locator: PMC209666 full PDF p.795, Results/Purification of diDHB-DH; p.796 Discussion
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Full original scanned PDF independently extracted/rendered; purified EntA
    Results p795 and octamer Discussion p796 support historical conflict. p797 inspected
    and corrected as locator.
  snapshot_sha256: 7202c514814dfe9e67fc5838273b600f8479a0e43d7588f3313f7591e9d1a19f
- evidence_id: e-ref-15
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:HOLO-ENTB
  locator: Protein[@frameid="HOLO-ENTB"]/unmodified-form; component-of; Protein[@frameid="HOLO-ENTB"]/unmodified-form
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: d362d5b6e979a61c48384ee743b5ae26be7d41b92644f49d51860530a622842e
- evidence_id: e-ref-16
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ENTB-MONOMER
  locator: Protein[@frameid="ENTB-MONOMER"]/dblink[dblink-db="UNIPROT"]; comment;
    Protein[@frameid="ENTB-MONOMER"]/dblink[dblink-db="UNIPROT"]
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 7f8a62919119df6a3a2ccbf489ec3b88da45fd0941095e2cf7f0bdf52772d1b9
- evidence_id: e-ref-17
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/20079748/
  locator: /resultList/result[id="20079748"]/abstractText
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected retained indexed primary abstract only; claim kept within its
    stated experimental and evidence scope.
  snapshot_sha256: 939a0b488eb4c78e124c74398c41f137c95639cdba0fe85713a693d1f5ea1c58
- evidence_id: e-ref-18
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-5901
  locator: Pathway[@frameid="PWY-5901"]/reaction-list; reaction-layout; Pathway[@frameid="PWY-5901"]/reaction-ordering
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 2b978bba42064a27efcf351934b22c6c0fa9c335e1f24965cc70897daf22427c
- evidence_id: e-ref-19
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ISOCHORSYN-RXN
  locator: Reaction[@frameid="ISOCHORSYN-RXN"]/dblink[dblink-db="RHEA"]; reaction-direction;
    left; right
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 12b0f7a51414fd2dc6ea14d9596d9cc7f0fcc121d0843c434e3ae5b23af90198
- evidence_id: e-ref-20
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:ISOCHORMAT-RXN
  locator: Reaction[@frameid="ISOCHORMAT-RXN"]/dblink[dblink-db="RHEA"]; reaction-direction;
    left; right
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: 17750d21f912eb41d92fa0e73773cf03caa447c64bcf1467fda491f69175c76c
- evidence_id: e-ref-21
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:DHBDEHYD-RXN
  locator: Reaction[@frameid="DHBDEHYD-RXN"]/dblink[dblink-db="RHEA"]; reaction-direction;
    left; right
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Inspected original source object and exact cited locators; structured assignments
    replayed independently.
  snapshot_sha256: e694e624fe8f8d1690686a60f51bed77323eb276f5ccecf67ecc9860c83de4e0
- evidence_id: e-ref-22
  kind: primary_source
  reference: https://europepmc.org/articles/PMC248643?pdf=render
  locator: PMC248643 full PDF pp.54-55, Identification of enzyme deficiency; Tables
    2 and 3
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Full original scanned PDF independently extracted/rendered. K12-derived
    mutant Table1/Methods and Results/Tables2–3 directly resolve EntC→EntB→EntA sequence
    and intermediate accumulation.
  snapshot_sha256: 297a466d033a1c5898897547cf390837d23aa3ff25b97cb32318b3c0bd8c7aae
- evidence_id: e-current
  kind: record_content
  reference: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
  locator: Entire final target and exact parsed delta against archived initial target
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Only p797→p796 supplementary locator changed; all other parsed record content
    unchanged.
  snapshot_sha256: bdb60326e2ffa5db8e15939ce29bf57a12b992c1f2e56899c1cec3ecf01e2859
- evidence_id: e-prior
  kind: prior_review
  reference: reviews/structured/20261011T061848Z-dhb-initial-independent-review/review.yaml
  locator: f-enta-discussion-page
  accessed_at: '2026-10-11T06:31:28Z'
  support: context_only
  summary: Immutable confirmed initial issue359 finding retained as predecessor.
  snapshot_sha256: d5cfc8248bba60f525dcaa5ac1434d01f2c14584fe9e8d9657a71beed9910bdb
- evidence_id: e-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-195/dhb-independent-final-review-audit.json
  locator: Full independent initial replay, exact final delta and raw structured context
    hashes
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Independent technical/source work, not a substitute for primary scientific
    interpretation.
  snapshot_sha256: 88ad172df0905d6f20c7bfd8822fe2f1b9d706abbba945533b37ae02dd052069
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-195/imodulondb-context.json
  locator: e_coli/precise_mg1655 queries entC/entB/entA; component52/FHL table
  accessed_at: '2026-10-11T06:31:28Z'
  support: context_only
  summary: Direct unchanged canonical-client fallback after unavailable console. Exact
    gene hits b0593,b0595,b0596; FHL substring module hit has no exact selected member.
    No negative biology, reaction or regulatory conclusion. All37body hashes independently
    rechecked.
  snapshot_sha256: b68015a40f63072b8595b1dba8a173dfa9adc757e0aa60c5c9c4b9a5914eadd1
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-195/integration-receipt.json
  locator: Final shared gates and graph/baseline receipt hashes
  accessed_at: '2026-10-11T06:31:28Z'
  support: supports
  summary: Actual final coordinated checks passed; original interrupted test observation
    remains explicitly distinct.
  snapshot_sha256: 1d9098c0ce1286cee43d296db7ad74a6d47a5023ed54d9ed65eb87ea452614ef
assessments:
- assessment_id: identity
  area: identity
  topic: Exact complete native pathway
  outcome: supported
  summary: PWY5901 denotes all three chorismate→DHB transformations, independent from
    mixed PathBank map. Upstream chorismate, downstream siderophore maturation and
    CueO overlay have explicit exclusions.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-ref-18
  - e-ref-22
- assessment_id: chemistry
  area: graph
  topic: Exact chemistry, direction and continuity
  outcome: supported
  summary: Independently parsed originalRhea142:11 side occurrences and all 3 atom/charge
    balances. Exact2S,3S intermediate retained, complete NAD/NADH/hydron chemistry.
    Master/directed/bidirectional bridges grounded separately; reversible EntC given
    native pathway direction. No separate aromatization doublecount.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-ref-0
  - e-ref-1
  - e-ref-2
  - e-audit
- assessment_id: catalysts
  area: grounding
  topic: Protein role, modified state and assembly
  outcome: supported
  summary: Active monomer EntC supported. Exact native holo-EntB dimer retains two
    modified HOLO-ENTB components, without claiming carrier modification required
    for N-terminal lyase. EntA tetramer selected with historical octamer and concentration-dependent
    dimer/tetramer disagreement explicit; no obligatory channeling or fixed multienzyme
    complex.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-ref-3
  - e-ref-6
  - e-ref-15
  - e-ref-7
  - e-ref-9
  - e-ref-13
  - e-ref-14
- assessment_id: scope
  area: scope
  topic: Taxon, cofactor and evidence tiers
  outcome: supported
  summary: K12-derived primary experiments are distinguished from native MG1655 annotation;
    taxon83333 verified directly. EntC Mg two-ion annotation and EntB Mg without occupancy
    are explicit reviewed statements, not inflated abstract conclusions. NAD is reaction
    cosubstrate.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-ref-22
  - e-ref-3
  - e-ref-7
  - e-ref-17
  - e-context
- assessment_id: resolution
  area: provenance
  topic: Issue359 exact source location
  outcome: supported
  summary: Final p796 Discussion is the original octamer paragraph, visually verified
    alongside correct Results p795. Exact one-field delta resolves initial finding
    while preserving all prior bytes and lineage.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-prior
  - e-current
  - e-ref-14
  - e-audit
- assessment_id: gates
  area: schema
  topic: Deterministic and generated integrity
  outcome: supported
  summary: Final coordinated native/closed schema, identifiers, tests, lint, export
    and whitespace checks passed, with actual logs independently inspected and hashed.
    Source replay and source science assessed separately.
  target_ids:
  - MetaCyc:PWY-5901
  evidence_ids:
  - e-gates
  - e-audit
findings:
- finding_id: f-enta-discussion-page
  issue_key: dhb-enta-octamer-discussion-page
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Historical EntA octamer Discussion page is 796, not 797
  description: dhb-edge-015 PMID:2521622 evidence locates Discussion on printed p797.
    Original PDF places that octamer discussion at printed p796. Correctly cited Results
    p795 already supports the assertion; no chemistry or assembly change requested.
    Matching projected evidence in dhb-source-projection.json should follow the correction.
  target_ids:
  - MetaCyc:PWY-5901
  field_paths:
  - mechanistic_edges[id=dhb-edge-015]/evidence[reference_id=PMID:2521622]/source_locator
  evidence_ids:
  - e-prior
  - e-current
  - e-ref-14
  - e-audit
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-3-dihydroxybenzoate-biosynthesis.yaml
    role: maintained pathway record
  rule_id: review-yaml-record precise source locators
  native_severity: minor
  normalization_reason: Bounded retrieval/provenance error, with scientifically supported
    assertion and one correct existing primary locator.
  previous_occurrences:
  - repository: CultureBotAI/PathwayMech
    review_id: 20261011T061848Z-dhb-initial-independent-review
    finding_id: f-enta-discussion-page
  disposition_reason: Exact supplementary locator changed to printed p796; independently
    rendered original p796 confirms the octamer discussion, and the semantic diff
    contains no other record changes.
actions: []
limitations:
- Several primary mechanistic sources were inspected as indexed abstracts only; full
  PDFs were independently read for1971mutant pathway evidence and1989EntA assembly
  conflict. Database-assigned details are attributed to databases.
- Native holo-EntB is a supported catalyst state, not proof its carrier modification
  is necessary for the independently active N-terminal domain.
- EntA physical state varies by concentration/experiment; retained historical octamer
  conflicts with selected tetramer and dimer/tetramer equilibrium. No unique physiological
  assembly asserted.
- Mg cofactor evidence includes reviewed annotation limits; no occupancy/metal dependence
  inferred merely from crystal or assay Mg.
- No browser visual inspection; generated graph validation is programmatic.
- Full gates were executed by root; reviewer independently inspected exact results/logs
  rather than claiming personal execution.
notes:
- Final changed inputs were explicitly re-inspected and reassessed. Initial target/dossiers
  remain archived with exact hashes; immutable initial review preserved.
- Canonical final inspect ran on frozen final target, author receipts, shared authority/gate
  inputs and independent audit before this save.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/359
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261011T061848Z-dhb-initial-independent-review
  relationship: successor resolving issue359 with exact prior occurrence
```
