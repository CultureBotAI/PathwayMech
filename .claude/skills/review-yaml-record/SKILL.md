---
name: review-yaml-record
description: "Review one PathwayMech YAML record without editing it: verify exact pathway identity, local taxa, participants, reactions, edge-level source support, evidence placement, and the exact follow-up a curator would need. Use when asked to audit, inspect, spot-check, or review one named pathway record. Not for category reviews, curation edits, source ingestion, paid research, or GitHub mutation."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  requires_database: false
  requires_internet: true
  version: 1.0.0
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
commands, one new Markdown report under the review-report path named below, and
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
- Preserve scope. Evidence about one strain, enzyme isoform, condition, or
  pathway variant is not evidence for a broader route unless the source makes
  that generalization.
- Preserve conflicts. If inspected sources disagree on pathway membership,
  directionality, cofactors, taxon scope, or regulation, report the disagreement
  and its scope instead of choosing the convenient source.
- A near miss is not a match. Do not ground a pathway, reaction, or participant
  to a plausible broader or adjacent term.

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

After resolving exactly one target and completing a review, write exactly one
timestamped Markdown report before the final response:

- Name it `reports/yaml_record_review/<YYYYMMDDTHHMMSSZ>-<record-stem>.md`.
  Use `date -u +%Y%m%dT%H%M%SZ` for the UTC timestamp. Preserve the target
  file stem when it is already filename-safe; otherwise slugify it to
  lower-case ASCII words joined with `-`.
- Create `reports/yaml_record_review/` if it does not exist.
- Do not overwrite or append to a prior review. If a filename already exists,
  regenerate the timestamp.
- Keep this section order so review reports are easy to diff across the fleet:

```markdown
# YAML Record Review: <record label>

- Repository:
- Record:
- Started UTC:
- Finished UTC:
- Verdict:

## Target
## Validation
## Identity and Grounding
## Graph and Local References
## Edge Evidence
## Completeness
## Findings
## Recommended Edits
## Follow-up Checks
## Additional Notes
```

Use `None found` or `Not checked: <reason>` when a section has no findings or a
check cannot run; do not delete required headings.

Do not edit the YAML, regenerate `pages/`, append curation history, or create a
GitHub item from this read-only review. If the request needs disambiguation
before one target is resolved, ask for it without creating a report.

In the final response, link the report path and summarize only the verdict,
finding counts by severity, skipped validators, and unresolved blockers.
