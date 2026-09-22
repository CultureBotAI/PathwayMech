---
name: source-triage
description: Evaluate microbial pathway definition sources for PathwayMech, fold source-discovery research into conf/sources.yaml, and rank candidates by license, stable identifiers, microbial coverage, machine access, and curation value. Use when asked what source to add next or whether a pathway database should be ingested; this does not authorize fetching or adopting the source.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Triage Pathway Sources

Keep PathwayMech's candidate source inventory aligned with current source
research. This is adapted from sibling Mech `source-queue` skills, but
PathwayMech currently ranks candidates directly in `conf/sources.yaml` plus
notes under `research/source_discovery/` instead of a separate
`curation/source_queue.tsv`.

## Read First

- `conf/sources.yaml` for active and deferred sources.
- `research/source_discovery/` for evidence behind source candidates.
- `docs/CURATION.md` for where source-specific normalization notes belong.
- `docs/HARMONIZATION.md` for preferred identifier systems.
- `scripts/seed_from_sources.py` for the source-ingestion surface that emits
  the priority-sorted seed queue.

## Ranking Rule

Rank sources by what they let PathwayMech curate with less manual invention,
not by database fame. In order:

1. **Exact pathway definitions in scope.** A source with curated microbial
   pathway or biosynthetic modules outranks a source that only has broad human
   signaling diagrams or taxon-level pathway calls.
2. **Stable native identifiers.** Per-pathway, per-reaction, and per-compound
   IDs must be citable and versionable enough to reproduce a YAML record.
3. **Cross references.** Prefer direct joins to `GO`, `gomodel`,
   `WikiPathways`, `MetaCyc`, `KEGG`, `RHEA`, `MIBiG`, `ModelSEED`, `BiGG`,
   `BV-BRC`, `Reactome`, `PathBank`, `CHEBI`, `EC`, `SGD`, `UniProtKB`,
   `NCBITaxon`, `GTDB`, or `GO_REF`.
4. **Redistribution and attribution.** Verify the source's own terms. A
   restricted source may still guide manual curation, but it must not be
   copied into committed YAML unless the license allows that use.
5. **Machine access.** Prefer stable downloads, APIs, KGML, SBML, BioPAX, RDF,
   TSV, or JSON over source pages that require manual scraping.
6. **Taxon specificity.** Sources that say where a pathway is observed or
   studied beat organism-agnostic maps.
7. **Implementation effort.** Count effort only after scope, license,
   identifiers, access, and taxon linkage are understood.

Two sources that fill the same gap should not both become active at once. Add
one canary ingestion path, measure what it contributes, and then re-rank the
remaining source.

## Evaluating a Candidate

For each candidate, establish:

- the exact files, API endpoints, or download formats it exposes;
- the license URL, required attribution, and redistribution limits;
- native IDs for pathways, reactions, metabolites, enzymes, and taxa;
- how those IDs join to the allowed PathwayMech CURIE prefixes;
- whether records are experimentally curated or computationally predicted;
- the smallest canary pathway that could be ingested end to end.

If a field cannot be verified, keep the conclusion explicit in the research
note and keep the source disabled unless the user asks for an active placeholder.

## Updating PathwayMech

For a source-discovery report, update one row per source in
`conf/sources.yaml`:

- use stable lower-case `id` values;
- set `priority` to the source's numeric ingest priority;
- set `ingest_status` to `next`, `support`, `fixture`, `license-gated`,
  `active`, or `deferred`;
- set `enabled: false` for candidates that have no implemented ingestion path;
- keep `role` specific, such as `pathway-reference`, `reaction-reference`,
  `pathway-grounding`, `causal-activity-model`, or
  `biosynthetic-gene-cluster-reference`;
- keep `notes` to one curation-relevant sentence and leave details in
  `research/source_discovery/`.

Questions about what to ingest next are triage only. Do not download bulk data,
spend provider credits, write an extractor, or mark a source adopted unless the
user explicitly asks for that work.

## Verify

After editing source inventory or research notes, run:

```bash
just seed
just validate
just test
just lint
git diff --check
```

## Report

Report the top candidates, the gap each closes, what remains unverified about
license or access, any `conf/sources.yaml` rows changed, and every validation
command that passed or was unavailable.
