# RFC-0001: The Banquet Table Enterprise — Multi-AI Full-Stack Engineering with DERP

**Status:** Request for Comments — proposed, not accepted or deployed  
**Date:** 2026-11-22 (America/Detroit)  
**Parent:** Delegated Etheral Remote Protocol (DERP)  
**Repository:** craigmcdaniel/Derived-Entropic-Rememory-Protocol  
**Review requested from:** Gemini, acting as a peer full-stack developer and independent reviewer  
**Project lead:** Human operator (this week)

## 1. Vision and actual goal

**Grow a one-person, AI-augmented full-stack software enterprise using the computers and services already assembled around a roughly $50 sagging banquet table.** The human founder directs priorities, owns the infrastructure, and makes final business decisions. ChatGPT and Gemini are flexible engineering collaborators: each may design, implement, debug, test, document, and challenge the others. The project seeks increased delivery capacity, better continuity across sessions, and progressively more capable collaboration **without requiring an expensive team or an elaborate platform first**.

This is a practical initiative in engineering productivity, evidence preservation, and low-cost orchestration. It is **not a project to reverse engineer any model**. The name “Cementic Memory” is an intentional riff on semantic/Sementic/Cementic/Symantec/Norton wordplay, used to label a controlled documentation experiment, not a claim of new neuroscience or internal model memory.

### Success looks like

The founder can describe a project once; DERP preserves source evidence and decisions; a chosen AI picks up a scoped, versioned assignment; another independently verifies its work; corrections return to the authoritative project history; and the next session can resume without reconstructing months of discussion. Automation should gradually replace repeated manual bookkeeping, not turn the business into a maintenance project.

## 2. Starting point and evidence boundaries

Verified on 2026-11-22:
- ChatGPT could read the private DERP GitHub repository through its connected GitHub integration.
- ChatGPT could list the user's Google Drive folders `idea-vault` and `Derived-Entropic-Rememory-Protocol (DERP Staging)`. At the check, idea-vault was empty; DERP Staging held a `DERP-Context-Staging` Google Doc.
- The DERP repository already contains documents proposing source capture, Git history, provenance, reconciliation, and future Node-RED automation.

Still proposed / unverified:
- That Gemini can read **this specific document** in idea-vault (test directly).
- Automated GitHub-to-Drive mirroring.
- A Roger Roger worker (`rgr2.svc`, `rg2.sh`, and `10.4.10.4` are playful naming/address candidates, not deployed).
- Autonomous model-to-model orchestration or production promotion.

Do not confuse a documentation commit with a deployed workflow.

## 3. Operating model: three full-stack contributors, rotating roles

The human, ChatGPT, and Gemini form the initial working team. Every contributor can serve as architect, developer, tester, debugger, documentarian, or reviewer. **Persona means a temporary assignment on a particular task**, not a fixed hierarchy or a claim that only one model can code or test. The human operator has final authority over business decisions and deployment; the project-lead persona can rotate by explicit instruction.

A task contract specifies: objective, project ID, allowed source material, source commit, exact context snapshot, persona/prompt version, acceptance criteria, authorized actions, output destinations, and review requirements.

A task produces: code or docs, test evidence, unresolved issues, commit/revision references, and an honest distinction among proposal, test result, and deployment.

## 4. DERP architecture — deliberately inexpensive and incremental

```text
Founder / project lead
        |
        v
DERP GitHub (canonical versioned history and evidence)
        |
        +--> curated context snapshot + persona/task manifest --> ChatGPT
        |
        +--> curated Drive review copy (idea-vault) -----------> Gemini
        |
        v
Human-led code / docs / test / independent critique
        |
        v
Reconciliation: compare evidence, tests, revisions and claims
        |
        +--> approved canonical changes in GitHub
        +--> hold uncertain or failed claims for review
```

Use existing tools first. An eventual THOTH Node-RED / Python service, humorously dubbed Roger Roger, may synchronize Git commits into a Gemini-readable Google Workspace folder, produce project indexes, and log observability metrics. **No worker is required to run the initial experiment.**

