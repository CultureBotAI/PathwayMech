# Complete staphyloferrin A biosynthesis

This addition represents all three transformations of MetaCyc:PWY-7990, corroborated by KEGG:M00876: ornithine racemization, SfaD N5-citrylation and SfaB N2-citrylation. The record contains 14 participants, 31 edges, 59 evidence entries and 28 references. All 19 named nodes occur in the generated graph and KGX export. Transport, ferric loading, citrate supply and staphyloferrin B lie outside the exact native boundary.

Versioned Newman protein identities remain distinct from engineered experimental preparations and NCTC8325 comparison sequences. SfaC activity and PLP support remain qualified inference; native ligase Mg annotations do not establish metal specificity or binding stoichiometry. Newman SfaD differs from its comparison sequence at residue 532. No unsupported assembly or compartment is asserted.

Native citryl structures leave stereochemistry unspecified. Current ChEBI intermediate and product assignments are explicit chemical-authority conventions; inspected Figure 2 supports ferric receptor-bound product stereochemistry, not a free-intermediate assay. The Cotton article remains abstract-only, Beasley web-only access has no fabricated local body hash, and iModulon context is kept in its actual strain scope with the original parser failure retained.

`portable-replay/staphyloferrin-a-replay.py` is the current executable replay. Top-level author scripts and metadata preserve the historical submission. Four archived scratch/review scripts use `.py.txt`; `archive-packaging-successor.json` maps their historical locations to byte-identical archives. The initial lint failure, subsequent lint pass and independent packaging review remain separate preserved observations. Historical copy and baseline receipts were not rewritten.

From the repository root, supply original source bodies at their hash-bound manifest locations and a new external output path:

```bash
.venv/bin/python research/pathway_additions/2026-10-11-next-214/portable-replay/staphyloferrin-a-replay.py \
  --repo-root . \
  --record data/pathways/staphyloferrin-a-biosynthesis.yaml \
  --source-manifest research/pathway_additions/2026-10-11-next-214/staphyloferrin-a-source-manifest.json \
  --source-projection research/pathway_additions/2026-10-11-next-214/staphyloferrin-a-source-projection.json \
  --stereo-python /absolute/path/to/python-with-rdkit \
  --output /private/tmp/staphyloferrin-a-new-replay.json
```

The replay verified 53 original bodies, 16 chemical sides and three balanced reactions against the installed authorities. It does not itself integrate authorities or replace full-corpus gates and scientific review. Raw source bodies remain external.

Canonical authority integration added two source inputs, seven ontology terms and four source terms while preserving all prior entries. Final coverage is 519 manifest inputs, 1807 ontology terms and 2122 source terms. The integration was prepared on the independently reviewed Petrobactin head; the subsequent actual-merge bridge proves whole-tree equality and preservation of all 75 prepared files.

All final corpus gates ran on the actual Petrobactin merged base. 1256 passed, 3 skipped, 3 warnings in 544.14s (0:09:04). The batch exit was 1 solely because it retains the initial archived-script lint failure; the separately observed lint successor passed. All other gates and all 22 pinned governed artifacts passed. Independent graph/export inspection verifies every prior record, history, review, page and record-scoped KGX context remained unchanged. No record history was added after rendering. This is programmatic artifact inspection; no browser interaction is claimed.

`integration-receipt.json`, `full-gate-receipts.json` and lossless `console-transcripts.json` bind these observations. Final canonical scientific review, remote PR checks, merge and live publication remain separate subsequent steps. More pathway candidates remain.
