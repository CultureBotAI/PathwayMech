---
name: review-yaml-record
description: "Review one PathwayMech YAML record without editing it: verify exact pathway identity, local taxa, participants, reactions, edge-level source support, evidence placement, and the exact follow-up a curator would need. Use when asked to audit, inspect, spot-check, or review one named pathway record. Not for category reviews, curation edits, source ingestion, paid research, or GitHub mutation."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Review One PathwayMech YAML Record

- Repository: `CultureBotAI/PathwayMech`
- Records: `data/pathways/*.yaml`
- Schema: `src/pathwaymech/schema.py`

## The Contract

Produce a read-only judgement of one pathway record: what is sound, what is
unsupported or internally inconsistent, what is materially incomplete, and what
bounded checks would resolve the remaining uncertainty.

Reviewing is not curation. A review request authorizes reads, validation
commands, one structured YAML/Markdown review bundle described below, and
a concise final summary; it does not authorize editing a pathway record,
regenerating pages, spending provider credits, contacting anyone, or creating
or mutating GitHub issues, pull requests, comments, labels, or settings.

Resolve exactly one target under `data/pathways/` before judging anything. If a
label, identifier, file stem, or source accession matches several records, stop
and disambiguate.

Read the entire target file before making a finding. Rendered pages, raw
research reports, and search snippets are useful leads, but they hide context
and cannot support a record-level verdict on their own.

## Scope

Review only YAML records from `data/pathways/`. The YAML is the maintained
curation surface. `pages/` is generated from YAML, so report stale rendered
pages but do not patch them by hand.

Future fixes usually belong to the target YAML itself, `conf/sources.yaml`,
`templates/pathway_mechanism_research.md`, or extractor code once a source is
adopted. This repository does not yet have sibling-style `write_validated_*`,
inline curation-history, record-status promotion, or source-overlay helpers; do
not invent them in a review report.

Use `.claude/skills/add-pathway/SKILL.md`, `docs/CURATION.md`, and
`docs/HARMONIZATION.md` as the local field and identifier rubric.

## Evidence Rules

- Verify every stable pathway, reaction, metabolite, enzyme, taxon, DOI, PMID,
  ontology CURIE, and internal `reference_id` the record relies on.
- Attach evidence to the narrowest mechanistic edge it supports. A source that
  supports one reaction or enzyme does not support every edge in a pathway map.
- Treat search results, raw research reports, database summaries, generated
  pages, and generated indexes as leads. Only inspected source text can support
  a claim.
- Keep direct quotations short and exact. Interpretation belongs in notes or in
  the review report, not inside quoted snippets.
- For structured database statements, verify `source_assertion` against the
  exact native object or triple in `source_locator`; it is not a quotation from
  a paper cited by that database. Follow `docs/CAUSAL_GRAPHS.md` for component
  roles, cofactors, compartments, reaction directions, and evidence limitations.
- Preserve scope. Evidence about one strain, enzyme isoform, condition, or
  pathway variant is not evidence for a broader route unless the source makes
  that generalization.
- Preserve conflicts. If inspected sources disagree on pathway membership,
  directionality, cofactors, taxon scope, or regulation, report the disagreement
  and its scope instead of choosing the convenient source.
- A near miss is not a match. Do not ground a pathway, reaction, or participant
  to a plausible broader or adjacent term.

## Structured Source Cross-Checks

<!-- canonical:begin structured-source-cross-checks -->
Use structured source adapters before open-ended web search when this record
names a gene, locus tag, UniProt accession, regulator, pathway, reaction,
enzyme, or transcriptomics dataset that may already be represented in a shared
database.

For iModulonDB candidates, first resolve the runner. In the commands below,
`<kg-microbe-sources>` means either an installed `kg-microbe-sources` console
script or `uv run --project <claw-root> kg-microbe-sources` from a local
`culturebotai-claw` checkout. If neither runner is available, record the
structured adapter as unavailable and fall back to inspected iModulonDB source
pages or open web search.

- Run `<kg-microbe-sources> imodulondb datasets` to find covered
  organism/dataset keys.
- Run `<kg-microbe-sources> imodulondb search --organism <organism> --dataset
  <dataset> --query <term>` for a record gene, locus, regulator, protein name,
  pathway term, reaction term, or iModulon name that matches a covered
  organism.
- Run `<kg-microbe-sources> imodulondb summarize --organism <organism>
  --dataset <dataset> --k <component>` for any iModulon hit that would inform
  the record verdict.
