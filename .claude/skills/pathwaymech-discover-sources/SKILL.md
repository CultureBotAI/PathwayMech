---
name: pathwaymech-discover-sources
description: Find additional microbial pathway definition sources and check known sources for data, identifier, license, or access changes in PathwayMech. Use for incremental source discovery and update scans, not importer implementation or exhaustive landscape reviews.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Discover New and Updated Pathway Sources

Use inside the PathwayMech repository. Produce a dated, source-grounded delta
report and keep the candidate inventory aligned with it. Discovery does not
mean that a source is ingested or that its data can be redistributed.

## Establish the Baseline

Read `conf/sources.yaml`, the newest relevant notes in
`research/source_discovery/`, `docs/HARMONIZATION.md`, and the implemented
source's module, tests, and local provenance when comparing ingestion state.
The initial incremental baseline is
`research/source_discovery/2026-10-03-additional-sources-and-updates.md`.

Follow the requested scope: **discover**, **updates**, or **both** (default).
Select a manageable source subset; list what was checked and what was not.
For an exhaustive all-source review, use
`.claude/skills/review-pathway-sources/SKILL.md` instead.

Before calling a candidate new, search aliases, former names, native prefixes,
research notes, caches, and importer references with ignored files included:

```bash
rg --no-ignore --hidden -n -i '<source|alias|native-prefix>' . -g '!/.git/**' -g '!/.venv/**'
```

Inspect relevant configured caches outside the repository too. State any
excluded locations when an absence claim depends on them. Distinguish a
mention or identifier alias from an inventoried or implemented source.

## Discover

Search primary database sites, maintained repositories, current database
papers, and their supplements. Follow promising citations to actual files or
API documentation. Vary queries across bacteria, archaea, fungi, algae, and
protists and underrepresented functions such as xenobiotic degradation,
anaerobic metabolism, glycan use, and biosynthesis. Search combinations of
pathway/module definitions, reaction or protein identifiers, and machine
formats, rather than only database names.

For each credible candidate, establish:

- Contribution: directed reaction topology, logical enzyme-step rules,
  membership, reaction grounding, crosswalk, or model/diagram only.
- Taxon scope and whether organism attribution is experimental, predicted,
  or absent; a generic map is not a demonstrated microbial phenotype.
- Native pathway and element IDs with an actual example. Separate biological
  IDs from local drawing IDs. Mixed protein namespaces require explicit
  resolution; pathway labels alone are not canonical pathway IDs.
- Machine access and a small inspected sample: exact URL, file or API path,
  fields, version, and what relationships the sample actually encodes.
- Data reuse and access terms from primary pages. Record software, data,
  third-party, and paper licenses separately, with attribution obligations.
- Missing evidence or mapping work and one bounded canary for an ingestion
  handoff. Preserve local IDs as provenance until the schema permits them.

Do not treat arithmetic abundance formulas as reaction order or Boolean
completeness. Do not count a mirror, successor, or KEGG/MetaCyc derivative as
independent experimental evidence. Preserve upstream lineage and dataset
scope, including organism-specific PGDB IDs.

## Check Updates

Compare the same data artifact with a prior successful observation. Capture
the upstream version separately from the last locally ingested version;
either may be unknown. For GitHub, inspect data-path history or blob hashes,
not only repository push dates or releases. Pin inspected files to full commit
SHAs. For release servers, record exact filenames and schema versions; compute
checksums only when bytes were actually obtained.

Useful source-specific checks:

- WikiPathways: current GPML directory versus the previously inspected release.
- GO-CAM: JSON model snapshots and relevant taxon/model changes, not deprecated
  TTL exports.
- GapMind: `gaps/aa` and `gaps/carbon` data, not PaperBLAST documentation commits.
- UniPathway: `upa.obo` content, not regeneration dates alone.
- BRENDA: release, pathway export structure, and data license acceptance.
- HADEG: `Tables/7_All_pathways.csv` plus evidence tables and license.
- DRAM: distinguish DRAM1 `master` data from DRAM2 `dev`; compare rule files.
- DiTing: follow the original repository's maintained fork and formula file.
- enviPath: check current terms and legacy/current package migration before
  attempting a data request; an old paper license is not current permission.

Classify observations as **new candidate**, **first baseline**, **changed**,
**unchanged for the compared artifact**, or **unverified/blocked**. A repository
commit can be documentation-only; a rebuilt portal can retain old data. A
timeout is not retirement. Without a prior artifact/version, do not claim an
update or no change. Do not replace a successful baseline with a failed fetch.

## Persist and Hand Off

Write `research/source_discovery/YYYY-MM-DD-<scope>.md` with:

- check date, coverage and exclusions, and comparison baseline;
- ranked candidates, inspected IDs/formats, primary links, and blockers;
- an update table naming exact artifacts, observations, prior state, and the
  next comparison trigger;
- separate observed-upstream and local-ingestion state, with unknowns explicit;
- top next actions and a canary's success criteria.

Preserve historical reports and link the new findings from the landscape memo.
Keep source facts next to their citations and distinguish observed facts from
recommendations. Report counts as measured or publisher-reported; do not turn
a paper's historical count into a current dataset measurement.

Apply `.claude/skills/source-triage/SKILL.md` when adding or reprioritizing
`conf/sources.yaml`. Keep unsupported candidates `enabled: false`, with `next`,
`deferred`, or `license-gated` as justified. Existing enabled importers can
remain fixture/support/license-gated; enablement does not establish complete
corpus ingestion. Update inventory tests when changing the source list.

Research authorization covers bounded public inspection and local research
edits, not bulk mirroring, account creation, license acceptance, importer work,
or GitHub mutations unless the user separately requests them. Stop an affected
data request at authentication or terms that disallow its intended use; public
documentation can still establish the blocker. After repeated fetch failures,
record the check as unverified and continue with other sources.

## Verify and Report

After changing inventory or research, run `just seed`, `just validate`,
`just test`, `just lint`, and `git diff --check`. Validate new skill frontmatter
with the available skill-creator validator as well as `just validate-skills`.
Report checks that could not run.

Summarize the most useful new sources, verified changes, unresolved access or
reuse questions, and the report path. Explicitly say whether any ingestion
occurred. Do not create a scheduled scan unless asked.
