# DERP — Git Health and Knowledge-System Observability

- **Recorded:** 2026-11-22 (America/Detroit)
- **Status:** Proposed research/design; no deployed dashboard or Node-RED monitor asserted
- **Parent:** [Delegated Etheral Remote Protocol](./README.md)
- **Related:** [Architecture brainstorm](./Architecture-Brainstorm.md)

## Conversation-driven research trajectory

This working session developed incrementally:
1. Mobile ChatGPT voice and brainstorm capture, preserving original wording separately from polished project notes.
2. Direct ChatGPT ↔ GitHub repository read/write, without relying on an always-on worker for every note.
3. Optional THOTH Node-RED commit watcher, context handoff builder and conflict-aware Obsidian synchronization.
4. Shared, generated handoff manifests for later ChatGPT and Gemini sessions, with source/commit references.
5. Node-RED health monitoring of Git remote/local synchronization, context age, failed pushes, and reconciliation.
6. **New idea:** Grafana dashboard integrating GitHub repository activity and custom local sync/context-health metrics.

These are design evolutions, not blanket claims of completed implementations.

## Dashboard concept — DERP | Repository & Context Health

Two distinct data sources:

### GitHub data source

Grafana GitHub data source plugin:
https://grafana.com/grafana/plugins/grafana-github-datasource/

Investigate repository commit activity, pull-request history, and commit annotations. Verify plugin compatibility with the installed Grafana edition/version and API authentication/permissions before deployment.

### THOTH Node-RED → Prometheus / Grafana

Proposed locally observed metrics:
- GitHub API reachability and response latency
- Latest remote commit SHA
- Last processed commit SHA
- Local Obsidian Git HEAD SHA
- Local dirty working-tree indicator
- Number of commits ahead/behind (divergence)
- Last successful pull/push time
- Local-to-remote synchronization lag
- Last successful model-context snapshot generation
- Context snapshot age
- Sync attempts, conflicts and failures

SHA labels should avoid unbounded Prometheus series cardinality; prefer text/status annotation or logs for detailed identifiers, and numeric gauges/counters for metrics.

## Suggested dashboard sections

1. Repository access and last observed commit
2. GitHub commit/PR activity
3. Local Obsidian vault divergence and sync status
4. GPT/Gemini context freshness (only after those paths exist)
5. Node-RED reconciliation job results and error history
6. Commit annotations over operational telemetry, when grounded

## Operational model

Begin in **read-only observation mode**: inspect latest remote commit and local state, export telemetry, do not auto-resolve divergence or modify the vault.

Then test idempotent commit processing, retries, stale-token handling, missing-remote behavior, and conflicting local edits before enabling any pulls/pushes.

An up-to-date GitHub remote is not proof that local Obsidian has pulled, nor proof that an AI client has refreshed its context. Those must have separate states.

## Backlog status

- 10-minute autosave: explicitly deferred
- cron/systemd migration to Node-RED: exploratory, not implemented
- Git health dashboard: proposed, not deployed
- Node-RED Git watcher: proposed, not deployed

## Open verification

- Inspect current Grafana version and GitHub plugin support
- Confirm THOTH metrics exposure method and Prometheus scrape configuration
- Inventory local vault path, Git state and synchronization method
- Test an end-to-end remote commit → local observation → context freshness metric
