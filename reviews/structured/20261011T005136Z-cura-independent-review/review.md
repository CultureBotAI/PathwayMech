# Independent scientific review of the complete two-step CurA curcumin pathway

- Review: 20261011T005136Z-cura-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T00:43:07Z
- Finished UTC: 2026-10-11T00:51:36Z
- Reviewer: Codex independent CurA reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete two-step CurA pathway is supported across all 13 named nodes, 17 edges and 28 evidence blocks, preserving primary strain/construct, localization and endpoint limitations. No corrective finding identified in this target; final integrated gates passed.

## Scope And Provenance

Full independent scientific assessment of one maintained CurA record and its complete local graph/reference set.

Selection: Exact assigned GO:0036040 at data/pathways/curcumin-degradation.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 67c91f091fcbb215582b0cc479ea124a28315f2a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036040 | data/pathways/curcumin-degradation.yaml | maintained | curcumin catabolic process |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed inspect before assessment | passed | False | GO:0036040 | Initial actual terminal0 captured frozen target814e063d and seven author dossiers; all original input hashes unchanged at final recheck. |
| Independent raw replay | passed | False | GO:0036040 | Actual terminal0, 17 edges / 28 evidence reviewed; native identities,10 chemical sides, both step balances and net equation pass. |
| just render-pages | passed | False | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| just lint | passed | True | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| just check-identifiers | passed | False | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| git diff --check | passed | True | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| just kgx-export --output-dir /private/tmp/pathwaymech-next-routes-kgx | passed | False | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| just validate | passed | True | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| just test | passed | True | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 1048 passed, 3 skipped, 3 warnings in 181.71 s. |
| just vendored-check | passed | False | GO:0036040 | Parent actual terminal exit0, independently read and rehashed log; 174 record integrated scope; pass |
| Initial test run before final rerender | failed | False | GO:0036040 | 1047 passed, one committed-site-currentness test failed, three skipped; exact locator fixes during the initial run made generated pages stale. Rerendered and reran the full suite on the frozen final inputs. |
| Canonical structured-source CLI | unavailable | False | GO:0036040 | Parent runner attempt exited1 before retrieval with missing dotenv; structured CLI was unavailable. Unchanged direct client retrieval succeeded and exact CurA responses were independently rehashed/read. |

## Scientific And Domain Assessments

### Exact complete two-step curcumin route

identity: supported. Targets: GO:0036040.

GO identity is appropriate for the selected native two-step CurA pathway. Both intermediate and terminal product retained; one enzyme catalyzing two source-defined reactions does not collapse this into an isolated enzyme/reaction record. Full boundary matches both native sources.

### Direction, chemical forms and complete edges

representation: supported. Targets: GO:0036040.

All10 chemical edges match exact Rhea directed sides and coefficients, with balanced elements and charge. Both right_to_left metadata fields follow master orientation. The redundant two-NADPH net reaction is excluded. Primary product structures agree; mass/UV identification is not overstated as independent complete stereochemical determination.

### Physical homodimer and diffusible NADPH

evidence: supported. Targets: GO:0036040.

Both catalysis edges use the same explicitly supported homodimer. Native dimer membership and P76113 accession bridge agree with primary results. NADPH cofactor and consumed cosubstrate roles are compatible; no bound prosthetic or zinc requirement is inferred.

### Taxon, localization and biological limits

scope: supported. Targets: GO:0036040.

K12 DH10B purification/gene identification, recombinant BL21 characterization, current K12 UniProt and native MG1655 annotation are distinguished. Computational cytosol placement and unknown uptake/downstream fate are explicit. No in-vivo MG1655 flux, complete mineralization or universal strain activity is claimed.

### Edge-local citations and source limits

provenance: supported. Targets: GO:0036040.

All17 edge assertions and 28 evidence blocks inspected at their native locators; literal homodimer quote exact. Current UniProt recommended protein name and native complex label remain separate. Failed XML/SI requests remain unusable; successful full main paper supports retained mechanistic claims.

### Structured expression cross-check

evidence: supported. Targets: GO:0036040.

Applicable iModulon raw responses inspected after successful unchanged-client retrieval; gene hits provide context only. No matching module name and empty alias response are not negative biological evidence.

### Final deterministic gates and generated evidence preservation

graph: supported. Targets: GO:0036040.

