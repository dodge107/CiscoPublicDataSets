# Cisco Public Datasets

> **Disclaimer:** This project is a personal initiative and is not endorsed, sponsored, or affiliated with Cisco Systems in any way. While the author is a Cisco employee, this dataset was compiled independently using only publicly available information from Cisco's public documentation, release notes, and support pages.
>
> Every effort has been made to ensure accuracy and keep version data current, but errors and omissions may exist. Software versions, product availability, and EOL status change frequently. **Always verify information against official Cisco documentation before making any permanent business, architectural, or procurement decisions.**

A reference dataset of Cisco networking products for use in AI/ML projects, chatbots, and knowledge bases. Covers product families, categories, OS types, and latest software versions — sourced entirely from public Cisco documentation.

## Files

All CSV files live in the `data/` subdirectory.

<!-- AUTO-GENERATED:FILE-TABLE:BEGIN -->

| File | Rows | ID Prefix | Description |
|---|---:|---|---|
| `data/cisco_campus_switching.csv` | 14 | CSW | Campus Switching |
| `data/cisco_dc_switching.csv` | 7 | DCW | DC Switching |
| `data/cisco_enterprise_routing.csv` | 9 | ERT | Enterprise Routing |
| `data/cisco_sp_routing.csv` | 6 | SPR | SP Routing |
| `data/cisco_wireless.csv` | 10 | WLS | Wireless |
| `data/cisco_security.csv` | 10 | FWL | Firewalls |
| `data/cisco_sdwan.csv` | 3 | SDW | SD-WAN |
| `data/cisco_software.csv` | 15 | SFT | Management & Software |
| `data/cisco_sp_extended.csv` | 12 | SPX | SP Extended |
| `data/cisco_collaboration.csv` | 11 | CLB | Collaboration |
| `data/cisco_meraki.csv` | 15 | MRK | Meraki |
| `data/cisco_dc_compute.csv` | 15 | DCC | DC & Compute |
| `data/cisco_security_extended.csv` | 12 | SES | Security Extended |
| `data/cisco_industrial.csv` | 14 | IND | Industrial / IoT |
| `data/cisco_sp_mobile.csv` | 11 | SPM | SP Mobile |
| `data/cisco_all_products.csv` | 164 | — | **Combined all-in-one** (generated) |
| `data/cisco_sources.csv` | 116 | SRC | Source URL registry |

**Total product entries: 164**

<!-- AUTO-GENERATED:FILE-TABLE:END -->

---

## All Files — Shared Schema

All product CSV files use identical columns:

All product IDs use a uniform `XXX-NNN` format — 3-letter domain code + 3-digit sequence (e.g. `CSW-001`, `FWL-010`). IDs are globally unique across all files and carry through to the combined `cisco_all_products.csv`.

| File | Prefix | Example |
|---|---|---|
| cisco_campus_switching | CSW | CSW-001 |
| cisco_dc_switching | DCW | DCW-001 |
| cisco_enterprise_routing | ERT | ERT-001 |
| cisco_sp_routing | SPR | SPR-001 |
| cisco_wireless | WLS | WLS-001 |
| cisco_security | FWL | FWL-001 |
| cisco_sdwan | SDW | SDW-001 |
| cisco_software | SFT | SFT-001 |
| cisco_sp_extended | SPX | SPX-001 |
| cisco_collaboration | CLB | CLB-001 |
| cisco_meraki | MRK | MRK-001 |
| cisco_dc_compute | DCC | DCC-001 |
| cisco_security_extended | SES | SES-001 |
| cisco_industrial | IND | IND-001 |
| cisco_sp_mobile | SPM | SPM-001 |

| Field | Description |
|---|---|
| `product_id` | Globally unique identifier — format `XXX-NNN` (see prefix table above) |
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

<!-- AUTO-GENERATED:DATA-TABLES:BEGIN -->

