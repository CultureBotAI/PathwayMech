# YAML Record Review: adenosine deoxyribonucleotides de novo biosynthesis II

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech`
- Record: `data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml`
- Started UTC: 2026-09-25T10:45:40Z
- Finished UTC: 2026-09-25T10:45:40Z
- Verdict: PASS - no blocker, major, or minor findings

## Target

- Current branch: `add-gocam-pwy-7220`
- Maintained pathway id: `gomodel:YeastPathways_PWY-7220-1`
- Maintained label: `adenosine deoxyribonucleotides de novo biosynthesis II`
- Pathway type: `nucleotide-biosynthesis`
- Maintained local scope: 1 taxon, 13 participants, 4 reactions, 24 mechanistic edges, 1 reference
- Raw Noctua source checked: `/private/tmp/gocam-noctua/YeastPathways_PWY-7220-1.json`
- Compact SGD GO-CAM source checked: `/private/tmp/sgd-yeast-gocams/YeastPathways_PWY-7220-1.json`
- Exhaustive repository searches before absence checks used `rg --no-ignore --hidden` over `.` while excluding `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.

## Validation

- `just validate`: passed; validated 5 Claude skills, 91 pathway records, 3,527 evidence blocks, 12 source records, 6 documentation files, and the deep-research report contract.
- `just test`: passed; 34 tests passed.
- `just lint`: passed; Ruff reported `All checks passed!`.
- `git diff --check`: passed.
- Skipped validators: None.

## Identity and Grounding

- The exact repository search for `PWY-7220-1`, including ignored and hidden files except `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`, found one maintained YAML record plus its generated browse and record pages.
- The filename-safe slug search for `adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii` found exactly `data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml`.
- The raw Noctua JSON id is `gomodel:YeastPathways_PWY-7220-1`; its title annotation is `adenosine deoxyribonucleotides <i>de novo</i> biosynthesis II - imported from: Saccharomyces Genome Database`.
- The compact SGD GO-CAM id is also `gomodel:YeastPathways_PWY-7220-1`; its title is the same SGD-imported pathway title.
- The maintained record's one taxon, `NCBITaxon:559292` / `Saccharomyces cerevisiae S288C`, matches the raw Noctua `biolink:in_taxon` annotation and the compact SGD GO-CAM `taxon` value.
- The maintained `gomodel` pathway id denotes the exact SGD GO-CAM model supplied for `PWY-7220-1`, not a sibling pathway, broad parent, or a single reaction.

## Graph and Local References

- Every `mechanistic_edges` subject and object resolves locally to the record id or a declared participant or reaction.
- Every maintained predicate is in `ALLOWED_EDGE_PREDICATES`.
- Every evidence block cites the record's single declared reference, `gomodel:YeastPathways_PWY-7220-1`.
- All 47 maintained evidence quotes are exact substrings of the raw Noctua JSON.
- The generated page `pages/records/gomodel_YeastPathways_PWY-7220-1.html` lists all 24 YAML edges in order.
- The generated browse entry links to `records/gomodel_YeastPathways_PWY-7220-1.html` and reports `24 mechanistic edges`.

## Edge Evidence

- Edges `edge-001` through `edge-006` are supported by the raw `gomodel:ADPREDUCT-RXN` activity: CPX-1102 enables it, `CHEBI:15967` and `CHEBI:456216` are inputs, and `CHEBI:57667`, `CHEBI:18191`, and `CHEBI:15377` are outputs.
- Edges `edge-007` through `edge-012` are supported by the raw `gomodel:YeastPathways_PWY-7220-1/6a2b236300005372` activity: CPX-1103 enables it, `CHEBI:15967` and `CHEBI:456216` are inputs, and `CHEBI:57667`, `CHEBI:18191`, and `CHEBI:15377` are outputs.
- Edges `edge-013` through `edge-017` are supported by the raw `gomodel:DADPKIN-RXN` activity: YNK1 enables it, `CHEBI:57667` and `CHEBI:30616` are inputs, and `CHEBI:456216` and `CHEBI:61404` are outputs.
- `edge-018` is supported by the raw-only causal fact `gomodel:DADPKIN-RXN RO:0002411 gomodel:RXN0-745`.
- Edges `edge-019` through `edge-024` are supported by the raw-only `gomodel:RXN0-745` activity: `CHEBI:30616`, `CHEBI:15740`, and `CHEBI:15378` are inputs, and `CHEBI:16526`, `CHEBI:15377`, and `CHEBI:61404` are outputs.
- The compact SGD activity list has only three activities, `gomodel:ADPREDUCT-RXN`, `gomodel:YeastPathways_PWY-7220-1/6a2b236300005372`, and `gomodel:DADPKIN-RXN`; its omission of `gomodel:RXN0-745` is lossy rather than evidence against the maintained raw-only branch.

## Completeness

- The raw Noctua graph has 32 facts.
- The record captures all 24 non-BFO raw facts as mechanistic edges.
- The only raw facts not represented as YAML `mechanistic_edges` are the eight `BFO:0000050` part-of and `BFO:0000066` occurs-in facts for `gomodel:ADPREDUCT-RXN`, `gomodel:YeastPathways_PWY-7220-1/6a2b236300005372`, `gomodel:DADPKIN-RXN`, and `gomodel:RXN0-745`.
- Omitting those BFO facts is appropriate for the current local schema because `BFO:0000050`, `BFO:0000066`, and the raw `GO:0005829` location nodes cannot be encoded with the maintained `mechanistic_edges` predicate set.

## Findings

None found.

## Recommended Edits

None found.

## Follow-up Checks

None found. The relevant full-corpus checks already pass:

- `just validate`
- `just test`
- `just lint`
- `git diff --check`

## Additional Notes

- Exact `PWY-7220-1`, exact label, exact slug, and exact `RXN0-745` searches were gitignore-independent and covered hidden files while excluding only `.git`, `.venv`, `.pytest_cache`, and `.ruff_cache`.
- The maintained `RO:0002411` causal edge intentionally depends on the raw Noctua JSON; reviewers must not remove it merely because the compact SGD GO-CAM activity list omits `gomodel:RXN0-745`.
