---
title: Multi-Agent Semantic Memory — Copilot and DERP
created: 2026-11-24
updated: 2026-11-24
type: research
status: proposed
tags:
  - derp
  - obsidian
  - semantic-memory
  - copilot
  - multi-agent
  - sqlite
  - provenance
---

# Multi-Agent Semantic Memory — Microsoft Copilot and DERP

**Date:** 2026-11-24  
**Source:** User–ChatGPT discussion, morning of November 24, following the 04:30 EST embedded-DERP brainstorming session.  
**Classification:** Research/proposal; no Copilot connector, semantic index, or cross-agent access has been deployed by this entry.

## Core insight

The user proposed using **Copilot as another consumer of semantic memory in the same Obsidian Markdown environment**, not merely as a second chatbot, document reviewer, or one-off importer. The local Obsidian vault and Git-backed Markdown are shared persistent knowledge; AI models are replaceable interfaces over a retrieval layer.

**Working hypothesis:** One durable evidence base can supply context to ChatGPT, Microsoft Copilot where supported, local AI, and other compatible agents without relying on their private conversation memory. Every retrieved answer should cite the source document and provenance.

## Account discussion and trust boundary

The user has access to employer-provided Copilot, student Microsoft 365, and a personal Microsoft account sharing the email address used for ChatGPT. The **personal Microsoft account** is preferred for testing because it avoids tying personal DERP records to an employer or educational tenant. Matching email addresses do **not** provide automatic ChatGPT ↔ Copilot data access.

Microsoft 365 Copilot, personal Microsoft Copilot, GitHub Copilot, and third-party "Copilot for Obsidian" are distinct products. Do not treat plugin capabilities as proof that the personal Microsoft Copilot product supports direct access to an Obsidian vault, local MCP server, or custom semantic index.

**Unknown:** Whether the personal Copilot interface currently available to the user can query an external DERP search endpoint or connector. Verify account/product capabilities before committing to any adapter.

## Proposed structure

```text
ChatGPT       Microsoft Copilot*       Local LLMs       Other agents
      \              |                  |                /
       \------------- DERP retrieval / context API --------/
                     |  metadata + semantic search
                     |  source links + provenance
                SQLite index (rebuildable)
                     |
             Obsidian Markdown vault
                     |
                 Git history
                     |
          GitHub remote (versioned archive)

* Only if a compatible, authorized integration is verified.
```

Git/GitHub remains the **versioned source of truth for documents**, not the semantic search engine. SQLite holds **references and indexes for documents**, not the only copy of the documents. The vault remains usable without any specific AI vendor.

## Feature opportunities

1. Shared semantic and keyword retrieval across project notes, meeting/research logs, archival transcripts, and other indexed Markdown.
2. Context recovery: reconstruct a project state from source-linked excerpts, rather than from a model's remembered summary.
3. Independent comparison: multiple models answer the same historical question without reading one another's chat session.
4. Provenance: record source path, Git revision, original observation/event time, collection time, classification (confirmed / historical / proposed / unknown), confidence, and later corrections.
5. Reusable interface: a standard Python `sqlite3` query layer; scoped JSON CLI; minimal read-only HTTP endpoints; optional MCP adapter when client support is verified.
6. Controlled updates: agents may draft corrections but writing to canonical Markdown and Git requires review/approval, conflict detection, and commit evidence.
7. Future plugin architecture: projects embed Git and a small index, while a shared DERP Core emerges only after use in practical projects such as FREYR.

## Distinctions to preserve

- **Semantic index is proposed**, not an installed feature.
- **Personal Microsoft Copilot integration is unverified.** An Obsidian plugin named Copilot does not establish that integration.
- **GitHub sync is separate from retrieval.** A connected AI still needs an authorized method to discover, read and cite pertinent files.
- **Public DERP repository is a showcase, not the private vault.** No personal raw conversations, credentials, or financial documents should be copied into this public research entry.

## Experiment — cross-agent context portability

1. Choose a small sanitized set of Markdown files from an existing DERP project.
2. Build a read-only local index with document paths, hashes, Git revisions, timestamps, and section-level entries.
3. Provide a deterministic search interface yielding snippets and precise source references.
4. Test one compatible AI client with an unseen project-state question.
5. Test a second compatible client independently, without sharing the first one's answers.
6. Compare both reconstructions with the original evidence. Log omissions, contradictions, citations, and retrieval failures.
7. Only then investigate whether the user's personal Microsoft Copilot supports the needed retrieval connector or endpoint.

**Success criterion:** Two independent models accurately reconstruct the same documented project state from the same canonical files, preserving evidence and uncertainty.

## Related records

- [[DERP-Research-Backlog]] — especially 2026-11-24 04:30 EST FREYR / embedded DERP brainstorming
- [[Conversation-Archive-Strategy]]
- Git-backed Obsidian synchronization test documented on 2026-11-22

## Open questions

- What external connector, if any, is actually available to personal Microsoft Copilot?
- Local embedding model vs provider-based embeddings? How will re-indexing and deduplication work?
- File/section identifiers, source hashes, and stale-index detection after Git commits?
- Permissions, per-project boundaries, audit logs, and safe write approval?
- How should independent-agent results be compared and reconciled?

## Decision log

**2026-11-24 — Proposed:** Treat semantic memory as shared DERP infrastructure, not memory owned by any one AI. Preserve previous financial and embedded-project brainstorming unchanged. Append corroborating research even when ideas overlap.