### Campus Switching — `cisco_campus_switching.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| CSW-001 | Catalyst 9200 | Enterprise / SMB Access Layer | 17.18.4 | Active |
| CSW-002 | Catalyst 9300 | Enterprise Access Layer (primary stackable) | 17.18.4 | Active |
| CSW-003 | Catalyst 9400 | Distribution / Core (modular chassis) | 17.18.4 | Active |
| CSW-004 | Catalyst 9500 | Distribution / Core (fixed high-density) | 17.18.4 | Active |
| CSW-005 | Catalyst 9600 | Campus Core (large enterprise / modular) | 17.18.4 | Active |
| CSW-006 | Catalyst 3850 | Access / Distribution | 16.12.14 | EOL |
| CSW-007 | Catalyst 3650 | Access Layer | 16.12.14 | EOL |
| CSW-008 | Catalyst 2960-X / 2960-XR | Access Layer (SMB / Branch) | 15.2(7)E13 | EOL |
| CSW-009 | Catalyst 1000 | Access Layer (SMB) | 15.2(7)E13 | Active |
| CSW-010 | Catalyst 1300 | Access Layer (SMB) | 17.14.1 | Active |
| CSW-011 | Catalyst 6500 | Campus Core / Distribution (legacy modular chassis) | 15.5(1)SY16 | EOL |
| CSW-012 | Catalyst 6800 | Campus Core / Distribution (enhanced modular chassis) | 15.5(1)SY16 | EOL |
| CSW-013 | Catalyst 4500 / 4500-E / 4500-X | Distribution / Access (modular and fixed) | 3.11.13E | EOL |
| CSW-014 | Catalyst 3750-X / 3750-G | Access / Distribution (stackable legacy) | 15.2(4)E10 | EOL |

EOL status: **7 Active · 7 EOL**

### DC Switching — `cisco_dc_switching.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| DCW-001 | Nexus 9300 | Data Center ToR / Leaf / Access | 10.5(5)M | Active |
| DCW-002 | Nexus 9500 | Data Center Spine / Core | 10.5(5)M | Active |
| DCW-003 | Nexus 7000 / 7700 | Data Center Core / Aggregation | 8.4.x | EOL-Pending |
| DCW-004 | Nexus 5500 / 5600 | Data Center ToR / FEX Parent | 7.3.x | EOL |
| DCW-005 | Nexus 3000 / 3100 / 3200 | Data Center ToR / Leaf | 10.6(2)F | Active |
| DCW-006 | Nexus 3500 | Data Center ToR (ultra-low latency) | 7.0(3)I7.x | EOL-Pending |
| DCW-007 | Nexus 2000 FEX | Data Center Server Access (Fabric Extender) | Inherits parent switch NX-OS | Active |

EOL status: **4 Active · 2 EOL-Pending · 1 EOL**

### Enterprise Routing — `cisco_enterprise_routing.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| ERT-001 | ISR 4000 | WAN Edge / Branch Router | 17.15.6 | Active |
| ERT-002 | ISR 1000 | Branch / SOHO Router | 17.15.6 | Active |
| ERT-003 | Catalyst 8200 | WAN Edge / Branch (next-gen ISR) | 17.15.6 | Active |
| ERT-004 | Catalyst 8300 | WAN Aggregation / Mid-range Branch | 17.15.6 | Active |
| ERT-005 | Catalyst 8500 | WAN Core / High-performance Edge | 17.15.6 | Active |
| ERT-006 | ASR 1000 | WAN Aggregation / Enterprise Edge | 17.15.6 | Active |
| ERT-007 | CSR 1000V / Catalyst 8000V | Virtual WAN Router (cloud / VM / container) | 17.15.6 | Active |
| ERT-008 | ISR G2 2900 Series | Branch / WAN Edge Router (legacy) | 15.9(3)M10 | EOL |
| ERT-009 | ISR G2 3900 Series | WAN Aggregation / Branch Router (legacy) | 15.9(3)M10 | EOL |

EOL status: **7 Active · 2 EOL**

### SP Routing — `cisco_sp_routing.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| SPR-001 | ASR 9000 | Service Provider Core / Peering / Aggregation | 25.2.21 | Active |
| SPR-002 | NCS 5500 | SP Core / Metro Aggregation / Peering | 25.2.21 | Active |
| SPR-003 | NCS 540 / 560 | SP Metro Access / Aggregation | 25.2.21 | Active |
| SPR-004 | NCS 5000 | SP Metro Aggregation (older) | 6.5.x | EOL |
| SPR-005 | Cisco 8000 Series | Hyperscale / SP Core (next-gen) | 25.2.21 | Active |
| SPR-006 | NCS 1000 (Optical) | SP DWDM / Optical Transport | 7.11.x | Active |

