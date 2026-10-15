# Bounded existing-record correction for issue 558

Authored the requested correction in only these maintained files:

- `data/pathways/gallate-degradation-i.yaml`
- `data/pathways/protocatechuate-meta-cleavage.yaml`

Each now records RHEA:28932 as `left_to_right`, RHEA:17403 as `right_to_left`, and RHEA:28936 as `left_to_right`. The hydration member RHEA:17403 is right-to-left relative to master RHEA:17401; its own displayed equation and existing material edges still express CHM + water to CHA.

Eight gallate I material-edge descriptions and three protocatechuate membership descriptions now distinguish the separate native MetaCyc REVERSIBLE assertions from issuing Rhea member orientation. The protocatechuate spontaneous-conversion caveat and opposite-native-side hydration context are preserved. No graph endpoint, predicate, coefficient, evidence, qualifier, reference, identifier, label, category, or other claim was changed.

The 17 changed scalar fields are explicitly enumerated in `bounded-fix-proof.json`. Actual pre-edit and post-edit bytes are retained, with unified diffs. Scalar-splice editing preserved every byte outside those exact spans. The proof checks the complete parsed objects against a field whitelist, not just selected graph statistics. It also binds the independent scientist's Rhea-family projection and verifies REVERSIBLE directly in each of the three original MetaCyc reaction XML objects.

Final hashes:

- gallate I: `7edca6dce4346c76f389062d2b181cc685a2f00bcf6cd80941c27d8b9e4ea84e`
- protocatechuate meta-cleavage: `c36339efcbc6aeef084826b2b8a66fcbea46240aeed6c68c0275602fae21ea49`

Both records passed handwritten validation, closed LinkML validation, and a scoped `git diff --check`. This is an authoring package, not independent scientific approval. Root owns final integrated gates, source-normalization decisions, history, pages, reviews, and GitHub workflow.

An incidental observation was sent to root without editing it: gallate I edges native-002 through native-005 also retain generic wording about native reversible metadata for RHEA:28928. That separate original reaction needs checking before any claim of a broader direction audit.
