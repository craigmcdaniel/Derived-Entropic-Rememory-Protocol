---
title: DERP Research Backlog
created: 2026-11-22
updated: 2026-11-22
type: research-log
status: active
tags:
  - derp
  - research
  - backlog
  - rememory
---

# DERP Research Backlog

An append-oriented log for ideas, experiments, and unresolved integration questions. Keep original concepts distinguishable from implementation status; preserve revisions in Git.

## 2026-11-22 — Gemini Chat as a staging bridge

**Status:** Proposed / research backlog  
**Origin:** Conversation with user, November 22, 2026  
**Priority:** Back burner; no automation requested yet

### Intent

Use **Gemini Chat itself** as an additional conversational entry point to the same DERP knowledge vault. Google Drive is an intermediate staging mailbox, **not** the desired permanent database or synchronization mechanism.

### Proposed flow

```text
Gemini Chat
   ↓ writes
Google Drive: Derived-Entropic-Rememory-Protocol (DERP Staging)
   └── DERP-Context-Staging (Google Doc)
   ↓ ChatGPT reads and reconciles on request
Private GitHub: craigmcdaniel/Derived-Entropic-Rememory-Protocol
   ↕ Obsidian Git pull / commit-and-sync
Local Obsidian vault: H:\Vaults\DERP-Vault
```

ChatGPT can also commit Markdown directly to GitHub without passing through Gemini. **GitHub is the intended canonical versioned record**; the staging Google Doc is transient intake.

### Verified on 2026-11-22

- ChatGPT connector located and read the Gemini staging Google Doc.
- ChatGPT committed the dated staging snapshot to the private GitHub repository.
- ChatGPT committed a synchronization test note to GitHub; user confirmed it appeared in Obsidian.
- User committed and synchronized local Obsidian files; ChatGPT verified the remote Git commit (10 files).
- Therefore **ChatGPT ↔ GitHub ↔ Obsidian** was tested in both directions.

### Unverified / research questions

- Does Gemini reliably append or revise the intended Google Doc across sessions without replacing earlier context?
- Can Gemini-to-GitHub import be made low-friction while preserving the original wording, attribution, chronology, and correction history?
- What is the simplest way to detect new staging entries and avoid duplicate imports?
- What conflict-handling rules are needed if ChatGPT, Gemini, and Obsidian edit related material independently?
- Should a later automation reconcile staging periodically, or remain user-triggered?

### Operating rule for now

On request (e.g., **“Sync Gemini staging to DERP”**), read the staging document, compare against existing committed material, and commit only new or corrected Markdown content. Treat every observation as **confirmed, historical, proposed, or unknown** with its relevant time/source. Do not claim unattended automatic cross-assistant synchronization.

### Related notes

- [[DERP-Context-Staging-2026-11-22]]
- [[ChatGPT-Obsidian-Sync-Test-2026-11-22]]

## 2026-11-22 — One-person enterprise: personas, provenance, and revision history

**Status:** Idea to hone / research backlog  
**Origin:** Conversation with user, November 22, 2026  
**Priority:** Exploratory; no new infrastructure authorized

### Core premise

Ask how a **one-person development team can approximate useful enterprise capabilities** by combining specialized AI personas, a shared repository, reproducible evidence, and versioned institutional memory—without importing enterprise bureaucracy.

The user's core question: **"how does a 1 man dev team match an enterprise, revision history and persona's."**

### Proposed functional roles (not separate employees)

- **Human architect / owner:** chooses priorities, makes decisions, accepts or rejects changes.
- **ChatGPT:** research, conversation capture, reconciliation, documentation.
- **Gemini Chat:** second conversational input and alternative analysis, with Google Drive used as staging when appropriate.
- **Codex:** potential implementation, tests, and repository operations.
- **GitHub:** canonical history of committed files, not proof of truth by itself.
- **Obsidian / DERP:** local linked notes, evolving knowledge, historical context and retrieval.

