---
title: ".NET April 2026 Servicing — Security Patches You Should Apply Today"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "The April 2026 servicing release patches 6 CVEs across .NET 10, .NET 9, .NET 8, and .NET Framework — including two remote code execution vulnerabilities."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

The [April 2026 servicing updates](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) for .NET and .NET Framework are out, and this one includes security fixes you'll want to apply soon. Six CVEs patched, including two remote code execution (RCE) vulnerabilities.

## What's patched

Here's the quick summary:

| CVE | Type | Affects |
|-----|------|---------|
| CVE-2026-26171 | Security Feature Bypass | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Remote Code Execution** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Remote Code Execution** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denial of Service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denial of Service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denial of Service | .NET Framework 2.0–4.8.1 |

The two RCE CVEs (CVE-2026-32178 and CVE-2026-33116) affect the broadest range of .NET versions and should be the priority.

## Updated versions

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

All are available via the usual channels — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), container images on MCR, and Linux package managers.

## What to do

Update your projects and CI/CD pipelines to the latest patch versions. If you're running containers, pull the latest images. If you're on .NET Framework, check the [.NET Framework release notes](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) for the corresponding patches.

For those running .NET 10 in production (it's the current release), 10.0.6 is a mandatory update. Same for .NET 9.0.15 and .NET 8.0.26 if you're on those LTS tracks. Two RCE vulnerabilities are not something you postpone.
