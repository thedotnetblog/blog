---
title: "L'aggiornamento di marzo di Visual Studio permette di creare agenti Copilot personalizzati — e find_symbol è rivoluzionario"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'aggiornamento di marzo 2026 di Visual Studio porta agenti Copilot personalizzati, skill riutilizzabili, lo strumento find_symbol con riconoscimento del linguaggio, e profiling con Copilot dal Test Explorer."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "visual-studio-march-2026-custom-copilot-agents.md" >}}).*

Visual Studio ha appena ricevuto il suo aggiornamento Copilot più significativo. Mark Downie [ha annunciato il rilascio di marzo](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), e il titolo sono gli agenti personalizzati — ma onestamente, lo strumento `find_symbol` potrebbe essere la funzionalità che cambia di più il tuo workflow.

## Agenti Copilot personalizzati nel tuo repo

Vuoi che Copilot segua gli standard del tuo team? Gli agenti personalizzati sono definiti come file `.agent.md` in `.github/agents/`. Ogni agente ha accesso completo al workspace, comprensione del codice, strumenti, il tuo modello preferito e connessioni MCP.

## Agent skill: pacchetti di istruzioni riutilizzabili

Le skill vengono caricate automaticamente da `.github/skills/` nel tuo repo o `~/.copilot/skills/` nel tuo profilo.

## find_symbol: navigazione consapevole del linguaggio

Il nuovo strumento `find_symbol` dà alla modalità agente di Copilot una navigazione dei simboli basata sui servizi di linguaggio. Invece di cercare testo, l'agente può trovare tutti i riferimenti di un simbolo e accedere a informazioni su tipi e scope.

Per gli sviluppatori .NET, è un miglioramento enorme — i codebase C# con gerarchie di tipi profonde ne beneficiano enormemente.

## Profilare test con Copilot

C'è un nuovo **Profile with Copilot** nel menu contestuale del Test Explorer. Il Profiling Agent esegue il test e analizza le performance automaticamente.

## Perf tip durante il debug dal vivo

L'ottimizzazione delle performance ora avviene durante il debug. Visual Studio mostra il tempo di esecuzione inline. Linea lenta? Clicca sul Perf Tip e chiedi a Copilot suggerimenti.

## Correggere vulnerabilità NuGet dal Solution Explorer

Un link **Fix with GitHub Copilot** appare direttamente nel Solution Explorer quando viene rilevata una vulnerabilità.

## Per concludere

Agenti personalizzati e skill fanno il titolo, ma `find_symbol` è la gemma nascosta — cambia fondamentalmente la precisione di Copilot nel refactoring di codice .NET. Scarica [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) per provare tutto.