These are *possible workflow roles*, not guarantees that personas have independent judgment or that any currently untested integration is operating.

### Hypothesis to test

Persistent, shared records may let a solo developer recover past decisions and delegate bounded tasks across AI interfaces without depending on any single model session's memory. Compare this against the costs of review, context drift, conflict resolution, and coordinated mistakes.

### Research questions

- What minimum persona definitions actually improve quality versus simply duplicating the same assumptions?
- How should each contribution record **author/source, event time, collection time, evidence, inference, and corrections**?
- How do we separate an independent test from two models repeating the same claim?
- What review or acceptance gate should precede a change to production systems?
- Can Git commit history and linked Obsidian notes reconstruct **why** a decision changed, not merely **what** changed?
- What is the smallest useful workflow for a one-person team without meetings, approval theater, or unnecessary services?

### Current boundary

**Verified:** ChatGPT–GitHub–Obsidian bidirectional file exchange and versioned Markdown commits.  
**Proposed:** Durable multi-persona coordination and routine automated handoffs.  
**Not established:** Enterprise-level reliability, independent AI verification, or unattended conversation archival.

### Related

- [[DERP-Context-Staging-2026-11-22]]
- [[ChatGPT-Obsidian-Sync-Test-2026-11-22]]

## Log maintenance

Add later experiments as dated entries. Prefer preserving prior observations and appending corrections rather than rewriting history.


## 2026-11-24 — 04:30 EST — FREYR and embedded DERP brainstorming

Status: research/proposed; correlation with other research deferred. User ended session to rest.

- FREYR: financial DERP, first practical reference implementation. Branch `feature/thoth-finance` created from `main` in `craigmcdaniel/thoth-git`. No deployment implied.
- Watch directories for bank statements and paycheck stubs; extract embedded PDF text first, OCR when necessary. Preserve originals, hashes, dates, extraction confidence, corrections and duplicate detection. PostgreSQL holds authoritative financial records; Grafana provides budgeting, payroll, spending, reconciliation and cash-flow analytics. Potential utility/HVAC/power correlation and QuickBooks-style accounting.
- Design for AI chatbots from inception: deterministic accounting, model-independent interfaces, read-only access initially, proposed corrections rather than silent writes.
- Architectural inversion: embed Git in projects rather than merely embedding projects in Git. Applications can checkpoint, compare, branch, reconcile and publish approved configuration/documentation changes. Keep sensitive financial records and secrets outside Git.
- SQLite is an index for documents, not a document archive. Index paths, sections, keywords, relationships, source revisions, hashes and timestamps. Original documents remain authoritative; index is rebuildable. Explore federated project indexes and compact repository snapshots.
- Embed a portable Python SQL/query environment in each project, initially using standard-library sqlite3. Provide discovery instructions (AGENTS.md), schema, query CLI, structured JSON output and targeted source retrieval. Avoid requiring AI to reconstruct all context from Markdown.
- Small HTTP-driven interface: initially view-only rather than full CRUD; manifest, health, schema, search, document retrieval, relationships and history. CLI, HTTP and optional MCP adapters share a query engine. Scoped, revocable API keys with hashed storage outside Git, project permissions and audit trail; possible later gateway on THOTH. No unrestricted SQL or writes exposed by default.
- Emerging idea: independently useful applications act as plugins to a larger household AI system; each carries its own knowledge index, version history and interfaces. Extract reusable DERP Core only after practical validation.

First milestone: drop a bank statement into a directory and see validated transactions in Grafana. Preserve this brainstorming entry without attempting broader research reconciliation now.


## 2026-11-24 — Shared semantic memory / Microsoft Copilot

**Status:** Proposed; direct Microsoft personal Copilot integration unverified.  
**Origin:** Follow-up conversation, November 24, 2026.

