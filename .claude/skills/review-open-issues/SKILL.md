---
name: review-open-issues
description: Review and prioritize PathwayMech's full open GitHub issue queue against current code, pathway records, source inventory, evidence, and gates. Identify partial fixes, duplicates, and closure candidates; rank remaining work by severity and dependencies. Use inside PathwayMech for issue reviews or backlog triage, not for implementing fixes or discovering new sources. Read-only by default.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Review and Prioritize Open Issues

Produce an evidence-backed ranking of PathwayMech's open-issue queue, following
the full-queue, dependency-aware review pattern used in the other Mech repos.
Review the whole queue unless the user specifies a subset; a source inventory
or planning document is context, not a substitute for GitHub issues.

## Scope and Authorization

Review authorizes issue reads, public source checks, temporary review files,
and validation. Return the report in the conversation unless the user requests
a saved artifact. Do not implement fixes, edit records, regenerate committed
products, invoke paid research, or mutate GitHub merely to triage issues.

If the user also requests action on the findings, honor the specific actions
already authorized. Establish the issue numbers, proposed changes, and evidence
before any GitHub write. Ask only for missing authorization; do not repeatedly
confirm an already authorized batch. Do not infer permission to post comments,
mention people, open cross-repository issues, merge, or close unrelated issues.

## PathwayMech Sources of Truth

Read `CLAUDE.md`, `justfile`, and relevant CI workflows before evaluating claims
about what is maintained, generated, or checked. Then follow the affected stage:

```text
source terms and snapshots (conf/sources.yaml, research/source_discovery/)
  -> importers, identifiers, and source mappings (src/pathwaymech/)
  -> schema and pathway records (src/pathwaymech/schema/, data/pathways/)
  -> edge evidence, references, and curation history
  -> validation and CI gates
  -> generated pages, KGX/SSSOM exports, and published claims
```

- `src/pathwaymech/schema/pathwaymech.yaml` is the closed LinkML contract;
  `src/pathwaymech/schema.py` adds semantic checks. A schema-valid graph does
  not prove that a paper supports its edges.
- Inspect `data/pathways/` recursively using the current record-discovery
  implementation. Do not assume the corpus remains small or flat, or quote
  historical record counts as current measurements.
- `conf/sources.yaml` records source roles and ingestion status. `enabled:
  true` alone does not mean full ingestion, curated evidence, or permission to
  redistribute. Distinguish active, fixture, support, and license-gated work;
  check importers, tests, and actual records before calling adoption complete.
- `docs/CURATION.md` and `docs/HARMONIZATION.md` define curation and identifier
  boundaries. Research reports are leads; verify material claims against the
  cited primary source and preserve strain, condition, and pathway-variant scope.
- `curation_history` in pathway records and session records under `history/`
  are existing contracts. Read the schema and `history/README.md` before
  classifying a history issue as missing infrastructure.
- `pages/` is generated and committed. Use `just check-pages` to assess drift;
  do not repair HTML or run `just render-pages` during a review. Inspect the
  current tracking and generation rules for exports before treating an absent
  local export as a broken committed product.
- The governed-file list in `CLAUDE.md` and `scripts/.vendored_canon_ref`
  identify changes owned by `culturebotai-claw`. Recommend an upstream fix and
  re-pin when appropriate; do not propose patching vendored files locally.

## Workflow

### 1. Capture the Full Queue and Discussions

Resolve and check the repository identity before fetching issues. Paginate the
REST issue list and each discussion; the issue endpoint also returns pull
requests, so exclude those explicitly. Run this in Bash:

```bash
set -euo pipefail
repo="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
review_dir="$(mktemp -d "${TMPDIR:-/tmp}/pathwaymech-issues.XXXXXX")"
gh api --paginate "repos/$repo/issues?state=open&sort=created&direction=asc&per_page=100" \
  | jq -s '[.[][] | select(has("pull_request") | not)]' \
  > "$review_dir/issues.json"
jq -r '.[] | [.number, .created_at[:10], (.labels|map(.name)|join(",")), .title] | @tsv' \
  "$review_dir/issues.json"
jq length "$review_dir/issues.json"
while IFS= read -r number; do
  gh api --paginate "repos/$repo/issues/$number/comments?per_page=100" \
    | jq -s 'add // []' > "$review_dir/comments-$number.json"
done < <(jq -r '.[] | select(.comments > 0) | .number' "$review_dir/issues.json")
```

Read bodies and complete discussions, not only the printed overview. Comments
can withdraw a claim, record a fix, or narrow the remaining scope. Keep the
repository, capture time, issue count, and any fetch failures with the review.
Never interpret a failed request, partial JSON, or truncated tool output as an
empty queue or proof that an issue is resolved. If remote access is unavailable,
use available local notes and clearly limit the coverage claim.

### 2. Identify the Exact Tree and Gate Results

```bash
git status --short --branch
git fetch origin main
git rev-parse HEAD origin/main
just validate
just test
just lint
git diff --check
```

Fetching `origin/main` does not change the checkout. Report the tested commit
and local modifications. If this is a feature branch or a dirty tree, inspect
`origin/main` separately with `git show` or use an isolated checkout for
default-branch validation; preserve the user's working files. A local-only fix
is work in progress, not evidence that the default branch is fixed. If fetching
fails, state that the available base ref may be stale.

