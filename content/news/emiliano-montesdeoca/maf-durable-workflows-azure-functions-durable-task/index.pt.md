---
title: "Workflows Duráveis no Microsoft Agent Framework: De In-Memory ao Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "O modelo de programação de workflows do MAF agora suporta execução durável apoiada pelo Durable Task — veja como construir workflows de agentes compostos que sobrevivem a reinicializações de processos e escalam no Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Um dos pontos problemáticos com os primeiros workflows de agentes de IA: eles são frágeis. Um workflow multi-etapas de longa duração vinculado a um único processo significa que reinicialização do processo = estado perdido. Para demos simples está bem. Para cargas de trabalho em produção não está.

O modelo de programação de workflows do Microsoft Agent Framework agora suporta **execução durável**, apoiada pelo framework Durable Task, com hospedagem no Azure Functions. Aqui está como o modelo de programação funciona e por que a história de durabilidade importa.

## Os Blocos de Construção Fundamentais

**Executors** são a unidade fundamental de trabalho. Cada um é tipado — pega uma entrada específica e produz uma saída específica:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // buscar o pedido, retorná-lo
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Workflows** conectam executors em grafos direcionados usando um builder fluente. O framework cuida da execução, do fluxo de dados entre os passos e da propagação de erros.

Você pode modelar:
- Cadeias sequenciais (passo A → passo B → passo C)
- Fan-out/fan-in paralelo (executar agentes A, B, C em paralelo, agregar resultados)
- Ramificação condicional
- Aprovações de humano no ciclo (pausar workflow, esperar sinal externo)

## O Runner In-Memory para Desenvolvimento Local

Começar é rápido:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

O pacote principal inclui um runner leve em processo. Sem dependências externas, sem banco de dados, sem recursos Azure. Funciona muito bem para desenvolvimento local e testes unitários.

## Adicionando Durabilidade com Durable Task

Quando um workflow precisa sobreviver a reinicializações de processo — porque é de longa duração, porque tem passos de humano no ciclo, porque se distribui em muitas chamadas de agentes em paralelo — o runner in-memory não é suficiente.

A integração Durable Task do MAF armazena o estado do workflow no Azure Storage. Se o processo for reiniciado, o workflow retoma de onde parou. O modelo de programação permanece o mesmo; você apenas troca o runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Os mesmos executors, o mesmo grafo de workflow — apoiado por estado durável.

## Hospedagem no Azure Functions

A terceira camada é a hospedagem no Azure Functions. Seu workflow se torna um aplicativo Function: acione o workflow via um endpoint HTTP, e o runtime durável cuida do escalonamento, estado e confiabilidade.

Isso significa que um workflow multi-agente com chamadas paralelas, ramos condicionais e aprovações humanas pode escalar em um ambiente Functions serverless sem gerenciamento de estado personalizado.

## Por Que Isso Importa

A combinação é significativa para sistemas de IA reais:

- **Chamadas de agentes em paralelo** — distribuir para múltiplos agentes especializados simultaneamente sem bloqueio, agregar resultados quando todos concluírem
- **Processos de longa duração** — workflows que envolvem aprovação humana ou eventos externos podem pausar e retomar ao longo de horas ou dias
- **Escalonamento** — Azure Functions escala a execução horizontalmente; o framework Durable Task gerencia a coordenação do estado paralelo

Se você está construindo workflows MAF além de demos locais simples, este é o caminho para execução de qualidade produção.

Post original: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
