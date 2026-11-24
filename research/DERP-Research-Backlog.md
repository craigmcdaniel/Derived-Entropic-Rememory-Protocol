---
title: DERP Research Backlog
created: 2026-11-22
updated: 2026-11-22
type: research-log
status: active
tags:
  - derp
  - research
  - backlog
  - rememory
---

# DERP Research Backlog

An append-oriented log for ideas, experiments, and unresolved integration questions. Keep original concepts distinguishable from implementation status; preserve revisions in Git.

## 2026-11-22 — Gemini Chat as a staging bridge

**Status:** Proposed / research backlog  
**Origin:** Conversation with user, November 22, 2026  
**Priority:** Back burner; no automation requested yet

### Intent

Use **Gemini Chat itself** as an additional conversational entry point to the same DERP knowledge vault. Google Drive is an intermediate staging mailbox, **not** the desired permanent database or synchronization mechanism.

### Proposed flow

```text
Gemini Chat
   ↓ writes
Google Drive: Derived-Entropic-Rememory-Protocol (DERP Staging)
   └── DERP-Context-Staging (Google Doc)
   ↓ ChatGPT reads and reconciles on request
Private GitHub: craigmcdaniel/Derived-Entropic-Rememory-Protocol
   ↕ Obsidian Git pull / commit-and-sync
Local Obsidian vault: H:\Vaults\DERP-Vault
```

ChatGPT can also commit Markdown directly to GitHub without passing through Gemini. **GitHub is the intended canonical versioned record**; the staging Google Doc is transient intake.

### Verified on 2026-11-22

- ChatGPT connector located and read the Gemini staging Google Doc.
- ChatGPT committed the dated staging snapshot to the private GitHub repository.
- ChatGPT committed a synchronization test note to GitHub; user confirmed it appeared in Obsidian.
- User committed and synchronized local Obsidian files; ChatGPT verified the remote Git commit (10 files).
- Therefore **ChatGPT ↔ GitHub ↔ Obsidian** was tested in both directions.

### Unverified / research questions

- Does Gemini reliably append or revise the intended Google Doc across sessions without replacing earlier context?
- Can Gemini-to-GitHub import be made low-friction while preserving the original wording, attribution, chronology, and correction history?
- What is the simplest way to detect new staging entries and avoid duplicate imports?
- What conflict-handling rules are needed if ChatGPT, Gemini, and Obsidian edit related material independently?
- Should a later automation reconcile staging periodically, or remain user-triggered?

### Operating rule for now

On request (e.g., **“Sync Gemini staging to DERP”**), read the staging document, compare against existing committed material, and commit only new or corrected Markdown content. Treat every observation as **confirmed, historical, proposed, or unknown** with its relevant time/source. Do not claim unattended automatic cross-assistant synchronization.

### Related notes

- [[DERP-Context-Staging-2026-11-22]]
- [[ChatGPT-Obsidian-Sync-Test-2026-11-22]]

## 2026-11-22 — One-person enterprise: personas, provenance, and revision history

**Status:** Idea to hone / research backlog  
**Origin:** Conversation with user, November 22, 2026  
**Priority:** Exploratory; no new infrastructure authorized

### Core premise

Ask how a **one-person development team can approximate useful enterprise capabilities** by combining specialized AI personas, a shared repository, reproducible evidence, and versioned institutional memory—without importing enterprise bureaucracy.

The user's core question: **"how does a 1 man dev team match an enterprise, revision history and persona's."**

### Proposed functional roles (not separate employees)

- **Human architect / owner:** chooses priorities, makes decisions, accepts or rejects changes.
- **ChatGPT:** research, conversation capture, reconciliation, documentation.
- **Gemini Chat:** second conversational input and alternative analysis, with Google Drive used as staging when appropriate.
- **Codex:** potential implementation, tests, and repository operations.
- **GitHub:** canonical history of committed files, not proof of truth by itself.
- **Obsidian / DERP:** local linked notes, evolving knowledge, historical context and retrieval.

These are *possible workflow roles*, not guarantees that personas have independent judgment or that any currently untested integration is operating.

### Hypothesis to test

Persistent, shared records may let a solo developer recover past decisions and delegate bounded tasks across AI interfaces without depending on any single model session's memory. Compare this against the costs of review, context drift, conflict resolution, and coordinated mistakes.

