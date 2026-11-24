# THOTH — provisioned Grafana dashboard cleanup

**Date:** 2026-11-24 (America/Detroit). **Context:** A maintenance digression during the portfolio's reconstruction of the weather-app → Grafana history.

## Problem
Grafana's UI would not allow deletion of five redundant **provisioned** dashboards. Three user-selected dashboards had to be preserved. The user also wanted to reduce unnecessary resource usage.

## Solution
Identified dashboard JSON by its title and UID, explicitly verified five remove-candidates and three keepers, quarantined the five JSON definitions from `/var/lib/grafana/dashboards`, and inspected the active provider configuration.

- **Quarantine:** `/home/thoth/grafana-cleanup-20261124/removed/`
- **Remove:** Nest HVAC History (`thoth-nest-hvac`), History v2 (`thoth-nest-hvac-v2`), Rich (`thoth-nest-hvac-rich`), Unified (`thoth-nest-hvac-unified`), Power Today — Corrected (`thoth-power-today-corrected`).
- **Keep:** Mosquitto Broker (`thoth-mosquitto-broker`), Nest HVAC Runtime Lab (`thoth-nest-hvac-runtime-lab`), Power Spectrum — Drilldown v4 (`thoth-power-drilldown-v4`).
- **Provider:** `/etc/grafana/provisioning/dashboards/thoth.yaml` uses `disableDeletion: false`, a 10-second refresh, and the active dashboard directory.
- **Verification:** Terminal output confirms five quarantined filenames, three preserved filenames, nine remaining JSON files and `grafana-server` service state `active`. Journal excerpt did not explicitly report deletion events; the user confirmed “we are good to go.”
- **Observed effect:** User subsequently reported “this freed up a little bit of ram in the container lol.” This is a qualitative user observation; no byte counts or controlled baseline were supplied. No measured reduction or causal attribution is claimed.
- **Backup caveat:** The original script copied the files to `BACKUP/removed` and then moved originals to the *same target paths*; this did not produce two independent copies. The quarantined source files remain available for restoration.

## Original scripts and terminal output

The following is the **user-supplied pasted terminal session**, preserved as evidence, including command inputs and their outputs. Shell prompts and pasted source are retained; this is not a freshly runnable consolidated script.

