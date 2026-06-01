---
title: "O Padrão Handoff: Quando Um Agente Não É Suficiente"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "O padrão de orquestração Handoff do Microsoft Agent Framework permite que os agentes decidam quem lida com o próximo turno — sem perder o contexto da conversa ou quebrar as regras de topologia."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

Em algum momento, todo sistema multi-agente supera um roteador simples. O primeiro sinal é geralmente quando um agente especialista precisa fazer uma pergunta de acompanhamento, ou percebe no meio do turno que outro agente deveria continuar. Um pipeline fixo falha aí. Um roteador de passagem única falha aí.

Exatamente para isso é que o padrão de orquestração Handoff no Microsoft Agent Framework foi projetado.

## Como Handoff Funciona

O desenvolvedor declara um grafo: aqui estão os agentes, aqui estão as arestas entre eles. O framework faz o resto — sintetiza uma ferramenta handoff por aresta de saída e a injeta em cada agente. Quando um agente decide passar o controle, ele chama a ferramenta. O framework aplica a topologia.

Três coisas tornam isso diferente de simplesmente fazer com que os agentes se chamem:

1. **Uma transcrição compartilhada** — o agente receptor vê o histórico completo da conversa. Sem começar do zero.
2. **Aplicação de topologia** — um agente só pode fazer handoff para destinos declarados. Bugs de roteamento são detectados no momento de criação, não em produção.
3. **Terminação natural** — quando o agente ativo termina seu turno sem chamar uma ferramenta de handoff, o fluxo de trabalho cede ao usuário. Sem polling, sem condições de saída explícitas.

## Um Exemplo Mínimo

Em .NET, construir um fluxo de trabalho handoff fica assim:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triagem pode enviar para qualquer especialista. Ambos os especialistas podem enviar de volta para triagem. O grafo é compatível com acíclico, mas suporta arestas de retorno quando você as precisa ("preciso de mais informações" → de volta à pesquisa).

## Quando Usar Handoff (e Quando Não)

Handoff é uma boa escolha quando:

- **A propriedade pode mudar no meio da conversa** — um agente pode perceber que é o especialista errado
- **Arestas de retorno importam** — você pode precisar revisitar um passo anterior sem reiniciar
- **As decisões de roteamento são difusas** — a decisão de fazer handoff é contextual e melhor tomada pelo modelo do que por predicados tipados

*Não* é a escolha certa quando:

- Seu pipeline é fixo e sequencial — use o fluxo de trabalho `Sequential` para isso
- Cada passo é independente — agentes compartilhando uma transcrição onde apenas um deles precisava dela é apenas ruído
- Você precisa de garantias rígidas de processamento — o não-determinismo do roteamento orientado por modelo não é o que você quer

## Arestas de Retorno e Human-in-the-Loop

Uma das formas mais interessantes que o Handoff permite são as arestas de retorno genuínas. Um agente pode decidir "não tenho informações suficientes" e rotear de volta para um passo de pesquisa, não com um loop codificado, mas porque o modelo decide que é a decisão certa.

As interações human-in-the-loop também se compõem naturalmente. Quando um especialista precisa de entrada do usuário, o fluxo de trabalho cede de volta ao usuário via o loop de turno padrão, coleta a resposta e retoma com contexto completo. O agente nunca perdeu a conversa.

## Conclusão

Handoff é um desses padrões que parece simples, mas permite muito uma vez que você o internaliza: roteamento descentralizado, contexto compartilhado, topologia aplicada, terminação natural. É o próximo passo certo quando seus agentes começam a dizer "na verdade, alguém mais deveria lidar com isso."

Leia o passo a passo completo no post original: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