The user clarified that Copilot should access the **same semantic memory over the Git-backed Obsidian Markdown environment** as ChatGPT or future local models, rather than simply reviewing an exported note. The vault is model-independent persistent knowledge; a rebuildable index and retrieval API supplies source-linked context to multiple agents. Keep Git as the versioned evidence record. Personal Microsoft Copilot, Microsoft 365 Copilot, GitHub Copilot, and an Obsidian plugin named Copilot are different integration targets. Prefer personal over institutional identity for tests, but verify real connector support first. Cross-agent context portability is the proposed success metric.

**Full research note:** [[Multi-Agent-Semantic-Memory-Copilot-2026-11-24]] — architecture, identity boundaries, capabilities, uncertainties, experiment plan. Deliberate overlap with the 04:30 FREYR/SQLite/HTTP brainstorming is retained.

## 2026-11-24 — Inventory interview: immediate work sequence

**Source:** User-directed one-question-at-a-time backlog inventory. **Status:** Priorities selected; task completion not implied. This records the work order rather than asserting specific TryHackMe module names or lab results.

**User direction (verbatim):** “I'd like to fuck around for a bit with check stubs and shit. Then we'll finish up this try hack me, putting it all together in planning and scoping, then there is a review task to recheck and verify the infection or whatnot is ok. then its on to our favorite, coding for penetration. the pthon an dpowershell stuff.”

### Prioritized sequence

1. **FREYR / CraigBooks: paycheck-stub exploration (active next).** Test extraction from an actual paycheck stub, understand gross pay, deductions and net pay, and identify reusable data fields. Treat this as exploration before building full automation. Financial source documents and extracted personal records remain in private storage; this public backlog records only project direction.
2. **TryHackMe: Planning and Scoping (next).** Complete current room/course exercises. Exact module/task identifier needs to be verified from the user's room before tracking completion.
3. **TryHackMe: review and verification task (then).** Recheck the infection-related result or state described by the task; scope and wording not yet independently inspected. Do not prematurely classify as verified or assume a live infection.
4. **TryHackMe: Coding for Penetration Testing (afterwards).** Continue Python and PowerShell training exercises within the course environment.
5. **DERP Core / VERN: architecture (deferred relative to current sequence).** Preserve the appliance concept, workers and indexes in the research backlog, without initiating additional infrastructure merely to support the first paycheck-stub experiment.

### Inventory state

- **Decision:** User has explicitly ordered these activities.
- **Confirmed completed:** None established by this interview turn.
- **Open:** Exact TryHackMe task names, original financial ingestion tests, and practical constraints for the paycheck-stub experiment.
- **Next interview question:** Determine the first paycheck-stub source format and whether a private local example already exists.

### Editorial boundary

No assumption that the first FREYR experiment must deploy PostgreSQL, Grafana, or a Python service. Extract and reconcile a sample first, then decide what code or storage is justified by the evidence.

## 2026-11-24 — DERPBooks architecture correction: Git-centric application from inception

**User correction (verbatim):** “the derpbooks was going to be the first project we made git centric from the get go with a dedicated data layer with sql ops”

**Status:** Architectural intent explicitly clarified; implementation unverified.

### Corrected scope

**DERPBooks** (earlier working names FREYR / CraigBooks in this backlog) is intended to be the **first application designed Git-centrically from the beginning**, with a **dedicated, queryable data layer exposing SQL operations**. It is **not merely a paycheck-stub extraction script** or a one-off dashboard experiment.

