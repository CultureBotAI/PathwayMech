---
name: review-yaml-category
description: "Review one coherent PathwayMech YAML record category or cohort without editing records: resolve membership, find duplicate or over-split pathways, audit identity and evidence patterns, and report exact curation follow-up. Use when asked to audit a pathway type, identifier namespace, taxon slice, source slice, folder, or record set. Not for one named record, curation edits, source ingestion, paid research, or GitHub mutation."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Review One PathwayMech YAML Category

- Repository: `CultureBotAI/PathwayMech`
- Records: `data/pathways/*.yaml`
- Schema: `src/pathwaymech/schema.py`

## The Contract

Produce a read-only judgement of a coherent pathway-record cohort: which
records belong together, which are duplicates or aliases that should be merged,
which represent variants that should stay split, which patterns are well
supported, and which future curation changes would make the cohort sound.

Reviewing a category is not curation. A review request authorizes reads,
validation commands, structured YAML/Markdown review bundles described below,
and a concise final summary; it does not authorize editing records,
regenerating products, spending provider credits, contacting anyone, or
creating or mutating GitHub issues, pull requests, comments, labels, or
settings.

Use the user's words as a starting point, not as an unquestioned file glob. A
PathwayMech cohort can be a `pathway_type`, an identifier namespace, a taxon
slice, a source slice, a shared participant or reaction, or an explicit list of
YAML files. If the request names a mixture, split it into coherent cohorts and
review each cohort separately.

## Scope

Review only YAML records from `data/pathways/`. The YAML is the maintained
curation surface; `pages/` is generated and should only be reported when it is
stale.

Use `.claude/skills/review-yaml-record/SKILL.md` for the per-record review
rubric. Category review adds a boundary layer: membership, duplicate pathway
identity, over-broad cohorts, over-split species variants, and systemic
patterns across the member records.

## Evidence Rules

- Verify every stable identifier, DOI, PMID, ontology CURIE, source accession,
  and internal reference that a boundary, lump, or split finding relies on.
- Treat a shared string, pathway map, reaction, or source accession as a lead
  for equivalence, not proof that two PathwayMech records have the same
  intended identity.
- Treat search results, raw research reports, generated summaries, rendered
  pages, and generated indexes as leads. Only inspected source text can support
  a claim.
- Preserve legitimate variants. Alternative routes, organism-specific variants,
  adjacent modules, and pathway subsets may be separate records on purpose.
- Preserve conflicts. If inspected sources disagree, report the disagreement
  and its scope instead of forcing the category to look tidy.
- Use `docs/CAUSAL_GRAPHS.md` for source-fact coverage, enzyme/cofactor and
  compartment roles, reaction directions, and traceable structured assertions.

## Structured Source Cross-Checks

<!-- canonical:begin structured-source-cross-checks -->
Use structured source adapters before open-ended web search when the cohort
boundary depends on genes, locus tags, UniProt accessions, regulators,
pathways, reactions, enzymes, or transcriptomics datasets that may already be
represented in a shared database.

For iModulonDB candidates, first resolve the runner. In the commands below,
`<kg-microbe-sources>` means either an installed `kg-microbe-sources` console
script or `uv run --project <claw-root> kg-microbe-sources` from a local
`culturebotai-claw` checkout. If neither runner is available, record the
structured adapter as unavailable and fall back to inspected iModulonDB source
pages or open web search.

- Run `<kg-microbe-sources> imodulondb datasets` to find covered
  organism/dataset keys.
- Run `<kg-microbe-sources> imodulondb search --organism <organism> --dataset
  <dataset> --query <term>` for member genes, loci, regulators, protein names,
  pathway terms, reaction terms, or iModulon names that match covered
  organisms.
- Run `<kg-microbe-sources> imodulondb summarize --organism <organism>
  --dataset <dataset> --k <component>` for iModulon hits that explain a
  repeated evidence or membership pattern.