EOL status: **5 Active · 1 EOL**

### Wireless — `cisco_wireless.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| WLS-001 | Catalyst 9800-40 WLC | Campus Wireless LAN Controller (mid-range) | 17.18.4a (with APSP2) | Active |
| WLS-002 | Catalyst 9800-80 WLC | Campus Wireless LAN Controller (large campus) | 17.18.4a (with APSP2) | Active |
| WLS-003 | Catalyst 9800-L WLC | Branch / Small Campus WLC | 17.18.4a (with APSP2) | Active |
| WLS-004 | Catalyst 9800-CL WLC (virtual) | Virtual WLC (cloud / on-prem VM) | 17.18.4a (with APSP2) | Active |
| WLS-005 | Catalyst 9100 APs (Wi-Fi 6) | Wi-Fi 6 (802.11ax) Access Points | Tracks 9800 WLC IOS-XE version | Active |
| WLS-006 | Catalyst 9100 APs (Wi-Fi 6E / Wi-Fi 7) | Wi-Fi 6E / Wi-Fi 7 (802.11be) Access Points | Tracks 9800 WLC IOS-XE version | Active |
| WLS-007 | Aironet 4800 / 3800 / 2800 | Wi-Fi 5 (802.11ac Wave 2) APs (legacy) | 8.10.x (AireOS) | EOL |
| WLS-008 | Cisco WLC 5500 | Campus Wireless LAN Controller (legacy) | 8.10.190.0 | EOL |
| WLS-009 | Cisco WLC 8500 | Large Campus / SP Wireless LAN Controller (legacy) | 8.10.190.0 | EOL |
| WLS-010 | Aironet 3700 / 3600 / 2700 / 1700 | Wi-Fi 4 / early Wi-Fi 5 (802.11n/ac Wave 1) APs (legacy) | 8.5.182.0 | EOL |

EOL status: **6 Active · 4 EOL**

### Firewalls — `cisco_security.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| FWL-001 | Secure Firewall ASA 5500-X | SMB / Branch Next-Generation Firewall | 9.12.x (final for these models) | EOL |
| FWL-002 | Secure Firewall ASA 5585-X | High-end Enterprise Firewall | 9.14.x (final) | EOL |
| FWL-003 | Secure Firewall ASAv (virtual) | Virtual Firewall (cloud / hypervisor) | 9.24(10) | Active |
| FWL-004 | Secure Firewall 1000 | SMB / Branch NGFW | 7.6.6 | Active |
| FWL-005 | Secure Firewall 2100 | Mid-range NGFW | 7.6.6 | Active |
| FWL-006 | Secure Firewall 3100 | Mid-high Range NGFW | 7.6.6 | Active |
| FWL-007 | Secure Firewall 4100 | High-performance DC / Enterprise NGFW | 2.18.0 | Active |
| FWL-008 | Secure Firewall 4200 | High-performance NGFW (latest generation) | 7.6.6 | Active |
| FWL-009 | Firepower 9300 | SP / Large DC NGFW (multi-blade chassis) | 2.18.0 | Active |
| FWL-010 | Secure Firewall ASA 5500 (original) | SMB / Enterprise Firewall (legacy) | 9.2.4 (5505) / 9.1.7 (5510-5550) | EOL |

EOL status: **7 Active · 3 EOL**

### SD-WAN — `cisco_sdwan.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| SDW-001 | Catalyst SD-WAN vEdge (Viptela hardware) | SD-WAN Branch Edge (legacy Viptela hardware) | 20.15.x | EOL |
| SDW-002 | Catalyst SD-WAN cEdge | SD-WAN Branch / WAN Edge (IOS-XE SD-WAN) | 17.15.5 | Active |
| SDW-003 | Catalyst SD-WAN Controllers | SD-WAN Control Plane / Management / Orchestration | 20.15.5.2 | Active |

EOL status: **2 Active · 1 EOL**

