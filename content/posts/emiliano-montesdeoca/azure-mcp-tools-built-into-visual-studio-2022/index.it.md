---
title: "Gli strumenti Azure MCP sono ora integrati in Visual Studio 2022 — Nessuna estensione necessaria"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: "Gli strumenti Azure MCP vengono distribuiti come parte del carico di lavoro di sviluppo Azure in Visual Studio 2022. Oltre 230 strumenti, 45 servizi Azure, zero estensioni da installare."
tags:
  - visual-studio
  - azure
  - mcp
  - copilot
  - developer-tools
---

> *Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "azure-mcp-tools-built-into-visual-studio-2022.md" >}}).*

Se hai usato gli strumenti Azure MCP in Visual Studio tramite l'estensione separata, conosci il rituale — installare il VSIX, riavviare, sperare che non si rompa nulla, gestire le incompatibilità di versione. Quella frizione è finita.

Yun Jung Choi ha [annunciato](https://devblogs.microsoft.com/visualstudio/azure-mcp-tools-now-ship-built-into-visual-studio-2022-no-extension-required/) che gli strumenti Azure MCP vengono ora distribuiti direttamente come parte del carico di lavoro di sviluppo Azure in Visual Studio 2022. Nessuna estensione. Nessun VSIX. Nessun balletto del riavvio.

## Cosa significa concretamente

A partire da Visual Studio 2022 versione 17.14.30, il Azure MCP Server è incluso nel carico di lavoro di sviluppo Azure. Se hai già quel carico di lavoro installato, basta attivarlo in GitHub Copilot Chat e sei a posto.

Oltre 230 strumenti per 45 servizi Azure — accessibili direttamente dalla finestra di chat. Elenca i tuoi account di archiviazione, fai il deploy di un'app ASP.NET Core, diagnostica problemi di App Service, interroga Log Analytics — tutto senza aprire una scheda del browser.

## Perché questo conta più di quanto sembri

Il punto sugli strumenti per sviluppatori è questo: ogni passaggio in più è frizione, e la frizione uccide l'adozione. Avere MCP come estensione separata significava incompatibilità di versione, errori di installazione e un'altra cosa da tenere aggiornata. Integrarlo nel carico di lavoro significa:

- **Un unico percorso di aggiornamento** tramite il Visual Studio Installer
- **Nessuna divergenza di versione** tra l'estensione e l'IDE
- **Sempre aggiornato** — il MCP Server si aggiorna con i rilasci regolari di VS

Per i team che standardizzano su Azure, questo è un grande vantaggio. Installi il carico di lavoro una volta, attivi gli strumenti, e sono disponibili per ogni sessione.

## Cosa puoi farci

Gli strumenti coprono l'intero ciclo di vita dello sviluppo tramite Copilot Chat:

- **Imparare** — chiedi informazioni sui servizi Azure, best practice, pattern architetturali
- **Progettare e sviluppare** — ottieni raccomandazioni sui servizi, configura il codice dell'applicazione
- **Fare deploy** — provisiona risorse e fai il deploy direttamente dall'IDE
- **Risolvere problemi** — interroga i log, verifica lo stato delle risorse, diagnostica problemi in produzione

Un esempio rapido — scrivi questo in Copilot Chat:

```
List my storage accounts in my current subscription.
```

Copilot chiama gli strumenti Azure MCP dietro le quinte, interroga le tue sottoscrizioni e restituisce una lista formattata con nomi, posizioni e SKU. Niente portale necessario.

## Come attivarlo

1. Aggiorna a Visual Studio 2022 **17.14.30** o superiore
2. Assicurati che il carico di lavoro **Azure development** sia installato
3. Apri GitHub Copilot Chat
4. Clicca sul pulsante **Select tools** (l'icona delle due chiavi)
5. Attiva **Azure MCP Server**

Tutto qui. Rimane attivato tra le sessioni.

## Un'avvertenza

Gli strumenti sono disattivati per default — devi attivarli manualmente. E gli strumenti specifici per VS 2026 non sono disponibili in VS 2022. La disponibilità degli strumenti dipende anche dai permessi della tua sottoscrizione Azure, come nel portale.

## Il quadro generale

Questo fa parte di una tendenza chiara: MCP sta diventando lo standard per esporre gli strumenti cloud negli IDE di sviluppo. Abbiamo già visto il [rilascio stabile di Azure MCP Server 2.0](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/) e integrazioni MCP in VS Code e altri editor. Averlo integrato nel sistema dei carichi di lavoro di Visual Studio è la naturale evoluzione.

Per noi sviluppatori .NET che viviamo in Visual Studio, questo elimina un altro motivo per fare context-switch verso il portale Azure. E onestamente, meno cambi di scheda si fanno, meglio è.
