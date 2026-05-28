# Cisco Public Datasets

> **Disclaimer:** This project is a personal initiative and is not endorsed, sponsored, or affiliated with Cisco Systems in any way. While the author is a Cisco employee, this dataset was compiled independently using only publicly available information from Cisco's public documentation, release notes, and support pages.
>
> Every effort has been made to ensure accuracy and keep version data current, but errors and omissions may exist. Software versions, product availability, and EOL status change frequently. **Always verify information against official Cisco documentation before making any permanent business, architectural, or procurement decisions.**

A reference dataset of Cisco networking products for use in AI/ML projects, chatbots, and knowledge bases. Covers product families, categories, OS types, and latest software versions — sourced entirely from public Cisco documentation.

## Files

All CSV files live in the `data/` subdirectory.

| File | Rows | Description |
|---|---|---|
| `data/cisco_products.csv` | 49 | Core networking — campus switching, DC switching, enterprise/SP routing, wireless, security, SD-WAN |
| `data/cisco_software.csv` | 15 | Management and software platforms — Catalyst Center, ISE, NSO, ThousandEyes, Secure Client, XDR, Umbrella, Duo |
| `data/cisco_sp_extended.csv` | 10 | Additional SP products — ASR 920/901, NCS 2000/4000/6000, XRv 9000, BNG |
| `data/cisco_collaboration.csv` | 16 | Unified Communications and Collaboration — CUCM, Unity Connection, Expressway, IP Phones, Webex devices |
| `data/cisco_meraki.csv` | 15 | Meraki cloud-managed products — MX, MS, MR, MV, MT, MG, Z series |
| `data/cisco_dc_compute.csv` | 15 | DC compute and ACI — APIC, ACI, MDS SAN, UCS B/C/X-Series, Fabric Interconnects, HyperFlex |
| `data/cisco_security_extended.csv` | 12 | Extended security portfolio — Secure Email, Secure Web, Secure Endpoint, XDR, Secure Access SASE, Cyber Vision, FMC |
| `data/cisco_industrial.csv` | 14 | Industrial networking / IoT — IE switches, IR routers, IW APs, Cyber Vision, IoT OD |
| `data/cisco_sp_mobile.csv` | 11 | SP mobile core — ASR 5000/5500/5700, Ultra Packet Core, 5G SA (AMF/SMF/UPF/PCF), BroadWorks, IoT Control Center |
| `data/cisco_sources.csv` | 99 | Source URLs (SRC-001 to SRC-099) for refreshing version data |

**Total product entries: 157**

---

## All Files — Shared Schema

All product CSV files use identical columns:

| Field | Description |
|---|---|
| `product_id` | Unique identifier per file (P001–, S001–, SP001–, C001–, M001–) |
| `product_family` | Marketing name (e.g., Catalyst 9300, Meraki MX, CUCM) |
| `product_series` | Model variants within the family |
| `example_pids` | Representative Cisco product IDs (orderable SKUs) |
| `category` | High-level grouping (see below) |
| `use_case` | Deployment role (e.g., Enterprise Access Layer, SP Core) |
| `os_type` | Operating system (see OS Types Reference below) |
| `latest_version` | Newest available release for this platform (any train) |
| `gold_version` | TAC-recommended / suggested release — the most stable, widely validated version. May differ from `latest_version`. For SaaS products both fields read `Continuous delivery (SaaS)`. |
| `eol_status` | `Active`, `EOL`, or `EOL-Pending` |
| `source_ids` | Comma-separated IDs referencing rows in `cisco_sources.csv` |
| `notes` | Migration guidance, caveats, key features |
| `last_updated` | ISO date (YYYY-MM-DD) when this row was last modified |

---

## cisco_products.csv — Core Networking

| Category | Count | Families |
|---|---|---|
| Campus Switching | 10 | Catalyst 9200, 9300, 9400, 9500, 9600, 3850, 3650, 2960-X, 1000, 1300 |
| Security | 9 | ASA 5500-X, ASAv, Secure Firewall 1000/2100/3100/4100/4200, Firepower 9300 |
| DC Switching | 7 | Nexus 9300, 9500, 7000/7700, 5500/5600, 3000/3100, 3500, 2000 FEX |
| Enterprise Routing | 7 | ISR 4000/1000, Catalyst 8200/8300/8500, ASR 1000, CSR 1000V/C8000V |
| Wireless | 7 | Catalyst 9800 WLC (×4), 9100 APs (Wi-Fi 6 + 6E/7), Aironet |
| SP Routing | 5 | ASR 9000, NCS 5500, NCS 540/560, NCS 5000, Cisco 8000 |
| SD-WAN | 3 | vEdge (EOL), cEdge (Catalyst 8000/ISR), SD-WAN Controllers |
| Optical / SP Routing | 1 | NCS 1000 (DWDM/OTN) |

