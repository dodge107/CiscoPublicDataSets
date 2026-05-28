# /update-cisco-data

Update the Cisco product datasets with the latest software versions, gold (TAC-recommended) versions, new products, and refreshed source URLs. Then update the README counts and the `last_verified` dates in `cisco_sources.csv`.

## Arguments

`$ARGUMENTS` can be:
- empty / `all` — update every product file
- a file stem, e.g. `campus_switching`, `dc_switching`, `enterprise_routing`, `sp_routing`, `wireless`, `security`, `sdwan`, `meraki`, `collaboration`, `dc_compute`, `security_extended`, `industrial`, `sp_mobile`, `sp_extended`, `software`
- a category keyword, e.g. `switching`, `routing`, `wireless`, `security`, `meraki`, `collab`, `sp`, `industrial`, `compute`, `sdwan`

## How to run this update

Read CLAUDE.md first to understand the schema, conventions, and gold-version rules. Then follow the steps below exactly.

---

### Step 1 — Read current state

Read ALL product CSV files and `cisco_sources.csv` to understand what is currently recorded before making any changes. Note the highest existing SRC-xxx ID so you know where to start for new sources.

```
Files to read:
  data/cisco_campus_switching.csv
  data/cisco_dc_switching.csv
  data/cisco_enterprise_routing.csv
  data/cisco_sp_routing.csv
  data/cisco_wireless.csv
  data/cisco_security.csv
  data/cisco_sdwan.csv
  data/cisco_software.csv
  data/cisco_sp_extended.csv
  data/cisco_collaboration.csv
  data/cisco_meraki.csv
  data/cisco_dc_compute.csv
  data/cisco_security_extended.csv
  data/cisco_industrial.csv
  data/cisco_sp_mobile.csv
  data/cisco_sources.csv
```

---

### Step 2 — Launch parallel research agents

Spawn one Agent per domain group below. Run ALL groups in a single message so they execute concurrently. Each agent must use WebSearch and WebFetch to retrieve LIVE data from Cisco.com (or Meraki docs). Do not rely on training data for version numbers.

#### Agent instructions to pass (adapt scope if $ARGUMENTS limits to a subset):

**Agent A — Campus Switching & Wireless**
Research the following from cisco.com. For each platform family find:
1. The absolute LATEST software release (any train)
2. The TAC-recommended / gold release (check the "Recommended Releases" TAC doc for that platform — this is the most important value)
3. Any new product families announced since the last update
4. Confirm the release notes list URL still resolves (HTTP 200)

Platforms: Catalyst 9200, 9300, 9400, 9500, 9600, 3850, 3650, 2960-X, 1000, 1300, Catalyst 9800 WLC (all variants), Catalyst 9100 APs, Aironet

Key TAC recommended-release pages to fetch:
- https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9300-series-switches/214814-recommended-releases-for-catalyst-9200-9.html
- https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/214749-tac-recommended-ios-xe-builds-for-wirele.html

Return structured data: product_family | latest_version | gold_version | source_url_still_valid (yes/no) | notes

---

**Agent B — DC Switching, Enterprise Routing & SD-WAN**
Research the following from cisco.com:
1. Latest release and TAC-recommended/gold release for each platform
2. New product families in each area
3. Confirm release notes URLs resolve

Platforms: Nexus 9300, 9500, 7000/7700, 3000/3100, 3500, 2000 FEX; ISR 4000, ISR 1000, Catalyst 8200/8300/8500, ASR 1000, CSR/C8000V; SD-WAN vEdge/cEdge/Controllers

Key pages:
- https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-16/215567-recommended-releases-for-asr1000-isr400.html
- https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/recommended_release/b_Minimum_and_Recommended_Cisco_NX-OS_Releases_for_Cisco_Nexus_9000_Series_Switches.html
- https://www.cisco.com/c/en/us/support/docs/routers/sd-wan/215676-cisco-tac-and-bu-recommended-sd-wan-soft.html

Return: product_family | latest_version | gold_version | source_url_ok | notes

---

**Agent C — SP Routing (IOS-XR platforms)**
Research from cisco.com:
1. Latest and gold IOS-XR release for each platform
2. Any new NCS/ASR/Cisco 8000 platforms announced
3. URL validation

