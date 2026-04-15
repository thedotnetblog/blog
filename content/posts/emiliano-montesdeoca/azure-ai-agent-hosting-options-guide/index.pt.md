---
title: "Onde hospedar seus agentes de IA no Azure? Um guia prático de decisão"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "O Azure oferece seis formas de hospedar agentes de IA — de containers brutos a Foundry Hosted Agents totalmente gerenciados. Veja como escolher a opção certa para sua carga de trabalho .NET."
tags:
  - azure
  - ai
  - agents
  - containers
  - microsoft-foundry
  - cloud-native
  - aks
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "azure-ai-agent-hosting-options-guide.md" >}}).*

Se você está construindo agentes de IA com .NET agora, provavelmente notou algo: existem *muitas* formas de hospedá-los no Azure. Container Apps, AKS, Functions, App Service, Foundry Agents, Foundry Hosted Agents — e todos parecem razoáveis até você precisar escolher um. A Microsoft acabou de publicar um [guia completo sobre hospedagem de agentes IA no Azure](https://devblogs.microsoft.com/all-things-azure/hostedagent/) que esclarece isso, e eu quero detalhar tudo pela perspectiva prática de um desenvolvedor .NET.

## As seis opções de relance

Aqui está como eu resumiria o cenário:

| Opção | Melhor para | Você gerencia |
|-------|------------|---------------|
| **Container Apps** | Controle total de containers sem complexidade K8s | Observabilidade, estado, ciclo de vida |
| **AKS** | Compliance empresarial, multi-cluster, rede customizada | Tudo (esse é o ponto) |
| **Azure Functions** | Tarefas de agentes curtas e orientadas a eventos | Quase nada — serverless real |
| **App Service** | Agentes HTTP simples, tráfego previsível | Deploy, config de scaling |
| **Foundry Agents** | Agentes sem código via portal/SDK | Quase nada |
| **Foundry Hosted Agents** | Agentes com framework customizado e infra gerenciada | Apenas seu código de agente |

As quatro primeiras são computação de propósito geral — você *pode* rodar agentes nelas, mas não foram projetadas para isso. As duas últimas são nativas de agentes: entendem conversas, chamadas de ferramentas e ciclos de vida de agentes como conceitos de primeira classe.

## Foundry Hosted Agents — o ponto ideal para desenvolvedores .NET de agentes

Isso foi o que chamou minha atenção. Foundry Hosted Agents ficam bem no meio: você tem a flexibilidade de rodar seu próprio código (Semantic Kernel, Agent Framework, LangGraph — o que for) mas a plataforma cuida da infraestrutura, observabilidade e gerenciamento de conversas.

A peça-chave é o **Hosting Adapter** — uma camada de abstração fina que conecta seu framework de agentes à plataforma Foundry. Para o Microsoft Agent Framework, fica assim:

```python
from azure.ai.agentserver.agentframework import from_agent_framework

agent = ChatAgent(
    chat_client=AzureAIAgentClient(...),
    instructions="You are a helpful assistant.",
    tools=[get_local_time],
)

if __name__ == "__main__":
    from_agent_framework(agent).run()
```

Essa é toda a sua história de hosting. O adapter cuida da tradução de protocolos, streaming via server-sent events, histórico de conversa e rastreamento OpenTelemetry — tudo automaticamente. Sem middleware customizado, sem encanamento manual.

## Deploy é genuinamente simples

Já fiz deploy de agentes no Container Apps antes e funciona, mas você acaba escrevendo muito código de cola para gerenciamento de estado e observabilidade. Com Hosted Agents e `azd`, o deploy é:

```bash
# Instalar a extensão de agente IA
azd ext install azure.ai.agents

# Inicializar a partir de um template
azd ai agent init

# Construir, enviar, fazer deploy — pronto
azd up
```

Esse único `azd up` constrói seu container, envia para o ACR, provisiona o projeto Foundry, faz deploy dos endpoints de modelo e inicia seu agente. Cinco etapas condensadas em um único comando.

## Gerenciamento de conversas integrado

Essa é a parte que economiza mais tempo em produção. Em vez de construir seu próprio store de estado de conversa, Hosted Agents lidam com isso nativamente:

```python
# Criar uma conversa persistente
conversation = openai_client.conversations.create()

# Primeira rodada
response1 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Remember: my favorite number is 42.",
)

# Segunda rodada — contexto é preservado
response2 = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent_reference": {"name": "MyAgent", "type": "agent_reference"}},
    input="Multiply my favorite number by 10.",
)
```

Sem Redis. Sem store de sessões Cosmos DB. Sem middleware customizado para serialização de mensagens. A plataforma simplesmente cuida disso.

## Meu framework de decisão

Depois de passar pelas seis opções, aqui está meu modelo mental rápido:

1. **Precisa de zero infraestrutura?** → Foundry Agents (portal/SDK, sem containers)
2. **Tem código de agente customizado mas quer hosting gerenciado?** → Foundry Hosted Agents
3. **Precisa de tarefas de agentes curtas orientadas a eventos?** → Azure Functions
4. **Precisa de máximo controle de containers sem K8s?** → Container Apps
5. **Precisa de compliance rigorosa e multi-cluster?** → AKS
6. **Tem um agente HTTP simples com tráfego previsível?** → App Service

Para a maioria dos desenvolvedores .NET construindo com Semantic Kernel ou Microsoft Agent Framework, Hosted Agents é provavelmente o ponto de partida certo. Você obtém scale-to-zero, OpenTelemetry integrado, gerenciamento de conversas e flexibilidade de framework — sem gerenciar Kubernetes ou montar sua própria stack de observabilidade.

## Para finalizar

O cenário de hospedagem de agentes no Azure está amadurecendo rápido. Se você está começando um novo projeto de agente IA hoje, eu consideraria seriamente Foundry Hosted Agents antes de recorrer a Container Apps ou AKS por hábito. A infraestrutura gerenciada economiza tempo real, e o padrão hosting adapter permite manter sua escolha de framework.

Confira o [guia completo da Microsoft](https://devblogs.microsoft.com/all-things-azure/hostedagent/) e o [repo Foundry Samples](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents) para exemplos funcionais.
