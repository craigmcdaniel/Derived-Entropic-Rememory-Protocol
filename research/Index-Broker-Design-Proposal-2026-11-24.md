---
title: "Index Broker Design Proposal — Build Artifact First, Daemon Last"
date: 2026-11-24
status: proposed
type: design-proposal
author: Claude Sonnet 5.5 (AI-authored at the user's request; the user has not adopted any recommendation below)
scope: Obsidian stack (vault, Git, assistant handoff, index)
tags: [derp, index, sqlite, fts5, retrieval, handoff-integrity, obsidian]
---

# Index Broker Design Proposal

**Status: PROPOSED.** This note records a recommendation. It is not a decision, not a built component, and not tested. Nothing here has been implemented.

## Origin and attribution

- **User idea (verbatim):** "We were going to make a index worker, that uses sqlite to index records."
- **User question (verbatim):** "What would be a better way to broker the index?"
- **Assistant proposal:** Everything under *Proposal* onward is Claude's recommendation in response. Treat it as an ASSISTANT EXPANSION in the [lineage](./lineage/DERP-Continuity-Idea-Lineage.md) vocabulary until the user selects something.
- **Scope:** Per the user's direction on 2026-11-24 to scale back to the Obsidian stack, this note covers only the vault, Git, and assistant retrieval. It does not cover DERPBooks, Continuity, or other parked projects.

**Not read when this was written:** [Multi-Agent Semantic Memory / Copilot](./Multi-Agent-Semantic-Memory-Copilot-2026-11-24.md), where the original index idea was sketched. A constraint already decided there may contradict this note; that note should win until reconciled.

## Problem

Assistants need to find the right part of a large, append-only record, and to cite it in a way a reviewer can check. The research backlog is about 1,160 lines of dated sections in one file; a fresh model must read most of it to learn current state. The [cross-model handoff review](./artifacts/2026-11-24-ChatGPT-Response-to-Claude-Handoff.md) found a second problem: the written record **lags reality** (a later screenshot confirmed something the backlog still listed as pending). Any index of the repo inherits that lag, so the index must expose *how fresh it is*.

## Proposal

### 1. Make the index a build artifact, not a service

A single command (for example `derp-index build`) walks the vault and writes a SQLite database. Run it from a Git post-commit or post-merge hook, or a GitHub Action, and make it incremental by file hash. There is no always-on process, no open port, and no authentication to manage.

### 2. Broker in tiers; stop at the first that works

| Tier | What | Reaches | Cost |
|---|---|---|---|
| 1 | Generated, deterministic text committed to the repo: `INDEX.md` (sections, statuses, backlinks) and a Current State digest | Any model that can read the repo | Lowest |
| 2 | Local SQLite with FTS5 and a CLI that returns JSON | Agents on the owner's own machines | Low |
| 3 | An MCP adapter over the same query engine | Local-only tools that cannot read the repo | Medium |

Do **not** build an HTTP API exposed to external models unless a concrete need appears. It adds authentication, key management, and network exposure.

**Hypothesis (untested):** Tier 1 alone covers most of the benefit, because the assistants in this workflow can already read GitHub.

### 3. Index by section, not by file

The unit of retrieval is the heading. Per section, store:

- path and heading anchor
- date from the heading, where present
- status label (confirmed, proposed, user-reported, historical, unknown), where present
- tagged verbatim user quotes
- outgoing links, and whether each resolves
- file content hash

Add FTS5 full-text search over section text. Every build records the **Git commit SHA** and a build timestamp. Every query result returns path, anchor, and SHA so the citation can be checked.

### 4. Make freshness explicit

Prompted by the handoff review:

- Put a **Current State / Next Step** block at the top of long logs, with an "as of" date and a "last verified by" note.
- Have the index surface that block first and report the build SHA and time with every answer.
- Keep three evidence tiers separate, as ChatGPT's review does: *documented at commit*, *known from later user-provided evidence*, and *independently verified operationally*. The index only ever represents the first.

## Rules

1. The index is **derived and rebuildable**. It is never a source of truth; the Markdown and Git history are.
2. Keep the `.sqlite` file **out of Git and out of the Obsidian sync folder** (binary, lock files, sync conflicts). Keep it on local disk, not a network share.
3. Build **separate indexes** for the public repository and the private vault. Anything shown to an external model must be built only from the sanitized tree.
4. Builds are **deterministic and idempotent**. Add a verification gate in the spirit of the existing pipelines: section counts, broken-link count, and a rebuild that produces identical output.
5. Defer embeddings and vector search. Structure plus FTS5 comes first; add semantic retrieval only if measured failures justify it.
6. Generated Tier 1 files must be labeled as generated and must not contain anything the public policy would withhold (internal addresses, credentials, personal data).

## Falsifiable test

1. Freeze a commit.
2. Build the index on the public repo.
3. Ask five questions whose answers live in different sections, including one about current state.
4. Score whether the returned anchors and SHAs are correct and whether staleness is reported.
5. Run the same questions against a model reading the files with only a good `INDEX.md`.

**Decision rule:** if the file-only baseline matches the SQLite path, the SQLite worker has not yet earned its place. This follows the cross-model experiment ChatGPT proposed: freeze the commit, record which files the model actually opened, and score accuracy, citation, and effort separately.

## Open questions (owner decisions)

- Which assistants need to reach the index, and can each read the GitHub repo or only something on the local network?
- Should Tier 1 digests be committed, or generated on demand only?
- Where should the Current State block live: top of the backlog, a separate file, or both?
- Is the private-vault index in scope now, or only the public one?

## Boundaries

- Nothing here is built, tested, or approved.
- No claim is made that SQLite or FTS5 outperforms reading files; the test above is how that gets decided.
- Reviews by other models are feedback, not independent verification of this design.

## Related

- [Multi-Agent Semantic Memory / Copilot](./Multi-Agent-Semantic-Memory-Copilot-2026-11-24.md)
- [Cross-model handoff review (ChatGPT)](./artifacts/2026-11-24-ChatGPT-Response-to-Claude-Handoff.md)
- [Cross-model handoff review (Claude)](./artifacts/2026-11-24-Handoff-Integrity-Claude-Review.md)
- [Idea lineage](./lineage/DERP-Continuity-Idea-Lineage.md)
- [Research backlog](./DERP-Research-Backlog.md)
- [Publication Policy](../PUBLICATION-POLICY.md)
