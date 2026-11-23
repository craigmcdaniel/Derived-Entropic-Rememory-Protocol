# Container Security Lab — Host Namespace Access and Container Identification

**Status:** Task source captured / execution not verified  
**Recorded:** 2026-11-23 (America/Detroit)  
**Source:** User-supplied training-lab excerpt in conversation, beginning “The Exploit,” plus the user's subsequent comment. This is a **workflow verification case** for ChatGPT → GitHub → Obsidian; not an assertion that the lab was completed.

## Source task: namespace access

The supplied exercise introduces `nsenter` as a way to enter namespaces associated with a target process. It provides the following command as its lab example:

```text
nsenter --target 1 --mount --uts --ipc --net /bin/bash
```

The source describes these options as entering the target's mount, UTS, IPC and network namespaces. Its demonstration uses a hostname check to illustrate a change in execution environment. The lab states that the container can see the host's `/sbin/init` process and asks the student to inspect the resulting environment.

**Important source assumptions:** PID 1 refers to the host init process *in this lab configuration*, not universally; the task's claim of automatic “ultimate root” access is not established merely by entering those namespaces. Actual credentials and effective permissions depend on user namespaces and security configuration. A hostname change alone does not prove complete host-root privilege.

The full pasted lab text remains in the conversation record; this document preserves the task's technical details and interpretation, rather than asserting it was executed.

## User's answer to the next lab question

User's own words:

> “how do you know you'r ein a contianer, i say, virtual nic duh”

**Interpretation:** The user proposes a virtual network interface as an indicator that the environment is containerized.

**Reconciliation:** A veth interface, Docker bridge networking or related network namespace evidence can be useful clues, but **not conclusive proof** on their own. Virtual network interfaces also exist in VMs and ordinary Linux hosts, and containers may use host networking or other setups. A stronger determination combines several observations, such as process namespace relationships, cgroup paths, mount information, container-specific filesystem markers and runtime metadata, with the limitations of each. The exact intended answer from the training task has not been supplied.

## Work performed versus not performed

| Item | Status | Evidence |
| --- | --- | --- |
| Previous cgroup capabilities task inspection | Observed previously | See [container lab README](./README.md) |
| Namespace-escape task instructions | Captured | User's pasted excerpt |
| User's virtual-NIC hypothesis | Preserved verbatim | User's comment above |
| Namespace escape performed in this task | **Not verified** | No terminal output supplied for this task |
| Correct response accepted by learning platform | **Unknown** | No feedback supplied |
| Document pushed to GitHub | Verify commit receipt separately | This file |

## Documentation workflow test

1. Capture source and user's own words without retroactively rewriting them.
2. Keep the user's hypothesis separate from supplemental technical interpretation.
3. Store the document as a canonical GitHub commit, retaining the commit SHA as proof of persistence.
4. Pull in Obsidian and inspect whether headings, verbatim quote and links render correctly.
5. If the lab returns feedback, append that as a dated correction with evidence; do not replace the original hypothesis.

**Next checkpoint:** Confirm this note appears in Obsidian after the normal Git pull. No lab commands or configuration changes are required for this documentation test.