Required integrated gates passed on final inputs, and graph/KGX receipts preserve all 17 edges and 28 evidence blocks for this target. Programmatic inspection is not a browser visual review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-record | data/pathways/curcumin-degradation.yaml; Entire frozen target, all 13 named nodes, 17 edges, 28 evidence blocks and 10 references | supports | Complete target read before assessment and rehashed before persistence; target unchanged since governed inspect. |
| e-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC3080977/?report=xml; Full main text; Results Discovery, Cofactors, Cloning, Overexpression, Molecular mass, Identification of Products; Discussion; Figures2–4; Materials and Methods | supports | Independently read successfully retained full main HTML. DH10B enzyme identification and recombinant BL21 characterization are separate; the paper demonstrates sequential reduction via DHC, NADPH rescue but not NADH rescue, an82kDa homodimer, and no further reduction beyond THC under the tested conditions. Main-text metal-independent conclusion is explicit. Detailed SI methods were unavailable. |
| e-figure | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8512/3080977/a0fde92c0e4c/pnas.1016217108fig04.jpg; Figure4, visually inspected actual downloaded image | supports | The two C=C reductions and DHC intermediate match retained chemical identities; both use NADPH. The figure does not establish MG1655 flux or further metabolism. |
| e-uniprot | https://rest.uniprot.org/uniprotkb/P76113.json; organism; genes; proteinDescription; comments0,2,3,6; physiologicalReactions; entryAudit | supports | Full raw reviewed entry supports K12 taxon83333, curA/yncB/b1449, separate physiological34821 and34813 reactions and experimental homodimer; current recommendedName differs from the native complex label and both are preserved. Release2026_03 verified in retained HTTP scientific metadata; entry158/sequence3. |
| e-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036040; results0 id/name/definition/xrefs/synonyms; independent go.db identity lookup | supports | The exact curcumin catabolic process term and curcumin degradation synonym cite this primary paper. The record narrows the process to the source-defined two-step Ecoli route rather than equating every curcumin transformation with it. |
| e-native | https://pathway.yeastgenome.org/getxml?META:PWY0-1527; Native PWY0-1527 reaction-list, reaction-ordering, layouts; separately inspected RXN0-6676 and RXN0-6677 enzyme and side fields | supports | MetaCyc22.5 native boundary has exactly both component reactions in sequence. RXN0-6676/6677 use CPLX0-7927 and native left-to-right reduction. This older public snapshot is distinguished from current reviewed UniProt. |
| e-assembly | https://pathway.yeastgenome.org/getxml?META:CPLX0-7927; component G6760-MONOMER coefficient2; molecular-weight-exp82; separately inspected G6760-MONOMER UNIPROT unification and has-go-term evidence | supports | Native dimer identity and accession bridge are explicit; primary gel filtration/SDS-PAGE agrees. Cytosol source has EV-COMP-AINF and is represented with that computational limitation; no monomer sufficiency or direct localization experiment is claimed. |
| e-pathbank | https://pathbank.org/downloads/pathbank_primary_biopax.zip; PW001896.owl; SMP0001910 pathway; Reactions5204/5205; Catalysis5165/5166; ProteinComplex3920; Protein10350/P76113 coefficient2 | supports | Direct BioPAX parsing independently corroborates both reactions and same dimer. PathBank acid forms of NADPH/NADP remain in research; exact Rhea anions define the graph species without acid-anion sameAs. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Merged repeated native RDF subjects34811/34813,34819/34821 and excluded34815/34817; directionalReaction/seeAlso/substrates/products/contains1/compound/chebi; directions TSV | supports | Independent fresh streaming replay verifies both right-to-left master-relative directions, every10 chemical-side locator and coefficient, exact native reaction links, and excluded multistep net. Native MetaCyc left-to-right and Rhea right-to-left are different source-equation conventions. |
| e-replay | /private/tmp/pathwaymech-cura-independent-review/replay.json; Independent replay.py and terminal0 replay.log; source bytes, SQL authority checks, family/side/assembly replays and balances | supports | Independent reviewer script validates all chemical/GO/taxon labels, native identities, reference-body hashes, exact source locators, both elemental/charge balances and their summed net. Fourteen usable raw source/archive bodies rehashed; discarded HTML bodies are not scientific evidence. |
| e-imodulon | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=curA; Retained API datasets and curA/yncB/b1449/curcumin response bodies; shared context and validation receipts | context_only | Reviewer independently rehashed and read the five applicable raw responses. curA,b1449,curcumin return gene b1449 and no module-name hits; yncB alias query empty. No module membership or biological absence inferred. Canonical CLI unavailable for missing dotenv; root ran unchanged client methods successfully. |
| e-search | /private/tmp/pathwaymech-cura-independent-review/duplicate-search.txt; Ignored-inclusive exact ID/accession/name search across data,research,reports,reviews | context_only | 126 hits include only this maintained pathway record and research/history context. Older single-enzyme rejection is superseded transparently by complete two-reaction pathway boundary reasoning; no assertion of source exhaustion. |
| e-gates | research/pathway_additions/2026-10-10-next-routes/integration-validation.json; Actual final terminal outcomes and log hashes inspected by independent reviewer | supports | Final integrated read-only gates and current graph/KGX output checks were executed by the parent and audited here; these deterministic corpus checks do not scientifically review other records. |