### Management & Software — `cisco_software.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| SFT-001 | Cisco Catalyst Center | Enterprise Network Automation / Assurance / Provisioning | 3.2.3 | Active |
| SFT-002 | Cisco Identity Services Engine (ISE) | Network Access Control (NAC) / Policy / AAA / Zero Trust | 3.5 cumulative patch 4 | Active |
| SFT-003 | Cisco Crosswork NSO (Network Services Orchestrator) | Multi-vendor Network Automation / Orchestration / Service Provisioning | 2026.02.0 (SMI AFP) | Active |
| SFT-004 | Cisco Crosswork Network Controller | SP / DC WAN Traffic Engineering and Segment Routing Automation | 7.2.x | Active |
| SFT-005 | Cisco Crosswork Optimization Engine | SP WAN Traffic Optimization / Bandwidth Management | 5.x | Active |
| SFT-006 | Cisco ThousandEyes | Internet / SaaS / WAN Visibility and Network Intelligence | Continuous delivery (no fixed version) | Active |
| SFT-007 | Cisco Secure Network Analytics (Stealthwatch) | Network Traffic Analysis / NDR / Threat Detection | 7.6.0 | Active |
| SFT-008 | Cisco Secure Client (AnyConnect) | Remote Access VPN / Zero Trust Network Access (ZTNA) / Endpoint Security | 5.1.x | Active |
| SFT-009 | Cisco Umbrella | DNS-layer Security / Cloud-delivered Secure Web Gateway / CASB / ZTNA | Continuous delivery | Active |
| SFT-010 | Cisco Duo Security | Multi-Factor Authentication (MFA) / Zero Trust Access | Continuous delivery | Active |
| SFT-011 | Cisco Intersight | Hybrid Cloud / Data Center Infrastructure Management (DCIM) / UCS Management | 1.0.9-xxx (appliance) | Active |
| SFT-012 | Cisco Secure Workload (Tetration) | Application Micro-segmentation / Workload Security / Policy Enforcement | 3.9.x | Active |
| SFT-013 | Cisco AppDynamics | Application Performance Monitoring (APM) / Full-Stack Observability | Continuous delivery | Active |
| SFT-014 | Cisco SD-WAN Manager (vManage) | Centralized SD-WAN Management and Policy Controller | 20.15.5.2 | Active |
| SFT-015 | Cisco Prime Infrastructure | Legacy Enterprise Network Management (NMS/FCAPS) | 3.10.x | EOL-Pending |

EOL status: **14 Active · 1 EOL-Pending**

### SP Extended — `cisco_sp_extended.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| SPX-001 | ASR 920 | SP Metro CE / Mobile Backhaul / Aggregation | 17.15.6 | Active |
| SPX-002 | ASR 901 / 901S | SP Metro CE / Cell Site Backhaul (small / ruggedized) | 17.15.x | EOL-Pending |
| SPX-003 | ASR 9900 | SP Ultra High-density Core (fixed chassis) | 25.2.21 | Active |
| SPX-004 | NCS 2000 Series | SP ROADM / Optical Line System (OLS) / DWDM | 26.x (IOS-XR 26.x) | Active |
| SPX-005 | NCS 4000 Series | Converged Packet-Optical Transport (SP Metro) | 6.5.35 | EOL-Pending |
| SPX-006 | XRv 9000 (virtual IOS-XR) | Virtual SP Router (lab / simulation / cloud PE) | 25.2.21 | Active |
| SPX-007 | Cisco 8800 Series (SP Core) | Hyperscale / SP Core (large modular chassis) | 25.2.21 | Active |
| SPX-008 | NCS 55A2-MOD / 55A1 | SP Metro / Aggregation / DC Peering (fixed) | 25.2.21 | Active |
| SPX-009 | Cisco Network Convergence System 6000 | SP Core (large chassis — legacy) | 6.6.x | EOL |
| SPX-010 | vBNG / BNG (Broadband Network Gateway) | SP Broadband Subscriber Management (BNG) | 25.2.21 | Active |
| SPX-011 | Cisco CRS (Carrier Routing System) | SP Core / Backbone Router (legacy large chassis) | 5.3.4 | EOL |
| SPX-012 | ME 3600X / ME 3800X | Metro Ethernet / Provider Edge Access Switch (legacy) | 3.8.0E (15.2(4)E) | EOL |

EOL status: **7 Active · 3 EOL · 2 EOL-Pending**

