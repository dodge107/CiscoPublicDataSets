#!/usr/bin/env python3
"""Validate the Cisco product CSVs against the documented schema.

Checks performed:
  1. Every product file has the exact 13-column header from CLAUDE.md.
  2. product_id matches ^[A-Z]{3}-\\d{3}$ and the prefix matches the file's domain.
  3. IDs are unique across all files (and within a file).
  4. eol_status is one of Active / EOL / EOL-Pending.
  5. Every source_ids value resolves to a row in cisco_sources.csv.
  6. last_updated / last_verified are ISO dates (YYYY-MM-DD).
  7. cisco_sources.csv source_id format, uniqueness and URL sanity.
  8. The README "OS Types Reference" table still documents the version trains
     that actually appear in the data. This is the guard against the hand-
     written parts of the README silently going stale after a data refresh -
     a failure mode that has already happened once (RoomOS was documented as
     "26.x (year-based)" when no such build exists).

Exit code 0 = all good, 1 = at least one ERROR. Warnings never fail the run.
Run with --strict to also fail on warnings.
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
README = ROOT / "README.md"

PRODUCT_HEADER = [
    "product_id", "product_family", "product_series", "example_pids",
    "category", "use_case", "os_type", "latest_version", "gold_version",
    "eol_status", "source_ids", "notes", "last_updated",
]
SOURCE_HEADER = ["source_id", "description", "platform_scope", "url", "last_verified"]

EOL_VALUES = {"Active", "EOL", "EOL-Pending"}
ID_RE = re.compile(r"^[A-Z]{3}-\d{3}$")
SRC_RE = re.compile(r"^SRC-\d{3}$")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# ---------------------------------------------------------------------------
# README "OS Types Reference" cross-check
# ---------------------------------------------------------------------------
# The OS Types table is hand-written (it describes version *formats*, not
# values), so it is the part of the README most likely to drift out of date.
# For each documented OS we name a small set of representative product_ids; the
# expected version train is then DERIVED FROM THE DATA rather than hardcoded, so
# the check cannot itself go stale.
#
#   (README row label, product_ids to sample, extra literal that must appear)
OS_TYPES_CHECKS: list[tuple[str, list[str], str | None]] = [
    ("IOS-XE",            ["CSW-001", "WLS-001"], None),
    ("IOS-XR",            ["SPR-001"], None),
    ("NX-OS",             ["DCW-001"], None),
    ("NX-OS (ACI mode)",  ["DCC-002"], None),
    ("MDS NX-OS",         ["DCC-003"], None),
    ("APIC OS",           ["DCC-001"], None),
    ("FTD",               ["FWL-004"], None),
    ("FXOS",              ["FWL-007"], None),
    ("ASA OS",            ["FWL-003"], None),
    ("IOS (Classic)",     ["CSW-014"], None),
    ("UCSM",              ["DCC-007"], None),
    ("HXDP",              ["DCC-012"], None),
    ("Viptela OS",        ["SFT-014"], None),
    ("AireOS",            ["WLS-008"], None),
    ("AsyncOS (Email)",   ["SES-001"], None),
    ("AsyncOS (Web)",     ["SES-003"], None),
    ("StarOS",            ["SPM-002"], None),
    ("UC OS",             ["CLB-001"], None),
    ("Expressway OS",     ["CLB-003"], None),
    ("RoomOS",            ["CLB-008"], None),
    ("Meraki MX firmware", ["MRK-001"], None),
    ("Meraki MS firmware", ["MRK-005"], None),
    ("Meraki MR firmware", ["MRK-009"], None),
    ("Meraki MG firmware", ["MRK-015"], None),
    ("BroadWorks OS",     ["SPM-009"], "27"),
]

# Leading version train, e.g.
#   "17.18.4a (with APSP2)" -> "17.18.4"
#   "MX 26.2.X"             -> "26.2"
#   "X15.5.x"               -> "X15.5"
#   "Continuous delivery"   -> None
TRAIN_RE = re.compile(r"^[A-Za-z]*\d+(?:\.\d+)*")

# Values that are deliberately not numeric and cannot be train-checked.
NON_VERSION = re.compile(
    r"^(manual|latest ga|continuous|tracks |inherits |intersight|converged|"
    r"appliance|1\.0\.9|uaas)",
    re.I,
)

# file stem -> expected product-id prefix
PREFIXES = {
    "cisco_campus_switching": "CSW",
    "cisco_dc_switching": "DCW",
    "cisco_enterprise_routing": "ERT",
    "cisco_sp_routing": "SPR",
    "cisco_wireless": "WLS",
    "cisco_security": "FWL",
    "cisco_sdwan": "SDW",
    "cisco_software": "SFT",
    "cisco_sp_extended": "SPX",
    "cisco_collaboration": "CLB",
    "cisco_meraki": "MRK",
    "cisco_dc_compute": "DCC",
    "cisco_security_extended": "SES",
    "cisco_industrial": "IND",
    "cisco_sp_mobile": "SPM",
}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# ---------------------------------------------------------------------------
# README OS Types cross-check helpers
# ---------------------------------------------------------------------------
def parse_os_types_table(text: str) -> dict[str, str]:
    """Return {OS label: full row text} for the README OS Types Reference table."""
    start = text.find("## OS Types Reference")
    if start == -1:
        return {}
    rest = text[start:]
    nxt = rest.find("\n## ", 3)
    section = rest if nxt == -1 else rest[:nxt]

    rows: dict[str, str] = {}
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---") or "OS |" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        label = cells[0].strip("*").strip()
        if label:
            rows[label] = line
    return rows


def version_train(value: str) -> str | None:
    """Extract the leading version train, or None for non-numeric values."""
    v = (value or "").strip()
    if not v or NON_VERSION.match(v):
        return None
    m = TRAIN_RE.match(v)
    return m.group(0) if m else None


def token_covers(token: str, train: str) -> bool:
    """Does a documented format token plausibly describe this version train?

    Wildcards (x / X / MM) and parenthesised groups are ignored; the literal
    prefix in front of the first wildcard is what has to line up. Compared in
    both directions so that `26.x.x` covers a `26.2` train and `3.212` covers
    a `3.212` train.
    """
    lit = re.split(r"[xX]|MM|\(|\)", token.strip("` ").strip(), maxsplit=1)[0].strip()
    if not lit:
        return True  # token is entirely wildcard - covers anything
    return train.startswith(lit) or lit.startswith(train)


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    # ---- sources -----------------------------------------------------------
    src_path = DATA / "cisco_sources.csv"
    if not src_path.exists():
        print(f"FATAL: {src_path} not found", file=sys.stderr)
        return 1

    with src_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        src_header = next(reader, [])
    if src_header != SOURCE_HEADER:
        err(f"cisco_sources.csv header mismatch\n  expected: {SOURCE_HEADER}\n  actual:   {src_header}")

    sources = read_csv(src_path)
    known_src: set[str] = set()
    for row in sources:
        sid = (row.get("source_id") or "").strip()
        if not SRC_RE.match(sid):
            err(f"cisco_sources.csv: bad source_id {sid!r}")
        if sid in known_src:
            err(f"cisco_sources.csv: duplicate source_id {sid}")
        known_src.add(sid)

        url = (row.get("url") or "").strip()
        if not url.startswith(("http://", "https://")):
            err(f"{sid}: url is not absolute http(s): {url!r}")

        lv = (row.get("last_verified") or "").strip()
        if not ISO_RE.match(lv):
            err(f"{sid}: last_verified not ISO date: {lv!r}")
        else:
            try:
                dt.date.fromisoformat(lv)
            except ValueError:
                err(f"{sid}: last_verified not a real date: {lv!r}")

    # ---- product files -----------------------------------------------------
    seen_ids: dict[str, str] = {}
    by_id: dict[str, dict] = {}
    total_rows = 0

    for stem, prefix in PREFIXES.items():
        path = DATA / f"{stem}.csv"
        if not path.exists():
            err(f"missing product file: {path.name}")
            continue

        with path.open(newline="", encoding="utf-8") as fh:
            header = next(csv.reader(fh), [])
        if header != PRODUCT_HEADER:
            err(f"{path.name}: header mismatch\n  expected: {PRODUCT_HEADER}\n  actual:   {header}")
            continue

        rows = read_csv(path)
        total_rows += len(rows)

        for i, row in enumerate(rows, start=2):  # start=2 -> account for header
            pid = (row.get("product_id") or "").strip()
            loc = f"{path.name}:{i}"

            if not ID_RE.match(pid):
                err(f"{loc}: product_id does not match XXX-NNN: {pid!r}")
            if not pid.startswith(prefix + "-"):
                err(f"{loc}: product_id prefix should be {prefix!r}, got {pid!r}")
            if pid in seen_ids:
                err(f"{loc}: duplicate product_id {pid} (also in {seen_ids[pid]})")
            else:
                seen_ids[pid] = path.name
            by_id[pid] = row

            eol = (row.get("eol_status") or "").strip()
            if eol not in EOL_VALUES:
                err(f"{loc} ({pid}): eol_status {eol!r} not in {sorted(EOL_VALUES)}")

            raw_src = (row.get("source_ids") or "").strip()
            if not raw_src:
                warn(f"{loc} ({pid}): source_ids is empty")
            for token in (t.strip() for t in raw_src.split(",") if t.strip()):
                if token not in known_src:
                    err(f"{loc} ({pid}): source_id {token!r} not found in cisco_sources.csv")

            lu = (row.get("last_updated") or "").strip()
            if not ISO_RE.match(lu):
                err(f"{loc} ({pid}): last_updated not ISO date: {lu!r}")
            else:
                try:
                    dt.date.fromisoformat(lu)
                except ValueError:
                    err(f"{loc} ({pid}): last_updated not a real date: {lu!r}")

            for col in ("latest_version", "gold_version"):
                if not (row.get(col) or "").strip():
                    warn(f"{loc} ({pid}): {col} is empty")

    # ---- README OS Types cross-check ---------------------------------------
    # Guards the hand-written part of the README against drift after a refresh.
    if not README.exists():
        warn("README.md not found - skipping the OS Types cross-check")
    else:
        os_rows = parse_os_types_table(README.read_text(encoding="utf-8"))
        if not os_rows:
            err("README.md: could not parse the 'OS Types Reference' table")
        else:
            for label, pids, literal in OS_TYPES_CHECKS:
                row_text = os_rows.get(label)
                if row_text is None:
                    err(f"README OS Types: no row labelled {label!r} (table may have been restructured)")
                    continue

                tokens = re.findall(r"`([^`]+)`", row_text)
                if literal and literal not in row_text:
                    err(
                        f"README OS Types [{label}]: does not mention {literal!r}, "
                        f"but the data uses it"
                    )

                for pid in pids:
                    prow = by_id.get(pid)
                    if prow is None:
                        warn(f"README OS Types [{label}]: sample id {pid} not found in the data")
                        continue
                    for col in ("latest_version", "gold_version"):
                        val = (prow.get(col) or "").strip()
                        train = version_train(val)
                        if train is None:
                            continue  # SaaS / "Manual verification required" etc.
                        if not any(token_covers(t, train) for t in tokens):
                            err(
                                f"README OS Types [{label}]: documents none of the "
                                f"tokens {tokens} that describe {pid}.{col}={val!r} "
                                f"(train {train!r}). Update the table."
                            )

    # ---- freshness signal --------------------------------------------------
    # If every row shares one date, the field carries no information: it means the
    # whole dataset was rewritten at once rather than incrementally verified.
    dates: set[str] = set()
    for stem in PREFIXES:
        path = DATA / f"{stem}.csv"
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                dates.add((row.get("last_updated") or "").strip())
    dates.discard("")
    if len(dates) == 1 and total_rows:
        only = next(iter(dates))
        warn(
            f"all {total_rows} product rows share last_updated={only}; the field "
            "carries no per-row freshness information"
        )

    # ---- combined file -----------------------------------------------------
    combined = DATA / "cisco_all_products.csv"
    if combined.exists():
        crows = read_csv(combined)
        if len(crows) != total_rows:
            err(
                f"cisco_all_products.csv has {len(crows)} rows but product files "
                f"total {total_rows} - regenerate with tools/build.py"
            )
        cids = [r.get("product_id") for r in crows]
        missing = set(seen_ids) - set(cids)
        if missing:
            err(f"cisco_all_products.csv missing {len(missing)} product(s): {sorted(missing)[:10]}")
    else:
        err("cisco_all_products.csv not found")

    # ---- report ------------------------------------------------------------
    print(f"product rows : {total_rows}")
    print(f"sources      : {len(sources)}")
    print(f"errors       : {len(errors)}")
    print(f"warnings     : {len(warnings)}")

    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")

    if errors:
        print("\nFAILED")
        return 1
    if warnings and "--strict" in sys.argv:
        print("\nFAILED (strict mode: warnings treated as errors)")
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