EOL status: **38 Active · 9 EOL · 2 EOL-Pending**

---

## cisco_software.csv — Management & Software Platforms

| Product | Use Case | OS / Delivery |
|---|---|---|
| Cisco Catalyst Center | Network Automation / Assurance | Catalyst Center OS 3.2.2 |
| Cisco ISE | NAC / Policy / Zero Trust | ISE OS 3.5 |
| Cisco Crosswork NSO | Multi-vendor Orchestration | NSO 6.x |
| Cisco Crosswork Network Controller | SP Traffic Engineering Automation | Crosswork 7.2.x |
| Cisco ThousandEyes | Internet & SaaS Visibility | SaaS (continuous) |
| Cisco Secure Network Analytics | NDR / NetFlow Threat Detection | 7.6.0 |
| Cisco Secure Client (AnyConnect) | Remote Access VPN / ZTNA | 5.1.x |
| Cisco Umbrella | DNS Security / SASE | SaaS (continuous) |
| Cisco Duo Security | MFA / Device Trust | SaaS (continuous) |
| Cisco Intersight | DC/Cloud Infrastructure Management | SaaS (continuous) |
| Cisco Secure Workload | App Micro-segmentation | 3.9.x |
| Cisco AppDynamics | APM / Full-Stack Observability | SaaS (continuous) |
| Cisco SD-WAN Manager (vManage) | SD-WAN Management Plane | 20.15.x |
| Cisco Prime Infrastructure | Legacy NMS | 3.10.x (EOL-Pending) |

---

## cisco_sp_extended.csv — Service Provider Extended

| Product | Use Case | OS |
|---|---|---|
| ASR 920 | Metro CE / Mobile Backhaul | IOS-XE 26.1.x |
| ASR 901/901S | Metro CE / Cell Backhaul (compact) | IOS-XE 17.15.x |
| ASR 9900 | SP Ultra High-density Core | IOS-XR 26.1.1 |
| NCS 2000 | ROADM / DWDM Optical Line System | IOS-XR 26.x |
| NCS 4000 | Converged Packet-Optical | IOS-XR 6.5.35 (EOL-Pending) |
| XRv 9000 | Virtual SP Router (lab/cloud PE) | IOS-XR 26.1.1 |
| Cisco 8800 (large chassis) | Hyperscale SP Core | IOS-XR 26.1.1 |
| NCS 55A1/55A2-MOD | SP Metro Aggregation (fixed) | IOS-XR 26.1.1 |
| NCS 6000 | SP Core (legacy) | IOS-XR 6.6.x (EOL) |
| vBNG / BNG | SP Broadband Subscriber Management | IOS-XR 26.1.1 |

---

## cisco_collaboration.csv — Unified Communications & Collaboration

| Product | Use Case | OS / Platform |
|---|---|---|
| CUCM | Enterprise IP Telephony / Call Control | UC OS 15.SU4a |
| Unity Connection | Enterprise Voicemail | UC OS 15.SU4a |
| Cisco Expressway | MRA / B2B Video Edge | Expressway X15.5.x |
| Cisco Meeting Server | On-prem Video Bridges | CMS OS 3.9.x |
| IP Phone 6800 | Mid-range Desktop Phone | SIP 12.0(4)SR1 |
| IP Phone 7800 | Business Desktop Phone | SIP 14.2(1)SR1 |
| IP Phone 8800 | Premium Desktop / Video Phone | SIP 12.0(2) / 14.2(1)SR1 |
| Webex Desk / Desk Pro / Desk Mini | Personal Video Collaboration | RoomOS 26.2 |
| Webex Board / Board Pro | Interactive Whiteboard | RoomOS 26.2 |
| Room Kit / Room Bar / Room Bar Pro | Small/Medium Room Video | RoomOS 26.2 |
| Room Kit EQ / Codec Pro / EQ | Large Room / Boardroom Video | RoomOS 26.2 |
| Room 70 / Room 55 / Room Panorama | Integrated Room Systems | RoomOS 26.2 |
| Room Navigator | Touch Controller / Room Booking | RoomOS 26.2 |
| CUBE (Unified Border Element) | SIP Trunk / Session Border Controller | IOS-XE 26.1.x |
| Webex Calling | Cloud UCaaS / Business Phone | SaaS (continuous) |
| Cisco Jabber | Legacy Soft Client | 14.x (EOL) |

