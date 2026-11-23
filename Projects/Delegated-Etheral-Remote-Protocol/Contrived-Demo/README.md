# Contrived — Am I a Big Fat Phoney in the Day and Age of Vibe Coding?

**A Case Study.** An earnestly documented, slow-burn troll in which the evidence-management system becomes evidence in its own investigation.

**Status:** Source prototype; not tested on the user's workstation, not deployed. This is intended as the basis for a **separate future public GitHub repository**, not a publication of the private DERP vault.

## First demo

Run `New-ContrivedVault.ps1` in Windows PowerShell. It asks for a **new** vault destination, creates Markdown notes with Obsidian properties, a `.base` index, and an introduction, and optionally initializes local Git and creates the first commit. If asked, it may connect an **existing empty GitHub repository** and push only with approval. It doesn't install Obsidian, create GitHub accounts/repositories, or run a background sync service.

Open the resulting folder with **Obsidian → Open folder as vault**; enable the built-in Bases core plugin if needed.

## The actual up/down test

After a verified first push, edit a journal entry through GitHub's web editor and commit it. Pull using `git pull --ff-only` from the local vault. Inspect the changed entry in Obsidian. Write another observation locally, `git add Journal`, `git commit`, and `git push`. Preserve and record the two SHAs. If histories diverge, stop instead of force-pushing.

An assistant must have a verified authorized connector to the source. Saying 'read the folder and push' does not give it filesystem or GitHub permissions.

## Public release rules

Develop in private DERP staging; publish a **clean standalone repository** once reviewed. Include an explicit license, sanitized sample data, README, tested installer, version tag, and documented limitations. **Never mirror private conversation archives, home-lab data, credentials, or the parent Git history into the public release.**

## Story arc

Entry 001: Is prompting really building? Entry 002: Is a confident assistant a reliable witness? Entry 003: The repository cross-examines its own creation. The final punchline is earned by recurring self-references, not explained away in the introduction.

## Known limitations

Obsidian Bases provides a local Markdown-backed table, not a standalone SQL database. This prototype has not been exercised end-to-end on an actual Windows/Obsidian install, and a remote push is not proof of a subsequent pull. Manual installation and remote-edit steps remain.

See [Bootstrapper outline](../Obsidian-Vault-Bootstrapper-Outline.md).
