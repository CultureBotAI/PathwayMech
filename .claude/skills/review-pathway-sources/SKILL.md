---
name: review-pathway-sources
description: Review PathwayMech's complete microbial pathway data-source landscape across bacteria, archaea, fungi, algae, and protists, then update conf/sources.yaml and research/source_discovery/ with current source, license, identifier, access, and ingestion decisions. Use for broad source-inventory refreshes, not single-source triage or importer implementation.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review Microbial Pathway Sources

Refresh the whole PathwayMech microbial pathway source inventory and leave a
reusable decision trail. This is broader than `source-triage`, which answers
"should we ingest this one source next?"

## Read First

- `conf/sources.yaml`
- `research/source_discovery/microbial_pathway_sources.md`
- `research/source_discovery/pathway_element_identifier_sources.md`
- `research/source_discovery/current_open_source_ingest_triage.md`
- `docs/HARMONIZATION.md`
- `.claude/skills/source-triage/SKILL.md`

## Scope

Keep the review centered on source data that could define, ground, or
taxonomically support microbial pathways for:

- bacteria
- archaea
- fungi
- algae
- protists

Do not promote a source solely because it annotates enzymes, genes, compounds,
metabolites, genomes, or expression. A candidate needs at least one of:

- curated pathway topology;
- a Pathway Tools, BioPAX, KGML, GPML, SBML, JSON, TSV, RDF, or rule format
  that can be mapped to pathway elements;
- organism-specific pathway membership that helps choose a pathway record from
  another topology source;
- a crosswalk that grounds pathway reactions, compounds, proteins, or genes
  into PathwayMech CURIEs.

## Review Loop

1. Fetch current source pages, license pages, and download/API pages for every
   row in `conf/sources.yaml`.
2. Search for new or changed microbial pathway sources in each neglected taxon
   slice, especially fungal, algal, archaeal, and protist resources.
3. Before adding a source ID or declaring a source absent, search with:

   ```bash
   rg --no-ignore --hidden -n "<source-id|label|native-prefix>" . -g '!/.git' -g '!/.venv'
   ```

4. Classify every credible source by:

   - microbial taxon scope;
   - native pathway, reaction, compound, enzyme, gene, and taxon identifiers;
   - exact data formats and endpoints;
   - license URL and redistribution blocker;
   - whether the source is primary topology, a reaction reference, an organism
     membership layer, a crosswalk, or only a model/fixture;
   - the smallest canary pathway or BGC record that could test ingestion;
   - the reason it is active, support-only, fixture-only, license-gated, or
     deferred.

5. Rank sources by PathwayMech curation value, not fame:

   1. curated microbial pathway topology with stable element IDs;
   2. open, machine-readable formats;
   3. taxon coverage that fills bacteria, archaea, fungi, algae, or protist
      gaps not already covered by active importers;
   4. exact links to accepted CURIE prefixes;
   5. permissive redistribution terms;
   6. implementation effort.

6. Update `research/source_discovery/microbial_pathway_sources.md` first, then
   fold the durable rows into `conf/sources.yaml`.

## Inventory Rules

- Keep `conf/sources.yaml` sorted by `priority`.
- Use stable lower-case IDs.
- Keep one concise row per source.
- Use `enabled: true` only for implemented sources or support sources the code
  can currently consume.
- Keep source details in `research/source_discovery/`, not in YAML notes.
- Leave sources disabled when license, native ID, redistribution, or parser
  blockers still require a decision.
- Put aggregators and model corpora in a deferred/crosswalk table unless they
  expose canonical microbial pathway definitions.

## Handoffs

Use `.claude/skills/source-triage/SKILL.md` after this review when one source
needs a detailed next-ingest decision. Do not download bulk archives, write an
extractor, or mark a candidate active as part of this broad landscape refresh.

## Verify

After editing source inventory, source-discovery notes, or this skill, run:

```bash
just seed
just validate
just test
just lint
git diff --check
```

## Report

Summarize:

- source rows changed in `conf/sources.yaml`;
- sources added, demoted, or deferred;
- new license/access/identifier blockers;
- the top two next sources or why no source outranks the active queue;
- validation commands run and their results.
