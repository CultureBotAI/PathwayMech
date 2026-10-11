# Independent scientific review of complete myxochelin A and B biosynthesis

- Review: 20261011T172833Z-myxochelin-a-b-independent-scientific-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T17:26:24Z
- Finished UTC: 2026-10-11T17:28:33.014036Z
- Reviewer: Codex /root/ed_whole_record_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The entire maintained Myxochelin A/B record is supported within its stated scope. All9 native reactions,78 edges,239 evidence occurrences and62 references were assessed against original structured objects and inspected primary evidence. Fresh current checks confirm native directions, structures, sequence bridges and production source versions; current full-corpus gates and graph preservation passed. No new actionable finding. Historical issues402/404 have evidence-backed fixes and are described as external lineage, without fabricated canonical predecessors.

## Scope And Provenance

Whole-record scientific review of the complete maintained MetaCyc:PWY-8383 record and exact local context/proof inputs after final integration freeze.

Selection: The single explicitly assigned maintained myxochelin-a-and-b-biosynthesis.yaml, unchanged target SHA5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base babe44ad1992d2950701e432f400965631d538a7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-8383 | data/pathways/myxochelin-a-and-b-biosynthesis.yaml | maintained | myxochelin A and B biosynthesis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| render | passed | True | MetaCyc:PWY-8383 | Rendered218 records. |
| validate | passed | True | MetaCyc:PWY-8383 | Current full corpus validation passed, including schema, history, identifiers, evidence and page currency. |
| test | passed | True | MetaCyc:PWY-8383 | 1256 tests passed;3 skipped;3 warnings. |
| lint | passed | True | MetaCyc:PWY-8383 | All lint checks passed. |
| identifiers | passed | True | MetaCyc:PWY-8383 | 218 records passed authority identity/label checks. |
| kgx | passed | True | MetaCyc:PWY-8383 | Separate KGX export from218 records completed. |
| diff-tracked | passed | True | MetaCyc:PWY-8383 | Tracked whitespace check passed. |
| Current reviewer original-source audit | passed | True | MetaCyc:PWY-8383 | 103 response digests,239 locators,9members,46sides,13 exact selected InChIs and4 CDS bridges passed. |
| Current reviewer authority/metadata audit | passed | True | MetaCyc:PWY-8383 | All prior entries preserved and all21 corrected source versions match original bodies. |
| Current integrated source/runtime checks | passed | True | MetaCyc:PWY-8383 | All4 child checks and1645 endpoint bindings passed. |
| Generated SVG and KGX preservation | passed | True | MetaCyc:PWY-8383 | 37SVG/38KGX nodes,78 edges,239 evidence objects and prior corpus preservation passed. |
| Complete staged whitespace check | passed | True | MetaCyc:PWY-8383 | Complete staged change set passed git diff --cached --check. |
| Canonical input capture | passed | True | MetaCyc:PWY-8383 | Actual inspect captured80 final input files and exact working-tree target at basebabe44ad. |

## Scientific And Domain Assessments

### Exact native pathway and supplied precursor boundary

identity: supported. Targets: MetaCyc:PWY-8383.

The record denotes MetaCyc:PWY-8383 with all nine native reaction objects and both myxochelin product branches. PWY-5901 precursor supply remains separate. Composite RXN-23309/RXN-23311 are explanatory enzyme activities rather than additional pathway steps.

### Chemical identities, direction and carrier classes

grounding: supported. Targets: MetaCyc:PWY-8383.

Fresh original XML-to-YAML comparison confirms 46 chemical sides and native physiological right-to-left RXN-23314. Thirteen small-molecule native InChIs match selected original ChEBI SQL assertions exactly. Native myxochelin A has a specified stereocenter absent from CHEBI:31877 and retains its narrower MetaCyc ID. B matches CHEBI:7061 by exact structure, without adopting contradictory prose. Six carrier states are native Protein classes and are not misrepresented as free metabolites or fully formulated polypeptides.

### Derived material balance

quantity: supported. Targets: MetaCyc:PWY-8383.

The preserved independently reviewed source audit reports zero elemental/charge residual for all nine reactions using explicitly symbolic carrier scaffolds, and carrier cancellation for both product nets. Each product requires two DHB activation/loading cycles and one lysine activation, hence three ATP-to-AMP events; A uses two NADPH, B uses one NADPH plus glutamate. These are derived stoichiometric accounting results, not measured yields, whole-protein formulas or energetics.

### Primary reconstitution and branch evidence

evidence: supported. Targets: MetaCyc:PWY-8383.

Fresh reading of the complete relevant 2001 Methods/Results/Discussion and Figure 5 supports E/F/G reconstitution, lysine activation/loading, two condensations, and reductive release. That paper directly identifies A; MxcL/B was proposed there. Fresh reading of all four 2008 SI pages supplies His6-MxcL/PLP spectra, E/F/G/L reconstitution producing A and B, and MS2/PFBHA methods for the free aldehyde. The unavailable 2005/2008 main bodies are not promoted to fully inspected paper evidence.

### Acylation order, assembly and regulation limits

scope: supported. Targets: MetaCyc:PWY-8383.

N6-first is preserved as the native database representation while all relevant record claims qualify that 2001 Figure5C leaves the first lysine amide unresolved. The record does not assert a fixed E/F/G/L complex, a fixed number of carrier molecules, a demonstrated MxcL-MxcG assembly, a cellular compartment or regulatory edges. Concentration-dependent product partition in the SI is not treated as proof of a complex.

### Native strain, exact proteins and assay constructs

provenance: supported. Targets: MetaCyc:PWY-8383.

Fresh NCBI AF299336.1 parsing confirms Sg a15/taxon675526 source and all four versioned CDS translations exactly match UniProt Q9F638/Q9F637/Q9F636/Q9F631 lengths543/311/1456/420. UniProt entries remain species-level taxon41 and unreviewed. 2001 chromosomal E/F/G amplification, cleaved initiation residues and residual vector extensions are explicit; 2008 MxcL derives from pCBP-MxcL with His6 tag and does not establish a fully reconstructed native assay construct.

### Component roles and cofactors

evidence: supported. Targets: MetaCyc:PWY-8383.

E enables DHB activation/loading; G enables lysine activation/loading, both condensations and reductive branches; F enables delivery as a carrier, not a separately inferred transferase. MxcF and isolated PCPG gain about340Da after heterologous MtaA coexpression; this does not identify the native Sga15 PPTase or prove full-length G occupancy. Electronic UniProt phosphopantetheine annotations retain their evidence tier. MxcL PLP binding has direct SI spectroscopy, whereas Mg is an assay ingredient without a claimed binding edge. Slower NADH activity stays an alternative assay context, without redefining exact native NADPH reactions.

### Every edge and evidence placement

graph: supported. Targets: MetaCyc:PWY-8383.

All78 edge descriptions/endpoints and239 evidence occurrences were read. The118 distinct source assertions were assessed against exact structured objects or claim-specific primary locations. Fresh selector resolution is recorded separately from this scientific judgment. Membership, chemical usage, enabling, cofactor and continuity statements retain their proper directions and narrow evidence scopes. Rhea20230 is corroboration for the shared DHB adenylation only and does not infer organism-specific enzyme assignment.

### Source authority version correction and preservation

provenance: supported. Targets: MetaCyc:PWY-8383.

Fresh review confirms all21 new source-version strings against actual original MetaCyc database/software footers or UniProt entryAudit. The production selection resolves issue404 while preserving the initial erroneous proposal as historical evidence. All prior manifest/source/ontology entries remain equal to babe44ad;21 source inputs/terms and5 ontology terms are additive. Generic PathwayTools27.0 footers are not asserted as database release27.0 where absent.

