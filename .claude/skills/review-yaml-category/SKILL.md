---
name: review-yaml-category
description: "Review one coherent PathwayMech YAML record category or cohort without editing records: resolve membership, find duplicate or over-split pathways, audit identity and evidence patterns, and report exact curation follow-up. Use when asked to audit a pathway type, identifier namespace, taxon slice, source slice, folder, or record set. Not for one named record, curation edits, source ingestion, paid research, or GitHub mutation."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  requires_database: false
  requires_internet: true
  version: 1.0.0
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
validation commands, Markdown reports under the review-report path named below,
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

After resolving at least one coherent target category and completing a review,
write one timestamped Markdown report per reviewed cohort before the final
response:

- Name each report
  `reports/yaml_category_review/<YYYYMMDDTHHMMSSZ>-<category-slug>.md`. Use
  `date -u +%Y%m%dT%H%M%SZ` for the UTC timestamp. Preserve the category slug
  when it is already filename-safe; otherwise slugify it to lower-case ASCII
  words joined with `-`.
- Create `reports/yaml_category_review/` if it does not exist.
- Do not overwrite or append to a prior review. If a filename already exists,
  regenerate the timestamp.
- Keep this section order so review reports are easy to diff across the fleet:

```markdown
# YAML Category Review: <category label>

- Repository:
- Category:
- Selection Rule:
- Started UTC:
- Finished UTC:
- Verdict:

## Target Category
## Selection and Membership
## Validation
## Lump and Split Review
## Identity and Grounding
## Graph and Evidence Patterns
## Completeness Patterns
## Findings
## Recommended Edits
## Follow-up Checks
## Additional Notes
```

Use `None found` or `Not checked: <reason>` when a section has no findings or a
check cannot run; do not delete required headings. If only a sample was read,
the verdict must say `sampled` and must not claim full-category coverage.

Do not edit YAML, regenerate pages, append curation history, or create a
GitHub item from this read-only review. If the request needs disambiguation
before a coherent category is resolved, ask for it without creating a report.

In the final response, link every report path and summarize only each verdict,
finding counts by severity, skipped validators, and unresolved blockers.