---

## cisco_meraki.csv — Meraki Cloud-Managed

All Meraki products are managed entirely via the **Meraki Dashboard** (cloud SaaS). No on-prem controller required.

| Series | Use Case | Latest Firmware |
|---|---|---|
| MX (Small: MX64/67/68) | Branch Security / SD-WAN / UTM | MX 19.2.8 (rec.) / 26.1.4 |
| MX (Mid: MX75/85/95/105) | Mid-size Branch / Campus Security | MX 19.2.8 (rec.) / 26.1.4 |
| MX (Enterprise: MX250/450) | Enterprise Edge / SD-WAN Hub | MX 19.2.8 (rec.) / 26.1.4 |
| Z (Teleworker: Z3/Z4) | Home Office Secure Gateway | MX firmware (same as MX) |
| MS (Small: MS120/130) | SMB/Branch Access Switching | MS 18.1.7 |
| MS (Mid: MS210/225/250) | Enterprise Access Switching | MS 18.1.7 |
| MS (Distribution: MS350/355/390) | Enterprise Distribution Switching | MS 18.1.7 |
| MS (Core: MS410/425/450) | Campus Core / DC Switching | MS 18.1.7 |
| MR (Wi-Fi 5 legacy: MR33/42/52/53) | Wi-Fi 5 APs | MR 32.2.3 (EOL-Pending) |
| MR (Wi-Fi 6: MR36/44/46/55/56) | Wi-Fi 6 Indoor/Outdoor APs | MR 32.2.3 |
| MR (Wi-Fi 6E/7: MR57/76/86) | Wi-Fi 6E / Wi-Fi 7 APs | MR 32.2.3 |
| MV (Indoor: MV2/12/22/32) | Smart Cameras / Video Analytics | MV 7.2.1 |
| MV (Outdoor: MV52/72/93) | Outdoor Smart Cameras | MV 7.2.1 |
| MT (IoT Sensors) | Environmental / Asset Monitoring | Latest GA |
| MG (Cellular: MG21/41/51) | 4G LTE / 5G WAN Gateway | MG 26.1.3 |

---

## cisco_dc_compute.csv — Data Centre, ACI & Compute

| Product | Use Case | OS |
|---|---|---|
| Cisco APIC | ACI Policy Controller | APIC OS 6.2(2) |
| Nexus 9000 (ACI mode) | ACI Leaf / Spine | NX-OS ACI 16.2(2) |
| MDS 9132T / 9148T / 9148V | Small/Mid SAN (FC + NVMe-oF) | MDS NX-OS 9.4(5) |
| MDS 9220i | Integrated SAN / IP Storage | MDS NX-OS 9.4(5) |
| MDS 9396T / 9396V | High-density SAN | MDS NX-OS 9.4(5) |
| MDS 9706 / 9710 / 9718 | Director-class SAN Core | MDS NX-OS 9.4(5) |
| UCS B-Series (B200 M6/M7) | Blade Servers | UCSM 4.3.x |
| UCS C-Series (C220/C240 M6/M7) | Rack Servers | CIMC/UCSM 4.3.x / 6.0 |
| UCS X-Series (X9508 chassis) | Next-gen Modular Compute | UCSM 6.0 / Intersight |
| UCS Fabric Interconnect 6400 | UCS Domain FI (B/C-Series) | UCSM 4.3.x |
| UCS Fabric Interconnect 6500 (6536) | UCS X-Series FI | UCSM 6.0 |
| HyperFlex HX220c | 2-socket HCI Node | HXDP 6.0(1x) |
| HyperFlex HX240c | High-density HCI Node | HXDP 6.0(1x) |
| HyperFlex Edge | 2-node ROBO HCI | HXDP 6.0(1x) |
| ACI Multi-Site / NDO | Multi-DC ACI Policy Mgmt | NDO 4.2.x |

## cisco_security_extended.csv — Extended Security Portfolio

