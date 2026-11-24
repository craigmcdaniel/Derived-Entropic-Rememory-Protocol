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

## 2026-11-24 — THOTH PostgreSQL confirmed live, database reuse checkpoint

**Source:** User-pasted THOTH SSH terminal output, 2026-11-24. Earlier lines of same paste re-show prior Grafana quarantine commands and verification; they are historical context, not newly performed cleanup at this checkpoint.

**Exact relevant commands from pasted output:**
```bash
systemctl list-units --all --type=service 'postgresql*' --no-pager
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}' 2>/dev/null | grep -Ei 'NAMES|postgres|pgsql'
sudo ss -lntp | grep -E '(:5432|:5433|postgres)' || true
psql --version 2>/dev/null || true
```

**Verbatim key results:**
```text
postgresql.service         loaded active exited  PostgreSQL RDBMS
postgresql@18-main.service loaded active running PostgreSQL Cluster 18-main
LISTEN 0      200          0.0.0.0:5432       0.0.0.0:*    users:(("postgres",pid=1257,fd=6))
LISTEN 0      200             [::]:5432          [::]:*    users:(("postgres",pid=1257,fd=7))
psql (PostgreSQL) 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1)
```

**Reconciliation:** PostgreSQL is a *native THOTH service* running cluster `18-main`, not a Docker PostgreSQL container. It listens on all IPv4/IPv6 interfaces at port 5432, so remote connection is potentially possible. Neither `pg_hba.conf` rules nor INFINITY-to-THOTH connectivity has been checked; the `money` database/role do not yet have confirmed existence. No permission or firewall changes have been made.

**Grafana preservation corroboration:** Same paste shows 5 named JSON dashboards quarantined to `/home/thoth/grafana-cleanup-20261124/removed`, 3 explicit keepers retained; provisioning `disableDeletion: false`, `updateIntervalSeconds: 10`; subsequent file list contains 9 remaining dashboard JSON files and `systemctl is-active grafana-server` returned `active`. This is previous cleanup evidence, not a new operation.

**Next:** Run `Test-NetConnection 192.168.5.83 -Port 5432` on INFINITY. Then inspect THOTH's PostgreSQL role/database names and pg_hba access to see what isolated `money` provisioning requires. Keep all financial private data and any passwords outside public Git.

**Status:** Native PostgreSQL running and listening on THOTH; application DB integration not yet configured or proven.

## 2026-11-24 — INFINITY to THOTH PostgreSQL TCP connectivity verified

**Source:** User-pasted Windows PowerShell 5.1 output from INFINITY (`C:\Users\mcfuc`).

**Command and verbatim outcome:**
```powershell
Write-Host "=== INFINITY TO THOTH POSTGRESQL ==="
Test-NetConnection 192.168.5.83 -Port 5432 |
    Select-Object ComputerName, RemoteAddress,
        RemotePort, TcpTestSucceeded
```
```text
ComputerName RemoteAddress RemotePort TcpTestSucceeded
------------ ------------- ---------- ----------------
192.168.5.83 192.168.5.83        5432             True
```

**Confirmed:** INFINITY reaches TCP port 5432 at THOTH `192.168.5.83`; earlier THOTH output independently confirmed a running PostgreSQL 18.6 cluster listening there. This does **not** establish valid PostgreSQL credentials, `pg_hba.conf` acceptance, or existence of Go Money's `money` role/database.