### Replay safeguard issue402 disposition

provenance: supported. Targets: MetaCyc:PWY-8383.

The maintained f91 successor is the exact accepted external helper. Preserved independent execution includes a full positive plus five authentic controls: late prior-proof mutation, late projection mutation, pre-import proof mutation, same-bytes symlink relocation and output collision. Their successful rejection supports issue402 correction. These prior executions are attributed, not relabelled as my own fresh runs. Current integrated driver and separately checked production authorities now passed with terminal receipts; original helper scope is unchanged.

### Transcriptomic applicability

scope: not_applicable. Targets: MetaCyc:PWY-8383.

The retained original iModulonDB inventory has20 organism rows and28 datasets, with no applicable Allostigmatella/Stigmatella Sga15 row. This is bounded dataset applicability, not biological absence or negative regulatory evidence. No expression-module membership is promoted to catalysis or pathway membership.

### Whole-record scope and completed final checks

completeness: supported. Targets: MetaCyc:PWY-8383.

Final canonical assessment covers the entire maintained record:9 reactions,27 participants,1 taxon,78edges,239evidence blocks and62references. After final freeze, all80 canonical input bytes and106 adopted proof hashes were rechecked. Terminal whole-corpus gates and graph receipts support current integration. No new actionable finding remains in this record scope.

### Final page/export representation and contribution disclosure

graph: supported. Targets: MetaCyc:PWY-8383.

Current graph receipt preserves both branches, six protein carrier classes, native reverse23314 and21 qualified acylation-order edge descriptions. All78 edges and239 evidence objects remain linked and complete.37SVG nodes exclude the isolated scope taxon that remains among38KGX nodes. Existing whitespace normalization is documented;47 trailing-space trims do not alter evidence. The graph reviewer's prior authority-preparation contribution is disclosed; scientific approval rests on this reviewer's source assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: MetaCyc:PWY-8383. Retain complete native9-member pathway with both A/B branches; precursor DHB supply is a separate native boundary and composite activity summaries are not extra reactions.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/myxochelin-a-and-b-biosynthesis.yaml; entire record; all declared nodes, reactions, edge evidence and references | supports | Exact maintained whole record: 9 reactions, 27 participants, 1 taxon, 78 edges, 239 evidence occurrences and 62 references. |
| fresh-sources | research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-source-check.json; original_responses; evidence_occurrences; native_equations; exact_structure_comparisons; sequence_bridges | supports | This reviewer freshly rehashed all103 response bodies, resolved all239 locators, compared9 native members and46 chemical sides, queried13 exact original ChEBI InChIs and compared4 versioned CDS translations. Selector resolution is distinct from scientific entailment. |
| primary-2001 | https://pmc.ncbi.nlm.nih.gov/articles/PMC58696/; Original PMC58696.html; abstract/introduction, sections sec2-sec6/sec8-sec11; Figure5 original image and caption | supports | Fresh full relevant Methods/Results/Discussion and Figure5 reading: E/F/G reconstitution and A identification, slower NADH alternative, F/isolated-PCPG phosphopantetheinylation, construct processing, unresolved lysine amide order. MxcL/B remains proposed in this paper. |
| primary-2008-si | https://ndownloader.figshare.com/files/4631935; Original ja8025278_si_001.pdf, pages S1-S4, Figures S1-S3; associated DOI:10.1021/ja8025278 | supports | Fresh text and visual reading of all4 SI pages supports His6-MxcL preparation, PLP/PMP spectra, glutamate-containing E/F/G/L assays producing A/B and free-aldehyde MS2/PFBHA methods. This is the supplement, not the unavailable complete main article. |
| native-cds | NCBI:AF299336.1; Original AF299336.1.xml: source strain/taxon and CDS protein_id AAG31128.1/AAG31129.1/AAG31130.1/AAG31135.1 translation qualifiers | supports | Fresh exact translation-to-UniProt comparison gives lengths543/311/1456/420. Original source is Sg a15/taxon675526; UniProt entries are species-level taxon41 and unreviewed. Native bridges do not reconstruct all engineered assay residues. |
| native-database | research/pathway_additions/2026-10-11-next-217/draft/myxochelin-source-manifest.json; 62 references with original whole-body digests and exact source objects; original XML PWY8383 and9 native reactions | supports | Original native objects independently support membership, coefficients, direction and carrier class identities. Current body count is103; the manifest source_access_limits historical66-body sentence is qualified by root acceptance/current fresh audit. Database citations are not treated as quotations from papers. |
| prior-chemistry | research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/source-audit.json; reaction_balances; branch_nets; native_sequence_bridges; exact_native_CHEBI_inchis | supports | Attributed previous independent audit:9 zero atom/charge residuals using symbolic carrier scaffolds, two net equations with carrier cancellation and3 ATP-to-AMP events. Fresh present review confirms exact target/source identity and13 chemical mappings; it does not claim a new whole-database balance run. |
| prior-structures | research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/independent-structures.json; structures CPD25904, A_stereounspecified, CPD25905 and all13 mapped chemicals | supports | Attributed RDKit interpretation of exact original InChIs: native A/B are S; ChEBI31877 has unspecified stereochemistry. B matches7061 structure; contradictory definition prose is excluded. |
| prior-rhea | research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/rhea-independent.json; Rhea142 master20229 forward20230 five side-participant-compound-ChEBI chains | supports | Attributed original RDF chain proof confirms only shared DHB adenylation, including coefficients and direction. No catalyst or Sga15-specific assertion is inferred from Rhea. |
| external-review | research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/whole-record-successor-review.json; whole external target review and explicitly preserved execution evidence | supports | Earlier whole external review assessed the same target hash and helper successor. It is external evidence, not a fabricated canonical predecessor. The prior reviewer later prepared authorities and audited graphs, which are separately attributed. |
| root-source | research/pathway_additions/2026-10-11-next-217/external-evidence/root-acceptance/pathwaymech-myxochelin-root-source-acceptance-20261011.json; fresh original bodies, full issuing SQL digest and immutable archive/proof bindings | supports | Root independently accepted exact final external sources and lineage. Whole database/source proof is reused with attribution; current reviewer freshly checked all103 small responses and selected SQL assertions. |
| current-authority | research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-authority-check.json; all three preservation comparisons; selected_versions | supports | This reviewer independently confirmed all21 new production versions against original footers or entryAudit and preserved all prior manifest/source/ontology entries. Additions:21 sources/terms and5 ontology terms. |
| issue-402 | research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/successor-probes.json; positive, prior-proof, projection, early-prior, symlink and output-collision executions | supports | Exact helper f91 successor passed full positive and rejected five authentic controls. These preserved actual independent executions support correction of issue402; they are not this reviewer's new full replay runs. |
| issue-404 | research/pathway_additions/2026-10-11-next-217/external-evidence/authority-preparation/version-production-disposition.json; selected_entries, reused_entry and original proposal/finding identities | supports | Issue404 correction uses actual MetaCyc database/software footers or UniProt entryAudit for production metadata while preserving the original incorrect proposal. The reused DHB authority and its label ordering remain unchanged. |
| imod-context | research/pathway_additions/2026-10-11-next-217/external-evidence/imodulondb/context.json; datasets, related_inventory_rows, status and limits | context_only | Inspected20-organism/28-dataset inventory has no applicable Allostigmatella/Stigmatella Sga15 dataset. This is bounded applicability, not biological absence, expression evidence or regulation. |
| integrated-replay | research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/positive/integration-replay.json; commands, bound_inputs, helper/target digests and limits | supports | Actual92304/0 terminal325b2d integration ran unchanged source helper plus current identifier/native-schema corpus and explicit target strict checks. All1645 bindings rechecked. Child helper proves historical proposal scope; current production authority metadata is separately checked. |
| integrated-root | research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/root-adoption/pathwaymech-next-217-integrated-replay-root-adoption.json; actual_execution;1533 formal and111 small-source/proof rehashes; limits | supports | Root observed and adopted current terminal integration, read all commands/logs and rehashed formal/small inputs. Driver/child performed complete database hashing; root did not claim another full database pass. |
| full-gates | research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-gate-receipts.json; all7 exact commands, start/finish, exit codes and log digests | supports | Actual full-corpus render, validate, test, lint, identifiers, KGX and tracked whitespace commands exited0; reviewer freshly checked original log digests and terminal summaries. |
| full-gates-root | research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/root-adoption.json; execution28093/0/93010c;422 rechecked inputs;1256 passed/3 skipped | supports | Root terminal observation and final422-input recheck support current full-corpus acceptance. These checks were executed by root; this reviewer inspected the exact receipts and logs. |
| graph | research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/graph-audit-successor.json; records, KGX, representation_checks, exact_KGX_ID_set_delta, reviewer_role and limits | supports | Actual structural audit22020/0/fef01d verified37SVG nodes/38KGX nodes,78 edges/239 evidence blocks, all A/B/source-direction qualifications and prior corpus preservation. It is programmatic; no browser interaction check or scientific approval by graph preparer is claimed. |
| dedup | research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-current-duplicate-check.json; baseline duplicate search and bounded exclusions | supports | Root fresh search on actual babe44ad baseline included ignored, hidden and symlinked content; exact pathway ID/label/slug, AF299336 and defining DOI were not previously represented. This is attributed baseline evidence, not a claim that the now-added record is absent. |
| archive | research/pathway_additions/2026-10-11-next-217/final-proofs-adoption.json; 106 exact preserved proof files and modes | supports | Fresh canonical preparation rehashed all106 final adopted current proofs and all80 inspected canonical inputs. Inert scripts, lossless wrappers and symlink observations preserve original evidence without becoming interchangeable execution manifests. |
| preassessment | research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/scientific-preassessment.json; all12 preparatory assessments, fresh checks and tool limitations | supports | This reviewer's preparatory full scientific reading, source checks and disclosed fallback attempts. Final assessment follows actual canonical inspection at17:26:24Z, after parent freeze; this preparatory record itself is not a canonical completed review. |

