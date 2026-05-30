---
title: "Seu Agente MAF Local Acabou de Ganhar um Lar em Produção"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents dá ao seu agente Microsoft Agent Framework identidade, escalamento, persistência de sessão e observabilidade sem configuração adicional. Veja como isso parece na prática."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Fazer um agente funcionar localmente é a parte divertida. A parte complicada é tudo que vem depois: implantá-lo sem enlouquecer, gerenciar sessões, configurar identidade, conectar observabilidade. Normalmente isso significa muita infraestrutura personalizada.

O Foundry Hosted Agents acabou de remover a maior parte dessa infraestrutura para usuários do Microsoft Agent Framework (MAF).

## O Que o Foundry Hosted Agents Realmente Faz

Quando você implanta um agente MAF no Foundry Hosted Agents, a plataforma lida com uma lista surpreendentemente longa de coisas que você teria que construir por conta própria:

- **Escalar para zero** — seu agente não custa nada quando ocioso e volta automaticamente
- **Sandboxes isolados por VM por sessão** — cada sessão de usuário tem seu próprio sandbox com persistência do sistema de arquivos que sobrevive a eventos de redução de escala
- **Entra ID integrado** — cada agente tem sua própria identidade para chamar modelos Foundry, Toolbox e serviços Azure sem segredos na imagem
- **Implantações versionadas** — cada implantação é um snapshot imutável, com suporte a blue/green e canary rollout
- **Observabilidade sem configuração** — `APPLICATIONINSIGHTS_CONNECTION_STRING` é injetado em tempo de execução para que os traces OpenTelemetry do MAF fluam automaticamente para o App Insights

Esse último é genuinamente agradável. Sem fiação extra, sem configuração adicional. Os traces simplesmente aparecem.

## A Diferença no Código É Mínima

Isso é o que mais aprecio nessa integração. Você não reescreve seu agente. Você simplesmente o envolve:

**Em .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**Em Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

É isso. A mesma lógica que você testou localmente é o que roda em produção. A plataforma a envolve na infraestrutura de gerenciamento de sessões, identidade e escalamento.

## Dois Protocolos, Um Agente

Os Hosted Agents suportam dois estilos de endpoints:

- **Responses** (`/responses`) — compatível com OpenAI, gerencia histórico de conversas e streaming. Bom padrão para agentes em forma de chat.
- **Invocations** (`/invocations`) — você define o esquema de requisição/resposta. Bom para workflows não conversacionais.

Se você está construindo algo que parece uma conversa, comece com Responses. Se está construindo um agente em forma de API que recebe entrada estruturada e retorna saída estruturada, Invocations te dá a flexibilidade.

## O Fluxo de Implantação com `azd`

Quando você executa `azd up` com um agente MAF:

1. Opcionalmente cria um projeto Foundry e implanta um modelo
2. Empacota seu código e envia uma imagem para o Azure Container Registry
3. Provisiona compute a partir da imagem ACR
4. Atribui um Entra ID dedicado ao agente
5. Expõe um endpoint estável (`https://{project_endpoint}/agents/{agent_name}`)
6. Lida com tudo mais a partir desse ponto

As sessões persistem por até 30 dias. O compute ocioso é desprovisionado após 15 minutos e restaurado transparentemente na próxima requisição. Da perspectiva do agente, nada mudou.

## Conclusão

A distância entre "funcionando localmente" e "rodando em produção" tem sido historicamente longa e dolorosa para agentes de IA. Foundry Hosted Agents + MAF fecha essa lacuna significativamente. Se você já tem um agente local construído com Agent Framework, vale a pena tentar hoje.

A equipe diz que o GA está chegando em breve — atualmente está em preview. Confira os [docs de integração MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) e os [exemplos .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents) para começar.

Artigo original: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
