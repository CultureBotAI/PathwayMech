# Additive Table III correction

The first independent review missed a real description defect: the F6P experiment's E4P cell is **blank / not determined**, not “not detected.” This is additional minor finding ATP-SCI-004, issue453. The exact primary cell is `/article/body/sec[2]/sec[6]/table-wrap/table/tbody/tr[11]/td[6]`; the footnote defines blank versus ND.

The earlier advisory also mischaracterized the no-metabolite column. Its S7P, SBP, DHAP and E4P cells are **all ND**; F6P and FBP are blank/not determined. Six preparations still means the combined S7P experiment plus five controls, so the YAML five-controls count itself is valid.

This receipt corrects those interpretations and acknowledges the missed finding. All89 files in the earlier sealed review remain unchanged. No second full-record review, maintained-file change or Git mutation is claimed. Exact cell/header/footnote proof and the current erroneous description are in `table-proof.json`; bounded remediation and preserved history are in `correction-receipt.json`.
