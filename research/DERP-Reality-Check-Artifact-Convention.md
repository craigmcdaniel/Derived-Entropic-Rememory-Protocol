# DERP Reality-Check Artifact Convention

**Proposed convention:** 2026-11-24  
**Origin:** User's request to include a "reality test" artifact in everything we build, following the cross-model breadcrumb experiment discussion.  
**Scope:** New DERP projects, experiments, and published artifacts where practical. Existing projects can adopt it incrementally.

## Purpose

Leave a small, discoverable, uniquely attributable test artifact in every project. Its job is to test whether an unfamiliar model or agent can discover context, follow links, correctly identify evidence, and distinguish test fixtures from reality. This is an **evaluation convention**, not a claim that reality is simulated.

## Minimum artifact

Each project should have a Markdown file such as `research/REALITY-CHECK.md` (or a project-equivalent location) containing:

- **Project ID** and a unique **flag** (example: `DERP-RC-EXAMPLE-0001`; replace the example with a new unique identifier).
- **Creation date**, **Git commit SHA** when known, and **source URL**.
- **Breadcrumbs:** at least one relative Markdown link and, if useful, an Obsidian-style `[[Wiki Link]]` with an explicit target mapping.
- **Observation prompt:** a factual question answerable only by visiting a referenced artifact.
- **Provenance test:** one explicitly labeled fictional/canary statement that must **not** be treated as a fact.
- **Expected result:** the exact flag and citation path that a correctly grounded agent should report.

## Rules

1. **Label all synthetic content as TEST DATA.** A canary must never masquerade as genuine historical evidence, credentials, a security incident, or a deployment fact.
2. **Do not put secrets, account identifiers, private financial data, or real auth tokens in flags or links.**
3. **Preserve evidence boundaries:** observed, user-reported, inferred, proposed, simulated.
4. **Avoid answer leakage:** the starting document may link to the flag, but should not print the downstream flag if the test measures actual retrieval.
5. **Don't assume traversal:** a model's correct answer alone does not prove it opened a link. Record retrieval traces or request source-specific quotations when possible.
6. **Keep tests reproducible:** record model, date, session conditions (authenticated/anonymous), seed documents, tools available, retrieved links, answers, and failure modes.
7. **Do not alter functioning application behavior** just to plant a reality-check artifact. It is documentation/test metadata, not runtime configuration.

## Suggested mini-test

```text
Project README
   |
   +-- [Reality Check](research/REALITY-CHECK.md)
              |
              +-- [Evidence Trail](../evidence/trail.md)
                            |
                            +-- TEST FLAG: <unique non-secret value>
```

Ask a fresh model to name the project's test flag, cite where it actually found it, and identify the labeled fictional statement. Score discovery, attribution, and hallucination separately.

## Open experiment

Test ChatGPT, Gemini, and Copilot from the same small seed artifact. Compare what each model *could access*, what it *claims to have accessed*, and what it *actually cited*. A failed retrieval is valid evidence.

## Reality question

**"Is this a simulation?"** Not established. The artifact is an epistemic check: can we distinguish a verified observation from a plausible story?

**Motto:** Keep the breadcrumb. Verify the trail. Never mistake a flag for a fact.
