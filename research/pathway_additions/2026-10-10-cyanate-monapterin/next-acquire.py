"""Reproduce the bounded next-candidate source acquisition; raw bytes stay external."""

import json
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

OUT = Path(__file__).resolve().parent
RAW = Path("/private/tmp/pathwaymech-cyanate-monapterin-evidence/next")
ARCHIVE = Path(
    "/private/tmp/pathwaymech-pathbank-dbcan-evidence/pathbank/pathbank_primary_biopax.zip"
)
RAW.mkdir(parents=True, exist_ok=True)
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"


def acquire(item):
    name, url = item
    receipt = {"file": name, "url": url, "retrieved_at": datetime.now(UTC).isoformat()}
    try:
        with urlopen(
            Request(url, headers={"User-Agent": "PathwayMech source research"}), timeout=60
        ) as response:
            data = response.read()
            receipt.update(
                status=response.status,
                resolved_url=response.url,
                headers={
                    k: v
                    for k, v in response.headers.items()
                    if k.lower()
                    in {
                        "content-type",
                        "last-modified",
                        "etag",
                        "x-uniprot-release",
                        "x-uniprot-release-date",
                    }
                },
            )
        (RAW / name).write_bytes(data)
        receipt.update(path=str(RAW / name), bytes=len(data), sha256=sha256(data).hexdigest())
    except Exception as error:
        receipt["error"] = str(error)
    return receipt


def main():
    archive_sha = sha256(ARCHIVE.read_bytes()).hexdigest()
    assert archive_sha == "b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44"
    projections = []
    receipts = []
    with zipfile.ZipFile(ARCHIVE) as archive:
        for name in [
            "PW002050.owl",
            "PW002058.owl",
            "PW002075.owl",
            "PW002057.owl",
            "PW002113.owl",
        ]:
            data = archive.read(name)
            (RAW / name).write_bytes(data)
            objects = []
            for element in ET.fromstring(data):
                objects.append(
                    {
                        "type": element.tag.rsplit("}", 1)[-1],
                        "id": element.get(RDF + "ID") or element.get(RDF + "about"),
                        "properties": [
                            {
                                "predicate": child.tag.rsplit("}", 1)[-1],
                                "text": child.text,
                                "attributes": dict(child.attrib),
                            }
                            for child in element
                        ],
                    }
                )
            projections.append(
                {"member": name, "sha256": sha256(data).hexdigest(), "objects": objects}
            )
            receipts.append(
                {
                    "file": name,
                    "path": str(RAW / name),
                    "bytes": len(data),
                    "sha256": sha256(data).hexdigest(),
                    "archive_sha256": archive_sha,
                    "url": "https://pathbank.org/downloads/pathbank_primary_biopax.zip",
                    "version": "preserved primary archive; Last-Modified 2019-08-16",
                }
            )
    (OUT / "next-native-projections.json").write_text(json.dumps(projections, indent=2) + "\n")
    proteins = [
        "P77231",
        "P0A6G5",
        "P77390",
        "P27253",
        "P52045",
        "P52043",
        "P77671",
        "P77425",
        "P75713",
        "P77555",
        "P37306",
        "Q47208",
        "P77129",
        "P0AAS5",
    ]
    urls = [(f"uniprot-{p}.json", f"https://rest.uniprot.org/uniprotkb/{p}.json") for p in proteins]
    for pmc in ["PMC11326118", "PMC12535856", "PMC2741639"]:
        urls.append(
            (f"{pmc}.xml", f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML")
        )
    for query in [
        "EXT_ID:10924139 AND SRC:MED",
        'TITLE:"Identification of triphosphoribosyl-dephospho-CoA"',
        'TITLE:"Discovering new enzymes and metabolic pathways"',
        "EXT_ID:38888336 AND SRC:MED",
        'TITLE:"Dual Regulation of the allF Operon"',
    ]:
        urls.append(
            (
                f"pubmed-query-{len(urls)}.json",
                "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
                + urlencode(
                    {"query": query, "format": "json", "resultType": "core", "pageSize": 10}
                ),
            )
        )
    for identifier in ["PWY0-43", "PWY0-41", "P2-PWY"]:
        urls.append(
            (
                f"metacyc-{identifier}.xml",
                f"https://pathway.yeastgenome.org/getxml?META:{identifier}",
            )
        )
    for pmid in ["36384810", "23284870", "18950999"]:
        urls.append(
            (
                f"pubmed-{pmid}.json",
                "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
                + urlencode(
                    {"query": f"EXT_ID:{pmid} AND SRC:MED", "format": "json", "resultType": "core"}
                ),
            )
        )
    urls.append(
        (
            "PMC3527362.xml",
            "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3527362/fullTextXML",
        )
    )
    with ThreadPoolExecutor(max_workers=5) as pool:
        receipts.extend(pool.map(acquire, urls))
    (OUT / "next-source-manifest.json").write_text(json.dumps(receipts, indent=2) + "\n")
    print(json.dumps({"sources": len(receipts), "failures": [r for r in receipts if "error" in r]}))


if __name__ == "__main__":
    main()
