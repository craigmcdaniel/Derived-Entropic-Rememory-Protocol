# Basic Memory — Partial Integration and Worker Recipe Proposal

**Status:** Proposed / evaluation only; no installation, migration, or worker execution performed.
**Recorded:** 2026-11-23 (America/New_York).
**Parent:** [Delegated Etheral Remote Protocol](./README.md).
**Related:** [Obsidian Vault Bootstrapper](./Obsidian-Vault-Bootstrapper-Outline.md).
**Source:** User/assistant discussion in task “Suggest GPT model to test”, task ID 01a2086c-55a4-71f2-8d82-7550d3f76790. Individual message timestamps were not available; recorded date is not an event-time reconstruction.

## Verbatim user source

The following are selected exact user messages, not a complete transcript. Assistant interpretations are recorded separately below.

> earlier we looked at copilot integration, now lets look at applications that do what our obsdian pipeline does.

> Can it support using it as a storage for md files full of python to build on the fly via worker before it?

> So contrast basic memory vs our stack with obsidian, then with obsidian independent of our stack

> So we could modify part of what we are doing, and keep part of it.

> please commit our ideas regarding basic memory to the repository

## Edited interpretation and direction

Evaluate selective adoption rather than replacing the existing workflow wholesale. Basic Memory is a candidate for shared retrieval and persistent AI-accessible knowledge. Keep human-readable Markdown, Obsidian editing, Git/GitHub history, and DERP's preservation of evidence, corrections, uncertainty, and project chronology.

This records an architectural direction and a proposed experiment. It does not establish that Basic Memory is installed, that all clients can connect, or that its retrieval is better than our current workflow. The worker is a proposed separate component.

## Responsibility boundaries

| Component | Proposed responsibility |
| --- | --- |
| Markdown and supporting files | Portable canonical knowledge and source material |
| Obsidian | Human editing, navigation, links, and knowledge browsing |
| Basic Memory | Indexing, keyword/semantic retrieval, structured relations, and AI read/write tools |
| Git/GitHub | Versioned history, review, recovery, and exact source revisions |
| DERP practices | Raw versus interpreted records, provenance, corrections, uncertainty, and reconciliation |
| AI clients | Reasoning over retrieved evidence and drafting updates |
| Separate worker | Materialize recipes, resolve declared dependencies, validate, execute, and record outputs |

Proposed relationship:

```text
AI clients / orchestration worker
                |
       Basic Memory tools
                |
      Markdown project files
          /           \
     Obsidian       Git/GitHub

Execution worker -> isolated run directory -> outputs + execution record
```

Shared files do not eliminate concurrency problems. Define ownership, revision checks, and synchronization behavior before multiple clients write. Do not introduce competing sync mechanisms.

## Comparison

- **Basic Memory alone:** supplies a knowledge service and retrieval tools. The local core is not a complete autonomous execution worker, an AI model, or our evidence policy.
- **Our proposed stack:** combines memory with capture, reconciliation, versioning, model portability, and eventual execution. Existing and planned pieces must be inventoried separately.
- **Obsidian independently:** provides the notebook interface and local files. Semantic AI retrieval and external-agent access depend on additional components.

The intended benefit is less custom indexing and connector maintenance while retaining our methods and portability. That benefit remains a hypothesis until measured.

## Capabilities reviewed in vendor documentation

Documentation reviewed during this conversation describes Markdown-first storage with a secondary index, a file watcher, MCP tools, keyword/vector/hybrid search, metadata and cross-project filtering, observations and relations, optional schemas, and guarded writes using revision checks.

It also documents supported document extraction into Markdown beside originals, with ingestion provenance. Supported agent integrations provide recall/checkpoint hooks; lifecycle metadata capture is not a full conversation transcript.

Cloud adds managed remote access, editing, collaboration, sync, history/snapshots, and newer wiki/live-note and beta agent features. These are vendor-documented capabilities, not locally verified outcomes. Validate the installed release and actual client support before adopting them.

## Python-in-Markdown recipe library

