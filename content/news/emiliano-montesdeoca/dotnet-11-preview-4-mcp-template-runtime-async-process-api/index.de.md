---
title: ".NET 11 Preview 4: MCP-Server-Vorlage, Runtime-Async-Bibliotheken, Prozess-API"
date: 2026-05-25
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 4 ist verfügbar. Die Highlights: die MCP-Server-Vorlage im SDK, mit Runtime-Async kompilierte Laufzeitbibliotheken, dotnet watch für Mobile und eine umfangreiche Erweiterung der Prozess-API."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - .NET MAUI
---

.NET 11 Preview 4 ist verfügbar. Jede Hauptversion einer .NET-Preview fügt eine lange Liste von Elementen über Runtime, SDK, Bibliotheken, ASP.NET Core, MAUI, C# und Entity Framework hinzu. Anstatt die vollständige Liste zu wiederholen, hier die Dinge, die mir aufgefallen sind.

## Die MCP-Server-Vorlage kommt ins .NET SDK

Das interessanteste Element: Eine MCP-Server-Projektvorlage ist jetzt im SDK enthalten. Das bedeutet, dass `dotnet new mcp-server` (oder wie der Befehl letztendlich heißen wird) ohne zusätzliche Konfiguration funktioniert. Für alle, die MCP-Tooling in .NET entwickeln, reduziert das den Aufwand für den Einstieg erheblich. Die MCP-Integration in die Plattform-Toolchain signalisiert die Richtung, in die das Ökosystem geht.

## Laufzeitbibliotheken mit Runtime-Async kompiliert

Die Laufzeit selbst kompiliert jetzt ihre Standardbibliotheken mit der Runtime-Async-Funktion. Das ist eine interne Änderung, die die Performance betrifft — Async-Zustandsmaschinen in der Laufzeit werden effizienter. Die Bedeutung liegt nicht in sichtbaren API-Änderungen; es ist vielmehr, dass Runtime-Async reif genug ist, um für die BCL selbst verwendet zu werden, was ein bedeutsames Signal über die Bereitschaft der Funktion ist.

## JIT-Optimierungen und Hardware-Intrinsics

Preview 4 setzt die JIT-Arbeit fort. Verbesserungen bei Hardware-Intrinsics und der Codegenerierung werden hier geliefert — Details finden sich in den Runtime-Versionshinweisen. Diese Art von Änderungen verbessert typischerweise den Durchsatz bei rechenintensiven Schleifen, ohne dass Code-Änderungen Ihrerseits erforderlich sind.

## Erweiterung der Prozess-API

Ein umfangreiches Update für `System.Diagnostics.Process` kommt in Preview 4:

- `Process.RunAndCaptureTextAsync` — einen Prozess starten, stdout/stderr erfassen, auf das Ende warten, alles in einem Aufruf ohne Deadlock-Risiko
- `KillOnParentExit` — leichte Lebensdauer-Kopplung zwischen Eltern- und Kindprozessen
- `SafeProcessHandle`-basierte APIs, die trimmer-freundlicher sind

Wenn Sie jemals Boilerplate geschrieben haben, um Prozessausgaben ohne Deadlocks zu erfassen (asynchrones Lesen von stdout *und* stderr gleichzeitig), ist `RunAndCaptureTextAsync` die API, die Ihnen fehlte.

## dotnet watch für Android und iOS

`dotnet watch` unterstützt jetzt die Geräteauswahl für .NET MAUI Android- und iOS-Projekte. Schnellere Iteration auf Mobilgeräten ohne manuelle Verwaltung von Geräteverbindungen im Build-Loop.

## Span-basierte Komprimierungs-APIs

Neue span-basierte Deflate-, ZLib- und GZip-Encoder-/Decoder-APIs kommen in die Bibliotheken. Weniger Allokationen beim Umgang mit komprimierten Daten — relevant, wenn Sie hochdurchsatzfähige Datenverarbeitung betreiben.

## Ausprobieren

[.NET 11 Preview 4 herunterladen](https://dotnet.microsoft.com/download/dotnet/11.0) — es ist eine Preview, nicht produktionsreif, aber es lohnt sich, sie gegen Ihre Projekte zu testen, um Probleme frühzeitig vor dem RC-Zyklus zu erkennen.

Originalpost: [.NET 11 Preview 4 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-4/)
