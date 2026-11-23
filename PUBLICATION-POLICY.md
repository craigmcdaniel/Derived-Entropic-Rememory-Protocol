# DERP Publication Policy

**Adopted for public editorial workflow:** 2026-11-23  
**Repository:** Public  
**Status:** Guidance for future contributions, not a retroactive guarantee of privacy.

## Purpose

Maintain a complete, honest technical history while presenting public research professionally. Preserve full engineering chronology: experiments, commands, outcomes, errors, corrections, interpretation, and uncertainty. Do **not** shrink a detailed case study into a success-only summary.

## Public versus source records

- **Original evidence:** Exact conversations, exports, and other source records are retained separately in a restricted archive **once one is established**. Do not publish new raw transcripts by default. The original source archive has **not yet been created or verified** as part of this cleanup.
- **Public editions:** Edit unnecessary profanity and personal insults into accurate descriptions of tone or frustration without removing findings or misrepresenting the sequence of events.
- **Technical outputs:** Preserve exact terminal output when relevant, but inspect for secrets, internal addresses, credentials, and personal data before release. When a sensitive detail is withheld, label the redaction and retain its rationale.
- **Provenance:** Distinguish original/unedited from editorially normalized, and observed from proposed, inferred, or user-reported.
- **Date and state:** Historical notes keep their original timestamps and claims; add dated corrections/current-state headers when assumptions have changed.

## Publication checks

Before committing or merging public-facing changes:

1. Inspect the diff and commit message for conversational insults, profanity, accidental raw transcript text, and personally identifying material.
2. Review new paths under `archive/`, `staging/`, `.obsidian/` and scripts for unexpected local state, internal topology, secrets, large binaries, and attachments.
3. Verify that commands, quoted technical evidence, scope, outcomes, and uncertainties were not silently altered.
4. Check relative links and Markdown rendering.
5. Use a specific, professional Git commit message.
6. Disclose AI-authored or AI-edited material when attribution matters; never claim independent execution of a test based only on user-pasted output.

## Git visibility limitation

**Editing or deleting a public file does not remove its prior versions from Git history.** Earlier publication copies, including the previously unedited conversations and internal IP addresses, can remain accessible in older commits, forks, caches, and clones. Changing a repository's visibility or rewriting history is a separate operation and has **not** occurred in this cleanup.

`.gitignore` applies only to untracked files; it does not remove already tracked Obsidian runtime files.

## Ownership of decisions

The user directs scope and publication decisions. AI may prepare edits and record evidence, but must identify what was actually verified and avoid silently changing or deleting primary technical evidence.

See [Editorial cleanup record](./research/Publication-Cleanup-2026-11-23.md).
