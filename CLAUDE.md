# Cisco Public Datasets — Project Context

## Purpose
This project maintains CSV-based reference datasets of Cisco products for use in AI/ML applications. It covers product families, OS types, recommended software versions, and EOL status across all major Cisco product domains.

## File Structure

All CSV files live in the `data/` subdirectory.

Product IDs use a uniform `XXX-NNN` format: 3-letter domain code, dash, 3-digit zero-padded sequence. IDs are globally unique across all product files and carry over into the combined file.

| File | Product Domain | ID Prefix | Current Range |
|---|---|---|---|
| `data/cisco_campus_switching.csv` | Campus switching (Catalyst 9200/9300/9400/9500/9600, 3850/3650/2960-X, 1000/1300, 6500/6800/4500/3750-X legacy) | CSW | CSW-001–CSW-014 |
| `data/cisco_dc_switching.csv` | DC switching (Nexus 9300/9500/7000/5500/3000/3500/2000 FEX) | DCW | DCW-001–DCW-007 |
| `data/cisco_enterprise_routing.csv` | Enterprise routing (ISR 4000/1000, Catalyst 8200/8300/8500, ASR 1000, CSR/C8000V, ISR G2 legacy) | ERT | ERT-001–ERT-009 |
| `data/cisco_sp_routing.csv` | SP routing core (ASR 9000, NCS 5500/540/560/5000/1000, Cisco 8000) | SPR | SPR-001–SPR-006 |
| `data/cisco_wireless.csv` | Wireless (Catalyst 9800 WLCs, 9100 APs Wi-Fi 6/6E/7, Aironet + WLC 5500/8500 legacy) | WLS | WLS-001–WLS-010 |
| `data/cisco_security.csv` | Firewalls (ASA 5500-X/5585-X/ASAv, FTD 1000/2100/3100/4100/4200, FPR 9300, ASA 5500 original legacy) | FWL | FWL-001–FWL-010 |
| `data/cisco_sdwan.csv` | SD-WAN (Catalyst SD-WAN vEdge, cEdge, Controllers) | SDW | SDW-001–SDW-003 |
| `data/cisco_software.csv` | Management & software platforms (Catalyst Center, ISE, NSO, ThousandEyes, etc.) | SFT | SFT-001–SFT-015 |
| `data/cisco_sp_extended.csv` | SP routing extended (ASR 920/901, NCS 2000/4000, XRv 9000, BNG, CRS/ME legacy) | SPX | SPX-001–SPX-012 |
| `data/cisco_collaboration.csv` | UC & Collaboration (CUCM, Unity, Expressway, IP Phones, Webex devices) | CLB | CLB-001–CLB-011 |
| `data/cisco_meraki.csv` | Meraki cloud-managed (MX, MS, MR, MV, MT, MG, Z) | MRK | MRK-001–MRK-015 |
| `data/cisco_dc_compute.csv` | DC, ACI & Compute (APIC, MDS SAN, UCS, HyperFlex) | DCC | DCC-001–DCC-015 |
| `data/cisco_security_extended.csv` | Extended security (Secure Email, Web, Endpoint, XDR, SASE, Cyber Vision, FMC) | SES | SES-001–SES-012 |
| `data/cisco_industrial.csv` | Industrial networking / IoT (IE, IR, IW, Cyber Vision, IC3000, IoT OD) | IND | IND-001–IND-014 |
| `data/cisco_sp_mobile.csv` | SP mobile core (ASR 5000/5500, Ultra Packet Core, 5G SA NFs, BroadWorks) | SPM | SPM-001–SPM-011 |
| `data/cisco_all_products.csv` | **Combined all-in-one** — all product files merged (auto-generated, do not edit directly) | — | all 164 rows |
| `data/cisco_sources.csv` | Source URL registry | SRC | SRC-001–SRC-109 |

## CSV Schema (all product files share identical columns)

```
product_id, product_family, product_series, example_pids, category, use_case,
os_type, latest_version, gold_version, eol_status, source_ids, notes, last_updated
```

- `latest_version`: The absolute newest release available for the platform, regardless of stability.
- `gold_version`: The TAC-recommended / suggested release — the most stable, widely validated version. Where Cisco publishes a "recommended release" page, that value goes here. This may be older than `latest_version`. For SaaS/continuous-delivery products both fields are `Continuous delivery (SaaS)`.
- `eol_status`: One of `Active`, `EOL`, or `EOL-Pending`
- `source_ids`: Comma-separated SRC-xxx IDs from `cisco_sources.csv`
- `last_updated`: ISO date (YYYY-MM-DD) when this row was last modified. Update whenever any field in the row changes.

