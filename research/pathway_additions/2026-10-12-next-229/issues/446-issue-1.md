Issue key: `eg-fuco-cu-cd-context-omission`

Independent scientific review of the pending `MetaCyc:PWY0-1280` ethylene-glycol record found this minor correction. The draft is not yet merged.

The selected 2005 source reports earlier Cu(II)/Cd(II) inhibition of FucO, but the candidate and its scope/disposition owners preserve the direct Zn/Fe assay and older Mn alternative without disposing this additional inhibitor context. The existing copper edge eg-035 targets AldA and does not cover FucO.

Maintained owner on integration: `data/pathways/ethylene-glycol-degradation.yaml`, with its research context/construct dispositions.

Source: [FucO structure and function study, PMID 15995211](https://pmc.ncbi.nlm.nih.gov/articles/PMC1169507/).

This sentence reports prior work; Figure 4 itself tests Zn/Fe on His6-FucO, not Cu/Cd.

Add concise source-qualified prose and an explicit dossier disposition stating that the 2005 paper reports prior Cu/Cd inhibition; retain the older primary-access limit and keep the direct Zn/Fe experiment separate. If an original older assay is later acquired, assess it independently before adding any new precise edge.

Acceptance checks:

- Original 2005 paragraph and reference-40 identity remain bound by full-original hash and exact locator.
- Candidate and context ledger explicitly preserve Cu/Cd FucO context with earlier-study/secondary-report wording and abstract-only older-source limit.
- No invented Cu/Cd dose, EG-oxidation IC50, physiological threshold, direct binding, or Fig.4 assay assertion.
- All original 82 edge identities/core chemistry remain unchanged unless separately justified; native schema/strict and exact successor review pass.

Review packet SHA-256: `41bc34c098e852a3f1e2f13f1f97ec318742a220494603e4e1ee45019a9ac3ec`. Original draft SHA-256: `c24808501b16cc9ad53b1d9c52cd503f0eb5d9be55af4c1406ec6ad47803f704`.

Retain the original review and an independently assessed successor. Close through the eventual integration PR after the correction and required gates pass.
