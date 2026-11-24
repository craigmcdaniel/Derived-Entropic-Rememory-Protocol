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

## Boundaries

- Reviews by other models are feedback, not independent verification.
- Operational results recorded in the repo (the DERPBooks pipeline) are user-reported and were not reproduced by either reviewer.
- Counts and size estimates are Claude's and approximate.

## Related

- [Claude cold-read review](./artifacts/2026-11-24-Handoff-Integrity-Claude-Review.md)
- [ChatGPT review](./artifacts/2026-11-24-ChatGPT-Response-to-Claude-Handoff.md)
- [Publication Policy](../PUBLICATION-POLICY.md)