## Limits And Additional Notes

- N6-first is a native database convention;2001 Figure5C leaves acylation order unresolved.
- Six carrier-bound states are symbolic protein classes. Balance does not define full polypeptide formulas, fixed complex stoichiometry, channeling or thermodynamic flux.
- Native Sga15 CDS identity is distinct from species-level unreviewed UniProt annotations and historically tagged/processed assay constructs. Exact2008 engineered MxcL residues are not fully reconstructed.
- NADH is a slower observed alternative; native equations retain NADPH. MtaA is heterologous activation, PLP has direct SI support, magnesium is an assay ingredient, and three ATP events are derived accounting.
- Complete2005/2008 main articles were not inspected locally;2008 SI and2001 primary body evidence are explicitly scoped.
- No compartment, regulation, native PPTase, fixed E:F:G:L assembly or iModulon biological-absence conclusion is inferred.
- Previous full SQL/Rhea/RDKit/balance and authentic mutation-control executions are attributed preserved proofs; current reviewer did not duplicate a20GB full replay. Current source/authority selected checks and root terminal integrated/full-corpus receipts were freshly inspected.
- Endpoint digest checks do not exclude arbitrary transient machine-state mutation or attest every installed dependency implementation. Narrow integration boundary controls are not full production mutation replays.
- Programmatic37SVG/38KGX node preservation is not a browser visual or interaction check.
- Working-tree input attestation binds80 final files at available basebabe44ad; it does not assert that those bytes were already committed, merged or published.
- Preparatory scientific reading preceded final input freeze by parent instruction. Actual canonical inspect ran successfully after explicit final freeze at17:26:24Z; final assessment retained unchanged exact bytes and completed receipts.
- Initial local reading fallbacks and input-list preparation typo are retained in preparatory/external execution receipts; none was a record/source defect.
- No maintained target, authority, history, page or dossier changes were made by this reviewer; only the canonical immutable review bundle is saved.
- Issue402 and404 are external GitHub/preintegration lineage, not previous_occurrences or invented saved canonical review identities.
- Initial canonical validator bf18c7/1 rejected an unsaved review ID prefixed with start rather than finished UTC timestamp; the corrected ID uses finished17:28:33Z. No bundle existed or was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T172833Z-myxochelin-a-b-independent-scientific-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of complete myxochelin A and B biosynthesis
started_at: '2026-10-11T17:26:24Z'
finished_at: '2026-10-11T17:28:33.014036Z'
reviewer:
  identity: Codex /root/ed_whole_record_review
  kind: agent
  independence: independent
  independence_basis: No contribution to Myxochelin record/helper authorship, authority
    preparation, integration, history or rendering. I performed fresh source interpretation
    and current selected-source/authority checks. Earlier external review, source
    balance/RDKit/Rhea proofs, root integration/gates and contributor graph audit
    are reused only with explicit attribution. Root integrated maintained changes;
    /root/pathway_authority_cache previously reviewed then prepared authorities/copy
    plan and audited graphs; /root/pyochelin_packaging_successor prepared integration
    proof packaging. Their artifacts do not self-approve this scientific judgment.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: Complete nine-reaction native record with both product branches supported
  within explicitly qualified biochemical, construct and source-access limits.
scientific_review: true
summary: The entire maintained Myxochelin A/B record is supported within its stated
  scope. All9 native reactions,78 edges,239 evidence occurrences and62 references
  were assessed against original structured objects and inspected primary evidence.
  Fresh current checks confirm native directions, structures, sequence bridges and
  production source versions; current full-corpus gates and graph preservation passed.
  No new actionable finding. Historical issues402/404 have evidence-backed fixes and
  are described as external lineage, without fabricated canonical predecessors.