- **Git-centric lifecycle:** Project structure, code, schemas/migrations, query definitions, documentation, and approved configuration changes are versioned together, with source history and provenance integral to the application's workflow. “Embed Git in projects” is a design requirement for this pilot, not a speculative future add-on.
- **Dedicated data layer and SQL operations:** A persistent structured store and intentionally defined SQL query/write operations are part of the application's initial architecture. The exact DB engine and approved operation surface have not been decided here; earlier research mentions PostgreSQL for financial records and SQLite for document indexing, which serve distinct possible roles and should not be silently conflated.
- **Evidence model:** Preserve original financial documents privately, associate them with hashes, timestamps, extracted fields, revisions, reconciliation outcomes and Git-linked development provenance. Keep personal records and secret material out of the public DERP repository.
- **First use case:** Explore paycheck stubs to exercise ingestion, structured records, queries and reconciliation, not to define or limit the application's architecture.
- **AI interoperability:** The previously proposed portable Python SQL/query environment and optional view-only API are possible interfaces to the dedicated data layer; neither is confirmed built.

### Correction to earlier inventory wording

The preceding inventory entry over-simplified DERPBooks as “extract a check stub before deciding whether to build a database.” **Superseded:** A dedicated SQL-capable data layer and Git-centric design are foundational requirements. We can still choose a minimal first vertical slice without pre-building the entire financial application.

**Next inventory question:** Clarify the relationship between the financial records store (possibly PostgreSQL) and the repository-local index (possibly SQLite): one database or two distinct purposes? Preserve the decision before defining a schema or repository scaffold.

## 2026-11-24 — DERPBooks intake clarification: inbox/outbox PDF ingestion

**User's wording:** “and if you recall, taking inspiration from the inbox/outbox thing, and earlier the ocntent away nature of obsidian this is going to ingest pdfs the same way”

**Status:** Foundational design requirement clarified by user; pipeline not yet implemented or tested in DERPBooks.

### Required design

DERPBooks combines the previously discussed **inbox/outbox ingestion pattern** with the **Obsidian-style separation of content from its index**:

1. **File intake:** PDFs (initially paycheck stubs; later bank/financial documents) are placed into an incoming directory. This should be a deliberate, repeatable workflow, not a one-off paste into a chatbot.
2. **Original source preservation:** Keep the original PDF as an authoritative file. Track identity, hash, path, ingestion/source timestamps, and processing history. Preserve originals without rewriting them.
3. **Processing:** Extract embedded PDF text where available, OCR only where necessary; normalize candidate financial fields, record provenance and confidence, and track correction/review state.
4. **Structured data layer:** Ingest verified/approved fields and financial records into a dedicated SQL-backed layer, supporting queries, reconciliation and controlled modifications; never treat the document index as a replacement for the original PDF.
5. **Outbox / result area:** Produce reviewed outputs, extraction reports, indexes or sanitized summaries, with explicit association to source document IDs. Exact routing of successful, failed, and review-needing items remains to be designed.
6. **Git-centric project:** Version code, schemas, migrations, transformation definitions, documentation and approved metadata/configuration; keep private pay statements and sensitive financial data out of the **public** DERP repository. Git records application changes and provenance, not an automatic mandate to commit original financial documents.
7. **Obsidian-inspired storage principle:** Documents remain standalone files, the database stores searchable indexes/relationships and financial entities, and the links between them can be rebuilt from source evidence where practical.

### Architectural interpretation to verify later

Earlier brainstorming distinguished a **SQLite document index** from a **PostgreSQL authoritative financial ledger**. This is a possible two-layer implementation, not a requirement to run two database engines; the core user requirements are file-oriented ingestion and dedicated SQL operations from the start.

### Correction to prior backlog wording

The project is **not** a “check stub parser first, maybe add a database later.” A minimal initial vertical slice already includes inbox → document preservation → extraction → SQL indexing/records → outbox/reconciliation, all inside a Git-native application lifecycle.

**Next inventory question:** What should the outbox mean operationally—processed documents, reports for review, or both? Keep this open until the user defines the desired handoff.

## 2026-11-24 — DERPBooks alternative intake: HTML upload via API

**User's wording:** “or we could just have an upload mechanism on a html page edxposed via api”

**Status:** Proposed alternative to filesystem drop-folder intake; no deployment or selection confirmed.

The inbox/outbox requirement is **logical**, not necessarily a watched directory. Candidate intake front ends:

