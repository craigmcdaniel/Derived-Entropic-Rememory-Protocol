---
title: "DERP Continuity — Portable Points of Truth and Continuity as a Service"
date: 2026-11-24
timezone: America/Detroit
status: concept-paper-v0.1
classification: proposed-architecture-and-business
tags: [derp, continuity, disaster-recovery, zbook, vdi, guacamole, hybrid-cloud, provenance]
---

# DERP Continuity
## Portable Points of Truth — Continuity as a Service

**Concept paper | v0.1 | November 24, 2026**

> **The workstation is replaceable. The working environment is portable. The authoritative records survive both.**

**Evidence status:** This is a proposed product architecture based on existing home-lab experience and brainstorming. It is not a deployed commercial service, audited SLA, independent security assessment, or market-tested pricing model.

## Executive summary

DERP Continuity combines **leased HP ZBook workstations**, **browser-accessible virtual desktops and applications**, **portable endpoint brokerage**, and **verified recovery services**. Customers receive a managed working environment rather than merely rented hardware.

The ZBook is a *portable access point to the source of truth*, not necessarily the authoritative data store. Its job is to connect an authorized person to appropriate services while remaining rapidly replaceable. The application or desktop may run on local hosting, a secondary site, or eventually AWS. Versioned manifests, monitored dependencies, backups, and reproducible recovery tests make the arrangement auditable.

Commercially this combines **Workstation as a Service (WaaS)**, **Desktop as a Service (DaaS)**, **Business Continuity as a Service (BCaaS)**, and selected **Disaster Recovery as a Service (DRaaS)** capabilities.

**Core selling proposition:** We maintain the customer's ability to resume work and demonstrate that capability with repeatable recovery exercises.

## 1. The problem

A small organization may have backups but no practical way to restore employees' ability to work after its computers, servers, building, or network fail. Replacing a workstation can involve rebuilding applications, remapping shares, recovering configuration, and reconstructing undocumented procedures. A storage copy alone does not restore the business.

DERP Continuity addresses three separable failures:

| Failure | What must survive | Recovery approach |
|---|---|---|
| Endpoint failure | Employee access and approved configuration | Replace/reassign ZBook; reconnect to same environment |
| Hosted service failure | Applications, desktops, identity, dependencies | Recover or redirect workloads to alternate compute |
| Data/site failure | Authoritative information and business operations | Verified restoration/replication and alternate worksite/network |

A broker cannot manufacture an unavailable service. Access continuity is only as strong as the reachable execution, identity, data, and connectivity layers behind it.

## 2. Design principle: separate five planes

1. **Access plane:** Leased ZBooks, thin clients, browsers, local networking and protected connections. Devices are replaceable and retain minimal customer state.
2. **Execution plane:** RDS/VDI desktops, applications, databases, and workers hosted on local virtualization or other capacity.
3. **Data plane:** Designated authoritative datasets and protected backups. Cached displays and telemetry are not automatically systems of record.
4. **Control plane:** Customer-specific deployment manifests, inventories, service registries, authorizations, recovery policies, and orchestration workflows.
5. **Evidence plane:** DERP provenance—what was observed, when, on what system, under which configuration, and whether a recovery test actually passed.

Separating responsibilities early makes a later change of hosting location a deployment choice instead of a wholesale rewrite.

## 3. Reference architecture

```text
            CUSTOMER WORKSITE / ALTERNATE WORKSITE
      +----------------------------------------------+
      | Leased ZBooks / browser endpoints            |
      | Minimal durable state, managed identity      |
      +----------------------+-----------------------+
                             |
                   protected connectivity
                             |
                 +-----------v-----------+
                 | Access broker/gateway |
                 | Guacamole + RDP/other |
                 +-----------+-----------+
                             |
               +-------------+--------------+
               |                            |
      +--------v---------+         +--------v---------+
      | Local hosted VDI |         | Recovery location|
      | Apps / services  |         | Secondary / AWS  |
      +--------+---------+         +--------+---------+
               |                            |
               +-------------+--------------+
                             |
         +-------------------v----------------------+
         | DERP continuity control + evidence planes|
         | Inventory / manifests / health / tests   |
         | Backup verification / incident timelines |
         +------------------------------------------+
```

