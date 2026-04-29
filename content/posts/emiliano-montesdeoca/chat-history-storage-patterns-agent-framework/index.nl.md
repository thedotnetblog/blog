---
title: "Waar Onthoudt uw Agent Dingen? Een Praktische Gids voor Chat-geschiedenis Opslag"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Door de service of de client beheerd? Lineair of vertakkend? De architectuurbeslissing die bepaalt wat uw AI-agent echt kan doen — met codevoorbeelden in C# en Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Dit bericht is automatisch vertaald. Klik [hier]({{< ref "index.md" >}}) voor de originele versie.*

Wanneer u een AI-agent bouwt, besteedt u het grootste deel van uw energie aan het model, de tools en de prompts. De vraag *waar de conversatiegeschiedenis leeft* lijkt een implementatiedetail — maar het is een van de belangrijkste architectuurbeslissingen die u zult nemen.

Het bepaalt of gebruikers gesprekken kunnen vertakken, antwoorden ongedaan kunnen maken, sessies na een herstart kunnen hervatten en of uw gegevens ooit uw infrastructuur verlaten. Het [Agent Framework-team heeft een diepgaande analyse gepubliceerd](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Twee fundamentele patronen

**Door de service beheerd**: de AI-service slaat de conversatiestatus op. Uw app bewaart een referentie en de service voegt automatisch de relevante geschiedenis toe aan elk verzoek.

**Door de client beheerd**: uw app behoudt de volledige geschiedenis en stuurt relevante berichten met elk verzoek. De service is stateless. U beheert alles.

## Hoe Agent Framework dit abstraheert

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Mijn naam is Alice.", session);
var second = await agent.RunAsync("Wat is mijn naam?", session);
```

```python
session = agent.create_session()
first = await agent.run("Mijn naam is Alice.", session=session)
second = await agent.run("Wat is mijn naam?", session=session)
```

## Snelle referentie van providers

| Provider | Opslag | Model | Comprimering |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Client | N/A | U |
| Foundry Agent Service | Service | Lineair | Service |
| Responses API (standaard) | Service | Vertakkend | Service |
| Anthropic Claude, Ollama | Client | N/A | U |

## Hoe te kiezen

1. **Vertakking of "ongedaan maken" nodig?** → Responses API door service beheerd
2. **Gegevenssouvereiniteit nodig?** → Door client beheerd met database-backend
3. **Eenvoudige chatbot?** → Lineair door service beheerd is prima

Lees het [volledige bericht](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) voor de volledige beslissingsboom.
