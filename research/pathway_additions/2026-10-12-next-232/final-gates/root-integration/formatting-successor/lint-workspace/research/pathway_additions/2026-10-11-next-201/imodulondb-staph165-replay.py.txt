"""Replay the bounded native fallback without repairing nullable source metadata."""

import argparse
import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--raw", type=Path, required=True)
parser.add_argument("--adapter-src", type=Path, required=True)
args = parser.parse_args()
dossier = Path(__file__).resolve().parent
context = json.loads((dossier / "imodulondb-staph165-context.json").read_text())
fallback = json.loads((dossier / "imodulondb-staph165-native-fallback.json").read_text())
manifest = json.loads((dossier / "imodulondb-staph165-source-manifest.json").read_text())
module = args.adapter_src / "kg_microbe_sources/imodulondb.py"
assert hashlib.sha256(module.read_bytes()).hexdigest() == context["adapter_sha256"]
sys.path.insert(0, str(args.adapter_src))
from kg_microbe_sources.imodulondb import ImodulonDBClient, ImodulonDBError  # noqa: E402

bodies = {}
for item in manifest + fallback["source_manifest"]:
    original = (args.raw / item["file"]).read_bytes()
    assert len(original) == item["bytes"]
    assert hashlib.sha256(original).hexdigest() == item["sha256"]
    assert item["url"] not in bodies
    bodies[item["url"]] = json.loads(original)
used = set()


def transport(url):
    used.add(url)
    return bodies[url]


client = ImodulonDBClient(transport=transport)
normalize = lambda value: json.loads(json.dumps(value))  # noqa: E731
assert normalize([asdict(x) for x in client.organism_datasets()]) == context["datasets"]
successful_queries = 0
for query, expected in context["queries"].items():
    try:
        actual = normalize(asdict(client.search("s_aureus", "staph_precise165", query)))
    except ImodulonDBError as exc:
        assert query == "SigB"
        assert str(exc) == expected["error"] == fallback["initial_search_error"]
    else:
        assert actual == expected
        successful_queries += 1
assert successful_queries == 8
assert bodies[fallback["native_search_source"]["url"]] == fallback["native_search_response"]
try:
    client.imodulon_genes("s_aureus", "staph_precise165", fallback["component"])
except ImodulonDBError as exc:
    assert type(exc).__name__ + ": " + str(exc) == fallback["gene_table_parser_error"]
else:
    raise AssertionError("Expected the recorded nullable-metadata failure")
native_table = bodies[fallback["source_manifest"][0]["url"]]
assert len(native_table["genes"]) == fallback["native_table_rows"]
assert native_table["threshold"] == fallback["native_table_threshold"]
for item in fallback["selected_native_gene_rows"] + [fallback["null_metadata_row"]]:
    assert native_table["genes"][item["array_index"]] == item["native_row"]
assert used == bodies.keys()
print(
    json.dumps(
        {
            "result": "passed within declared scope",
            "original_bodies_replayed": len(bodies),
            "successful_searches": successful_queries,
            "expected_adapter_failures_reproduced": 2,
            "selected_native_rows": len(fallback["selected_native_gene_rows"]),
            "limit": (
                "Reproduces source projections and failures; does not certify a successful "
                "full-table adapter parse or biological mechanism."
            ),
        },
        indent=2,
    )
)
