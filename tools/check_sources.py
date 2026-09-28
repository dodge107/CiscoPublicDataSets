#!/usr/bin/env python3
"""Check the HTTP status of every source URL in data/cisco_sources.csv.

IMPORTANT — how to read the results
------------------------------------
A bare curl/request against cisco.com returns HTTP 403 even for pages that are
perfectly alive. That is bot-blocking, NOT a dead link. This script therefore
classifies each result:

    OK       200 — page is live
    WARN     403 — almost certainly a bot-block on a cisco.com host.
                    Re-check in a real browser before changing anything.
    DEAD     404 — content is genuinely gone. Look up the replacement in
                    data/source_endpoints.yml, or re-discover via the Meraki
                    search API documented in CLAUDE.md.
    UNKNOWN  any other status (5xx, timeouts, 000) — retry, then investigate.

Meraki occasionally returns a spurious 404 from its CDN, so DEAD entries are
retried twice before being reported.

Usage:
    python3 tools/check_sources.py                 # all sources
    python3 tools/check_sources.py SRC-065 SRC-066  # specific IDs
    python3 tools/check_sources.py --retries 3
    python3 tools/check_sources.py --timeout 30
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_CSV = ROOT / "data" / "cisco_sources.csv"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)


def classify(code: int, url: str) -> tuple[str, str]:
    if code == 200:
        return "OK", ""
    if code == 403:
        if "cisco.com" in url and "documentation.meraki.com" not in url:
            return "WARN", "cisco.com bot-block — verify in a browser before replacing"
        return "WARN", "403 — check manually"
    if code == 404:
        return "DEAD", "content gone — see replacements in data/source_endpoints.yml"
    if code == 0:
        return "UNKNOWN", "no response / timeout — retry"
    return "UNKNOWN", f"HTTP {code}"


def fetch(url: str, timeout: int) -> int:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="specific source_ids to check")
    ap.add_argument("--retries", type=int, default=2, help="retries for 404 (default 2)")
    ap.add_argument("--timeout", type=int, default=25, help="per-request timeout seconds")
    args = ap.parse_args()

    with SRC_CSV.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    if args.ids:
        wanted = set(args.ids)
        rows = [r for r in rows if r["source_id"] in wanted]
        if not rows:
            print(f"no sources matched {args.ids}", file=sys.stderr)
            return 1

    results: list[tuple[str, int, str, str]] = []
    for i, row in enumerate(rows, start=1):
        sid, url = row["source_id"], row["url"]
        print(f"[{i}/{len(rows)}] {sid} ...", end="", flush=True, file=sys.stderr)

        code = fetch(url, args.timeout)

        # retry transient 404s - Meraki's CDN is flaky
        attempts = 0
        while code == 404 and attempts < args.retries:
            attempts += 1
            time.sleep(1.5)
            code = fetch(url, args.timeout)

        status, note = classify(code, url)
        if attempts:
            note += f" (recovered after {attempts} retr{'y' if attempts == 1 else 'ies'})" if code != 404 else f" ({attempts} retries)"

        results.append((sid, code, status, note))
        print(f" {code} {status}", file=sys.stderr)

    print()
    print("=" * 78)
    print(f"{'ID':<10} {'CODE':<6} {'STATUS':<8} NOTE")
    print("-" * 78)
    for sid, code, status, note in results:
        if status != "OK" or note:
            print(f"{sid:<10} {code:<6} {status:<8} {note}")
    print("-" * 78)

    tally: dict[str, int] = {}
    for _sid, _c, status, _n in results:
        tally[status] = tally.get(status, 0) + 1
    print("  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print("=" * 78)

    if tally.get("DEAD"):
        print("\nDEAD sources found. For each one:")
        print("  1. retry once more manually (Meraki CDN returns spurious 404s)")
        print("  2. look it up in data/source_endpoints.yml for a replacement")
        print("  3. if none, re-discover via the Meraki search API in CLAUDE.md")
        print("  4. update cisco_sources.csv AND source_endpoints.yml")
        return 1

    if tally.get("WARN"):
        print("\nWARN entries are usually cisco.com bot-blocks, not dead links.")
        print("Confirm in a browser before changing any URL.")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