- A simple HTML form uploads a PDF to an application HTTP endpoint.
- A filesystem inbox can optionally feed the **same** ingestion service later; do not build duplicate extraction logic.

A minimal vertical slice would be browser upload → PDF validation → hash and original-file preservation → extraction → SQL records plus source linkage → reviewable result/outbox. Track extraction status and errors, but do not assume fields are correct until reconciled.

**Architecture invariant:** DERPBooks remains Git-native from inception, with a dedicated SQL operations layer and financial PDFs kept outside the public source repo. The API can later be reused by VERN and other permitted clients.

**Open design choice:** For the first prototype, HTML upload only versus HTML upload plus watched folder. No UI hosting endpoint or deployment target selected.

## 2026-11-24 — DERPBooks: extraction and transformation are mandatory

**User's wording:** “well I think it has to be extracted and transformed to be useful from the raw pdf”

**Decision:** Regardless of whether the intake adapter is an HTML form/API or an inbox folder, the first usable DERPBooks vertical slice **must convert PDF content into structured, validated financial data**, not merely store uploaded files.

**Required flow:** Receive PDF → preserve original and hash → extract embedded text/tables (OCR only if required) → transform document-specific labels and layouts into typed normalized earnings, deductions, taxes, dates and current/YTD amounts → validate totals and flag uncertain mappings → load accepted records into the dedicated SQL layer with document provenance → expose queries, reports and future Grafana consumption.

**Provenance requirements:** Link every parsed value to source document and extraction/revision; retain raw extractions, transformation rules, validation outcomes and correction history. Preserve failed/ambiguous records for review, not silently force them into a ledger.

**Status:** Design requirement, not implemented. Parser support, schema, review workflow and API contract remain unselected. The HTML upload vs watched-folder question is secondary to this shared ingestion pipeline.

**Next inventory interview topic:** What should count as an accepted transformation—automatic mapping only when reconciled, or a human review gate for the first paycheck documents?

## 2026-11-24 — DERPBooks: first real PDF specimen (private payroll document)

**Source:** User-supplied one-page paycheck PDF dated 2025-12-26; this public research log intentionally excludes all identifying fields, account details, pay amounts and the raw document.

**Inspection (2026-11-24):** PDF opened with PyMuPDF; one page, 2,061 selectable text characters, 52 text blocks and four detected tables. Native extraction is feasible; OCR is not needed for this sample. Visual inspection agrees that the page uses separate summary, earnings, deductions/taxes and deposit areas.

**Extraction and normalization challenges observed:**
- Columns distinguish current-period amounts from YTD amounts. Many rows contain only YTD values; blank current values must remain NULL, not be misinterpreted as current earnings.
- Some benefit/deduction rows carry separate employee and employer current/YTD columns; preserve all four dimensions, not just a single amount.
- Labels can wrap across lines, and certain glyphs use ligatures; extraction needs normalized labels plus preserved source text.
- Summary fields, detailed lines and deposit amounts need typed, independently validated relationships; totals alone do not establish full breakdown consistency.
- Source pointers should refer to document hash, page, row/section and extraction version, and any uncertain mapping needs review.

**Architectural implication:** The minimum first vertical slice is native PDF parse → document-type-aware transform → schema validation → staged SQL records → review/reconciliation, preserving the original privately. An HTML API upload or watched folder may both call the same ingestion worker.

**Status:** File inspection confirmed in current ChatGPT analysis environment; no DERPBooks service, SQL schema, worker, upload endpoint or database ingestion is deployed by this inspection. No private financial content was committed.

**Next decision:** Introduce a staging/review state for extracted pay records, then promote approved or rules-validated records into the financial ledger. Determine precise approval policy after testing a representative set of differing paycheck layouts.

## 2026-11-24 — DERPBooks initial source families: LCC and HNB

