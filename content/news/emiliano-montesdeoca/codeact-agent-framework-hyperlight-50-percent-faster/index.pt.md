---
title: "CodeAct no Agent Framework: Como Reduzir a Latência do seu Agente pela Metade"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "O CodeAct colapsa cadeias de ferramentas de múltiplas etapas em um único bloco de código sandboxed — reduzindo a latência em 52% e o uso de tokens em 64%. O que isso significa para os seus agentes e quando usá-lo."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Existe aquele momento em todo projeto de agentes em que você olha para o trace e pensa: "por que isso está demorando tanto?" O modelo está ótimo. As ferramentas funcionam. Mas há sete round trips para obter um resultado que poderia ser calculado de uma só vez.

Esse é exatamente o problema que o CodeAct resolve — e a [equipe do Agent Framework acabou de lançar suporte alpha](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) via o novo pacote `agent-framework-hyperlight`.

## O que é CodeAct?

O [padrão CodeAct](https://arxiv.org/abs/2402.01030) é elegantemente simples: em vez de dar ao modelo uma lista de ferramentas para chamar uma por uma, você dá a ele uma única ferramenta `execute_code` e deixa-o expressar o *plano completo* como um curto programa Python. O agente escreve o código uma vez, o sandbox o executa, e você recebe de volta um único resultado consolidado.

| Fiação | Tempo | Tokens |
|--------|------|--------|
| Tradicional | 27,81s | 6.890 |
| CodeAct | 13,23s | 2.489 |
| **Melhoria** | **52,4%** | **63,9%** |

## A peça de segurança: Micro-VMs do Hyperlight

O pacote `agent-framework-hyperlight` usa micro-VMs do [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Cada chamada `execute_code` obtém sua própria micro-VM recém-criada. A inicialização é medida em milissegundos. O isolamento é essencialmente gratuito.

Suas ferramentas continuam sendo executadas no host. O *código de cola* gerado pelo modelo é executado no sandbox. Essa é a divisão correta.

## Configuração mínima

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## Quando usar o CodeAct (e quando não usar)

**Use o CodeAct quando:**
- A tarefa encadeia muitas chamadas pequenas de ferramentas (lookups, joins, cálculos)
- A latência e o custo de tokens importam
- Você quer isolamento forte por chamada no código gerado pelo modelo

**Fique com o tool-calling tradicional quando:**
- O agente só faz uma ou duas chamadas de ferramentas por turno
- Cada chamada tem efeitos colaterais a serem aprovados individualmente
- As descrições de ferramentas são esparsas ou ambíguas

## Experimente agora

```bash
pip install agent-framework-hyperlight --pre
```

Confira o [post completo no blog do Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) para uma cobertura mais profunda.
