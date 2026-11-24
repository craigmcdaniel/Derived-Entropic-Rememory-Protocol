---
title: "Experiment 1 Results — Documenting Note-Taking Evolution in Obsidian"
date: 2026-11-24
status: draft-for-owner-edit
type: experiment-results
author: Claude Sonnet 5.5 (AI-authored draft; the owner has not adopted any conclusion below)
freeze_commit: fbdf791
tags: [derp, experiment-1, results, obsidian, provenance, handoff-integrity]
---

# Experiment 1 Results

**Status: DRAFT for the owner to edit.** AI-authored. Findings are labeled by evidence basis. Nothing here is a user decision.

**Freeze point:** commit `fbdf791` (2026-11-24, 40 Markdown files). A tag named `experiment-1` is intended but was not on the remote when this note was written. Changes after the freeze should be additive corrections, not rewrites.

## What the experiment was

**Owner's framing (verbatim):** "this first experiment was the experiment of documenting our evolution of note taking this way with obsidian as obsidian and in obsidian"

The repository is both the method and the data: a Git-backed Obsidian vault that recorded its own evolution, with several AI assistants contributing and reviewing. That makes the volume of notes a result, not clutter.

## What it produced

About 40 Markdown files (about 418 KB) covering handoff architecture, provenance conventions, a cross-model review, and several side projects. The research backlog alone is about 111 KB, roughly 27% of the total. By title and size, an estimated 235 KB belongs to projects outside the Obsidian stack.

## Reviewer retrieval test — observed outcome

- **PASS (reported result):** ChatGPT retrieved the exact Experiment 1 flag, correctly identified fictional statement B, and supported A and C; the review was scored as a pass for discovery, attribution, and avoiding hallucination, based on the assistant's disclosed response rather than an independently verified tool trace.
- **LIMITATION (test design):** ChatGPT reported starting at `README.md` but locating the results and evidence through commit history and patches, not a README-to-results link chain (no such README link existed); the descriptive commit message and public patch exposed the target, so this demonstrated commit discovery rather than the intended link traversal. A neutral-message, linked, history-controlled retest remains proposed, not completed.

## Three experiments, kept separate

Framing from the owner–ChatGPT discussion on 2026-11-24 (pasted into the Claude session); table adapted by Claude.

| Experiment | Objective | Status |
|---|---|---|
| 1 — Persistence and portability | Can Obsidian and Git preserve usable context between AI systems? | Demonstrated, provisionally (one run, one owner, two models) |
| 2 — Repository discipline | Can multiple assistants maintain that context without creating disorder? | Not yet tested |
| 3 — Indexed retrieval | Does SQLite improve reconstruction over well-organized Markdown? | Proposed |

**Credit boundary:** Experiment 1 exercised plain Markdown in Git, read and written through a GitHub connector. Obsidian is the owner's editing and linking workspace; no model used it, so the experiment gives it no credit beyond the owner's own reports. Git preserved the sequence of changes, corrections, and reviews.

## Findings

**Worked**
- **Provenance discipline.** Status labels, verbatim decision quotes, and the rule that an assistant expansion is never promoted to a user decision. ChatGPT's review marked the related claims supported, with the caveat that this does not imply perfect compliance everywhere. *(Basis: ChatGPT review, claims 1, 2, 6.)*
- **A cold-read handoff.** A model with no prior context reconstructed a usable, self-qualified picture from the repo alone. ChatGPT judged this provisionally successful for orientation and provenance, and explicitly not yet shown for technical correctness. *(Basis: ChatGPT review.)*
- **Coverage disclosure.** Listing what was read, partly read, and unread let the reviewer separate missing context from wrong interpretation. *(Basis: ChatGPT review.)*
- **Handoff evidence trail.** The commit-by-commit record of the review exchange is in [Handoff evidence trail](./experiment-1/evidence/handoff-trail.md).

