# Portfolio build journal — inception

**Date:** 2026-11-24 (America/Detroit)  
**Provenance:** Current ChatGPT project-planning conversation; this is a concise record of decisions, **not** a verbatim transcript.

### 2026-11-24 — New project proposed

- **Context:** Interview preparation suggested the value of presenting actual lab engineering through Grafana and other verified monitoring tools on a tablet.
- **User direction:** Create another project, jokingly named “Dios de Ignatio De Portfellatio”, for the technical portfolio.
- **Decision:** Separate the portfolio from interview practice; curate evidence-backed case studies instead of copying complete lab or interview archives.
- **Status:** Proposed architecture; no completed portfolio demonstration established.

### 2026-11-24 — Put it under DERP provenance

- **User direction:** “make this project under the derp provenance as a sub. We can share it. Documentation of building the portfolio will go in th eportfollio for our pipeline here”
- **Decision:** Use the existing **public** Derived-Entropic-Rememory-Protocol repository under `Projects/Technical-Portfolio/`. Keep the separate private telemetry and Bluebayou repositories unchanged.
- **Evidence:** GitHub repository metadata confirmed that Derived-Entropic-Rememory-Protocol is public and already documents a Markdown-first provenance pipeline; it uses `Projects/` for subprojects.
- **Status:** Repo destination confirmed; initial scaffolding pending commit at time of this entry's drafting.

### 2026-11-24 — Begin recording interactions

- **User direction:** “so lets get into that mind set now. Start recording our interactions and stuff, I'll keep it clean and succinct.”
- **Decision:** Maintain a concise, chronological build journal for substantive portfolio decisions, demonstrations, corrections and outcomes. Preserve original intent and corrections without treating summaries as verbatim transcripts.
- **Boundary:** Record deliberately during active sessions via repository commits; no claim of always-on or background capture.
- **Action:** Add project README, protocol, template and this inception journal.
- **Status:** Documentation scaffold created when the corresponding Git commit succeeds.
- **Next:** Select first verified portfolio case study and gather public-safe evidence, potentially Grafana/Prometheus monitoring recovery.

### Initial evidence candidates (not yet published)

| Candidate | Current classification | Rationale |
| --- | --- | --- |
| Prometheus crash recovery and Grafana observability | Historical / confirmed recovery in prior session outputs | Demonstrates analysis, backups, TSDB/WAL diagnosis and verification; needs sanitized evidence |
| DERP telemetry and Kibana | Partial historical evidence, deployment states vary | Distinguish real ingestion from unverified dashboard proposals |
| Windows / Linux / virtualization integration | Candidate only | Select bounded, well-evidenced implementations |
| Application security and risk management | Skills demonstrated in interview hypotheticals, not deployment evidence | No claims of live institutional security findings |

### Publication checklist

- Source and timestamps accounted for
- Implementation separated from brainstorming
- Institutional and home-lab details reviewed for publication
- Outcome grounded in logs, code or demonstration
- Corrections preserved

### 2026-11-24 — CHARON origin story: retrospective Sprint 1

- **Evidence type:** First-person retrospective recollection, recorded on 2026-11-24. Original event dates **not yet established** from the archive.
- **User's wording:** “I remember most of it. Charon started out just with 16 gigs of ram and hosting blue iris with local inference. After upgrading it, one day while installing kali on it, in vmware, I was like, this sucks, I want server. I wonder if we can install server in a vhdx and make it portable like I thought I read, then we did it, and I posted in ethical hacking class about the vhdx and how it makes images portable as fuck. That was basically sprint 1 -4d”
- **Sequence as remembered:** (1) CHARON initially had 16 GB RAM and ran Blue Iris with local inference; (2) hardware was upgraded (specifications/date pending); (3) installing Kali in VMware prompted a desire to move to a server OS; (4) explored installing Windows Server into a portable VHDX; (5) completed a VHDX-based installation; (6) discussed the portability of VHDX images in ethical hacking class.
- **Interpretation:** User refers to this formative sequence as **Sprint 1**; suffix “-4d” preserved above, duration **not independently established**.
- **Status:** **Historical recollection, uncorroborated** until dates, original discussion, hardware changes, boot configuration and class post can be traced to source records. Do not assume this is the later INFINITY VHDX migration.
- **Portfolio relevance:** Motivating problem → architecture investigation → implementation → knowledge sharing. Potential first-person systems-engineering case study once the archive corroborates details.
- **Next:** Search original converted ChatGPT history for CHARON's early RAM/Blue Iris configuration, VMware Kali discussion, VHDX installation and class commentary. Attach source references and correct chronology without overwriting this recollection.

### 2026-11-24 — TryHackMe learning-path clarification