**User's wording:** “all the check stubs are from LCC only. Financial statements such as banking and what not are usually from HUNTINGTON national. Or HNB. I can share those too.”

**Inventory classification:** Source-format constraint confirmed by user, not evidence of a fully surveyed corpus.

- **Payroll family:** Lansing Community College (LCC) pay statements exclusively, according to the user. Begin with a specific LCC PDF transformer and validate across multiple periods before assuming perfect consistency.
- **Banking family:** Huntington National Bank (HNB) statements are the typical banking source. Await a sample before asserting statement layout, fields, text extraction quality, or parsing rules.
- **Common ingestion architecture:** Both arrive through file/upload adapters into a shared preserve/hash/extract/stage/review pipeline. Source-family-specific transformers produce typed records in a common SQL layer with source-document references and correction history.
- **Financial reconciliation opportunity (proposed):** Match approved net-pay deposit amounts to later bank transactions by amount/date and supporting references; do not infer matches or post transactions without verifying source evidence.
- **Privacy:** Sample PDFs and extracted personal financial content stay outside this public Git repository. Only sanitized format findings, schema decisions, implementation and tests belong here.

**Next inventory step:** Inspect one HNB statement as the second source family, then decide its minimum SQL entities and validation rules. No HNB statement has been provided in this turn; no HNB parsing has been performed.

## 2026-11-24 — DERPBooks: Huntington bank-statement PDF inspection

**Source:** One 4-page Huntington statement supplied privately by the user. This public log intentionally excludes the statement itself, financial amounts, account identifiers, customer identity and transaction descriptions.

**Technical inspection:** Four-page PDF generated by Actuate Document Transform 5.1 (PDF 1.4); all pages have extractable text. PDF catalog has neither `StructTreeRoot` nor `MarkInfo`, and the inspected file has no AcroForm. PyMuPDF's initial table detector returned zero tables despite recognizable text-aligned transaction sections. OCR is unnecessary for this specimen.

**Structural findings:** The document has a summary, credits/deposits, ATM withdrawals, debit-card activity, other withdrawals, periodic fees, balance history and disclosure pages. Some long transaction descriptions wrap to multiple lines or across pages; a transformer must reassemble them before interpreting monetary values. Preserve section names, page references, and date context.

**Validation:** At the statement summary level, signed opening balance + credits − debits − fees equals reported closing balance. This is a confirmed arithmetic check for the supplied specimen, **not** verification that every detail transaction has yet been extracted or reconciled.

**Architecture consequence:** Keep format-specific `hnb_statement` and `lcc_payroll` transformers behind one Git-centric PDF ingestion interface; use original files as evidence, structured SQL as queryable meaning, and explicit staging/review of ambiguous fields. Native text and positional reconstruction precede any OCR fallback. Bank-statement layout should not be assumed to have PDF accessibility tags.

**Status:** PDF inspection and summary arithmetic verified in analysis; no worker, SQL ingestion, cross-document matching, API endpoint or hosted application has been deployed. Await more specimens to check format stability and detailed transaction totals.

## 2026-11-24 — DERPBooks: transaction fidelity, categories and extensible budgets

**User decision (verbatim):** “yeah lets go that route, as its going to be extensible enough for me to be able to add budget entries and shit too”

**Decision / confirmed requirement:** Preserve **every individual imported bank transaction**, including its original bank-provided description, while allowing separately normalized merchant identity, categorization and user-entered budget entries. DERPBooks must support budgeting as a first-class feature rather than treating it as another extracted statement.

### Data model direction (design, not yet implemented)