### Collaboration — `cisco_collaboration.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| CLB-001 | Cisco Unified Communications Manager (CUCM) | Enterprise IP Telephony / Call Control / PBX | 15SU4a | Active |
| CLB-002 | Cisco Unity Connection (CUC) | Enterprise Voicemail / Unified Messaging | 15 SU3 | Active |
| CLB-003 | Cisco Expressway Series | Video / Voice Collaboration Edge (Firewall Traversal / B2B / MRA) | X15.5.x | Active |
| CLB-004 | Cisco Meeting Server (CMS) | On-premises Video Conferencing Infrastructure / Bridges | 3.9.x | Active |
| CLB-005 | Cisco IP Phone 6800 Series | Desktop IP Phone (Mid-range) | 12.0(4)SR1 | Active |
| CLB-006 | Cisco IP Phone 7800 Series | Desktop IP Phone (Business) | 14.4(1)SR3 | Active |
| CLB-007 | Cisco IP Phone 8800 Series | Desktop IP Phone (Premium / Video) | 14.4(1)SR4 | Active |
| CLB-008 | Cisco Webex Desk / Desk Pro / Desk Mini | Personal Video Collaboration Device (Desk) | 11.32.7.0 | Active |
| CLB-009 | Cisco Webex Board / Board Pro | Interactive Whiteboard / Room Video Collaboration | 11.32.7.0 | Active |
| CLB-010 | Cisco Room Kit / Room Bar / Room Bar Pro | Video Conferencing Endpoint (Small / Medium Rooms) | 11.32.7.0 | Active |
| CLB-011 | Cisco Room Kit EQ / Codec Pro / Codec EQ | Video Conferencing Endpoint (Large Rooms / Boardrooms) | 11.32.7.0 | Active |

EOL status: **11 Active**

### Meraki — `cisco_meraki.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| MRK-001 | Meraki MX (Small Branch) | Small Branch Security / SD-WAN / Unified Threat Management | MX 26.2.X | Active |
| MRK-002 | Meraki MX (Mid-size Branch) | Mid-size Branch / Campus Security / SD-WAN | MX 26.2.X | Active |
| MRK-003 | Meraki MX (Enterprise / DC) | Enterprise / DC Edge Security / SD-WAN Concentrator | MX 26.2.X | Active |
| MRK-004 | Meraki Z (Teleworker Gateway) | Teleworker / Work-from-Home Secure Gateway | MX 26.2.X | Active |
| MRK-005 | Meraki MS (Access Switches — Small) | SMB / Branch Access Layer Switching | MS 18.1.7 | Active |
| MRK-006 | Meraki MS (Access Switches — Mid) | Enterprise Access Layer Switching | MS 18.1.7 | Active |
| MRK-007 | Meraki MS (Distribution / Aggregation) | Enterprise Distribution / Aggregation Switching | MS 18.1.7 | Active |
| MRK-008 | Meraki MS (Core / Data Center) | Campus Core / DC Access Switching | MS 18.1.7 | Active |
| MRK-009 | Meraki MR (Wi-Fi 5 APs — legacy) | Wi-Fi 5 (802.11ac Wave 2) Access Points | MR 32.2.X | EOL-Pending |
| MRK-010 | Meraki MR (Wi-Fi 6 APs) | Wi-Fi 6 (802.11ax) Access Points | MR 32.2.X | Active |
| MRK-011 | Meraki MR (Wi-Fi 6E / Wi-Fi 7 APs) | Wi-Fi 6E / Wi-Fi 7 (802.11be) Access Points | MR 32.2.X | Active |
| MRK-012 | Meraki MV (Smart Cameras — Indoor) | Cloud-managed IP Surveillance / Video Analytics | Manual verification required | Active |
| MRK-013 | Meraki MV (Smart Cameras — Outdoor) | Cloud-managed Outdoor IP Surveillance | Manual verification required | Active |
| MRK-014 | Meraki MT (IoT Sensors) | IoT Environmental and Asset Monitoring | Latest GA | Active |
| MRK-015 | Meraki MG (Cellular Gateways) | Cloud-managed Cellular WAN / 4G LTE / 5G Gateway | MG 3.212 (stable) | Active |

EOL status: **14 Active · 1 EOL-Pending**

