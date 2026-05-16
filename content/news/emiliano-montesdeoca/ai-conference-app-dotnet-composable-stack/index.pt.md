---
title: "Construindo um app de conferência com IA com a stack componível do .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "A Microsoft criou o ConferencePulse — um app Blazor para conferências ao vivo — combinando Microsoft.Extensions.AI, DataIngestion, VectorData, MCP e Agent Framework. Veja como as peças se encaixam."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[Construindo um app de conferência com IA com a stack componível do .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — A Microsoft criou o ConferencePulse, um app Blazor Server para sessões de conferência ao vivo, combinando cinco bibliotecas de extensão do .NET. Foi utilizado no MVP Summit.

## O que o ConferencePulse faz

O ConferencePulse é executado durante as sessões ao vivo e fornece: enquetes geradas por IA a partir do conteúdo da sessão, perguntas e respostas do público com um pipeline RAG que extrai de uma base de conhecimento ao vivo, insights gerados automaticamente e resumos de sessões produzidos por múltiplos agentes de IA concorrentes. A stack é .NET 10, Blazor Server, Aspire, dividida em cinco projetos: Web, Core, Ingestion, Agents, Mcp e AppHost.

## Microsoft.Extensions.AI: uma abstração para tudo

`IChatClient` é a abstração unificada — configura-se uma vez e a mesma interface funciona para Azure OpenAI, OpenAI, Anthropic ou qualquer outro provedor. Seis linhas para obter um cliente totalmente configurado com invocação de funções, rastreamento OpenTelemetry e middleware de logging:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

O mesmo `IChatClient` é reutilizado posteriormente para o passo de enriquecimento da ingestão de dados — sem necessidade de um cliente separado para isso.

## Pipeline de DataIngestion

O conteúdo da sessão flui por um pipeline: `MarkdownReader` → `HeaderChunker` (500 tokens, 50 tokens de sobreposição) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Os enriquecedores usam o mesmo `IChatClient` para gerar resumos e extrair palavras-chave antes da indexação. Perguntas do público, pares de perguntas e respostas e resultados de enquetes são ingeridos em tempo real à medida que a sessão avança — a base de conhecimento cresce durante a apresentação.

## VectorData: busca independente do provedor

`VectorStoreCollection.SearchAsync()` funciona da mesma forma independentemente de o backing store ser Qdrant ou Azure AI Search. A busca híbrida (vetor + texto completo) é suportada. O pipeline RAG para perguntas e respostas do público consulta esta coleção e obtém chunks relevantes para passar como contexto ao cliente de chat.

## MCP: conteúdo da sessão como ferramentas

O conteúdo da sessão é exposto via MCP para que qualquer cliente compatível com MCP possa acessá-lo. Tanto o servidor quanto o cliente estão implementados — o servidor expõe o conhecimento da sessão como ferramentas MCP, e o cliente permite chamar essas ferramentas de dentro do pipeline do agente.

## Agent Framework: resumo multi-agente em paralelo

O resumo da sessão é gerado por três agentes executados de forma concorrente — `PollSummaryAgent`, `QuestionSummaryAgent` e `InsightSummaryAgent` — e então mesclados. Isso utiliza o padrão de chat em grupo ou execução paralela do Microsoft Agent Framework. Cada agente lida com uma preocupação; o orquestrador mescla as saídas.

## O princípio de design

O post faz um ponto que vale a pena guardar: use a ferramenta mais simples que se encaixe. Chamadas diretas ao `IChatClient` para tarefas simples de geração. Chamada de ferramenta/função para extração de dados estruturados. Agentes completos apenas quando você precisa de raciocínio autônomo de múltiplos passos. A camada de bibliotecas impõe isso — você pode usar o `Microsoft.Extensions.AI` sem incluir o Agent Framework completo.

Consulte o [post completo](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) para a estrutura completa do projeto e links de código-fonte.
