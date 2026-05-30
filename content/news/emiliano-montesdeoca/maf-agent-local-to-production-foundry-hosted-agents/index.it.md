---
title: "Il Tuo Agente MAF Locale Ha Appena Trovato Casa in Produzione"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents dà al tuo agente Microsoft Agent Framework identità, scaling, persistenza delle sessioni e osservabilità senza configurazione aggiuntiva. Ecco come si presenta in pratica."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Far funzionare un agente localmente è la parte divertente. La parte difficile è tutto ciò che viene dopo: distribuirlo senza impazzire, gestire le sessioni, configurare l'identità, collegare l'osservabilità. Di solito questo significa molta infrastruttura personalizzata.

Foundry Hosted Agents ha appena rimosso la maggior parte di quella infrastruttura per gli utenti di Microsoft Agent Framework (MAF).

## Cosa Fa Realmente Foundry Hosted Agents

Quando distribuisci un agente MAF in Foundry Hosted Agents, la piattaforma gestisce una lista sorprendentemente lunga di cose che altrimenti dovresti costruire tu stesso:

- **Scala a zero** — il tuo agente non costa nulla quando è inattivo e si riavvia automaticamente
- **Sandbox isolati per VM per sessione** — ogni sessione utente ottiene il proprio sandbox con persistenza del filesystem che sopravvive agli eventi di riduzione dello scale
- **Entra ID integrato** — ogni agente ottiene la propria identità per chiamare modelli Foundry, Toolbox e servizi Azure senza segreti nell'immagine
- **Deployment versionati** — ogni deployment è uno snapshot immutabile, con supporto per blue/green e canary rollout
- **Osservabilità senza configurazione** — `APPLICATIONINSIGHTS_CONNECTION_STRING` viene iniettato a runtime in modo che le tracce OpenTelemetry di MAF fluiscano automaticamente in App Insights

Quest'ultimo è genuinamente piacevole. Nessun cablaggio aggiuntivo, nessuna configurazione extra. Le tracce appaiono semplicemente.

## La Differenza nel Codice È Minima

Questo è ciò che apprezzo di più di questa integrazione. Non riscrivi il tuo agente. Lo avvolgi semplicemente:

**In .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**In Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

Tutto qui. La stessa logica che hai testato localmente è ciò che gira in produzione. La piattaforma la avvolge nell'infrastruttura di gestione delle sessioni, identità e scaling.

## Due Protocolli, Un Agente

Gli Hosted Agents supportano due stili di endpoint:

- **Responses** (`/responses`) — compatibile con OpenAI, gestisce la cronologia delle conversazioni e lo streaming. Buon default per agenti a forma di chat.
- **Invocations** (`/invocations`) — tu definisci lo schema richiesta/risposta. Buono per workflow non conversazionali.

Se stai costruendo qualcosa che assomiglia a una conversazione, inizia con Responses. Se stai costruendo un agente a forma di API che prende input strutturato e restituisce output strutturato, Invocations ti dà la flessibilità.

## Il Flusso di Deployment con `azd`

Quando esegui `azd up` con un agente MAF:

1. Crea opzionalmente un progetto Foundry e distribuisce un modello
2. Impacchetta il tuo codice e carica un'immagine su Azure Container Registry
3. Provvede compute dall'immagine ACR
4. Assegna un Entra ID dedicato all'agente
5. Espone un endpoint stabile (`https://{project_endpoint}/agents/{agent_name}`)
6. Gestisce tutto il resto da quel punto in poi

Le sessioni persistono per un massimo di 30 giorni. Il compute inattivo viene deprovisionato dopo 15 minuti e ripristinato trasparentemente alla successiva richiesta. Dal punto di vista dell'agente, nulla è cambiato.

## Conclusione

La distanza tra "funzionante localmente" e "in esecuzione in produzione" è stata storicamente lunga e dolorosa per gli agenti AI. Foundry Hosted Agents + MAF riduce significativamente questo divario. Se hai già un agente locale costruito con Agent Framework, vale la pena provarlo oggi.

Il team dice che GA arriverà presto — questo è attualmente in preview. Consulta i [documenti di integrazione MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) e gli [esempi .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) per iniziare.

Articolo originale: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
