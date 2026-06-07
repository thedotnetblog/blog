---
title: "VS Code 1.121: Aggiungere Modelli Preferiti, Compressione Output Terminal, SSH per Agent"
date: 2026-06-07
author: "Emiliano Montesdeoca"
description: "VS Code 1.121 aggiunge i modelli preferiti, compressione espansa dell'output del terminal per esecutori di test e strumenti di build, timer di silenziamento inattivo per terminali in background e autenticazione SSH interattiva da tastiera nell'agent host."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.121 continua i miglioramenti di qualità dell'agente Copilot da 1.120, con focus sulla gestione dei modelli e il comportamento del terminal.

## Aggiungere Modelli Preferiti

Il selettore di modelli ora supporta il pinning. Se utilizzi sempre lo stesso modello o due, aggiungili alla cima dell'elenco. Riduce lo scorrimento quando hai accesso a molti modelli di più provider.

## Compressione Espansa dell'Output del Terminal

Lo strumento terminal dell'agente comprimeva già l'output per i comandi comuni. 1.121 espande questo per coprire esecutori di test e strumenti di build:

- **Esecutori di test:** `pytest`, `jest`, `cargo test`
- **Strumenti di build:** `tsc`, `cargo build`, `make`
- **Linter, Docker, gestori di pacchetti**

Le lunghe output di build e i report di fallimenti dei test sono compressi in estratti rilevanti prima di essere passati al modello. Questo mantiene l'utilizzo del contesto gestibile quando l'agente esegue cicli di build o suite di test, che possono produrre migliaia di righe di output.

## Timer di Silenziamento Inattivo per Terminal in Background

Un nuovo timer di silenziamento inattivo per lo strumento `run_in_terminal`: se un comando sincrono non produce output per un periodo configurabile, viene automaticamente promosso all'esecuzione in background. Questo impedisce ai comandi a lungo termine di bloccare l'agente quando elaborano silenziosamente. Ottieni un ID terminal da controllare più tardi.

## Variabile d'Ambiente VSCODE_AGENT

Quando Copilot Chat esegue comandi nel terminal, ora viene impostata una variabile d'ambiente `VSCODE_AGENT`. Utile se hai script o strumenti che si comportano diversamente quando chiamati da una sessione agente rispetto a in modo interattivo.

## Aggiungi alla Chat dal Browser

Fare clic con il tasto destro nel browser integrato ora mostra un'opzione "Aggiungi alla Chat". Seleziona contenuto da una pagina web e aggiungilo direttamente al tuo contesto Copilot Chat senza copiare e incollare.

## Risolto: Comandi Shell Multi-linea in Agent Host

Una correzione di bug attesa: i comandi shell multi-linea nello strumento terminal di Agent Host ora funzionano correttamente. Precedentemente, questi potevano fallire o produrre comportamento errato.

## Autenticazione SSH Interattiva da Tastiera

Le connessioni SSH di Agent Host ora supportano l'autenticazione interattiva da tastiera — il metodo di autenticazione di fallback utilizzato da alcuni server SSH (incluse alcune configurazioni aziendali più vecchie). Gli agenti che lavorano su host SSH remoti hanno meno probabilità di incorrere in fallimenti di autenticazione.

Post originale: [Visual Studio Code 1.121](https://code.visualstudio.com/updates/v1_121)
