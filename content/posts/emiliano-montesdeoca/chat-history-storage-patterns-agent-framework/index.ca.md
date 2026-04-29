---
title: "On Recorda les Coses el teu Agent? Guia Pràctica sobre l'Emmagatzematge de l'Historial de Xat"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Gestionat pel servei o pel client? Lineal o amb bifurcacions? La decisió arquitectònica que defineix el que el teu agent IA pot fer realment."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Quan construeixes un agent IA, dediques la major part de la teva energia al model, les eines i els prompts. La pregunta de *on viu l'historial de conversa* sembla un detall d'implementació — però és una de les decisions arquitectòniques més importants que prendràs.

Determina si els usuaris poden bifurcar converses, desfer respostes, reprendre sessions després d'un reinici, i si les teves dades surten mai de la teva infraestructura. L'[equip d'Agent Framework ha publicat una anàlisi en profunditat](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Dos patrons fonamentals

**Gestionat pel servei**: el servei d'IA emmagatzema l'estat de la conversa. La teva app manté una referència i el servei inclou automàticament l'historial rellevant en cada sol·licitud.

**Gestionat pel client**: la teva app manté l'historial complet i envia missatges rellevants amb cada sol·licitud. El servei no té estat. Controles tot.

## Com Agent Framework abstreu això

```csharp
// C# — funciona igual independentment del proveïdor
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Em dic Alice.", session);
var second = await agent.RunAsync("Quin és el meu nom?", session);
```

```python
# Python
session = agent.create_session()
first = await agent.run("Em dic Alice.", session=session)
second = await agent.run("Quin és el meu nom?", session=session)
```

## Referència ràpida de proveïdors

| Proveïdor | Emmagatzematge | Model | Compactació |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Client | N/A | Tu |
| Foundry Agent Service | Servei | Lineal | Servei |
| Responses API (per defecte) | Servei | Bifurcació | Servei |
| Anthropic Claude, Ollama | Client | N/A | Tu |

Llegeix el [post complet](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) per a l'arbre de decisions complet.
