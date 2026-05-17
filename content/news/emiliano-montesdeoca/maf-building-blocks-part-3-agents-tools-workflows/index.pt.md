---
title: "Microsoft Agent Framework Parte 3: De Ferramentas a Workflows — As Peças se Encaixam"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "A terceira parte da série Building Blocks for AI no .NET cobre o Microsoft Agent Framework — de agentes simples com ferramentas a workflows multiagente com memória. Isso é o que realmente importa."
tags:
  - .NET
  - AI
  - Microsoft Agent Framework
  - C#
  - AI Agents
  - Workflows
  - Tool Calling
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Se você tem seguido a série Building Blocks for AI no .NET, sabe que a Parte 1 nos deu `IChatClient` (a interface universal de modelos) e a Parte 2 nos deu `Microsoft.Extensions.VectorData` (busca semântica e RAG). Ambos são fundamentais e úteis por si só. Mas é aqui que tudo começa a se conectar.

A Parte 3 é sobre o [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) — e honestamente, é a peça que eu estava esperando ver chegar no .NET. A versão 1.0 foi lançada em abril. A API é estável. É hora de construir agentes de verdade.

## O que é um Agente (vs. um Chatbot)

Antes de mergulhar no código, vamos esclarecer essa distinção. Um chatbot recebe input, chama um modelo, retorna output. Loop simples.

Um agente tem *autonomia*. Ele pode raciocinar sobre uma tarefa, decidir quais ferramentas usar, chamá-las, avaliar resultados e decidir o que fazer a seguir — tudo sem que você escreva lógica passo a passo para cada cenário. Você dá a ele ferramentas e instruções, e ele cuida da orquestração.

Pense assim: `IChatClient` é como ter uma conversa. Um agente é como delegar uma lista de tarefas para alguém.

## Seu Primeiro Agente em 10 Linhas

```bash
dotnet add package Microsoft.Agents.AI
```

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri(endpoint),
    new DefaultAzureCredential())
    .GetChatClient(deploymentName)
    .AsAIAgent(
        instructions: "You are good at telling jokes.",
        name: "Joker");

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate."));
```

O método de extensão `.AsAIAgent()` é a ponte. Mesmo padrão que `.AsIChatClient()` do MEAI — envolve o SDK do provedor em uma abstração estável. Funciona com Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry ou modelos locais.

Streaming também funciona:

```csharp
await foreach (var update in agent.RunStreamingAsync("Tell me a joke about a pirate."))
{
    Console.Write(update);
}
```

## Dando Ferramentas ao Agente

É aqui que os agentes param de ser chatbots sofisticados. Ferramentas são funções que o modelo pode decidir chamar com base no que o usuário pede. Sem lógica de roteamento da sua parte — o modelo descobre por si mesmo.

```csharp
[Description("Get the weather for a given location.")]
static string GetWeather(
    [Description("The location to get the weather for.")] string location)
    => $"The weather in {location} is cloudy with a high of 15°C.";

AIAgent agent = chatClient.AsAIAgent(
    instructions: "You are a helpful assistant",
    tools: [AIFunctionFactory.Create(GetWeather)]);
```

Duas coisas a notar. Primeiro, `AIFunctionFactory` é do MEAI — a mesma factory de ferramentas que você usaria com um `IChatClient` normal. Se você já tem ferramentas definidas para cenários de chat, elas funcionam aqui também.

Segundo, os atributos `Description` importam muito. É como o modelo entende o que uma ferramenta faz e quando usá-la. Trate-os como documentação para sua IA, não para humanos.

## Sessões: Conversas com Memória Real

```csharp
AgentSession session = await agent.CreateSessionAsync();

Console.WriteLine(await agent.RunAsync("Tell me a joke about a pirate.", session));

Console.WriteLine(await agent.RunAsync(
    "Now add some emojis and tell it in the voice of a pirate's parrot.",
    session));
