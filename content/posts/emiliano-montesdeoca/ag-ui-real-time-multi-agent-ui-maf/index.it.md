---
title: "Costruire UI Multi-Agente in Tempo Reale Che Non Sembrino una Scatola Nera"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI e Microsoft Agent Framework si alleano per dare ai workflow multi-agente un vero frontend — con streaming in tempo reale, approvazioni umane e piena visibilità su cosa stanno facendo i tuoi agenti."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

Ecco il punto dei sistemi multi-agente: nelle demo sono incredibili. Tre agenti che si passano il lavoro, risolvono problemi, prendono decisioni. Poi provi a metterlo davanti a utenti reali e... silenzio. Un indicatore che gira. Nessuna idea di quale agente stia facendo cosa o perché il sistema sia in pausa. Quello non è un prodotto — è un problema di fiducia.

Il team di Microsoft Agent Framework ha appena pubblicato un [fantastico walkthrough](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) su come accoppiare i workflow MAF con [AG-UI](https://github.com/ag-ui-protocol/ag-ui), un protocollo aperto per lo streaming degli eventi di esecuzione degli agenti verso un frontend tramite Server-Sent Events. E onestamente? È esattamente il ponte che ci mancava.

## Perché questo è importante per gli sviluppatori .NET

Se stai costruendo app alimentate dall'IA, probabilmente hai già sbattuto contro questo muro. La tua orchestrazione backend funziona benissimo — gli agenti si passano il lavoro, gli strumenti si attivano, le decisioni vengono prese. Ma il frontend non ha idea di cosa stia succedendo dietro le quinte. AG-UI risolve questo definendo un protocollo standard per lo streaming degli eventi degli agenti (pensa a `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) direttamente verso il tuo layer UI tramite SSE.

La demo è un workflow di supporto clienti con tre agenti: un agente di triage che smista le richieste, un agente rimborsi che gestisce le questioni di denaro, e un agente ordini che gestisce le sostituzioni. Ogni agente ha i propri strumenti, e la topologia di handoff è definita esplicitamente — niente "scoprilo dal prompt".

## La topologia di handoff è la vera star

Quello che mi ha colpito è come `HandoffBuilder` ti permette di dichiarare un grafo di routing diretto tra gli agenti:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Ogni `add_handoff` crea un arco diretto con una descrizione in linguaggio naturale. Il framework genera strumenti di handoff per ogni agente basandosi su questa topologia. Quindi le decisioni di routing sono fondate sulla tua struttura di orchestrazione, non solo su quello che il LLM decide di fare. Questo è un vantaggio enorme per l'affidabilità in produzione.

## Human-in-the-loop che funziona davvero

La demo mostra due pattern di interruzione di cui qualsiasi app di agenti reale ha bisogno:

**Interruzioni di approvazione strumenti** — quando un agente chiama uno strumento marcato con `approval_mode="always_require"`, il workflow si mette in pausa ed emette un evento. Il frontend mostra un modal di approvazione con il nome dello strumento e i suoi argomenti. Niente loop di retry che bruciano token — solo un flusso pulito pausa-approvazione-ripresa.

**Interruzioni di richiesta informazioni** — quando un agente ha bisogno di più contesto dall'utente (come un ID ordine), si mette in pausa e chiede. Il frontend mostra la domanda, l'utente risponde, e l'esecuzione riprende esattamente da dove si era fermata.

Entrambi i pattern vengono trasmessi come eventi AG-UI standard, quindi il tuo frontend non ha bisogno di logica personalizzata per agente — semplicemente renderizza qualsiasi evento arrivi dalla connessione SSE.

## Collegare il tutto è sorprendentemente semplice

L'integrazione tra MAF e AG-UI si riduce a una singola chiamata di funzione:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

La `workflow_factory` crea un workflow fresco per thread, così ogni conversazione ottiene il proprio stato isolato. L'endpoint gestisce tutta l'infrastruttura SSE automaticamente. Se stai già usando FastAPI (o puoi aggiungerlo come layer leggero), c'è praticamente zero frizione.

## La mia opinione

Per noi sviluppatori .NET, la domanda immediata è: "Posso farlo in C#?" L'Agent Framework è disponibile sia per .NET che per Python, e il protocollo AG-UI è agnostico rispetto al linguaggio (è solo SSE). Quindi anche se questa demo specifica usa Python e FastAPI, il pattern si traduce direttamente. Potresti configurare una API minimale ASP.NET Core con endpoint SSE seguendo lo stesso schema di eventi AG-UI.

Il messaggio più importante è che le UI multi-agente stanno diventando una preoccupazione di prima classe, non un ripensamento. Se stai costruendo qualcosa dove gli agenti interagiscono con gli umani — supporto clienti, workflow di approvazione, elaborazione documenti — questa combinazione di orchestrazione MAF e trasparenza AG-UI è il pattern da seguire.

## Per concludere

AG-UI + Microsoft Agent Framework ti dà il meglio di entrambi i mondi: orchestrazione multi-agente robusta nel backend e visibilità in tempo reale nel frontend. Niente più interazioni tra agenti come scatole nere.

Dai un'occhiata al [walkthrough completo](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) e al [repository del protocollo AG-UI](https://github.com/ag-ui-protocol/ag-ui) per approfondire.