- **Source documents:** Private original PDFs with hashes, paths, import timestamps, document type and extraction/revision IDs.
- **Statement + transaction facts:** Source-linked posted dates, statement periods, amounts, debit/credit direction, descriptions verbatim, transaction section and source page/location. Detect duplicates across overlapping statement imports using evidence rather than description alone.
- **Classification layer:** Separate optional normalized merchant/payee, user-editable categories/tags, mapping rules and revisions. Keep raw imported transaction facts unchanged when categorization is corrected.
- **Budgeting:** Distinct user-entered budget definitions/entries, applicable periods, categories and planned amounts. Budget items are **plans, not posted financial transactions**; compare budgeted versus actual only through explicit reporting/query logic.
- **Payroll:** Preserve LCC pay-period statements, earnings, deductions and pay deposits independently; future reconciliation may associate approved payroll net pay to HNB deposits without double-counting the income.
- **SQL operations:** Query transactions, grouped spend, category trends and budget-vs-actual; maintain controlled update paths for classifications and budgets. Every material correction should have provenance.
- **Extensibility:** Source-specific PDF adapters feed a stable normalized model; new financial institutions or additional manual data types should not require rewriting historical transactions.

**Status:** User-approved architectural direction only. Table schema, DB engine, API design, import worker and frontend are not yet built or selected.

**Next inventory question:** Should initial budget entries be entered manually by month/category, or should recurring budget rules also be included from the first version?

## 2026-11-24 — DERPBooks selects Go Money for initial evaluation

**User direction:** “ok lets pull in go money”

