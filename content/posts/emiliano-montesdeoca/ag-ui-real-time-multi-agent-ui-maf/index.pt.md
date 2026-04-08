---
title: "Construindo UIs Multi-Agente em Tempo Real Que Não Parecem uma Caixa Preta"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "AG-UI e Microsoft Agent Framework se unem para dar aos fluxos multi-agente um frontend de verdade — com streaming em tempo real, aprovações humanas e visibilidade total do que seus agentes estão fazendo."
tags:
  - agent-framework
  - ai
  - ag-ui
  - multi-agent
  - azure
  - sse
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "ag-ui-real-time-multi-agent-ui-maf" >}}).*

A questão com sistemas multi-agente é a seguinte: eles ficam incríveis nas demos. Três agentes passando trabalho entre si, resolvendo problemas, tomando decisões. Aí você tenta colocar na frente de usuários reais e... silêncio. Um indicador girando. Nenhuma ideia de qual agente está fazendo o quê ou por que o sistema pausou. Isso não é um produto — é um problema de confiança.

O time do Microsoft Agent Framework acabou de publicar um [tutorial fantástico](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) sobre como combinar fluxos MAF com [AG-UI](https://github.com/ag-ui-protocol/ag-ui), um protocolo aberto para transmitir eventos de execução de agentes para um frontend via Server-Sent Events. E sinceramente? Essa é a ponte que estava faltando.

## Por que isso importa para desenvolvedores .NET

Se você está construindo apps com IA, provavelmente já bateu nesse muro. Sua orquestração backend funciona perfeitamente — agentes passam tarefas entre si, ferramentas disparam, decisões são tomadas. Mas o frontend não faz ideia do que está acontecendo nos bastidores. AG-UI resolve isso definindo um protocolo padrão para transmitir eventos de agentes (pense em `RUN_STARTED`, `STEP_STARTED`, `TOOL_CALL_*`, `TEXT_MESSAGE_*`) diretamente para sua camada de UI via SSE.

A demo que construíram é um fluxo de suporte ao cliente com três agentes: um agente de triagem que roteia solicitações, um agente de reembolso que cuida de questões financeiras, e um agente de pedidos que gerencia substituições. Cada agente tem suas próprias ferramentas, e a topologia de handoff é definida explicitamente — nada de "descubra a partir do prompt".

## A topologia de handoff é a verdadeira estrela

O que me chamou a atenção é como o `HandoffBuilder` permite declarar um grafo dirigido de roteamento entre agentes:

```python
builder = HandoffBuilder(
    name="ag_ui_handoff_workflow_demo",
    participants=[triage, refund, order],
    termination_condition=termination_condition,
)

(
    builder
    .add_handoff(triage, [refund], description="Refunds, damaged-item claims...")
    .add_handoff(triage, [order], description="Replacement, exchange...")
    .add_handoff(refund, [order], description="Replacement logistics needed after refund.")
    .add_handoff(order, [triage], description="After replacement/shipping tasks complete.")
)
```

Cada `add_handoff` cria uma aresta dirigida com uma descrição em linguagem natural. O framework gera ferramentas de handoff para cada agente baseado nessa topologia. Então as decisões de roteamento são fundamentadas na sua estrutura de orquestração, não apenas no que o LLM resolve fazer. Isso é enorme para confiabilidade em produção.

## Human-in-the-loop que realmente funciona

A demo mostra dois padrões de interrupção que qualquer app de agentes do mundo real precisa:

**Interrupções de aprovação de ferramentas** — quando um agente chama uma ferramenta marcada com `approval_mode="always_require"`, o fluxo pausa e emite um evento. O frontend renderiza um modal de aprovação com o nome da ferramenta e seus argumentos. Sem loops de retry queimando tokens — apenas um fluxo limpo de pausa-aprovação-retomada.

**Interrupções de solicitação de informação** — quando um agente precisa de mais contexto do usuário (como um ID de pedido), ele pausa e pergunta. O frontend mostra a pergunta, o usuário responde, e a execução retoma exatamente de onde parou.

Ambos os padrões são transmitidos como eventos AG-UI padrão, então seu frontend não precisa de lógica personalizada por agente — simplesmente renderiza qualquer evento que chegue pela conexão SSE.

## Conectar tudo é surpreendentemente simples

A integração entre MAF e AG-UI é uma única chamada de função:

```python
from agent_framework.ag_ui import (
    AgentFrameworkWorkflow,
    add_agent_framework_fastapi_endpoint,
)

app = FastAPI()

demo_workflow = AgentFrameworkWorkflow(
    workflow_factory=lambda _thread_id: create_handoff_workflow(),
    name="ag_ui_handoff_workflow_demo",
)

add_agent_framework_fastapi_endpoint(
    app=app, agent=demo_workflow, path="/handoff_demo",
)
```

O `workflow_factory` cria um fluxo novo por thread, então cada conversa tem estado isolado. O endpoint cuida de toda a tubulação SSE automaticamente. Se você já usa FastAPI (ou pode adicioná-lo como uma camada leve), isso tem praticamente zero fricção.

## Minha opinião

Para nós desenvolvedores .NET, a pergunta imediata é: "Posso fazer isso em C#?" O Agent Framework está disponível para .NET e Python, e o protocolo AG-UI é agnóstico de linguagem (é apenas SSE). Então embora essa demo específica use Python e FastAPI, o padrão se traduz diretamente. Você poderia montar uma API mínima ASP.NET Core com endpoints SSE seguindo o mesmo schema de eventos AG-UI.

A conclusão mais importante é que UIs multi-agente estão se tornando uma preocupação de primeira classe, não algo deixado para depois. Se você está construindo qualquer coisa onde agentes interagem com humanos — suporte ao cliente, fluxos de aprovação, processamento de documentos — essa combinação de orquestração MAF e transparência AG-UI é o padrão a seguir.

## Concluindo

AG-UI + Microsoft Agent Framework te dá o melhor dos dois mundos: orquestração multi-agente robusta no backend e visibilidade em tempo real no frontend. Sem mais interações de agentes como caixas pretas.

Confira o [tutorial completo](https://devblogs.microsoft.com/agent-framework/ag-ui-multi-agent-workflow-demo/) e o [repositório do protocolo AG-UI](https://github.com/ag-ui-protocol/ag-ui) para se aprofundar.