source:
  git_revision: babe44ad1992d2950701e432f400965631d538a7
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
  - path: conf/identifier_sources.json
    sha256: d3af218f3256620c8c8138505bd81652323bac2e9b0d9159a0279a575da72476
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 98851d38c6f2b81dc166054815f42784b84cbbfd1d42a54b8353402e8b6c1e02
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 842f5f41d3a9f9bb92972b069f1916b17303f2c65e119556fa50991ced6bc070
    role: context
  - path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    sha256: 5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2
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
  - path: docs/IDENTIFIERS.md
    sha256: 543bbaf6a79fa164ab18d45b110741b4c8c96141c8e72f395e5ac5ff06bc1da4
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
  - path: pages/records/MetaCyc_PWY-8383.html
    sha256: c8d82a43ded4ce8f61a8073eea61df644deb0037e1ef9e3496d772b849753805
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/README.md
    sha256: bc540a2d971ce4c0db5e20c71d559d8adffcd84caafe581cf0d7683a95015791
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/dossier-adoption.json
    sha256: 7c04e9b4fe012f9c77791fea312f86516dd02e95cfb1338b066a86006bee25f6
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/draft/myxochelin-authority-integration-dispositions.json
    sha256: 94c837203ebfd2456369811217c613255f31b960fdeb7249d3277f3cf82fb523
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/draft/myxochelin-authority-proposal.json
    sha256: eb904a6505c7f20f3773282ebee278848558a351b5838c3aa752127187e6d235
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/draft/myxochelin-source-manifest.json
    sha256: 5d660f2c023a4120a093bf6ff02d85f3208049d8f986a61543cfd7569e515fa2
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/draft/myxochelin-source-projection.json
    sha256: d27edc38af264315b38f0efa5a07938a2a04a6e65bdfe8d6915045e2defc85b5
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/authority-preparation/selected/selection.json
    sha256: a19a6d8f69bb10c12083ab2b1b0b006aae948ba824ba58889008cab05682e346
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/authority-preparation/version-attribution-finding.json
    sha256: 3ca4897abe4d49313f4d27c6241e2b5a12b71f30da647e7d21d182647355d0c4
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/authority-preparation/version-production-disposition.json
    sha256: e54719c7cf56575b7b8afdf2d320345e7a4f31ae17eb5ee658a54a1b1ca77aac
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-diff-tracked.log.json
    sha256: 20727fb46b877d807227b2eb0b7668c8b543361419872c9b43e39f610d63cdcd
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-gate-inputs.json
    sha256: b1448b7e2b640a46e78a5a4dcfd99474414513c9010880891d84f54f9fbe925c
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-gate-receipts.json
    sha256: d4bbaadcb8d5134778dd261941bdc653fe28beb65aa95f51e27cd3b16ff0c17e
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-gates.py.txt
    sha256: 5ad66f6c21f9179f007f1eee3b5574fcf5db66f46a35edaa1cd4447c4bdebdf6
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-identifiers.log.json
    sha256: 7ba10980ab33d244891427159022d3baa74a3533301adf725f14b9ee127067e2
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-kgx.log.json
    sha256: ada913b24574714bce1fa68da3fff72309cdb58515c45d7127866cbf05589902
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-lint.log.json
    sha256: 1e5d8f15c6790a86c2a5c6f942e70a8dbed280bb737e1e9c340ec61298c3428a
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-render.log.json
    sha256: fa243016b420900a75c42d01d34eca373fbf143a2eaaf9f06f7cb6e4d7e91d4d
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-test.log.json
    sha256: ed632a50fd6317144dbb8ce9367a17d263ec059db0d17b37faa77d7429f163ba
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-validate.log.json
    sha256: 83902b6e07231075713908c798847d7fb2623fee79cec1018f5167e5e57deda2
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-seal-final-gates.py.txt
    sha256: 70d6d8393d9787d548d22ab25f3b4aa0688dab438defe0c22a09d5c2449e73dd
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/root-adoption.json
    sha256: 1b2dbe37984043a2d401e4507897c9c211a77c9f9ac83292a87dee5b0d74ff35
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/audit-harness-correction.json
    sha256: d168b4e56e396d7bdfe8ffa3189e0c2360886815f92a001d5eb847cc55e6c9bb
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/completion.json
    sha256: 6028c1af6a63cd9179c5db2478aa5f73501f21d113d84eb70c3416943f8a3d14
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/graph-audit-successor.json
    sha256: 76f4333aed3a712042adc2cb7ef67d689ff6cf323fd43986d69595a03bb3fea1
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/graph-audit-successor.py.txt
    sha256: 5fe0b7cf164f59d056d8eaef166a34172fc8adb8be8f37d2d857903ab98e9522
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/summary.md
    sha256: 28b3e48b99787ec372ebbc9560ab765b62da84479436a8bca39900fb470518f3
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-authority-check.json
    sha256: b40d3b4425dd6d9c421abdbf5bf1e29b00c8db82652d42570e8b5fcf6a4e1601
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-source-check.json
    sha256: ca8342f7e330208428f6c3454149fcf4e65a42e818d826ce880c8a722c9bed2e
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-source-check.py.txt
    sha256: 3b357665903d6fd695b4ccb3edb96a1c05ddacfed81a83e756d081a9320f2ec3
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/preassessment-handoff.json
    sha256: 58fa3dd7f1bf8aebb018881f8cb053781025eccea3d18e69f35776329d66e802
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/scientific-preassessment.json
    sha256: 4991e5b3c960b31be026f86f20c013f80cde12c4c4f46236945de0d61cf310ac
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/imodulondb/context.json
    sha256: de9955026b23f4d9a6623bdb0d6e3ff73dad6fbc3de46eed62a9942d7e360d7c
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/imodulondb/manifest.json
    sha256: 6898bab91f11fbda7fec316a5ba682f6705a15caa1d82b65f2e2739fc731786f
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/finding.json
    sha256: c2699b3573c66bee9aac69c27e3ce162fa6b0eb7bb6ca76855376d2880c8e8ad
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/independent-structures.json
    sha256: fae67872dc341273cd05d7aaaf8abc5644ae80720eaf895c4c92a586f9b5878c
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/rhea-independent.json
    sha256: d7f1cbe1ce96f342cf0b45fac8bbeed9b6330ebf2321ed15bcc34acb165726c4
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/source-audit.json
    sha256: 2f2fecfe8520394740645d959d4ac5ccce91530f718d2dadade80e7d051b859f
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/successor-probes.json
    sha256: 51a2a9ace17fe2041a69603e6e438e07f75970c1066d137a839bcb93bd7c6205
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/whole-record-successor-review.json
    sha256: ee779267e2b2a1d3c550accdde4c26a0e28c702dd40cd433ef01db23c8541ecf
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/positive/integration-replay.json
    sha256: 453b8abcfd0c7336582465fa2cacc68b510ee5db91aa70da13c6c83e1a2b5b89
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/positive/source-replay.json
    sha256: 5b5a65d2fe88d4c2d2e4919faa37cfef1c4cbd5c5b3233d79404c03544a16778
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/preparation/README.md
    sha256: 745bae020900b584886a01958736997bb0443805eda253deb400dcf266f9b288
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/preparation/completion.json
    sha256: e0ba32df7b6b2ee56f3eb3ec5ec9a56d4136f983eefb2fdf9da63a7b0439976d
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/preparation/expected-bindings.json
    sha256: 39b94e1fe4285bb26704a4809569010320b7325b896425463d42a84a9c6c9c17
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/preparation/integration-replay.py.txt
    sha256: 0ef1dd3bea13d2e9d4f69a3a4090e74d75990bd97f90794a72090280e634c8ab
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/root-adoption/pathwaymech-next-217-integrated-replay-root-adoption.json
    sha256: d6234731d992709a8fc33f50542f5927079ccc733614e9c0b411761cf4c9e9d8
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/root-driver-review.json
    sha256: 50bc16fb16b97586df8c7dada377b80b5ff844aaefa42f9502fda030a298c667
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-acceptance/pathwaymech-myxochelin-root-source-acceptance-20261011.json
    sha256: 54075502678a75d09b2e486296a243a9a0fd51b01cb3e45d00b0381aa6943a80
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-adopt-record-authorities.py.txt
    sha256: cf1528fb8f575030bc4c1bc6a2872ba1708592367b8483c0d42497a1f25812f2
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-authority-root-review.json
    sha256: 2d3fd54c7f707b33e6e780f734c82e3813a6373d93f65c1b7cc4471408d27b51
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-authority-root-review.py.txt
    sha256: 30a01a3f824f1a64ed96e6d96b2de55ce8f3871e7ac2dc44513b366c03e970b6
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-core-adoption.json
    sha256: c9e1a1c00aab4a149699909932a92a9459552d21b7ffc1755d1abeec4cc3dfdf
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-current-duplicate-check.json
    sha256: 2f25b8fd5ca5833c0675ca8df1e584aa9b748ae0b20427f3060b30618eaa71ed
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-merged-baseline-bridge.json
    sha256: 4d2962dc51d93da8a347e0f705ceacb5904a73bfc97afed64491d531401530ed
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/final-proofs-adoption.json
    sha256: bfb6c3b75c706e913ccac53c44ba986e65a179f419a9754dab6d9a2dc0b984c7
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/myxochelin-replay-successor.py
    sha256: f91bb984deb34364e794cc2f83b4fcdff6ba53567df066f4af55a123e96cf1ad
    role: context
  - path: research/pathway_additions/2026-10-11-next-217/rhea-crosscheck.json
    sha256: c132793814972f5a0c4ecc7bf9d07b11341c2adf9e3e80becc862b189abc3086
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/pathwaymech/graph_view.py
    sha256: 3f133d2251dd965a4152cdc91b9169e75776c3615bd80c7a5a679abe27e4f86a
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: b2725526a658aa3d54e2ac3398fd499b71f0081ae2b3ed18c84f5872ee6f1af4
    role: context
  - path: src/pathwaymech/schema.py
    sha256: e81f95da70943090d470b1837d248fec2a592c5f4b53fc6587bc4214adbf35f3
    role: context
  - path: src/pathwaymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 5e4a0bcb5b4901b603e9e0e89ce8b2172efbd8fcbe5e68cac7283555c6a1c056
    role: context
