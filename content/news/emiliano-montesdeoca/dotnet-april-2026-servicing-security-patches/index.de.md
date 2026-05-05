---
title: ".NET April 2026 Servicing — Sicherheitspatches, die du heute einspielen solltest"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Das Servicing-Release vom April 2026 behebt 6 CVEs in .NET 10, .NET 9, .NET 8 und .NET Framework — darunter zwei Schwachstellen für Remotecodeausführung."
tags:
  - dotnet
  - security
  - servicing
  - dotnet-framework
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "dotnet-april-2026-servicing-security-patches.md" >}}).*

Die [Servicing-Updates vom April 2026](https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-april-2026-servicing-updates/) für .NET und .NET Framework sind da, und dieses Mal sind Sicherheitsfixes dabei, die ihr zeitnah einspielen solltet. Sechs CVEs wurden gepatcht, darunter zwei Schwachstellen für Remotecodeausführung (RCE).

## Was wurde gepatcht

Hier die Kurzübersicht:

| CVE | Typ | Betrifft |
|-----|-----|----------|
| CVE-2026-26171 | Umgehung von Sicherheitsfunktionen | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-32178 | **Remotecodeausführung** | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-33116 | **Remotecodeausführung** | .NET 10, 9, 8 |
| CVE-2026-32203 | Denial of Service | .NET 10, 9, 8 + .NET Framework |
| CVE-2026-23666 | Denial of Service | .NET Framework 3.0–4.8.1 |
| CVE-2026-32226 | Denial of Service | .NET Framework 2.0–4.8.1 |

Die beiden RCE-CVEs (CVE-2026-32178 und CVE-2026-33116) betreffen die breiteste Palette an .NET-Versionen und sollten Priorität haben.

## Aktualisierte Versionen

- **.NET 10**: 10.0.6
- **.NET 9**: 9.0.15
- **.NET 8**: 8.0.26

Alle sind über die üblichen Kanäle verfügbar — [dotnet.microsoft.com](https://dotnet.microsoft.com/download/dotnet/10.0), Container-Images auf MCR und Linux-Paketmanager.

## Was zu tun ist

Aktualisiert eure Projekte und CI/CD-Pipelines auf die neuesten Patch-Versionen. Wenn ihr Container nutzt, zieht die neuesten Images. Wenn ihr .NET Framework einsetzt, prüft die [.NET Framework Release Notes](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes) für die entsprechenden Patches.

Für alle, die .NET 10 in Produktion betreiben (es ist das aktuelle Release), ist 10.0.6 ein Pflicht-Update. Gleiches gilt für .NET 9.0.15 und .NET 8.0.26, falls ihr auf diesen LTS-Versionen seid. Zwei RCE-Schwachstellen sind nichts, was man aufschiebt.
