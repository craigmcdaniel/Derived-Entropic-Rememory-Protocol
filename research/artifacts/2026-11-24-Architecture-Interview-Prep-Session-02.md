---
title: "Architecture & Interview Prep — Ephemeral Systems, StemCell Memory, and LCC Session 02"
date: 2026-11-24
timezone: America/Detroit
tags:
  - derp
  - cementic
  - architecture
  - stemcell
  - interview-prep
  - lcc
  - homelab
status: captured
---

# Session Context Summary — November 24, 2026

## Part 1: Systems Architecture & The DERP / Cementic Philosophy

### 1. Ephemeral Execution & Inverting Software Modularity
* **Core Thesis:** Flip traditional stateful software modularity (permanent client apps, bloated frontends, always-on background daemons) into **on-demand assembly**: `Intent → Git Repo Code → Ephemeral Execution → Stateless Display/I/O`.
* **`Roger_Roger` (`rgr2.sh` on `10.4.10.4`):**
  * **Current State:** Minimalist network daemon/listener answering `"roger roger"` when poked ("butter robot" v0.1).
  * **Target Role:** Lightweight LAN execution agent / MCP bridge. Receives structured intent, pulls vetted scripts from Git on the fly, executes scoped jobs (e.g., spinning up `python3 -m http.server` on `tvPort`), verifies port binding, logs the Git commit SHA, and tears down temporary processes when idle.
* **Stateless Display Endpoints:**
  * Treat any screen with a web browser and subnet route (e.g., living room smart TV hitting `http://10.4.10.4:tvPort`) as a zero-install thin client—bypassing app stores, sideloading, and self-signed SSL friction.
* **Blank-Vessel Hardware & PXE/Guacamole Bootstrapping (`:8776/hi`):**
  * **Edge Hardware (Raspberry Pi / ESP32):** Flash only network connectivity and a minimal listener on port `8776`. On `:8776/hi`, the node queries the GitHub repo tree and prompts: *"What DERP product would you like to load today?"*—pulling its role and scripts dynamically.
  * **Bare Metal & Remote Sharing:** Extend the same pattern to x86/Pi hardware via **iPXE netbooting** (stateless RAM `initramfs` loading directly from Git) and external demos via **ephemeral datacenter containers wrapped in Apache Guacamole** HTML5 sessions.

### 2. AI-Native OS, Kernel Shadowing & Unified Drivers
* **Separation of Hot Path vs. Control Plane:** Keep microsecond hardware interrupts, preemptive CPU time-slicing, memory paging, and `cgroups` inside a deterministic microkernel/HAL. Position the AI above the kernel to emulate userspace orchestration (`PID 1` / `systemd` / `cron`).
* **Shadow-Mode Training Loop:**
  1. Stream read-only kernel/userspace telemetry (`/proc`, `auditd`/`bpftrace`, `inotify`, socket bindings) to the AI.
  2. Have the AI predict scheduling/daemon actions without executing syscalls, scoring predictions against ground-truth `systemd`/kernel behavior.
  3. Run full AI-driven end-to-end stimulus and chaos tests inside isolated VMs (e.g., Proxmox guests with snapshots) to build an empirical topology map before graduated cutover.
* **Driverless / Unified AI Hardware Layer:** Treat hardware drivers as dynamic translation bridges—reading bus descriptors (PCIe, USB, I2C) to synthesize minimal, sandboxed micro-shims (e.g., eBPF) on the fly rather than maintaining static kernel driver trees.

### 3. DERPBooks v0.1 & Empirical Proof of Concept (Samsung Health Tombstones)
* **DERPBooks Ingestion Pipeline:**
  * Native text-layer PDFs eliminate the need for probabilistic OCR—extracting deterministic strings directly into an immutable PostgreSQL staging layer.
  * **Ingestion Guardrails:** Atomic folder states (`inbox/`, `processing/`, `staged/`, `quarantine/`), file-stability checks prior to read, `SHA-256` content-hash idempotency, and Git commit SHA provenance stamping.
* **Samsung Health Multi-Year Proof of Concept:**
  * Successfully processed **7 years (2019–2026)** of longitudinal Samsung Health exports (sleep, steps, HRV, heart rate min/max/avg) into immutable PostgreSQL tombstones using a repeatable, lifted ingestion script.
  * Visualized in **Grafana** with a parameterized Metric Explorer and a **Historical Coverage Density** panel to distinguish missing data gaps (e.g., 2021–2024) from zero-value flatlines.
  * **28-Thread Benchmark Lesson:** Compared 1 year under normal scheduling vs. `14×2` (28) parallel threads. All tombstones committed cleanly to PostgreSQL, but unthrottled concurrency caused interleaved logs and ~100× JSON data amplification (`1–2 MB` raw → `~200 MB` output)—empirically proving the need for atomic work-claiming (`FOR UPDATE SKIP LOCKED`) and state-aware scheduling.
  * **Future Expansion:** Shipping sealed PostgreSQL tombstones into **Elasticsearch/Kibana** alongside Suricata network logs for cross-domain anomaly correlation.

