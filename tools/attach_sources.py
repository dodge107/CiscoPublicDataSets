#!/usr/bin/env python3
"""Attach the newly discovered source IDs (SRC-110..116) to the product rows
they authoritatively support. Appends to the existing source_ids field so no
existing provenance is lost. Idempotent: re-running will not duplicate IDs.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TODAY = "2026-09-29"

PRODUCT_FILES = [
    "cisco_campus_switching", "cisco_dc_switching", "cisco_enterprise_routing",
    "cisco_sp_routing", "cisco_wireless", "cisco_security", "cisco_sdwan",
    "cisco_software", "cisco_sp_extended", "cisco_collaboration", "cisco_meraki",
    "cisco_dc_compute", "cisco_security_extended", "cisco_industrial",
    "cisco_sp_mobile",
]

# product_id -> extra source ids to merge into source_ids
ADDITIONS: dict[str, list[str]] = {}


def add(pids, *srcs):
    for p in pids:
        ADDITIONS.setdefault(p, []).extend(srcs)


add(("SPR-001", "SPR-002", "SPR-003", "SPR-005"), "SRC-110")           # IOS-XR
add(("SPX-003", "SPX-006", "SPX-007", "SPX-008", "SPX-010"), "SRC-110")  # IOS-XR
add(("ERT-001", "ERT-002", "ERT-003", "ERT-004", "ERT-005", "ERT-006", "ERT-007"), "SRC-111")
add(("DCC-001", "DCC-002"), "SRC-112")                                  # ACI
add(("DCC-003", "DCC-004", "DCC-005", "DCC-006"), "SRC-113")            # MDS
add(("FWL-004", "FWL-005", "FWL-006", "FWL-008", "SES-012"), "SRC-114")  # FTD/FMC
add(("CLB-008", "CLB-009", "CLB-010", "CLB-011"), "SRC-115")            # RoomOS
add(("SDW-002", "SDW-003", "SFT-014"), "SRC-116")                       # SD-WAN


def main() -> int:
    dry = "--dry-run" in sys.argv
    total = 0
    for stem in PRODUCT_FILES:
        path = DATA / f"{stem}.csv"
        if not path.exists():
            print(f"ERROR: missing {path.name}", file=sys.stderr)
            return 1
        with path.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            fields = reader.fieldnames or []
            rows = list(reader)

        file_changed = False
        for row in rows:
            pid = row.get("product_id", "").strip()
            extra = ADDITIONS.get(pid)
            if not extra:
                continue
            existing = [t.strip() for t in (row.get("source_ids") or "").split(",") if t.strip()]
            merged = existing[:]
            for s in extra:
                if s not in merged:
                    merged.append(s)
            if merged != existing:
                if not dry:
                    print(f"  {pid}  source_ids: {','.join(existing)} -> {','.join(merged)}")
                    row["source_ids"] = ",".join(merged)
                file_changed = True
                total += 1

        if file_changed and not dry:
            with path.open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=fields)
                w.writeheader()
                w.writerows(rows)

    print(f"\n{'would update' if dry else 'updated'} {total} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
