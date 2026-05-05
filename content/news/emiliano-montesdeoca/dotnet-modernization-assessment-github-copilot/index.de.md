---
title: "GitHub Copilots Modernisierungs-Assessment ist das beste Migrationstool, das du noch nicht nutzt"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Die Modernisierungserweiterung von GitHub Copilot schlägt nicht nur Code-Änderungen vor — sie erstellt ein vollständiges Migrations-Assessment mit umsetzbaren Issues, Azure-Zielvergleichen und einem kollaborativen Workflow. Hier erfährst du, warum das Assessment-Dokument der Schlüssel zu allem ist."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "dotnet-modernization-assessment-github-copilot.md" >}}).*

Eine Legacy-.NET-Framework-App auf modernes .NET zu migrieren ist eine dieser Aufgaben, von der jeder weiß, dass sie erledigt werden sollte, die aber niemand anfangen will. Es ist nie nur „ändere das Ziel-Framework." Es sind APIs, die verschwunden sind, Pakete, die nicht mehr existieren, Hosting-Modelle, die völlig anders funktionieren, und eine Million kleiner Entscheidungen darüber, was containerisiert, was umgeschrieben und was in Ruhe gelassen werden soll.

Jeffrey Fritz hat gerade einen [tiefen Einblick in GitHub Copilots Modernisierungs-Assessment](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) veröffentlicht, und ehrlich? Das ist das beste Migrationstooling, das ich für .NET gesehen habe. Nicht wegen der Code-Generierung — das ist mittlerweile Standard. Wegen des Assessment-Dokuments, das es erstellt.

## Es ist nicht nur eine Code-Vorschlagsmaschine

Die VS Code-Erweiterung folgt einem **Bewerten → Planen → Ausführen**-Modell. Die Bewertungsphase analysiert deine gesamte Codebase und erstellt ein strukturiertes Dokument, das alles erfasst: was sich ändern muss, welche Azure-Ressourcen provisioniert werden müssen, welches Deployment-Modell verwendet werden soll. Alles Nachfolgende — Infrastructure as Code, Containerisierung, Deployment-Manifeste — leitet sich aus den Ergebnissen des Assessments ab.

Das Assessment wird unter `.github/modernize/assessment/` in deinem Projekt gespeichert. Jeder Durchlauf erzeugt einen unabhängigen Report, sodass du eine Historie aufbaust und verfolgen kannst, wie sich deine Migrationsposition entwickelt, wenn du Issues behebst.

## Zwei Wege zum Start

**Empfohlenes Assessment** — der schnelle Weg. Wähle aus kuratierten Domains (Java/.NET Upgrade, Cloud Readiness, Sicherheit) und erhalte aussagekräftige Ergebnisse ohne Konfigurationsaufwand. Ideal für einen ersten Blick, wo deine App steht.

**Benutzerdefiniertes Assessment** — der gezielte Weg. Konfiguriere genau, was analysiert werden soll: Ziel-Compute (App Service, AKS, Container Apps), Ziel-OS, Containerisierungsanalyse. Wähle mehrere Azure-Ziele, um Migrationsansätze nebeneinander zu vergleichen.

Diese Vergleichsansicht ist wirklich nützlich. Eine App mit 3 obligatorischen Issues für App Service könnte 7 für AKS haben. Beides zu sehen hilft bei der Hosting-Entscheidung, bevor man sich auf einen Migrationspfad festlegt.

## Die Issue-Aufschlüsselung ist umsetzbar

Jedes Issue kommt mit einem Kritikalitätslevel:

- **Obligatorisch** — muss behoben werden, sonst scheitert die Migration
- **Potenziell** — könnte die Migration beeinflussen, braucht menschliche Beurteilung
- **Optional** — empfohlene Verbesserungen, blockiert die Migration nicht

Und jedes Issue verlinkt zu betroffenen Dateien und Zeilennummern, liefert eine detaillierte Beschreibung dessen, was falsch ist und warum es für deine Zielplattform wichtig ist, gibt konkrete Behebungsschritte (nicht nur „repariere das") und enthält Links zur offiziellen Dokumentation.

Du kannst einzelne Issues an Entwickler weitergeben, und sie haben alles, was sie zum Handeln brauchen. Das ist der Unterschied zwischen einem Tool, das dir sagt „es gibt ein Problem" und einem, das dir sagt, wie du es löst.

## Die abgedeckten Upgrade-Pfade

Für .NET spezifisch:
- .NET Framework → .NET 10
- ASP.NET → ASP.NET Core

Jeder Upgrade-Pfad hat Erkennungsregeln, die wissen, welche APIs entfernt wurden, welche Patterns kein direktes Äquivalent haben und welche Sicherheitsprobleme Aufmerksamkeit erfordern.

Für Teams, die mehrere Apps verwalten, gibt es auch ein CLI, das Multi-Repo-Batch-Assessments unterstützt — alle Repos klonen, alle bewerten, App-spezifische Reports plus eine aggregierte Portfolio-Ansicht bekommen.

## Meine Einschätzung

Wenn du auf Legacy-.NET-Framework-Apps sitzt (und seien wir ehrlich, die meisten Enterprise-Teams tun das), ist dies *das* Tool zum Starten. Allein das Assessment-Dokument ist die Zeit wert — es verwandelt ein vages „wir sollten modernisieren" in eine konkrete, priorisierte Liste von Arbeitspaketen mit klaren Wegen nach vorn.

Der kollaborative Workflow ist auch clever: Assessments exportieren, mit deinem Team teilen, importieren ohne erneut auszuführen. Architektur-Reviews, bei denen die Entscheider nicht diejenigen sind, die die Tools ausführen? Abgedeckt.

## Zusammenfassung

GitHub Copilots Modernisierungs-Assessment verwandelt .NET-Migration von einem beängstigenden, undefinierten Projekt in einen strukturierten, nachverfolgbaren Prozess. Starte mit einem empfohlenen Assessment, um zu sehen, wo du stehst, und nutze dann benutzerdefinierte Assessments, um Azure-Ziele zu vergleichen und deinen Migrationsplan zu erstellen.

Lies den [vollständigen Walkthrough](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) und hole dir die [VS Code-Erweiterung](https://aka.ms/ghcp-appmod/vscode-ext), um es an deinem eigenen Code auszuprobieren.