scope:
  description: Whole-record scientific review of the complete maintained MetaCyc:PWY-8383
    record and exact local context/proof inputs after final integration freeze.
  selection: The single explicitly assigned maintained myxochelin-a-and-b-biosynthesis.yaml,
    unchanged target SHA5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-8383
  exclusions:
  - target: Whole pathway corpus scientific validity
    reason: 218-record deterministic gates and baseline preservation do not constitute
      scientific re-review of all records.
  - target: 2005/2008 complete main article bodies and exact engineered MxcL sequence
    reason: Locally unavailable/incompletely reconstructable; only inspected2001 full
      relevant body and2008 complete supporting information support attributed claims.
  - target: Browser visual/interactivity acceptance
    reason: Graph verification is programmatic SVG/KGX with explicitly disclosed scope.
targets:
- target_id: MetaCyc:PWY-8383
  path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
  label: myxochelin A and B biosynthesis
  record_class: PathwayRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
    role: maintained pathway identity, scientific scope and mechanistic evidence
  ownership_note: Generated pages and KGX are contextual artifacts owned by the maintained
    YAML and renderer; this review authorizes no record, history or generated artifact
    changes.
checks:
- check_id: gate-render
  name: render
  status: passed
  required: true
  summary: Rendered218 records.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: just render-pages
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: gate-validate
  name: validate
  status: passed
  required: true
  summary: Current full corpus validation passed, including schema, history, identifiers,
    evidence and page currency.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: just validate
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: gate-test
  name: test
  status: passed
  required: true
  summary: 1256 tests passed;3 skipped;3 warnings.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: just test
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: gate-lint
  name: lint
  status: passed
  required: true
  summary: All lint checks passed.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: just lint
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: gate-identifiers
  name: identifiers
  status: passed
  required: true
  summary: 218 records passed authority identity/label checks.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: just check-identifiers
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: gate-kgx
  name: kgx
  status: passed
  required: true
  summary: Separate KGX export from218 records completed.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: just kgx-export --output-dir /private/tmp/pathwaymech-next-217-final-kgx
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: gate-diff-tracked
  name: diff-tracked
  status: passed
  required: true
  summary: Tracked whitespace check passed.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - full-gates
  - full-gates-root
  command: git diff --check
  scope_note: Root execution in current worktree; exact terminal receipts/logs inspected,
    not rerun or claimed as reviewer-owned execution.
- check_id: fresh-originals
  name: Current reviewer original-source audit
  status: passed
  required: true
  summary: 103 response digests,239 locators,9members,46sides,13 exact selected InChIs
    and4 CDS bridges passed.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - fresh-sources
  command: PYTHONPATH=src /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python
    /private/tmp/pathwaymech-next-217-independent-scientific-review/fresh-source-check.py
  scope_note: Actual reviewer command badc81/0 before freeze; exact target and authority/source
    inputs remain unchanged at final inspection. Whole database hash and scientific
    entailment are separate.
- check_id: authority-preservation
  name: Current reviewer authority/metadata audit
  status: passed
  required: true
  summary: All prior entries preserved and all21 corrected source versions match original
    bodies.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - current-authority
  - issue-404
  scope_note: Actual reviewer inline Python948195/0; fresh git-show baseline comparisons
    and selected original source fields.
- check_id: integration
  name: Current integrated source/runtime checks
  status: passed
  required: true
  summary: All4 child checks and1645 endpoint bindings passed.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - integrated-replay
  - integrated-root
  scope_note: Root-observed92304/0 execution; original helper proposal and current
    authority checks remain distinct. Driver boundary controls are narrow real-function
    fixture checks, not full mutation replays.
- check_id: graph-artifacts
  name: Generated SVG and KGX preservation
  status: passed
  required: true
  summary: 37SVG/38KGX nodes,78 edges,239 evidence objects and prior corpus preservation
    passed.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - graph
  scope_note: Attributed actual22020/0/fef01d structural audit. The auditor contributed
    prior authority preparation; this reviewer makes independent scientific assessment.
    No browser visual claim.
- check_id: staged-whitespace
  name: Complete staged whitespace check
  status: passed
  required: true
  summary: Complete staged change set passed git diff --cached --check.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - record
  - archive
  command: git diff --cached --check
  scope_note: Actual current reviewer execution14322b/0 after final freeze.
- check_id: canonical-input-inspection
  name: Canonical input capture
  status: passed
  required: true
  summary: Actual inspect captured80 final input files and exact working-tree target
    at basebabe44ad.
  target_ids:
  - MetaCyc:PWY-8383
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - archive
  - record
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python scripts/record_review.py
    inspect --targets /private/tmp/pathwaymech-next-217-independent-scientific-review/targets.json
    [79 explicit --input arguments]
  scope_note: Actualbaf15a/0; exact full argv/receipts retained externally. All80
    bytes archived and rechecked51d56a/0 before final assessment. Initial input-list
    typo failed before inspect and was corrected using ignored-inclusive file inventory.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/myxochelin-a-and-b-biosynthesis.yaml
  locator: entire record; all declared nodes, reactions, edge evidence and references
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: 'Exact maintained whole record: 9 reactions, 27 participants, 1 taxon,
    78 edges, 239 evidence occurrences and 62 references.'
  snapshot_sha256: 5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2
- evidence_id: fresh-sources
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-source-check.json
  locator: original_responses; evidence_occurrences; native_equations; exact_structure_comparisons;
    sequence_bridges
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: This reviewer freshly rehashed all103 response bodies, resolved all239
    locators, compared9 native members and46 chemical sides, queried13 exact original
    ChEBI InChIs and compared4 versioned CDS translations. Selector resolution is
    distinct from scientific entailment.
  snapshot_sha256: ca8342f7e330208428f6c3454149fcf4e65a42e818d826ce880c8a722c9bed2e
- evidence_id: primary-2001
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC58696/
  locator: Original PMC58696.html; abstract/introduction, sections sec2-sec6/sec8-sec11;
    Figure5 original image and caption
  accessed_at: '2026-10-11T17:16:57Z'
  support: supports
  summary: 'Fresh full relevant Methods/Results/Discussion and Figure5 reading: E/F/G
    reconstitution and A identification, slower NADH alternative, F/isolated-PCPG
    phosphopantetheinylation, construct processing, unresolved lysine amide order.
    MxcL/B remains proposed in this paper.'
  snapshot_sha256: bb6c753d74cc5d2461d994162ae1c9b65710dc912cda322b50f801b64c8821e2
