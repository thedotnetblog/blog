---
title: "SQL MCP Server, Copilot in SSMS und ein Database Hub mit KI-Agenten: Was von der SQLCon 2026 wirklich zählt"
date: 2026-03-28
author: "Emiliano Montesdeoca"
description: "Microsoft hat auf der SQLCon 2026 eine ganze Reihe von Datenbank-Ankündigungen gemacht. Hier ist das, was wirklich zählt, wenn du KI-gestützte Apps auf Azure SQL baust."
tags:
  - azure
  - ai
  - sql
  - databases
  - mcp
---

Microsoft hat gerade die [SQLCon 2026 zusammen mit der FabCon in Atlanta](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) eröffnet, und es gibt eine Menge zu besprechen. Die ursprüngliche Ankündigung deckt alles ab, von Sparplänen bis hin zu Enterprise-Compliance-Features. Ich werde die Enterprise-Preisfolien überspringen und mich auf die Dinge konzentrieren, die wichtig sind, wenn du als Entwickler mit Azure SQL und KI arbeitest.

## SQL MCP Server ist in der Public Preview

Das ist für mich die Hauptnachricht. Azure SQL Database Hyperscale hat jetzt einen **SQL MCP Server** in der Public Preview, mit dem du deine SQL-Daten sicher mit KI-Agenten und Copilots über das [Model Context Protocol](https://modelcontextprotocol.io/) verbinden kannst.

Wenn du die MCP-Welle verfolgt hast — und ehrlich gesagt, man kann sie gerade kaum übersehen — dann ist das eine große Sache. Statt eigene Datenpipelines zu bauen, um deinen KI-Agenten Kontext aus der Datenbank zu liefern, bekommst du ein standardisiertes Protokoll, um SQL-Daten direkt zur Verfügung zu stellen. Deine Agenten können live Datenbankinformationen abfragen, darüber nachdenken und darauf reagieren.

Für diejenigen von uns, die KI-Agenten mit Semantic Kernel oder dem Microsoft Agent Framework bauen, eröffnet das einen sauberen Integrationspfad. Dein Agent muss den Lagerbestand prüfen? Einen Kundendatensatz nachschlagen? Eine Bestellung validieren? MCP gibt ihm einen strukturierten Weg, das zu tun, ohne dass du für jedes Szenario maßgeschneiderten Datenabruf-Code schreiben musst.

## GitHub Copilot in SSMS 22 ist jetzt GA

Wenn du Zeit in SQL Server Management Studio verbringst — und seien wir ehrlich, die meisten von uns tun das immer noch — GitHub Copilot ist jetzt in SSMS 22 allgemein verfügbar. Dieselbe Copilot-Erfahrung, die du bereits in VS Code und Visual Studio nutzt, aber für T-SQL.

Der praktische Nutzen ist klar: Chat-basierte Unterstützung beim Schreiben von Abfragen, Refactoring von Stored Procedures, Fehlerbehebung bei Performance-Problemen und Verwaltungsaufgaben. Konzeptionell nichts Revolutionäres, aber es direkt in SSMS zu haben bedeutet, dass du nicht zu einem anderen Editor wechseln musst, nur um KI-Hilfe für deine Datenbankarbeit zu bekommen.

## Vector Indexes haben ein ernsthaftes Upgrade bekommen

Azure SQL Database hat jetzt schnellere, leistungsfähigere Vector Indexes mit voller Unterstützung für Insert, Update und Delete. Das bedeutet, deine Vektordaten bleiben in Echtzeit aktuell — kein Batch-Reindexing mehr nötig.

Das ist neu:
- **Quantisierung** für kleinere Indexgrößen ohne zu viel Genauigkeit zu verlieren
- **Iteratives Filtering** für präzisere Ergebnisse
- **Engere Integration mit dem Query Optimizer** für vorhersagbare Performance

Wenn du Retrieval-Augmented Generation (RAG) mit Azure SQL als Vector Store machst, sind diese Verbesserungen direkt nützlich. Du kannst deine Vektoren zusammen mit deinen relationalen Daten in derselben Datenbank halten, was deine Architektur im Vergleich zum Betrieb einer separaten Vektordatenbank erheblich vereinfacht.

Dieselben Vektor-Verbesserungen sind auch in SQL Database in Fabric verfügbar, da beide unter der Haube auf derselben SQL-Engine laufen.

## Database Hub in Fabric: Agentisches Management

Dieser Punkt ist eher zukunftsorientiert, aber er ist interessant. Microsoft hat den **Database Hub in Microsoft Fabric** (Early Access) angekündigt, der dir eine einheitliche Ansicht über Azure SQL, Cosmos DB, PostgreSQL, MySQL und SQL Server via Arc bietet.

Der interessante Aspekt ist nicht nur die einheitliche Ansicht — es ist der agentische Ansatz beim Management. KI-Agenten überwachen kontinuierlich dein Datenbankökosystem, zeigen auf, was sich geändert hat, erklären, warum es wichtig ist, und schlagen vor, was als nächstes zu tun ist. Es ist ein Human-in-the-Loop-Modell, bei dem der Agent die Vorarbeit leistet und du die Entscheidungen triffst.

Für Teams, die mehr als eine Handvoll Datenbanken verwalten, könnte das den operativen Lärm wirklich reduzieren. Statt zwischen Portalen zu wechseln und manuell Metriken zu prüfen, bringt der Agent das Signal zu dir.

## Was das für .NET-Entwickler bedeutet

Der rote Faden, der all diese Ankündigungen verbindet, ist klar: Microsoft bettet KI-Agenten in jede Schicht des Datenbank-Stacks ein. Nicht als Spielerei, sondern als praktische Werkzeugebene.

Wenn du .NET-Apps baust, die auf Azure SQL basieren, hier ist, was ich tatsächlich tun würde:

1. **Probier den SQL MCP Server aus**, wenn du KI-Agenten baust. Es ist der sauberste Weg, deinen Agenten Datenbankzugriff zu geben, ohne eigene Plumbing zu bauen.
2. **Aktiviere Copilot in SSMS**, falls du es noch nicht getan hast — ein kostenloser Produktivitätsgewinn für die tägliche SQL-Arbeit.
3. **Schau dir Vector Indexes an**, wenn du RAG machst und derzeit einen separaten Vector Store betreibst. Die Konsolidierung auf Azure SQL bedeutet einen Service weniger zu verwalten.

## Zusammenfassung

Die vollständige Ankündigung enthält mehr — Sparpläne, Migrationsassistenten, Compliance-Features — aber die Developer-Story liegt im MCP Server, den Vektor-Verbesserungen und der agentischen Management-Schicht. Das sind die Dinge, die verändern, wie du baust, nicht nur wie du budgetierst.

Schau dir die [vollständige Ankündigung von Shireesh Thota](https://www.microsoft.com/en-us/sql-server/blog/2026/03/18/advancing-agentic-ai-with-microsoft-databases-across-a-unified-data-estate/) für das komplette Bild an, und [melde dich für den Database Hub Early Access an](https://aka.ms/database-hub), wenn du die neue Management-Erfahrung ausprobieren möchtest.