### 4. `O(1)` 360-Point Context Tensor & `StemCell` Data Capsules
* **Bounded Working Memory (`maxDataPoints = 360`):**
  * Modeled on Grafana's query engine: active memory never exceeds **360 points**, regardless of time horizon (`4-minute` resolution over 24 hours; `~5-day` rollups over 5 years).
* **Nested Multi-Scale Tensor & Recursive `"Show Me More"` Drill-Down:**
  * Embed high-resolution `24-hour` inner windows inside `5-year` outer macro trajectories across aligned cross-domain channels (biometrics, finance, network telemetry, agent logs).
  * Preserve bucket boundary keys / provenance pointers (`SHA-256`, Git commit SHA, timestamp/ID ranges) so the AI can spot macro outliers and execute targeted SQL drill-downs into raw cementic tombstones on demand.
  * Planned **Provenance Manager** to bridge Obsidian `.md` notes into PostgreSQL with full file/block hash and commit lineage if/when notes graduate to SQL.
* **`StemCell` (Infini-hedron) Year Capsules:**
  * Model each year (`2020..2026+`) as an undifferentiated, immutable capsule exposing a strict two-sided contract:
    * **`API_IN`:** Ingests and seals raw, provenance-stamped events into immutable tombstones.
    * **`API_OUT`:** Polymorphic trait/mixin interface that dynamically projects any required lens (360-point Grafana series, Kibana security feed, DERPBooks ledger, or scene tensor) on demand without mutating the underlying core.

### 5. Target Hardware & Infrastructure Vision
* **Compute Node:** Dual-socket 96-core Threadripper/EPYC (192 cores / 384 threads) + full-fat Blackwell workstation GPU (96GB ECC GDDR7) + 10Gb symmetrical business fiber.
* **Power & Cooling Envelope:** ~1,450W–1,650W peak draw (~200W–300W idle), requiring a dedicated **240V/20A** circuit, active heat exhaust, and ~**6–8 kW rooftop solar** on a standing-seam metal roof.
* **Vision & Scheduling Architecture:** Ingesting hundreds of dozens of camera streams + LiDAR point clouds (with felt-backed Styrofoam multipath dampening) by slicing the Blackwell GPU via **NVIDIA MIG (Multi-Instance GPU)** into hardware-isolated partitions served by competing Python worker arrays.

---

## Part 2: LCC Interview Prep — Session 01 & Session 02 Consolidated

### Target Role & Candidate Profile
* **Role:** Lansing Community College (LCC) — Technical Specialist / Information Security Specialist (`400 N Washington Sq, Lansing, MI 48933`).
* **Candidate Positioning:**
  * **Enterprise Dev Background (Accenture):** Built/supported State of Michigan systems (*MiChildSupport*, *Michigan Treasury Collections*) involving Oracle, J2EE, Bootstrap migrations, nightly encrypted batch processing, Section 508, and PCI/payment integrations.
  * **LCC Institutional Insider (2018–Present):** Active IT support with privileged access across Duo provisioning/reporting, Active Directory sync, Banner, and D2L.
  * **Hands-On Security & Lab:** Networking/cybersecurity coursework paired with Proxmox, VDI, Linux, honeypots, and Blue Iris/AI automation.

### Session 01 Recap (Core Principles)
1. **Phished Credentials & MFA:** Contain identity compromise immediately—revoke active Entra/M365/VPN session tokens (stolen session cookies bypass fresh MFA), reset credentials, preserve evidence, and audit M365 + VPN/Duo + Banner/Argos logs before concluding whether data was accessed.
2. **Legacy Web Apps & Attack Surface:** Follow `Inventory → Ownership → Exposure → Exploitability/Business Impact → Remediation → Monitoring`. Use authorized, least-disruptive validation and staging clones rather than aggressive testing against production.
3. **Academic Stakeholder Liaison (Legacy WordPress):** *"Hosting !== maintaining."* Keep functional department apps running while reducing dependency sprawl (strip unused external lookups, fix asset paths via env vars), move hosting into a managed container/control plane with Grafana monitoring, and keep content ownership with the existing BA.
4. **Risk Prioritization & Continuity:** Anchor priority in institutional survival (**Title IV financial aid, accreditation, FERPA student data**) rather than CVSS score alone. Apply short-term containment on public attack paths while scheduling high-impact backend fixes, and reschedule change windows when business-critical student deadlines emerge.
5. **DLP & Workflow Remediation:** Evaluate DLP tuning by analyst triage cost, operational interruption, and missed real exposures—not raw false-positive counts. Track repeat recurrence, severity trends, and coaching effectiveness for CIO reporting. Partner with BAs to move sensitive spreadsheets from email attachments into properly scoped SharePoint workflows.

### Session 02 Drills & Sharpened Answers
1. **Dual-Role IAM Offboarding (Student + Employee):**
   * **Mechanism:** Disable the employee **`star.lcc.edu`** domain account and revoke active session tokens while leaving the student **`.mail.lcc.edu`** Microsoft identity intact. Audit SharePoint/IAM groups for manual student-account grants and tie `star` deprovisioning to Banner/HR termination dates.
2. **Risk Acceptance vs. Governance Authority:**
   * **Boundary:** A Department Chair can accept localized operational risk, **not** institutional regulatory or compliance exposure (**PCI-DSS, Title IV financial aid accreditation, FERPA**), which requires ISO/CISO/executive review.
