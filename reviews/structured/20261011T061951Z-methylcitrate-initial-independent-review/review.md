# Initial independent scientific review of 2-methylcitrate cycle I

- Review: 20261011T061951Z-methylcitrate-initial-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T06:13:30.975936Z
- Finished UTC: 2026-10-11T06:19:51.793940Z
- Reviewer: Codex /root/pathway_authority_cache (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Full scientific target assessed; complete five-step native route and issued generic reaction representation are supported with unresolved absolute stereochemistry. One confirmed minor nearest-source provenance gap remains on PrpD metal-conflict description (#358). Required final corpus gates remain pending; immutable finding saved before correction.

## Scope And Provenance

One maintained pathway,24participants,5reactions,41edges,75evidence,27references.

Selection: Exact assigned target; full scientific review, no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d776b82c9c598bb79885ad01514b07900a678de0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-42 | data/pathways/2-methylcitrate-cycle-i.yaml | maintained | 2-methylcitrate cycle I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| inspect | passed | True | MetaCyc:PWY0-42 | Initial inspect before scientific assessment; all original inputs unchanged at save. |
| replay | passed | True | MetaCyc:PWY0-42 | Observed18764terminal0; earlier invocation lacked preserved terminal result and is not attested. |
| pdf | passed | True | MetaCyc:PWY0-42 | Actualexit0;14pages independently extracted; pages7/13 visually inspected. |
| test | failed | True | MetaCyc:PWY0-42 | Parent reports intentionally interrupted pre-fix run:1022passed3skipped,KeyboardInterrupt exit2; not a full pass. Final post-fix suite remains pending. |
| validate | unavailable | True | MetaCyc:PWY0-42 | Root reports pass but independent terminal receipt inspection deferred to successor; partial initial does not attest these gates. |
| lint | unavailable | True | MetaCyc:PWY0-42 | Root reports pass but independent terminal receipt inspection deferred to successor; partial initial does not attest these gates. |
| diff | unavailable | True | MetaCyc:PWY0-42 | Root reports pass but independent terminal receipt inspection deferred to successor; partial initial does not attest these gates. |

## Scientific And Domain Assessments

### Complete native pathway

identity: supported. Targets: MetaCyc:PWY0-42.

All five steps retained; external TCA regeneration and routeII excluded according to source boundary.

### Uncertainty-preserving exact chemistry

grounding: supported. Targets: MetaCyc:PWY0-42.

Issued generic57493/57497 and unspecified15598 preserve experimentally established transformations without assigning absolute stereo or all-isomer acceptance. This supports the representation branch of #332, not resolution of its biological question. All21sides/5balances match.

### Gene-product roles and assemblies

representation: supported. Targets: MetaCyc:PWY0-42.

PrpC dimer/PrpB tetramer have exact assemblies; PrpD monomer and AcnB enables preserve source scope. Activation alternatives remain inference-qualified.

### Strain and cofactor tiers

scope: supported. Targets: MetaCyc:PWY0-42.

NativeMG1655/reviewedK12 and actualW3350/Bacillus/Pseudomonas scopes remain distinct. Protein-levelMg/cluster assignments are qualified; no obligatoryPrpDcofactor asserted.

### Exact edge-local support

provenance: concern. Targets: MetaCyc:PWY0-42.

Other source assertions and reference metadata are supported; edge036 metal-conflict wording requires actual conflict sources attached locally.

## Findings

### f-prpd-metal-conflict-attribution: PrpD metal-conflict description lacks its actual source evidence

minor / open / confirmed; issue key: methylcitrate-prpd-metal-conflict-source-attribution.

Edge036 reports unstable2Fe2S versus no metal requirement, but attached P77243comments0/6/11, PMID28956599abstract and Rhea57497 do not report that conflict. Retained nativeG6199-MONOMER/comment and primary11782506 support a bounded conflict statement and need source-separated evidence. Issue https://github.com/CultureBotAI/PathwayMech/issues/358.

## Recommended Actions And Acceptance Checks

### attach-metal-conflict-sources

Attach exact native conflict source and primary unstable2Fe2S evidence; align precise wording to inspected source scope. Preserve reactions and no-obligatory-metal decision.

- Verify added reference/bodyhash/locator and source-specific assertions; do not attribute metal conflict to UniProt or2017abstract.
- Re-run source replay/render/full gates after correction and independently inspect changedbytes.
- Save successor retaining exact previous_occurrences lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/pathways/2-methylcitrate-cycle-i.yaml; Complete frozen YAML SHAea0940ee8eeb80d6552bed44e7afeeed4167866c919a291b750998997476745b | supports | Complete target read after canonical inspect;41edges/75evidence/27references. |
| native | https://pathway.yeastgenome.org/getxml?META:PWY0-42; Full pathway reaction-list/comment/layout; five reaction XML objects and component objects CPLX0-251/CPLX0-1021 | supports | Full five-step boundary includes propionate activation; external TCA regeneration and cycleII are explicitly separate. PrpC dimer/PrpB tetramer native coefficients and exact protein crosswalks match. |
| rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Original142 RDF87subjects; masters20373/57492/57496/17941/16809, directed20374/57493/57497/17943/16810; side containsN chains | supports | Independent streaming extraction confirms21sides/five balances and original generic parent links23780→57492,17725→57496, approved status and citation28956599. No specific equation is edited. |
| si | https://doi.org/10.1021/acs.biochem.7b00778; Original14-page supporting PDF SHA2380572de62615d206018042902b221f945f421d72961bb54f6c7cddba3361a2; S3,S5,S7,S10–S13 and PMID28956599 abstract | supports | Independently extracted all pages and visually read S7/S13. Comparative EcoliPrpC/PrpD experiments support the known transformations and cis branch while absolute stereochemistry remains unresolved; no universal acceptance claim. |
| chebi | https://ftp.ebi.ac.uk/pub/databases/chebi/; PinnedChEBI255 SQLite statements for all chemicals including15598,58853,10860 | supports | Generic15598 has C7H7O7 charge−3 and no InChI stereo layer. Disputed specific nodes absent from YAML/export. Primary biochemical comparison, not balance alone, grounds broader mapping. |
| later | https://pmc.ncbi.nlm.nih.gov/articles/PMC11982470/; Original BioC passages22/25/28/39/41/55, offset36579 | supports | 2025 PAO1 experiments and commercial LC-MS standards do not establish Ecoli absolute stereochemistry; Ecoli is heterologous expression host in this study. |
| protein | https://rest.uniprot.org/uniprotkb/P77243.json; Complete reviewed2026_03 six proteins P77495/P27550/P31660/P77243/P36683/P77541, exact comments/catalytic crossrefs/organisms | supports | PrpE remains annotated alternative; Acs propionate inference is separately grounded in native/primary context, not its acetate UniProt equation. PrpD monomer and AcnB enables retain assembly scope; AcsMg,AcnB4Fe4S and PrpBMg preserve evidence tier. |
| primary | https://pubmed.ncbi.nlm.nih.gov/12473114/; Inspected full indexed abstracts11422389/12473114/12706720/11782506/11992126/9579066; auxiliary serialized2002 publisher excerpts369–385 | supports | NativeMG1655/reviewedK12 versus actualW3350 propionate experiments are distinguished. Older assembly/metal conclusions retain abstract or database scope. |
| metal | https://pathway.yeastgenome.org/getxml?META:G6199-MONOMER; Full Protein frameG6199-MONOMER comment; PMID11782506 abstract; compare attached P77243 comments0/6/11 | refutes | Native comment explicitly reports disagreement whether PrpD contains an Fe-S cluster. Primary11782506 gives exact unstable2Fe2S. Edge036 attached sources concern function/monomer/stereo, not its precise metal-conflict description. |
| audit | research/pathway_additions/2026-10-11-next-195/propanoyl-independent-review-audit.json; Independent replay18764 terminal0;39bodyhashes,87originalRDFsubjects,21sides,5balances,twoassemblies,sixproteinprojections,actualKGX | supports | All technical source/chemistry checks passed; all41edges/75evidence/31nodes and descriptions preserved without disputed specific stereochemical nodes. Source replay complements scientific review. |
| context | research/pathway_additions/2026-10-11-next-195/imodulondb-context.json; e_coli/precise_mg1655 prpB/b0331,prpC/b0333,prpD/b0334,prpE/b0335; component52 table; unchanged canonical client receipts | supports | Exactgene hits, no corresponding module-name hits; only component52 from broad cohort search summarized. No candidate members there, no biological absence claim; Acs/AcnB not queried. Computational context only. |
| dedup | research/pathway_additions/2026-10-11-next-195/propanoyl-duplicate-searches.json; Ignored/hidden-inclusive author original+worktree searches and reviewer rg --no-ignore --hidden over data/pathways/research; prior propanoyl-handoff | supports | Existing Sbm and other routes differ; prior issue332 deferral explicitly reassessed rather than overwritten. |

## Limits And Additional Notes

- Final required full-corpus gate receipts pending; full scientific coverage does not make this a completedreview.
- Absolute methylcitrate configuration remains unresolved; generic identities do not establish universal isomer acceptance.
- 2017 mainpaper and older primaries are abstract-scoped; fullSI independently inspected. Serialized2002publisher excerpts are transformed context, not original HTML.
- iModulon computational context is not catalysis or absence proof; Acs/AcnB were not searched.
- Programmatic KGX audit is not browser visual inspection.
- No reviewed target/sharedfiles edited. Parent owns issue358 and coordinated correction.
- Issue332 representation assessment is separate from minor358; no fabricated previous finding or biological stereo resolution.
- Initial reviewer document validation rejected YAML aliases and incorrect publication/record enum values. Corrected review serialization and metadata only; target/source bytes unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T061951Z-methylcitrate-initial-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Initial independent scientific review of 2-methylcitrate cycle I
started_at: '2026-10-11T06:13:30.975936Z'
finished_at: '2026-10-11T06:19:51.793940Z'
reviewer:
  identity: Codex /root/pathway_authority_cache
  kind: agent
  independence: independent
  independence_basis: Did not author methylcitrate target/dossiers. Authored separateDHB.
    Independently inspected primary/native/protein/chemical originals and actualKGX;
    root owns sharedgates.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Full scientific target assessed; complete five-step native route and issued
  generic reaction representation are supported with unresolved absolute stereochemistry.
  One confirmed minor nearest-source provenance gap remains on PrpD metal-conflict
  description (#358). Required final corpus gates remain pending; immutable finding
  saved before correction.
scope:
  description: One maintained pathway,24participants,5reactions,41edges,75evidence,27references.
  selection: Exact assigned target; full scientific review, no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-42
  exclusions:
  - target: Other scientific records
    reason: Separate author/reviewer assignments.
source:
  git_revision: d776b82c9c598bb79885ad01514b07900a678de0
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 51eee8026be46917276ac3047b36e1f3905fa9a3cfaee1a84e6a385baaab09ac
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 56d26c06b72b5de61bb690d1e7b0e8b6e2410b1741ff5c7537f8c4c0506ba8f8
    role: context
  - path: data/pathways/2-methylcitrate-cycle-i.yaml
    sha256: ea0940ee8eeb80d6552bed44e7afeeed4167866c919a291b750998997476745b
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
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-context.json
    sha256: b68015a40f63072b8595b1dba8a173dfa9adc757e0aa60c5c9c4b9a5914eadd1
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-parser-replay.json
    sha256: 5e1a3aae8d47c568a3ca74a851a90edb287b3362016bfeed99d42d6e51450eeb
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/imodulondb-runner-availability.json
    sha256: 7996cefbe69cc800c1b560de79e17a0ac65e18147fb847311ecd87513058766a
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-assessment.json
    sha256: d34b3c67a6a1a74707f75b3c0b71111338f59aff408c62c5419c39439fa5407f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-coverage.json
    sha256: e55cff246b6fc483153832b7943697c9a27963f010f5b2e119968d960fa45e69
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-curation.md
    sha256: 729ef9abceed65984e0120b6aa452d943fd8e7c833cb5fd8ca3caeba74884c65
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-duplicate-searches.json
    sha256: a854995ebad2c69721dca4f6c94e2a2bd5d22f7f77ad7a21069409cb6ebe66a9
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-identifiers.json
    sha256: 7c869e339fed648259e1056bf6141a47fc8f189763a87c0b43b82856f9d47d5f
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-independent-review-audit.json
    sha256: 75ee09ec4080513ee43effe7b36d420c5baa1499e1a455af2dc7317ca8204db9
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-replay.py
    sha256: 8b6eb12b4198b33107702a6868f5b89a9561a9dae239d944634de3f6df47a720
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-source-manifest.json
    sha256: e8f3feeffa19dbb6bd290155e3fbbc87f5018aab88042f580f7fd6583b45b3b5
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-source-projection.json
    sha256: 0ebeaf0a3b678aa8567baa83276020b6ff87a797529dd6c90737c81538a0fe1d
    role: context
  - path: research/pathway_additions/2026-10-11-next-195/propanoyl-validation.json
    sha256: 1e3a5bdc547d1c653cd5c7bbdd918c5cde3622dd8ceddb459b9da1c0d452bfa3
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY0-42
  path: data/pathways/2-methylcitrate-cycle-i.yaml
  label: 2-methylcitrate cycle I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-methylcitrate-cycle-i.yaml
    role: maintained pathway record
checks:
- check_id: inspect
  name: inspect
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-195-evidence/methylcitrate-review/targets.yaml
    --input conf/identifier_policy.yaml --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input data/pathways/2-methylcitrate-cycle-i.yaml
    --input docs/CAUSAL_GRAPHS.md --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-195/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-assessment.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-coverage.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-curation.md --input
    research/pathway_additions/2026-10-11-next-195/propanoyl-duplicate-searches.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-identifiers.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-replay.py --input
    research/pathway_additions/2026-10-11-next-195/propanoyl-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-source-projection.json
    --input research/pathway_additions/2026-10-11-next-195/propanoyl-validation.json
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
  summary: Initial inspect before scientific assessment; all original inputs unchanged
    at save.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - target
  exit_code: 0
  expected_exit_code: 0
- check_id: replay
  name: replay
  status: passed
  required: true
  command: PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-next-195-evidence/methylcitrate-review/replay.py
  summary: Observed18764terminal0; earlier invocation lacked preserved terminal result
    and is not attested.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - audit
  exit_code: 0
  expected_exit_code: 0
- check_id: pdf
  name: pdf
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache uv run --offline
    --no-project --with pypdfium2 --with pillow python -
  summary: Actualexit0;14pages independently extracted; pages7/13 visually inspected.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - target
  exit_code: 0
  expected_exit_code: 0
- check_id: test
  name: test
  status: failed
  required: true
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  summary: Parent reports intentionally interrupted pre-fix run:1022passed3skipped,KeyboardInterrupt
    exit2; not a full pass. Final post-fix suite remains pending.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - target
  exit_code: 2
  expected_exit_code: 0
- check_id: validate
  name: validate
  status: unavailable
  required: true
  command: just validate
  summary: Root reports pass but independent terminal receipt inspection deferred
    to successor; partial initial does not attest these gates.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - target
- check_id: lint
  name: lint
  status: unavailable
  required: true
  command: just lint
  summary: Root reports pass but independent terminal receipt inspection deferred
    to successor; partial initial does not attest these gates.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - target
- check_id: diff
  name: diff
  status: unavailable
  required: true
  command: git diff --check
  summary: Root reports pass but independent terminal receipt inspection deferred
    to successor; partial initial does not attest these gates.
  target_ids:
  - MetaCyc:PWY0-42
  evidence_ids:
  - target
evidence:
- evidence_id: target
  kind: record_content
  reference: data/pathways/2-methylcitrate-cycle-i.yaml
  locator: Complete frozen YAML SHAea0940ee8eeb80d6552bed44e7afeeed4167866c919a291b750998997476745b
  summary: Complete target read after canonical inspect;41edges/75evidence/27references.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-42
  locator: Full pathway reaction-list/comment/layout; five reaction XML objects and
    component objects CPLX0-251/CPLX0-1021
  summary: Full five-step boundary includes propionate activation; external TCA regeneration
    and cycleII are explicitly separate. PrpC dimer/PrpB tetramer native coefficients
    and exact protein crosswalks match.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Original142 RDF87subjects; masters20373/57492/57496/17941/16809, directed20374/57493/57497/17943/16810;
    side containsN chains
  summary: Independent streaming extraction confirms21sides/five balances and original
    generic parent links23780→57492,17725→57496, approved status and citation28956599.
    No specific equation is edited.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: si
  kind: primary_source
  reference: https://doi.org/10.1021/acs.biochem.7b00778
  locator: Original14-page supporting PDF SHA2380572de62615d206018042902b221f945f421d72961bb54f6c7cddba3361a2;
    S3,S5,S7,S10–S13 and PMID28956599 abstract
  summary: Independently extracted all pages and visually read S7/S13. Comparative
    EcoliPrpC/PrpD experiments support the known transformations and cis branch while
    absolute stereochemistry remains unresolved; no universal acceptance claim.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: chebi
  kind: authority
  reference: https://ftp.ebi.ac.uk/pub/databases/chebi/
  locator: PinnedChEBI255 SQLite statements for all chemicals including15598,58853,10860
  summary: Generic15598 has C7H7O7 charge−3 and no InChI stereo layer. Disputed specific
    nodes absent from YAML/export. Primary biochemical comparison, not balance alone,
    grounds broader mapping.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: later
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11982470/
  locator: Original BioC passages22/25/28/39/41/55, offset36579
  summary: 2025 PAO1 experiments and commercial LC-MS standards do not establish Ecoli
    absolute stereochemistry; Ecoli is heterologous expression host in this study.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: protein
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P77243.json
  locator: Complete reviewed2026_03 six proteins P77495/P27550/P31660/P77243/P36683/P77541,
    exact comments/catalytic crossrefs/organisms
  summary: PrpE remains annotated alternative; Acs propionate inference is separately
    grounded in native/primary context, not its acetate UniProt equation. PrpD monomer
    and AcnB enables retain assembly scope; AcsMg,AcnB4Fe4S and PrpBMg preserve evidence
    tier.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: primary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/12473114/
  locator: Inspected full indexed abstracts11422389/12473114/12706720/11782506/11992126/9579066;
    auxiliary serialized2002 publisher excerpts369–385
  summary: NativeMG1655/reviewedK12 versus actualW3350 propionate experiments are
    distinguished. Older assembly/metal conclusions retain abstract or database scope.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: metal
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:G6199-MONOMER
  locator: Full Protein frameG6199-MONOMER comment; PMID11782506 abstract; compare
    attached P77243 comments0/6/11
  summary: Native comment explicitly reports disagreement whether PrpD contains an
    Fe-S cluster. Primary11782506 gives exact unstable2Fe2S. Edge036 attached sources
    concern function/monomer/stereo, not its precise metal-conflict description.
  support: refutes
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-195/propanoyl-independent-review-audit.json
  locator: Independent replay18764 terminal0;39bodyhashes,87originalRDFsubjects,21sides,5balances,twoassemblies,sixproteinprojections,actualKGX
  summary: All technical source/chemistry checks passed; all41edges/75evidence/31nodes
    and descriptions preserved without disputed specific stereochemical nodes. Source
    replay complements scientific review.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-195/imodulondb-context.json
  locator: e_coli/precise_mg1655 prpB/b0331,prpC/b0333,prpD/b0334,prpE/b0335; component52
    table; unchanged canonical client receipts
  summary: Exactgene hits, no corresponding module-name hits; only component52 from
    broad cohort search summarized. No candidate members there, no biological absence
    claim; Acs/AcnB not queried. Computational context only.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
- evidence_id: dedup
  kind: record_content
  reference: research/pathway_additions/2026-10-11-next-195/propanoyl-duplicate-searches.json
  locator: Ignored/hidden-inclusive author original+worktree searches and reviewer
    rg --no-ignore --hidden over data/pathways/research; prior propanoyl-handoff
  summary: Existing Sbm and other routes differ; prior issue332 deferral explicitly
    reassessed rather than overwritten.
  support: supports
  accessed_at: '2026-10-11T06:19:51.793940Z'
assessments:
- assessment_id: identity
  area: identity
  topic: Complete native pathway
  outcome: supported
  target_ids:
  - MetaCyc:PWY0-42
  summary: All five steps retained; external TCA regeneration and routeII excluded
    according to source boundary.
  evidence_ids:
  - target
  - native
  - dedup
- assessment_id: chemistry
  area: grounding
  topic: Uncertainty-preserving exact chemistry
  outcome: supported
  target_ids:
  - MetaCyc:PWY0-42
  summary: 'Issued generic57493/57497 and unspecified15598 preserve experimentally
    established transformations without assigning absolute stereo or all-isomer acceptance.
    This supports the representation branch of #332, not resolution of its biological
    question. All21sides/5balances match.'
  evidence_ids:
  - rhea
  - chebi
  - si
  - later
  - audit
- assessment_id: roles
  area: representation
  topic: Gene-product roles and assemblies
  outcome: supported
  target_ids:
  - MetaCyc:PWY0-42
  summary: PrpC dimer/PrpB tetramer have exact assemblies; PrpD monomer and AcnB enables
    preserve source scope. Activation alternatives remain inference-qualified.
  evidence_ids:
  - native
  - protein
  - primary
- assessment_id: scope
  area: scope
  topic: Strain and cofactor tiers
  outcome: supported
  target_ids:
  - MetaCyc:PWY0-42
  summary: NativeMG1655/reviewedK12 and actualW3350/Bacillus/Pseudomonas scopes remain
    distinct. Protein-levelMg/cluster assignments are qualified; no obligatoryPrpDcofactor
    asserted.
  evidence_ids:
  - protein
  - primary
  - context
- assessment_id: provenance
  area: provenance
  topic: Exact edge-local support
  outcome: concern
  target_ids:
  - MetaCyc:PWY0-42
  summary: Other source assertions and reference metadata are supported; edge036 metal-conflict
    wording requires actual conflict sources attached locally.
  evidence_ids:
  - target
  - metal
  - audit
findings:
- finding_id: f-prpd-metal-conflict-attribution
  issue_key: methylcitrate-prpd-metal-conflict-source-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: PrpD metal-conflict description lacks its actual source evidence
  description: Edge036 reports unstable2Fe2S versus no metal requirement, but attached
    P77243comments0/6/11, PMID28956599abstract and Rhea57497 do not report that conflict.
    Retained nativeG6199-MONOMER/comment and primary11782506 support a bounded conflict
    statement and need source-separated evidence. Issue https://github.com/CultureBotAI/PathwayMech/issues/358.
  target_ids:
  - MetaCyc:PWY0-42
  field_paths:
  - mechanistic_edges[id=methylcitrate-edge-036]/description
  - mechanistic_edges[id=methylcitrate-edge-036]/evidence
  - references
  evidence_ids:
  - target
  - metal
  - protein
  rule_id: 'review-yaml-record Evidence Rules: narrowest edge and exact source assertion'
  native_severity: minor
  normalization_reason: Bounded provenance gap; retained originals support uncertainty
    and chemistry remains sound.
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-methylcitrate-cycle-i.yaml
    role: maintained_record
actions:
- action_id: attach-metal-conflict-sources
  description: Attach exact native conflict source and primary unstable2Fe2S evidence;
    align precise wording to inspected source scope. Preserve reactions and no-obligatory-metal
    decision.
  finding_ids:
  - f-prpd-metal-conflict-attribution
  target_ids:
  - MetaCyc:PWY0-42
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/2-methylcitrate-cycle-i.yaml
    role: maintained_record
  acceptance_checks:
  - Verify added reference/bodyhash/locator and source-specific assertions; do not
    attribute metal conflict to UniProt or2017abstract.
  - Re-run source replay/render/full gates after correction and independently inspect
    changedbytes.
  - Save successor retaining exact previous_occurrences lineage.
limitations:
- Final required full-corpus gate receipts pending; full scientific coverage does
  not make this a completedreview.
- Absolute methylcitrate configuration remains unresolved; generic identities do not
  establish universal isomer acceptance.
- 2017 mainpaper and older primaries are abstract-scoped; fullSI independently inspected.
  Serialized2002publisher excerpts are transformed context, not original HTML.
- iModulon computational context is not catalysis or absence proof; Acs/AcnB were
  not searched.
- Programmatic KGX audit is not browser visual inspection.
notes:
- No reviewed target/sharedfiles edited. Parent owns issue358 and coordinated correction.
- Issue332 representation assessment is separate from minor358; no fabricated previous
  finding or biological stereo resolution.
- Initial reviewer document validation rejected YAML aliases and incorrect publication/record
  enum values. Corrected review serialization and metadata only; target/source bytes
  unchanged.
```
