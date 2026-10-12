from __future__ import annotations

from pathlib import Path

from pathwaymech.chebi import load_chebi_xrefs
from pathwaymech.source_mapping import CurieMapping

FIXTURE = Path("tests/fixtures/chebi/kegg_compounds.obo")


def test_chebi_obo_maps_supported_xrefs_to_chebi() -> None:
    assert load_chebi_xrefs(FIXTURE) == {
        "CAS:98-92-0": CurieMapping(
            subject_id="CAS:98-92-0",
            subject_label="CAS:98-92-0",
            object_id="CHEBI:17154",
            object_label="nicotinamide",
        ),
        "ChemSpider:555": CurieMapping(
            subject_id="ChemSpider:555",
            subject_label="ChemSpider:555",
            object_id="CHEBI:17154",
            object_label="nicotinamide",
        ),
        "HMDB:HMDB0000902": CurieMapping(
            subject_id="HMDB:HMDB0000902",
            subject_label="HMDB:HMDB0000902",
            object_id="CHEBI:17154",
            object_label="nicotinamide",
        ),
        "KEGG:C00197": CurieMapping(
            subject_id="KEGG:C00197",
            subject_label="2-phospho-D-glycerate",
            object_id="CHEBI:58289",
            object_label="2-phosphonato-D-glycerate(3-)",
        ),
        "KEGG:C00236": CurieMapping(
            subject_id="KEGG:C00236",
            subject_label="3-phospho-D-glycerate",
            object_id="CHEBI:58272",
            object_label="3-phosphonato-D-glycerate(3-)",
        ),
        "PubChem:647": CurieMapping(
            subject_id="PubChem:647",
            subject_label="PubChem:647",
            object_id="CHEBI:17154",
            object_label="nicotinamide",
        ),
    }