- evidence_id: primary-2008-si
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/4631935
  locator: Original ja8025278_si_001.pdf, pages S1-S4, Figures S1-S3; associated DOI:10.1021/ja8025278
  accessed_at: '2026-10-11T17:16:57Z'
  support: supports
  summary: Fresh text and visual reading of all4 SI pages supports His6-MxcL preparation,
    PLP/PMP spectra, glutamate-containing E/F/G/L assays producing A/B and free-aldehyde
    MS2/PFBHA methods. This is the supplement, not the unavailable complete main article.
  snapshot_sha256: 3e242f7d232af6b285fc1bc7b4d97cda4b85a03714332a50437e55917c9238fd
- evidence_id: native-cds
  kind: database
  reference: NCBI:AF299336.1
  locator: 'Original AF299336.1.xml: source strain/taxon and CDS protein_id AAG31128.1/AAG31129.1/AAG31130.1/AAG31135.1
    translation qualifiers'
  accessed_at: '2026-10-11T17:16:57Z'
  support: supports
  summary: Fresh exact translation-to-UniProt comparison gives lengths543/311/1456/420.
    Original source is Sg a15/taxon675526; UniProt entries are species-level taxon41
    and unreviewed. Native bridges do not reconstruct all engineered assay residues.
  snapshot_sha256: e9ef9bc9825dda8aa6e027cc381faf09a287571ebdff2f582a143a7797226ed6
- evidence_id: native-database
  kind: database
  reference: research/pathway_additions/2026-10-11-next-217/draft/myxochelin-source-manifest.json
  locator: 62 references with original whole-body digests and exact source objects;
    original XML PWY8383 and9 native reactions
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Original native objects independently support membership, coefficients,
    direction and carrier class identities. Current body count is103; the manifest
    source_access_limits historical66-body sentence is qualified by root acceptance/current
    fresh audit. Database citations are not treated as quotations from papers.
  snapshot_sha256: 5d660f2c023a4120a093bf6ff02d85f3208049d8f986a61543cfd7569e515fa2
- evidence_id: prior-chemistry
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/source-audit.json
  locator: reaction_balances; branch_nets; native_sequence_bridges; exact_native_CHEBI_inchis
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Attributed previous independent audit:9 zero atom/charge residuals using
    symbolic carrier scaffolds, two net equations with carrier cancellation and3 ATP-to-AMP
    events. Fresh present review confirms exact target/source identity and13 chemical
    mappings; it does not claim a new whole-database balance run.
  snapshot_sha256: 2f2fecfe8520394740645d959d4ac5ccce91530f718d2dadade80e7d051b859f
- evidence_id: prior-structures
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/independent-structures.json
  locator: structures CPD25904, A_stereounspecified, CPD25905 and all13 mapped chemicals
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: 'Attributed RDKit interpretation of exact original InChIs: native A/B are
    S; ChEBI31877 has unspecified stereochemistry. B matches7061 structure; contradictory
    definition prose is excluded.'
  snapshot_sha256: fae67872dc341273cd05d7aaaf8abc5644ae80720eaf895c4c92a586f9b5878c
- evidence_id: prior-rhea
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/rhea-independent.json
  locator: Rhea142 master20229 forward20230 five side-participant-compound-ChEBI chains
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Attributed original RDF chain proof confirms only shared DHB adenylation,
    including coefficients and direction. No catalyst or Sga15-specific assertion
    is inferred from Rhea.
  snapshot_sha256: d7f1cbe1ce96f342cf0b45fac8bbeed9b6330ebf2321ed15bcc34acb165726c4
- evidence_id: external-review
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/whole-record-successor-review.json
  locator: whole external target review and explicitly preserved execution evidence
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Earlier whole external review assessed the same target hash and helper
    successor. It is external evidence, not a fabricated canonical predecessor. The
    prior reviewer later prepared authorities and audited graphs, which are separately
    attributed.
  snapshot_sha256: ee779267e2b2a1d3c550accdde4c26a0e28c702dd40cd433ef01db23c8541ecf
- evidence_id: root-source
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/root-acceptance/pathwaymech-myxochelin-root-source-acceptance-20261011.json
  locator: fresh original bodies, full issuing SQL digest and immutable archive/proof
    bindings
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Root independently accepted exact final external sources and lineage. Whole
    database/source proof is reused with attribution; current reviewer freshly checked
    all103 small responses and selected SQL assertions.
  snapshot_sha256: 54075502678a75d09b2e486296a243a9a0fd51b01cb3e45d00b0381aa6943a80
- evidence_id: current-authority
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/fresh-authority-check.json
  locator: all three preservation comparisons; selected_versions
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: This reviewer independently confirmed all21 new production versions against
    original footers or entryAudit and preserved all prior manifest/source/ontology
    entries. Additions:21 sources/terms and5 ontology terms.
  snapshot_sha256: b40d3b4425dd6d9c421abdbf5bf1e29b00c8db82652d42570e8b5fcf6a4e1601
- evidence_id: issue-402
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/independent-review/successor-probes.json
  locator: positive, prior-proof, projection, early-prior, symlink and output-collision
    executions
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Exact helper f91 successor passed full positive and rejected five authentic
    controls. These preserved actual independent executions support correction of
    issue402; they are not this reviewer's new full replay runs.
  snapshot_sha256: 51a2a9ace17fe2041a69603e6e438e07f75970c1066d137a839bcb93bd7c6205
- evidence_id: issue-404
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/authority-preparation/version-production-disposition.json
  locator: selected_entries, reused_entry and original proposal/finding identities
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Issue404 correction uses actual MetaCyc database/software footers or UniProt
    entryAudit for production metadata while preserving the original incorrect proposal.
    The reused DHB authority and its label ordering remain unchanged.
  snapshot_sha256: e54719c7cf56575b7b8afdf2d320345e7a4f31ae17eb5ee658a54a1b1ca77aac
- evidence_id: imod-context
  kind: search
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/imodulondb/context.json
  locator: datasets, related_inventory_rows, status and limits
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: context_only
  summary: Inspected20-organism/28-dataset inventory has no applicable Allostigmatella/Stigmatella
    Sga15 dataset. This is bounded applicability, not biological absence, expression
    evidence or regulation.
  snapshot_sha256: de9955026b23f4d9a6623bdb0d6e3ff73dad6fbc3de46eed62a9942d7e360d7c
  search_scope: Original iModulonDB /api/datasets body and structured adapter inventory
    on2026-10-11; exact target species/strain and historical genus considered. No
    applicable dataset, so no gene/component query is claimed. This is an external
    inventory search, not a repository-file absence claim.
- evidence_id: integrated-replay
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/positive/integration-replay.json
  locator: commands, bound_inputs, helper/target digests and limits
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Actual92304/0 terminal325b2d integration ran unchanged source helper plus
    current identifier/native-schema corpus and explicit target strict checks. All1645
    bindings rechecked. Child helper proves historical proposal scope; current production
    authority metadata is separately checked.
  snapshot_sha256: 453b8abcfd0c7336582465fa2cacc68b510ee5db91aa70da13c6c83e1a2b5b89
- evidence_id: integrated-root
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/integrated-replay/root-adoption/pathwaymech-next-217-integrated-replay-root-adoption.json
  locator: actual_execution;1533 formal and111 small-source/proof rehashes; limits
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Root observed and adopted current terminal integration, read all commands/logs
    and rehashed formal/small inputs. Driver/child performed complete database hashing;
    root did not claim another full database pass.
  snapshot_sha256: d6234731d992709a8fc33f50542f5927079ccc733614e9c0b411761cf4c9e9d8
- evidence_id: full-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/pathwaymech-next-217-final-gate-receipts.json
  locator: all7 exact commands, start/finish, exit codes and log digests
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Actual full-corpus render, validate, test, lint, identifiers, KGX and tracked
    whitespace commands exited0; reviewer freshly checked original log digests and
    terminal summaries.
  snapshot_sha256: d4bbaadcb8d5134778dd261941bdc653fe28beb65aa95f51e27cd3b16ff0c17e
