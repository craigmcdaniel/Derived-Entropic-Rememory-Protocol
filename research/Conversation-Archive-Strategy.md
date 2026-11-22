---
title: DERP Conversation Archive Strategy
created: 2026-11-22
status: proposed
type: research-plan
tags:
  - derp
  - rememory
  - archive
  - provenance
---

# DERP Conversation Archive Strategy

## Goal

Recover months of conversational research, experiments, spontaneous ideas, corrections, and creative work into a private, searchable, version-controlled Obsidian vault.

The user retains authority over which material is archived and how it is classified. GitHub is the canonical versioned vault; local Obsidian synchronizes it. Google Workspace is staging for the Gemini Chat bridge, not the permanent source of truth.

## Source hierarchy

1. **Original ChatGPT export or original full transcript:** primary historical evidence. Preserve original author, message ordering, stable conversation/message identifiers when provided, and available timestamps.
2. **Original artifacts, log output, screenshots, and repository history:** corroborating source material. Link instead of rewriting when practical.
3. **ChatGPT memory, prior summaries, or reconstructed chronology:** useful leads but *not* verbatim transcripts. Label as reconstructed and identify provenance gaps.
4. **AI interpretations:** derived notes, questions, candidate relationships, and hypotheses. Never silently promote these into historical facts.

## Storage convention (proposed; confirm against real export)

- `archive/conversations/YYYY/` — imported, human-readable Markdown transcripts, preserving message sequence and source metadata.
- `research/` — chronological experiment logs and backlog.
- `concepts/` — curated, linked ideas with backlinks to source conversations.
- `projects/` — consolidated documentation grounded in dated evidence.
- `archive/manifests/` — export/import batches, coverage, checksums, and deduplication decisions.

Keep the unmodified account export in a separate local archival location; don't automatically commit unrelated account data or raw binaries to GitHub. Never overwrite imported originals when producing summaries or corrected interpretations.

## Minimum metadata for each imported conversation

- Source platform and source conversation ID (if provided)
- Original conversation title and date/time (if provided)
- Import date/time, importer, and source export batch
- Participants / speaker attribution
- Raw versus reconstructed status
- Relative links to derived notes and projects
- Corrections or later reinterpretations as separate, dated entries

Do not invent missing timestamps. Prefer stable source IDs to titles as deduplication keys.

## Initial workflow

1. Export ChatGPT account data using Settings > Data controls > Export data, or the supported Privacy Portal.
2. Keep the original downloaded ZIP locally unchanged.
3. Inspect the actual export schema and inventory conversation count, date span, attachments, and gaps before writing a converter.
4. Convert a *small* batch of conversations to Markdown; compare against originals for completeness, ordering, speaker roles, and timestamps.
5. Commit the verified batch with a manifest, then pull into Obsidian and check links/readability.
6. Expand in batches and derive project/concept notes only after original conversations are preserved.
7. For new conversations, use explicit on-demand capture to GitHub; unattended capture is not yet implemented.

## Provenance rule

Classify claims as **confirmed**, **historical**, **proposed**, or **unknown**. Distinguish original wording from paraphrase, fact from inference, event time from collection/import time, and first observations from later corrections. Git commit date is *not* the original conversation date.

## Candidate retrospective collections (not evidence that originals are already archived)

- Network Observation Stack / DERP telemetry and reconciliation
- Frigate / Blue Iris / CodeProject.AI / YOLO investigations
- THOTH, CHARON, HORUS, INFINITY, CHIMERA infrastructure
- Semantic persona, AI assistant and rememory architecture
- DERP Elementary / The Investigation / creative writing and cultural references
- Study, AWS, and ethical-hacking lab work

## Immediate next decision

Use the real ChatGPT export, not memory alone, as the source for historical backfill. Preserve an import inventory so coverage, missing conversations, and duplicate records can be audited.
