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