**Did not work**
- **Staleness.** The written record lagged reality; one status claim was stale within hours. *(Basis: ChatGPT review, claim 5.)*
- **Inconsistent status format.** 14 of 40 files carry a frontmatter status; the rest use free text or none, so an index cannot extract it reliably. *(Basis: Claude's count at the freeze.)*
- **One repo, two jobs.** The public showcase doubles as the working log, and the backlog contains 27 private-address matches plus access-rule details. Both models counted 27. *(Basis: Claude and ChatGPT counts; the repo's own policy says prior public exposure occurred.)*
- **Sprawl.** One 1,159-line backlog and overlapping notes make current state expensive to find. *(Basis: Claude's inventory.)*
- **No review gate.** Multiple assistants push to `main` with the owner reviewing afterward. *(Basis: commit history for this session.)*

**Unknown**
- Whether an index beats a model simply reading files plus a good `INDEX.md`.
- Whether a fresh model can perform a technically correct task from the repo alone.
- Whether Gemini staging works reliably across sessions.

## Observation (Claude's, not evidence)

The notes about the notes became part of the subject. Each review added documents that the next review then had to account for. That is worth recording as a result of the method itself.

## Carry-forward candidates for Experiment 2 (OPEN, not decisions)

- A lean vault with a Current State block and an "as of" date at the top of long logs.
- A machine-readable status convention.
- Per-assistant branches, with the owner merging.
- A public/private split and a pre-commit check for addresses and credentials.
- The index test from the [Index Broker Design Proposal](./Index-Broker-Design-Proposal-2026-11-24.md), including a file-only baseline.

## Experiment 2 — proposed pass/fail criteria (OPEN, set before running)

**Status:** PROPOSED by Claude, not adopted. The owner sets the thresholds; the numbers are starting suggestions. Fix them before the run begins and record any later change as a dated amendment.

**Question:** Can several assistants maintain this context without creating disorder?

**Starting conditions (no large restructuring):** a consistent note format (frontmatter with title, date, status, type), a simple navigation index, and assistants proposing changes on branches that the owner merges. The owner keeps using Obsidian as usual; no plugin or workflow change is required.

**Measures,** taken at a frozen commit at the end of the run. They apply to notes created or changed after the start; legacy notes are excluded unless stated.

| # | Measure | Baseline at Experiment 1 freeze | Proposed pass |
|---|---|---|---|
| 1 | Assistant commits made directly to `main` | All of them (at least 4 this session) | 0 |
| 2 | New or changed notes with a valid status field | 14 of 40 existing files | 100% of new notes |
| 3 | Broken internal links | Not measured | Measured at start; no increase |
| 4 | Fresh-model current-state questions answered correctly, with source and "as of" date | Not measured | At least 4 of 5, against a key written first and withheld |
| 5 | Active logs whose Current State predates their latest entry | Not measured (the backlog has no Current State block) | 0 |
| 6 | Internal addresses or credentials in new public commits | 27 address matches in the backlog | 0 |
| 7 | Assistant commits identifiable as such (author or trailer) | Claude's 3 are; commits recorded as ChatGPT's carry the owner's author name | 100% |

**Controls:** write the answer key before the run and withhold it from the model under test; record model, date, tools, and files opened for each trial; use a grader other than the model that designed the test where possible (in Experiment 1 one model did both).

**Out of scope:** indexing and SQLite (Experiment 3), and any rewrite of existing history.

## Boundaries

- Reviews by other models are feedback, not independent verification.
- The owner uses Obsidian but did not use the app on 2026-11-24 (owner-reported). The exchange between models ran through the repository, not through Obsidian.
- Git author names do not separate ChatGPT from the owner. Attribution of those commits comes from note content, not from the author field.
- Operational results recorded in the repo (the DERPBooks pipeline) are user-reported and were not reproduced by either reviewer.
- Counts and size estimates are Claude's and approximate.

## Related

- [Claude cold-read review](./artifacts/2026-11-24-Handoff-Integrity-Claude-Review.md)
- [ChatGPT review](./artifacts/2026-11-24-ChatGPT-Response-to-Claude-Handoff.md)
- [Publication Policy](../PUBLICATION-POLICY.md)