## Limits And Additional Notes

- MetaCyc source is explicitly public version22.5, complemented by current reviewed UniProt2026_03; no newest licensed MetaCyc claim.
- The full main primary paper and Fig4 were inspected. Supplementary PDF requests returned challenge/403 and were not inspected; main-text conclusions are not promoted to an independently reanalyzed supplementary experiment.
- In-vitro/recombinant characterization and DH10B observations do not establish native MG1655 flux. Cytosol evidence is computational; uptake and downstream THC fate remain outside this graph.
- Direct iModulon client retrieval succeeded after the canonical CLI failed before retrieval for missing dotenv. Empty module-name/alias hits are not absence evidence.
- Original Documents checkout was inaccessible; ignored-inclusive absence search covers the accessible worktree only. Browser surfaces unavailable; generated graph QA is programmatic.
- This is a bounded source review, not exhaustive current literature coverage or pathway-source exhaustion.
- Pyrimidine publication findings331 and333 were corrected by this reviewer in the separate author role; they do not constitute CurA findings or self-review of CurA.
- Fresh web access to PMC and ACS later-paper endpoints encountered challenge/403. Successfully acquired 2011 full main-text bytes and exact primary figure were inspected locally; search snippets did not supply any verdict claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T005136Z-cura-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of the complete two-step CurA curcumin pathway
started_at: '2026-10-11T00:43:07Z'
finished_at: '2026-10-11T00:51:36Z'
reviewer:
  identity: Codex independent CurA reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: A different agent authored CurA and its dossiers. This reviewer
    did not edit that target or its evidence; independently inspected primary/native
    sources and replayed raw RDF after governed inspect. This reviewer authored and
    corrected the separate pyrimidine pathway, which is excluded from this scientific
    verdict; prior broad candidate screening is disclosed.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete two-step CurA pathway is supported across all 13 named nodes,
  17 edges and 28 evidence blocks, preserving primary strain/construct, localization
  and endpoint limitations. No corrective finding identified in this target; final
  integrated gates passed.