- evidence_id: full-gates-root
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/current-full-gates/root-adoption.json
  locator: execution28093/0/93010c;422 rechecked inputs;1256 passed/3 skipped
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Root terminal observation and final422-input recheck support current full-corpus
    acceptance. These checks were executed by root; this reviewer inspected the exact
    receipts and logs.
  snapshot_sha256: 1b2dbe37984043a2d401e4507897c9c211a77c9f9ac83292a87dee5b0d74ff35
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/current-graph-review/graph-audit-successor.json
  locator: records, KGX, representation_checks, exact_KGX_ID_set_delta, reviewer_role
    and limits
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Actual structural audit22020/0/fef01d verified37SVG nodes/38KGX nodes,78
    edges/239 evidence blocks, all A/B/source-direction qualifications and prior corpus
    preservation. It is programmatic; no browser interaction check or scientific approval
    by graph preparer is claimed.
  snapshot_sha256: 76f4333aed3a712042adc2cb7ef67d689ff6cf323fd43986d69595a03bb3fea1
- evidence_id: dedup
  kind: search
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/root-integration/pathwaymech-next-217-current-duplicate-check.json
  locator: baseline duplicate search and bounded exclusions
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Root fresh search on actual babe44ad baseline included ignored, hidden
    and symlinked content; exact pathway ID/label/slug, AF299336 and defining DOI
    were not previously represented. This is attributed baseline evidence, not a claim
    that the now-added record is absent.
  snapshot_sha256: 2f25b8fd5ca5833c0675ca8df1e584aa9b748ae0b20427f3060b30618eaa71ed
  search_scope: Whole actual merged baseline using rg-uu/hidden/follow; only Git and
    dependency trees excluded. Current target is the single maintained addition; previous
    external candidate references are historical.
- evidence_id: archive
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-217/final-proofs-adoption.json
  locator: 106 exact preserved proof files and modes
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: Fresh canonical preparation rehashed all106 final adopted current proofs
    and all80 inspected canonical inputs. Inert scripts, lossless wrappers and symlink
    observations preserve original evidence without becoming interchangeable execution
    manifests.
  snapshot_sha256: bfb6c3b75c706e913ccac53c44ba986e65a179f419a9754dab6d9a2dc0b984c7
- evidence_id: preassessment
  kind: prior_review
  reference: research/pathway_additions/2026-10-11-next-217/external-evidence/current-scientific-preassessment/scientific-preassessment.json
  locator: all12 preparatory assessments, fresh checks and tool limitations
  accessed_at: '2026-10-11T17:28:33.014036Z'
  support: supports
  summary: This reviewer's preparatory full scientific reading, source checks and
    disclosed fallback attempts. Final assessment follows actual canonical inspection
    at17:26:24Z, after parent freeze; this preparatory record itself is not a canonical
    completed review.
  snapshot_sha256: 4991e5b3c960b31be026f86f20c013f80cde12c4c4f46236945de0d61cf310ac
assessments:
- assessment_id: assessment-01
  area: identity
  topic: Exact native pathway and supplied precursor boundary
  outcome: supported
  summary: The record denotes MetaCyc:PWY-8383 with all nine native reaction objects
    and both myxochelin product branches. PWY-5901 precursor supply remains separate.
    Composite RXN-23309/RXN-23311 are explanatory enzyme activities rather than additional
    pathway steps.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - record
  - fresh-sources
  - native-database
- assessment_id: assessment-02
  area: grounding
  topic: Chemical identities, direction and carrier classes
  outcome: supported
  summary: Fresh original XML-to-YAML comparison confirms 46 chemical sides and native
    physiological right-to-left RXN-23314. Thirteen small-molecule native InChIs match
    selected original ChEBI SQL assertions exactly. Native myxochelin A has a specified
    stereocenter absent from CHEBI:31877 and retains its narrower MetaCyc ID. B matches
    CHEBI:7061 by exact structure, without adopting contradictory prose. Six carrier
    states are native Protein classes and are not misrepresented as free metabolites
    or fully formulated polypeptides.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - fresh-sources
  - prior-structures
  - native-database
- assessment_id: assessment-03
  area: quantity
  topic: Derived material balance
  outcome: supported
  summary: The preserved independently reviewed source audit reports zero elemental/charge
    residual for all nine reactions using explicitly symbolic carrier scaffolds, and
    carrier cancellation for both product nets. Each product requires two DHB activation/loading
    cycles and one lysine activation, hence three ATP-to-AMP events; A uses two NADPH,
    B uses one NADPH plus glutamate. These are derived stoichiometric accounting results,
    not measured yields, whole-protein formulas or energetics.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - prior-chemistry
  - integrated-replay
- assessment_id: assessment-04
  area: evidence
  topic: Primary reconstitution and branch evidence
  outcome: supported
  summary: Fresh reading of the complete relevant 2001 Methods/Results/Discussion
    and Figure 5 supports E/F/G reconstitution, lysine activation/loading, two condensations,
    and reductive release. That paper directly identifies A; MxcL/B was proposed there.
    Fresh reading of all four 2008 SI pages supplies His6-MxcL/PLP spectra, E/F/G/L
    reconstitution producing A and B, and MS2/PFBHA methods for the free aldehyde.
    The unavailable 2005/2008 main bodies are not promoted to fully inspected paper
    evidence.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - primary-2001
  - primary-2008-si
- assessment_id: assessment-05
  area: scope
  topic: Acylation order, assembly and regulation limits
  outcome: supported
  summary: N6-first is preserved as the native database representation while all relevant
    record claims qualify that 2001 Figure5C leaves the first lysine amide unresolved.
    The record does not assert a fixed E/F/G/L complex, a fixed number of carrier
    molecules, a demonstrated MxcL-MxcG assembly, a cellular compartment or regulatory
    edges. Concentration-dependent product partition in the SI is not treated as proof
    of a complex.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - primary-2001
  - primary-2008-si
  - record
- assessment_id: assessment-06
  area: provenance
  topic: Native strain, exact proteins and assay constructs
  outcome: supported
  summary: Fresh NCBI AF299336.1 parsing confirms Sg a15/taxon675526 source and all
    four versioned CDS translations exactly match UniProt Q9F638/Q9F637/Q9F636/Q9F631
    lengths543/311/1456/420. UniProt entries remain species-level taxon41 and unreviewed.
    2001 chromosomal E/F/G amplification, cleaved initiation residues and residual
    vector extensions are explicit; 2008 MxcL derives from pCBP-MxcL with His6 tag
    and does not establish a fully reconstructed native assay construct.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - native-cds
  - fresh-sources
  - primary-2001
  - primary-2008-si
  dimensions:
  - name: strain_scope
    value: NCBITaxon:675526 Allostigmatella aurantiaca Sg a15; historical Stigmatella
      aurantiaca Sg a15
    definition: Native DNA/protein source scope; current unreviewed UniProt organism41
      is a species-level entry.
    evidence_ids:
    - native-cds
    - fresh-sources
  - name: construct_scope
    value: 2001 recombinant E/F/G with processing/extensions;2008 His6-MxcL frompCBP-MxcL
    definition: Assayed constructs are not asserted to be exact unmodified native
      chains.
    evidence_ids:
    - primary-2001
    - primary-2008-si