- Record useful `organism/dataset/component` and `organism/dataset/gene` keys
  under **Edge Evidence** or **Additional Notes**, and keep any copied summary
  table small enough to justify why a pathway protein is or is not supported.

iModulon membership is computational expression-module evidence. It can support
a bounded transcriptomic context finding for a covered strain, gene, regulator,
or protein, but it is not direct proof of pathway identity, reaction
membership, catalysis, metabolite usage, edge direction, or taxon scope. If no
covered organism/dataset matches the target, write that iModulonDB was not
applicable; absence from iModulonDB is not negative evidence.
<!-- canonical:end structured-source-cross-checks -->

## Missing Things

Before reporting that a record, source file, evidence object, pathway node,
generated product, or referenced artifact is absent, search for the identifier,
label, and slug with a gitignore-independent search such as
`rg --no-ignore --hidden`, `rg -uu`, `grep -r`, or `find`.

Say what the exhaustive search covered. If you used an ordinary ignored-aware
search, call the miss provisional.

## Workflow

1. Read the local guidance that names exact validators and field boundaries:
   `CLAUDE.md`, `justfile`, `docs/CURATION.md`,
   `docs/HARMONIZATION.md`, `.claude/skills/add-pathway/SKILL.md`, and
   `src/pathwaymech/schema.py`.
2. Resolve one YAML file under `data/pathways/`. Confirm its identifier,
   label, description, pathway type, taxa, participants, reactions,
   mechanistic edges, and references.
3. Run the validators that are read-only for this repository:

   ```bash
   just validate
   just test
   just lint
   git diff --check
   ```

   Do not invent a focused validator for one pathway until the repository
   exposes one; report full-corpus checks honestly.
4. Verify pathway identity first. Confirm that the record denotes the requested
   pathway, not an alternate route, a sibling module, a single reaction, a broad
   process parent, or a similarly named pathway from another taxon.
5. Verify local graph shape. Every `mechanistic_edges` endpoint must be the
   record id or a declared local taxon, participant, or reaction. Every
   predicate must appear in `ALLOWED_EDGE_PREDICATES`.
6. Verify every material assertion against its nearest cited source. Check
   pathway membership, participant identity, reaction identity, enzyme identity,
   taxon scope, edge direction, regulation, and reference metadata.
7. Classify findings by severity:
   **blocker** for invalid YAML, a broken local edge or reference, wrong
   pathway identity, or an edge that makes the record denote the wrong thing;
   **major** for unsupported evidence, wrong grounding, scope inflation,
   material incompleteness, or a recurring source-ingestion bug;
   **minor** for weak wording, redundant evidence, or non-blocking provenance
   gaps.
8. Report the exact follow-up: which maintained file should change, which
   generated page should be refreshed, which validator would prove the fix, and
   which uncertainty remains genuinely unresolved.

## Output

<!-- canonical:begin output -->
Save one immutable structured review bundle for the resolved record
using the CLAW-governed contract in `docs/record-reviews.md` and
`schema/record_review.yaml`. Preserve the local rubric identified by
`docs/record-review-profile.md`.

- Capture actual UTC start/finish, reviewer identity and independence, exact
  target IDs/locators, Git base, input hashes, and generated-input owners.
- Retain every check and its real result, domain assessments, inspected evidence,
  normalized findings, native rules/severity rationale, proposed actions with
  acceptance checks, and explicit limitations. Do not equate a deterministic
  check with scientific review.
- Use `kind: record`; it identifies exactly one target.
- Invoke `uv run python scripts/record_review.py inspect --targets <targets.yaml>`
  before assessment, then `validate <completed-review.yaml>` and
  `save --content <completed-review.yaml>` with the same script. Recheck changed
  inputs instead of silently refreshing their hashes.
- The saver writes
  `reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml` plus `review.md`.
  YAML is authoritative; do not hand-edit the rendered Markdown or overwrite an
  earlier bundle. Run `uv run python scripts/record_review.py check` afterward.
- If required checks are unavailable after the target is resolved, save an honest
  partial/blocked observation. If the shared saver itself cannot run, report
  that persistence is blocked; session-only prose is not a saved review.
- Retain stable issue keys and exact `previous_occurrences` when reassessing a
  finding. A later clean report does not close earlier unresolved findings.
- Do not append curation/history events or promote native scientific status.
  Those require a separately authorized curation change and native gates.

Do not create a report for an unresolved ambiguous target. In the final response,
link both saved files and summarize scope, verdict, findings by severity, and
unavailable checks. Existing ad hoc Markdown is historical, not the output format
for new reviews.
<!-- canonical:end output -->
