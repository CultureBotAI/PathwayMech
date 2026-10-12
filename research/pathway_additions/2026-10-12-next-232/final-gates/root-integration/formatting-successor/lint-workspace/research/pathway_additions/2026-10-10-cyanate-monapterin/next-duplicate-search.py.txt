"""Ignored-inclusive exact and semantic candidate search with reviewable receipts."""

import json
import subprocess
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOTS = [
    Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/PathwayMech"),
    Path("/private/tmp/pathwaymech-cyanate-monapterin-20261010"),
]
GROUPS = {
    "citrate_lyase_activation": [
        "SMP0002087",
        "PW002075",
        "P2-PWY",
        "citrate lyase activation",
        "citrate.lyase.*prosthetic",
        "prosthetic.*citrate.lyase",
        "P77231",
        "P0A6G5",
        "P77390",
        r"\bcitG\b",
        r"\bcitX\b",
        r"\bcitC\b",
        "RHEA:15117",
        "RHEA:16333",
        "RHEA:23788",
        "RHEA-COMP:10157",
        "RHEA-COMP:10158",
        "RHEA-COMP:13710",
        "10924139",
        "11042274",
        "10.1021/bi000401r",
        r"10\.1016/[sS]0014-5793\(00\)02105-0",
    ],
    "allantoin_anaerobic_oxamate": [
        "SMP0002064",
        "PW002050",
        "PWY0-41",
        "allantoin degradation",
        "oxamate",
        "oxalurate",
        "oxamic transcarbamylase",
        "P77671",
        "P77425",
        "P75713",
        "P77555",
        "P37306",
        "Q47208",
        "P77129",
        "P0AAS5",
        r"\ball[BCDEFGHK]\b",
        r"\ballFGH\b",
        r"\bylb[EF]\b",
        r"\bybcF\b",
        "RHEA:22984",
        "RHEA:22986",
        "RHEA:15329",
        "RHEA:27485",
        "RHEA:25241",
        "RHEA:10152",
        "RHEA:10154",
        "38888336",
        "41016821",
        "36384810",
        "23284870",
        "10.1128/aem.00957-24",
        "10.4014/jmb.2507.07057",
    ],
    "succinate_propanoate_cycle": [
        "SMP0002070",
        "PW002058",
        "SMP0002069",
        "PW002057",
        "PWY0-43",
        "succinate to propan",
        "succinate to propion",
        "sleeping beauty",
        "P27253",
        "P52045",
        "P52043",
        r"\bscp[ABC]\b",
        r"\bsbm\b",
        r"\bygf[GH]\b",
        "RHEA:22888",
        "RHEA:27666",
        "RHEA:28010",
        "10769117",
        "18950999",
        "10.1021/bi992888d",
        "10.1016/j.micres.2008.08.006",
    ],
    "methylglyoxal_overlap": [
        "SMP0002125",
        "PW002113",
        "methylglyoxal",
        "lactoylglutath",
        "PWY-901",
    ],
}


def main():
    rows = []
    for root in ROOTS:
        for group, patterns in GROUPS.items():
            cmd = [
                "rg",
                "--no-ignore",
                "--hidden",
                "--json",
                "-i",
                "-g",
                "!.git/**",
                "-g",
                "!.venv/**",
                "-g",
                "!**/__pycache__/**",
            ]
            for pattern in patterns:
                cmd.extend(["-e", pattern])
            cmd.append(".")
            result = subprocess.run(cmd, cwd=root, text=True, capture_output=True, check=False)
            assert result.returncode in {0, 1}, result.stderr
            matches = []
            for line in result.stdout.splitlines():
                item = json.loads(line)
                if item["type"] == "match":
                    data = item["data"]
                    content = data["lines"].get("text", "")
                    matches.append(
                        {
                            "path": data["path"].get("text"),
                            "line": data["line_number"],
                            "text": content[:500].rstrip(),
                            "text_truncated": len(content) > 500,
                        }
                    )
            rows.append(
                {
                    "root": str(root),
                    "group": group,
                    "patterns": patterns,
                    "command": cmd,
                    "exit_code": result.returncode,
                    "file_match_counts": dict(sorted(Counter(m["path"] for m in matches).items())),
                    "matches": matches,
                }
            )
    receipt = {
        "checked_at": datetime.now(UTC).isoformat(),
        "ignored_hidden_included": True,
        "exclusions": ["Git internals", ".venv", "__pycache__"],
        "note": (
            "All matching text files and line numbers retained; long individual lines capped at "
            "500 characters. Binary archives are separately parsed for selected native members. "
            "Current next-* research artifacts are included and identified as this pass, "
            "not prior records."
        ),
        "searches": rows,
    }
    (OUT / "next-duplicate-searches.json").write_text(json.dumps(receipt, indent=2) + "\n")
    for row in rows:
        print(
            row["root"],
            row["group"],
            len(row["matches"]),
            [p for p in row["file_match_counts"] if p.startswith("./data/pathways/")],
        )


if __name__ == "__main__":
    main()