**Decision:** Evaluate the upstream open-source [Go Money](https://github.com/ft-t/go-money) application as a candidate DERPBooks ledger/financial engine rather than implementing all financial accounting primitives from scratch.

**Verified upstream capabilities from official source:** Multi-account double-entry accounting; transaction rules using Lua; PostgreSQL; backend/frontend Docker image; Grafana-friendly reporting; an MCP service including read-only SQL tools; and CSV/XLSX imports. The upstream documentation does **not** establish native parsing of the supplied LCC payroll or Huntington PDF formats; PDF ETL and provenance remain DERPBooks responsibilities.

**Deployment constraint:** Upstream example Compose installs a separate PostgreSQL/Grafana/Traefik stack, potentially conflicting with THOTH services. Do not deploy its example unmodified on THOTH or assume it is installed. First clone and inspect the repository on INFINITY's H: volume; then select an isolated deployment and explicitly account for existing Grafana, ports, storage and data isolation.

**Recommended working checkout:** `H:\DERPBooks\vendor\go-money` on INFINITY. This path is a proposed operator command destination, **not** a verified local clone. Upstream code remains separate from public DERP project records.

**Next evidence required:** User output from Git clone, upstream commit, Compose files and local Docker availability. Only after these checks mark it deployed or integrated. Review AGPL-3.0 obligations before distributing a modified network service.

**Status:** Upstream selected for evaluation. Local cloning/deployment not verified.

## 2026-11-24 — Go Money v1.8.0 Windows extraction and startup diagnostic

**Source of evidence:** User-pasted Windows PowerShell 5.1 transcript from INFINITY, working as `C:\Users\mcfuc`; Windows Explorer screenshot of `E:\dls`.

**Confirmed:** User downloaded and extracted both `go-money-server_1.8.0_windows_amd64.zip` and `go-money-mcp-client_1.8.0_windows_amd64.zip` in `E:\dls`. The extracted server folder `E:\dls\go-money-server_1.8.0_windows_amd64` contains `go-money-server.exe` (39,130,624 bytes), `LICENSE` (33,893 bytes), and `README.md` (7,516 bytes). Windows Firewall prompted when the user previously launched the server, but there was no visible application window. A process query searching names matching `go-money` returned no processes at the time of the user's test; TCP listener query for those processes likewise returned nothing.

**Script diagnostic correction:** Earlier general recursive search over `E:\DLS` was manually interrupted using Ctrl+C; do **not** interpret its empty output as evidence that the download was absent. Later direct folder enumeration succeeded and located the executable. The lack of process/listener confirms only that the server was not running when checked; reason for exit remains **unknown**. Native binary is not an Obsidian-style GUI; browser interface requires running server and its dependencies.

**Next step:** Start `E:\dls\go-money-server_1.8.0_windows_amd64\go-money-server.exe` inside PowerShell from its extracted directory and capture stdout/stderr plus exit code. Read the accompanying `README.md` for runtime options; do not assume DB or firewall error until actual output is collected. Do not claim installation at `H:` yet. User intends eventual installation/data on `H:`.

**Status:** Extraction verified; startup not yet diagnosed; no installation, database provisioning, or service deployment verified. Preserve future command/output checkpoints and append to Git regularly.

## 2026-11-24 08:20 EST — Go Money startup failure identified: PostgreSQL not reachable

**Source:** User-copied native PowerShell 5.1 startup diagnostic output from INFINITY. This event time is explicitly present in the application log.

**Command in use:** `& $Exe 2>&1` in PowerShell, from the v1.8.0 extracted Windows server directory at `E:\dls\go-money-server_1.8.0_windows_amd64`.

**Verbatim decisive output:**
```text
2026/11/24 08:20:34 github.com/ft-t/go-money/pkg/boilerplate/gorm.go:20
[error] failed to initialize database, got error failed to connect to `user=money database=money`:
        [::1]:5432 (localhost): dial error: dial tcp [::1]:5432: connectex: No connection could be made because the target machine actively refused it.
        127.0.0.1:5432 (localhost): dial error: dial tcp 127.0.0.1:5432: connectex: No connection could be made because the target machine actively refused it.
```

**Additional logged state:** JSON info message said `HTTP server started on port [52056]`; then `setup postgres database`; then fatal `failed to initialize database`. Process exit code `1`. The user's Windows Firewall permission dialog reappeared and was approved.

**Interpretation:** Go Money server binary executes, but its attempted PostgreSQL connection at loopback IPv6/IPv4 port 5432 was refused. The HTTP listener log reflects a transient startup, **not** a running operational service. No evidence yet whether PostgreSQL is installed but stopped, absent, on a different port, or remote. Windows Firewall prompt is not evidence of the root failure; no need to change firewall rules at this step.

**Next action:** Read-only local check for PostgreSQL services, processes, ports and executable locations on INFINITY; then configure or provision an isolated database on H: as suitable, keeping financial data off public GitHub. Do not assert PostgreSQL is installed or Go Money is deployed.

**Status:** Root immediate blocking dependency verified: no PostgreSQL accepting localhost:5432 at application startup; database provisioning still pending.

## 2026-11-24 — Go Money database placement reconsidered: THOTH PostgreSQL

**User evidence:** Full INFINITY PowerShell audit pasted. `Get-CimInstance Win32_Service` matching postgres/pgsql produced no entries; `Get-Process postgres,pg_ctl` no entries; `Get-NetTCPConnection -LocalPort 5432` no entries; `Get-Command psql,pg_ctl,initdb` no entries in PATH. User then explicitly stated **“we have one on thoth”**.

**Confirmed:** Local INFINITY audit did not detect a local PostgreSQL service, process, port 5432 listener or utilities in PATH. **User-reported:** PostgreSQL exists on THOTH. Its running state, host binding, port, version, auth policy, existing DB ownership and remote access remain unverified.

**Architecture proposal (not deployed):** Keep Go Money v1.8.0 server native on INFINITY, connect via network to a separate `money` database and `money` role on existing THOTH PostgreSQL, reuse THOTH Grafana for later DERPBooks reporting. Preserve financial data isolation and credentials outside public Git. No firewall or pg_hba.conf modifications until inspecting existing setup.

**Next read-only evidence collection:** On THOTH, check PostgreSQL service/container identity, listen addresses/port, cluster/database inventory (names only), and network listener. On INFINITY, test `Test-NetConnection 192.168.5.83 -Port 5432`. Then choose an isolated app database and Go Money DB connection configuration; no changes yet.

**Status:** Reuse of THOTH's PostgreSQL proposed; external access not verified.
