Stable finding key: `nad-authority-relocation-narrative`

The sealed NAD authority-preparation README says its PathBank relocation record includes an actual missing-parent error. Independent audit identified a minor narrative mismatch, which root confirmed by reading the complete saved observation.

The authoritative `pathbank-relocation-observation.json` records the hidden/ignored/followed parent inventory completing with exit code 0, empty stderr and three existing files. The historical ZIP path itself was absent. The existing canonical-cache ZIP is hash-identical to the retained whole original and was reused read-only. There is no demonstrated corruption or new-download provenance issue.

Acceptance criteria:
- State that the old ZIP path was absent while its parent inventory succeeded.
- Preserve the sealed original README and observation unchanged, with an explicit linked successor/addendum explaining the correction.
- Carry the corrected statement and original lineage into maintained finalization/provenance documentation before publication.
- Reconfirm the correction in the independent authority review; no scientific graph, source body, authority object or identifier change is required.

The authority proposal and full scientific review remain under independent review. This issue tracks a documentation correction, not acceptance of the broader proposal.
