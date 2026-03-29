---
title: "Foundry Agent Service è GA: Cosa conta davvero per chi costruisce agenti .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Il Foundry Agent Service di Microsoft è appena andato in GA con networking privato, Voice Live, valutazioni di produzione e un runtime multi-modello aperto. Ecco cosa devi sapere."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Siamo onesti — costruire un prototipo di agente IA è la parte facile. La parte difficile è tutto quello che viene dopo: metterlo in produzione con un adeguato isolamento di rete, eseguire valutazioni che significhino davvero qualcosa, gestire i requisiti di conformità e non rompere nulla alle 2 di notte.

Il [Foundry Agent Service è appena andato in GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), e questo rilascio è focalizzato come un laser su quel gap del "tutto quello che viene dopo".

## Costruito sulla Responses API

Il titolo: il Foundry Agent Service di nuova generazione è costruito sulla OpenAI Responses API. Se stai già costruendo con quel wire protocol, migrare a Foundry richiede modifiche minime al codice. Cosa guadagni: sicurezza enterprise, networking privato, RBAC Entra, tracing completo e valutazione — sopra la tua logica di agente esistente.

L'architettura è intenzionalmente aperta. Non sei vincolato a un provider di modelli o a un framework di orchestrazione. Usa DeepSeek per la pianificazione, OpenAI per la generazione, LangGraph per l'orchestrazione — il runtime gestisce il livello di consistenza.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> Se vieni dal pacchetto `azure-ai-agents`, gli agenti sono ora operazioni di prima classe su `AIProjectClient` in `azure-ai-projects`. Rimuovi la dipendenza standalone e usa `get_openai_client()` per gestire le risposte.

## Networking privato: il bloccante enterprise rimosso

Questa è la funzionalità che sblocca l'adozione enterprise. Foundry ora supporta networking privato completo end-to-end con BYO VNet:

- **Nessun egress pubblico** — il traffico dell'agente non tocca mai internet pubblico
- **Iniezione di container/subnet** nella tua rete per comunicazione locale
- **Connettività degli strumenti inclusa** — server MCP, Azure AI Search, agenti dati Fabric operano tutti su percorsi privati

L'ultimo punto è critico. Non sono solo le chiamate di inferenza a restare private — ogni invocazione di strumento e chiamata di retrieval resta anch'essa all'interno del perimetro della tua rete. Per i team che operano sotto policy di classificazione dei dati che vietano il routing esterno, questo era ciò che mancava.

## Autenticazione MCP fatta bene

Le connessioni ai server MCP ora supportano l'intero spettro di pattern di autenticazione:

| Metodo di auth | Quando usarlo |
|----------------|---------------|
| Basato su chiave | Accesso condiviso semplice per strumenti interni all'organizzazione |
| Entra Agent Identity | Servizio a servizio; l'agente si autentica come se stesso |
| Entra Managed Identity | Isolamento per progetto; nessuna gestione delle credenziali |
| OAuth Identity Passthrough | Accesso delegato dall'utente; l'agente agisce per conto degli utenti |

OAuth Identity Passthrough è quello interessante. Quando gli utenti devono concedere a un agente l'accesso ai propri dati personali — il loro OneDrive, la loro organizzazione Salesforce, un'API SaaS con scope per utente — l'agente agisce per loro conto con flussi OAuth standard. Nessuna identità di sistema condivisa che finge di essere tutti.

## Voice Live: voce a voce senza l'idraulica

Aggiungere la voce a un agente significava unire STT, LLM e TTS — tre servizi, tre hop di latenza, tre superfici di fatturazione, tutto sincronizzato a mano. **Voice Live** collassa tutto in una singola API gestita con:

- Rilevamento semantico dell'attività vocale e del fine turno (capisce il significato, non solo il silenzio)
- Soppressione del rumore e cancellazione dell'eco lato server
- Supporto barge-in (gli utenti possono interrompere a metà risposta)

Le interazioni vocali passano attraverso lo stesso runtime dell'agente del testo. Stessi valutatori, stesse tracce, stessa visibilità dei costi. Per supporto clienti, servizio sul campo o scenari di accessibilità, questo sostituisce ciò che prima richiedeva una pipeline audio personalizzata.

## Valutazioni: da checkbox a monitoraggio continuo

Qui è dove Foundry diventa serio sulla qualità in produzione. Il sistema di valutazione ora ha tre livelli:

1. **Valutatori pronti all'uso** — coerenza, rilevanza, fondatezza, qualità del retrieval, sicurezza. Connetti a un dataset o al traffico live e ottieni punteggi.

2. **Valutatori personalizzati** — codifica la tua logica di business, standard di tono e regole di conformità specifiche del dominio.

3. **Valutazione continua** — Foundry campiona il traffico di produzione live, esegue la tua suite di valutatori e mostra i risultati nei dashboard. Imposta alert di Azure Monitor per quando la fondatezza cala o le soglie di sicurezza vengono superate.

Tutto viene pubblicato in Azure Monitor Application Insights. Qualità dell'agente, salute dell'infrastruttura, costi e telemetria dell'applicazione — tutto in un unico posto.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Sei nuove regioni per agenti ospitati

Gli agenti ospitati sono ora disponibili in East US, North Central US, Sweden Central, Southeast Asia, Japan East e altre. Questo conta per i requisiti di residenza dei dati e per comprimere la latenza quando il tuo agente gira vicino alle sue fonti dati.

## Perché è importante per gli sviluppatori .NET

Anche se gli esempi di codice nell'annuncio GA sono Python-first, l'infrastruttura sottostante è language-agnostic — e l'SDK .NET per `azure-ai-projects` segue gli stessi pattern. La Responses API, il framework di valutazione, il networking privato, l'auth MCP — tutto questo è disponibile da .NET.

Se stavi aspettando che gli agenti IA passassero da "demo cool" a "posso davvero consegnare questo al lavoro", questo rilascio GA è il segnale. Networking privato, autenticazione adeguata, valutazione continua e monitoraggio di produzione sono i pezzi che mancavano.

## Per concludere

Foundry Agent Service è disponibile ora. Installa l'SDK, apri [il portale](https://ai.azure.com) e inizia a costruire. La [guida quickstart](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) ti porta da zero a un agente funzionante in pochi minuti.

Per il deep-dive tecnico completo con tutti gli esempi di codice, consulta l'[annuncio GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
