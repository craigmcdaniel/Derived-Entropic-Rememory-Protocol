# DERP Research Note — Visual Evidence Serialization and Autosave

- **Recorded:** 2026-11-22 (America/Detroit)
- **Source:** Live chat/voice design discussion and DERP Experiment 002/003
- **Classification:** Research proposal
- **Deployment status:** Not deployed by this note

## Hypothesis

Preserve original images in economical local storage while committing compact, OCR-assisted, visually interpreted and serialized evidence records to the Git-backed Obsidian vault. This separates evidence from representation and permits progressive contextual retrieval.

## Proposed workflow

1. Capture original screenshot/photo, source and temporal provenance.
2. Compute SHA-256 for integrity/deduplication; archive original locally.
3. Extract visible text, keeping raw OCR distinct from the original image and any later interpretation.
4. Interpret topology, objects, and relationships; distinguish direct observations from inference.
5. Serialize to YAML/Markdown with evidence ID, event/capture time, ingestion time, source, system, extracted text, interpretations, confidence, corrections, original location and hash.
6. Commit/push small text records to GitHub; optionally include a few compressed previews.
7. Retrieve via high-level project outline, relevant evidence records, and original media only when necessary.

## Provenance and failure handling

- Preserve original observations and append later corrections; never silently rewrite history.
- OCR, visual interpretation, and operational verification are different layers.
- A screenshot of Node-RED showed an MQTT Frigate Reviews input and separate Blue Iris and Elasticsearch branches; this proves visible topology, not downstream delivery.
- Cross-session 'before/after' chicken-photo matching produced a false-positive association that the user corrected. **Image identity reconciliation failed** even though image retrieval succeeded. Do not identify a match by upload proximity, file name, or appearance alone.
- Serialized text is not a lossless substitute for imagery. Keep the original's stable locator and cryptographic hash.
- Do not automatically push private photos or surveillance footage into a public repository.

## Storage tiers

| Tier | Where | Content |
| --- | --- | --- |
| Index | GitHub/Obsidian | Markdown, YAML, OCR text, hashes, references, provenance |
| Preview | Selectively in GitHub | Small compressed thumbnails, if appropriate |
| Original | Home-lab storage | Full-resolution image/video binary archive |

## Ten-minute autosave proposal

User requested automatic save and push about every ten minutes for the working Obsidian vault. Preferred longer-term design is THOTH Node-RED orchestration, with potential migration of selected cron/systemd timer/service workflows **after inventory and review**.

Proposed control flow:

`10-minute inject → single-writer lock → detect scoped changes → stage allowed files → commit if dirty → push → record success/failure and release lock`

Requirements:

- Operate on the real local Obsidian vault, not an isolated copy.
- Confirm host/path, branch, Git identity and repository access before enabling.
- Explicitly exclude binary originals, large attachments, credentials and transient state.
- No empty commits, overlapping runs, force pushes, or silent conflict resolution.
- Failed pushes preserve local commits, emit error telemetry, and retry.
- Keep simple service startup, host boot dependencies and critical recovery paths outside Node-RED where appropriate, to avoid circular dependencies.
- Measure last successful local commit, last successful remote push, conflict count and backup lag.

**Current status:** Design documented, no claim that a local Node-RED flow or 10-minute on-host task has been installed.

## Next research direction

Inventory THOTH cron jobs, systemd timers and persistent services. Classify each as orchestration, one-shot scheduled work, service lifecycle, or critical boot dependency. Migrate only suitable workflows to Node-RED, with rollback and failure handling.