This diagram is a **target topology**. Failover of the gateway, VPN, identity provider, DNS, network and backups must be addressed separately. A diagram with two sites does not prove independent failure domains.

### Service manifest concept

```yaml
# CONCEPTUAL EXAMPLE — not a production configuration
customer_id: example-co
service_profile: office-standard
desktop:
  primary_target: local-vdi-pool
  recovery_target: secondary-vdi-pool
  health_check: desktop-login-test
data:
  authoritative_location: customer-file-service
  backup_policy: documented-customer-policy
recovery:
  runbook: docs/runbooks/example-co-recovery.md
  approval_required: true
  last_verified_restore: null
provenance:
  manifest_revision: git-commit-sha
```

Public Git may hold generic schemas, reusable code and research. Customer manifests, sensitive topology, identity records, secrets, backups, logs and private financial data belong in access-controlled storage.

## 4. The ZBook fleet: a portable access fabric

A dozen ZBooks are not twelve copies of a customer's server. They are **twelve interchangeable entry points**, subject to inventory and capacity. Some are leased to employees, some are staged as replacement units, and some can serve as temporary worksite access terminals.

Possible roles:

- Daily leased workstation: browser or thin-client session into assigned services.
- Hot spare: a replacement device prepared for rapid customer reassignment.
- Recovery-site access node: makes a recovered desktop available away from the failed office.
- Test/staging node: validates access, peripheral compatibility and continuity procedures.
- Optional limited edge service: a carefully scoped cache or broker when network conditions require it.

A parallel fleet can serve multiple users and customer sites simultaneously. It **does not automatically combine RAM, CPUs or GPUs** into one machine. Job clustering would be an optional, separate feature with its own scheduler and failure handling.

### The portable point-of-truth distinction

A device can **discover and verify** an authoritative service without *containing* its authoritative records. Replacing a ZBook should not rewrite or migrate the customer's data. That is the economic and operational advantage.

## 5. From local hosting to hybrid recovery

### Phase A — Local pilot

Use existing lab virtualization, Guacamole, monitoring and versioned configuration to provision a small synthetic customer environment. Prove replacement of one endpoint and recovery of one desktop/application without manual reconstruction.

### Phase B — Independent recovery location

Introduce a genuinely separate failure domain, verified backup copy, secure remote access, and tested alternate compute. Measure end-to-end restoration—not just whether a backup job finished. This may be a second physical site or cloud environment.

### Phase C — Hybrid AWS

Replicate selected backup and recovery assets; pilot restoration of a service into AWS; prove connectivity, identity, DNS and data integrity. Start with recovery-oriented capacity and move production only where operations and economics justify it.

### Phase D — Cloud-primary, if justified

Keep customer-facing access and configuration portable. Deploy workloads to the most appropriate location while retaining tested failback and avoiding dependence on undocumented manual steps.

**Do not confuse mirroring with resilience:** Synchronizing corrupt data or configuration can spread a problem. Recovery needs version history, protected copies, clear recovery points and restore testing.

## 6. Recovery service promises and evidence

Define RPO (maximum acceptable data loss) and RTO (maximum acceptable restoration time) **per service**, not as a vague blanket claim. Also specify the customer prerequisites: internet access, identity availability, licensed applications, local network equipment and workable endpoint connectivity.

Every rehearsal should produce a recovery record:

| Evidence | Why it matters |
|---|---|
| Incident/test ID and timestamp | Traceable exercise |
| Customer/workload manifest revision | Know precisely what was tested |
| Last good backup and integrity result | Establish restoration point |
| Failure injected or simulated | Identify the tested scenario |
| Actual recovery start/end | Measure observed RTO |
| Recovered data timestamp | Measure observed RPO |
| Desktop login and application tests | Confirm usability, not only VM boot |
| Errors, operator interventions and rollback | Identify hidden manual dependencies |
| Participant signoff and follow-up tasks | Make findings actionable |

