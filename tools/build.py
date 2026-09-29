#!/usr/bin/env python3
"""Regenerate derived files from the product CSVs.

Produces:
  * data/cisco_all_products.csv  - all product rows merged, in PREFIXES order
  * README.md                    - the per-file row-count table and per-product
                                   markdown tables between the AUTO-GENERATED markers

Only the marked regions of README.md are rewritten; all prose is left untouched.

Usage:
    python3 tools/build.py            # write files
    python3 tools/build.py --check    # verify derived files are current, write nothing
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
README = ROOT / "README.md"

# Ordered so the merged file is stable and matches the documented ID ordering.
FILES: list[tuple[str, str, str]] = [
    # (filename stem, display name, ID prefix)
    ("cisco_campus_switching", "Campus Switching", "CSW"),
    ("cisco_dc_switching", "DC Switching", "DCW"),
    ("cisco_enterprise_routing", "Enterprise Routing", "ERT"),
    ("cisco_sp_routing", "SP Routing", "SPR"),
    ("cisco_wireless", "Wireless", "WLS"),
    ("cisco_security", "Firewalls", "FWL"),
    ("cisco_sdwan", "SD-WAN", "SDW"),
    ("cisco_software", "Management & Software", "SFT"),
    ("cisco_sp_extended", "SP Extended", "SPX"),
    ("cisco_collaboration", "Collaboration", "CLB"),
    ("cisco_meraki", "Meraki", "MRK"),
    ("cisco_dc_compute", "DC & Compute", "DCC"),
    ("cisco_security_extended", "Security Extended", "SES"),
    ("cisco_industrial", "Industrial / IoT", "IND"),
    ("cisco_sp_mobile", "SP Mobile", "SPM"),
]

PRODUCT_HEADER = [
    "product_id", "product_family", "product_series", "example_pids",
    "category", "use_case", "os_type", "latest_version", "gold_version",
    "eol_status", "source_ids", "notes", "last_updated",
]

BEGIN = "<!-- AUTO-GENERATED:FILE-TABLE:BEGIN -->"
END = "<!-- AUTO-GENERATED:FILE-TABLE:END -->"
BEGIN_D = "<!-- AUTO-GENERATED:DATA-TABLES:BEGIN -->"
END_D = "<!-- AUTO-GENERATED:DATA-TABLES:END -->"
BEGIN_S = "<!-- AUTO-GENERATED:SOURCE-COUNT:BEGIN -->"
END_S = "<!-- AUTO-GENERATED:SOURCE-COUNT:END -->"


def read_rows(stem: str) -> list[dict]:
    path = DATA / f"{stem}.csv"
    if not path.exists():
        sys.exit(f"ERROR: missing {path}")
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def build_combined() -> list[dict]:
    merged: list[dict] = []
    for stem, _name, _prefix in FILES:
        merged.extend(read_rows(stem))
    out = DATA / "cisco_all_products.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=PRODUCT_HEADER)
        w.writeheader()
        w.writerows(merged)
    return merged


def file_table(merged: list[dict]) -> str:
    lines = [
        BEGIN,
        "",
        "| File | Rows | ID Prefix | Description |",
        "|---|---:|---|---|",
    ]
    for stem, name, prefix in FILES:
        n = sum(1 for r in merged if r["product_id"].startswith(prefix + "-"))
        lines.append(f"| `data/{stem}.csv` | {n} | {prefix} | {name} |")
    n_src = sum(1 for _ in csv.DictReader((DATA / "cisco_sources.csv").open(encoding="utf-8")))
    lines.append(f"| `data/cisco_all_products.csv` | {len(merged)} | — | **Combined all-in-one** (generated) |")
    lines.append(f"| `data/cisco_sources.csv` | {n_src} | SRC | Source URL registry |")
    lines += ["", f"**Total product entries: {len(merged)}**", "", END]
    return "\n".join(lines)


def data_tables() -> str:
    out = [BEGIN_D, ""]
    for stem, name, _prefix in FILES:
        rows = read_rows(stem)
        out.append(f"### {name} — `{stem}.csv`")
        out.append("")
        out.append("| ID | Product Family | Use Case | Gold Version | EOL Status |")
        out.append("|---|---|---|---|---|")
        for r in rows:
            use = (r.get("use_case") or "").replace("|", "\\|")
            fam = (r.get("product_family") or "").replace("|", "\\|")
            out.append(
                f"| {r['product_id']} | {fam} | {use} | {r['gold_version']} | {r['eol_status']} |"
            )
        counts: dict[str, int] = {}
        for r in rows:
            counts[r["eol_status"]] = counts.get(r["eol_status"], 0) + 1
        summary = " · ".join(f"{v} {k}" for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))
        out += ["", f"EOL status: **{summary}**", ""]
    out.append(END_D)
    return "\n".join(out)


def source_count_block() -> str:
    rows = list(csv.DictReader((DATA / "cisco_sources.csv").open(encoding="utf-8")))
    ids = sorted(r["source_id"] for r in rows if r.get("source_id"))
    n = len(ids)
    last = ids[-1] if ids else "none"
    nxt = f"SRC-{int(last.split('-')[1]) + 1:03d}" if ids else "SRC-001"
    # Everything this block owns MUST live between the markers. Any line
    # emitted outside them is not replaced on the next run, so it duplicates.
    return "\n".join([
        BEGIN_S,
        f"**{n} sources** ({ids[0]} to {last}) covering all product files. "
        "Each product's `source_ids` field links directly to the pages needed for version refresh.",
        "",
        f"Next available source ID: **{nxt}**.",
        END_S,
    ])


def splice(text: str, begin: str, end: str, block: str, label: str) -> str:
    """Replace the region between begin/end markers. If absent, append."""
    if begin in text and end in text:
        pre = text.split(begin)[0]
        post = text.split(end, 1)[1]
        return pre + block + post
    sys.exit(
        f"ERROR: markers not found for {label}.\n"
        f"  add these to README.md:\n    {begin}\n    {end}"
    )


def main() -> int:
    check = "--check" in sys.argv

    if not README.exists():
        sys.exit(f"ERROR: {README} not found")

    merged = build_combined()
    new_table = file_table(merged)
    new_data = data_tables()
    new_sources = source_count_block()

    original = README.read_text(encoding="utf-8")
    updated = splice(original, BEGIN, END, new_table, "file table")
    updated = splice(updated, BEGIN_D, END_D, new_data, "data tables")
    updated = splice(updated, BEGIN_S, END_S, new_sources, "source count")

    combined_path = DATA / "cisco_all_products.csv"
    combined_now = combined_path.read_text(encoding="utf-8")

    if check:
        problems = []
        if updated != original:
            problems.append("README.md generated sections are out of date")
        # cisco_all_products.csv was just rewritten; note it for the user
        print("cisco_all_products.csv regenerated in place (compare with git to see changes)")
        for p in problems:
            print(f"  STALE  {p}")
        if problems:
            print("\nFAILED - run `python3 tools/build.py` and commit")
            return 1
        print("OK - derived files are current")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"wrote {combined_path.relative_to(ROOT)} ({len(merged)} rows)")
    print(f"wrote {README.relative_to(ROOT)} (generated sections refreshed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
