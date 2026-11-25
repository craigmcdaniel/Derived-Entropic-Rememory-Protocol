---
title: "Experiment 2 — Hub-and-Spoke Repository Governance"
date: 2026-11-24
status: proposed-for-owner-review
type: experiment-design
origin: user-directed architecture; assistant-authored implementation draft
tags: [derp, experiment-2, git, governance, cross-model, provenance]
---

# Experiment 2 — Hub-and-Spoke Repository Governance

**Status: PROPOSED.** This is a draft for owner review, not evidence that the repositories, access boundaries, or branch protections exist. Experiment 1 established useful Obsidian/Git context portability; it also exposed concurrent writes to `main`, uneven note metadata, and ambiguous promotion authority.

## Objective

Keep `craigmcdaniel/Derived-Entropic-Rememory-Protocol` the human-curated canonical record. Give each AI a separate, private research space in which its own drafts, errors, reviews, and revisions remain attributable. Agents may review sibling research but may not alter it. Only the owner promotes vetted material into the hub.

## Repository topology

| Repository | Intended visibility | Writer | Other model access | Authority |
|---|---|---|---|---|
| `Derived-Entropic-Rememory-Protocol` | Existing public showcase | Owner/approved owner workflow | Read only | Canonical, curated |
| `derp-research-claude` | Private | Claude integration only | Read only when explicitly granted | Model research, noncanonical |
| `derp-research-chatgpt` | Private | ChatGPT integration only | Read only when explicitly granted | Model research, noncanonical |
| `derp-research-gemini` | Private | Gemini integration only | Read only when explicitly granted | Model research, noncanonical |

**Privacy boundary:** Do not copy raw private vault contents into the public canonical repo. Cross-model read access to a private spoke must be explicitly configured and verified; it is not automatic. Model labels denote intended connector identities, not proof of credential isolation.

## Minimum viable workflow

1. An agent reads the hub and any explicitly authorized peer spokes.
2. The agent drafts findings in its own spoke, including source links and an evidence tier (`confirmed`, `user-reported`, `historical`, `proposed`, or `unknown`).
3. A peer may review the draft read-only and place a separate review in its own spoke.
4. Owner selects, edits, and promotes a vetted artifact into the canonical hub through an owner-controlled branch and pull request.
5. Canonical changes cite their spoke origin, source revision, corrections, and owner approval. Rejected proposals remain in spokes and do not become facts.

## Access enforcement checklist (not yet configured)

- [ ] Create three **private** spoke repositories under the intended owner.
- [ ] Configure distinct GitHub App installations/credentials as supported by each AI client.
- [ ] Verify each integration can write **only its own** spoke, not the canonical hub or peer spokes.
- [ ] Verify each integration can read the canonical hub; grant sibling reads only as needed.
- [ ] Configure and test canonical `main` protection/rulesets and the owner promotion procedure.
- [ ] Inspect each repository's effective access with a real attempted read/write test (without destructive changes).
- [ ] Record exact repo URLs, permission evidence, and the date of verification.

**Permission caveat:** A fine-grained PAT's permission scope applies across the repositories selected for that token. Different read/write levels per repository generally require separate credentials or app installations. A connected assistant having an owner-authorized GitHub connector may still possess broad writes even if a document says otherwise; policy is not enforcement.

## Initial spoke layout

```text
README.md            # model identity, noncanonical status, how to submit research
research/             # dated drafts and experiments
reviews/              # reviews of cited commits in the hub or peers
```

No duplicated copies of the whole canonical vault. Reference hub files by GitHub path and pinned commit when possible.

## First verification experiment

1. Freeze the hub at a commit.
2. Give each model a distinct, harmless research prompt, with one source citation required.
3. Check its artifact lands only in its own spoke.
4. Ask another model to review that artifact without altering it.
5. Confirm unapproved drafts cannot reach canonical `main`.
6. Owner promotes one accepted paragraph through a PR, preserving exact provenance.

**Success criterion:** All allowed reads/writes succeed; unauthorized writes are denied by actual GitHub permissions; promotion is explicitly owner-approved; the result is traceable end-to-end. Log any failure rather than silently repairing history.

## Scope control

This is repository governance, not a new agent framework, search service, or indexing worker. Existing Obsidian and Markdown remain the writing and archival interface. Experiment 3 can test index quality independently after governance is stable.

## Open owner choices

- Whether sibling read access should be enabled immediately or on demand.
- Whether all agents should work from branches in their own spokes or may commit to spoke `main`.
- Whether the canonical hub should remain a public showcase while sensitive research stays private.
- Which GitHub client identities and permission mechanisms are actually supported.

**No repository creation, access-control change, or branch protection is implied by committing this proposal.**