### DC & Compute — `cisco_dc_compute.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| DCC-001 | Cisco APIC (Application Policy Infrastructure Controller) | DC Network Policy Controller for ACI (Application Centric Infrastructure) | 6.1(5e) | Active |
| DCC-002 | Nexus 9000 in ACI Mode | ACI Leaf / Spine (DC Fabric) | 16.1(5e) | Active |
| DCC-003 | Cisco MDS 9100 Series | Small / Mid-size SAN (FC / FCoE) | 9.4(5) | Active |
| DCC-004 | Cisco MDS 9200 Series | Integrated SAN / IP Storage Access | 9.4(5) | Active |
| DCC-005 | Cisco MDS 9396 Series | High-density SAN (FC / NVMe-oF) | 9.4(5) | Active |
| DCC-006 | Cisco MDS 9700 Series | Large Enterprise / SP SAN Core | 9.4(5) | Active |
| DCC-007 | Cisco UCS B-Series Blade Servers | Enterprise / HPC Blade Server (2/4-socket) | 4.3 | Active |
| DCC-008 | Cisco UCS C-Series Rack Servers | Enterprise Rack Server (1U/2U) | CIMC 6.0.2.260143 | Active |
| DCC-009 | Cisco UCS X-Series Modular System | Next-gen Modular Compute (Blade replacement) | Intersight (SaaS) | Active |
| DCC-010 | Cisco UCS Fabric Interconnect 6400 Series | UCS Domain Fabric Interconnect (Network Foundation) | 4.3 | Active |
| DCC-011 | Cisco UCS Fabric Interconnect 6500 Series | UCS X-Series Domain Fabric Interconnect | UCSM 6.0 | Active |
| DCC-012 | Cisco HyperFlex HX220c | 2-Node Hyper-Converged Infrastructure (HCI) | 6.0(1x) | Active |
| DCC-013 | Cisco HyperFlex HX240c | High-density Hyper-Converged Infrastructure (HCI) | 6.0(1x) | Active |
| DCC-014 | Cisco HyperFlex Edge | HCI for Remote / Branch Sites (ROBO) | 6.0(1x) | Active |
| DCC-015 | Cisco ACI Multi-Site / Multi-Pod | Multi-DC / Multi-Cloud ACI Policy Management | 4.2.x | Active |

EOL status: **15 Active**

### Security Extended — `cisco_security_extended.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| SES-001 | Cisco Secure Email Gateway | Email Security / Anti-Spam / Anti-Malware / DLP (on-prem) | 16.0.4 HP2 | Active |
| SES-002 | Cisco Secure Email Cloud Gateway | Cloud Email Security / Anti-Spam / Anti-Malware / DLP (SaaS) | 16.0.4 | Active |
| SES-003 | Cisco Secure Web Appliance | Web Proxy / URL Filtering / Malware Protection / CASB (on-prem) | 15.2.3 HP1 | Active |
| SES-004 | Cisco Secure Email and Web Manager | Centralised Management for SEG and SWA | 15.x | Active |
| SES-005 | Cisco Secure Endpoint (Connector) | Endpoint Detection and Response (EDR) / AMP | 8.5.x (connector agent) | Active |
| SES-006 | Cisco Secure Endpoint Private Cloud | On-prem EDR Management Console | SaaS-equivalent (console 5.4.x) | Active |
| SES-007 | Cisco XDR (Extended Detection and Response) | Threat Detection / Investigation / Response (XDR / SOC Platform) | 2.64 (as of April 2026) | Active |
| SES-008 | Cisco Secure Access (SASE / SSE) | Secure Access Service Edge (SASE) / Security Service Edge (SSE) / ZTNA | 2026.1.x (continuous) | Active |
| SES-009 | Cisco Multicloud Defense | Cloud Workload Firewall / East-West Cloud Security | Continuous delivery | Active |
| SES-010 | Cisco ISA 3000 (Industrial Security Appliance) | OT / ICS Network Segmentation Firewall | FTD 7.x | Active |
| SES-011 | Cisco Cyber Vision | OT / ICS / IoT Asset Visibility and Threat Detection | 4.x | Active |
| SES-012 | Cisco Secure Firewall Management Center (FMC) | Centralised NGFW Policy and Threat Management | 7.6.6 | Active |

EOL status: **12 Active**