## cisco_sources.csv Schema

```
source_id, description, platform_scope, url, last_verified
```

- `last_verified`: ISO date (YYYY-MM-DD) when the URL was last confirmed live and relevant
- Source IDs are sequential: next available is SRC-110

## Data Refresh Process

Read this section before attempting any version or EOL update. The rules below were
established by hands-on verification on **2026-09-29** — do not re-derive them by trial
and error.

### 1. Start from the endpoint registry, not from memory
`data/source_endpoints.yml` records every URL verified to work, plus the replacement
path for each source that has died. Consult it first. It saves rediscovering the Meraki
taxonomy and documents the known-broken fetch behaviours below.

### 2. Match the fetch method to the host — this is not optional

| Host | Method | Reason |
|---|---|---|
| `cisco.com` | **Integrated browser only** (Playwright / `open_browser_page` / `fetch_webpage`) | Returns **HTTP 403 to plain `curl` and `requests`**, even with a browser User-Agent and `Accept` headers. This is bot-blocking, **not** a dead link. A 403 from curl is *not* evidence of a broken source. |
| `documentation.meraki.com` | Plain HTTP works | Serves normal requests, but the body is **JavaScript-rendered** — raw HTML returns an empty `<body>`. Render the page before reading content. |

**Never conclude a Cisco URL is dead from a curl 403.** Confirm in the browser first.

### 3. Meraki URLs restructured in 2026
The old `/MX/...`, `/MS/...`, `/MR/...`, `/MV/...`, `/MG/...` per-product
`Firmware_Changelog` paths were retired and replaced by
`/Platform_Management/Product_Information/Compatibility_and_Firmware/*_Firmware_Features_Directory`
pages. The five replacements are recorded in `source_endpoints.yml`.

To discover current paths instead of guessing, use Meraki's public search API (call
from a browser context on any `documentation.meraki.com` page):

```js
fetch('https://documentation.meraki.com/@api/deki/site/query'
      + '?q=' + encodeURIComponent('firmware changelog')
      + '&limit=40&dream.out.format=json', { credentials: 'omit' })
```

Returns `{result: [{type, page: {path, title}}]}` — filter to `type === 'page'`.

### 4. Fast extraction patterns
- **Meraki "Features Directory" pages**: the table of contents lists firmware trains
  newest-first. The first few `X.Y.X` tokens give the current trains without parsing
  the body. Verified working for MX, MR, MS, MG.
- **Cisco TAC recommended-release pages**: contain a clean product-family →
  recommended-release table **plus** a "Revision History" table. Always read the
  revision history to confirm the page is current — it is the cheapest freshness check
  available.
- **Meraki "Last updated" dates are unreliable** as a freshness signal — some predate
  the versions they describe. Use them as weak evidence only.

### 5. Check for Beta and Archive labels before recording a version
Meraki directories explicitly label trains. The MG directory lists
`Beta Release - MG 26.1` and `Stable Release - MG 3.212` — the higher-numbered train is
**not** automatically the better answer. MX directories carry an
`Old Stable Release` and an `Archive` section that must not be mistaken for current.

### 6. Retry before declaring a URL dead
Meraki's CDN returns spurious `404` responses intermittently. A `404` was observed and
then immediately disappeared on retry. **Retry at least twice** before replacing a URL,
and record the confirmed-good URL.

### 7. URL-encoding
Some Meraki paths contain parentheses and commas, e.g.
`Security_and_SD-WAN_(MX,Z)_Features_Directory`. Both raw and percent-encoded
(`%28MX%2CZ%29`) forms resolve correctly, but percent-encode when embedding such a path
in a query string.

## Key Conventions

### Gold / Recommended Version
Cisco TAC publishes "recommended release" guides for most platforms. These are the preferred versions — not always the absolute latest, but the most stable and widely validated.

**`latest_version` and `gold_version` are different fields with different meanings — do
not conflate them:**
- `latest_version` = the absolute newest release available, *regardless* of stability.
- `gold_version` = the TAC-recommended release.