```text
thoth@thoth:~$
thoth@thoth:~$ echo "=== GRAFANA DASHBOARD CLEANUP INVENTORY ==="

sudo python3 - <<'PY'
import json
from pathlib import Path

remove = {
    "THOTH — Nest HVAC History",
    "THOTH — Nest HVAC History v2",
    "THOTH — Nest HVAC Rich",
    "THOTH — Nest HVAC Unified",
    "THOTH — Power Today — Corrected",
}

keep = {
    "THOTH — Mosquitto Broker",
    "THOTH — Nest HVAC Runtime Lab",
    "THOTH — Power Spectrum — Drilldown v4",
}

roots = [
    Path("/etc/grafana/provisioning"),
    Path("/var/lib/grafana/dashboards"),
    Path("/opt"),
]

for root in roots:
    if not root.exists():
        continue

    for path in root.rglob("*.json"):
        try:
            data = json.loads(path.read_text())
        except (OSError, ValueError):
            continue

        if not isinstance(data, dict):
            continue

        dashboard = data.get("dashboard", data)
        if not isinstance(dashboard, dict):
            continue

        title = dashboard.get("title", "")

        if title in remove:
            print(f"REMOVE CANDIDATE: {title}")
            print(f"  UID:  {dashboard.get('uid')}")
            print(f"  FILE: {path}")

        if title in keep:
            print(f"KEEP: {title}")
            print(f"  UID:  {dashboard.get('uid')}")
            print(f"  FILE: {path}")

print("\n=== INVENTORY COMPLETE ===")
PY
=== GRAFANA DASHBOARD CLEANUP INVENTORY ===
REMOVE CANDIDATE: THOTH — Power Today — Corrected
  UID:  thoth-power-today-corrected
  FILE: /var/lib/grafana/dashboards/thoth-power-today-corrected.json
REMOVE CANDIDATE: THOTH — Nest HVAC History v2
  UID:  thoth-nest-hvac-v2
  FILE: /var/lib/grafana/dashboards/thoth-nest-hvac-v2.json
REMOVE CANDIDATE: THOTH — Nest HVAC Unified
  UID:  thoth-nest-hvac-unified
  FILE: /var/lib/grafana/dashboards/thoth-nest-hvac-unified.json
KEEP: THOTH — Power Spectrum — Drilldown v4
  UID:  thoth-power-drilldown-v4
  FILE: /var/lib/grafana/dashboards/thoth-power-drilldown-v4.json
REMOVE CANDIDATE: THOTH — Nest HVAC Rich
  UID:  thoth-nest-hvac-rich
  FILE: /var/lib/grafana/dashboards/thoth-nest-hvac-rich.json
KEEP: THOTH — Nest HVAC Runtime Lab
  UID:  thoth-nest-hvac-runtime-lab
  FILE: /var/lib/grafana/dashboards/thoth-nest-hvac-runtime-lab.json
KEEP: THOTH — Mosquitto Broker
  UID:  thoth-mosquitto-broker
  FILE: /var/lib/grafana/dashboards/thoth-mosquitto-broker.json
REMOVE CANDIDATE: THOTH — Nest HVAC History
  UID:  thoth-nest-hvac
  FILE: /var/lib/grafana/dashboards/thoth-nest-hvac-history.json

=== INVENTORY COMPLETE ===
thoth@thoth:~$
thoth@thoth:~$ (
    set -e

    SOURCE="/var/lib/grafana/dashboards"
    BACKUP="/home/thoth/grafana-cleanup-20261124"

    REMOVE=(
        "thoth-nest-hvac-history.json"
        "thoth-nest-hvac-v2.json"
        "thoth-nest-hvac-rich.json"
        "thoth-nest-hvac-unified.json"
        "thoth-power-today-corrected.json"
    )

    KEEP=(
        "thoth-mosquitto-broker.json"
        "thoth-nest-hvac-runtime-lab.json"
        "thoth-power-drilldown-v4.json"
    )

    echo "=== VERIFY ALL FILES ==="

    for file in "${REMOVE[@]}" "${KEEP[@]}"; do
        sudo test -f "$SOURCE/$file"
        echo "FOUND: $file"
    done

    echo
    echo "=== CREATE BACKUP ==="

    mkdir -p "$BACKUP/removed"

    for file in "${REMOVE[@]}"; do
        sudo cp -p \
            "$SOURCE/$file" \
            "$BACKUP/removed/$file"
    done

    echo
    echo "=== QUARANTINE REDUNDANT DASHBOARDS ==="

    for file in "${REMOVE[@]}"; do
        sudo mv \
            "$SOURCE/$file" \
            "$BACKUP/removed/$file"
        echo "QUARANTINED: $file"
    done

    echo
    echo "=== VERIFY KEEPERS ==="

    for file in "${KEEP[@]}"; do
        sudo test -f "$SOURCE/$file"
        echo "PRESERVED: $file"
    done

    echo
    echo "=== PROVISIONING CONFIG ==="

    sudo grep -RInE \
        'disableDeletion|updateIntervalSeconds|path:|name:' \
        /etc/grafana/provisioning/dashboards \
        2>/dev/null || true

    echo
    echo "=== COMPLETE ==="
)
=== VERIFY ALL FILES ===
FOUND: thoth-nest-hvac-history.json
FOUND: thoth-nest-hvac-v2.json
FOUND: thoth-nest-hvac-rich.json
FOUND: thoth-nest-hvac-unified.json
FOUND: thoth-power-today-corrected.json
FOUND: thoth-mosquitto-broker.json
FOUND: thoth-nest-hvac-runtime-lab.json
FOUND: thoth-power-drilldown-v4.json

=== CREATE BACKUP ===

=== QUARANTINE REDUNDANT DASHBOARDS ===
QUARANTINED: thoth-nest-hvac-history.json
QUARANTINED: thoth-nest-hvac-v2.json
QUARANTINED: thoth-nest-hvac-rich.json
QUARANTINED: thoth-nest-hvac-unified.json
QUARANTINED: thoth-power-today-corrected.json

=== VERIFY KEEPERS ===
PRESERVED: thoth-mosquitto-broker.json
PRESERVED: thoth-nest-hvac-runtime-lab.json
PRESERVED: thoth-power-drilldown-v4.json

=== PROVISIONING CONFIG ===
/etc/grafana/provisioning/dashboards/thoth-nest-history.yaml.backup-20261013-104624:4:  - name: THOTH Nest
/etc/grafana/provisioning/dashboards/thoth-nest-history.yaml.backup-20261013-104624:8:    disableDeletion: false
/etc/grafana/provisioning/dashboards/thoth-nest-history.yaml.backup-20261013-104624:10:    updateIntervalSeconds: 30
/etc/grafana/provisioning/dashboards/thoth-nest-history.yaml.backup-20261013-104624:12:      path: /var/lib/grafana/dashboards
/etc/grafana/provisioning/dashboards/thoth.yaml:4:  - name: THOTH
/etc/grafana/provisioning/dashboards/thoth.yaml:8:    disableDeletion: false
/etc/grafana/provisioning/dashboards/thoth.yaml:9:    updateIntervalSeconds: 10
/etc/grafana/provisioning/dashboards/thoth.yaml:12:      path: /var/lib/grafana/dashboards
/etc/grafana/provisioning/dashboards/samsung-grafpollo.yaml:4:  - name: Samsung Grafpollo
/etc/grafana/provisioning/dashboards/samsung-grafpollo.yaml:8:    disableDeletion: false
/etc/grafana/provisioning/dashboards/samsung-grafpollo.yaml:10:    updateIntervalSeconds: 30
/etc/grafana/provisioning/dashboards/samsung-grafpollo.yaml:12:      path: /var/lib/grafana-grafpollo/dashboards

=== COMPLETE ===
thoth@thoth:~$ echo "=== GRAFANA PROVISIONING EVENTS ==="

sudo journalctl -u grafana-server \
    --since "10 minutes ago" \
    --no-pager |
    grep -Ei 'provision|dashboard|delet|error|failed' |
    tail -60

echo
echo "=== REMAINING DASHBOARD SOURCE FILES ==="

sudo find /var/lib/grafana/dashboards \
    -maxdepth 1 \
    -type f \
    -name '*.json' \
    -printf '%f\n' |
    sort

echo
echo "=== GRAFANA STATUS ==="

systemctl is-active grafana-server
=== GRAFANA PROVISIONING EVENTS ===
Nov 24 02:52:05 thoth grafana[1628]: logger=bleve-backend namespace=default group=dashboard.grafana.app resource=librarypanels reason=getStats t=2026-11-24T02:52:05.910531059-05:00 level=info msg="Building index using memory"
Nov 24 02:52:05 thoth grafana[1628]: logger=bleve-backend namespace=default group=dashboard.grafana.app resource=librarypanels reason=getStats t=2026-11-24T02:52:05.913595179-05:00 level=info msg="Finished building index" elapsed=1.807371ms listRV=1
Nov 24 02:52:05 thoth grafana[1628]: logger=bleve-backend namespace=default group=dashboard.grafana.app resource=librarypanels reason=getStats t=2026-11-24T02:52:05.9141162-05:00 level=info msg="Storing index in cache" key="{Namespace:default Group:dashboard.grafana.app Resource:librarypanels}" expiration=2026-11-24T03:02:05.9141121-05:00
Nov 24 02:53:23 thoth grafana[1628]: logger=live t=2026-11-24T02:53:23.273574533-05:00 level=info msg="Initialized channel handler" channel=grafana/dashboard/uid/thoth-horus-host address=grafana/dashboard/uid/thoth-horus-host
Nov 24 02:54:32 thoth grafana[1628]: logger=plugins.update.checker t=2026-11-24T02:54:32.183620792-05:00 level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
Nov 24 02:54:32 thoth grafana[1628]: logger=plugins.update.checker t=2026-11-24T02:54:32.183837-05:00 level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
Nov 24 02:54:32 thoth grafana[1628]: logger=plugins.update.checker t=2026-11-24T02:54:32.183959705-05:00 level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
Nov 24 02:57:34 thoth grafana[1628]: logger=plugins.update.checker t=2026-11-24T02:57:34.661085311-05:00 level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
Nov 24 02:57:34 thoth grafana[1628]: logger=plugins.update.checker t=2026-11-24T02:57:34.701174783-05:00 level=info msg="flag evaluation succeeded" flag="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}" details="{Value:false EvaluationDetails:{FlagKey:pluginsAutoUpdate FlagType:bool ResolutionDetail:{Variant:default Reason:STATIC ErrorCode: ErrorMessage: FlagMetadata:map[]}}}"
Nov 24 02:57:34 thoth grafana[1628]: logger=middleware.gzip t=2026-11-24T02:57:34.718779273-05:00 level=warn msg="Failed to write gzipped response" path=/public/fonts/inter/Inter-Regular.woff2 error="http: request method or response status code does not allow body"
Nov 24 02:57:34 thoth grafana[1628]: logger=middleware.gzip t=2026-11-24T02:57:34.976427178-05:00 level=warn msg="Failed to write gzipped response" path=/public/fonts/inter/Inter-Medium.woff2 error="http: request method or response status code does not allow body"

=== REMAINING DASHBOARD SOURCE FILES ===
thoth-charon-cpai.json
thoth-exporter-services.json
thoth-frigate-operations.json
thoth-horus-host.json
thoth-mosquitto-broker.json
thoth-nest-hvac-runtime-lab.json
thoth-power-drilldown-v4.json
thoth-systems.json
thoth-weather.json

=== GRAFANA STATUS ===
active
thoth@thoth:~$
```

## Provenance and next action
**Classification:** Confirmed local-file operation and running Grafana service; user-reported UI success and qualitative memory benefit; precise Grafana database state and RAM delta not independently measured. No source dashboards were altered.

**Return to main task:** reconstruct weather app → concentrated Grafana development week → Nest/power chronology from archived conversation evidence.
