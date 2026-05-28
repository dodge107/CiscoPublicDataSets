# Cisco Public Datasets — Project Context

## Purpose
This project maintains CSV-based reference datasets of Cisco products for use in AI/ML applications. It covers product families, OS types, recommended software versions, and EOL status across all major Cisco product domains.

## File Structure

All CSV files live in the `data/` subdirectory.

| File | Product Domain | ID Prefix |
|---|---|---|
| `data/cisco_campus_switching.csv` | Campus switching (Catalyst 9200/9300/9400/9500/9600, 3850/3650/2960-X, 1000/1300) | P001– |
| `data/cisco_dc_switching.csv` | DC switching (Nexus 9300/9500/7000/5500/3000/3500/2000 FEX) | P011– |
| `data/cisco_enterprise_routing.csv` | Enterprise routing (ISR 4000/1000, Catalyst 8200/8300/8500, ASR 1000, CSR/C8000V) | P018– |
| `data/cisco_sp_routing.csv` | SP routing core (ASR 9000, NCS 5500/540/560/5000/1000, Cisco 8000) | P025– |
| `data/cisco_wireless.csv` | Wireless (Catalyst 9800 WLCs, 9100 APs Wi-Fi 6/6E/7, Aironet legacy) | P031– |
| `data/cisco_security.csv` | Firewalls (Secure Firewall ASA 5500-X/5585-X/ASAv, FTD 1000/2100/3100/4100/4200, FPR 9300) | P038– |
| `data/cisco_sdwan.csv` | SD-WAN (Catalyst SD-WAN vEdge, cEdge, Controllers) | P047– |
| `data/cisco_software.csv` | Management & software platforms (Catalyst Center, ISE, NSO, ThousandEyes, etc.) | S001– |
| `data/cisco_sp_extended.csv` | SP routing extended (ASR 920/901, NCS 2000/4000, XRv 9000, BNG) | SP001– |
| `data/cisco_collaboration.csv` | UC & Collaboration (CUCM, Unity, Expressway, IP Phones, Webex devices) | C001– |
| `data/cisco_meraki.csv` | Meraki cloud-managed (MX, MS, MR, MV, MT, MG, Z) | M001– |
| `data/cisco_dc_compute.csv` | DC, ACI & Compute (APIC, MDS SAN, UCS, HyperFlex) | DC001– |
| `data/cisco_security_extended.csv` | Extended security (Secure Email, Web, Endpoint, XDR, SASE, Cyber Vision, FMC) | SE001– |
| `data/cisco_industrial.csv` | Industrial networking / IoT (IE, IR, IW, Cyber Vision, IC3000, IoT OD) | IO001– |
| `data/cisco_sp_mobile.csv` | SP mobile core (ASR 5000/5500, Ultra Packet Core, 5G SA NFs, BroadWorks) | SM001– |
| `data/cisco_sources.csv` | Source URL registry (SRC-001 to SRC-099) | SRC-001– |

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
- Source IDs are sequential: next available is SRC-100

## Key Conventions

### Gold / Recommended Version
Cisco TAC publishes "recommended release" guides for most platforms. These are the preferred versions — not always the absolute latest, but the most stable and widely validated. Always prefer the TAC-recommended version in `latest_version`. Format:
- IOS-XE: `26.1.x` (new year-based) or `17.15.x` (last stable legacy train) — show both if transitioning
- NX-OS: `10.6(3)F` for Nexus 9000, `9.4(5)` for MDS
- IOS-XR: `26.1.1`
- FTD: `10.0` (new) / `7.6.4` (stable recommended)
- Where both a "latest" and a "recommended stable" exist, format as: `NEW.VERSION / STABLE.VERSION (recommended)`

### EOL Status Rules
- `Active`: Currently sold and supported, receiving software updates
- `EOL-Pending`: End-of-Sale announced or within 12 months; still receiving security/bug fixes
- `EOL`: End-of-Sale passed AND end-of-software-maintenance reached or announced

### Source URL Quality
Prefer in this order:
1. Cisco TAC recommended-release guide (most authoritative for gold version)
2. Product release notes list page (cisco.com .../products-release-notes-list.html)
3. Product series support page (cisco.com .../series.html)
4. Meraki documentation changelog pages (documentation.meraki.com)

## What NOT to do
- Do not invent or guess product PIDs — only use known orderable Cisco PIDs
- Do not mark a product EOL without finding a Cisco EoL announcement
- Do not update `last_verified` unless you actually fetched and confirmed the URL
- Do not add duplicate source IDs — always check the highest existing SRC-xxx before adding new ones