- assessment_id: assessment-07
  area: evidence
  topic: Component roles and cofactors
  outcome: supported
  summary: E enables DHB activation/loading; G enables lysine activation/loading,
    both condensations and reductive branches; F enables delivery as a carrier, not
    a separately inferred transferase. MxcF and isolated PCPG gain about340Da after
    heterologous MtaA coexpression; this does not identify the native Sga15 PPTase
    or prove full-length G occupancy. Electronic UniProt phosphopantetheine annotations
    retain their evidence tier. MxcL PLP binding has direct SI spectroscopy, whereas
    Mg is an assay ingredient without a claimed binding edge. Slower NADH activity
    stays an alternative assay context, without redefining exact native NADPH reactions.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - primary-2001
  - primary-2008-si
  - fresh-sources
  dimensions:
  - name: evidence_tier
    value: Primary reconstitution/PLP spectra; separate ECO:0000256 electronic cofactor
      annotations
    definition: Direct biochemical observations remain distinct from computational
      annotation.
    evidence_ids:
    - primary-2001
    - primary-2008-si
    - fresh-sources
  - name: component_role
    value: MxcF carrier delivery; MxcE/MxcG/MxcL enzyme activity; symbolic carrier-bound
      states
    definition: Carrier enabling is not asserted to be independent condensation catalysis.
    evidence_ids:
    - record
    - primary-2001
- assessment_id: assessment-08
  area: graph
  topic: Every edge and evidence placement
  outcome: supported
  summary: All78 edge descriptions/endpoints and239 evidence occurrences were read.
    The118 distinct source assertions were assessed against exact structured objects
    or claim-specific primary locations. Fresh selector resolution is recorded separately
    from this scientific judgment. Membership, chemical usage, enabling, cofactor
    and continuity statements retain their proper directions and narrow evidence scopes.
    Rhea20230 is corroboration for the shared DHB adenylation only and does not infer
    organism-specific enzyme assignment.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - record
  - fresh-sources
  - native-database
  - primary-2001
  - primary-2008-si
  - prior-rhea
- assessment_id: assessment-09
  area: provenance
  topic: Source authority version correction and preservation
  outcome: supported
  summary: Fresh review confirms all21 new source-version strings against actual original
    MetaCyc database/software footers or UniProt entryAudit. The production selection
    resolves issue404 while preserving the initial erroneous proposal as historical
    evidence. All prior manifest/source/ontology entries remain equal to babe44ad;21
    source inputs/terms and5 ontology terms are additive. Generic PathwayTools27.0
    footers are not asserted as database release27.0 where absent.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - current-authority
  - issue-404
- assessment_id: assessment-10
  area: provenance
  topic: Replay safeguard issue402 disposition
  outcome: supported
  summary: 'The maintained f91 successor is the exact accepted external helper. Preserved
    independent execution includes a full positive plus five authentic controls: late
    prior-proof mutation, late projection mutation, pre-import proof mutation, same-bytes
    symlink relocation and output collision. Their successful rejection supports issue402
    correction. These prior executions are attributed, not relabelled as my own fresh
    runs. Current integrated driver and separately checked production authorities
    now passed with terminal receipts; original helper scope is unchanged.'
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - issue-402
  - integrated-replay
  - integrated-root
- assessment_id: assessment-11
  area: scope
  topic: Transcriptomic applicability
  outcome: not_applicable
  summary: The retained original iModulonDB inventory has20 organism rows and28 datasets,
    with no applicable Allostigmatella/Stigmatella Sga15 row. This is bounded dataset
    applicability, not biological absence or negative regulatory evidence. No expression-module
    membership is promoted to catalysis or pathway membership.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - imod-context
- assessment_id: assessment-12
  area: completeness
  topic: Whole-record scope and completed final checks
  outcome: supported
  summary: Final canonical assessment covers the entire maintained record:9 reactions,27
    participants,1 taxon,78edges,239evidence blocks and62references. After final freeze,
    all80 canonical input bytes and106 adopted proof hashes were rechecked. Terminal
    whole-corpus gates and graph receipts support current integration. No new actionable
    finding remains in this record scope.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - full-gates
  - full-gates-root
  - graph
  - record
  - preassessment
  metrics:
  - name: Native reactions assessed
    value: 9
    unit: reaction objects
    definition: Complete PWY8383 native membership, both branches.
    denominator: 9
  - name: Edge evidence occurrences assessed
    value: 239
    unit: evidence occurrences
    definition: Whole record claim-specific review,118 distinct assertions reused
      across239 occurrences.
    denominator: 239
- assessment_id: assessment-13
  area: graph
  topic: Final page/export representation and contribution disclosure
  outcome: supported
  summary: Current graph receipt preserves both branches, six protein carrier classes,
    native reverse23314 and21 qualified acylation-order edge descriptions. All78 edges
    and239 evidence objects remain linked and complete.37SVG nodes exclude the isolated
    scope taxon that remains among38KGX nodes. Existing whitespace normalization is
    documented;47 trailing-space trims do not alter evidence. The graph reviewer's
    prior authority-preparation contribution is disclosed; scientific approval rests
    on this reviewer's source assessment.
  target_ids:
  - MetaCyc:PWY-8383
  evidence_ids:
  - graph
  - record
  - full-gates
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - MetaCyc:PWY-8383
  rationale: Retain complete native9-member pathway with both A/B branches; precursor
    DHB supply is a separate native boundary and composite activity summaries are
    not extra reactions.
  evidence_ids:
  - native-database
  - primary-2001
  - primary-2008-si
  - record
limitations:
- N6-first is a native database convention;2001 Figure5C leaves acylation order unresolved.
- Six carrier-bound states are symbolic protein classes. Balance does not define full
  polypeptide formulas, fixed complex stoichiometry, channeling or thermodynamic flux.
- Native Sga15 CDS identity is distinct from species-level unreviewed UniProt annotations
  and historically tagged/processed assay constructs. Exact2008 engineered MxcL residues
  are not fully reconstructed.
- NADH is a slower observed alternative; native equations retain NADPH. MtaA is heterologous
  activation, PLP has direct SI support, magnesium is an assay ingredient, and three
  ATP events are derived accounting.
- Complete2005/2008 main articles were not inspected locally;2008 SI and2001 primary
  body evidence are explicitly scoped.
- No compartment, regulation, native PPTase, fixed E:F:G:L assembly or iModulon biological-absence
  conclusion is inferred.
- Previous full SQL/Rhea/RDKit/balance and authentic mutation-control executions are
  attributed preserved proofs; current reviewer did not duplicate a20GB full replay.
  Current source/authority selected checks and root terminal integrated/full-corpus
  receipts were freshly inspected.
- Endpoint digest checks do not exclude arbitrary transient machine-state mutation
  or attest every installed dependency implementation. Narrow integration boundary
  controls are not full production mutation replays.
- Programmatic37SVG/38KGX node preservation is not a browser visual or interaction
  check.
- Working-tree input attestation binds80 final files at available basebabe44ad; it
  does not assert that those bytes were already committed, merged or published.
notes:
- Preparatory scientific reading preceded final input freeze by parent instruction.
  Actual canonical inspect ran successfully after explicit final freeze at17:26:24Z;
  final assessment retained unchanged exact bytes and completed receipts.
- Initial local reading fallbacks and input-list preparation typo are retained in
  preparatory/external execution receipts; none was a record/source defect.
- No maintained target, authority, history, page or dossier changes were made by this
  reviewer; only the canonical immutable review bundle is saved.
- Issue402 and404 are external GitHub/preintegration lineage, not previous_occurrences
  or invented saved canonical review identities.
- Initial canonical validator bf18c7/1 rejected an unsaved review ID prefixed with
  start rather than finished UTC timestamp; the corrected ID uses finished17:28:33Z.
  No bundle existed or was overwritten.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/402
- https://github.com/CultureBotAI/PathwayMech/issues/404
tags:
- scientific-review
- whole-record
- myxochelin
- independent
- complete-native-pathway
```