Platforms: ASR 9000, ASR 9900, NCS 5500, NCS 55A1/55A2, NCS 540/560, NCS 5000, NCS 1000, NCS 2000, NCS 4000, Cisco 8000, Cisco 8800, XRv 9000, vBNG, ASR 920, ASR 901

Key pages:
- https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xr-software/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/routers/asr-9000-series-aggregation-services-routers/products-release-notes-list.html
- https://www.cisco.com/c/en/us/td/docs/routers/iosxr/release-notes/25xx/cisco-ncs5500-series-routers-release-notes-2542.html

Return: product_family | latest_version | gold_version | source_url_ok | notes

---

**Agent D — Security (Firewall, Email, Web, Endpoint, XDR)**
Research from cisco.com:
1. Latest and gold release for each platform
2. Any new secure firewall hardware announced
3. URL validation

Platforms: ASA 5500-X, ASAv, Secure Firewall 1000/2100/3100/4100/4200, Firepower 9300, FMC/FMCv, Secure Email Gateway, Secure Web Appliance, Secure Email & Web Manager, Secure Endpoint, XDR, Secure Access (SASE), Multicloud Defense, ISA 3000, Cyber Vision, ISE

Key pages:
- https://www.cisco.com/c/en/us/support/security/firepower-ngfw/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/security/email-security-appliance/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/security/identity-services-engine/products-release-notes-list.html

Return: product_family | latest_version | gold_version | source_url_ok | notes

---

**Agent E — Meraki**
Research from the Meraki firmware feed and documentation.meraki.com:
1. Latest GA firmware for MX, MS, MR, MV, MG (and Z series)
2. Recommended/stable firmware for each (often differs from latest GA)
3. Any new Meraki product families
4. Confirm changelog URLs resolve

Key pages:
- https://community.cisco.com/t5/meraki-firmware-upgrades-feed/bg-p/networking-firmwareupgrades
- https://documentation.meraki.com/MX/MX_Overview_and_Specifications/MX_Firmware_Changelog
- https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS_Firmware_Changelog
- https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR_Firmware_Changelog

Return: product_family | latest_version | gold_version | source_url_ok | notes

---

**Agent F — Collaboration, DC/Compute & Software Platforms**
Research from cisco.com:
1. Latest and gold release for each platform
2. Any new product families
3. URL validation

Platforms:
- Collab: CUCM, Unity Connection, Expressway, CMS, IP Phones 6800/7800/8800, Webex devices (RoomOS), CUBE, Webex Calling, Jabber
- DC/Compute: APIC, ACI Nexus, MDS 9000, UCS B/C/X-Series, UCS FI 6400/6500, HyperFlex, NDO
- Software: Catalyst Center, ISE, NSO, Crosswork, ThousandEyes, Secure Network Analytics, Secure Client, Intersight, Secure Workload, AppDynamics, Prime Infrastructure

Key pages:
- https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/cloud-systems-management/dna-center/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/storage-networking/mds-9000-nx-os-san-os-software/products-release-notes-list.html
- https://collaborationhelp.cisco.com/article/en-us/nx3gh4

Return: product_family | latest_version | gold_version | source_url_ok | notes

---

**Agent G — Industrial & SP Mobile Core**
Research from cisco.com:
1. Latest and gold release for each platform
2. Any new OT/industrial platforms or 5G core products announced
3. URL validation

Platforms:
- Industrial: IE3100/3200/3300/3400, IE9300, IR1101, IR1800, IR8100, IW6300, IW9165/9167, Cyber Vision, IC3000, IoT OD
- SP Mobile: ASR 5000/5500/5700, Ultra Packet Core (VPC), Ultra Cloud Core AMF/SMF/UPF/PCF, BroadWorks, IoT Control Center

Key pages:
- https://www.cisco.com/c/en/us/support/switches/catalyst-ie3400-rugged-series/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/routers/catalyst-ir1800-rugged-series-routers/products-release-notes-list.html
- https://www.cisco.com/c/en/us/support/unified-communications/broadworks/products-release-notes-list.html

