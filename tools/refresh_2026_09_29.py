#!/usr/bin/env python3
"""One-shot refresh of product rows from verified source research (2026-09-29).

Every value below was read from a fetched Cisco or Meraki page on 2026-09-29.
Sources are recorded in data/source_endpoints.yml. Rows NOT listed here are
left untouched - this is a targeted correction pass, not a blanket rewrite.

Run with --dry-run first to preview.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TODAY = "2026-09-29"

# product_id -> {field: new_value}
UPDATES: dict[str, dict[str, str]] = {}


def u(pid, latest=None, gold=None, eol=None, note=None):
    d = UPDATES.setdefault(pid, {})
    if latest is not None:
        d["latest_version"] = latest
    if gold is not None:
        d["gold_version"] = gold
    if eol is not None:
        d["eol_status"] = eol
    if note is not None:
        d["_note"] = note


# ---------------------------------------------------------------- campus
# SRC-001 TAC page, rev 27.0 (04-Sep-2026): "Added 17.18.4 in addition to 17.15.6"
CAT9K_NOTE = ("TAC recommends 17.18.4 and 17.15.6 (both Extended-Support trains); "
              "17.18.4 recorded as gold per dual-recommendation rule.")
for pid in ("CSW-001", "CSW-002", "CSW-003", "CSW-004", "CSW-005"):
    u(pid, latest="26.1.x", gold="17.18.4", note=CAT9K_NOTE)

# Legacy Catalyst - SRC 214946 (updated 05-Mar-2026)
u("CSW-006", latest="16.12.14", gold="16.12.14", note="TAC recommended 16.12.14 (was 16.12.10).")
u("CSW-007", latest="16.12.14", gold="16.12.14", note="TAC recommended 16.12.14 (was 16.12.10).")
u("CSW-008", latest="15.2(7)E13", gold="15.2(7)E13", note="TAC recommended 15.2(7)E13 (was 15.2(7)E9).")
u("CSW-009", latest="15.2(7)E13", gold="15.2(7)E13", note="TAC recommended 15.2(7)E13 (was 15.2(7)E9).")
u("CSW-011", latest="15.5(1)SY16", gold="15.5(1)SY16", note="TAC recommended 15.5(1)SY16 (was 15.5(1)SY3).")
u("CSW-012", latest="15.5(1)SY16", gold="15.5(1)SY16", note="TAC recommended 15.5(1)SY16 (was 15.5.1SY).")
u("CSW-013", latest="3.11.13E", gold="3.11.13E", note="TAC recommended 3.11.13E (was 3.11.7E).")
# CSW-010 Catalyst 1300 - no verified source found this pass; left as-is.

# ---------------------------------------------------------------- DC switching
# Nexus 9000 recommended page (updated 04-Jun-2026): gold 10.5(5)M
NEXUS_NOTE = ("Gold 10.5(5)M per TAC recommended-releases page; 10.6(x) is available "
              "(up to 10.6(4)M) but is not yet the recommended train.")
for pid in ("DCW-001", "DCW-002"):
    u(pid, latest="10.6(4)M", gold="10.5(5)M", note=NEXUS_NOTE)

# ---------------------------------------------------------------- SP routing
# IOS-XR doc 222669 (updated 27-Jul-2026): gold 25.2.21
XRR_NOTE = ("Gold 25.2.21 (EMR) per TAC 'Resolve Releases for IOS XR Routers'; "
            "26.3.1 is the newest Feature Release.")
u("SPR-001", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # ASR 9000
u("SPR-002", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # NCS 5500
u("SPR-003", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # NCS 540/560
u("SPR-005", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # Cisco 8000

# ---------------------------------------------------------------- enterprise routing
# Doc 215567 (updated 15-Jun-2026): 17.15.6 is the Extended-Support recommendation
ERT_NOTE = ("TAC recommended 17.15.6 (Extended-Support). 17.12.8 is the alternative "
            "listed for ISR/8500; 17.9.10 for older RP2/4200 hardware.")
for pid in ("ERT-001", "ERT-002", "ERT-003", "ERT-004", "ERT-005", "ERT-006", "ERT-007"):
    u(pid, latest="17.18.x", gold="17.15.6", note=ERT_NOTE)

# ---------------------------------------------------------------- SP extended
u("SPX-001", latest="17.15.6", gold="17.15.6",
  note="Newest in 17.15.x train is 17.15.6. No TAC recommended-release page covers ASR 920; gold tracks newest verified.")
u("SPX-003", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # ASR 9900
u("SPX-006", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # XRv 9000
u("SPX-007", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # Cisco 8800
u("SPX-008", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # NCS 55A2/55A1
u("SPX-010", latest="26.3.1", gold="25.2.21", note=XRR_NOTE)   # vBNG

# ---------------------------------------------------------------- wireless
# SRC-028 TAC page rev 52.0 (03-Sep-2026): C9800-40/80/L/CL -> 17.18.4a with APSP2
WLC_NOTE = ("TAC recommended 17.18.4a with APSP2 for C9800-40/80/L/CL. 17.15.5 with "
            "APSP5 is recommended only for EWC-AP. 26.1.2 is newest for the 26 train.")
for pid in ("WLS-001", "WLS-002", "WLS-003", "WLS-004"):
    u(pid, latest="26.1.2", gold="17.18.4a (with APSP2)", note=WLC_NOTE)

# ---------------------------------------------------------------- firewalls
# FTD/FMC: Cisco "New Features by Release" page - suggested release is 7.6.6
FTD_NOTE = ("Cisco suggested release is 7.6.6. FTD/FMC have no 8.x or 9.x train; "
            "the 10.x train exists (10.1.0) but is not yet the suggested release.")
for pid in ("FWL-004", "FWL-005", "FWL-006", "FWL-008"):
    u(pid, latest="10.1.0", gold="7.6.6", note=FTD_NOTE)

FXOS_NOTE = "FXOS 2.18.10 newest; 2.18.0 is the companion to the FTD 10.x train."
u("FWL-007", latest="2.18.10", gold="2.18.0", note=FXOS_NOTE)   # 4100
u("FWL-009", latest="2.18.10", gold="2.18.0", note=FXOS_NOTE)   # FPR 9300

u("FWL-003", latest="9.24(10)", gold="9.24(10)",
  note="ASA 9.24(10) is current with ASDM 7.24(10) (21-Sep-2026). No TAC recommended-release page exists for ASA.")

# ---------------------------------------------------------------- SD-WAN
u("SDW-002", latest="17.18.x", gold="17.15.5",
  note="TAC recommended cEdge IOS XE 17.15.5 (also 17.12.7b). Controller releases 20.12.7.1 / 20.15.5.2.")
u("SDW-003", latest="20.15.5.2", gold="20.15.5.2",
  note="TAC recommended SD-WAN controller 20.15.5.2 (also 20.12.7.1).")

# ---------------------------------------------------------------- software
u("SFT-001", latest="3.2.3", gold="3.2.3",
  note="3.2.3 is the latest generally available release. 3.3.1 exists but is controlled availability only (not GA).")
u("SFT-002", latest="3.5 cumulative patch 4", gold="3.5 cumulative patch 4",
  note="ISE 3.5 cumulative patch 4 GA 14-Sep-2026. Cisco publishes no TAC recommended-release page for ISE; gold tracks latest GA.")
u("SFT-014", latest="20.15.5.2", gold="20.15.5.2",
  note="vManage tracks the controller train; TAC recommended 20.15.5.2.")

# ---------------------------------------------------------------- DC compute
u("DCC-001", latest="6.2(3g)", gold="6.1(5e)",
  note="ACI: latest 6.2(3g); TAC recommended 6.1(5e), alternative 6.0(9e). N9K ACI-mode follows the same 6.x train (16.2(3g)/16.1(5e)).")
u("DCC-002", latest="16.2(3g)", gold="16.1(5e)",
  note="N9K in ACI mode tracks the APIC 6.x train: latest 16.2(3g), recommended 16.1(5e).")
for pid in ("DCC-003", "DCC-004", "DCC-005", "DCC-006"):
    u(pid, latest="9.4(5)", gold="9.4(5)",
      note="MDS NX-OS 9.4(5) is the TAC recommended release across all listed MDS platforms (page updated 06-Aug-2026).")
u("DCC-007", latest="4.3", gold="4.3", note="UCSM 4.3 current for B/C-Series domains.")
u("DCC-010", latest="4.3", gold="4.3", note="UCSM 4.3 current for B/C-Series domains.")
u("DCC-008", latest="CIMC 6.0.2.260143", gold="CIMC 6.0.2.260143",
  note="CIMC 6.0.2.260143 for M6/M8 servers; 4.3.2.260020 for M5. UCSM major 6.0 released 23-Sep-2026.")
u("DCC-011", latest="UCSM 6.0", gold="UCSM 6.0", note="UCSM 6.0 is the current major release.")

# ---------------------------------------------------------------- security extended
u("SES-001", latest="16.5", gold="16.0.4 HP2",
  note="AsyncOS 16.5 is newest for Secure Email Gateway (15-Sep-2026); 16.0.4 HP2 is the latest maintenance track.")
u("SES-002", latest="16.5", gold="16.0.4",
  note="Secure Email Cloud Gateway shares the ESA AsyncOS train.")
u("SES-003", latest="16.0", gold="15.2.3 HP1",
  note="AsyncOS 16.0 is newest for Secure Web Appliance; no 16.5 exists for WSA.")
u("SES-012", latest="10.1.0", gold="7.6.6", note=FTD_NOTE)

# ---------------------------------------------------------------- industrial
IND_NOTE = ("IOS-XE 26.2.x is now available for IE3x00/ESS3300 and IR1101/1800/8140/8340; "
            "26.1.x is the previous train. No TAC recommended-release page found for these.")
for pid in ("IND-002", "IND-003", "IND-004", "IND-005", "IND-006", "IND-007", "IND-008", "IND-010"):
    u(pid, latest="26.2.x", gold="26.2.x", note=IND_NOTE)
u("IND-001", latest="17.14.x", gold="17.14.x",
  note="IE3100 remains on the 17.14.x train; 26.x is not offered for this model.")

# ---------------------------------------------------------------- SP mobile
u("SPM-002", latest="2026.03.gh1", gold="2026.03.gh1",
  note="StarOS 2026.03.gh1 released 09-Sep-2026. Note: ASR 5500 hardware is not listed as qualified in the 2026.02 platform table - verify before new deployments.")
u("SPM-003", latest="2026.03.gh1", gold="2026.03.gh1", note="StarOS 2026.03.gh1 released 09-Sep-2026.")
u("SPM-004", latest="2026.03.gh1", gold="2026.03.gh1", note="StarOS 2026.03.gh1 released 09-Sep-2026.")
u("SPM-009", latest="Release 27", gold="Release 27",
  note="BroadWorks Release 27 documentation guide updated 07-Sep-2026. No Release 28 exists yet.")

# ---------------------------------------------------------------- collaboration
u("CLB-001", latest="15SU4a", gold="15SU4a",
  note="CUCM 15SU4a is newest on the 15 branch (14 tops out at 14SU6). Cisco publishes no TAC recommended-release page for CUCM; gold tracks latest.")
u("CLB-002", latest="15 SU3", gold="15 SU3",
  note="Unity Connection 15 SU3 is the newest 15-branch cumulative update. (Dataset previously recorded 15.SU4a, which is a CUCM designation and does not exist for Unity.)")
u("CLB-003", latest="X15.5.x", gold="X15.5.x",
  note="Expressway X15.5.x is newest; no X16 section exists on the release-notes list.")
u("CLB-006", latest="14.4(1)SR3", gold="14.4(1)SR3", note="IP Phone 7800 series SIP image 14.4(1)SR3.")
u("CLB-007", latest="14.4(1)SR4", gold="14.4(1)SR4",
  note="IP Phone 8800/8845 series SIP image 14.4(1)SR4. (Dataset previously had latest 12.0(2) and gold 14.2(1)SR1.)")
ROOMOS_NOTE = ("RoomOS 11.32.7.0 (18-Aug-2026) is the current release. Note: there is no "
               "'RoomOS 26' build; 11.32 is the final RoomOS 11 train.")
for pid in ("CLB-008", "CLB-009", "CLB-010", "CLB-011"):
    u(pid, latest="11.32.7.0", gold="11.32.7.0", note=ROOMOS_NOTE)

# ---------------------------------------------------------------- meraki
MX_NOTE = ("MX 26.2.X is the current GA train (features directory updated 09-Sep-2026); "
           "26.1.X is the previous GA train. 19.2.X is the last of the old 19.x line.")
for pid in ("MRK-001", "MRK-002", "MRK-003", "MRK-004"):
    u(pid, latest="MX 26.2.X", gold="MX 26.2.X", note=MX_NOTE)

MS_NOTE = "MS 18 is the current train (features directory lists MS 18/17/16/15)."
for pid in ("MRK-005", "MRK-006", "MRK-007", "MRK-008"):
    u(pid, latest="MS 18.1.7", gold="MS 18.1.7", note=MS_NOTE)

MR_NOTE = ("MR directory TOC lists 32.2.X / 32.1.X / 31.1.X; a 33.1.1 build reference "
           "appears in the body, so the 33.x train is starting to ship.")
for pid in ("MRK-009", "MRK-010", "MRK-011"):
    u(pid, latest="MR 32.2.X", gold="MR 32.2.X", note=MR_NOTE)

MG_NOTE = ("MG directory explicitly labels 'Beta Release - MG 26.1' and 'Stable Release - "
           "MG 3.212'. Stable is recorded as gold per the Beta-vs-Stable rule.")
u("MRK-015", latest="MG 26.1 (beta)", gold="MG 3.212 (stable)", note=MG_NOTE)

u("MRK-012", latest="Manual verification required", gold="Manual verification required",
  note="No machine-readable MV version source exists. The replacement page is a how-to guide with zero extractable version numbers - verify in the Dashboard.")
u("MRK-013", latest="Manual verification required", gold="Manual verification required",
  note="No machine-readable MV version source exists. Verify in the Dashboard.")


PRODUCT_FILES = [
    "cisco_campus_switching", "cisco_dc_switching", "cisco_enterprise_routing",
    "cisco_sp_routing", "cisco_wireless", "cisco_security", "cisco_sdwan",
    "cisco_software", "cisco_sp_extended", "cisco_collaboration", "cisco_meraki",
    "cisco_dc_compute", "cisco_security_extended", "cisco_industrial",
    "cisco_sp_mobile",
]


def main() -> int:
    dry = "--dry-run" in sys.argv
    # Explicit list: never glob, so cisco_sources.csv / cisco_all_products.csv
    # can never be touched by a version refresh.
    files = [DATA / f"{stem}.csv" for stem in PRODUCT_FILES]
    missing = [p.name for p in files if not p.exists()]
    if missing:
        print(f"ERROR: missing product files: {missing}", file=sys.stderr)
        return 1

    applied = 0
    unmatched: set[str] = set()

    for path in files:
        with path.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            fieldnames = reader.fieldnames or []
            rows = list(reader)

        file_changed = False
        for row in rows:
            pid = row.get("product_id", "").strip()
            upd = UPDATES.get(pid)
            if not upd:
                continue
            row_changed = False
            for field in ("latest_version", "gold_version", "eol_status"):
                if field in upd and row.get(field) != upd[field]:
                    if not dry:
                        print(f"  {pid}  {field}: {row.get(field)!r} -> {upd[field]!r}")
                        row[field] = upd[field]
                    row_changed = True
            if "_note" in upd and not dry:
                # append the verification note, keeping any existing note
                existing = (row.get("notes") or "").rstrip()
                row["notes"] = f"{existing} [{TODAY}] {upd['_note']}" if existing else f"[{TODAY}] {upd['_note']}"
                row_changed = True
            if row_changed:
                if not dry:
                    row["last_updated"] = TODAY
                file_changed = True
            applied += 1

        if file_changed and not dry:
            with path.open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(rows)

    matched = {pid for pid in UPDATES if any(pid in (r.get("product_id", "").strip() for r in csv.DictReader((DATA / f).open(encoding="utf-8"))) for f in [p.name for p in files])}
    unmatched = set(UPDATES) - matched

    verb = "would update" if dry else "updated"
    print(f"\n{verb} {applied} rows across {len(files)} files")
    if unmatched:
        print(f"WARNING: {len(unmatched)} product_ids did not match any file: {sorted(unmatched)}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
