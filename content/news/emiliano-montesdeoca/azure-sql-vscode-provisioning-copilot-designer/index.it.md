---
title: "L'estensione MSSQL per VS Code sta diventando silenziosamente una piattaforma molto più grande"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "L'ultimo aggiornamento dell'estensione MSSQL aggiunge provisioning di Azure SQL, progettazione dello schema assistita da Copilot, Data API builder e notebook. La parte interessante è quanta parte del lavoro sui database può ora restare dentro VS Code."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

L'estensione MSSQL per VS Code è cresciuta da tempo, ma questo ultimo aggiornamento rende la direzione molto più chiara.

Non è più solo «connetti e lancia qualche query».

Con il **provisioning di Azure SQL**, **Schema Designer con Copilot**, i **SQL Notebooks** e **Data API builder** tutti spinti in avanti in un'unica release, l'estensione sta diventando un ambiente di lavoro molto più completo per lo sviluppo centrato sui database.

## Il richiamo pratico è il provisioning direttamente dall'editor

L'articolo sorgente dice che ora puoi creare un database cloud completamente gestito «direttamente dal tuo editor e senza costi» usando il tier gratuito.

È il tipo di funzionalità che sembra piccola finché non ti rendi conto di quanta frizione di configurazione elimina.

Per molti sviluppatori, la parte fastidiosa delle sperimentazioni pesanti sui dati non è SQL in sé. È il gap di ambiente tra:

- idea
- database
- schema
- API
- backend testabile

Se quel gap si accorcia dentro un solo tool, l'intero workflow diventa più attraente.

## Ecco come appare un inner loop più forte per il lavoro sui dati

Quello che mi piace di questa release è che mantiene più parte del workflow del database nello stesso posto:

- provisioning del database
- progettazione dello schema
- revisione delle modifiche
- generazione di script ORM
- esposizione di API
- test degli endpoint
- documentazione e query tramite notebook

Questa è una storia molto più convincente che trattare SQL come uno strumento laterale scollegato nello stack.

## Il flusso di lavoro dello schema assistito da Copilot è dove il valore dell'AI sembra reale

Le aggiunte al designer dello schema sono particolarmente interessanti perché sembrano trovare un buon equilibrio.

Il valore non è «l'AI progetta il tuo modello dati e tu ti fidi ciecamente».

Il valore è:

- punti di partenza più rapidi
- revisione visiva
- tracciamento delle modifiche
- output orientato alla migrazione
- controlli espliciti accetta/annulla

È un workflow AI molto più sano di una generazione automatica completa senza un percorso di ispezione.

E per il lavoro sui database, la revisabilità conta moltissimo.

## Data API builder è un moltiplicatore silenzioso

L'altra funzionalità che non ignorerei è l'integrazione di Data API builder.

Se puoi passare dallo schema a:

- REST
- GraphQL
- endpoint MCP

all'interno dello stesso ambiente, crei un percorso molto efficiente per prototipi backend e tool interni.

Questo non sostituisce un'ingegneria backend più profonda. Ma accorcia moltissimo il percorso dall'idea di database a un'interfaccia funzionante.

## La mia lettura

Questa release fa sembrare l'estensione MSSQL più una piccola piattaforma dentro VS Code che un semplice add-on.

Per gli sviluppatori che costruiscono API, strumenti dati, tool di amministrazione o prototipi basati su SQL, è un cambiamento significativo.

E se Microsoft continuerà a stringere questo loop, l'estensione diventerà molto più strategicamente utile di quanto molte persone pensino ancora.

Articolo originale: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)