# Delegated Etheral Remote Protocol (DERP)

**Status:** Proposed new project — research and design, not implemented  
**Recorded:** 2026-11-22 (America/Detroit)  
**Parent:** Derived-Entropic-Rememory-Protocol  
**Verbatim source:** [Verbatim Source](./Verbatim-Source.md)

> **Naming note:** The project name is preserved exactly as supplied: **Delegated Etheral Remote Protocol**. “Ethereal” is the conventional spelling of that adjective, but renaming the project requires an explicit decision. This is not a conventional networking protocol at this stage; “Protocol” is part of the working project name.

## Goal

Enable conversational note-taking and brainstorming with GPT while away from home, using voice or typed input from a mobile device. Preserve original utterances verbatim and also produce clear, corrected, structured documentation suitable for Obsidian and the existing DERP Git repository.

Remote work should not require a live connection to the home lab for each note. The design should tolerate disconnected capture, later synchronization, and independently verifiable Git commits.

## Requirements (proposed)

1. **Dual record:** Preserve the raw user utterance separately from a professionally edited note. Never silently substitute paraphrase for source.
2. **Immediate capture:** Record ideas from phone voice/text with minimal friction, including provisional/incomplete thoughts.
3. **Provenance:** Source message/session, captured time, received time, interpretation, corrections, and commit SHA where available.
4. **Out-of-home access:** ChatGPT/GitHub should remain usable when the user is away from THOTH or local network.
5. **Selective retrieval:** Retrieve only relevant project branches rather than flooding context with the full archive.
6. **Conflict-safe writes:** Append or create new notes, inspect remote state before modifying, and never force-push over divergent changes.
7. **Privacy/storage:** Do not automatically publish raw personal photos, camera footage or sensitive content. Keep binary originals separate from compact documentation.
8. **Reconciliation:** Corrected conclusions must remain linked to originals, including known retrieval mistakes.
9. **Automation boundary:** The proposed ten-minute vault autosave and migration of cron/systemd timers to Node-RED are deferred, not enabled by this project note.

## Initial capture architecture (research candidate)

`Mobile voice or text → ChatGPT conversation → verbatim source record + edited research note → GitHub DERP repository → desktop Obsidian pull/index`

This minimal approach uses already established ChatGPT-to-GitHub access, avoids opening inbound home-lab services, and permits capture away from home when internet is available. A later optional workflow could ingest an offline mobile queue and merge it after connectivity returns.

**Important limitation:** A chat message is not automatically a GitHub commit. An explicit write operation or tested automation is required; never report an idea as saved unless the repository confirms it.

## Research — mobility and synchronization options

- **Baseline: ChatGPT + GitHub:** Work from a phone via GPT, committing paired notes directly to the repository through authorized repository access. Minimal moving parts; internet and working account/connectors required.
- **Obsidian Mobile + sync:** Obsidian's local Markdown vault works offline. Obsidian Sync supports syncing with version history; Git-backed mobile methods exist but vary in reliability and merge handling. Select one sync mechanism per vault to avoid conflicting writers.
- **Git-based mobile plugins:** Obsidian Git documents experimental mobile support. Other mobile-capable Git sync community plugins exist; assess maintenance, permissions, merge behavior and credentials before adoption.
- **Future Node-RED relay:** Optional event ingestion, queueing and classification on THOTH, only after we establish remote connectivity, auth boundary, retry/idempotency and a recovery path. Not required for phase one.

Sources consulted 2026-11-22:
- https://obsidian.md/help/sync-notes
- https://obsidian.md/help/sync
- https://community.obsidian.md/plugins/obsidian-git
- https://docs.github.com/en/get-started/using-github/github-mobile

## Phased test plan

1. **Capture test:** From mobile, dictate one idea and create both verbatim and edited Markdown files.
2. **Identity test:** Reopen both from a fresh conversation and verify source wording, timestamp and Git commit.
3. **Disconnection test:** Determine what can be captured locally without connectivity and how it is queued.
4. **Merge test:** Edit a related note from desktop and mobile, verify that no records disappear.
5. **Retrieval test:** Ask for a high-level outline, then expand a specific topic without bringing unrelated material into context.

## Acceptance criteria

- Verbatim text survives unchanged.
- Edited text fixes obvious transcription/spelling problems without rewriting the user's intent.
- Repository writes are demonstrably committed, with path and commit recorded.
- Offline and concurrent-write behavior is explicitly tested rather than presumed.
- Local images and unrelated raw history are not silently uploaded.

## Open design decisions

- Which phone capture surface becomes primary: ChatGPT or Obsidian Mobile?
- Whether offline capture is needed immediately or belongs in phase two.
- Whether editorial transformations are user-reviewed before committing.
- How to link future Node-RED automation without making THOTH a single point of failure.

## Current review documents

- [Workspace Discipline and Engineering Lifecycle](./Workspace-Discipline-and-Engineering-Lifecycle.md) — proposed lifecycle, workspace contract, status model and inventory-first adoption plan; no deployment or directory reorganization completed.
- [Remote Capture and Repository-Aware Routing](./Remote-Capture-and-Repository-Routing.md) — staging-first design; remote source capture is separate from canonical knowledge.
- [Framework Review and Adoption Plan](./Framework-Review-and-Adoption-Plan.md) — comparison and staged adoption research.

- [RFC-0001 — Banquet Table Enterprise](./RFC-0001-One-Person-Multi-AI-Engineering-Enterprise.md) — open proposal for a low-cost, one-person multi-AI full-stack engineering workflow.
- [RFC-0001 — Gemini Peer Review & Reconciliation (2026-11-22)](./RFC-0001-Gemini-Peer-Review-Reconciliation-2026-11-22.md) — Rev 1–3 cross-model review, naming/status corrections, deferred sync design, and next test plan; original Drive evidence linked.