### Research questions

- What minimum persona definitions actually improve quality versus simply duplicating the same assumptions?
- How should each contribution record **author/source, event time, collection time, evidence, inference, and corrections**?
- How do we separate an independent test from two models repeating the same claim?
- What review or acceptance gate should precede a change to production systems?
- Can Git commit history and linked Obsidian notes reconstruct **why** a decision changed, not merely **what** changed?
- What is the smallest useful workflow for a one-person team without meetings, approval theater, or unnecessary services?

### Current boundary

**Verified:** ChatGPT–GitHub–Obsidian bidirectional file exchange and versioned Markdown commits.  
**Proposed:** Durable multi-persona coordination and routine automated handoffs.  
**Not established:** Enterprise-level reliability, independent AI verification, or unattended conversation archival.

### Related

- [[DERP-Context-Staging-2026-11-22]]
- [[ChatGPT-Obsidian-Sync-Test-2026-11-22]]

## Log maintenance

Add later experiments as dated entries. Prefer preserving prior observations and appending corrections rather than rewriting history.


## 2026-11-24 — 04:30 EST — FREYR and embedded DERP brainstorming

Status: research/proposed; correlation with other research deferred. User ended session to rest.

- FREYR: financial DERP, first practical reference implementation. Branch `feature/thoth-finance` created from `main` in `craigmcdaniel/thoth-git`. No deployment implied.
- Watch directories for bank statements and paycheck stubs; extract embedded PDF text first, OCR when necessary. Preserve originals, hashes, dates, extraction confidence, corrections and duplicate detection. PostgreSQL holds authoritative financial records; Grafana provides budgeting, payroll, spending, reconciliation and cash-flow analytics. Potential utility/HVAC/power correlation and QuickBooks-style accounting.
- Design for AI chatbots from inception: deterministic accounting, model-independent interfaces, read-only access initially, proposed corrections rather than silent writes.
- Architectural inversion: embed Git in projects rather than merely embedding projects in Git. Applications can checkpoint, compare, branch, reconcile and publish approved configuration/documentation changes. Keep sensitive financial records and secrets outside Git.
- SQLite is an index for documents, not a document archive. Index paths, sections, keywords, relationships, source revisions, hashes and timestamps. Original documents remain authoritative; index is rebuildable. Explore federated project indexes and compact repository snapshots.
- Embed a portable Python SQL/query environment in each project, initially using standard-library sqlite3. Provide discovery instructions (AGENTS.md), schema, query CLI, structured JSON output and targeted source retrieval. Avoid requiring AI to reconstruct all context from Markdown.
- Small HTTP-driven interface: initially view-only rather than full CRUD; manifest, health, schema, search, document retrieval, relationships and history. CLI, HTTP and optional MCP adapters share a query engine. Scoped, revocable API keys with hashed storage outside Git, project permissions and audit trail; possible later gateway on THOTH. No unrestricted SQL or writes exposed by default.
- Emerging idea: independently useful applications act as plugins to a larger household AI system; each carries its own knowledge index, version history and interfaces. Extract reusable DERP Core only after practical validation.

First milestone: drop a bank statement into a directory and see validated transactions in Grafana. Preserve this brainstorming entry without attempting broader research reconciliation now.


## 2026-11-24 — Shared semantic memory / Microsoft Copilot

**Status:** Proposed; direct Microsoft personal Copilot integration unverified.  
**Origin:** Follow-up conversation, November 24, 2026.

The user clarified that Copilot should access the **same semantic memory over the Git-backed Obsidian Markdown environment** as ChatGPT or future local models, rather than simply reviewing an exported note. The vault is model-independent persistent knowledge; a rebuildable index and retrieval API supplies source-linked context to multiple agents. Keep Git as the versioned evidence record. Personal Microsoft Copilot, Microsoft 365 Copilot, GitHub Copilot, and an Obsidian plugin named Copilot are different integration targets. Prefer personal over institutional identity for tests, but verify real connector support first. Cross-agent context portability is the proposed success metric.

**Full research note:** [[Multi-Agent-Semantic-Memory-Copilot-2026-11-24]] — architecture, identity boundaries, capabilities, uncertainties, experiment plan. Deliberate overlap with the 04:30 FREYR/SQLite/HTTP brainstorming is retained.