**Next read-only audit:** `sudo -u postgres psql` database/role inventory and `pg_hba_file_rules` (don't disclose passwords or private financial data). Choose specific `money` role and DB without disturbing existing applications; validate application connection settings before writing changes.

**Status:** Network path CONFIRMED, database authentication/provisioning NOT YET VERIFIED.

## 2026-11-24 — PostgreSQL database/role inventory and HBA blocker verified

**Evidence:** User-pasted THOTH read-only PostgreSQL SQL query output (18-main).

**Verbatim inventory:**
```text
=== DATABASES ===
metasploit
netbox
postgres
template0
template1

=== ROLES ===
metasploit|t
netbox|t
postgres|t
```

**Verbatim pg_hba_file_rules output (columns abbreviated only in this note's heading):**
```text
 line_number | type  |   database    |  user_name   |   address   |  auth_method  | error
-------------+-------+---------------+--------------+-------------+---------------+-------
         118 | local | {all}         | {postgres}   |             | peer          |
         123 | local | {all}         | {all}        |             | peer          |
         125 | host  | {all}         | {all}        | 127.0.0.1   | scram-sha-256 |
         127 | host  | {all}         | {all}        | ::1         | scram-sha-256 |
         130 | local | {replication} | {all}        |             | peer          |
         131 | host  | {replication} | {all}        | 127.0.0.1   | scram-sha-256 |
         132 | host  | {replication} | {all}        | ::1         | scram-sha-256 |
         133 | host  | {metasploit}  | {metasploit} | 192.168.4.0 | scram-sha-256 |
(8 rows)
```

**Paths:**
```text
/etc/postgresql/18/main/postgresql.conf
/etc/postgresql/18/main/pg_hba.conf
```

**Reconciliation:** No `money` database or role exists. The visible PostgreSQL HBA rules contain only loopback host auth and a remote Metasploit-specific entry; none would authorize a remote Go Money connection. Earlier `Test-NetConnection` from INFINITY succeeded at TCP level but does not bypass HBA nor prove database login. Preserve existing Metasploit/NetBox databases and roles untouched.

**Next safe steps:** Verify INFINITY's actual IPv4 address used to reach THOTH and check upstream Go Money connection configuration. Subsequently create a least-privilege dedicated `money` role/database and narrow SCRAM HBA entry allowing only INFINITY's /32, with backed-up HBA, validate config and reload instead of restarting THOTH PostgreSQL. No changes have been made yet.

**Status:** DB provisioning and HBA change proposed, not executed.

## 2026-11-24 — INFINITY PostgreSQL route source confirmed; optional renumbering deferred

**Evidence:** User-provided INFINITY Windows PowerShell 5.1 `Find-NetRoute -RemoteIPAddress 192.168.5.83` and repeated `Test-NetConnection` output.

**Verbatim decisive evidence:**
```text
InterfaceAlias : vEthernet (Infinity Prime)
InterfaceIndex : 19
IPAddress      : 192.168.4.189
NextHop        :

InterfaceAlias : vEthernet (Infinity Prime)
InterfaceIndex : 19
IPAddress      :
NextHop        : 0.0.0.0

RemoteAddress RemotePort TcpTestSucceeded
------------- ---------- ----------------
192.168.5.83        5432             True
```

**Reconciliation:** The observed INFINITY source address for direct traffic to THOTH is `192.168.4.189`; THOTH PostgreSQL listens at `192.168.5.83:5432`, TCP verified. A candidate least-privilege PostgreSQL HBA entry is `host money money 192.168.4.189/32 scram-sha-256`; not yet applied. THOTH existing `metasploit` and `netbox` databases/roles must remain intact.

**User consideration:** May later change INFINITY's main IPv4 address to `192.168.4.2` for ease of use; no renumbering has been performed, uniqueness/reservation of `.2` is unverified. Recommendation: defer address change until the Go Money connection is validated, then revisit IP/DHCP/AD/DNS references and HBA rule together.

**Cultural aside:** User phrased `knwowhtimeanvern`, a playful reference to VERN and the proposed `n0wut1m34n.py` service naming.

**Next proposed change:** Create dedicated `money` PostgreSQL login and database on THOTH, back up `pg_hba.conf`, add narrow INFINITY-source SCRAM rule, reload rather than restart PostgreSQL, and verify connectivity. Do not commit plaintext credentials.

**Status:** Source IP verified; renumbering proposed, no network/database modifications confirmed.

## 2026-11-24 approximately 08:32 EST — Go Money PostgreSQL role and database provisioned

**Evidence:** User-pasted THOTH terminal output immediately following the earlier database-provisioning script. The original command generated a random credential into `$HOME/derpbooks/money-db-password` (mode 0600) and attempted `CREATE ROLE money LOGIN`, then created the `money` database with `--owner=money`.

**Verbatim output:**
```text
=== DERPBOOKS DATABASE PROVISIONING ===

=== CREATE DATABASE ROLE ===
CREATE ROLE

=== CREATE DATABASE ===

=== VERIFY ===
money|money

=== COMPLETE ===
```

**Confirmed:** The script reports `CREATE ROLE`, and subsequent SQL query reports `money|money`: PostgreSQL role `money` created and database `money` exists owned by `money` on THOTH. The generated private password file is expected at `/home/thoth/derpbooks/money-db-password` per the command but its file ownership, existence and contents have not been independently audited; never commit password material. Authentication and Go Money schema creation are not yet validated.

**Next:** Safely back up `/etc/postgresql/18/main/pg_hba.conf`, add specific `host money money 192.168.4.189/32 scram-sha-256` rule, validate rule parsing, reload PostgreSQL (not restart), then validate connectivity and app configuration. Preserve Metasploit/NetBox services.

**Status:** PostgreSQL provisioning confirmed; remote access and Go Money server still pending.

## 2026-11-24 08:33 EST — Go Money PostgreSQL HBA access rule added and reloaded

**Evidence:** User-pasted THOTH terminal output after suggested HBA modification script.

**Verbatim key output:**
```text
=== DERPBOOKS POSTGRESQL ACCESS ===

=== BACKUP ===
Backup: /etc/postgresql/18/main/pg_hba.conf.backup-20261124-083336

=== ADD ACCESS RULE ===
Rule added

=== RELOAD CONFIGURATION ===
t

=== VERIFY RULE ===
 line_number | database | user_name |    address    |  auth_method  | error
-------------+----------+-----------+---------------+---------------+-------
         135 | {money}  | {money}   | 192.168.4.189 | scram-sha-256 |
(1 row)

=== COMPLETE ===
```

**Confirmed:** THOTH `pg_hba.conf` backup created, specific allow entry for `money` role and database from INFINITY's `192.168.4.189/32` added, PostgreSQL reload returned `t`, `pg_hba_file_rules` parses entry at line 135 without error. Existing Metasploit/NetBox entries were not intentionally modified. SCRAM login of `money` user and end-to-end Go Money application startup still **unverified**.

**Upstream finding from project architecture docs:** `go-money-server` is backend-only; `go-money-full` Docker image includes web frontend. Earlier suggestion that native server binary alone would provide a browser financial UI needs correction. Go Money `DB_HOST`, `DB_PORT`, `DB_DB`, `DB_USER`, `DB_PASSWORD`, and `DB_SSL_MODE` are environment settings; verify against v1.8.0 release configuration before final setup. Frontend delivery may require separate build or `go-money-full` container, so don't promise native Windows GUI from server exe.

**Next:** Verify `money` credential by authenticating locally on THOTH via TCP loopback, then from INFINITY with env settings, ensuring secrets not printed or committed. No passwords in Git.

## 2026-11-24 — Go Money PostgreSQL local SCRAM authentication succeeded

**Source:** User-pasted THOTH interactive terminal output following the private credential file and loopback TCP login test.

**Command:**
```bash
PASSWORD_FILE="$HOME/derpbooks/money-db-password"
if [ ! -s "$PASSWORD_FILE" ]; then
    echo "PASSWORD FILE MISSING"
else
    PGPASSWORD="$(cat "$PASSWORD_FILE")" \
        psql -h 127.0.0.1 -p 5432 \
        -U money -d money \
        -Atc "SELECT current_user, current_database();"
fi
```

**Verbatim result:**
```text
=== GO MONEY DATABASE LOGIN TEST ===
money|money
=== TEST COMPLETE ===
```

**Confirmed:** PostgreSQL on THOTH accepted the dedicated `money` user's generated credential via local TCP SCRAM authentication, and the session connected to database `money`. No password value was exposed in console output or committed. The result does **not** yet confirm remote authentication from INFINITY, successful Go Money database migrations, or successful application/GUI startup.

**Next:** Confirm Go Money v1.8.0 configuration environment keys in upstream source/release documentation; configure INFINITY's backend to target `192.168.5.83:5432`, with password delivered privately and not logged, and capture startup output. Distinguish backend server from web frontend.

**Status:** Database-side local login CONFIRMED; application remote login unverified.

## 2026-11-24 08:36 EST — Go Money Windows backend connects to THOTH, MCP docs packaging blocker

**User-pasted Windows PowerShell startup evidence (Go Money v1.8.0, binary commit e423145):**
```text
2026-11-24T08:36:04-05:00 HTTP server started on port [52056]
2026-11-24T08:36:04-05:00 setup postgres database
2026-11-24T08:36:04-05:00 ========= DB [192.168.5.83] [money] ============
2026-11-24T08:36:04-05:00 [Db] start migrations
2026-11-24T08:36:05-05:00 SELECT * FROM "system_configurations" WHERE id = 'jwt_private_key' ... record not found
2026-11-24T08:36:05-05:00 jwt private key is empty. Generating new key and storing in database
2026-11-24T08:36:05-05:00 path ./mcp Reading mcp docs
2026-11-24T08:36:05-05:00 fatal: GetFileAttributesEx .: The system cannot find the file specified. failed to read mcp docs
Exit code: 1
```

**Reconciliation:** Native Windows server started only transiently; no Windows service or automatic startup was installed. Remote DB login succeeded and database migrations began, making durable changes on THOTH's dedicated `money` database. A missing MCP docs directory prevented startup completion. Upstream v1.8.0 source `pkg/configuration/types.go` confirms `MCP_DISABLE` defaults false and `MCP_DOCS_DIR` defaults `./mcp`; `pkg/mcp/docs.go` walks markdown files beneath that directory. Next quick test: set `MCP_DISABLE=true` before launching with DB environment; re-enable with docs later. Source: https://github.com/ft-t/go-money/tree/v1.8.0.

**User clarification request:** Asked whether the command actually dropped a server. Answer: only started a temporary process listening on ops HTTP port 52056, then exited code 1; did not deploy a persistent Windows service. Server data/schema changes persist in THOTH PostgreSQL.

**Status:** Database connected, startup blocked at optional MCP documentation; no persistent backend running.

## 2026-11-24 08:39 EST — Go Money Windows backend starts successfully against THOTH

**Source:** User-pasted INFINITY PowerShell stdout/stderr, from the retry with `MCP_DISABLE=true`, using Go Money v1.8.0 (`commit_sha=e423145`) native Windows server binary in `E:\dls\go-money-server_1.8.0_windows_amd64`. THOTH PostgreSQL `192.168.5.83:5432`, `money` database and role; database password obtained privately over SSH.

**Verbatim startup evidence (log messages):**
```text
2026-11-24T08:39:25-05:00 setup postgres database
2026-11-24T08:39:25-05:00 HTTP server started on port [52056]
2026-11-24T08:39:25-05:00 ========= DB [192.168.5.83] [money] ============
2026-11-24T08:39:25-05:00 [Db] start migrations
2026-11-24T08:39:25-05:00 using jwt private key from database
2026-11-24T08:39:25-05:00 job scheduler started
2026-11-24T08:39:25-05:00 server started on port 52055
2026-11-24T08:39:25-05:00 server grpc listening at 0.0.0.0:52055
2026-11-24T08:39:25-05:00 daily gaps fixed successfully
```

**Reconciliation:** Go Money backend completed startup sequence without fatal errors in provided output. It reported gRPC server on 52055 and ops HTTP listener on 52056. Initial PowerShell `NativeCommandError` comes from invoking native stderr with `2>&1`, not proof of server failure. User reported “we up” and no termination or exit code was shown. Independent process and port probes still pending. The backend is foreground-only, not installed as persistent Windows service. The native Windows release contains backend only; end-user financial web frontend remains to be provisioned. MCP temporarily disabled; no need to reenable until docs are supplied.

**Next:** From second INFINITY PowerShell session, verify process and TCP listeners; read `README.md` / upstream source for frontend build/deployment, then relocate to H: and plan service persistence. Preserve secrets outside Git.

**Status:** Application backend started successfully (log-confirmed), operational probe pending.

## 2026-11-24 — Go Money process/listeners independently verified and HTTP health routes identified

**Evidence source:** User-pasted second INFINITY Windows PowerShell 5.1 terminal query plus v1.8.0 upstream source review.

**Verbatim decisive output:**
```text
ProcessId      : 26104
Name           : go-money-server.exe
ExecutablePath : E:\dls\go-money-server_1.8.0_windows_amd64\go-money-server.exe

LocalAddress LocalPort  State
------------ ---------  -----
::               52056 Listen
::               52055 Listen
```

**Confirmed:** Go Money native backend was alive on INFINITY at test time and owns listening TCP ports 52055 and 52056. No persistent Windows service established. User asked whether there is an HTTP endpoint.

**Exact v1.8.0 upstream source verification:** `pkg/boilerplate/ops.go` registers `GET /health`, `GET /ready`, and `/metrics` through Prometheus HTTP handler on the ops HTTP server (`OPS_HTTP_PORT`, default 52056); `cmd/server/main.go` starts gRPC/application gateway service on `GRPC_PORT`, default 52055, and may register `/mcp` only when MCP is enabled. In current session MCP is disabled due to absent docs. Source paths: https://github.com/ft-t/go-money/blob/v1.8.0/pkg/boilerplate/ops.go and https://github.com/ft-t/go-money/blob/v1.8.0/cmd/server/main.go.

**Correct distinction:** HTTP operational endpoints do exist on 52056, but they are not the financial user-facing dashboard; 52055 is the application gRPC/HTTP gateway and is not itself a bundled native Windows GUI. Still need to test GET /health and GET /ready and provision/host the frontend separately.

**Next:** From INFINITY check `http://localhost:52056/health` and `/ready` (should return HTTP 200), then assess frontend delivery before deciding native Windows vs Docker for full UI.

**Status:** Process and port listeners confirmed; URL-level HTTP probe pending.

## 2026-11-24 — Go Money HTTP health and readiness confirmed; VERN interface separation

**Source:** User-pasted INFINITY PowerShell 5.1 live process check and local HTTP requests; user explicitly proposed using VERN as an independently adaptable interface to Go Money's backend.

**Verbatim key evidence:**
```text
ProcessId      : 26104
Name           : go-money-server.exe
ExecutablePath : E:\dls\go-money-server_1.8.0_windows_amd64\go-money-server.exe

LocalAddress LocalPort  State
------------ ---------  -----
::               52056 Listen
::               52055 Listen

health : HTTP 200
ready : HTTP 200
```

**Confirmed:** Windows Go Money server v1.8.0 was running on INFINITY and independently verified listening on ports 52055 and 52056. `Invoke-WebRequest` on `http://localhost:52056/health` and `/ready` both returned HTTP 200, establishing health and readiness at time of test. THOTH PostgreSQL `money` database connection was verified in prior startup logs. MCP remained temporarily disabled (`MCP_DISABLE=true`). This is foreground execution from E:\dls, **not** a persistent Windows service and not yet relocated to H:.

**Architectural idea (user wording):** “the server exists doing its shit ... how we display it is our own VERN, kwim”. Use Go Money as preexisting accounting system/backend and VERN as a separate flexible UI / ChatOps interface; use DERP as provenance/evidence system and planned document ingestion as adapter. Go Money has its own frontend that can be reused initially; a bespoke VERN presentation is **proposed**, not already built. Prefer supported API boundaries, not direct mutation of internal Go Money DB tables.

**Next:** Inspect Go Money v1.8.0 frontend hosting options and API routes, choose easiest working dashboard; then plan H: migration and durable service, while preserving separate THOTH DB and Git-based DERPBooks integration.

**Status:** Backend health/readiness verified, financial frontend and VERN integration not deployed.

## 2026-11-24 — DERPBooks visualization-first, no-manual-entry workflow priority

**User direction (verbatim):** “this is a cool project, I like the modularity.Yeah we need the front end, I'd say its not nearly as important as the visualization, but I don't want ot type shit in”

**Decision / priority:** Treat Grafana-based financial visualization and automatic source-document ingestion as priorities over hand-operated UI data entry. Go Money's native frontend remains desirable for administration, exceptions, corrections and fallback, but the daily workflow must not require manually transcribing bank statement transactions or payroll values.

**Proposed flow:** Original LCC paycheck PDF and Huntington statement PDF → private document inbox → Python layout-specific extraction/ETL → typed normalization, arithmetic reconciliation, duplicate detection, provenance linkages and review exceptions → supported Go Money API/import operations → THOTH PostgreSQL `money` database → existing THOTH Grafana dashboards. A later VERN adapter can support conversational queries and corrections. Keep raw source documents and any financial values outside the public repo; preserve unmodified transactions and their provenance separately from normalized descriptions and categories.

**Engineering constraint:** Verify Go Money v1.8.0's actual account, double-entry transaction and import semantics before implementing adapters or claiming PDFs are supported natively. Do not use direct SQL writes as a substitute for its accounting API. Never conflate planned budget entries with observed bank transactions.

**Current verified deployment:** Go Money v1.8.0 backend running in foreground from `E:\dls` on INFINITY, THOTH PostgreSQL reachable with dedicated database/role, both ops `/health` and `/ready` confirmed HTTP 200. Native frontend, Grafana finance dashboards, PDF ingestion and VERN connector are **not** implemented yet.

**Status:** Workflow preference captured, implementation proposed.

## 2026-11-24 — Go Money production schema inspected on THOTH: 18 tables

**Source:** User-pasted read-only THOTH `sudo -u postgres psql -d money` output after Go Money v1.8.0 backend startup. The command queried `information_schema.tables`, selected `information_schema.columns` for account/transaction/category-name tables, and measured database size.

**Confirmed output:** 18 public base tables (`accounts`, `app_configs`, `categories`, `currencies`, `daily_stat`, `double_entries`, `import_deduplication`, `import_ignored_transactions`, `jti_revocations`, `migrations`, `rules`, `schedule_rules`, `service_tokens`, `system_configurations`, `tags`, `transaction_history`, `transactions`, `users`). `pg_size_pretty(pg_database_size('money'))` returned `8630 kB`.

**Selected schema evidence:** `accounts` has `id`, `name`, `current_balance`, `currency`, `extra` JSONB, `type`, `deleted_at`, `account_number`, `iban`, `first_transaction_at`, `tag_ids`. `transactions` has distinct source and destination account IDs, amounts, currencies; `transaction_date_only`, `transaction_date_time`; `title`, `notes`, `extra` JSONB, `reference_number`, `category_id`, `deleted_at`, `voided_by_transaction_id`; base currency and FX fields. `transaction_history` includes `transaction_id`, `event_type`, `actor_type`, `actor_user_id`, `actor_rule_id`, `actor_extra`, `snapshot` JSONB, `diff` JSONB, `occurred_at`. `import_deduplication` and `import_ignored_transactions` are present.

**Interpretation:** Go Money has useful native structures for double entry, automated rules, history and import deduplication; whether its change history or deduplication meet DERP's exact source-document requirements remains untested. Avoid assuming historical snapshots replace independent immutable PDF lineage. No user financial transactions shown in this output.

**Next read-only checks:** Table row counts (do not print account numbers or monetary transaction details), relevant import/history/double-entry column metadata and constraints, and potentially default categories/accounts. Then plan a separate read-only PostgreSQL role for Grafana with narrow grants or explicitly defined views; do not give Grafana the owner/\`money\` role. Investigate official APIs for importing validated PDF-derived data; do not directly write Go Money's internal tables.

**Status:** Go Money schema creation verified. No Grafana finance datasource/dashboard or PDF ingestion deployed.

## 2026-11-24 — Go Money Angular frontend source checkout confirmed on H:

**Evidence:** User-pasted INFINITY PowerShell 5.1 transcript and THOTH schema-audit output.

**Confirmed frontend source checkout on INFINITY:**
```text
git version 2.52.0.windows.1
node v24.22.0
npm 11.19.1
Cloning into 'H:\DERPBooks\go-money'...
Note: switching to 'e423145d3058fc81d0d9f3592f3575655df8f219'.
e423145 feat(mcp): import dedup and delete tools, clearer import errors (#128)
angular.json        5322
package-lock.json 646433
package.json        2323
```

**Reconciliation:** The upstream Go Money repository v1.8.0 successfully cloned into `H:\DERPBooks\go-money`, detached HEAD at release tag commit `e423145`. Angular source manifest files are present at `frontend\`. Node 24/npm 11 and Git available. No evidence yet that `npm ci` ran, a frontend was built, served or connected.

**Companion THOTH accounting model audit (user-uploaded transcript):** `pg_stat_user_tables` estimated row counts included `accounts=5`, `currencies=166`, `daily_stat=10`, `migrations=30`, `transactions=0`, `double_entries=0`, `users=0`, `import_deduplication=0`. These are estimates, not transactional exact counts. `double_entries` has `transaction_id`, `account_id`, debit flag, base currency amount, transaction date; `import_deduplication` has `import_source`, `key`, `transaction_id`, creation time. PostgreSQL `pg_constraint` query returned **zero foreign key constraints** in `public`; therefore rely on application API/invariants, not direct SQL writes. No actual financial transactions imported.

**Upstream v1.8.0 frontend details:** Angular app under `frontend`; `package.json` scripts `start: ng serve` and `build: ng build`. `frontend/src/app/configuration/prod.json` and `dev.json` include `http://localhost:8000/` host defaults that do not match current INFINITY backend gRPC/Connect listener on port 52055. The build or launch must align app transport configuration; avoid claiming frontend works until actual browser/API handshake succeeds.

**Next:** `npm ci` in `H:\DERPBooks\go-money\frontend` only (keep packages and build on H:); inspect Angular client transport host/config mapping and arrange browser frontend connection via correct host/port, likely port 52055. No additional PostgreSQL/schema changes required now.

**Status:** Frontend source and prerequisites confirmed; install/build/serve pending.

## 2026-11-24 — Go Money Angular dependency install verified and same-origin transport identified

**Evidence:** User's INFINITY PowerShell 5.1 output from `npm ci` then `npm exec -- ng version` and `Test-Path .\\node_modules\\@angular\\core` under `H:\DERPBooks\go-money\frontend`.

**Verbatim key details:**
```text
Angular CLI       : 21.2.27
Angular           : 21.2.25
Node.js           : 24.22.0
Package Manager   : npm 11.19.1
Operating System  : win32 x64
=== VERIFY INSTALL ===
True
=== COMPLETE ===
```

**Interpretation:** Angular frontend dependencies have been installed under the H: source checkout; UI build and browser launch are not yet verified.

**Upstream source v1.8.0:** `frontend/src/app.config.ts` constructs a ConnectRPC transport and checks `CookieInstances.CustomApiHost`; when absent, defaults to relative `baseUrl: '/'`. A local Angular development proxy forwarding application requests to `http://127.0.0.1:52055` should permit same-origin frontend connectivity without editing upstream Angular files, provided the API supports browser transport and proxy path semantics. Although `frontend/src/app/configuration/*.json` contain localhost:8000 sample hosts, actual transport factory uses relative path unless overridden by cookie. Source: https://github.com/ft-t/go-money/blob/v1.8.0/frontend/src/app.config.ts.

**Next:** Add untracked H:-local Angular dev proxy config, run `npm start -- --host 127.0.0.1 --port 4200 --proxy-config <file>`, open `http://localhost:4200/`, validate login/api access against currently running native backend. Persist config deliberately in DERPBooks-owned integration layer, not by editing upstream vendor release. Do not publish credentials or data.

**Status:** Dependencies verified; frontend not yet running.

## 2026-11-24 — Go Money Angular build succeeds but proxy JSON fails at byte one

**Evidence:** User-pasted INFINITY PowerShell output from `npm start -- --host 127.0.0.1 --port 4200 --proxy-config proxy.conf.json` in the Angular v1.8.0 frontend checkout `H:\DERPBooks\go-money\frontend`.

**Verbatim decisive output:**
```text
Initial chunk files | Names         | Raw size
main.js             | main          |  1.06 MB
styles.css          | styles        | 80.37 kB
polyfills.js         | polyfills     | 95 bytes
Initial total                       | 1.14 MB
Application bundle generation complete. [5.648 seconds] - 2026-11-24T14:06:53.979Z
Watch mode enabled. Watching for file changes...
An unhandled exception occurred: Proxy configuration file H:\DERPBooks\go-money\frontend\proxy.conf.json contains parse errors:
[1, 1] InvalidSymbol
See "C:\Users\mcfuc\AppData\Local\Temp\ng-1wvHxJ\angular-errors.log" for further details.
```

**Diagnosis:** Angular application compiled, but development server failed to start because the proxy JSON could not be parsed. Earlier script generated this JSON with Windows PowerShell 5.1 `Set-Content -Encoding UTF8`, which writes a UTF-8 BOM. A BOM at the first byte is a likely cause of `[1, 1] InvalidSymbol`; this has not yet been independently confirmed by inspecting raw bytes, so treat as highly plausible rather than definitive. User's browser connection-refused symptom follows from Angular not starting.

**Remediation proposed:** Rewrite `proxy.conf.json` on H: using `[System.IO.File]::WriteAllText(path, json, (New-Object System.Text.UTF8Encoding($false)))`, then `ConvertFrom-Json` and rerun `npm start`. Test frontend loads and confirm API requests via DevTools. Keep backend and THOTH database unchanged.

**Status:** Angular compilation CONFIRMED; frontend runtime blocked by invalid JSON until successful rerun.

## 2026-11-24 — Go Money Angular frontend reaches login screen on INFINITY

**User observation:** “im at a login screen” after repairing Angular development proxy JSON encoding and launching the frontend at localhost:4200.

**Confirmed:** Angular development server was able to serve/render Go Money v1.8.0 login page on INFINITY. This resolves prior `[1, 1] InvalidSymbol` parse error / connection refused; no browser API authentication has yet been demonstrated. Go Money backend remained healthy at last check, on ports 52055 / 52056 and using THOTH's PostgreSQL `money` database.

**Upstream source verification:** `frontend/src/app/modules/auth/login/login.component.ts` calls `ConfigurationService.getConfiguration({})` on init; `shouldCreateAdmin` toggles register vs sign-in flow. Registration uses `UsersService.create`, then normal sign-in uses `UsersService.login`; thus fresh install is designed to prompt initial administrator registration, no default credentials implied. HTML shows Register only when `isRegisterFlow`, Sign In otherwise. This first user account concerns Go Money's app authentication, separate from PostgreSQL role `money`. Sources: https://github.com/ft-t/go-money/blob/v1.8.0/frontend/src/app/modules/auth/login/login.component.ts and corresponding `login.component.html`.

**Caution:** The current Angular dev proxy matches `/gomoneypb.**`; actual ConnectRPC requests need browser network verification for path and responses. A login page rendering alone does not establish that API calls work. Do not assert successful initial user creation or authenticated access until confirmed.

**Next:** Check whether page says `Register to continue` vs `Sign in to continue`. If register, user creates app administrator credentials in browser; no password supplied in chat/Git. If login API fails, capture status/URL and refine proxy. Later move from dev server to intentional H:-based production/frontend hosting.

## 2026-11-24 — Go Money login renders but Register option absent

**User observation (verbatim):** “nope just login, and can't rewire to /register”

**Confirmed code-level behavior, Go Money upstream v1.8.0:** `frontend/src/app.routes.ts` routes to `login` but has no `register` route. `frontend/src/app/modules/auth/login/login.component.ts` initially sets `isRegisterFlow=false`, then calls `ConfigurationService.getConfiguration({})` and updates the flag from `val.shouldCreateAdmin`. Registration uses `UsersService.create` on the same login page; the Sign In/Register button is conditional. `frontend/src/app/consts/demo.ts` enables demo mode when `localStorage.getItem('is_demo') === 'true'` or hostname `gomoney.ft-t.dev`; demo mode bypasses registration logic and forces normal sign-in. Previous PostgreSQL estimated `users=0` suggests initial administrator still needed but did not prove current exact user count.

**Working diagnosis:** Login view renders, but configuration API may be inaccessible through local Angular proxy `/gomoneypb.**`, or browser `is_demo` flag could force login. Neither cause verified yet. No direct database user insertion or manual Angular source edits recommended.

**Next diagnostic on INFINITY:** POST JSON `{}` to `http://127.0.0.1:52055/gomoneypb.configuration.v1.ConfigurationService/GetConfiguration` and the corresponding `http://127.0.0.1:4200/...` proxy route. Compare HTTP code and response body (especially `shouldCreateAdmin`), then check local browser demo flag if backend/proxy agree. Do not disclose JWTs/passwords. Preserve actual results.

**Status:** Frontend rendering confirmed; registration/authentication blocked; diagnostic pending.

## 2026-11-24 — Go Money registration failure isolated to Angular proxy 404

**Source:** User-pasted INFINITY Windows PowerShell 5.1 POST test with JSON body `{}`, using configuration RPC `/gomoneypb.configuration.v1.ConfigurationService/GetConfiguration`.

**Verbatim evidence:**
```text
=== TEST: http://127.0.0.1:52055/gomoneypb.configuration.v1.ConfigurationService/GetConfiguration ===
HTTP: 200
Response: {"shouldCreateAdmin":true,"baseCurrency":"USD","backendVersion":"1.8.0","commitSha":"e423145"}

=== TEST: http://127.0.0.1:4200/gomoneypb.configuration.v1.ConfigurationService/GetConfiguration ===
ERROR: The remote server returned an error: (404) Not Found.
HTTP: 404
```

**Confirmed:** Native Go Money v1.8.0 backend on localhost:52055 correctly reports that no initial administrator exists (`shouldCreateAdmin=true`). Angular's port-4200 proxy is not forwarding the request (HTTP 404). Therefore the UI remained on sign-in because the initial `getConfiguration` call could not return the registration flag, not because a registration route is missing or the user is already registered. No database or backend change required.

**Probable cause:** Earlier Angular dev proxy key `^/gomoneypb\\.` was regex-like but unsupported as a match expression in this Vite Angular proxy context; the replacement key should match the ConnectRPC service/method path via glob `/gomoneypb.*/**`. Need validate by restarting Angular dev server then comparing identical POST request to 4200 and 52055. Ensure UTF-8 no BOM on PowerShell 5.1.

**Remediation (proposed, not yet confirmed):** Replace `H:\DERPBooks\go-money\frontend\proxy.conf.json` with JSON mapping `"/gomoneypb.*/**"` to `http://127.0.0.1:52055`; use UTF8Encoding(false), restart Angular, repeat API POST. Once HTTP 200 `shouldCreateAdmin=true` appears through port 4200, reload login and use native Register flow on same page. No need to invent /register.

**Status:** Root fault narrowed to Angular proxy; fix pending.

## 2026-11-24 — Go Money frontend access confirmed by operator

**Operator statement (verbatim):** “we in”

**Context:** Earlier Angular frontend on INFINITY showed sign-in only because `POST /gomoneypb.configuration.v1.ConfigurationService/GetConfiguration` returned 404 through port 4200 while backend on 52055 returned HTTP 200 `{"shouldCreateAdmin":true,"baseCurrency":"USD","backendVersion":"1.8.0","commitSha":"e423145"}`. A corrected Angular dev proxy pattern `/gomoneypb.*/**` was supplied, followed by operator's successful-access report.

**Reconciled state:** Operator reports that the Go Money v1.8.0 native UI is now accessible and they are **in**. Treat as user-confirmed successful entry rather than independent account/API audit; credentials and screenshots were not supplied. App stack: INFINITY Windows backend (previously observed `go-money-server.exe` PID 26104, listeners 52055/52056, HTTP /health and /ready 200) using THOTH PostgreSQL `money`; Angular source and dependencies at `H:\DERPBooks\go-money\frontend` served on localhost:4200. Backend binary still at `E:\dls` as last observed. MCP disabled for missing docs. Git checkout pinned tag v1.8.0 commit `e423145`.

**Next priorities:** Establish stable H:-based deployment/launcher and frontend/API proxy beyond development shell; then configure existing THOTH Grafana with restricted read-only finance datasource and dashboards; add automated PDF ingestion for LCC payroll and Huntington statements. Do not require manual transaction transcription. No financial transaction imports yet verified; protect source PDFs and credentials outside public repository.

**Status:** UI access OPERATOR-CONFIRMED. Persistence, financial dashboards and ETL pending.

## 2026-11-24 — Go Money dashboard screenshot exposes missing Grafana URL

**User evidence:** Screenshot of the real Angular Go Money v1.8.0 UI on INFINITY after successful registration/access. Left navigation includes Dashboard, Deposits, Expenses, Transfers, All; page displays a Grafana integration warning and a "Navigate to grafana" action.

**Exact UI warning:** `Grafana url is not set. Please set it using env variable - GRAFANA_CONFIG_URL. For more details refer to official documentation.`

**Confirmed:** Authenticated frontend/dashboard renders, beyond merely showing login. Go Money's financial dashboard relies on external Grafana integration. The source config `pkg/configuration/types.go` defines `GrafanaConfig.Url` under prefix `GRAFANA_CONFIG_`, matching environment variable `GRAFANA_CONFIG_URL`. This setting hasn't yet been applied to the running INFINITY backend. Grafana already exists on THOTH but its exact current user-facing browser URL/port and its Go Money datasource privileges are unverified.

**Next:** Determine working THOTH Grafana URL on LAN, then supply `GRAFANA_CONFIG_URL` when launching Go Money backend on INFINITY. Restarting backend will interrupt the current foreground session and require existing DB/MCP variables; avoid changing until launch environment is preserved. Independently provision a read-only PostgreSQL reporting role/datasource and deploy initial Grafana finance dashboards; URL configuration alone doesn't produce reports.

**State:** Frontend authenticated and functioning; Grafana integration banner visible; reporting not configured.

## 2026-11-24 — THOTH Grafana 13.2.3 health verified from INFINITY

**Source:** User-pasted INFINITY PowerShell 5.1 `Invoke-RestMethod -Uri http://192.168.5.83:3000/api/health` result.

**Verbatim output:**
```text
database : ok
version  : 13.2.3
commit   : 90ffed056f0884267356c12a0eeb72a022af53f1
```

**Confirmed:** THOTH's existing Grafana HTTP API is reachable from INFINITY at `http://192.168.5.83:3000`, with Grafana v13.2.3 reporting its own database status `ok`. This is Grafana's *internal health database status*, **not** evidence of a configured `money` PostgreSQL datasource or finance dashboard. Earlier pasted failed registration API proxy test (52055 HTTP 200 / 4200 HTTP 404) is historical; the user previously confirmed UI access after proxy repair.

**Next:** When Go Money backend is deliberately restarted, add `GRAFANA_CONFIG_URL=http://192.168.5.83:3000` alongside already working DB settings and `MCP_DISABLE=true` to remove warning from native frontend. Separately configure a least-privilege read-only Grafana PostgreSQL role and datasource to `money` on THOTH. Preserve finances and credentials outside public repo. Current Go Money backend is a foreground process; changing environment in a different PowerShell session will not affect it until restart.

**Status:** Grafana reachability VERIFIED; Go Money UI URL integration and financial datasource NOT YET CONFIGURED.

## 2026-11-24 — Go Money Navigate to Grafana link confirmed functional

**User observation:** “navigate to grafana works just fine. im t th edsh board landing page”

**Confirmed:** From Go Money's authenticated frontend on INFINITY, the `Navigate to grafana` control successfully opens the preexisting THOTH Grafana landing page. Prior PowerShell health endpoint response confirmed Grafana v13.2.3 at `http://192.168.5.83:3000`. The Go Money backend's `GRAFANA_CONFIG_URL` is evidently set to a usable destination, but the exact successful backend restart output was not pasted; distinguish observed navigation success from uninspected process environment.

**Still outstanding:** Grafana financial PostgreSQL datasource, dashboard(s) and transaction ETL. Go Money's link working does not imply Grafana can query the `money` database. We have zero verified imported financial transactions. Next action: create a dedicated least-privilege read-only `money_report` PostgreSQL role on THOTH (SELECT only reporting-safe finance tables/views, not users, JWT/system configuration or tokens), configure PostgreSQL datasource in existing Grafana, use dashboard/API read tests.

**Status:** Navigation verified; finance visualization data connection not yet verified.

## 2026-11-24 — Grafana money_report role privilege audit passes

**User evidence:** THOTH terminal output from SQL privilege audit after the proposed role/password creation and grants.

**Verbatim result:**
```text
=== VERIFY PRIVILEGES ===
      table_name       | can_read
-----------------------+----------
 accounts              | t
 categories            | t
 daily_stat            | t
 double_entries        | t
 service_tokens        | f
 system_configurations | f
 tags                  | t
 transactions          | t
 users                 | f
(9 rows)

=== COMPLETE ===
```

**Confirmed:** PostgreSQL role `money_report` has SELECT privileges on six targeted financial tables and no SELECT privilege on `users`, `service_tokens`, or `system_configurations`. Successful script output supports initial reporting-role creation, but no independent password authentication test or actual Grafana datasource Save & test has yet been shown.

**User reaction (verbatim):** “There was suprinsgly more to this than I expected.”

**Next:** Connect existing THOTH Grafana 13.2.3 at `http://192.168.5.83:3000` to the local THOTH PostgreSQL `money` database using host `127.0.0.1:5432`, role `money_report`, and private credential from `/home/thoth/derpbooks/money-grafana-password`; initial SSL mode can match loopback-only database access. Grafana should not use PostgreSQL owner `money` or PostgreSQL superuser. If datasource Save & test fails, validate `money_report` TCP password login from THOTH first. Initial financial reporting contains no verified actual transactions.

**Status:** Table grants verified; Grafana datasource and dashboards not yet created or tested.

## 2026-11-24 — DERPBooks Grafana headless provisioning script prepared

**User request (verbatim):** “good idea using this rather than making our own attempt, this is pretty mature. I don't want to mess iwth grafana GUI thi smorning, write a script. There is an official dashboard”

**Upstream investigation:** In ft-t/go-money tag `v1.8.0` (`e423145`), verified `compose/grafana/provisioning/datasources/datasources.yaml` and reporting SQL examples exist, but Git tree did not contain a bundled dashboard JSON in `docs/reporting/dashboards`. The project's Grafana wiki describes using Grafana and provides queries; its live demonstration is `https://gomoney-grafana.ft-t.dev`. **Do not claim an upstream official JSON dashboard was imported.** Its location/export remains unresolved. Official Grafana documentation supports file provisioning for datasources and dashboards and `$__file{}` secret expansion.

**Script prepared in current conversation:** `provision-derpbooks-grafana.sh`; SHA-256 `3ade12525ac75d07550846a2a95fa3f6e0e222f8d7c60fbdd45024ba16d147cc`. This file was authored as a downloadable conversation artifact, **not yet executed on THOTH and not claimed committed to this Git repository**. It is intended to run under `sudo bash` on THOTH. It verifies the `money_report` TCP credential and SELECT grant; backs up any existing DERPBooks-specific provisioning files; copies reporting password from `/home/thoth/derpbooks/money-grafana-password` to a protected Grafana-readable file; creates datasource UID `derpbooks_pg` for local `money` PostgreSQL; creates a separate dashboard provisioning provider and a **custom starter** overview dashboard UID `derpbooks-overview`, showing counts and transaction activity rather than pretending to be upstream official dashboard. It restarts **only Grafana** to load the datasource; no other dashboard provisioning is intentionally changed. Link target when deployed: `http://192.168.5.83:3000/d/derpbooks-overview`.

**Source status:** v1.8.0 official demo and reporting examples confirmed; official importable dashboard not located. GitHub provenance checkpoint must distinguish script preparation from deployment success.

**Next evidence:** User execution output (including datasource provisioning logs and dashboard rendering); if errors, inspect Grafana journal and roll back using timestamped backup. Later import upstream dashboard if its exact verified JSON file or ID is identified. No actual financial records imported yet.

**Status:** Headless setup **prepared**, not deployed.
