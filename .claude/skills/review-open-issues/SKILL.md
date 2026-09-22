---
name: review-open-issues
description: Sweep and triage PathwayMech's full open-issue queue. Fetch every open issue, check each against main, the pathway corpus, source inventory, research notes, validators, and docs, flag duplicates and already-fixed items, and assign a priority tier. Produces a short ranked report; only touches GitHub when explicitly asked.
allowed-tools: Bash, Read, Grep, Glob
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review and Prioritize Open Issues

Produce an honest, current ranking of the whole PathwayMech open-issue queue.
This skill ranks issues; it does not implement fixes, merge, close, relabel, or
promote records.

## Read-Only Default

Fetching and reading issues is allowed. Closing, relabeling, retitling,
commenting, opening issues, editing projects, merging pull requests, and
mentioning people are writes; ask for explicit authorization before each batch
of GitHub mutations and keep the evidence in the comment concise.

## What Makes PathwayMech Different

- The curated corpus is still small and flat: all maintained pathway records
  are direct YAML files in `data/pathways/`.
- `pages/` is generated. A stale page or empty browse view should be checked
  against `just validate` and `just render-pages`, then fixed by regenerating
  from YAML, not by patching HTML.
- `conf/sources.yaml` is the current source inventory. Candidate source
  adoption and licensing questions should be handed to `source-triage`.
- The first local gates validate YAML shape, local edge endpoints, local
  reference IDs, documentation presence, the deep-research report contract, and
  tests. They do not establish that a cited paper really supports an edge.
- PathwayMech does not yet have record status, curation history, or guarded
  writers. Treat issues asking for those as infrastructure work, not record
  curation.

## Workflow

### 1. Fetch the Full Open-Issue Queue

```bash
repo="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
queue_file="${TMPDIR:-/tmp}/pathwaymech-open-issues.json"
gh issue list -R "$repo" --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt,url > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], (.labels|map(.name)|join(",")), .title] | @tsv' "$queue_file"
jq length "$queue_file"
```

`--limit` caps silently; print the JSON length and say whether coverage was
complete. Read bodies and comments from the JSON before calling an issue stale.

If `gh` or the network is unavailable, review any locally available issue
notes and say that remote coverage was unavailable. Do not pretend the queue
was complete.

### 2. Establish the Tree State

Run the local read-only gates before checking issue claims:

```bash
git fetch origin main
git status -sb
just validate
just test
just lint
git diff --check
```

If `just validate` fails on `main`, that is the first finding and every other
verdict is provisional until the failing gate is explained.

### 3. Group and Classify

Group by pathway identifier, source candidate, PR reference, validator, or the
same failure shape. Issues filed by one review pass often describe one
underlying defect.

Classify each issue:

- **verifiable now**: about a file, pathway record, source row, rendered page,
  documentation page, or identifier that can be checked now;
- **source triage**: asks which pathway source to adopt, or whether a source's
  license, identifiers, or access are good enough;
- **curation review**: alleges a factual pathway error that needs source
  reading, not just a shape validator;
- **decision**: needs the owner to choose policy, scope, or license posture;
- **upstream**: belongs in GO, MetaCyc, KEGG, Rhea, ChEBI, kg-microbe, or
  another sibling Mech first.

### 4. Check Each Issue Against Current Reality

- **Already fixed on `origin/main`?** Use
  `git log --oneline origin/main --perl-regexp --grep "#<N>\\b"`. The `\\b`
  matters because `#4` also matches `#40`.
- **Path still exists?** Use `rg --no-ignore --hidden` or `find` before
  reporting that a named file, record, report, or source row is absent.
- **Identifier claim still true?** Resolve the exact GO, MetaCyc, KEGG, Rhea,
  CHEBI, EC, UniProtKB, NCBITaxon, GTDB, DOI, or PMID named in the issue.
- **Count still true?** Re-derive from the YAML or source inventory; do not
  trust counts in old prose.
- **Source status changed?** Cross-check `conf/sources.yaml` and
  `research/source_discovery/` before ranking a database-adoption issue.
- **Gate still missing?** Confirm the test, script, or validator named in the
  issue does or does not exist in the current tree.

### 5. Assign Priority

- **P0 - silently wrong data or license breach.** A pathway record whose
  identity, local graph, source support, or redistribution state is wrong while
  all gates pass.
- **P1 - real and schedulable.** A gate gap that could let a P0 through, a
  missing test with a known failure, or an implemented source-adoption step
  with bounded scope.
- **P2 - process or documentation.** Broken guidance, stale generated docs, or
  a non-data workflow gap.
- **P3 - backlog.** Real but unscheduled corpus growth or future polish.

`decision`, `curation-review`, `source-triage`, and `upstream` are orthogonal
labels, not severities. Label changes are GitHub writes; ask first.

### 6. Present the Report

Report:

- the count reviewed and whether queue coverage was complete;
- what `just validate`, `just test`, and `just lint` said on the checked tree;
- a ranked list of still-open work, P0 first, one line per issue or group;
- issues that are fixed in code and should be closed, with the commit, PR, or
  file that proves it;
- issues needing a decision, curation review, source triage, or upstream work;
- the top two or three issues to act on next, with a one-sentence reason.

Do not edit GitHub unless the user explicitly asks you to act on the reviewed
queue.

## Conventions

- Full-queue coverage beats first-page sampling. State the count.
- Evidence over intuition. Every fixed, duplicate, or false-positive verdict
  cites a commit, PR, file, or exact lookup.
- Resolve exact identifiers live when they are part of the issue.
- Use gitignore-independent search before reporting that something is absent.
- Read-only by default.
- No @-mentions without explicit per-mention authorization.

## Related

- `.claude/skills/source-triage/SKILL.md` for source-adoption issues.
- `.claude/skills/review-yaml-record/SKILL.md` for named pathway review.
- `.claude/skills/review-yaml-category/SKILL.md` for cohort review.
- `just validate`, `just test`, and `just lint` for local gates.
