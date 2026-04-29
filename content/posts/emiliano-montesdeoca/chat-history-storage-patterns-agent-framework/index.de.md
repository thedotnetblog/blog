---
title: "Wo Erinnert sich dein Agent an Dinge? Ein Praxisleitfaden zur Chat-Verlauf-Speicherung"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Service-managed oder client-managed? Linear oder verzweigend? Die Architekturentscheidung, die bestimmt, was dein KI-Agent wirklich tun kann — mit Code-Beispielen in C# und Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Beim Aufbau eines KI-Agenten investierst du die meiste Energie in Modell, Tools und Prompts. Die Frage, *wo der Gesprächsverlauf lebt*, scheint ein Implementierungsdetail — ist aber eine der wichtigsten Architekturentscheidungen, die du treffen wirst.

Sie bestimmt, ob Nutzer Gespräche verzweigen, Antworten rückgängig machen, Sitzungen nach einem Neustart fortsetzen können und ob deine Daten deine Infrastruktur jemals verlassen.

## Zwei grundlegende Muster

**Service-managed**: Der KI-Dienst speichert den Gesprächszustand. Deine App hält eine Referenz und der Dienst fügt automatisch den relevanten Verlauf in jede Anfrage ein.

**Client-managed**: Deine App verwaltet den vollständigen Verlauf und sendet relevante Nachrichten mit jeder Anfrage. Der Dienst ist zustandslos. Du kontrollierst alles.

## Wie Agent Framework das abstrahiert

```csharp
// C# — funktioniert gleich, unabhängig vom Provider
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Mein Name ist Alice.", session);
var second = await agent.RunAsync("Wie ist mein Name?", session);
```

```python
# Python
session = agent.create_session()
first = await agent.run("Mein Name ist Alice.", session=session)
second = await agent.run("Wie ist mein Name?", session=session)
```

## Provider-Schnellreferenz

| Provider | Speicherort | Modell | Komprimierung |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Client | N/A | Du |
| Foundry Agent Service | Service | Linear | Service |
| Responses API (Standard) | Service | Verzweigend | Service |
| Anthropic Claude, Ollama | Client | N/A | Du |

## Wie du die Wahl triffst

1. **Brauchst du Verzweigung oder „Rückgängig"?** → Responses API service-managed
2. **Brauchst du vollständige Datensouveränität?** → Client-managed mit datenbankgestütztem Provider
3. **Ist es ein einfacher Chatbot?** → Service-managed linear reicht
4. **Brauchst du Portabilität zwischen Providern?** → Client-managed bietet Portabilität

Lies den [vollständigen Beitrag](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) für den vollständigen Entscheidungsbaum.
