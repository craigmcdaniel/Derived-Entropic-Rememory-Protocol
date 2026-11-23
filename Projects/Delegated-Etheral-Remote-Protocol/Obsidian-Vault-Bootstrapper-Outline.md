# DERP Obsidian Vault Bootstrapper — Initial Outline

**Status:** Proposed / outline only; nothing installed or deployed  
**Recorded:** 2026-11-22 (America/Detroit)  
**Parent project:** [Delegated Etheral Remote Protocol](./README.md)  
**Vision:** A reusable piece of the one-person Banquet Table Enterprise, built from the existing Git-backed Obsidian workflow.

## Goal

Give another person a small, auditable bootstrap script that sets up a local Obsidian vault, guides them through optional GitHub initialization, confirms their first commit, and explains how to use a chat assistant to read and contribute to a shared, versioned workspace. Preserve the evolution of ideas—not just finished notes—without selling a magical, always-on AI memory system.

The initial deliverable is a **repeatable setup and clear instructions**, not a hosted service or a monetization promise. Any future paid assistance or productization should follow real user tests.

## User experience (proposed)

1. Launch one signed or inspectable bootstrap script, with clear prompts and no hidden system changes.
2. Preflight the host: operating system, Obsidian, Git, and optional GitHub CLI; report which components are installed. Offer links or supported installation commands only after approval. Support offline/manual fallback where practical.
3. Short setup questionnaire: vault name, location, private/local vs Git-backed, GitHub repository (existing or new), and whether to enable Obsidian Git. Defaults should suit a nontechnical individual without overwriting existing material.
4. Create a minimal vault directory and starter notes: `README.md`, `Inbox/`, `Projects/`, `Research/`, `Decisions/`, `Templates/`, and `Context/` as needed. Empty folders may need a tracked placeholder. Include a sample capture showing **verbatim source** separated from **edited interpretation**, status, timestamps, and source.
5. Initialize Git locally if requested; offer to authenticate GitHub using GitHub CLI or the user's existing configured method. Never ask the script to collect or store a password/token. Confirm target URL, visibility (private by default), and any remote writes.
6. Create a first local commit and, with affirmative approval, push to the intended GitHub repository. Verify remote branch and commit; report exactly what succeeded and failed.
7. Guide the user to open the vault in Obsidian and, optionally, install/enable Obsidian Git through supported marketplace/CLI flow, respecting the application's version and available plugin support.
8. Display a succinct assistant handoff: “Read the relevant shared folder/repository, preserve original notes, draft proposed updates, and push to Git only with my permission and a verified connector.” Explain that a chatbot **cannot** automatically see local folders unless explicitly shared, uploaded, synchronized, or connected.
9. Print a plain-English success report, paths, repository URL, current commit SHA, next steps, and rollback notes.

## First-release boundaries

- **Windows/PowerShell first**, matching the currently working environment; architecture should permit a future cross-platform shell/Python port.
- No mandatory Node-RED, databases, remote workers, background agents, SIEM, or cloud resources.
- No copying personal notes, credentials, home-lab addresses or private repository content into a distributable template.
- No force pushes, resets, destructive cleanup or hidden publication. Existing vaults are left untouched unless the user explicitly selects a migration workflow.
- GitHub integration remains **optional**. No GitHub account or internet connection is required to start taking local notes.
- Differentiate **script installed**, **vault created**, **Git initialized**, **initial commit created**, **pushed and verified**, and **AI connector configured**. These are distinct outcomes.
- Do not silently install or enable community plugins; support a reviewed fallback if programmatic CLI installation is unavailable for the installed Obsidian release.
- Avoid assuming the AI assistant can write to GitHub. Document provider-specific permission and connection steps only after they are verified.

## Minimal four-field task contract

- **Goal:** Establish a working Obsidian/Git documentation workflow.
- **Source snapshot / commit:** Script version, source repo/tag and eventual resulting vault commit.
- **Boundaries & status:** Installation and external writes require user approval; integration is proposed until tested.
- **Acceptance criteria:** A new user can create a vault, write an Inbox note, commit it, optionally push, reopen it in Obsidian, and point a connected AI at the correct shared source.

## Milestones and experiments

**M0 — Specification & safety:** inspect existing vault/repo conventions and identify a starter structure. Write a dry-run contract and expected prompts.

**M1 — Local bootstrap:** PowerShell script creates a new vault and Git repository without external dependencies beyond Git; test with fresh directories, paths containing spaces, existing destinations, missing Git, and cancellation.

**M2 — Optional GitHub publishing:** account/repository selection and visibility confirmation; test remote verification and non-destructive failure recovery.

**M3 — Obsidian onboarding:** validate plugin installation/enablement paths on an actual supported Obsidian version; produce human-readable launch instructions.

**M4 — Chat assistant handoff:** controlled two-way test with a real connector: capture → proposed change → human approval → verified Git write → Obsidian pull. Keep original evidence.

**M5 — Distribution and market test:** package with documentation/license, versioned releases, minimal support expectations and clearly stated limitations; separately test if users find it valuable enough to pay for assistance or tooling.

## Design questions (deferred)

- Whether the first version should support existing vault adoption in addition to new vault creation.
- Whether GitHub repository creation belongs in the guided CLI or a browser-based step.
- Whether a lightweight semantic index or association quiz is a later optional module, built from a local/consented data set rather than exported personal history.
- Whether the installer can offer both “solo notes” and “AI-assisted research” profiles without bloating the questionnaire.
- The user's intended visual mockup, not yet provided; do not invent a final interface.

## Relation to existing DERP work

This is a **proposed productization path** for an existing workflow, not a new deployment. It builds on [Workspace Discipline](./Workspace-Discipline-and-Engineering-Lifecycle.md), [Remote Capture](./Remote-Capture-and-Repository-Routing.md) and the [Banquet Table RFC](./RFC-0001-One-Person-Multi-AI-Engineering-Enterprise.md).

**Next action after rest:** Review this outline; then implement the smallest possible dry-run-first local bootstrapper. No automation or installer has been executed by this documentation commit.
