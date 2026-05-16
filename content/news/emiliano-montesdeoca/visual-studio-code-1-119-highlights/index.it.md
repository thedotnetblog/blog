---
title: "VS Code 1.119: OpenTelemetry per le sessioni degli agenti, integrazione del browser e sicurezza"
date: 2026-05-15
author: "Emiliano Montesdeoca"
description: "VS Code 1.119 (maggio 2026) aggiunge il tracciamento OpenTelemetry per le sessioni degli agenti, la condivisione delle schede del browser, miglioramenti di fiducia e sicurezza, e una patch di sicurezza 1.119.1."
tags:
  - VS Code
  - .NET
  - Developer Tools
  - Productivity
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[VS Code 1.119](https://code.visualstudio.com/updates/v1_119) è stato rilasciato il 6 maggio 2026 (con una patch di sicurezza 1.119.1 poco dopo). La versione si concentra sull'osservabilità degli agenti, l'interazione con il browser e la riduzione delle interruzioni.

## Tracciamento OpenTelemetry per le sessioni degli agenti

Questa è la funzionalità di punta per chiunque esegua agenti in produzione o esegua il debug di flussi di lavoro agentici. Abilitarla con due impostazioni:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.otlpEndpoint": "http://localhost:4318"
```

Le tracce seguono le convenzioni semantiche GenAI. Ogni richiesta dell'agente produce uno span root `invoke_agent` con span figli annidati: `chat`, `execute_tool` e `execute_hook`. L'utilizzo dei token viene riportato per richiesta — inclusi i conteggi di lettura della cache e creazione della cache.

Funziona con l'agente locale, l'agente in background Copilot CLI e l'agente Claude. Qualsiasi backend compatibile OTLP accetta le tracce — l'[Aspire Dashboard standalone](https://learn.microsoft.com/en-us/dotnet/aspire/fundamentals/dashboard/standalone) funziona bene per lo sviluppo locale.

## Gli agenti ora possono accedere alle schede del browser

Gli agenti possono richiedere l'accesso alle schede del browser integrato — ma non è automatico. È necessario condividere esplicitamente una scheda tramite il selettore di contesto, trascinamento e rilascio o contesto suggerito. C'è un pulsante di condivisione nel browser per revocare l'accesso. Quando un agente tenta di aprire una nuova scheda sullo stesso dominio di una scheda già aperta (non condivisa), VS Code chiede di riutilizzare la scheda esistente.

## Utilizzo ottimizzato dei token

Un modello leggero sperimentale ora gestisce le liste di attività degli agenti, mantenendo questo lavoro amministrativo lontano dal modello primario più costoso. Riduce il consumo di token per attività che non richiedono piena capacità di ragionamento.

## Fiducia e sicurezza

Meno interruzioni: VS Code 1.119 riduce i prompt per le richieste di accesso alla rete e le scritture nelle cartelle temporanee da parte degli agenti. La patch 1.119.1 risolve specifici problemi di sicurezza — vale la pena aggiornare se non è ancora stato fatto.

## Cambio rapido all'anteprima Markdown

Piccolo ma utile: ora è possibile passare rapidamente dall'editor corrente all'anteprima Markdown senza navigare.

## VS Code Agents (anteprima Insiders)

L'interfaccia di sessione degli agenti riprogettata — nuovo selettore di repository (locale/repos/remoto), miglioramenti delle sotto-sessioni, rifinitura web e mobile, animazioni di avanzamento — è disponibile in Insiders su [insiders.vscode.dev/agents](https://insiders.vscode.dev/agents).

Changelog completo: [code.visualstudio.com/updates/v1_119](https://code.visualstudio.com/updates/v1_119).