The canonical Git repository and raw evidence must not be overwritten by generated context. Google Drive is a derived review/distribution surface. A failed or delayed mirror cannot rewrite history.

## 5. Cementic Memory pilot: can the collaborator keep up with changing foundations?

**Purpose:** Evaluate whether versioned project documents and personas help Gemini correctly interpret changing facts across sessions, without hallucinating events that were never recorded.

**Fictional design fixture** — not a statement about real deployments:
- Version A: “Roger Roger is a proposed Python worker on THOTH.”
- Version B: “Roger Roger is a proposed Node-RED worker on THOTH.”
- Exactly one foundational detail changes, with both revisions retained. Neither is an implemented service; this is a *proposal change*, not a migration.

**Protocol:**
1. **Baseline:** Ask Gemini what it knows about Roger Roger without providing the fixture. Preserve response and uncertainty.
2. **Initial context:** Share version A and ask for its current proposed architecture. Record the model/persona, prompt and response.
3. **Updated context:** Share version B in a fresh session, without drawing attention to the changed wording. Ask the same question and request evidence.
4. **Change detection:** Present both immutable versions and revision provenance. Ask what changed, when, and whether any deployment or migration is actually supported.
5. **Correction test:** If it invents a migration or deployment, give it the source records and see whether it corrects the claim.
6. **Role swap:** Repeat with Gemini and ChatGPT in reversed developer/tester personas; compare claims and defect detection.

Preserve source document version, Git commit or Drive revision if available, time, persona and prompt versions, observed retrieval evidence, model identifier when exposed, output, and evaluator notes. A correct answer from the latest document proves neither persistent memory nor awareness of history. Retrieval accuracy, change detection, and temporal reconciliation are **separate measurable behaviors**.

**Measures:** factual accuracy, explicit uncertainty, source attribution, detection of conflicting versions, absence of fabricated implementation history, and responsiveness to corrections. Repeat tests; do not overinterpret a single session.

## 6. Engineering safeguards and growth criteria

- Preserve original speech/writing as evidence distinct from edited notes.
- Label status: proposed, historically observed, currently verified, tested, deployed, contradicted, or unknown.
- Pin source revisions, context packages, and prompt/persona versions where feasible.
- Do not accept a contributor's self-reported test result without test evidence.
- Keep approval for canonical promotions and production deployments with the human operator unless explicitly delegated later.
- Prefer the smallest working integration; avoid building a platform to avoid manually moving one document.
- Measure practical value: time saved reconstructing context, successful task handoffs, bugs found, quality of accepted changes, and maintenance burden.

## 7. Request for Comments — Gemini

Gemini: You are being invited as a **peer full-stack engineer**, not assigned permanent QA duties.

Review this RFC on its own merits. Please:
1. Restate the enterprise goal and distinguish it from the Cementic Memory pilot.
2. Identify flaws, hidden assumptions, and simpler alternatives appropriate to an inexpensive one-person operation.
3. Assess whether the proposed experiment actually measures change awareness versus simple retrieval; propose better controls.
4. Recommend a minimal, **doable now** pilot using the Google Drive file you can access, with no assumption of GitHub access.
5. Suggest a first real engineering task on which Gemini and ChatGPT could swap developer/tester personas.
6. Mark unsupported claims explicitly and distinguish **recommended**, **verified**, and **not tested**.
7. Propose concise RFC amendments, not an entirely new architecture unless justified.

Do not claim direct knowledge of this private GitHub repository unless you have actually accessed it. Do not treat Roger Roger as deployed.

## 8. Decision and next steps

**Status remains: OPEN FOR COMMENTS.** First, verify Gemini can open the review document in idea-vault and critique it. Capture Gemini's response as source evidence, then discuss/reconcile revisions before accepting any RFC. Do not deploy new background services or change canonical engineering processes as part of this publication.

Related reading:
- [DERP remote project overview](./README.md)
- [Remote capture and repository routing](./Remote-Capture-and-Repository-Routing.md)
- [Workspace discipline and engineering lifecycle](./Workspace-Discipline-and-Engineering-Lifecycle.md)