| Product | Use Case | OS / Version |
|---|---|---|
| Cisco Secure Email Gateway | On-prem Email Security | AsyncOS 16.0.4 HP2 |
| Cisco Secure Email Cloud Gateway | Cloud Email Security | AsyncOS 16.0.4 (SaaS) |
| Cisco Secure Web Appliance | On-prem Web Proxy / URL Filtering | AsyncOS 15.2.3 HP1 |
| Cisco Secure Email and Web Manager | Centralised SEG/SWA Management | AsyncOS 15.x |
| Cisco Secure Endpoint (connector) | EDR / AMP Endpoint Agent | 8.5.x (connector) |
| Cisco Secure Endpoint Private Cloud | Air-gapped EDR Console | 5.4.x |
| Cisco XDR | Threat Detection / SOC Platform | 2.64 (SaaS) |
| Cisco Secure Access (SASE/SSE) | Cloud ZTNA / SWG / CASB / FWaaS | 2026.1.x (SaaS) |
| Cisco Multicloud Defense | Cloud Workload Firewall | Continuous (SaaS) |
| Cisco ISA 3000 | OT/ICS Segmentation Firewall | ASA 9.14.x / FTD 7.x |
| Cisco Cyber Vision | OT/ICS Asset Visibility + Threat Detection | 4.x |
| Cisco FMC (Firewall Management Center) | Centralised FTD Management | FMC OS 10.0 / 7.6.4 |

## cisco_industrial.csv — Industrial Networking / IoT

| Product | Use Case | OS |
|---|---|---|
| Catalyst IE3100 Rugged | Industrial Access Switch (DIN-rail) | IOS-XE 17.14.x |
| Catalyst IE3200 Rugged | Industrial Access Switch | IOS-XE 17.15.x / 26.1.x |
| Catalyst IE3300 Rugged | Industrial Distribution Switch | IOS-XE 17.15.x / 26.1.x |
| Catalyst IE3400 Rugged / Heavy Duty | Industrial Access/Distribution (IP67) | IOS-XE 17.15.x / 26.1.x |
| Catalyst IE9300 Rugged | Next-gen Industrial Aggregation Switch | IOS-XE 17.15.x / 26.1.x |
| Catalyst IR1101 Rugged Router | Compact Industrial IoT Router | IOS-XE 26.1.x |
| Catalyst IR1800 Rugged Router | Industrial WAN Edge / IoT Router | IOS-XE 26.1.x |
| Catalyst IR8100/IR8140/IR8340 | Large Industrial Router / SD-WAN Edge | IOS-XE 26.1.x |
| IW6300 Heavy Duty (Wi-Fi 5) | Industrial Outdoor AP | IOS 15.3.3-JQ (EOL-Pending) |
| Catalyst IW9165 / IW9167 Rugged | Industrial Wi-Fi 6/6E AP | IOS-XE 26.1.x |
| Cisco Cyber Vision | OT Asset Discovery + Threat Detection | 4.x |
| Cisco IC3000 Gateway | Industrial IoT Edge Compute | 1.x |
| Cisco IoT Operations Dashboard | Cloud IoT Device Management | SaaS (continuous) |
| Cisco Kinetic | IoT Data Platform | 2.x (EOL) |

## cisco_sp_mobile.csv — SP Mobile Core

| Product | Use Case | OS |
|---|---|---|
| Cisco ASR 5000 | 4G LTE EPC (legacy hardware) | StarOS 21.28.x (EOL-Pending) |
| Cisco ASR 5500 | 4G/5G NSA Packet Core | StarOS 2026.02.x |
| Cisco ASR 5700 | High-capacity 4G/5G NSA Core | StarOS 2026.02.x |
| Cisco Ultra Packet Core (VPC-DI/SI) | Virtual EPC (NFV) | StarOS 2026.02.x |
| Ultra Cloud Core AMF | 5G SA Access & Mobility | Cloud-native 2026.x |
| Ultra Cloud Core SMF | 5G SA Session Management | Cloud-native 2026.x |
| Ultra Cloud Core UPF | 5G SA User Plane | Cloud-native 2026.x |
| Ultra Cloud Core PCF | 5G SA Policy Control | Cloud-native 2026.x |
| Cisco BroadWorks | SP Cloud Calling / UCaaS Platform | Release 26 (R27 Aug 2026) |
| Cisco IoT Control Center | SP SIM / IoT Connectivity Mgmt | SaaS (continuous) |
| Cisco NFVI / VIM | SP NFV Infrastructure (OpenStack) | 5.x |

## cisco_sources.csv — Source Reference

| Field | Description |
|---|---|
| `source_id` | Unique ID (SRC-001 to SRC-099) referenced in all product files |
| `description` | What the page covers |
| `platform_scope` | Which product(s) the source applies to |
| `url` | Direct URL to Cisco's release notes or documentation page |
| `last_verified` | Date this source was last checked |

**99 sources** covering all product files. Each product's `source_ids` field links directly to the pages needed for version refresh.

---

## OS Types Reference