source:
  git_revision: 67c91f091fcbb215582b0cc479ea124a28315f2a
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 296ab1a206afa3aa9b487eae7f5f8d836c09001a4ce9ee8016c36abe198cdc0d
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: ce251789f0e5b8b885a579e29a00a2a30e779143bfd6c4bdb9631d6b8fa6df17
    role: context
  - path: conf/sources.yaml
    sha256: 49507bca325f9529bd25b3507b062a1241c403916293dbab96d3cb598d6a7a95
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 309f7328f9020ec2f51fa043dcec03367d3fad49dc07163005655f33257dbbc6
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 9d24f21e66e5143261da9e785758df7dde23378fb119de9f7a4f22aa6dce4cab
    role: context
  - path: data/pathways/curcumin-degradation.yaml
    sha256: 814e063d50371068e9a7f3d6238b0f6ad76e172f6072c59b570cafdba0cb407b
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
  - path: pages/records/GO_0036040.html
    sha256: e1a950540f59a9ebd7eda26171d031ba4040a9c7935bd0faa8f7484fa7849c4e
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-curation.md
    sha256: e7e9620352f63dba94c958cf44e61dc6ab98be31e2e2a62ac4d7c70cc3f627df
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-identifiers.json
    sha256: 6f90db406c065f2881fe16acacf47c97abf82d5bbe8736755151b7209d8ae104
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-native-projection.json
    sha256: bc792657f2b062ce30b52fafc09634c6c8d322f91470d36ab8464caecdae159d
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-search-ledger.json
    sha256: d35d7b308dc4f9e813551fdc2b0c9991042e3f729f8d894730a24248600ee8ad
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-source-manifest.json
    sha256: 558fd751faa921a62bf70adfdbcbc86bb9bb3fad62a3364f6a2b1800f5532652
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-source-projection.json
    sha256: 34b62662eb1f1dd58a48dbd9946bb1bf5560f26678dbec61718d3b276dfc0372
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/curcumin-validation.json
    sha256: 3f91bded9e54dc5241c95af27fe8d587afb72e3c55c787a046caad504c9a1313
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/generated-graph-kgx-audit.json
    sha256: 994856e29535ca85f9aaf373f1d48c33f9ca70475801f67796a724c29184d496
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/imodulondb-context.json
    sha256: df0c92f7539a37a1a99f238977d64abbf2641677e9a93177f123bcba298c6aa1
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/imodulondb-independent-replay.json
    sha256: b6dc412632b69a75458d52f40e013b17a380989a3498c31c31147bf40016f7e7
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/imodulondb-source-manifest.json
    sha256: e17d6529edf8a5e10e12f79246b79cf1e0e632dbc3bc8a2cac818d343e410ef2
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/imodulondb-validation.json
    sha256: c26e49783b1bef409e77cefe3ab7bd23968bcdc4960eeccb631cbf39d7659abc
    role: context
  - path: research/pathway_additions/2026-10-10-next-routes/integration-validation.json
    sha256: 847b745e455243530ae69e25fb705ca4422d80f800c02c4ff5655d80d7299689
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Full independent scientific assessment of one maintained CurA record
    and its complete local graph/reference set.
  selection: Exact assigned GO:0036040 at data/pathways/curcumin-degradation.yaml.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036040
  exclusions:
  - target: All other records including the separately authored pyrimidine pathway
    reason: Outside this independent scientific assessment; full corpus deterministic
      gates do not scientifically review the corpus.
  - target: Uninspected supplementary PDF and later literature search leads
    reason: Supplementary access failed; later homolog engineering and alternative
      hydrolase search results are leads, not used as mechanistic evidence or interpreted
      as source exhaustion.
targets:
- target_id: GO:0036040
  path: data/pathways/curcumin-degradation.yaml
  label: curcumin catabolic process
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/curcumin-degradation.yaml
    role: maintained pathway owner
checks:
- check_id: c-inspect
  name: Governed inspect before assessment
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-cura-independent-review/targets.yaml
    [explicit context inputs retained in source]
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Initial actual terminal0 captured frozen target814e063d and seven author
    dossiers; all original input hashes unchanged at final recheck.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-record
- check_id: c-replay
  name: Independent raw replay
  command: .venv/bin/python /private/tmp/pathwaymech-cura-independent-review/replay.py
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Actual terminal0, 17 edges / 28 evidence reviewed; native identities,10
    chemical sides, both step balances and net equation pass.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-rhea
  - e-replay
- check_id: c-final-0
  name: just render-pages
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-render-final.log'
- check_id: c-final-1
  name: just lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-lint-final.log'
- check_id: c-final-2
  name: just check-identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-identifiers-final.log'
- check_id: c-final-3
  name: git diff --check
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-diff-final.log'
- check_id: c-final-4
  name: just kgx-export --output-dir /private/tmp/pathwaymech-next-routes-kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-routes-kgx
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-kgx-audit-cli.log'
- check_id: c-final-5
  name: just validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-validate-final.log'
- check_id: c-final-6
  name: just test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: Parent actual terminal exit0, independently read and rehashed log; 1048
    passed, 3 skipped, 3 warnings in 181.71 s.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-test-final.log'
- check_id: c-final-7
  name: just vendored-check
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: false
  summary: Parent actual terminal exit0, independently read and rehashed log; 174
    record integrated scope; pass
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: 'Executed by parent agent on frozen final inputs; independently audited
    exact receipt/log hashes, not rerun by this reviewer. Log: /private/tmp/pathwaymech-next-routes-vendored-final.log'
- check_id: c-initial-test
  name: Initial test run before final rerender
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 1
  expected_exit_code: 0
  status: failed
  required: false
  summary: 1047 passed, one committed-site-currentness test failed, three skipped;
    exact locator fixes during the initial run made generated pages stale. Rerendered
    and reran the full suite on the frozen final inputs.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  scope_note: Historical superseded parent run, not the final required gate. Initial
    failure retained openly; final complete suite passed after rerender.