Store small Python utilities in documented Markdown recipes that a worker can discover and build on demand. Basic Memory stores and retrieves the recipe; a separate worker runs it.

Proposed recipe fields:

- Stable recipe identifier and version/status: proposed, tested, or retired.
- Purpose, inputs, expected outputs, and assumptions.
- Python/runtime requirements and pinned dependencies where practical.
- Clearly designated code blocks and intended output filenames.
- Required file/network access and resource limits.
- Validation examples, expected results, and known limitations.
- Links to source evidence, related recipes, and previous revisions.

Proposed execution sequence:

1. Search by meaning to discover candidates.
2. Select and read an exact recipe path at a recorded revision; similarity alone is not authorization to execute.
3. Extract designated blocks into a separate working directory.
4. Resolve declared dependencies in an isolated environment and run appropriate checks.
5. Execute within the task's authorized scope.
6. Record recipe revision/checksum, generated-code revision where applicable, input references, dependencies, command, result, and output locations.
7. Save the execution record and reviewed knowledge updates; retain original source separately.

For larger programs, keep executable source in ordinary Git-tracked Python files. Markdown becomes the explanation and execution contract rather than a second unsynchronized copy of the program. Retrieval or schema validation does not prove code correctness.

## Initial evaluation proposal

Start with the free local version and a copy of one bounded Obsidian project. No wholesale migration or paid subscription is selected.

1. Record the baseline project snapshot and a small set of known-answer questions.
2. Configure indexing and one compatible AI client.
3. Ask for current state, supporting evidence, superseded decisions, and unresolved questions.
4. Repeat with a second AI client using the same knowledge.
5. Test a controlled note edit and subsequent retrieval; verify original wording survives.
6. Test conflicting edits and recovery before enabling shared writes.
7. Optionally run one harmless deterministic Python recipe and verify its execution record.
8. Compare retrieval quality, evidence accuracy, latency, resource use, setup effort, maintenance, and model costs with the baseline.

Accept only if it reduces friction without losing source fidelity, portability, or revision history. Keep the original vault unchanged during evaluation; a rejected experiment should not require rebuilding the archive.

## Open questions and cautions

- Which local host and AI clients should participate first?
- How will remote/mobile clients reach the knowledge without assuming local MCP is remotely accessible?
- Which schemas encode DERP records without rewriting existing source?
- What mechanism captures complete source conversations, separately from summaries?
- How are simultaneous edits, indexing delay, Git commits, and remote synchronization reconciled?
- Where does the worker run, and how are tested recipes distinguished from newly generated code?
- Can beta cloud agents add useful reconciliation later without obscuring original evidence?

Local Basic Memory is documented as free/open source; model subscriptions, API usage, and hosting are separate. Cloud pricing pages reviewed disagreed on starting price, so no fixed price is adopted here.

## Sources and evidence limits

Vendor documentation supports product-capability descriptions; the architecture, worker contract, and test plan above are our proposals.

- [Architecture](https://docs.basicmemory.com/reference/technical-information)
- [Local quickstart](https://docs.basicmemory.com/start-here/quickstart-local)
- [Search](https://docs.basicmemory.com/concepts/semantic-search)
- [Knowledge format](https://docs.basicmemory.com/concepts/knowledge-format)
- [Schemas](https://docs.basicmemory.com/concepts/schema-system)
- [MCP tool reference](https://docs.basicmemory.com/reference/mcp-tools-reference)
- [Document ingestion](https://docs.basicmemory.com/concepts/documents-and-pdfs)
- [Agent lifecycle capture](https://docs.basicmemory.com/integrations/harness-capture)
- [Client integrations](https://docs.basicmemory.com/integrations)
- [Cloud and local overview](https://docs.basicmemory.com/start-here/what-is-basic-memory)
- [Version 1.0 features](https://docs.basicmemory.com/whats-new/basic-memory-1-0)

**Next action:** inventory the current vault/retrieval workflow, then select a small copied project for a measured Basic Memory trial. This documentation commit does not install or enable anything.
