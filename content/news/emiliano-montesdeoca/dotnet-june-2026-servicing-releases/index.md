---
title: ".NET and .NET Framework June 2026 servicing releases updates"
description: "Microsoft's June 2026 servicing update fixes three .NET CVEs and ships .NET 10.0.9, 9.0.17, and 8.0.28, while .NET Framework has no new updates this month."
date: 2026-10-27
author: "Emiliano Montesdeoca"
tags: [".NET", "Security", "Updates", "Maintenance Release", "CVE"]
slug: dotnet-june-2026-servicing-releases
---

Original source: [.NET and .NET Framework June 2026 servicing releases updates](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-june-2026-servicing-updates/)

The June 2026 .NET servicing update is a reminder that routine maintenance is part of security work. Microsoft lists three fixed CVEs across .NET 10.0, .NET 9.0, and .NET 8.0, along with the corresponding runtime, installer, container, and Linux package updates. The release also makes an important boundary clear: .NET Framework has no new security or non-security updates this month.

## Three CVEs fixed across supported .NET versions

The update lists these vulnerabilities:

- **CVE-2026-45591**: .NET Security Vulnerability, applying to .NET 10.0, 9.0, and 8.0
- **CVE-2026-45491**: .NET Security Vulnerability, applying to .NET 10.0, 9.0, and 8.0
- **CVE-2026-45490**: .NET Security Vulnerability, applying to .NET 10.0, 9.0, and 8.0

The source identifies the CVEs and links to the Microsoft Security Response Center guidance, but it does not describe their attack surfaces in the servicing post. That makes the release notes and the linked vulnerability guidance the right places to investigate impact for a specific application. Do not infer severity or exploitability from the short release summary alone.

The released patch versions are:

- **.NET 10.0.9**
- **.NET 9.0.17**
- **.NET 8.0.28**

These versions are listed in the release notes and installer links for each major release. Microsoft also points to updated container images, Linux package instructions, and known-issues pages. Teams that build applications from official .NET container images should verify the base image tag they use and rebuild through the normal validation path.

## The servicing surface is broader than the runtime binary

A runtime patch is not only an installer on a developer workstation. The June guidance links to release notes, installers and binaries, container images, Linux packages, and known issues for .NET 10.0, 9.0, and 8.0. Each deployment path needs its own check.

For a containerized ASP.NET Core service, that can mean updating the base image reference, rebuilding the image, running the application tests, and confirming that the resulting artifact is the one deployed by CI. For Linux-hosted services installed from packages, confirm the package update and the runtime selected by the service. For build agents, check the SDK and runtime installations separately instead of assuming that updating one machine updated the whole pipeline.

The linked ASP.NET Core and runtime changelogs are also useful. They show the servicing work behind the headline versions and can reveal fixes that are relevant to an application even when the CVE list is the immediate reason for upgrading.

## .NET Framework is unchanged this month

The .NET Framework section is concise: there are no new security or new non-security updates available for June 2026. That is not a reason to stop monitoring Framework workloads; it is simply the correct result for this month’s servicing cycle.

Teams maintaining a mix of modern .NET and .NET Framework applications should keep the two release paths distinct in their inventory. The absence of a Framework update does not change the required patch decision for .NET 10.0, 9.0, or 8.0 applications, and a modern .NET update does not imply a Framework update.

## A focused update checklist

1. **Inventory the running versions.** Check the runtime and SDK versions on build agents, hosts, and deployment images.
2. **Review the CVE guidance.** Follow the linked MSRC entries and release notes for the applications and versions you operate.
3. **Check known issues.** Read the known-issues page for the target .NET major version before promoting the update.
4. **Update each delivery path.** Patch installers, Linux packages, container base images, and CI environments as applicable.
5. **Test before production.** Run unit, integration, startup, and deployment checks against the new patch version.
6. **Record the Framework decision.** Note that no new .NET Framework update is available this month, then keep its release notes in the normal monthly review.

This is standard servicing work rather than a reason to improvise a deployment. A clear version inventory, a short validation cycle, and a documented production change window are enough to turn the June update into a controlled maintenance task.