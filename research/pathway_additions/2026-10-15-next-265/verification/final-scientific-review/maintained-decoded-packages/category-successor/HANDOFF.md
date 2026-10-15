# PWY-1361 typed reaction category successor

This immutable root-authored successor addresses [issue 578](https://github.com/CultureBotAI/PathwayMech/issues/578), finding NEXT265-TYPED-REACTION-CATEGORY-01. It adds only `category: molecular_activity` to reactions[3], MetaCyc:RXN-2424, as required by the unchanged typed native-reaction consumer. Exact JSON/YAML equality and removal-of-added-field equality to the frozen original both pass. All seven steps, chemistry, 67 edges, 68 references and putative/no-catalyst limitations remain unchanged.

The original integrated-design package and failed consumer remain immutable; this package binds their hashes and preserves the actual failed receipt and unchanged validator. The original chemical-node equality assertion is superseded only for this explicit category field, not chemical identity or reaction content. No broad test, independent acceptance, authority rebuild or maintained-record integration is claimed. The separate actual-corpus consumer and integrated-design reviewer must assess this successor.

A separate bio005 evidence-locator finding remains under review and is not corrected by this category-only package.
