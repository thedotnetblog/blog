---
title: "Onde seu Agente se Lembra das Coisas? Guia Prático de Armazenamento do Histórico de Chat"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Gerenciado pelo serviço ou pelo cliente? Linear ou ramificável? A decisão arquitetural que molda o que seu agente IA pode realmente fazer — com exemplos de código em C# e Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Ao criar um agente IA, você gasta a maior parte da energia no modelo, nas ferramentas e nos prompts. A pergunta de *onde vive o histórico de conversa* parece um detalhe de implementação — mas é uma das decisões arquiteturais mais importantes que você tomará.

Ela determina se usuários podem bifurcar conversas, desfazer respostas, retomar sessões após uma reinicialização e se seus dados saem da sua infraestrutura. A [equipe do Agent Framework publicou uma análise aprofundada](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Dois padrões fundamentais

**Gerenciado pelo serviço**: o serviço IA armazena o estado da conversa. Seu app mantém uma referência e o serviço inclui automaticamente o histórico relevante em cada requisição.

**Gerenciado pelo cliente**: seu app mantém o histórico completo e envia mensagens relevantes com cada requisição. O serviço é stateless. Você controla tudo.

## Como o Agent Framework abstrai isso

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Meu nome é Alice.", session);
var second = await agent.RunAsync("Qual é o meu nome?", session);
```

```python
session = agent.create_session()
first = await agent.run("Meu nome é Alice.", session=session)
second = await agent.run("Qual é o meu nome?", session=session)
```

## Referência rápida de provedores

| Provedor | Armazenamento | Modelo | Compactação |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Cliente | N/A | Você |
| Foundry Agent Service | Serviço | Linear | Serviço |
| Responses API (padrão) | Serviço | Ramificável | Serviço |
| Anthropic Claude, Ollama | Cliente | N/A | Você |

## Como escolher

1. **Precisa de ramificação ou "desfazer"?** → Responses API gerenciado pelo serviço
2. **Precisa de soberania de dados?** → Gerenciado pelo cliente com provedor de banco de dados
3. **É um chatbot simples?** → Gerenciado pelo serviço linear está ótimo

Leia o [post completo](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) para a árvore de decisão completa.
