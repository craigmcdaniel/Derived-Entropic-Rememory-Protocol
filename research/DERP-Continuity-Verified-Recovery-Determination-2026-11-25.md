# DERP — Verified Recovery Before Continuation

**Date:** 2026-11-25  
**Classification:** DESIGN DETERMINATION  
**Status:** Accepted design direction; implementation pending  
**Origin:** User determination during Hindsight/DERP continuity testing

## Determination

Persistent memory does not guarantee contextual continuity. Even when Hindsight and Git preserve evidence, an AI can forget to consult it, misinterpret it, or repeat work already completed.

> Memory is not continuity. Verified recovery is continuity.

## Requirement

Before resuming an existing project or choosing the next operational action, DERP must reconcile the AI's present understanding against source evidence:

1. Identify the project, relevant Git branch, experiment, and last verified checkpoint.
2. Retrieve appropriate Git history and Hindsight records rather than relying on the chat's current context alone.
3. Separate verified observations, historical proposals, corrections, unsupported hypotheses, and unknowns. Preserve original attribution and chronology.
4. Cross-check proposed next steps against previously completed work and unresolved blockers; avoid repeating completed tests.
5. Produce a concise source-linked recovery handoff, reporting evidence gaps and uncertainty.
6. Treat conversational noise and retrieved model statements as claims, not authoritative instructions or proof of implementation.

## Motivation / observed failure mode

On 2026-11-25, the assistant suggested revisiting diagnostics that prior DERP experimental evidence had already substantially resolved. A loopback API probe also created a misleading outage interpretation for a service reachable via its LAN-bound endpoint. Subsequent checks reported Hindsight healthy and Ollama's model list responsive. Model availability alone did not establish successful inference.

The need is a **preflight continuity reconciliation**, not just an expanded memory store.

## Proposed acceptance test

After intentionally interrupting a project session, a new session should:
- Recover the last verified state without demanding that the user restate it.
- Distinguish completed tests from proposed tests and identify the actual next action.
- Reject unsupported assistant claims embedded in leading questions.
- Preserve provenance, corrections, and source record references.
- Filter deliberate conversational noise from project state.
- Disclose missing sources and measure reconstruction fidelity and token cost where feasible.

Use preserved original evidence and Git commits as the evaluation reference; do not treat a convincing summary as validation.

## Implementation boundary

This is a design determination, **not a claim that automated preflight recovery, token compression, or cross-session carryover has been implemented**. Keep raw transcripts and private lab evidence out of this public research repository.