DERP's evidence methodology is a differentiator **only if records remain faithful to what actually occurred**.

## 7. Commercial packaging and preliminary economics

Potential bundles:

| Offer | Included idea |
|---|---|
| Managed Endpoint | ZBook lease, maintenance, inventory, replacement workflow |
| Managed Desktop | Hosted desktop/app access plus endpoint management |
| Continuity | Monitoring, backups, runbooks and periodic recovery tests |
| Enhanced Recovery | Dedicated alternate compute, tighter recovery targets and incident support |

Revenue is recurring; costs are not trivial. The model must account for acquisition/depreciation of ZBooks, spares, batteries, shipping, licensing, hosting, backup retention, power, network redundancy, support labor, insurance, taxes, and incident-response time.

**Pricing is not validated.** Do not mistake an illustrative monthly fee or an AWS estimate for a positive contribution margin. Model cost per concurrent desktop, peak utilization, expected hardware replacement, support hours, storage growth, and disaster-scenario capacity before selling an SLA.

An important commercial issue is **Microsoft service-provider and desktop virtualization licensing**; Windows Server RDS and hosted Windows client OS rights are different questions. Evaluate licensing with the appropriate provider before any customer deployment. Review third-party open-source licenses, redistribution, branding, data-processing obligations, cyber-insurance terms, and customer contracts.

## 8. Minimum viable pilot

**Goal:** Show that one external participant can replace an endpoint and recover a usable desktop/application without reconstructing the environment by hand.

**Scope:** One synthetic or explicitly authorized pilot customer, two ZBooks, one hosted desktop/application, one designated recovery target, and documented service dependencies.

**Exercises:**

1. **Endpoint swap:** Kill or remove ZBook A; assign ZBook B; verify login, documents, app session and permissions.
2. **Desktop-host outage:** Disable the primary hosted desktop; recover it elsewhere; prove application usability.
3. **Data restore:** Recover from a specified backup point; verify record accuracy and evidence trail.
4. **Access-path failure:** Test gateway/connectivity loss; document exactly which operations can continue and which cannot.
5. **Fresh operator rehearsal:** Have someone other than the system builder follow the runbook; record missed steps and undocumented assumptions.

**Success criteria:** Repeatable execution, independently reviewable evidence, measured RTO/RPO for tested scenarios, no unreported data loss, and a credible operational cost profile.

**No claim of instant failover** until the end-to-end event is actually demonstrated.

## 9. Existing foundations versus gaps

The following are **historical home-lab foundations reported in this research context**, not claims that a commercial service is already running:

- Windows domain, Hyper-V/RDS and VDI experience; VDI01/HYDRA examples.
- HORUS Proxmox and virtualization experimentation.
- Guacamole/reverse-proxy experience.
- THOTH Grafana/Prometheus/Loki and PostgreSQL patterns.
- Git/Markdown/Obsidian-based documentation and evolving DERP provenance conventions.
- ZBook hardware experimentation and proposed endpoint-broker fleet.

**Unverified or not yet built for customers:** fleet provisioning and lifecycle management, customer isolation, commercially valid licensing, identity recovery, redundant network/control plane, independent backup location, automated recovery, audited security practices, contracts, service desk processes and measured SLAs.

## 10. Risks and design constraints

- **Single-host risk:** A large INFINITY host—even with proposed 256 GB RAM—is still one failure domain.
- **Control-plane dependence:** Git, secrets, identity, DNS, access proxy and manifests need recoverable paths.
- **Tenant isolation:** Cross-customer data exposure is unacceptable; start with strong isolation and narrow scope.
- **Network dependence:** Remote VDI cannot be assumed usable during ISP outages; alternate connectivity may be required.
- **Licensing:** Hosted desktops and multi-customer services require proper entitlement analysis.
- **Endpoint security:** Replaceable does not mean unmanaged; device and session trust still matter.
- **Overpromising:** Distinguish backup, restore, warm standby, active failover and business continuity explicitly.
- **Business economics:** A major incident can create simultaneous support and capacity demand from multiple customers.
- **Data sovereignty and privacy:** Customer records must stay in authorized systems with contractually clear retention and access.

