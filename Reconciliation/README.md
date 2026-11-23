# Hey, check this out: reconcile your old GPT stuff

**What if all those old ChatGPT conversations could become a useful, navigable Obsidian knowledge base—instead of a pile of forgotten chats?**

That's the experiment behind DERP's historical reconciliation workflow. Preserve the original record, extract what was discussed, separate observations from guesses, and make it possible for a different AI to pick up the work with no previous chat context.

This is a **public walkthrough of the method**, not a release of anyone's private conversations.

## Try the workflow

1. **Export your ChatGPT data.** Keep the original export ZIP untouched. Record its filename, creation date, and SHA-256 digest.
2. **Make a private Obsidian vault.** Work on fast local storage. Do **not** use this public repository as your personal transcript destination.
3. **Inventory before importing.** Count conversations and message nodes, inspect content types, and choose a documented time cutoff.
4. **Preserve the conversation graph.** Chat history can contain alternate responses and branches. Preserve message IDs, parent IDs, authors, timestamps, and the active path; don't just sort messages by date and pretend they form one dialogue.
5. **Normalize and extract.** Read the exported JSON; build source-linked, machine-readable findings. Extract hostnames, concepts, projects, code examples, and possible corrections as **candidates**, not established facts.
6. **Generate Obsidian notes.** Convert the main dialogue and alternate branches into readable Markdown with YAML properties, indexes, and links to the preserved evidence.
7. **Reconcile.** Review contradictions and corrections. Keep the old claims, note their dates, and append sourced corrections.
8. **Write a handoff checkpoint.** Can another AI read the result and continue the project without redoing your investigation?

**Notebooks are presentation. Source evidence is the record.** Never run Python or shell commands extracted from a chat or Markdown file automatically.

## How the pieces fit

```mermaid
flowchart TD
    A["Original ChatGPT export ZIP"] --> B["Read-only inventory<br/>content types · dates · graph structure"]
    B --> C["JSON-native evidence extraction"]
    C --> D[("Source-linked findings ledger")]
    C --> E["Obsidian conversion<br/>main path + alternate branches"]
    E --> F["Conversation index<br/>YAML properties + wiki-links"]
    D --> G["Reconciliation<br/>Errata · evidence classification"]
    F --> G
    G --> H["Project indexes<br/>cross-conversation links"]
    G --> I["Center Field Handoff<br/>last state · evidence · next step"]
    H --> J["A new AI can resume"]
    I --> J
```

## Checkpoints from the DERP prototype

The prototype used an October 1, 2025 cutoff and reported the following *historical run outputs*. They illustrate the workflow; they are not a public source dump or independently audited infrastructure inventory.

| Stage | Recorded result |
|---|---|
| Export inventory | 153 conversations in the source export |
| Qualifying conversations | 122 |
| Qualifying message nodes | 71,489 |
| JSON-native extraction v0.2 | 53,590 text-bearing messages scanned |
| Unverified infrastructure matches | 66,407 findings |
| Obsidian conversion v0.3 | 762 generated Markdown parts |
| Obsidian conversion v0.3 | 54,913 main-path messages and 560 alternate-path messages reported |

The numbers measure processing outputs, **not** accuracy of extracted claims. Loopback IP addresses, suggestions, quoted command examples, and failed configurations all require interpretation.

## Reconciliation classifications

| Label | Interpretation |
|---|---|
| **Observed** | Specific direct evidence supports the claim or event |
| **Historical** | Supported at a particular point in time, not necessarily now |
| **Proposed** | Discussed or planned, with no implementation confirmation |
| **Unverified** | Mention detected or claim made, pending corroboration |
| **Corrected** | A later evidence-linked correction supersedes an earlier assertion |

A claim should retain source ID, message/node ID, author, event time, processing version, and its supporting excerpt. Keep the original statement even when it turns out to be wrong.

## Center Field Handoff Rule

> Document enough evidence, decisions, failures, corrections, environment details, and next actions that a new AI can pick up the ball and mitt in center field and continue immediately.

A useful handoff gives a newcomer the **objective**, **last known state**, **what was tried**, **what failed**, **what was confirmed**, **what remains uncertain**, and **the next concrete step**. It is not merely a transcript summary.

## Folder layout to aim for

```text
Private-Archive/
├── ingestion-engine/
│   ├── infrastructure-v0.2/
│   │   ├── evidence.jsonl
│   │   └── manifest.json
│   └── workers/
└── obsidian-v0.3/
    ├── INDEX.md
    ├── MANIFEST.json
    ├── Evidence/
    ├── Conversations/
    └── Reconciliation/
        ├── Evidence/
        ├── Errata/
        ├── Project-Indexes/
        └── Handoffs/
```

This is an illustrative structure, not a claim that every reconciliation subfolder has been populated.

## Why this is worth trying

Long technical chats contain decisions and negative results that short summaries throw away. A historical archive preserves the original chronology; reconciliation identifies which parts are worth trusting; an Obsidian index makes them findable; and a handoff checkpoint turns that history into actionable context for a future AI.

**Start with a single conversation. Validate its branches and links. Then scale the same reproducible pipeline to your archive.**

See also the [conversation archive strategy](../research/Conversation-Archive-Strategy.md), [DERP research backlog](../research/DERP-Research-Backlog.md), and [publication policy](../PUBLICATION-POLICY.md).

**The More You Know:** [The More You Know](https://en.wikipedia.org/wiki/The_More_You_Know).