- check_id: c-imodulon-cli
  name: Canonical structured-source CLI
  command: PYTHONPATH=/private/tmp/claw-published-duf-offline-20261007/src .venv/bin/python
    -m kg_microbe_sources imodulondb datasets
  status: unavailable
  required: false
  summary: Parent runner attempt exited1 before retrieval with missing dotenv; structured
    CLI was unavailable. Unchanged direct client retrieval succeeded and exact CurA
    responses were independently rehashed/read.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-imodulon
evidence:
- evidence_id: e-record
  kind: record_content
  reference: data/pathways/curcumin-degradation.yaml
  locator: Entire frozen target, all 13 named nodes, 17 edges, 28 evidence blocks
    and 10 references
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Complete target read before assessment and rehashed before persistence;
    target unchanged since governed inspect.
  snapshot_sha256: 814e063d50371068e9a7f3d6238b0f6ad76e172f6072c59b570cafdba0cb407b
- evidence_id: e-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3080977/?report=xml
  locator: Full main text; Results Discovery, Cofactors, Cloning, Overexpression,
    Molecular mass, Identification of Products; Discussion; Figures2–4; Materials
    and Methods
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Independently read successfully retained full main HTML. DH10B enzyme identification
    and recombinant BL21 characterization are separate; the paper demonstrates sequential
    reduction via DHC, NADPH rescue but not NADH rescue, an82kDa homodimer, and no
    further reduction beyond THC under the tested conditions. Main-text metal-independent
    conclusion is explicit. Detailed SI methods were unavailable.
  snapshot_sha256: 0087006dfbb589812da82459f7e09000d4d48eab7c537a13cce676d62fec2e65
- evidence_id: e-figure
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8512/3080977/a0fde92c0e4c/pnas.1016217108fig04.jpg
  locator: Figure4, visually inspected actual downloaded image
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: The two C=C reductions and DHC intermediate match retained chemical identities;
    both use NADPH. The figure does not establish MG1655 flux or further metabolism.
  snapshot_sha256: 99b35f6450c5cd7033beec613a1b5cd59d0255420f9647ac7c4fe84e1145d4f8
- evidence_id: e-uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P76113.json
  locator: organism; genes; proteinDescription; comments0,2,3,6; physiologicalReactions;
    entryAudit
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Full raw reviewed entry supports K12 taxon83333, curA/yncB/b1449, separate
    physiological34821 and34813 reactions and experimental homodimer; current recommendedName
    differs from the native complex label and both are preserved. Release2026_03 verified
    in retained HTTP scientific metadata; entry158/sequence3.
  snapshot_sha256: bd0d8f2a0e9532eb832736ca6bfbada22c279d412b0ac00c7f0384ee65e41a38
- evidence_id: e-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036040
  locator: results0 id/name/definition/xrefs/synonyms; independent go.db identity
    lookup
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: The exact curcumin catabolic process term and curcumin degradation synonym
    cite this primary paper. The record narrows the process to the source-defined
    two-step Ecoli route rather than equating every curcumin transformation with it.
  snapshot_sha256: 83e343c17b49b6800e3e32aa07fc27bf98a74c00e921a195d76a72708f64d386
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-1527
  locator: Native PWY0-1527 reaction-list, reaction-ordering, layouts; separately
    inspected RXN0-6676 and RXN0-6677 enzyme and side fields
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: MetaCyc22.5 native boundary has exactly both component reactions in sequence.
    RXN0-6676/6677 use CPLX0-7927 and native left-to-right reduction. This older public
    snapshot is distinguished from current reviewed UniProt.
  snapshot_sha256: 5f55b220915a56d6b0ea4b941487d024b852a14db9e8a1efc6d7c298c0ec86ed
- evidence_id: e-assembly
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:CPLX0-7927
  locator: component G6760-MONOMER coefficient2; molecular-weight-exp82; separately
    inspected G6760-MONOMER UNIPROT unification and has-go-term evidence
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Native dimer identity and accession bridge are explicit; primary gel filtration/SDS-PAGE
    agrees. Cytosol source has EV-COMP-AINF and is represented with that computational
    limitation; no monomer sufficiency or direct localization experiment is claimed.
  snapshot_sha256: f672f616d46ee50d7351f5c5b5bfa942a0e20c7a9a29e3286ad9933ac7b80886
