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