- **User's wording:** “Lol I had gotten through nmap in try hackme and just stopped doing it for a while there”
- **Context:** Clarification offered while recounting CHARON's early evolution and the later Kali/VMware-to-server experiment.
- **Historical recollection:** The TryHackMe learning path had reached Nmap before a period of inactivity. The length and exact placement of that pause relative to CHARON's hardware upgrade and VHDX installation are not yet verified.
- **Status:** First-person recollection, pending archive reconciliation.
- **Editorial rule:** Do not conflate completing the Nmap material with completing TryHackMe, or assert that the pause caused the CHARON redesign.

### 2026-11-24 — From TryHackMe Nmap to home-LAN discovery

- **User's wording:** “we started doing our own nmaps on our own lan then”
- **Sequence clarified:** After reaching Nmap in TryHackMe and taking a break from that learning path, the user began applying Nmap to their own LAN. This is practical exploration of their own environment; no specific discovery or scan output has been supplied in this recollection.
- **Status:** Historical first-person recollection. Exact scan dates, commands, discovered hosts and relationship to CHARON's server migration remain to be reconciled against original records.
- **Portfolio significance:** Transition from a guided exercise to self-directed network discovery, later informing infrastructure mapping and lab expansion.
- **Next:** Find archived scan results or conversation records to reconstruct what the initial LAN scans actually revealed.

### 2026-11-24 — Hypothesis: LAN discovery led to the domain

- **User's wording:** “I think that is why we built a domain”
- **Context:** This follows the recollection that, after TryHackMe Nmap material, the user began conducting Nmap scans on their own LAN.
- **Proposed chronology:** Guided Nmap learning → hands-on LAN discovery → a decision to build an Active Directory domain. This is **the user's tentative explanation**, not an independently established causal chain.
- **Status:** **Hypothesis / historical recollection**, pending original conversation dates and records of domain deployment.
- **Interpretive possibility (not a recorded motive):** Centralized identity, naming, management and a more structured lab could have been benefits of a domain; do not assert these were the original reasons without evidence.
- **Next:** Locate initial LAN-scan discussions and first domain-controller setup records; use dated evidence to test the order and motives.

### 2026-11-24 — CHARON, THOTH and Grafana order: retrospective

- **User's wording:** “and it snowballed from there. I think the server came before grafana, as thoth was built on charon”
- **Recollection:** The infrastructure expanded organically following early LAN scanning and domain work. The user believes CHARON's server stage preceded the Grafana deployment and remembers THOTH being built on CHARON.
- **Status:** **Historical recollection / tentative chronology**, not yet verified. “THOTH was built on CHARON” is preserved as stated; the exact VM, container, installation or migration relationship is unknown and must not be inferred.
- **Working order to test:** CHARON server environment → THOTH built on CHARON → Grafana introduced. The order of domain deployment relative to those events remains unverified.
- **Next:** Correlate archived conversation timestamps, THOTH installation/deployment records, hypervisor configuration and first Grafana/Prometheus setup. Distinguish the original THOTH from its later standalone Linux-host state.

### 2026-11-24 — Original stack and ZBook Windows Server driver adaptation

- **User's wording:** “we we started all we had was blue iris, and neolink. Then we had to adjust windows server 2025 to work with the zbook, that is why test signing is enabled for the drivers to work. In this caseit was really just the joystick and mousepad, but we also had issues with the bluetooth and sound drivers I think”
- **Starting services (recollection):** Blue Iris and NeoLink were the original stack, before later observability and distributed components.
- **Subsequent engineering problem:** Adapt Windows Server 2025 for the HP ZBook hardware. User associates enabled Windows test-signing mode with getting the ZBook's pointing-device drivers working (joystick/pointing stick and touchpad).
- **Less-certain issues:** Bluetooth and audio driver trouble are recalled tentatively (“I think”); exact symptoms, resolution and whether test-signing was required for them have **not** been established.
- **Status:** Historical first-person recollection; original dates, driver package names, commands, boot configuration and outcomes require archive or system evidence. Do not generalize that every driver needed test-signing or that this is a recommended production setup.
- **Chronology note:** The initial Blue Iris + NeoLink baseline and later Server 2025 adaptation are distinct phases; their relationship to the earlier VMware/Kali and VHDX experiment needs reconciliation rather than forced ordering.
- **Portfolio angle:** Demonstrates hardware/OS compatibility troubleshooting and deliberate trade-offs when running a server OS on workstation hardware.
- **Next:** Find the earliest Blue Iris/NeoLink references and archived ZBook driver/test-signing diagnostics; distinguish a successful installation from any remaining Bluetooth or sound issues.

### 2026-11-24 — Grafana origins: Nest and smart-plug hypothesis