## 11. Open research questions

1. Is the first market local professional offices, small nonprofits, or technical teams with documented remote-work needs?
2. Does a pilot require hosted Windows applications, or can a Linux/browser-only workflow reduce initial licensing complexity?
3. Which access and identity dependencies survive loss of the primary site?
4. Which applications are realistically portable, and which have site-bound licensing or hardware constraints?
5. What is the minimum useful broker configuration on a ZBook?
6. What RTO/RPO can be *demonstrated* at different price tiers?
7. How will fleet inventory, chain of custody, secure wiping and device replacement be documented?
8. At what customer count does secondary-site/AWS capacity improve reliability and economics?
9. Can a new technician execute a recovery using only the DERP-maintained runbook and artifacts?

## 12. Proposed next milestone

**Build a one-customer, two-endpoint, two-host recovery demonstration using synthetic data.** Archive the configuration, test procedure, observed results, failure cases, and Git revision as a versioned DERP exhibit. This converts a persuasive architecture into defensible evidence without presuming commercial readiness.

---

### Reality-check note

This document contains *concepts* and *historical claims* but no secretly planted fictional deployment facts. Any future breadcrumb tests should use explicitly labeled synthetic fixtures kept separate from customer operating records.

### Closing statement

**We are not leasing a laptop. We are delivering a replaceable doorway into a managed, recoverable working environment.**

**DERP Continuity: Portable Points of Truth — Continuity as a Service.**

---

## Addendum A — Disconnected edge operations and reconciliation

**Captured:** 2026-11-24  
**Status:** Proposed design extension; no McDonald's integration, authorized POS access, offline payment capability, or deployed retail pilot is claimed.

### Scenario and boundary conditions

A retail restaurant loses electricity, local networking and/or WAN connectivity. Physical operations (kitchen equipment, refrigeration, power-dependent terminals and switches) may remain unavailable; VDI cannot make unpowered equipment function. A usable continuity design must account separately for portable/backup power and an alternate network path such as cellular uplink. Access to another operational location is a third fallback.

Retail **back-office workflows**—scheduling, management reports, local inventory workflows—are more suitable for browser/VDI recovery. **Front-counter POS**, payment acceptance, kitchen coordination and time-sensitive operations may require vendor-approved local applications, bounded latency and offline transaction handling. A generic cloned database is not a replacement for a proprietary POS/payment service.

### Proposed local shadow-store pattern

```text
        Central authoritative data / application
                     ^            |
              accepted deltas   versioned snapshot
                     |            v
               [sync/reconcile service]
                        |
                  local edge node
            +-----------+-----------+
            | scoped working replica |
            | append-only outbox     |
            | local app services     |
            +-----------+-----------+
                        |
             leased endpoints / terminals
```

**Lifecycle:** (1) provision a scoped baseline snapshot and checkpoint; (2) permit only explicitly authorized offline actions; (3) journal every mutation as an immutable event with unique idempotency key, local sequence, origin, actor, schema version, timestamp and base revision; (4) on reconnection submit pending events and fetch authoritative changes; (5) validate, deduplicate, reconcile conflicts and record per-event acknowledgments; (6) advance checkpoints only after durable commit and read-back verification. Protect local data at rest and provide a retention/deletion policy after successful sync.

The edge journal records **what the local site did**. It does not imply a central system has accepted the change. Maintain statuses such as `local_pending`, `submitted`, `accepted`, `conflicted`, and `rejected`. Preserve immutable evidence of failed or retried operations.

### Failure cases to exercise

