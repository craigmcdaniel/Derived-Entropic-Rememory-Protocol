# Dios de Ignatio de Portfellatio

**Public-facing title:** Technical Portfolio  
**Parent:** [DERP — Derived-Entropic-Rememory-Protocol](../../README.md)  
**State:** Initiated 2026-11-24; portfolio case studies and live demonstrations not yet published.

This project documents **the making of a technical portfolio**, not just its finished output. It uses the DERP provenance method to distinguish an idea from an implementation and an implementation from a verified demonstration.

## Purpose

Build an interview-ready portfolio that tells truthful, concise technical stories from development, infrastructure, security, automation, observability and incident response. The target audience may be technical or nontechnical. A demonstration may use a tablet and private network access; **public readers must not need lab access**.

The nickname is internal lore; the professional presentation name is **Technical Portfolio**.

## Scope and data boundaries

- **This public folder:** Sanitized construction journal, decisions, methods, progress and publishable case studies.
- **Bluebayou (private GitHub repository):** Interview drills, answers, feedback and personal preparation. Do not mirror it here.
- **DERP Distributed Event Reconciliation (private):** Implementation notes and raw operational evidence. Link only to shareable/redacted derivatives.
- **Home lab / private vault:** Raw logs, screenshots, addresses and infrastructure details remain private unless individually reviewed for release.

No automatic recording or background Git synchronization is implied. Entries are appended through deliberate collaboration and commits.

## Proposed portfolio tracks

1. **Observability and operations:** Grafana, Prometheus, Loki, Alloy, service recovery, data interpretation.
2. **Security engineering:** Detection, risk reduction, identity, network segmentation and security investigations.
3. **Infrastructure engineering:** Windows, Linux, virtualization, networking and service architecture.
4. **Development and automation:** PowerShell, Python, code modernization and reproducible workflows.

These are **candidate sections**, not claims that a portfolio piece has been built.

## Evidence and publication rule

Each case study should record: problem; system boundary; evidence and timestamp; approach; actual implementation; validation; outcome; corrections; and what remains uncertain.

Status terms:

- **Confirmed:** Independently observed in supplied outputs, files, committed code or reproducible demonstration.
- **Historical:** Verified for a particular previous point in time; current state may differ.
- **Proposed:** Discussed but not implemented or tested.
- **Unknown:** Evidence does not establish the outcome.

Publish sanitized diagrams and screenshots only after reviewing for credentials, internal hostnames and other infrastructure details. Avoid implying the portfolio was endorsed by an employer.

## Contents

- [Build journal](./journal/2026-11-24-inception.md) — first chronological project entry
- [Recording protocol](./docs/RECORDING-PROTOCOL.md) — how decisions, interactions and evidence become entries
- [Case-study template](./templates/CASE-STUDY.md) — repeatable portfolio writing format

## Next milestone

Select the first case study from existing *verified* work, establish the evidence chain and build a short, readable demonstration. The initial candidate is monitoring and incident recovery using Grafana/Prometheus evidence.
