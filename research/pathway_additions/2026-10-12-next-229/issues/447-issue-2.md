Issue key: `eg-fuco-iron-occupancy-construct-conflation`

Independent scientific review of the pending `MetaCyc:PWY0-1280` ethylene-glycol record found this minor correction. The draft is not yet merged.

eg-025 carries the 0.53 Fe atom/subunit WT solution observation while its sole subject construct qualifier specifies the pQE32/pCM1 N-terminal His6 crystallographic preparation. The body generally mentions a separate cleaved pCM2 preparation, but does not assign this exact solution comparator to it. This leaves the edge-level accompanying observation scoped to the wrong preparation.

Maintained owner on integration: `data/pathways/ethylene-glycol-degradation.yaml`, with its research context/construct dispositions.

Source: [FucO structure and function study, PMID 15995211](https://pmc.ncbi.nlm.nih.gov/articles/PMC1169507/).

Methods assigns WT and mutant preparations for site-directed-mutagenesis studies to GST/factor-Xa cleavage of pCM2; the metal-analysis paragraph reports mutants and WT examined in parallel, including WT 0.53. That comparator is separate from the pCM1 His6 crystal site.

Clarify eg-025 evidence and subject qualifier (or move the supporting solution observation to explicitly qualified context) so the His6 pCM1 crystal site and cleaved pCM2 WT/mutant solution comparison each have their correct source/construct roles. Preserve the value and native cofactor edge; do not invent a simultaneous mixed construct.

Acceptance checks:

- Exact source Methods and Results locators are preserved and independently replayable.
- pCM1/pQE32 His6/M15(pREP4) applies to the crystal evidence; pCM2/pGEX3X factor-Xa-cleaved WT/mutant/BL21 applies to the solution comparison.
- The 0.53 value is not assigned to the His6 crystal preparation or made a universal occupancy.
- No change to Fe-cofactor identity, two core events, original edge identity or reference identities; validate the exact scientific successor and updated construct ledger.

Review packet SHA-256: `41bc34c098e852a3f1e2f13f1f97ec318742a220494603e4e1ee45019a9ac3ec`. Original draft SHA-256: `c24808501b16cc9ad53b1d9c52cd503f0eb5d9be55af4c1406ec6ad47803f704`.

Retain the original review and an independently assessed successor. Close through the eventual integration PR after the correction and required gates pass.
