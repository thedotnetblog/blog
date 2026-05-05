---
title: "Foundry Agent Service está GA: O que realmente importa para construtores de agentes .NET"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "O Foundry Agent Service da Microsoft acaba de chegar ao GA com rede privada, Voice Live, avaliações de produção e um runtime multi-modelo aberto. Aqui está o que você precisa saber."
tags:
  - azure
  - ai
  - foundry
  - agents
  - dotnet
---

Vamos ser honestos — construir um protótipo de agente IA é a parte fácil. A parte difícil é tudo o que vem depois: colocá-lo em produção com isolamento de rede adequado, executar avaliações que realmente signifiquem algo, lidar com requisitos de conformidade e não quebrar nada às 2 da manhã.

O [Foundry Agent Service acabou de chegar ao GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/), e esta versão está focada como um laser nessa lacuna do "tudo que vem depois".

## Construído sobre a Responses API

A manchete: o Foundry Agent Service de próxima geração é construído sobre a OpenAI Responses API. Se você já está construindo com esse protocolo, migrar para o Foundry requer mudanças mínimas de código. O que você ganha: segurança empresarial, rede privada, RBAC Entra, rastreamento completo e avaliação — sobre sua lógica de agente existente.

A arquitetura é intencionalmente aberta. Você não está preso a um provedor de modelo ou um framework de orquestração. Use DeepSeek para planejamento, OpenAI para geração, LangGraph para orquestração — o runtime cuida da camada de consistência.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                    credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
    agent = project_client.agents.create_version(
        agent_name="my-enterprise-agent",
        definition=PromptAgentDefinition(
            model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
            instructions="You are a helpful assistant.",
        ),
    )

    conversation = openai_client.conversations.create()
    response = openai_client.responses.create(
        conversation=conversation.id,
        input="What are best practices for building AI agents?",
        extra_body={
            "agent_reference": {"name": agent.name, "type": "agent_reference"}
        },
    )
    print(response.output_text)
```

> Se você vem do pacote `azure-ai-agents`, os agentes agora são operações de primeira classe no `AIProjectClient` em `azure-ai-projects`. Remova a dependência standalone e use `get_openai_client()` para conduzir as respostas.

## Rede privada: o bloqueador empresarial removido

Esta é a funcionalidade que desbloqueia a adoção empresarial. Foundry agora suporta rede privada completa de ponta a ponta com BYO VNet:

- **Sem egress público** — o tráfego do agente nunca toca a internet pública
- **Injeção de contêiners/sub-redes** na sua rede para comunicação local
- **Conectividade de ferramentas incluída** — servidores MCP, Azure AI Search, agentes de dados Fabric, todos operam sobre caminhos privados

Esse último ponto é crítico. Não são apenas as chamadas de inferência que ficam privadas — cada invocação de ferramenta e chamada de recuperação também fica dentro do perímetro da sua rede. Para equipes operando sob políticas de classificação de dados que proíbem roteamento externo, isso era o que faltava.

## Autenticação MCP feita direito

Conexões de servidores MCP agora suportam o espectro completo de padrões de autenticação:

| Método de auth | Quando usar |
|----------------|-------------|
| Baseado em chave | Acesso compartilhado simples para ferramentas internas da organização |
| Entra Agent Identity | Serviço a serviço; o agente se autentica como ele mesmo |
| Entra Managed Identity | Isolamento por projeto; sem gerenciamento de credenciais |
| OAuth Identity Passthrough | Acesso delegado por usuário; agente age em nome dos usuários |

OAuth Identity Passthrough é o interessante. Quando usuários precisam dar a um agente acesso aos seus dados pessoais — seu OneDrive, sua organização Salesforce, uma API SaaS com escopo por usuário — o agente age em seu nome com fluxos OAuth padrão. Sem identidade de sistema compartilhada fingindo ser todos.

## Voice Live: voz a voz sem a encanação

Adicionar voz a um agente costumava significar juntar STT, LLM e TTS — três serviços, três saltos de latência, três superfícies de faturamento, tudo sincronizado à mão. **Voice Live** colapsa isso em uma única API gerenciada com:

- Detecção semântica de atividade de voz e fim de turno (entende significado, não apenas silêncio)
- Supressão de ruído e cancelamento de eco do lado do servidor
- Suporte a barge-in (usuários podem interromper no meio da resposta)

Interações de voz passam pelo mesmo runtime de agente que o texto. Mesmos avaliadores, mesmos traces, mesma visibilidade de custos. Para suporte ao cliente, serviço de campo ou cenários de acessibilidade, isso substitui o que antes requeria um pipeline de áudio personalizado.

## Avaliações: de checkbox para monitoramento contínuo

Aqui é onde o Foundry fica sério sobre qualidade em produção. O sistema de avaliação agora tem três camadas:

1. **Avaliadores prontos para uso** — coerência, relevância, fundamentação, qualidade de recuperação, segurança. Conecte a um dataset ou tráfego ao vivo e obtenha pontuações.

2. **Avaliadores personalizados** — codifique sua própria lógica de negócio, padrões de tom e regras de conformidade específicas do domínio.

3. **Avaliação contínua** — Foundry amostra tráfego de produção ao vivo, executa sua suíte de avaliadores e exibe resultados em dashboards. Configure alertas do Azure Monitor para quando a fundamentação cai ou limites de segurança são violados.

Tudo é publicado no Azure Monitor Application Insights. Qualidade do agente, saúde da infraestrutura, custo e telemetria da aplicação — tudo em um só lugar.

```python
eval_object = openai_client.evals.create(
    name="Agent Quality Evaluation",
    data_source_config=DataSourceConfigCustom(
        type="custom",
        item_schema={
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
        include_sample_schema=True,
    ),
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "fluency",
            "evaluator_name": "builtin.fluency",
            "initialization_parameters": {
                "deployment_name": os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"]
            },
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
        },
    ],
)
```

## Seis novas regiões para agentes hospedados

Agentes hospedados agora estão disponíveis em East US, North Central US, Sweden Central, Southeast Asia, Japan East e mais. Isso importa para requisitos de residência de dados e para comprimir latência quando seu agente roda perto de suas fontes de dados.

## Por que isso importa para desenvolvedores .NET

Embora os exemplos de código no anúncio de GA sejam Python-first, a infraestrutura subjacente é agnóstica a linguagem — e o SDK .NET para `azure-ai-projects` segue os mesmos padrões. A Responses API, o framework de avaliação, a rede privada, a autenticação MCP — tudo isso está disponível a partir do .NET.

Se você tem esperado os agentes IA passarem de "demo legal" para "consigo realmente entregar isso no trabalho", esta versão GA é o sinal. Rede privada, autenticação adequada, avaliação contínua e monitoramento de produção são as peças que faltavam.

## Para finalizar

Foundry Agent Service está disponível agora. Instale o SDK, abra [o portal](https://ai.azure.com) e comece a construir. O [guia de início rápido](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) leva você de zero a um agente rodando em minutos.

Para o mergulho técnico completo com todos os exemplos de código, confira o [anúncio de GA](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/).