| OS | Platforms | Version Format |
|---|---|---|
| **IOS-XE** | Catalyst 9000 switches, ISR/ASR/C8000 routers, Catalyst 9800 WLC, ASR 920, CUBE | `26.x.x` (from Apr 2026) / previously `17.x.x` |
| **IOS-XR** | ASR 9000/9900, NCS 5500, Cisco 8000, NCS 540/560, XRv 9000, BNG | `26.x.x` (from 2026) / previously `7.x.x` |
| **NX-OS** | Nexus 9000/7000/5000/3000/2000 | `10.x(y)F` (feature) or `10.x(y)M` (maintenance) |
| **FTD** | Secure Firewall 1000/2100/3100/4100/4200, Firepower 9300 | `10.x` (from 2026) / previously `7.x.x` |
| **FXOS** | Secure Firewall 4100, Firepower 9300 chassis | `2.x.x` (separate from FTD) |
| **ASA OS** | ASA 5500-X, ASAv | `9.x.x` |
| **IOS (Classic)** | Catalyst 2960-X, Catalyst 1000 | `15.2(x)Ex` |
| **Viptela OS** | SD-WAN vEdge, SD-WAN Controllers (vManage/vSmart/vBond) | `20.x.x` |
| **AireOS** | Aironet APs (legacy) | `8.10.x` |
| **RoomOS** | Webex Room / Board / Desk devices | `26.x` (year-based) |
| **Meraki MX firmware** | Meraki MX, Z Series | `19.x.x` (stable) / `26.x.x` (latest) |
| **Meraki MS firmware** | Meraki MS Switches | `18.x.x` |
| **Meraki MR firmware** | Meraki MR APs | `32.x.x` |
| **Meraki MV firmware** | Meraki MV Cameras | `7.x.x` |
| **Meraki MG firmware** | Meraki MG Cellular Gateways | `26.x.x` |
| **SaaS (continuous)** | ThousandEyes, Umbrella, Duo, Webex Calling, Meraki Dashboard, XDR, Secure Access | No fixed version — continuous delivery |
| **UC OS** | CUCM, Unity Connection | `15.x` (major) + SU suffix (e.g., 15.SU4a) |
| **Expressway OS** | Cisco Expressway | `X15.x.x` |
| **APIC OS** | Cisco APIC (ACI controller) | `6.x(y)` |
| **NX-OS (ACI mode)** | Nexus 9000 in ACI mode | `16.x(y)` (separate track from standalone NX-OS 10.x) |
| **MDS NX-OS** | MDS 9000 SAN switches | `9.x(y)` |
| **UCSM** | UCS Manager (B/C/X-Series + Fabric Interconnects) | `4.3.x` / `6.0` |
| **CIMC** | UCS C-Series standalone management | `4.3.x` / `6.0` |
| **HXDP** | HyperFlex Data Platform | `5.x` / `6.0(1x)` |
| **AsyncOS (Email)** | Cisco Secure Email Gateway | `16.x.x` |
| **AsyncOS (Web)** | Cisco Secure Web Appliance | `15.x.x` |
| **StarOS** | ASR 5000/5500/5700, Ultra Packet Core | `2026.MM.x` (from 2024) / previously `21.x.x` |
| **Cloud-native** | Ultra Cloud Core 5G SA NFs (AMF/SMF/UPF/PCF) | `2026.x` (containerised, Kubernetes) |
| **BroadWorks OS** | Cisco BroadWorks | Release `26` / `27` (annual major releases) |

### IOS-XE Versioning Change (April 2026)

Cisco switched IOS-XE to a year-based Extended Maintenance Release (EMR) cadence from April 2026:

```
Old format:  17.15.x  (sequential major.minor.patch)
New format:  26.1.x   (YY.Half.Maintenance — 26 = 2026, 1 = first half)
```

Two EMRs per year are now published instead of one. IOS-XR adopted the same year-based scheme. Both numbering schemes appear in Cisco docs during the transition period.

---

## Keeping This Data Current

1. Open `data/cisco_sources.csv` and find the `source_id(s)` for the product to update.
2. Visit the URL — each links directly to Cisco's release notes list or recommended-release page.
3. Update `latest_version` in the relevant product CSV.
4. Update `last_verified` in `cisco_sources.csv`.

Recommended check frequency: **quarterly** — Cisco ships major releases every 6 months, with maintenance updates in between. Meraki firmware updates more frequently (monthly).

> **Note on SaaS products**: ThousandEyes, Umbrella, Duo, Webex Calling, AppDynamics, and Meraki Dashboard have no discrete version numbers — they use continuous delivery. Check each product's release notes/changelog page for recent changes.

---

## Data Currency

Versions verified against live Cisco.com: **28 May 2026**

All source URLs are canonical Cisco.com or Meraki documentation pages — they remain stable even as new software versions are released.
