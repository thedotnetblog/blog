---
title: "NTLM Is Ending in Git/libcurl: Azure DevOps Server Teams Need a Real Migration Plan"
date: 2026-07-20
author: Emiliano Montesdeoca
description: "The September 2026 NTLM removal is not a minor compatibility issue; it is an identity architecture deadline for on-prem Azure DevOps Server environments."
tags:
  - Azure DevOps Server
  - Git
  - Security
  - Kerberos
  - Authentication
  - Enterprise IT
---

The upcoming NTLM removal in libcurl is one of those changes that looks technical but is actually organizational. If your Git over HTTPS path to Azure DevOps Server still depends on NTLM, your issue is not tooling, it is identity debt.

Original source: https://devblogs.microsoft.com/devops/upcoming-change-ntlm-removal-in-git-libcurl-impact-to-azure-devops-server-customers/

Microsoft is right to push hard here. NTLM has known cryptographic weaknesses and should not be a modern enterprise default. The dangerous part is that many environments believe they are using Kerberos when they are actually surviving on silent SPNEGO fallback to NTLM. That illusion disappears in September 2026.

My opinion: **do not treat this as a "client version" problem**. Re-enabling NTLM flags, pinning old Git builds, or hoping fallback remains available is a short-lived workaround with long-term risk. If your remediation strategy is downgrade-and-delay, you are actively increasing operational fragility.

A practical migration sequence should be blunt and measurable.

- **Verify current auth behavior now.** Run trace-based checks and ticket cache validation in real developer and build-agent contexts, including off-domain and remote-network paths.
- **Fix Kerberos end-to-end:** SPNs, DNS aliases, load balancer settings, delegation, and domain controller reachability.
- **Identify non-domain-joined or workgroup scenarios early** and design an SSH lane where Kerberos cannot be made reliable.

You also need ownership clarity. Security teams should define policy baselines, but platform engineering must own implementation readiness. This cannot be a side task for individual repo admins. It requires coordinated changes across IIS, AD, network edge, CI agents, and developer workstation guidance.

One subtle risk is automation. Build agents and service accounts frequently run in contexts where Kerberos tickets are missing or invalid, even when human users are fine. If you only test interactive developer workflows, you will miss the most critical breakpoints.

The upside is real. Moving cleanly to Kerberos or SSH not only avoids breakage, it **reduces attack surface and aligns identity controls** with modern compliance expectations. The teams that start this transition now will treat September as a nonevent. The teams that wait will be debugging auth failures under release pressure.

This is not a warning to archive. **It is a deadline to execute against.**
