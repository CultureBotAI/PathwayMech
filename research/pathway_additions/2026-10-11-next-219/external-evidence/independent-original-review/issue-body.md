# Denitrification: two bounded provenance corrections

Review target: `b904248ef7c83cf39f2400075ca57b18a49cda1b87376d16d8c6c6e1b9b6e759`; helper: `4ceae4866d3bf58e2f8754aa35985a7d65a29f7bde82004980604c0fd9b0851c`. External draft, no maintained edits or canonical approval.

1. **Anr experiment locator (minor).** `denitrification-edge-063`, evidence 1, cites PMID:17400734 Results paragraph 1 for a statement that also includes motif mutation. The original `PMC1913380.html` paragraph 1 contains mutant/complementation results; paragraph 2 contains the Anr-box nucleotide exchanges and resulting loss of reporter activity. Include both exact paragraphs, updating the corresponding projection and regression. The biological expression-level assertion remains supported.

2. **NarK1 localization source scope (minor).** `denitrification-edge-074`, evidence 0, attributes “cell/inner membrane” to G3XD60 `/comments/0`. The authentic comment says only “Membrane” and “Multi-pass membrane protein”, with ARBA inference. Its GO cross-reference is generic membrane GO:0016020. Narrow the source-local wording and separately ground the more specific GO:0005886 edge, or use a source-supported location. This does not refute NarK1 physiology; it corrects the evidence attribution.

Acceptance requires source-specific checks for the corrected assertions/locators, a bounded recorded delta, and preserved original target, helper, projection and initial observations. All five native transformations and the documented transport-mode uncertainty must remain.

Exact original body paths/hashes, selected comments and stable finding keys are in `initial-findings.json`. No correction has been applied by this reviewer.