### Industrial / IoT — `cisco_industrial.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| IND-001 | Cisco Catalyst IE3100 Rugged Series | Industrial / Utility Access Layer Switching (DIN-rail) | 17.14.x | Active |
| IND-002 | Cisco Catalyst IE3200 Rugged Series | Industrial Access Layer Switching (DIN-rail / rack) | 26.2.x | Active |
| IND-003 | Cisco Catalyst IE3300 Rugged Series | Industrial Distribution Layer Switching | 26.2.x | Active |
| IND-004 | Cisco Catalyst IE3400 Rugged Series | Industrial Access / Distribution Switching (extended temp / IP67) | 26.2.x | Active |
| IND-005 | Cisco Catalyst IE9300 Rugged Series | Next-gen Industrial Distribution / Aggregation Switching | 26.2.x | Active |
| IND-006 | Cisco Catalyst IR1101 Rugged Router | Industrial IoT Edge Router / Cell Site Router (compact) | 26.2.x | Active |
| IND-007 | Cisco Catalyst IR1800 Rugged Series Routers | Industrial WAN Edge / IoT Aggregation Router | 26.2.x | Active |
| IND-008 | Cisco Catalyst IR8100 Heavy Duty Series | Industrial WAN Aggregation / SD-WAN Edge (large / outdoor) | 26.2.x | Active |
| IND-009 | Cisco IW6300 Heavy Duty Series (Wi-Fi 5) | Industrial / Outdoor Wi-Fi 5 (802.11ac) Access Point | 15.3.3-JQ (final maintenance) | EOL-Pending |
| IND-010 | Cisco Catalyst IW9165 / IW9167 Rugged Series | Industrial Wi-Fi 6 / Wi-Fi 6E Access Point (rugged outdoor) | 26.2.x | Active |
| IND-011 | Cisco Cyber Vision | OT / ICS / IoT Asset Discovery and Threat Detection | 4.x | Active |
| IND-012 | Cisco IC3000 Industrial Compute Gateway | Industrial IoT Edge Compute Gateway / Sensor Aggregation | 1.x | Active |
| IND-013 | Cisco IoT Operations Dashboard | Centralized IoT Device / Connectivity Management | Continuous delivery | Active |
| IND-014 | Cisco Kinetic for Cities / Kinetic (EOL) | IoT Data Processing / Edge Intelligence Platform | 2.x (final) | EOL |

EOL status: **12 Active · 1 EOL-Pending · 1 EOL**

### SP Mobile — `cisco_sp_mobile.csv`

| ID | Product Family | Use Case | Gold Version | EOL Status |
|---|---|---|---|---|
| SPM-001 | Cisco ASR 5000 | SP Mobile Packet Core — 4G LTE (legacy platform) | 21.28.x (legacy train) | EOL-Pending |
| SPM-002 | Cisco ASR 5500 | SP 4G LTE EPC / 5G NSA Core | 2026.03.gh1 | Active |
| SPM-003 | Cisco ASR 5700 | SP 4G LTE / 5G NSA Packet Core (high-density) | 2026.03.gh1 | Active |
| SPM-004 | Cisco Ultra Packet Core (UPC) — Virtual EPC | Virtualised SP 4G LTE EPC / 5G NSA Core (NFV) | 2026.03.gh1 | Active |
| SPM-005 | Cisco Ultra Cloud Core — AMF (5G SA) | 5G Standalone Core — Access and Mobility | 2026.x | Active |
| SPM-006 | Cisco Ultra Cloud Core — SMF (5G SA) | 5G Standalone Core — Session Management | 2026.x | Active |
| SPM-007 | Cisco Ultra Cloud Core — UPF (5G SA) | 5G Standalone Core — User Plane / Data Path | 2026.x | Active |
| SPM-008 | Cisco Ultra Cloud Core — PCF (5G SA) | 5G Standalone Core — Policy Control | 2026.x | Active |
| SPM-009 | Cisco BroadWorks | SP Cloud Calling Platform / UCaaS for Service Providers | Release 27 | Active |
| SPM-010 | Cisco IoT Control Center (formerly Jasper) | SP IoT / SIM / Connectivity Management Platform | Continuous delivery | Active |
| SPM-011 | Cisco Network Function Virtualization Infrastructure (NFVI) | SP NFV Infrastructure / ETSI NFV-compliant Cloud | 5.x | Active |

EOL status: **10 Active · 1 EOL-Pending**

<!-- AUTO-GENERATED:DATA-TABLES:END -->

## cisco_sources.csv — Source Reference