- **User's wording:** “I think it might have been nest, then we figured out the google fee, and said, smart plugs.”
- **Context:** In response to the question of which Grafana dashboard came first, the assistant proposed a HORUS bare-metal dashboard without establishing original creation dates. The user recalled an earlier Nest integration and a subsequent shift toward smart plugs after learning about a Google fee.
- **Working hypothesis:** Nest-related monitoring/integration → discovery of a Google-related cost or fee → pivot toward smart-plug monitoring. Whether each stage produced a Grafana dashboard, and the order relative to HORUS, are **not verified**.
- **Correction:** Retract the assumption that HORUS was the first Grafana dashboard. Preserve it as a candidate, not a confirmed first.
- **Status:** Historical first-person recollection / tentative chronology. Specific Google service, fee amount, dates, smart-plug brands, and earliest dashboard title are unknown.
- **Next:** Inspect early ChatGPT/Obsidian archive entries and Grafana dashboard creation metadata for Nest, Google integration costs, smart plugs and HORUS. Establish first *attempt*, first *functioning datasource*, and first *dashboard* separately.

### 2026-11-24 — Power telemetry earliest date recalled

- **User's wording:** “power goes back to 10/10”
- **Context:** Follow-up to the Nest → Google fee → smart-plug discussion about the origins of Grafana.
- **Observation reported by user:** Power monitoring data extends back to **October 10** (year and dashboard/data-source metadata not separately supplied in this message; likely referring to 2026 given discussion date, but do not treat as independently verified).
- **Status:** User-reported telemetry retention boundary / historical evidence lead, not yet confirmed by query or Grafana metadata. Does **not** establish the original dashboard creation date or the date collection first began.
- **Next:** Check power-series earliest timestamp, datasource retention and dashboard creation history, and compare with Nest and HORUS records.

### 2026-11-24 — Nest start date clarified

- **User's wording:** “we started with nest on 10/15”
- **Reported date:** Nest work began **October 15**; presumed year 2026 based on conversational context, not independently corroborated.
- **Reconciliation:** Earlier user report states power telemetry reaches back to **October 10**. Thus the reported power-data date predates the reported Nest start by five days, if both are from 2026. The working account “Nest → smart plugs” cannot be assumed to describe the initial start of power-data collection.
- **Status:** User-reported historical date anchors; original configuration dates, earliest telemetry timestamps and the creation date of the first Grafana dashboard remain unverified.
- **Next:** Retrieve dated Nest setup messages and earliest smart-plug/power ingestion records; distinguish data collection, dashboard creation and Google-fee discovery.

### 2026-11-24 — Weather app to concentrated Grafana work; maintenance digression

- **User's wording:** “so for that week after we did the weather app, we just hit fucking grafana hard dude.”
- **Historical recollection:** The weather app preceded a roughly week-long intensive period of Grafana development. Exact dates, dashboard creation order and overlap with the October 10 power-data and October 15 Nest anchors still need source reconciliation.
- **Digression:** User reported obsolete provisioned Grafana dashboards they could not remove in the UI, selected five for removal and three to preserve, and executed an inventory, quarantine and verification on THOTH.
- **Confirmed output:** Five dashboard JSON definitions quarantined; three keepers preserved; Grafana service active. User: “we are good to go” and subsequently “this freed up a little bit of ram in the container lol”. No quantified RAM delta.
- **Full scripts and copied terminal output:** [THOTH Grafana dashboard cleanup — 2026-11-24](../case-studies/2026-11-24-thoth-grafana-dashboard-cleanup.md).
- **User's subsequent note:** “our dashboard dashboard is getting busy” — observation about increasing dashboard index complexity, **not** a request to change the architecture during this digression.
- **Status:** Maintenance completed per user's confirmation; early Grafana chronology remains historical recollection pending archive records.
- **Next:** Return to the weather-app-to-Grafana period and identify the earliest creation timestamps/evidence.

### 2026-11-24 — Grafana visual evidence requested

- **User's direction:** “sien we will have a grafana section eventially, if fits. Ad this to documentations” (image attached in this conversation).
- **Decision:** Reserve this visual evidence for the eventual Grafana/observability portfolio section alongside the documented cleanup. Do not conflate the screenshot with the historical first Grafana dashboard.
- **Current evidence:** A user-shared image was supplied in this conversation, but its binary asset was not accessible to the repository-writing integration at this checkpoint. The image itself has **not** been published into GitHub; this entry is a provenance placeholder, not a claim of image preservation.
- **Related maintenance record:** [THOTH provisioned-dashboard cleanup](../case-studies/2026-11-24-thoth-grafana-dashboard-cleanup.md), containing the original command/terminal transcript.
- **Next:** Export or provide the screenshot as a file available for an actual image commit, review it for public-safe content and link it from the future Grafana case study. Keep the archive chronology as the main thread.
