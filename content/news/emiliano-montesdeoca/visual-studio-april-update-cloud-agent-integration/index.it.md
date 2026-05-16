---
title: "Aggiornamento di aprile di Visual Studio 2026: agente cloud, agenti personalizzati e agente debugger"
date: 2026-05-14
author: "Emiliano Montesdeoca"
description: "L'aggiornamento di aprile di Visual Studio 2026 (18.5) porta l'integrazione dell'agente cloud, agenti personalizzati a livello utente, strumenti C++ in GA e un Agente Debugger che valida le correzioni contro il comportamento runtime reale."
tags:
  - Visual Studio
  - .NET
  - AI Agents
  - Productivity
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

[L'aggiornamento di aprile di Visual Studio 2026 (18.5)](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/) include l'integrazione dell'agente cloud, agenti personalizzati a livello utente, strumenti C++ che raggiungono la GA e un nuovo Agente Debugger.

## Agente cloud: delegare il lavoro a una sessione Copilot remota

Dal selettore di agenti nella finestra Chat, selezionando **Cloud** è possibile delegare un'attività a un agente di coding Copilot remoto. Si descrive il lavoro, l'agente crea un issue GitHub nel repository, poi apre una PR quando ha finito. Si riceve una notifica con "View PR" / "Open in browser" — tutto funziona mentre si continua a programmare, o anche con l'IDE chiuso.

## Gli agenti personalizzati ora ti seguono ovunque

Gli agenti personalizzati a livello utente memorizzati in `%USERPROFILE%/.github/agents/` non sono più limitati al repository — ti seguono attraverso i progetti. Il percorso di archiviazione è configurabile in Tools > Options > GitHub > Copilot > Chat. Il pulsante `+` nel selettore di agenti consente di creare nuovi agenti direttamente. Ottengono le stesse capacità degli agenti con scope di repository: consapevolezza dello spazio di lavoro, strumenti, selezione del modello e connessioni MCP.

Agenti integrati: Agent, Ask, Copilot CLI, Debugger, Modernize, Profiler.

## Gli strumenti di editing del codice C++ diventano GA

Due strumenti — `get_symbol_call_hierarchy` e `get_symbol_class_hierarchy` — sono ora attivi per impostazione predefinita. Forniscono a Copilot una navigazione consapevole del linguaggio nelle basi di codice C++, coprendo gerarchie di ereditarietà e catene di chiamate di funzioni. Abilitare tramite l'icona Tools in Copilot Chat. Funziona meglio con i modelli di tool-calling.

## Agente Debugger: correzioni validate contro il comportamento runtime reale

Inizia da un issue GitHub o Azure DevOps (o una descrizione in linguaggio naturale), passa alla modalità Debugger, e l'agente:

1. Crea un riproduttore minimo
2. Genera ipotesi di errore
3. Strumenta l'app con tracepoint e breakpoint condizionali
4. Esegue una vera sessione di debug
5. Analizza la telemetria in tempo reale
6. Suggerisce una correzione precisa

Si rimane nel ciclo durante tutto il processo — è interattivo, non completamente autonomo.

## Correzione della priorità IntelliSense

VS ora sopprime i completamenti Copilot mentre la lista IntelliSense è attiva. Un solo suggerimento alla volta. Era un punto di attrito frequente e ora è attivo per impostazione predefinita.

Note di rilascio complete e download su [devblogs.microsoft.com](https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/).