```

Sem sessão, cada chamada a `RunAsync` é stateless. Com sessão, o agente sabe a qual piada você está se referindo. `AgentSession` preserva o histórico de conversa entre os turnos.

Para serviços sem estado em produção, as sessões serializam de forma limpa:

```csharp
JsonElement sessionState = await agent.SerializeSessionAsync(session);
// ... armazene em algum lugar ...
var restoredSession = await agent.DeserializeSessionAsync(sessionState);
Console.WriteLine(await agent.RunAsync("What were we just talking about?", restoredSession));
```

Isso é crítico se seu agente roda em ambiente serverless ou com escalonamento horizontal.

## AIContextProvider: Memória Persistente Entre Sessões

Sessões preservam o histórico *dentro* de uma sessão. Mas e sobre conhecer coisas sobre um usuário entre sessões? `AIContextProvider` cuida disso.

Tem dois hooks:
- **`ProvideAIContextAsync`** — executa *antes* de cada interação, injeta contexto no agente
- **`StoreAIContextAsync`** — executa *depois* de cada interação, permite aprender e persistir

O padrão é elegante: você pode empilhar múltiplos providers — um para preferências do usuário, um para interações recentes, um que consulta seu store VectorData para documentos relevantes. Este último é exatamente o padrão RAG da Parte 2, agora executando automaticamente a cada chamada do agente.

## Workflows Multiagente

É aqui que o framework merece seu nome. Inclui um sistema de workflows baseado em grafos onde executors (agentes, funções, o que for) se conectam via arestas.

Alguns padrões suportados nativamente:

- **Sequencial**: A saída do Agente A alimenta o Agente B
- **Concorrente (fan-out/fan-in)**: Despacha para múltiplos agentes em paralelo, coleta resultados
- **Roteamento condicional**: Roteia trabalho para diferentes agentes com base na saída
- **Loops escritor-crítico**: Um agente escreve, outro avalia, loop até aprovação
- **Sub-workflows**: Compõe workflows hierarquicamente

Um exemplo de escritor-crítico:

```csharp
WorkflowBuilder builder = new(writerAgent);
builder
    .AddEdge(writerAgent, criticAgent)
    .AddEdge(criticAgent, writerAgent, condition: result => !result.IsApproved)
    .WithOutputFrom(criticAgent, condition: result => result.IsApproved);
var workflow = builder.Build();
```

Limpo, legível, e o roteamento baseado em condições significa que você não escreve a lógica do loop você mesmo.

## Human-in-the-Loop

Nem tudo deve rodar de forma completamente autônoma. Para operações sensíveis — escritas em banco de dados, transações financeiras, envio de comunicações — você quer que um humano aprove antes do agente executar.

O framework tem suporte integrado para isso via `FunctionApprovalRequestContent` e `FunctionApprovalResponseContent`. O agente propõe a chamada de ferramenta, seu código de aplicação a apresenta ao usuário, e a resposta determina se a execução prossegue.

Essa é a forma correta de pensar em agentes em ambientes corporativos: não completamente autônomos, mas *autonomia com guardrails*.

## O Quadro Completo

Se você der um passo atrás:

- **MEAI** te dá uma interface universal para qualquer modelo
- **VectorData** dá aos seus agentes acesso ao conhecimento da sua organização através de busca semântica
- **Agent Framework** orquestra tudo — usa `IChatClient` internamente, compõe com context providers, e coordena através de workflows

Cada peça foi projetada para se compor com as outras. Confira o [post original de Jeremy Likness](https://devblogs.microsoft.com/dotnet/microsoft-agent-framework-building-blocks-for-ai-part-3/) e o [repositório GitHub do Agent Framework](https://github.com/microsoft/agent-framework/tree/main/dotnet) para os exemplos completos.

## Conclusão

O post Parte 3 do Microsoft Agent Framework fecha o loop da série de building blocks. Para desenvolvedores .NET que querem construir agentes de IA — não apenas chatbots, mas agentes reais que usam ferramentas, lembram coisas e coordenam — este é o caminho.

O lançamento estável 1.0 significa que você pode construir isso em produção. Se você estava esperando para mergulhar no desenvolvimento de agentes em .NET, o momento é agora.