Run gates without pipelines that hide exit status. `just validate` checks
skills and runs the QC sequence in `src/pathwaymech/cli.py`; QC stops at its
first failure. List subsequent checks as not run unless you ran them separately.
A failure is a finding to explain, not a reason to stop reviewing unaffected
issues. Separate a repository defect from unavailable dependencies or services.

### 3. Place, Group, and Verify Every Issue

For each issue, identify its pipeline stage, affected files or identifiers,
owning repository, dependencies, and a decisive acceptance check. Group shared
root causes while retaining every member's number and remaining scope.

Verify the claims using the cheapest decisive evidence:

- **Fixed on the default branch?** Search `origin/main`, not `--all`:
  `git log --oneline origin/main --perl-regexp --grep '#<N>\b'`.
  The boundary prevents `#4` matching `#40`. A missing issue number in commit
  messages is not proof that no fix exists; inspect the current implementation.
- **Related PR merged?** Inspect exact links in the issue and
  `gh issue view <N> -R "$repo" --json closedByPullRequestsReferences`, then
  check candidate PRs with `gh pr view <PR> -R "$repo" --json state,mergedAt,url`.
  Confirm the change remains on the current base. Number-only PR searches and
  merge messages are leads, not proof that every acceptance criterion is met.
- **Fully or partly addressed?** Compare each acceptance criterion with current
  behavior and tests. Name the completed part and narrowed residual. A tracker
  or corpus-wide backlog is not complete because one slice landed.
- **Still reproducible?** Inspect the current schema, importer, validator,
  tests, and workflow triggers relevant to the claim. A renamed file does not
  resolve a defect if the behavior moved elsewhere. Distinguish code inspection
  from an executed reproduction, and inspect whether CI actually runs the gate.
- **Missing artifact or capability?** Include ignored files in searches:
  `rg --no-ignore --hidden` or `find`. Search identifiers, aliases, old paths,
  research notes, and relevant configured caches. State the searched scope and
  exclusions; a miss from an ordinary ignored-aware search is provisional.
- **Identity or evidence error?** Resolve the exact CURIE, accession, DOI, or
  PMID through primary sources. Inspect the cited text for the specific edge,
  direction, participants, and taxon scope. Membership, coexpression, a diagram,
  or an enzyme-step rule is not automatically a causal reaction graph. Failed
  access means unverified, not nonexistent or unsupported.
- **Source or count claim?** Re-derive counts from the current records or
  inventory. Check dated source-discovery notes and verify current access,
  versions, and reuse terms from primary sources when relevant. Separate
  observed upstream changes from what has actually been imported locally.
- **Duplicate or superseded?** Cite the surviving issue and compare scope.
  Similar titles alone do not establish a duplicate; retain unique residuals.

Use temporary copies for any reproduction that requires changing an input.
Do not weaken a schema, threshold, baseline, or exception rule to make a check
pass. Report what would establish a fix when testing it exceeds review scope.

### 4. Rank Consequence Separately from Cost and Readiness

- **P0 — active data or publication risk.** Wrong pathway identity, unsupported
  causal evidence, identifier corruption, or prohibited redistribution reaching
  maintained records or published products; a demonstrably blind gate exposing
  those consumers also belongs here. A speculative risk alone is not P0.
- **P1 — real and schedulable.** Reproducible defects, provenance gaps, bounded
  source-adoption work, or gate gaps with a concrete failure scenario.
- **P2 — process or documentation.** Guidance drift, noncritical workflow
  problems, and presentation defects without a material data consequence.
- **P3 — backlog.** Unscheduled corpus growth, optional audits, or future polish.

Keep **decision**, **curation review**, **source triage**, and **upstream** as
separate routing annotations. Mark unresolved evidence as **unverified**, not
as fixed. Dispositions such as **fixed**, **duplicate**, **superseded**, and
**partial** describe status, not severity. These are report annotations, not
instructions to create or change GitHub labels.

Record blockers and a rough cost class (inspection, local fix, corpus sweep,
regeneration, or external dependency). Sequence upstream fixes and missing
guards before the downstream work they protect. Preserve severity when a
high-impact issue is expensive or blocked; do not rank solely by age or an old
priority label.

### 5. Refresh and Report

Before finalizing, refresh the open issue list and compare numbers and
`updated_at` values with the snapshot. Re-read changed discussions, account for
new or closed issues, and disclose any remaining coverage gap. If the queue
continues moving, report a time-bounded snapshot rather than chasing it forever.

Return a compact report containing:

- Repository, review time, tested/base commits, issue count, and coverage.
- Gate results, including failures, skipped checks, and dirty-tree limitations.
- The top two or three next actions and what each unblocks.
- A ranked table with issue links, disposition, priority, concrete evidence,
  dependencies, cost, and next acceptance check. Include every reviewed issue,
  either individually or explicitly within a group.
- Closure/update candidates with exact commits, PRs, files, or comments that
  support the recommendation; partial fixes retain their residual work.
- Unresolved decisions, evidence gaps, source questions, and upstream owners.

Distinguish measured results, code inspection, inference, and proposed checks.
If actions were separately authorized, report precisely which mutations were
completed and which remain proposals. Write multiline GitHub bodies through a
structured API argument or `--body-file`, not shell-interpolated prose.

## Related Skills

- `.claude/skills/source-triage/SKILL.md` for source-adoption decisions.
- `.claude/skills/pathwaymech-discover-sources/SKILL.md` for source discovery
  and update scans.
- `.claude/skills/review-yaml-record/SKILL.md` for detailed named-record review.
- `.claude/skills/review-yaml-category/SKILL.md` for a cohort review.