- evidence_id: e-pathbank
  kind: database
  reference: https://pathbank.org/downloads/pathbank_primary_biopax.zip
  locator: PW001896.owl; SMP0001910 pathway; Reactions5204/5205; Catalysis5165/5166;
    ProteinComplex3920; Protein10350/P76113 coefficient2
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Direct BioPAX parsing independently corroborates both reactions and same
    dimer. PathBank acid forms of NADPH/NADP remain in research; exact Rhea anions
    define the graph species without acid-anion sameAs.
  snapshot_sha256: becce110780d247444c98ee0ed16b36e4d5f5ab9a9e61ba4201f82d3b36ebcbe
- evidence_id: e-rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Merged repeated native RDF subjects34811/34813,34819/34821 and excluded34815/34817;
    directionalReaction/seeAlso/substrates/products/contains1/compound/chebi; directions
    TSV
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Independent fresh streaming replay verifies both right-to-left master-relative
    directions, every10 chemical-side locator and coefficient, exact native reaction
    links, and excluded multistep net. Native MetaCyc left-to-right and Rhea right-to-left
    are different source-equation conventions.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-replay
  kind: validation
  reference: /private/tmp/pathwaymech-cura-independent-review/replay.json
  locator: Independent replay.py and terminal0 replay.log; source bytes, SQL authority
    checks, family/side/assembly replays and balances
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Independent reviewer script validates all chemical/GO/taxon labels, native
    identities, reference-body hashes, exact source locators, both elemental/charge
    balances and their summed net. Fourteen usable raw source/archive bodies rehashed;
    discarded HTML bodies are not scientific evidence.
  snapshot_sha256: 8fe74daeff8ea385db3a2c7b2ac85d9444cdee68a90be810d1e49e7c9e7c4b3d
- evidence_id: e-imodulon
  kind: database
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=curA
  locator: Retained API datasets and curA/yncB/b1449/curcumin response bodies; shared
    context and validation receipts
  accessed_at: '2026-10-11T00:51:19Z'
  support: context_only
  summary: Reviewer independently rehashed and read the five applicable raw responses.
    curA,b1449,curcumin return gene b1449 and no module-name hits; yncB alias query
    empty. No module membership or biological absence inferred. Canonical CLI unavailable
    for missing dotenv; root ran unchanged client methods successfully.
- evidence_id: e-search
  kind: search
  reference: /private/tmp/pathwaymech-cura-independent-review/duplicate-search.txt
  locator: Ignored-inclusive exact ID/accession/name search across data,research,reports,reviews
  accessed_at: '2026-10-11T00:51:19Z'
  support: context_only
  summary: 126 hits include only this maintained pathway record and research/history
    context. Older single-enzyme rejection is superseded transparently by complete
    two-reaction pathway boundary reasoning; no assertion of source exhaustion.
  search_scope: rg -n -uu -i -g '!.git/**' -g '!.venv/**' 'GO:0036040|PWY0-1527|SMP0001910|P76113|curcumin.*degrad|curcumin.*catabolic'
    data research reports reviews; hidden/ignored included. Original Documents checkout
    inaccessible, not searched successfully.
- evidence_id: e-gates
  kind: validation
  reference: research/pathway_additions/2026-10-10-next-routes/integration-validation.json
  locator: Actual final terminal outcomes and log hashes inspected by independent
    reviewer
  accessed_at: '2026-10-11T00:51:19Z'
  support: supports
  summary: Final integrated read-only gates and current graph/KGX output checks were
    executed by the parent and audited here; these deterministic corpus checks do
    not scientifically review other records.
assessments:
- assessment_id: a-identity
  area: identity
  topic: Exact complete two-step curcumin route
  outcome: supported
  summary: GO identity is appropriate for the selected native two-step CurA pathway.
    Both intermediate and terminal product retained; one enzyme catalyzing two source-defined
    reactions does not collapse this into an isolated enzyme/reaction record. Full
    boundary matches both native sources.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-go
  - e-native
  - e-pathbank
  - e-primary
