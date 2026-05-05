---
title: "Respostas em segundo plano no Microsoft Agent Framework: chega de ansiedade com timeouts"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "O Microsoft Agent Framework agora permite descarregar tarefas de IA de longa duração com tokens de continuação. Veja como as respostas em segundo plano funcionam e por que importam para seus agentes .NET."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

Se você já construiu algo com modelos de raciocínio como o3 ou GPT-5.2, conhece a dor. Seu agente começa a pensar numa tarefa complexa, o cliente fica esperando, e em algum ponto entre "tá tudo bem" e "será que travou?" sua conexão expira por timeout. Todo aquele trabalho? Perdido.

O Microsoft Agent Framework acabou de lançar [respostas em segundo plano](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — e honestamente, essa é uma daquelas funcionalidades que deveria ter existido desde o primeiro dia.

## O problema com chamadas bloqueantes

Num padrão tradicional de requisição-resposta, seu cliente bloqueia até o agente terminar. Funciona bem para tarefas rápidas. Mas quando você pede a um modelo de raciocínio que faça pesquisa profunda, análise em múltiplas etapas, ou gere um relatório de 20 páginas? São minutos de tempo real. Durante essa janela:

- Conexões HTTP podem expirar
- Quedas de rede matam toda a operação
- Seu usuário fica olhando um spinner se perguntando se algo está acontecendo

Respostas em segundo plano invertem isso completamente.

## Como os tokens de continuação funcionam

Em vez de bloquear, você dispara a tarefa do agente e recebe um **token de continuação**. Pense nisso como um ticket de retirada numa oficina — você não fica parado no balcão esperando, volta quando está pronto.

O fluxo é direto:

1. Envie sua requisição com `AllowBackgroundResponses = true`
2. Se o agente suporta processamento em segundo plano, você recebe um token de continuação
3. Consulte no seu ritmo até o token retornar `null` — isso significa que o resultado está pronto

Aqui está a versão .NET:

```csharp
AIAgent agent = new AzureOpenAIClient(
    new Uri("https://<myresource>.openai.azure.com"),
    new DefaultAzureCredential())
    .GetResponsesClient("<deployment-name>")
    .AsAIAgent();

AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();

AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

// Consultar até completar
while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

Se o agente completa imediatamente (tarefas simples, modelos que não precisam de processamento em segundo plano), nenhum token de continuação é retornado. Seu código simplesmente funciona — sem tratamento especial necessário.

## Streaming com retomada: a verdadeira mágica

Polling é bom para cenários de disparar e esquecer, mas e quando você quer progresso em tempo real? Respostas em segundo plano também suportam streaming com retomada embutida.

Cada atualização do stream carrega seu próprio token de continuação. Se sua conexão cair no meio do stream, você retoma exatamente de onde parou:

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponseUpdate? latestUpdate = null;

await foreach (var update in agent.RunStreamingAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options))
{
    Console.Write(update.Text);
    latestUpdate = update;
    break; // Simular uma interrupção de rede
}

// Retomar exatamente de onde paramos
options.ContinuationToken = latestUpdate?.ContinuationToken;
await foreach (var update in agent.RunStreamingAsync(session, options))
{
    Console.Write(update.Text);
}
```

O agente continua processando no servidor independentemente do que aconteça com seu cliente. Isso é tolerância a falhas embutida sem que você escreva lógica de retry ou circuit breakers.

## Quando realmente usar isso

Nem toda chamada ao agente precisa de respostas em segundo plano. Para completações rápidas, você está adicionando complexidade sem razão. Mas aqui é onde elas brilham:

- **Tarefas de raciocínio complexo** — análise em múltiplas etapas, pesquisa profunda, qualquer coisa que faça um modelo de raciocínio realmente pensar
- **Geração de conteúdo longo** — relatórios detalhados, documentos de múltiplas partes, análises extensas
- **Redes pouco confiáveis** — clientes móveis, deployments no edge, VPNs corporativas instáveis
- **Padrões UX assíncronos** — envie uma tarefa, vá fazer outra coisa, volte para os resultados

Para nós desenvolvedores .NET construindo apps empresariais, esse último é particularmente interessante. Pense numa app Blazor onde um usuário solicita um relatório complexo — você dispara a tarefa do agente, mostra um indicador de progresso, e os deixa continuar trabalhando. Sem ginástica de WebSocket, sem infraestrutura de filas personalizada, apenas um token e um loop de polling.

## Para finalizar

Respostas em segundo plano estão disponíveis agora tanto em .NET quanto em Python através do Microsoft Agent Framework. Se você está construindo agentes que fazem algo mais complexo que simples Q&A, vale a pena adicionar isso ao seu toolkit. O padrão de token de continuação mantém as coisas simples enquanto resolve um problema de produção muito real.

Confira a [documentação completa](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) para a referência completa da API e mais exemplos.
