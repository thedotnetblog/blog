---
title: "Dove il tuo Agente Ricorda le Cose? Guida Pratica all'Archiviazione della Cronologia Chat"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Gestito dal servizio o dal client? Lineare o ramificabile? La decisione architetturale che definisce cosa può fare davvero il tuo agente IA — con esempi di codice in C# e Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

Quando costruisci un agente IA, dedichi la maggior parte dell'energia al modello, agli strumenti e ai prompt. La domanda su *dove vive la cronologia della conversazione* sembra un dettaglio di implementazione — ma è una delle decisioni architetturali più importanti che prenderai.

Determina se gli utenti possono ramificare le conversazioni, annullare le risposte, riprendere le sessioni dopo un riavvio e se i tuoi dati escono mai dalla tua infrastruttura. Il [team di Agent Framework ha pubblicato un'analisi approfondita](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Due pattern fondamentali

**Gestito dal servizio**: il servizio IA archivia lo stato della conversazione. La tua app mantiene un riferimento e il servizio include automaticamente la cronologia rilevante in ogni richiesta.

**Gestito dal client**: la tua app mantiene la cronologia completa e invia messaggi rilevanti con ogni richiesta. Il servizio è stateless. Tu controlli tutto.

## Come Agent Framework astrae questo

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Mi chiamo Alice.", session);
var second = await agent.RunAsync("Come mi chiamo?", session);
```

```python
session = agent.create_session()
first = await agent.run("Mi chiamo Alice.", session=session)
second = await agent.run("Come mi chiamo?", session=session)
```

## Riferimento rapido ai provider

| Provider | Archiviazione | Modello | Compattazione |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Client | N/A | Tu |
| Foundry Agent Service | Servizio | Lineare | Servizio |
| Responses API (default) | Servizio | Ramificabile | Servizio |
| Anthropic Claude, Ollama | Client | N/A | Tu |

## Come scegliere

1. **Hai bisogno di ramificazione o "annulla"?** → Responses API gestito dal servizio
2. **Hai bisogno di sovranità dei dati?** → Gestito dal client con provider di database
3. **È un semplice chatbot?** → Gestito dal servizio lineare va benissimo

Leggi il [post completo](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) per l'albero decisionale completo.