- assessment_id: a-chemistry
  area: representation
  topic: Direction, chemical forms and complete edges
  outcome: supported
  summary: All10 chemical edges match exact Rhea directed sides and coefficients,
    with balanced elements and charge. Both right_to_left metadata fields follow master
    orientation. The redundant two-NADPH net reaction is excluded. Primary product
    structures agree; mass/UV identification is not overstated as independent complete
    stereochemical determination.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-rhea
  - e-replay
  - e-figure
  dimensions:
  - name: source_direction
    value: Rhea right-to-left; MetaCyc left-to-right
    definition: Orientation relative to each native master equation, preserving identical
      chemical reduction direction.
    evidence_ids:
    - e-rhea
    - e-native
- assessment_id: a-catalyst
  area: evidence
  topic: Physical homodimer and diffusible NADPH
  outcome: supported
  summary: Both catalysis edges use the same explicitly supported homodimer. Native
    dimer membership and P76113 accession bridge agree with primary results. NADPH
    cofactor and consumed cosubstrate roles are compatible; no bound prosthetic or
    zinc requirement is inferred.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-primary
  - e-assembly
  - e-uniprot
  - e-rhea
- assessment_id: a-scope
  area: scope
  topic: Taxon, localization and biological limits
  outcome: supported
  summary: K12 DH10B purification/gene identification, recombinant BL21 characterization,
    current K12 UniProt and native MG1655 annotation are distinguished. Computational
    cytosol placement and unknown uptake/downstream fate are explicit. No in-vivo
    MG1655 flux, complete mineralization or universal strain activity is claimed.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-primary
  - e-uniprot
  - e-assembly
  dimensions:
  - name: experimental_scope
    value: DH10B purification; recombinant BL21 characterization
    definition: Direct primary organism/construct scope, narrower than general Ecoli
      physiological activity.
    evidence_ids:
    - e-primary
  - name: localization_grade
    value: EV-COMP-AINF
    definition: Native computational annotation, not direct localization experiment.
    evidence_ids:
    - e-assembly
- assessment_id: a-provenance
  area: provenance
  topic: Edge-local citations and source limits
  outcome: supported
  summary: All17 edge assertions and 28 evidence blocks inspected at their native
    locators; literal homodimer quote exact. Current UniProt recommended protein name
    and native complex label remain separate. Failed XML/SI requests remain unusable;
    successful full main paper supports retained mechanistic claims.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-record
  - e-primary
  - e-native
  - e-assembly
  - e-rhea
  - e-replay
- assessment_id: a-context
  area: evidence
  topic: Structured expression cross-check
  outcome: supported
  summary: Applicable iModulon raw responses inspected after successful unchanged-client
    retrieval; gene hits provide context only. No matching module name and empty alias
    response are not negative biological evidence.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-imodulon
- assessment_id: a-integration
  area: graph
  topic: Final deterministic gates and generated evidence preservation
  outcome: supported
  summary: Required integrated gates passed on final inputs, and graph/KGX receipts
    preserve all 17 edges and 28 evidence blocks for this target. Programmatic inspection
    is not a browser visual review.
  target_ids:
  - GO:0036040
  evidence_ids:
  - e-gates
  - e-record
findings: []
actions: []
limitations:
- MetaCyc source is explicitly public version22.5, complemented by current reviewed
  UniProt2026_03; no newest licensed MetaCyc claim.
- The full main primary paper and Fig4 were inspected. Supplementary PDF requests
  returned challenge/403 and were not inspected; main-text conclusions are not promoted
  to an independently reanalyzed supplementary experiment.
- In-vitro/recombinant characterization and DH10B observations do not establish native
  MG1655 flux. Cytosol evidence is computational; uptake and downstream THC fate remain
  outside this graph.
- Direct iModulon client retrieval succeeded after the canonical CLI failed before
  retrieval for missing dotenv. Empty module-name/alias hits are not absence evidence.
- Original Documents checkout was inaccessible; ignored-inclusive absence search covers
  the accessible worktree only. Browser surfaces unavailable; generated graph QA is
  programmatic.
- This is a bounded source review, not exhaustive current literature coverage or pathway-source
  exhaustion.
notes:
- Pyrimidine publication findings331 and333 were corrected by this reviewer in the
  separate author role; they do not constitute CurA findings or self-review of CurA.
- Fresh web access to PMC and ACS later-paper endpoints encountered challenge/403.
  Successfully acquired 2011 full main-text bytes and exact primary figure were inspected
  locally; search snippets did not supply any verdict claim.
tags:
- pathway
- curcumin
- independent
- scientific-review
```
