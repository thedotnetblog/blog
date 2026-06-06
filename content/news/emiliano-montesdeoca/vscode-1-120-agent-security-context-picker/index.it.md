---
title: "VS Code 1.120: Prompt Password, Selettore Dimensione Contesto, Metadati GitHub in Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 è una release focalizzata per gli utenti di Copilot: gestione sicura dei prompt password, selettore dimensione contesto del modello, metadati PR GitHub nelle sessioni agente e gestione degli archivi di sessione."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 è uscito con un insieme di miglioramenti all'agente Copilot che sono piccoli individualmente ma notevolmente migliori nell'uso quotidiano.

## Rilevamento Sicuro dei Prompt Password nei Terminali dell'Agente

Quando un agente Copilot esegue un comando di terminale che innesca un prompt di password o passphrase, VS Code ora lo rileva e mostra un dialogo di conferma. Il dialogo focalizza il terminale in modo che tu possa digitare il segreto direttamente — e in modo cruciale, i segreti non vengono mai instradati attraverso il modello.

Questo è un miglioramento significativo della sicurezza. In precedenza, gli agenti che eseguivano comandi che innescavano prompt di autenticazione potevano creare situazioni in cui gli utenti potrebbero inavvertitamente esporre credenziali. L'annuncio del lettore di schermo significa che anche gli utenti con disabilità ricevono la notifica.

## Selettore Dimensione Contesto nel Selettore Modello

Un nuovo selettore di dimensione del contesto ti permette di selezionare quanto contesto il modello utilizza per una sessione. Diversi modelli hanno diverse dimensioni della finestra di contesto, e alcuni flussi di lavoro beneficiano di limitarla (latenza inferiore, costo inferiore) o massimizzarla (codebase complesse, sessioni di lunga durata).

## Metadati PR GitHub nelle Sessioni Agent Host

Per le sessioni supportate da un repository GitHub, VS Code ora mostra i metadati GitHub — incluso un pulsante di pull request — nell'interfaccia utente dell'agent host. Meno cambi di contesto verso il browser o l'estensione GitHub quando stai lavorando su una PR.

## Gestione dell'Archivio Sessioni Chat

Due miglioramenti per il Quick Pick delle sessioni:
- Le sessioni archiviate sono nascoste per impostazione predefinita (meno disordine visivo)
- La ricerca corrisponde ancora alle sessioni archiviate, in modo da poterne ripristinare una per titolo

Le sessioni sono anche raggruppate per recenza per impostazione predefinita, facilitando la ricerca del lavoro recente.

## Scoperta Plugin CLI Copilot

VS Code ora scopre automaticamente i plugin Copilot CLI installati dall'utente da `~/.copilot/installed-plugins/`. Se hai configurato WinUI o altre abilità agente specifiche del dominio, vengono rilevate senza configurazione manuale.

## API Editor Diff Personalizzato (Anteprima)

Per gli autori di estensioni: una nuova API proposta `customDiffEditorProvider` permette alle estensioni di renderizzare un diff unificato in una singola webview con accesso a entrambi i documenti originali e modificati, invece di due viste di editor personalizzate affiancate.

Post originale: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