- Record useful `organism/dataset/component` and `organism/dataset/gene` keys
  under **Graph and Evidence Patterns** or **Additional Notes**, and keep any
  copied summary tables small enough to justify why pathway proteins are or
  are not supported.

iModulon membership is computational expression-module evidence. It can support
a bounded transcriptomic context finding for a covered strain, gene, regulator,
or protein, but it is not direct proof of pathway identity, reaction
membership, catalysis, metabolite usage, edge direction, or taxon scope. If no
covered organism/dataset matches the cohort, write that iModulonDB was not
applicable; absence from iModulonDB is not negative evidence.
<!-- canonical:end structured-source-cross-checks -->

## Missing Things

Before reporting that a sibling pathway, duplicate record, source file,
evidence object, generated product, or referenced artifact is absent, search
for the identifier, label, slug, and plausible source aliases with a
gitignore-independent search such as `rg --no-ignore --hidden`, `rg -uu`,
`grep -r`, or `find`.

Say what the exhaustive search covered. If you used an ordinary ignored-aware
search, call the miss provisional.

## Workflow

1. Read `CLAUDE.md`, `justfile`, `docs/CURATION.md`,
   `docs/HARMONIZATION.md`, `.claude/skills/review-yaml-record/SKILL.md`, and
   `src/pathwaymech/schema.py`.
2. Resolve the requested category into one or more bounded cohorts under
   `data/pathways/`. Record the selection rule for each cohort, then enumerate
   its candidate members from the filesystem. Do not write a report for an
   ambiguous or unbounded set.
3. Search outside the initial candidate list for aliases, duplicate labels,
   adjacent pathway IDs, source rows, or ontology siblings that might need to
   be lumped into the review or split out of it. Include ignored and hidden
   files before declaring no sibling exists.
4. Read every member record when the cohort is bounded and tractable. If the
   cohort is too large for full manual inspection, split it into smaller
   coherent cohorts. Use deterministic, explicitly documented strata only when
   the user's question really is a sample.
5. Run the documented read-only validators:

   ```bash
   just validate
   just test
   just lint
   git diff --check
   ```

6. Judge the set before judging individual records: membership, duplicate
   pathway identities, over-split variants, over-broad groups, ontology-parent
   drift, and records whose identifiers, labels, pathway types, taxa, or
   evidence put them outside the resolved boundary.
7. Apply the per-record checklist to the members that drive the category
   verdict. Promote repeated per-record findings into systemic findings when
   the same source, identifier namespace, template, or schema pattern owns
   them.
8. Classify findings by severity:
   **blocker** for a boundary that denotes the wrong kind of record, a
   duplicate/split error that makes records incorrect, invalid YAML, or broken
   local edges;
   **major** for unsupported category membership, wrong pathway grounding,
   scope inflation, missing required mechanism, or duplicate records with the
   same intended identity;
   **minor** for style, weak wording, redundant evidence, or non-blocking
   provenance gaps.
9. Report the exact follow-up: which maintained file should change, which
   generated page should be refreshed, which validator would prove the fix, and
   which uncertainty remains genuinely unresolved.

## Output

<!-- canonical:begin output -->
Save one immutable structured review bundle per reviewed cohort
using the CLAW-governed contract in `docs/record-reviews.md` and
`schema/record_review.yaml`. Preserve the local rubric identified by
`docs/record-review-profile.md`.

- Capture actual UTC start/finish, reviewer identity and independence, exact
  target IDs/locators, Git base, input hashes, and generated-input owners.
- Retain every check and its real result, domain assessments, inspected evidence,
  normalized findings, native rules/severity rationale, proposed actions with
  acceptance checks, and explicit limitations. Do not equate a deterministic
  check with scientific review.
- Use `kind: category`; enumerate reviewed members, population and selection,
  and record explicit lump/split/retain/defer decisions with evidence. Sampled
  coverage must retain its method and uninspected remainder.
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
