from __future__ import annotations

from pathlib import Path

from pathwaymech.chebi import load_chebi_xrefs

FIXTURE = Path("tests/fixtures/chebi/kegg_compounds.obo")


def test_chebi_obo_maps_supported_xrefs_to_chebi() -> None:
    assert load_chebi_xrefs(FIXTURE) == {
        "CAS:98-92-0": "CHEBI:17154",
        "ChemSpider:555": "CHEBI:17154",
        "HMDB:HMDB0000902": "CHEBI:17154",
        "KEGG:C00197": "CHEBI:58289",
        "KEGG:C00236": "CHEBI:58272",
        "PubChem:647": "CHEBI:17154",
    }
