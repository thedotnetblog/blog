---
title: "Dove dovresti ospitare i tuoi agenti IA su Azure? Una guida decisionale pratica"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure offre sei modi per ospitare agenti IA — dai container grezzi ai Foundry Hosted Agents completamente gestiti. Ecco come scegliere quello giusto per il tuo workload .NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "azure-ai-agent-hosting-options-guide.md" >}}).*

Se stai costruendo agenti IA con .NET in questo momento, probabilmente hai notato qualcosa: ci sono *molti* modi per ospitarli su Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — e tutti sembrano ragionevoli finché non devi effettivamente sceglierne uno. Microsoft ha appena pubblicato una [guida completa all'hosting di agenti IA su Azure](https://devblogs.microsoft.com/all-things-azure/hostedagent/) che chiarisce tutto, e voglio analizzarla dalla prospettiva pratica di uno sviluppatore .NET.

## Le sei opzioni a colpo d'occhio

Ecco come riassumerei il panorama:

| Opzione | Ideale per | Gestisci tu |
|---------|-----------|-------------|
| **Container Apps** | Controllo totale dei container senza complessità K8s | Osservabilità, stato, ciclo di vita |
| **AKS** | Compliance aziendale, multi-cluster, networking personalizzato | Tutto (è quello il punto) |
| **Azure Functions** | Task di agenti event-driven e di breve durata | Quasi niente — serverless vero |
| **App Service** | Agenti HTTP semplici, traffico prevedibile | Deploy, config di scaling |
| **Foundry Agents** | Agenti senza codice via portale/SDK | Quasi niente |
| **Foundry Hosted Agents** | Agenti con framework personalizzato e infra gestita | Solo il tuo codice agente |

Le prime quattro sono compute general-purpose — *puoi* eseguire agenti su di esse, ma non sono state progettate per quello. Le ultime due sono native per agenti: comprendono conversazioni, chiamate a strumenti e cicli di vita degli agenti come concetti di prima classe.

## Foundry Hosted Agents — il punto ideale per sviluppatori .NET di agenti

Questo è ciò che ha catturato la mia attenzione. I Foundry Hosted Agents si posizionano proprio nel mezzo: ottieni la flessibilità di eseguire il tuo codice (Semantic Kernel, Agent Framework, LangGraph — qualsiasi cosa) ma la piattaforma gestisce infrastruttura, osservabilità e gestione delle conversazioni.

Il pezzo chiave è l'**Hosting Adapter** — un sottile livello di astrazione che collega il tuo framework di agenti alla piattaforma Foundry. Per Microsoft Agent Framework, appare così:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Questa è tutta la tua storia di hosting. L'adapter gestisce traduzione di protocolli, streaming via server-sent events, cronologia delle conversazioni e tracing OpenTelemetry — tutto automaticamente. Nessun middleware personalizzato, nessun plumbing manuale.

## Il deploy è genuinamente semplice

Ho fatto deploy di agenti su Container Apps prima e funziona, ma finisci per scrivere molto codice di collegamento per gestione dello stato e osservabilità. Con Hosted Agents e `azd`, il deploy è:

```bash
# Installare l'estensione agente IA
azd ext install azure.ai.agents

# Inizializzare da un template
azd ai agent init

# Costruire, pushare, fare deploy — fatto
azd up
```

Quel singolo `azd up` costruisce il tuo container, lo pusha su ACR, provisiona il progetto Foundry, fa deploy degli endpoint del modello e avvia il tuo agente. Cinque passaggi condensati in un solo comando.

## Gestione conversazioni integrata

Questa è la parte che fa risparmiare più tempo in produzione. Invece di costruire il tuo store di stato delle conversazioni, gli Hosted Agents lo gestiscono nativamente:

```python
# Creare una conversazione persistente
conversation = openai_client.conversations.create()

# Primo turno
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Secondo turno — il contesto è preservato
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Niente Redis. Niente session store Cosmos DB. Niente middleware personalizzato per la serializzazione dei messaggi. La piattaforma semplicemente se ne occupa.

## Il mio framework decisionale

Dopo aver esaminato tutte e sei le opzioni, ecco il mio modello mentale rapido:

1. **Hai bisogno di zero infrastruttura?** → Foundry Agents (portale/SDK, niente container)
2. **Hai codice agente personalizzato ma vuoi hosting gestito?** → Foundry Hosted Agents
3. **Hai bisogno di task agente event-driven e di breve durata?** → Azure Functions
4. **Hai bisogno di massimo controllo dei container senza K8s?** → Container Apps
5. **Hai bisogno di compliance rigorosa e multi-cluster?** → AKS
6. **Hai un agente HTTP semplice con traffico prevedibile?** → App Service

Per la maggior parte degli sviluppatori .NET che costruiscono con Semantic Kernel o Microsoft Agent Framework, Hosted Agents è probabilmente il punto di partenza giusto. Ottieni scale-to-zero, OpenTelemetry integrato, gestione conversazioni e flessibilità di framework — senza gestire Kubernetes o montare il tuo stack di osservabilità.

## Per concludere

Il panorama dell'hosting di agenti su Azure sta maturando velocemente. Se stai iniziando un nuovo progetto di agente IA oggi, considererei seriamente Foundry Hosted Agents prima di ricorrere a Container Apps o AKS per abitudine. L'infrastruttura gestita fa risparmiare tempo reale, e il pattern hosting adapter ti permette di mantenere la tua scelta di framework.

Dai un'occhiata alla [guida completa di Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) e al [repo Foundry Samples](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) per esempi funzionanti.
