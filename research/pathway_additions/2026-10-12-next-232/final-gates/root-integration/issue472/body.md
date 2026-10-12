Independent review of the external issue471 formatting bridge found that its helper-binding verification loop accepted an incomplete `bridge.files` list. Isolated controls demonstrated that an empty list, omission of `common.py`, or duplication of `run-gates.py` in place of `preserve-maintained.py` bypassed complete helper coverage.

Require exactly three unique relative paths (`common.py`, `run-gates.py`, `preserve-maintained.py`) before checking each bound body. Retain the original failing controls and independently replay all controls against the corrected helper before root accepts or uses it. No maintained source, record, cache or history has been changed by this bridge yet.

Finding: `NAD-FORMATTING-BRIDGE-001`. The original probe and correction will be archived with the NAD addition dossier, together with issue471 and the actual full gate rerun.