## 2026-11-24 — Inventory interview: immediate work sequence

**Source:** User-directed one-question-at-a-time backlog inventory. **Status:** Priorities selected; task completion not implied. This records the work order rather than asserting specific TryHackMe module names or lab results.

**User direction (verbatim):** “I'd like to fuck around for a bit with check stubs and shit. Then we'll finish up this try hack me, putting it all together in planning and scoping, then there is a review task to recheck and verify the infection or whatnot is ok. then its on to our favorite, coding for penetration. the pthon an dpowershell stuff.”

### Prioritized sequence

1. **FREYR / CraigBooks: paycheck-stub exploration (active next).** Test extraction from an actual paycheck stub, understand gross pay, deductions and net pay, and identify reusable data fields. Treat this as exploration before building full automation. Financial source documents and extracted personal records remain in private storage; this public backlog records only project direction.
2. **TryHackMe: Planning and Scoping (next).** Complete current room/course exercises. Exact module/task identifier needs to be verified from the user's room before tracking completion.
3. **TryHackMe: review and verification task (then).** Recheck the infection-related result or state described by the task; scope and wording not yet independently inspected. Do not prematurely classify as verified or assume a live infection.
4. **TryHackMe: Coding for Penetration Testing (afterwards).** Continue Python and PowerShell training exercises within the course environment.
5. **DERP Core / VERN: architecture (deferred relative to current sequence).** Preserve the appliance concept, workers and indexes in the research backlog, without initiating additional infrastructure merely to support the first paycheck-stub experiment.

### Inventory state

- **Decision:** User has explicitly ordered these activities.
- **Confirmed completed:** None established by this interview turn.
- **Open:** Exact TryHackMe task names, original financial ingestion tests, and practical constraints for the paycheck-stub experiment.
- **Next interview question:** Determine the first paycheck-stub source format and whether a private local example already exists.

### Editorial boundary

No assumption that the first FREYR experiment must deploy PostgreSQL, Grafana, or a Python service. Extract and reconcile a sample first, then decide what code or storage is justified by the evidence.

## 2026-11-24 — DERPBooks architecture correction: Git-centric application from inception

**User correction (verbatim):** “the derpbooks was going to be the first project we made git centric from the get go with a dedicated data layer with sql ops”

**Status:** Architectural intent explicitly clarified; implementation unverified.

### Corrected scope

**DERPBooks** (earlier working names FREYR / CraigBooks in this backlog) is intended to be the **first application designed Git-centrically from the beginning**, with a **dedicated, queryable data layer exposing SQL operations**. It is **not merely a paycheck-stub extraction script** or a one-off dashboard experiment.

- **Git-centric lifecycle:** Project structure, code, schemas/migrations, query definitions, documentation, and approved configuration changes are versioned together, with source history and provenance integral to the application's workflow. “Embed Git in projects” is a design requirement for this pilot, not a speculative future add-on.
- **Dedicated data layer and SQL operations:** A persistent structured store and intentionally defined SQL query/write operations are part of the application's initial architecture. The exact DB engine and approved operation surface have not been decided here; earlier research mentions PostgreSQL for financial records and SQLite for document indexing, which serve distinct possible roles and should not be silently conflated.
- **Evidence model:** Preserve original financial documents privately, associate them with hashes, timestamps, extracted fields, revisions, reconciliation outcomes and Git-linked development provenance. Keep personal records and secret material out of the public DERP repository.
- **First use case:** Explore paycheck stubs to exercise ingestion, structured records, queries and reconciliation, not to define or limit the application's architecture.
- **AI interoperability:** The previously proposed portable Python SQL/query environment and optional view-only API are possible interfaces to the dedicated data layer; neither is confirmed built.

### Correction to earlier inventory wording

The preceding inventory entry over-simplified DERPBooks as “extract a check stub before deciding whether to build a database.” **Superseded:** A dedicated SQL-capable data layer and Git-centric design are foundational requirements. We can still choose a minimal first vertical slice without pre-building the entire financial application.

**Next inventory question:** Clarify the relationship between the financial records store (possibly PostgreSQL) and the repository-local index (possibly SQLite): one database or two distinct purposes? Preserve the decision before defining a schema or repository scaffold.
