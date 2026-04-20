---
title: ".NET April 2026 Servicing — Beveiligingspatches Die Je Vandaag Moet Toepassen"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "De servicing-release van april 2026 patcht 6 CVE's in .NET 10, .NET 9, .NET 8 en .NET Framework — inclusief twee kwetsbaarheden voor externe code-uitvoering."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "dotnet-april-2026-servicing-security-patches" >}}).*

De [servicing-updates van april 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) voor .NET en .NET Framework zijn beschikbaar, en deze bevat beveiligingsfixes die je snel wilt toepassen. Zes CVE's gepatcht, waaronder twee kwetsbaarheden voor externe code-uitvoering (RCE).

## Wat er gepatcht is

| CVE | Type | Betreft |
|-----|------|---------|
| CVE-2026-26171 | Beveiligingsfunctieomzeiling | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Externe code-uitvoering** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Externe code-uitvoering** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denial of service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denial of service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denial of service | .NET Framework 2.0–4.8.1 |

## Bijgewerkte versies

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

## Wat te doen

Update je projecten en CI/CD-pipelines naar de nieuwste patchversies. Twee RCE-kwetsbaarheden zijn niet iets wat je uitstelt.
