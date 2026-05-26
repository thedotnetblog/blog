---
title: "NuGet-Paket-Pruning in .NET 10 ist genau die Art von Verbesserung, die man überall spürt"
date: 2026-05-23
author: "Emiliano Montesdeoca"
description: "Das neue NuGet-Paket-Pruning in .NET 10 reduziert falsch positive Sicherheitsmeldungen, vereinfacht den Restore-Graphen und verbessert die Restore-Performance. Es ist eine dieser Plattformänderungen, die den Alltag still und leise besser machen."
tags:
  - .NET
  - NuGet
  - Security
  - Developer Tools
  - .NET 10
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "index.md" >}}).*

Manche Plattformverbesserungen sind spannend, weil sie neue Szenarien ermöglichen.

Andere sind spannend, weil sie bestehende Workflows weniger laut, weniger fragil und weniger nervig machen.

**NuGet-Paket-Pruning in .NET 10** gehört ganz klar zur zweiten Kategorie, und das meine ich als Kompliment.

## Warum das wichtig ist

Wenn du schon einmal mit Lärm durch transitive Schwachstellen, unnötig großen Restore-Graphen oder Paketen zu tun hattest, die technisch vorhanden sind, für den Laufzeitkontext deiner App aber gar nicht relevant sind, dann trifft diese Änderung einen echten Schmerzpunkt.

Pruning hilft, indem es von der effektiven Abhängigkeitsstruktur die von der Plattform bereitgestellten Pakete entfernt, wenn die Runtime sie bereits selbst liefert.

Das bedeutet:

- weniger falsch positive Sicherheitsmeldungen
- sauberere transitive Abhängigkeitsgraphen
- weniger Restore-Overhead
- aussagekräftigere Audit-Ergebnisse

## Meine Einschätzung

Genau so stelle ich mir sinnvolle .NET-Verbesserungen vor.

Sie machen die Defaults besser, reduzieren den mentalen Aufwand und verbessern gleichzeitig die Qualität der Security-Signale und das tägliche Verhalten der Tools.

Das ist ein Gewinn, selbst wenn es nie eine Keynote-Folie bekommt.

Originalbeitrag: [NuGet Package Pruning: Cleaner Dependencies and Actionable Vulnerability Reports](https://devblogs.microsoft.com/dotnet/nuget-package-pruning-in-dotnet-10/)
