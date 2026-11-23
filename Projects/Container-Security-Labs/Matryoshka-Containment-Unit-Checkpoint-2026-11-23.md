# Matryoshka Containment Unit — Checkpoint

**Status:** Paused after read-only reconnaissance; level1 identified, further layers unknown  
**Recorded:** 2026-11-23 (America/Detroit)  
**Source:** User-pasted TryHackMe lab introduction, terminal outputs, and conversational corrections. Outputs are attributed to the user’s lab terminal rather than independently reproduced.  
**Purpose:** Resume checkpoint and DERP evidence preservation, not a completed escape claim.

## Lab introduction

> Matryoshka Containment Unit  
> You set up a containment unit designed to trap and contain even the most nefarious viruses, but you accidentally got trapped in it while testing it.  
> Your memory is fuzzy, and you don't remember much about how you set it up.  
> Good luck!

The title prompted a nesting-doll analogy; whether there are multiple nested Docker daemons/containers remains **unverified**. The user suggested a more entertaining *Inception* countdown timer per layer as a design joke, not an implemented feature.

## Target and initial observed environment

SSH target for the resumed lab: `matryoshka@10.64.178.175` (ephemeral lab address; do not presume future persistence).

Observed prompt: `0314815ce7da:~$`.

| Property | User-observed value | Classification |
| --- | --- | --- |
| Identity | `uid=1000(matryoshka) gid=1000(matryoshka) groups=1000(matryoshka)` | Observed |
| Hostname | `0314815ce7da` | Observed |
| Kernel | `6.17.0-1013-aws` | Observed |
| PID 1 | `sleep infinity` | Observed |
| Container marker | `/.dockerenv` present | Observed |
| Cgroup | `0::/`; cgroup2 mounted | Observed |
| CapEff / CapPrm | `0000000000000000` | Observed |
| CapBnd | `00000000a80425fb` | Observed |
| User namespace | `user:[4026531837]` | Observed |
| UID/GID mappings | `0 0 4294967295` for both | Observed |
| Root filesystem reported by `/proc/mounts` | `/dev/root / ext4` | Observed |
| Installed utilities | Docker, `unshare`, `nsenter`; `findmnt` missing | Observed |

## Docker socket and daemon

Socket exists at `/run/docker.sock` and is `srw-rw-rw-` (mode 0666), owned by root and GID 2375. `/var/run` links to `/run`.

Docker client version: `26.1.5`. Default Docker context endpoint: `unix:///var/run/docker.sock`.

Daemon information returned successfully from the unprivileged shell:

- Name: `d275346ac26e`
- Server version: `25.0.5`
- Docker root directory: `/var/lib/docker`
- Storage driver: `vfs`
- Reported security options: `apparmor`, `seccomp,profile=builtin`, `cgroupns`

This **confirms usable Docker API access from an unprivileged container account**, but does not by itself prove outer-host control or a completed escape.

## Context correction: accidental SSH disconnect

An earlier SSH session to `10.64.148.193` closed, returning to prompt `root@ip-10-64-80-225:~#`. Docker inventory there included `revshellgenerator` and `cyberchef`; **those entries belong to the outer AttackBox context and are not Matryoshka level1 evidence**. The user then reconnected to `matryoshka@10.64.178.175`, restoring prompt `0314815ce7da:~$`.

Preserve the distinction between the two execution contexts when resuming.

## Verified inventory after reconnecting to Matryoshka

```text
CONTAINER ID   NAMES     IMAGE                     STATUS
0314815ce7da   level1    matryoshka-level1:local   Up 7 minutes
```

Available images: `matryoshka-level1:local` (`485e908211ec`) and `alpine:3.20` (`bf8527eb54c3`). Networks: `bridge`, `host`, `none`. No volumes listed.

### `docker inspect level1` observations

```text
Name: /level1
Image: matryoshka-level1:local
User: matryoshka
Privileged: false
PID Mode:
Network Mode: none
Readonly Rootfs: false

Mounts:
[{"Type":"bind","Source":"/var/run/docker.sock","Destination":"/var/run/docker.sock","Mode":"","RW":true,"Propagation":"rprivate"}]

Capabilities Added: null
Security Options: null
```

**Core finding:** The nonprivileged `level1` container with no Docker network has a writable bind mount of the managing Docker socket. This is a significant isolation weakness; available daemon operations and containment depth need separate verification. `CapAdd: null` describes no explicitly added capabilities, not the entire effective-capability state (which was observed separately as zero).

Mount anomaly noted: `/proc/mounts` displayed an overlay mount at `/run/docker.sock`, whereas `docker inspect` describes a bind mount at `/var/run/docker.sock`. The two paths resolve together through the symlink, but the underlying layered mount arrangement was not investigated further.

## Checkpoint and next action

- **Confirmed:** Level 1 is `0314815ce7da`, image `matryoshka-level1:local`, Docker name `level1`; daemon reachable; RW socket bind mount.
- **Not confirmed:** Number of nested layers, daemon's relationship to the outer host, any privilege escalation or escape, any flag, challenge completion.
- **Environment:** Lab user `matryoshka`; terminal prompt `0314815ce7da:~$`. Confirm prompt and session after any disconnect before interpreting new output.
- **Next:** Resume with read-only analysis of level boundaries and lab objectives, explicitly tracking execution context. Avoid treating the AttackBox's unrelated Docker inventory as target evidence.
- **Workflow:** GitHub is the canonical versioned record. Obsidian local pull/sync not verified at checkpoint.

No target files, containers, networks, or Docker daemon settings were changed during the documented checks.