Return: product_family | latest_version | gold_version | source_url_ok | notes

---

### Step 3 — Apply updates to CSVs

Wait for all agents to complete. Then for each product row where the agent found updated data:

1. Update `latest_version` with the newest available release
2. Update `gold_version` with the TAC-recommended/suggested release (from the TAC recommended-release page, not just the newest release)
3. Update `eol_status` if a new EoL announcement was found
4. Add new product rows for any new platform families found, continuing the file's ID sequence
5. Add a note in the `notes` field if the status changed significantly (e.g., "EOL announced MM/YYYY")
6. Set `last_updated` to today's date (YYYY-MM-DD) for every row you modify or add. Do not touch `last_updated` on rows where nothing changed.

**Do not change any field that the agent did not find updated data for.**

**Note on product IDs:**
All product IDs use a uniform `XXX-NNN` format (3-letter domain prefix + 3-digit zero-padded sequence). IDs are globally unique across all files and appear unchanged in `cisco_all_products.csv`. When adding new rows, continue from the last NNN in the relevant file. Current ranges are documented in CLAUDE.md.

---

### Step 4 — Update data/cisco_sources.csv

For every source URL that was validated by the agents:
- Update `last_verified` to today's date (YYYY-MM-DD)

For any new source URLs needed by new products:
- Add new rows continuing the SRC-xxx sequence (check the highest existing ID first)
- Fill all fields: source_id, description, platform_scope, url, last_verified

---

### Step 5 — Regenerate cisco_all_products.csv

After updating individual product CSVs, regenerate the combined all-in-one file using Python (do NOT use shell pipes — they risk RTK output injection):

```python
import csv, os
files = [
    'cisco_campus_switching.csv','cisco_dc_switching.csv','cisco_enterprise_routing.csv',
    'cisco_sp_routing.csv','cisco_wireless.csv','cisco_security.csv','cisco_sdwan.csv',
    'cisco_software.csv','cisco_sp_extended.csv','cisco_collaboration.csv','cisco_meraki.csv',
    'cisco_dc_compute.csv','cisco_security_extended.csv','cisco_industrial.csv','cisco_sp_mobile.csv'
]
os.chdir('/Users/roy/AIProjects/CiscoPublicDataSets/data')
header, rows = None, []
for f in files:
    with open(f, newline='', encoding='utf-8') as fh:
        file_rows = list(csv.reader(fh))
        if header is None:
            header = file_rows[0]
        rows.extend(file_rows[1:])
with open('cisco_all_products.csv', 'w', newline='', encoding='utf-8') as out:
    w = csv.writer(out)
    w.writerow(header)
    w.writerows(rows)
```

---

### Step 6 — Update README.md and CLAUDE.md

Recount rows per file using the updated CSVs and update:
1. The file table in README.md (Rows column) — including the cisco_all_products.csv total row
2. The total product entries count in README.md
3. The "Data Currency" date at the bottom of README.md
4. The "Current Range" column in CLAUDE.md's file table if any range endpoints changed

Do not rewrite any other section of the README unless a new OS type was added.

---

## Quality rules

- **Gold version takes priority** over latest version for the `gold_version` field. If Cisco's TAC recommended-release page says 17.15.5 but 26.1.x is available, then `latest_version=26.1.x` and `gold_version=17.15.5`.
- **Never guess PIDs.** Only add PIDs you found explicitly in Cisco documentation.
- **Never mark EOL** without a Cisco EoL announcement link.
- **Do not update `last_verified`** for a source unless the agent actually fetched and confirmed the page.
- **Always stamp `last_updated`** (today's date) on every product row you modify or add. Leave it unchanged on unmodified rows.
- **Preserve all existing notes** — append to them rather than replacing.
- **SaaS / continuous-delivery products** (ThousandEyes, Umbrella, Duo, Meraki Dashboard, Webex Calling, XDR): `latest_version` and `gold_version` should both be `Continuous delivery (SaaS)` unless Cisco publishes discrete version numbers.
- **Always regenerate cisco_all_products.csv** (Step 5) after any product CSV changes. Use the Python script — never shell pipes.
