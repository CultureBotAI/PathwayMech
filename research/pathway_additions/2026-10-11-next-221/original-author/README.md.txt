# Pathway mechanism research: Ethylmalonyl pathway

## Pathway scope

External author draft for **KEGG:M00373**, with all 14 issued reaction rows and all 12 mandatory orthology groups (13 KOs). The complete route forms malate and succinyl-CoA from three acetyl-CoA, CO2 and bicarbonate. Exact protein work is scoped to strain 2.4.1/DSM158; AM1 findings retain their own scope.

This is an author handoff, not an independent review or production ingestion approval. Root authorization is bound in `authorization.json`.

## Mechanistic summary

The seven-step ethylmalonyl segment supplies mesaconyl-CoA. Hydration and Mcl1 cleavage split the route into glyoxylate and propionyl-CoA branches. Mcl1 condenses glyoxylate with a third acetyl-CoA, and Mcl2 hydrolyzes the resulting malyl-CoA. The propionyl branch includes both carboxylase subunits, epimerase and methylmalonyl-CoA mutase through succinyl-CoA.

The distinct native MetaCyc PWY-5741 definition remains held: its terminal reverse ligase would form ATP. Its eleven-member definition and separately linked three-reaction propionyl branch remain fully accounted for in inherited preflight and `source-projections/coverage.json`.

## Evidence table

| Step | Issued reaction | Directional Rhea | Protein/assembly disposition |
| --- | --- | --- | --- |
| 1 | R00238 | RHEA:21037 | UniProtKB:Q3IZW1; tier in scientific ledger |
| 2 | R01977 | RHEA:45798 | UniProtKB:Q3IZW0 / RSP_0747; withheld |
| 3 | R03027 | RHEA:17850 | UniProtKB:Q3J425 / RSP_2305; withheld |
| 4 | R09291 | RHEA:28084 | UniProtKB:Q3IZ91; tier in scientific ledger |
| 5 | R09979 | RHEA:59730 | UniProtKB:Q3IZP4; tier in scientific ledger |
| 6 | R09292 | RHEA:45577 | UniProtKB:Q3IZ90; tier in scientific ledger |
| 7 | R09293 | RHEA:45029 | UniProtKB:D3JV03; tier in scientific ledger |
| 8 | R05076 | RHEA:38265 | UniProtKB:Q3IZ78; tier in scientific ledger |
| 9 | R00934 | RHEA:38260 | UniProtKB:Q3J5L6; tier in scientific ledger |
| 10 | R00473 | RHEA:16631 | UniProtKB:Q3J5L6; tier in scientific ledger |
| 11 | R10612 | RHEA:38292 | UniProtKB:D3JV05; tier in scientific ledger |
| 12 | R01859 | RHEA:23721 | UniProtKB:Q3J4D9, UniProtKB:Q3J4E3; tier in scientific ledger |
| 13 | R02765 | RHEA:20555 | UniProtKB:Q3IZP4; tier in scientific ledger |
| 14 | R00833 | RHEA:22889 | UniProtKB:Q3J4D7; tier in scientific ledger |

Every graph edge has a located assertion and a locally declared reference in the candidate YAML. `source-projections/reference-bindings.json` binds all reference originals. `scientific-ledger.json` separates primary experiments, current reviewed annotations, automatic assignments and unresolved claims.

## Gaps

- Exact first reductase and crotonase protein assignments remain unresolved; both chemical reactions are included. The thiolase and carboxylase alpha assignments retain automatic-evidence tiers.
- The 2008 mutase and 2009 Mcd papers remain abstract-only here. Detailed assembly/cofactor claims cite inspected current reviewed databases; they are not presented as inspected primary pages.
- Native 548-aa Mcd D3JV03/ADC44452.1 matches the deposited strain2.4.1 coding sequence. The 555-aa Q3J5V7 counterpart has seven additional N-terminal residues; no explanation is inferred. Purification tags have separate construct scope.
- ETF's formal whole-protein Rhea equation is distinct from the observed two one-electron reductions. Native CPD9409 stereochemistry and AM1 R/S assay wording conflicts remain explicit.
- Mcl2 dimer/trimer is unresolved; MCM/PCC assembly annotations are inferred. Metal alternatives and assay conditions are not physiological occupancy claims.
- PccR regulation is indirect through pccB expression; direct binding and a propionyl-CoA ligand remain unsupported.
- Four native complex authorities require a production Protein XML acquisition/parser step. `authority-proposal.json` is independently extracted author material; production canonical rebuild remains pending. Failed HTML bodies are preserved.

## Candidate YAML

The complete standalone candidate is `draft/ethylmalonyl-coa-pathway.yaml`. It contains 14 reactions, 50 participants, 105 edges and 44 references. The original-source replay, proposal canonical gate, closed schema, page and KGX checks are reported in `author-checks.json`; they are not an independent scientific review. Broad originals and full derived text remain external. Maintained history, full-corpus checks, review, Git and publication are root integration work.

## Reproduction

Use the existing Python at `/private/tmp/pathwaymech-next-195-20261011/.venv/bin/python`; never synchronize environments. `runtime-source-binding.json` records the actual imported source bytes, since the root's 220 checkout moved during Calvin work. `project-identities.py`, `build-draft.py`, `build-authority.py` and `replay-author.py` are external-only author tools. The draft's Rhea component labels use the independently extracted authority proposal when present, or the complete original Rhea RDF for a fresh reconstruction.
