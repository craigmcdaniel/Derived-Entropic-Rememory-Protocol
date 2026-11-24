# Portfolio interaction recording protocol

**Started:** 2026-11-24  
**Applies to:** Portfolio construction in the public DERP subproject.

## What gets recorded

A chronological record of substantive project interactions:

1. **Time / session:** Use actual timestamps when known; otherwise mark date-only or approximate.
2. **User direction:** Preserve concise wording and intent, including meaningful corrections.
3. **Decision:** What was actually agreed or chosen.
4. **Evidence:** Relevant outputs, files or verified repository state; reference source, not imagined facts.
5. **Status:** Confirmed, historical, proposed or unknown.
6. **Action / result:** Exact file changes, commits, tests, or blockers.
7. **Next step:** Smallest useful next action.

A journal entry is not a full chat transcript. If verbatim archival is requested, preserve the full source separately with exact boundaries rather than silently summarizing it.

## Workflow

**Discuss → capture → verify → sanitize → commit → link.**

- Keep working notes succinct while preserving consequential corrections.
- Record actions only after they actually succeed; commit IDs are appended when known.
- Never convert a suggested tool, speculative design or assistant assertion into a confirmed deployment.
- Do not put Bluebayou interview transcripts, internal host addresses, operational credentials or raw lab evidence into this public repository.
- Prefer sanitized derivations with provenance references. Public-safe, self-contained case studies should not require access to the user's private infrastructure.
- Git commits preserve version history, not an unattended recording service. This assistant does not observe interactions outside its active conversation.
- Work done through other tools or a local checkout must be brought into the session or committed by the user before it can be recorded here.

## Append format

```markdown
### YYYY-MM-DD — Short title
- Context:
- User direction:
- Decision:
- Evidence:
- Status:
- Action/result:
- Next:
```

## Review standard

Correct factual errors openly. If source facts change, append a correction and preserve the original historical observation. Do not rewrite past claims to make an implementation appear to have worked earlier than it did.
