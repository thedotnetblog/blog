---
title: "Microsoft Foundry Marzo 2026 — GPT-5.4, Agent Service GA e il Refresh dell'SDK Che Cambia Tutto"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "L'aggiornamento di marzo 2026 di Microsoft Foundry è enorme: Agent Service raggiunge la GA, GPT-5.4 porta un ragionamento affidabile, l'SDK azure-ai-projects diventa stabile in tutti i linguaggi, e Fireworks AI porta i modelli aperti su Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}}).*

I post mensili "Novità in Microsoft Foundry" sono solitamente un mix di miglioramenti incrementali e occasionali funzionalità di rilievo. L'[edizione di marzo 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? Praticamente tutte funzionalità di rilievo. Foundry Agent Service raggiunge la GA, GPT-5.4 arriva in produzione, l'SDK riceve un importante rilascio stabile, e Fireworks AI porta l'inferenza di modelli aperti su Azure. Vediamo cosa conta per gli sviluppatori .NET.

## Foundry Agent Service è pronto per la produzione

Questa è la grande notizia. Il runtime di agenti di nuova generazione è generalmente disponibile — costruito sull'API Responses di OpenAI, compatibile a livello di protocollo con gli agenti OpenAI, e aperto a modelli di diversi provider. Se state costruendo con l'API Responses oggi, migrare a Foundry aggiunge sicurezza enterprise, networking privato, RBAC di Entra, tracing completo e valutazione sulla vostra logica di agenti esistente.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Aggiunte chiave: networking privato end-to-end, espansione dell'autenticazione MCP (incluso il passthrough OAuth), anteprima di Voice Live per agenti voce-a-voce, e agenti ospitati in 6 nuove regioni.

## GPT-5.4 — affidabilità oltre l'intelligenza pura

GPT-5.4 non riguarda l'essere più intelligente. Riguarda l'essere più affidabile. Ragionamento più solido nelle interazioni lunghe, migliore aderenza alle istruzioni, meno fallimenti a metà workflow, e capacità integrate di computer use. Per gli agenti in produzione, quell'affidabilità conta molto più dei punteggi nei benchmark.

| Modello | Prezzo (per M token) | Ideale Per |
|---------|---------------------|------------|
| GPT-5.4 (≤272K) | $2.50 / $15 output | Agenti in produzione, coding, workflow documentali |
| GPT-5.4 Pro | $30 / $180 output | Analisi approfondita, ragionamento scientifico |
| GPT-5.4 Mini | Economico | Classificazione, estrazione, chiamate leggere a strumenti |

La mossa intelligente è una strategia di routing: GPT-5.4 Mini gestisce il lavoro ad alto volume e bassa latenza mentre GPT-5.4 si occupa delle richieste con ragionamento pesante.

## L'SDK è finalmente stabile

L'SDK `azure-ai-projects` ha rilasciato versioni stabili in tutti i linguaggi — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0, e .NET 2.0.0 (1 aprile). La dipendenza da `azure-ai-agents` è sparita — tutto vive sotto `AIProjectClient`. Installate con `pip install azure-ai-projects` e il pacchetto include `openai` e `azure-identity` come dipendenze dirette.

Per gli sviluppatori .NET, questo significa un singolo pacchetto NuGet per l'intera superficie di Foundry. Basta destreggiarsi tra SDK di agenti separati.

## Fireworks AI porta i modelli aperti su Azure

Forse l'aggiunta più interessante dal punto di vista architetturale: Fireworks AI elabora oltre 13 trilioni di token al giorno a ~180K richieste/secondo, ora disponibile tramite Foundry. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5, e MiniMax M2.5 al lancio.

La vera storia è il **bring-your-own-weights** — caricate pesi quantizzati o fine-tunati da qualsiasi luogo senza cambiare lo stack di serving. Deploy tramite serverless pay-per-token o throughput provisionato.

## Altri punti salienti

- **Phi-4 Reasoning Vision 15B** — ragionamento multimodale per grafici, diagrammi e layout di documenti
- **Evaluations GA** — valutatori pronti all'uso con monitoraggio continuo della produzione integrato in Azure Monitor
- **Priority Processing** (Preview) — corsia di calcolo dedicata per carichi di lavoro sensibili alla latenza
- **Voice Live** — runtime voce-a-voce che si connette direttamente agli agenti Foundry
- **Tracing GA** — ispezione end-to-end delle tracce degli agenti con ordinamento e filtraggio
- **Deprecazione di PromptFlow** — migrazione a Microsoft Framework Workflows entro gennaio 2027

## Conclusione

Marzo 2026 è un punto di svolta per Foundry. Agent Service GA, SDK stabili in tutti i linguaggi, GPT-5.4 per agenti di produzione affidabili, e inferenza di modelli aperti via Fireworks AI — la piattaforma è pronta per carichi di lavoro seri.

Leggete il [riepilogo completo](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) e [create il vostro primo agente](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) per iniziare.
