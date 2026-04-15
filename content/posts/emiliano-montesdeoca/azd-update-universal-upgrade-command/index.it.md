---
title: "azd update — Un solo comando per tutti i tuoi package manager"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI ora ha un comando di aggiornamento universale che funziona indipendentemente da come lo hai installato — winget, Homebrew, Chocolatey o script di installazione."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "azd-update-universal-upgrade-command.md" >}}).*

Conosci quel messaggio "È disponibile una nuova versione di azd" che compare ogni poche settimane? Quello che ignori perché non ricordi se hai installato `azd` tramite winget, Homebrew o quello script curl che hai eseguito sei mesi fa? Ecco, finalmente è stato risolto.

Microsoft ha appena rilasciato [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/) — un unico comando che aggiorna Azure Developer CLI all'ultima versione indipendentemente da come lo hai installato in origine. Windows, macOS, Linux — non importa. Un solo comando.

## Come funziona

```bash
azd update
```

Tutto qui. Se vuoi accesso anticipato alle nuove funzionalità, puoi passare alla build giornaliera insiders:

```bash
azd update --channel daily
azd update --channel stable
```

Il comando rileva il tuo metodo di installazione attuale e utilizza il meccanismo di aggiornamento appropriato dietro le quinte. Niente più "aspetta, ho usato winget o choco su questa macchina?"

## Il piccolo dettaglio

`azd update` è disponibile a partire dalla versione 1.23.x. Se sei su una versione precedente, dovrai fare un ultimo aggiornamento manuale usando il tuo metodo di installazione originale. Dopo di che, `azd update` gestisce tutto d'ora in avanti.

Controlla la tua versione attuale con `azd version`. Se hai bisogno di un'installazione da zero, la [documentazione di installazione](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) fa al caso tuo.

## Perché è importante

È un piccolo miglioramento della qualità della vita, ma per chi di noi usa `azd` quotidianamente per il deploy di agenti IA e app Aspire su Azure, essere aggiornati significa meno momenti "questo bug era già stato corretto nell'ultima versione". Una cosa in meno a cui pensare.

Leggi l'[annuncio completo](https://devblogs.microsoft.com/azure-sdk/azd-update/) e l'[approfondimento](https://blog.jongallant.com/2026/04/azd-update) di Jon Gallant per maggiori dettagli.