| Field | Description |
|---|---|
| `source_id` | Unique ID referenced in all product files |
| `description` | What the page covers |
| `platform_scope` | Which product(s) the source applies to |
| `url` | Direct URL to Cisco's release notes or documentation page |
| `last_verified` | Date this source was last checked |

<!-- AUTO-GENERATED:SOURCE-COUNT:BEGIN -->
**116 sources** (SRC-001 to SRC-116) covering all product files. Each product's `source_ids` field links directly to the pages needed for version refresh.

Next available source ID: **SRC-117**.
<!-- AUTO-GENERATED:SOURCE-COUNT:END -->

Fetch behaviour and known-good replacement URLs are recorded in `data/source_endpoints.yml` — read it before refreshing. Check URL health with `python3 tools/check_sources.py`.

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
| **RoomOS** | Webex Room / Board / Desk devices | `11.x` (e.g. 11.32.7.0) — 11.32 is the final RoomOS 11 train |
| **Meraki MX firmware** | Meraki MX, Z Series | `26.2.X` (current GA) / `19.2.X` (previous line) |
| **Meraki MS firmware** | Meraki MS Switches | `18.x.x` |
| **Meraki MR firmware** | Meraki MR APs | `32.x.x` (33.x train starting to ship) |
| **Meraki MV firmware** | Meraki MV Cameras | No machine-readable source — verify in the Dashboard |
| **Meraki MG firmware** | Meraki MG Cellular Gateways | `3.212` (stable) / `26.1` (**beta**) |
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

**Start here:** read `data/source_endpoints.yml`. It records the verified URL for every source, which ones are known-broken, and how each host behaves. That file saves rediscovering the Meraki taxonomy from scratch.

1. Run `python3 tools/check_sources.py` to find dead URLs.
2. For anything reported `DEAD`, look up the replacement in `source_endpoints.yml`.
3. Fetch the source and update `latest_version` and `gold_version` in the product CSV.
4. Update `last_verified` in `cisco_sources.csv` and `last_updated` in the product row.
5. Run `python3 tools/build.py && python3 tools/validate.py`.

**Fetching rules — these are not optional:**

| Host | How to fetch | Why |
|---|---|---|
| `cisco.com` | Integrated browser only | Returns **403** to `curl`/`requests`, even with a browser User-Agent. Bot-blocking, not a dead link. |
| `documentation.meraki.com` | Any HTTP client, then render | Serves requests normally but the body is JavaScript-rendered — raw HTML is empty. |
| `roomos.cisco.com` | Plain fetch works | Not bot-blocked; GitHub-sourced markdown. |

**Where to find gold versions.** Priority order:

1. TAC recommended-release pages (`source_endpoints.yml` lists which platform each covers)
2. Cisco release-notes list pages
3. Meraki `*_Firmware_Features_Directory` pages — the per-product `Firmware_Changelog` paths were retired in 2026

**Watch for Beta and Archive labels.** The Meraki MG directory lists `26.1` as *Beta* and `3.212` as *Stable*; the higher number is not automatically the better answer.

Recommended check frequency: **quarterly** — Cisco ships major releases every 6 months, with maintenance updates in between. Meraki firmware updates more frequently (monthly).

> **Note on SaaS products**: ThousandEyes, Umbrella, Duo, Webex Calling, AppDynamics, and Meraki Dashboard have no discrete version numbers — they use continuous delivery. Check each product's release notes/changelog page for recent changes.

---

## Data Currency

Versions verified against live Cisco and Meraki documentation: **29 September 2026** · Legacy product EOL dates sourced from Cisco EoL notices.

Coverage is uneven and deliberate. 97 of 164 rows were re-verified against a fetched source page on 29 September 2026; the remaining 67 have no machine-readable version source and were left unchanged rather than guessed. The `last_updated` column records which is which.

**Before trusting a version, note two traps:**

- A `curl` or scripted HTTP request to `cisco.com` returns **403** even for live pages. That is bot-blocking, not a dead link — confirm in a browser before replacing a URL.
- Cisco's "gold" (TAC-recommended) release is often *behind* the newest release, sometimes by a full major version. Secure Firewall gold is `7.6.6` while latest is `10.1.0`; that is Cisco's own "suggested release", not an error.

All source URLs are canonical Cisco.com or Meraki documentation pages — they remain stable even as new software versions are released.
