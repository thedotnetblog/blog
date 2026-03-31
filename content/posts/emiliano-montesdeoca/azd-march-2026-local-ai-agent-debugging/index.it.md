---
title: "azd ora permette di eseguire e debuggare agenti IA localmente — Ecco cosa è cambiato a marzo 2026"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI ha rilasciato sette versioni a marzo 2026. I punti salienti: un loop locale di esecuzione e debug per agenti IA, integrazione con GitHub Copilot nella configurazione dei progetti, e supporto per Container App Jobs."
tags:
  - azure
  - azd
  - ai
  - agents
  - dotnet
  - developer-tools
  - containers
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "azd-march-2026-local-ai-agent-debugging.md" >}}).*

Sette rilasci in un mese. È quello che il team dell'Azure Developer CLI (`azd`) ha pubblicato a marzo 2026, e la funzionalità principale è quella che stavo aspettando: **un loop locale di esecuzione e debug per agenti IA**.

PC Chan [ha pubblicato il riepilogo completo](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/), e anche se c'è molto contenuto, lasciatemi filtrare ciò che conta davvero per gli sviluppatori .NET che costruiscono app con IA.

## Eseguire e debuggare agenti IA senza deploy

Questa è la novità principale. La nuova estensione `azure.ai.agents` aggiunge comandi che danno un'esperienza di inner-loop adeguata per gli agenti IA:

- `azd ai agent run` — avvia il tuo agente localmente
- `azd ai agent invoke` — gli invia messaggi (locale o in produzione)
- `azd ai agent show` — mostra lo stato del container e la sua salute
- `azd ai agent monitor` — trasmette i log del container in tempo reale

Prima, testare un agente IA significava fare deploy su Microsoft Foundry ogni volta che facevi un cambiamento. Ora puoi iterare localmente, testare il comportamento del tuo agente, e fare deploy solo quando sei pronto.

## GitHub Copilot configura il tuo progetto azd

`azd init` ora offre un'opzione "Set up with GitHub Copilot (Preview)". Invece di rispondere manualmente ai prompt, un agente Copilot genera la configurazione per te. Quando un comando fallisce, `azd` offre troubleshooting assistito dall'IA — tutto senza lasciare il terminale.

## Container App Jobs e miglioramenti del deployment

- **Container App Jobs**: `azd` ora fa deploy di `Microsoft.App/jobs` tramite la config esistente `host: containerapp`.
- **Timeout configurabili**: Nuovo flag `--timeout` su `azd deploy` e campo `deployTimeout` in `azure.yaml`.
- **Fallback di build remoto**: Quando il build ACR fallisce, `azd` passa automaticamente a Docker/Podman locale.
- **Validazione preflight locale**: I parametri Bicep vengono validati localmente prima del deploy.

## Miglioramenti DX

- **Rilevamento automatico pnpm/yarn** per progetti JS/TS
- **Supporto pyproject.toml** per Python
- **Directory template locali** — `azd init --template` accetta percorsi del filesystem
- **Messaggi di errore migliori** in modalità `--no-prompt`
- **Variabili d'ambiente di build** iniettate in tutti i sottoprocessi di build (.NET, Node.js, Java, Python)

## Per concludere

Il loop locale di debug per agenti IA è la star di questa release, ma l'accumulo di miglioramenti al deployment e alla DX rende `azd` più maturo che mai. Se fai deploy di app .NET su Azure — specialmente agenti IA — questo aggiornamento vale la pena.

Consulta le [note di rilascio complete](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-march-2026/) per tutti i dettagli.
