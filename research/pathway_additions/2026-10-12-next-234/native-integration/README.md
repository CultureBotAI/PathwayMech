# Actual local integration evidence

Root adopted the separately reviewed complete PWY-7545 proposal against exact local THIO commit 8c871a5808c73b0f21a397a2561269d068ee7368. Native record and infrastructure histories preceded SSSOM export and page rendering.

All nine required gates passed: render, skills, strict validation, 3,705 tests (three skips and three dependency warnings), lint, KGX export, canonical vendored-file comparison, diff whitespace, and page freshness. The initial vendored attempt failed at sandbox DNS resolution. Its exact failed streams remain under gates/remaining-gates; gates/network-resumption contains the successful public-read retry and the two subsequent checks. Successful tests were not rerun for that network failure.

root-storage-map.json maps every retained external artifact to its durable repository owner and hashes both original and stored bytes. Compressed files are exact gzip transport, including historical Python helpers, streams and the SVG. The native gate receipts retain their actual external execution paths and times; those paths do not imply the temporary checkout is a publication artifact.

visual/ contains exact rendered SVG and PNG observations. The graph has 49 visual nodes and 69 arrows, with a complete evidence table. Dense junction labels remain a static readability limitation. No interactive browser test is claimed.

independent-qa/ is the separately reviewed preservation and native-review preparation packet. The original scientific review is retained by the parent dossier's portable evidence index; technical gates alone are not scientific validation. Native structured reviews are saved separately through scripts/record_review.py.

This is a local integration. Public push, PR and merge are not established by these receipts. No claim of source exhaustion or unrestricted redistribution is made.
