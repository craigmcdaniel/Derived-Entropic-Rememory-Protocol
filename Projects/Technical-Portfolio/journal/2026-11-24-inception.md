# Portfolio build journal — inception

**Date:** 2026-11-24 (America/Detroit)  
**Provenance:** Current ChatGPT project-planning conversation; this is a concise record of decisions, **not** a verbatim transcript.

### 2026-11-24 — New project proposed

- **Context:** Interview preparation suggested the value of presenting actual lab engineering through Grafana and other verified monitoring tools on a tablet.
- **User direction:** Create another project, jokingly named “Dios de Ignatio De Portfellatio”, for the technical portfolio.
- **Decision:** Separate the portfolio from interview practice; curate evidence-backed case studies instead of copying complete lab or interview archives.
- **Status:** Proposed architecture; no completed portfolio demonstration established.

### 2026-11-24 — Put it under DERP provenance

- **User direction:** “make this project under the derp provenance as a sub. We can share it. Documentation of building the portfolio will go in th eportfollio for our pipeline here”
- **Decision:** Use the existing **public** Derived-Entropic-Rememory-Protocol repository under `Projects/Technical-Portfolio/`. Keep the separate private telemetry and Bluebayou repositories unchanged.
- **Evidence:** GitHub repository metadata confirmed that Derived-Entropic-Rememory-Protocol is public and already documents a Markdown-first provenance pipeline; it uses `Projects/` for subprojects.
- **Status:** Repo destination confirmed; initial scaffolding pending commit at time of this entry's drafting.

### 2026-11-24 — Begin recording interactions

- **User direction:** “so lets get into that mind set now. Start recording our interactions and stuff, I'll keep it clean and succinct.”
- **Decision:** Maintain a concise, chronological build journal for substantive portfolio decisions, demonstrations, corrections and outcomes. Preserve original intent and corrections without treating summaries as verbatim transcripts.
- **Boundary:** Record deliberately during active sessions via repository commits; no claim of always-on or background capture.
- **Action:** Add project README, protocol, template and this inception journal.
- **Status:** Documentation scaffold created when the corresponding Git commit succeeds.
- **Next:** Select first verified portfolio case study and gather public-safe evidence, potentially Grafana/Prometheus monitoring recovery.

### Initial evidence candidates (not yet published)

| Candidate | Current classification | Rationale |
| --- | --- | --- |
| Prometheus crash recovery and Grafana observability | Historical / confirmed recovery in prior session outputs | Demonstrates analysis, backups, TSDB/WAL diagnosis and verification; needs sanitized evidence |
| DERP telemetry and Kibana | Partial historical evidence, deployment states vary | Distinguish real ingestion from unverified dashboard proposals |
| Windows / Linux / virtualization integration | Candidate only | Select bounded, well-evidenced implementations |
| Application security and risk management | Skills demonstrated in interview hypotheticals, not deployment evidence | No claims of live institutional security findings |

### Publication checklist

- Source and timestamps accounted for
- Implementation separated from brainstorming
- Institutional and home-lab details reviewed for publication
- Outcome grounded in logs, code or demonstration
- Corrections preserved

### 2026-11-24 — CHARON origin story: retrospective Sprint 1

- **Evidence type:** First-person retrospective recollection, recorded on 2026-11-24. Original event dates **not yet established** from the archive.
- **User's wording:** “I remember most of it. Charon started out just with 16 gigs of ram and hosting blue iris with local inference. After upgrading it, one day while installing kali on it, in vmware, I was like, this sucks, I want server. I wonder if we can install server in a vhdx and make it portable like I thought I read, then we did it, and I posted in ethical hacking class about the vhdx and how it makes images portable as fuck. That was basically sprint 1 -4d”
- **Sequence as remembered:** (1) CHARON initially had 16 GB RAM and ran Blue Iris with local inference; (2) hardware was upgraded (specifications/date pending); (3) installing Kali in VMware prompted a desire to move to a server OS; (4) explored installing Windows Server into a portable VHDX; (5) completed a VHDX-based installation; (6) discussed the portability of VHDX images in ethical hacking class.
- **Interpretation:** User refers to this formative sequence as **Sprint 1**; suffix “-4d” preserved above, duration **not independently established**.
- **Status:** **Historical recollection, uncorroborated** until dates, original discussion, hardware changes, boot configuration and class post can be traced to source records. Do not assume this is the later INFINITY VHDX migration.
- **Portfolio relevance:** Motivating problem → architecture investigation → implementation → knowledge sharing. Potential first-person systems-engineering case study once the archive corroborates details.
- **Next:** Search original converted ChatGPT history for CHARON's early RAM/Blue Iris configuration, VMware Kali discussion, VHDX installation and class commentary. Attach source references and correct chronology without overwriting this recollection.
