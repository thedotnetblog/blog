---
title: "Azure Data Studio è stato ritirato: sposta il tuo flusso di Azure SQL su VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio è stato ritirato il 6 febbraio 2025, con supporto fino al 28 febbraio 2026. Ecco il percorso di migrazione completo verso VS Code con l'estensione MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[Azure Data Studio è stato ritirato il 6 febbraio 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), con supporto fino al 28 febbraio 2026 — il sostituto consigliato è VS Code con l'estensione MSSQL.

## Cosa installare

Tre elementi per iniziare:

- **Estensione MSSQL** — cerca "SQL Server (mssql)" nel Marketplace di VS Code
- **Estensione SQL Database Projects** — schema come codice, validazione della build, pubblicazione guidata
- **.NET 8 SDK** — richiesto dal sistema di build; l'SDK mancante è il problema più comune al primo avvio

## Migrare le connessioni e le impostazioni di ADS

L'estensione MSSQL include l'**ADS Migration Toolkit**, che gestisce la migrazione una tantum in un flusso guidato: connessioni salvate, gruppi di connessioni, impostazioni e tasti di scelta rapida vengono importati automaticamente.

## Ripristinare la memoria muscolare del F5

Gli utenti di ADS si affidano a F5 per eseguire le query. Installa l'estensione **MSSQL Database Management Keymap** per recuperare i tasti di scelta rapida in stile ADS, incluso F5.

## SQL Database Projects: schema come codice

Clic destro su un progetto → **Pubblica** → configura la destinazione → rivedi lo script T-SQL generato → distribuisci. L'anteprima dello script prima del deployment è la funzionalità di sicurezza chiave. I modelli di elementi generano stub per tabelle, stored procedure e viste — lo stesso flusso di SSDT.

Problema frequente: un'**incompatibilità della piattaforma di destinazione** nel file `.sqlproj` causerà errori di build se il progetto è stato creato per una versione diversa di SQL Server.

## Schema Compare e Schema Designer

L'estensione include anche **Schema Compare** (differenza tra il progetto e il database distribuito) e **Schema Designer** (modifica visuale dello schema senza scrivere DDL a mano).

## Sviluppatori di Microsoft Fabric

La configurazione è identica, ma inizia dal **portale Fabric** e connetti prima il database a Git prima di aprirlo in VS Code. Microsoft ha una guida dedicata: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## In conclusione

La migrazione è un flusso guidato una tantum, non una ricostruzione manuale. Installa i tre strumenti, esegui l'ADS Migration Toolkit, ripristina i tuoi tasti di scelta rapida e sarai di nuovo operativo in meno di 10 minuti.

Consulta l'[articolo completo](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) per screenshot passo-passo e la guida specifica per Fabric.
