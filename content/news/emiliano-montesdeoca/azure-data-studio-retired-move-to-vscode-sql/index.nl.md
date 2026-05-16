---
title: "Azure Data Studio is met pensioen: verplaats je Azure SQL-workflow naar VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio is op 6 februari 2025 met pensioen gegaan, ondersteuning eindigt op 28 februari 2026. Hier is het volledige migratiepad naar VS Code met de MSSQL-extensie."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

[Azure Data Studio is op 6 februari 2025 met pensioen gegaan](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), ondersteuning eindigt op 28 februari 2026 — de aanbevolen vervanger is VS Code met de MSSQL-extensie.

## Wat te installeren

Drie dingen om mee te beginnen:

- **MSSQL-extensie** — zoek "SQL Server (mssql)" in de VS Code Marketplace
- **SQL Database Projects-extensie** — schema als code, buildvalidatie, begeleide publicatie
- **.NET 8 SDK** — vereist door het buildsysteem; ontbrekende SDK is het meest voorkomende probleem bij eerste gebruik

## ADS-verbindingen en instellingen migreren

De MSSQL-extensie bevat de **ADS Migration Toolkit**, die de eenmalige migratie in een begeleide flow afhandelt: opgeslagen verbindingen, verbindingsgroepen, instellingen en sneltoetsen worden allemaal automatisch geïmporteerd.

## F5-spiergeheugen herstellen

ADS-gebruikers vertrouwen op F5 om query's uit te voeren. Installeer de extensie **MSSQL Database Management Keymap** om ADS-stijl sneltoetsen terug te krijgen, inclusief F5.

## SQL Database Projects: schema als code

Rechtsklik op een project → **Publiceren** → doel configureren → gegenereerd T-SQL-script bekijken → implementeren. De scriptpreview vóór implementatie is de belangrijkste veiligheidsfunctie. Itemsjablonen genereren stubs voor tabellen, opgeslagen procedures en views — dezelfde workflow als SSDT.

Veelvoorkomend probleem: een **doelplatformconflict** in het `.sqlproj`-bestand veroorzaakt buildfouten als het project voor een andere versie van SQL Server was gemaakt.

## Schema Compare en Schema Designer

De extensie bevat ook **Schema Compare** (verschil tussen je project en de geïmplementeerde database) en **Schema Designer** (visuele schema-bewerking zonder handmatig DDL te schrijven).

## Microsoft Fabric-ontwikkelaars

De instelling is identiek, maar begin vanuit de **Fabric-portal** en verbind de database eerst met Git voordat je deze opent in VS Code. Microsoft heeft een speciale handleiding: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Afronding

De migratie is een eenmalige begeleide flow, geen handmatige herbouw. Installeer de drie tools, voer de ADS Migration Toolkit uit, herstel je sneltoetsen — en je bent in minder dan 10 minuten weer operationeel.

Zie het [volledige artikel](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) voor stap-voor-stap screenshots en de Fabric-specifieke walkthrough.
