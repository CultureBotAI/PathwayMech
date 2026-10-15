The new `data/pathways/catechol-degradation-i.yaml` draft on `feat/pathway-next-261-20261014` says that AdhE is excluded by PWY-5162. The original MetaCyc `enzymes-not-used` slot identifies only `MetaCyc:ADHE-CPLX`, whose source organism is E. coli K-12 MG1655. The same record intentionally retains distinct Clostridium and Bilophila proteins named AdhE as component context, so the opening sentence is too broad.

Independent technical finding: `catechol-i-adhe-exclusion-instance-scope` (minor), review `20261015T024904Z-next261-technical-initial`, F1. Reviewed record SHA-256: `38b3460b24131e7ee2d442e23d226618557bbc5ba56181d7ef9de9ac9e2a0255`.

Original evidence: `/ptools-xml/Pathway[@frameid="PWY-5162"]/enzymes-not-used[1]` (SHA-256 `267048b17a4e31be301718597cebe9ec75f508fa606f53885bcf9f8a985f5bea`) and `/ptools-xml/Protein[@frameid="ADHE-CPLX"]/species[1]` (SHA-256 `ac3c056c5ea023311235a9c47e25085b06a09c556e9a662c747723fd8d0f8b3b`). The graph already excludes the correct instance.

Acceptance:

- Name E. coli ADHE-CPLX in the maintained description without broadening the exclusion to unrelated AdhE proteins.
- Preserve all other graph claims; retain a separate disposition for any other review repair.
- Regenerate pages, pass the required repository checks, and save an evidence-backed successor review resolving F1.
