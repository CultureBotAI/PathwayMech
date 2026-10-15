# Decoder native-lint correction

Issue [606](https://github.com/CultureBotAI/PathwayMech/issues/606) records the
single E501 failure in the final source-documentation gate. Native validation
passed; lint failed; diff and final preservation did not run in that attempt.
The complete failed attempt is preserved in `failed-native-gates/`.

The correction splits one path literal with implicit concatenation. The complete
module AST is identical. `correction.json` binds both decoder and payload-manifest
versions. All 5,967 other payload files, source bytes and content maps are unchanged.
The preserved predecessor report and decoder retain their original observations.
Prior successful decoder execution is reused through AST identity; it is not
represented as a fresh execution. Independent final review and successor native
gates record their later observations separately.
