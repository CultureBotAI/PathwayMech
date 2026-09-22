---
name: add-pathway
description: Add one microbial pathway mechanism as a PathwayMech YAML record with exact identifier checks, local participant and reaction nodes, edge-level evidence, refreshed pages, and local validation. Use for a named pathway or paper lead; use source-triage for reusable database adoption.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add a PathwayMech Record

Turn one named microbial pathway, or one bounded literature lead, into a
validated YAML record under `data/pathways/`.

Search hits, pathway-database pages, and Deep Research reports are leads. Only
inspected primary sources, reviewed pathway definitions, or authoritative
database records should support a committed identifier, participant, reaction,
or mechanistic edge.

## Boundaries

- Add one pathway per task. If a request names a pathway family, split it into
  exact records whose identifiers and edges can be reviewed independently.
- Accept pathways with explicit biochemical, regulatory, biosynthetic, or
  physiological steps in microbes.
- Reject broad umbrella processes, unrelated pathway-map collages, pure
  phenotypes, single reactions, single enzymes, and taxon-level pathway
  predictions that lack mechanistic evidence.
- Do not mark an optional field as absent because the source omits it. This
  schema is intentionally small; leave unsupported nodes and edges out.
- Do not invent a local CURIE. `src/pathwaymech/schema.py` currently accepts
  `GO`, `gomodel`, `WikiPathways`, `MetaCyc`, `KEGG`, `RHEA`, `MIBiG`,
  `ModelSEED`, `BiGG`, `BV-BRC`, `Reactome`, `PathBank`, `CHEBI`, `EC`, `ECO`,
  `SGD`, `UniProtKB`, `NCBITaxon`, `GTDB`, `GO_REF`, `PMID`, and `DOI`.

## Read First

- `CLAUDE.md` for the record contract.
- `docs/CURATION.md` for the curation surface and provenance rule.
- `docs/HARMONIZATION.md` for the identifier sources this corpus harmonizes.
- `templates/pathway_mechanism_research.md` for research reports that can seed
  the first draft.
- `conf/sources.yaml` for sources already considered for ingestion.
- `src/pathwaymech/schema.py` for the required fields, CURIE prefixes,
  predicate enum, and evidence quote length limit.
- The closest records in `data/pathways/`, when any exist. Copy their local
  shape, not their claims.

## Prove the Pathway Is Missing

Before writing a record, search exact identifiers and labels across the whole
repository, including ignored and hidden files:

```bash
rg --no-ignore --hidden -n -F "<GO-or-WikiPathways-or-MetaCyc-or-KEGG-id>" . -g '!/.git' -g '!/.venv'
rg --no-ignore --hidden -n -F "<exact pathway label>" . -g '!/.git' -g '!/.venv'
rg --no-ignore --hidden -n -F "<RHEA-or-MIBiG-or-PMID-or-DOI>" . -g '!/.git' -g '!/.venv'
```

Search the candidate GO, GO-CAM, WikiPathways, MetaCyc, KEGG, Rhea, MIBiG,
Reactome, PathBank, ModelSEED, BiGG, and BV-BRC identifiers; exact pathway
labels and synonyms; defining reaction IDs; source accessions; and DOI or PMID
evidence. Never use a bare prefix such as `GO:` or `PMID:` to prove absence.

If a prior mention exists in `research/`, read it before continuing. A rejected
candidate, source gap, or unresolved identifier conflict changes the work from
record addition to follow-up research.

## Identity and Nodes

Choose the record `id` from the narrowest exact external pathway identifier:

- use `GO` when the biological-process term exactly denotes the pathway;
- use `MetaCyc` or `KEGG` when the database entry is the curated pathway being
  represented;
- do not collapse alternative routes, species-specific variants, or adjacent
  modules merely because they share a display name.

Declare every node used by an edge in one of the local node lists:

- `taxa`: microbial scope with `NCBITaxon` or `GTDB` identifiers;
- `participants`: small molecules, cofactors, enzymes, or proteins with
  `CHEBI`, `EC`, or `UniProtKB` identifiers;
- `reactions`: reaction nodes with `RHEA`, `gomodel`, `WikiPathways`,
  `MetaCyc`, `KEGG`, `Reactome`, or `PathBank` identifiers.

Resolve every CURIE at its issuing authority before committing it. Leave a node
out when the identifier is still a guess; a shorter true graph is better than a
full pathway map with invented accessions.

## Mechanistic Edges

Every edge must:

- use an `id` unique within the record;
- use one of the predicates in `ALLOWED_EDGE_PREDICATES`;
- set `subject` and `object` to the record id or a locally declared taxon,
  participant, or reaction id;
- cite at least one local `references` entry by `reference_id`;
- quote only exact text, at most 400 characters.

Attach evidence to the narrowest edge it supports. A database page can support
identifier equivalence or pathway membership; a primary paper should support
an organism-specific enzyme, reaction direction, regulatory step, or causal
edge. Preserve conflicts by omitting the edge or naming the gap in research,
not by picking whichever source makes the draft complete.

## Write and Verify

Create one YAML file under `data/pathways/`, named with a stable lower-case
ASCII slug for the pathway. Then run:

```bash
just validate
just render-pages
just test
just lint
git diff --check
```

`pages/` is generated from `data/pathways/`. Rebuild it with
`just render-pages`; do not edit generated pathway pages by hand.

## Report

End with the new record id, label, and YAML path; every GO, GO-CAM,
WikiPathways, MetaCyc, KEGG, Rhea, MIBiG, Reactome, PathBank, ModelSEED, BiGG,
BV-BRC, ChEBI, EC, UniProtKB, NCBITaxon, GTDB, PMID, and DOI identifier added;
the strongest identity and mechanism sources; any edges deliberately left out;
whether duplicate searches included ignored and hidden files; and every
validation command that passed or was unavailable.
