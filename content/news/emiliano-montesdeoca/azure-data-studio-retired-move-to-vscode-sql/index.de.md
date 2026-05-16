---
title: "Azure Data Studio wird eingestellt: Azure SQL-Workflows zu VS Code migrieren"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio wurde am 6. Februar 2025 eingestellt, der Support endet am 28. Februar 2026. Hier ist der vollständige Migrationspfad zu VS Code mit der MSSQL-Erweiterung."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

[Azure Data Studio wurde am 6. Februar 2025 eingestellt](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), der Support endet am 28. Februar 2026 — der empfohlene Ersatz ist VS Code mit der MSSQL-Erweiterung.

## Was zu installieren ist

Drei Dinge für den Einstieg:

- **MSSQL-Erweiterung** — suche nach „SQL Server (mssql)" im VS Code Marketplace
- **SQL Database Projects-Erweiterung** — Schema als Code, Build-Validierung, geführte Veröffentlichung
- **.NET 8 SDK** — vom Build-System benötigt; fehlendes SDK ist das häufigste Problem beim ersten Start

## ADS-Verbindungen und Einstellungen migrieren

Die MSSQL-Erweiterung enthält das **ADS Migration Toolkit**, das die einmalige Migration in einem geführten Ablauf übernimmt: gespeicherte Verbindungen, Verbindungsgruppen, Einstellungen und Tastenkürzel werden automatisch importiert.

## F5-Muskelgedächtnis wiederherstellen

ADS-Nutzer verlassen sich auf F5 zum Ausführen von Abfragen. Installiere die Erweiterung **MSSQL Database Management Keymap**, um ADS-Tastenkürzel inklusive F5 zurückzubekommen.

## SQL Database Projects: Schema als Code

Rechtsklick auf ein Projekt → **Veröffentlichen** → Ziel konfigurieren → generierten T-SQL-Script prüfen → deployen. Die Script-Vorschau vor dem Deployment ist das zentrale Sicherheitsmerkmal. Elementvorlagen erzeugen Stubs für Tabellen, gespeicherte Prozeduren und Views — derselbe Workflow wie bei SSDT.

Häufiges Problem: eine **Zielplattform-Inkompatibilität** in der `.sqlproj`-Datei verursacht Build-Fehler, wenn das Projekt gegen eine andere SQL Server-Version erstellt wurde.

## Schema Compare und Schema Designer

Die Erweiterung enthält außerdem **Schema Compare** (Unterschiede zwischen Projekt und bereitgestellter Datenbank) und **Schema Designer** (visuelle Schema-Bearbeitung ohne manuelles DDL-Schreiben).

## Microsoft Fabric-Entwickler

Die Einrichtung ist identisch, aber starte zunächst im **Fabric-Portal** und verbinde die Datenbank zuerst mit Git, bevor du sie in VS Code öffnest. Microsoft hat einen dedizierten Leitfaden: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Fazit

Die Migration ist ein einmaliger geführter Ablauf, kein manueller Neuaufbau. Installiere die drei Tools, führe das ADS Migration Toolkit aus, stelle die Tastenkürzel wieder her — und du bist in unter 10 Minuten wieder einsatzbereit.

Den [vollständigen Artikel](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) findest du mit Schritt-für-Schritt-Screenshots und der Fabric-spezifischen Anleitung.
