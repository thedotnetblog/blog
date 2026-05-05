---
title: "VS Code 1.115 — Notifiche del Terminale in Background, Modalità Agente SSH e Altro"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 porta notifiche del terminale in background per gli agenti, hosting remoto di agenti tramite SSH, incolla file nei terminali e tracciamento delle modifiche con riconoscimento di sessione. Ecco cosa conta per gli sviluppatori .NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "vscode-1-115-agent-improvements.md" >}}).*

VS Code 1.115 è appena [uscito](https://code.visualstudio.com/updates/v1_115), e sebbene sia un rilascio più leggero in termini di funzionalità principali, i miglioramenti relativi agli agenti sono genuinamente utili se lavori quotidianamente con assistenti di codice basati su IA.

Lasciami evidenziare cosa vale davvero la pena sapere.

## I terminali in background comunicano con gli agenti

Questa è la funzionalità di punta. I terminali in background ora notificano automaticamente gli agenti quando i comandi vengono completati, inclusi il codice di uscita e l'output del terminale. I prompt di input nei terminali in background vengono anche rilevati e mostrati all'utente.

Perché è importante? Se hai usato la modalità agente di Copilot per eseguire comandi di build o suite di test in background, conosci il dolore del "ma è già finito?" — i terminali in background erano essenzialmente spara-e-dimentica. Ora l'agente viene notificato quando il tuo `dotnet build` o `dotnet test` è completato, vede l'output e può reagire di conseguenza. È un piccolo cambiamento che rende i flussi di lavoro guidati dagli agenti significativamente più affidabili.

C'è anche un nuovo strumento `send_to_terminal` che permette agli agenti di inviare comandi ai terminali in background con conferma dell'utente, risolvendo il problema dove `run_in_terminal` con un timeout spostava i terminali in background e li rendeva di sola lettura.

## Hosting remoto di agenti tramite SSH

VS Code ora supporta la connessione a macchine remote tramite SSH, installando automaticamente la CLI e avviandola in modalità host di agenti. Questo significa che le tue sessioni di agenti IA possono puntare direttamente ad ambienti remoti — utile per gli sviluppatori .NET che compilano e testano su server Linux o VM nel cloud.

## Tracciamento delle modifiche nelle sessioni degli agenti

Le modifiche ai file effettuate durante le sessioni degli agenti ora vengono tracciate e ripristinate, con diff, annulla/ripristina e ripristino dello stato. Se un agente apporta modifiche al tuo codice e qualcosa va storto, puoi vedere esattamente cosa è cambiato e fare il rollback. Tranquillità nel lasciare che gli agenti modifichino la tua codebase.

## Riconoscimento delle schede del browser e altri miglioramenti

Alcune aggiunte aggiuntive per la qualità della vita:

- **Tracciamento delle schede del browser** — la chat ora può tracciare e collegare le schede del browser aperte durante una sessione, così gli agenti possono fare riferimento alle pagine web che stai guardando
- **Incolla file nel terminale** — incolla file (incluse immagini) nel terminale con Ctrl+V, trascinamento o clic destro
- **Copertura dei test nella minimap** — gli indicatori di copertura dei test ora appaiono nella minimap per una panoramica visiva rapida
- **Pinch-to-zoom su Mac** — il browser integrato supporta i gesti pinch-to-zoom
- **Diritti Copilot nelle Sessioni** — la barra di stato mostra le informazioni di utilizzo nella vista Sessioni
- **Favicon in Vai al File** — le pagine web aperte mostrano le favicon nella lista di selezione rapida

## Per concludere

VS Code 1.115 è un rilascio incrementale, ma i miglioramenti degli agenti — notifiche del terminale in background, hosting di agenti SSH e tracciamento delle modifiche — si sommano a un'esperienza notevolmente più fluida per lo sviluppo assistito dall'IA. Se stai usando la modalità agente di Copilot per progetti .NET, questi sono il tipo di miglioramenti di qualità della vita che riducono l'attrito quotidiano.

Dai un'occhiata alle [note di rilascio complete](https://code.visualstudio.com/updates/v1_115) per ogni dettaglio.