An earlier version of this document incorrectly instructed "always prefer the
TAC-recommended version in `latest_version`", which contradicts the schema and the
actual data. The TAC-recommended value belongs in `gold_version` only.

Format:
- IOS-XE: `26.1.x` (new year-based) or `17.15.x` (last stable legacy train) — show both if transitioning
- NX-OS: `10.6(3)F` for Nexus 9000, `9.4(5)` for MDS
- IOS-XR: `26.1.1`
- FTD: `10.0` (new) / `7.6.4` (stable recommended)
- Where both a "latest" and a "recommended stable" exist, format as: `NEW.VERSION / STABLE.VERSION (recommended)`

### Gold Version Selection When Two Releases Are Recommended
Cisco now publishes **two** recommended releases per platform on TAC pages. The
Catalyst 9000 page (SRC-001) currently recommends `17.18.4, 17.15.6` for the 9200/9300/
9400/9500/9600. Cisco designates every third train as **Extended-Support** (48-month
sustaining lifetime) and the others Standard-Support (12 months); 17.15 and 17.18 are
both Extended-Support.

**Rule:** when a TAC page lists two recommended releases, set `gold_version` to the
**newer** Extended-Support train and preserve the older alternative in the `notes` field
so no information is lost. Never drop the second recommendation silently.

Where a directory page marks one train `Beta` and another `Stable`, `gold_version` takes
the **Stable** train even when it is the lower-numbered one.

### EOL Status Rules
- `Active`: Currently sold and supported, receiving software updates
- `EOL-Pending`: End-of-Sale announced or within 12 months; still receiving security/bug fixes
- `EOL`: End-of-Sale passed AND end-of-software-maintenance reached or announced

### Source URL Quality
Prefer in this order:
1. Cisco TAC recommended-release guide (most authoritative for gold version)
2. Product release notes list page (cisco.com .../products-release-notes-list.html)
3. Product series support page (cisco.com .../series.html)
4. Meraki `*_Firmware_Features_Directory` pages (documentation.meraki.com) — these
   replaced the retired per-product `Firmware_Changelog` pages

### Per-platform known-good pages
- **Catalyst 9000 family (9200/9300/9400/9500/9600)** — `SRC-001`, TAC recommended
  releases. Page carries a "current as of" marker and a revision history.
- **Catalyst 1000/2960/3560/CDB/4500, 3650/3850, 6500/6800** — separate TAC page:
  `https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6500-series-switches/214946-recommended-releases-for-catalyst-2960-3.html`
- **Catalyst 9800 WLC** — `https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/214749-tac-recommended-ios-xe-builds-for-wirele.html`
  (identified but **not yet verified** — confirm before updating WLS-001..004)
- **Meraki MV cameras** — no machine-readable version source found. The replacement page
  is a how-to guide containing **zero** extractable version numbers. Treat MV as
  manual-only and do not fabricate a version.

## Tooling

| Path | Purpose |
|---|---|
| `data/source_endpoints.yml` | Verified endpoint registry: working URLs, dead-URL replacements, fetch notes, discovery techniques, and open items. **Update this whenever a URL is confirmed or replaced.** |
| `tools/check_sources.py` | HTTP status sweep over all registered source URLs. Run before a refresh to spot dead sources. |
| `tools/validate.py` | Schema, ID format, prefix-to-file, `eol_status` enum, and `source_ids` referential-integrity checks. |
| `tools/build.py` | Regenerates `data/cisco_all_products.csv` and the README data tables from the product CSVs. |

Regenerate derived files after **any** product CSV change:
```
python3 tools/build.py && python3 tools/validate.py
```

## What NOT to do
- Do not invent or guess product PIDs — only use known orderable Cisco PIDs
- Do not mark a product EOL without finding a Cisco EoL announcement
- Do not update `last_verified` unless you actually fetched and confirmed the URL
- Do not add duplicate source IDs — always check the highest existing SRC-xxx before adding new ones
- Do not treat a curl `403` from `cisco.com` as a dead link — it is bot-blocking; verify in a browser
- Do not declare a Meraki URL dead on a single `404` — retry, the CDN returns spurious 404s
- Do not put the TAC-recommended release into `latest_version`; it belongs in `gold_version`
- Do not record a `Beta`-labelled train as `gold_version` when a `Stable` train is listed
- Do not silently drop the second of two TAC-recommended releases — keep it in `notes`
