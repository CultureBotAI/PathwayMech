# Merge Queue

Before merging a curation pull request:

1. Confirm that `just validate` passes.
2. Confirm that every mechanistic edge has reference-backed evidence.
3. Confirm that generated pages were refreshed when curated YAML changed
   (`just check-pages`, also part of `just validate` and of CI).

## Protected-main workflow

Submit reviewed pull requests through GitHub's native merge queue. The required
`qc` and `vendored-sync` checks run on both pull requests and the combined
`merge_group` commit, so the queue validates changes together with current `main`.
See the [fleet merge queue guide](https://github.com/CultureBotAI/culturebotai-claw/blob/main/docs/guides/MERGE_QUEUES.md)
for queue policy and administration.

Capture the PR head, review that commit, then enqueue it:

```bash
pr=123  # Replace with the pull request number.
head_sha=$(gh pr view "$pr" --repo CultureBotAI/PathwayMech --json headRefOid --jq .headRefOid)
# Review the commit identified by "$head_sha" before continuing.
gh pr merge "$pr" --repo CultureBotAI/PathwayMech \
  --match-head-commit "$head_sha"
```

If the head changes, review the new commit before resubmitting it. Do not use
`--admin` to bypass the queue. A queued PR or enabled auto-merge is still pending;
confirm that GitHub reports `MERGED` before deleting its branch or worktree:

```bash
gh pr view "$pr" --repo CultureBotAI/PathwayMech \
  --json state,mergedAt,mergeCommit
```

Do not rebase solely because `main` advanced; the queue tests the combined result.
Resolve actual merge conflicts on the PR branch. If queue checks fail, inspect
the failing `merge_group` run, fix the cause, and review and enqueue the updated
head after its checks pass.