| Failure | Expected policy |
|---|---|
| Split brain: concurrent edits upstream and offline | Version-aware merge or explicit review; never overwrite silently |
| Network returns midway through batch | Idempotent retry with atomic checkpoint advancement |
| Clock drift between edge and central | Don't use wall-clock ordering as sole consistency rule |
| Schema/permissions changed while offline | Block incompatible replay pending migration or review |
| Offline device stolen, damaged or exhausted | Protect journal, minimize local data and document unrecoverable unsynced changes |
| Upstream sends corrupt/canceled data | Validate events and preserve prior checkpoints, don't blindly replicate |
| Offline card payment attempted | Use only provider-approved offline capabilities, controls and reconciliation; no generic financial database replay |

### Target pilot: network partition, then reconnect

Use **synthetic orders and inventory data** on an isolated local service with no real payment integrations. Establish central baseline; disconnect WAN; create several new local transactions; concurrently edit an upstream record; reconnect; verify unique event acceptance, conflict detection, exact count/hash reconciliation, no duplicate postings after retry, and a complete DERP evidence trail. Repeat with a power interruption using protected storage.

**Hypothesis:** A narrow, append-only edge working set plus explicit reconciliation can preserve selected business operations across temporary WAN failure. **Not yet proven** for any particular customer, POS platform, or outage scenario.

**Architectural consequence:** Continuity now has a sixth optional, tightly scoped function: **disconnected edge execution and reconciliation**, spanning execution/data/evidence planes. This must remain separate from guaranteed failover and physical power continuity.

---

## Addendum B — Battery-backed continuity appliance

**Captured:** 2026-11-24  
**Status:** Proposed power-resilience bundle; no field installation, customer deployment, certified product selection, or runtime test.

### Core idea

Bundle a **nominal 10 kWh battery bank**, appropriately rated inverter/transfer equipment, a ZBook access broker, a scoped offline-capable datastore, protected LAN switching, and optional 5G failover into a deployable DERP Continuity kit. The objective is to preserve **critical IT and authorized back-office workflows** through a combined local power and WAN interruption. It does not promise operation of commercial cooking, refrigeration, HVAC, or other high-load equipment.

**Boundary:** Battery-backed compute/connectivity is not full-site business continuity. Physical operations require separately engineered power, safety, and service dependencies.

### Illustrative runtime model

Usable AC energy is assumed to be **8 kWh** from a nominal 10 kWh system after battery reserves and losses. This is a planning assumption, not a product guarantee.

| Average continuous load | Illustrative runtime |
|---|---:|
| 200 W | 40 h |
| 400 W | 20 h |
| 800 W | 10 h |
| 1,600 W | 5 h |

Actual runtime depends on usable depth of discharge, battery health, temperature, inverter efficiency, auxiliary losses, startup surge and equipment load. Capacity (kWh) must not be confused with power/inverter rating (kW). Size for measured continuous draw and surge demand.

### Required engineering decisions

- Separate protected **IT circuits** from heavy equipment; define which loads are actually supported.
- Use appropriate **listed, compatible battery/inverter/transfer equipment**; verify installation requirements and local authority approval (applicable electrical/fire codes and standards such as NFPA 855 and UL 9540 where relevant).
- Provide clean power transfer for devices requiring uninterrupted sessions and documented low-battery shutdown.
- Include power-state telemetry: battery state of charge, rate of discharge, estimated remaining runtime, inverter faults, critical load measurements, and successful shutdown/recovery evidence.
- Specify independence of **cellular uplink** and local router/switch power; mobile coverage and carrier operation are not guaranteed during regional outages.
- Define the permitted offline dataset and pending-operation journal, especially for interrupted WAN and POS/payment operations.
- Rehearse outage, intermittent power, exhausted battery, failed inverter, loss of cellular service, return of utility power, and safe reconciliation after reconnection.

### Commercial packaging hypothesis

Offer **DERP Continuity PowerPack** as an optional tier for customers requiring local critical-workflow continuity. Separate battery ownership, installation, monitoring, maintenance, warranty, periodic test charges and eventual replacement in the cost model. Product suitability and economics remain unverified.

### Next evidence-producing test

Meter the actual ZBook + edge datastore + router + switch workload. Power the isolated synthetic environment through a commercially suitable battery system. Disconnect mains and WAN, log offline operations, restore the network, verify idempotent reconciliation, and record the observed load, runtime, data-integrity results and failure modes. No real retail payment processing in this test.

---

## Addendum C — Incremental backups and weekly OH SHIT tests

**Captured:** 2026-11-24  
**Status:** Design proposal, not deployed or benchmarked.  
**Revised scope:** **Data continuity**, not powering an entire retail business or physical site. The battery-backed node protects scoped data/IT services.

### Principle

A successful backup job is not evidence of a successful recovery. Pair incremental backup and transaction-log preservation with **weekly automated, isolated disaster-recovery rehearsals**. Run the deliberately destructive steps only against disposable test instances.

### Candidate workflow

1. Inventory protected datasets, application dependencies, schemas, backup policies and the latest known recovery points.
2. Create or verify a consistent base backup, subsequent incrementals and continuous database WAL/log archives as appropriate. Monitor recoverability of the complete chain, not just each file.
3. Restore a **selected recovery point** into an isolated scratch environment, with no route back to production writes.
4. Launch the restored database/application and execute health checks, structural checks and small known-answer queries against synthetic or appropriately handled test data.
5. Validate object counts, manifest/hashes when applicable, selected business invariants, idempotency and replay semantics; distinguish exact-point-in-time recovery from later transaction reconciliation.
6. Measure recovery time, actual restored data timestamp, gaps, dependencies, errors and manual interventions.
7. Record test start/end, backup-chain identifiers, dataset and code Git revisions, snapshot/WAL checkpoint, observed RTO/RPO, test result and evidence pointers.
8. Destroy/reset sandbox, cleanly report the outcome and alert on failure. Preserve immutable report history and keep original production backups untouched.

### Cadence and tiers

- **Incremental backups:** Frequency based on measured RPO; frequency alone does not prove consistency.
- **Continuous WAL/transaction archival:** For eligible databases where point-in-time recovery is required.
- **Weekly OH SHIT test:** Automated restoration and end-to-end verification of one or more representative workloads, rotating recovery points and failure scenarios.
- **Periodic full recovery exercise:** Rehearse complete application dependencies, identity, network access, cold startup and human handoff. One green database-restore check does not prove business-wide continuity.

### Evidence artifact sketch

```yaml
# SYNTHETIC EXAMPLE — not an executed test
test_id: DRP-EXAMPLE-0001
result: not_run
target: isolated-restoration-sandbox
dataset: sample-postgres
backup_chain: placeholder
recovery_point_requested: null
recovery_point_actual: null
observed_rto_seconds: null
observed_rpo_seconds: null
integrity_checks:
  restore_completed: null
  database_started: null
  consistency_passed: null
  application_query_passed: null
provenance:
  manifest_revision: null
  source_backup_manifest: null
```

### Failure modes the tests should catch

Broken incremental chains; missing WAL segments; corrupt archives; absent encryption keys; unrecoverable permissions; incompatible software versions; oversized restore times; unavailable storage; undeclared dependencies; silent partial synchronization; data-level corruption despite a healthy container; and disaster-time saturation when multiple customers need recovery simultaneously.

### Design caveats

- A **10 kWh** battery is a finite, separately tested bridge for protected IT power; it does not replace backups or guarantee a recoverable state.
- Ensure the recovery sandbox cannot sync stale or test writes back into the authoritative store.
- Validate restores with least-privilege credentials and retain secrets outside public Git.
- A green automated restore is necessary evidence, not a guarantee of availability in every incident.
- The service should sell **measured, repeatable recoverability**, not an unqualified promise of zero downtime.

**Working name:** DERP Continuity — *Weekly OH SHIT Recovery Assurance.*
