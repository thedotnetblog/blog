---
title: "Microsoft Foundry Março 2026 — GPT-5.4, Agent Service GA e a Atualização do SDK Que Muda Tudo"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "A atualização de março de 2026 do Microsoft Foundry é gigante: Agent Service chega ao GA, GPT-5.4 traz raciocínio confiável, o SDK azure-ai-projects se estabiliza em todas as linguagens, e Fireworks AI traz modelos abertos para o Azure."
tags:
  - foundry
  - ai
  - azure
  - gpt-5-4
  - agents
  - sdk
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "microsoft-foundry-march-2026-whats-new.md" >}}).*

Os posts mensais de "Novidades no Microsoft Foundry" costumam ser uma mistura de melhorias incrementais e alguma funcionalidade destaque ocasional. A [edição de março de 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)? É basicamente tudo destaque. Foundry Agent Service chega ao GA, GPT-5.4 é lançado para produção, o SDK recebe uma grande versão estável, e Fireworks AI traz inferência de modelos abertos para o Azure. Vamos detalhar o que importa para desenvolvedores .NET.

## Foundry Agent Service está pronto para produção

Essa é a grande novidade. O runtime de agentes de nova geração está em disponibilidade geral — construído sobre a API Responses da OpenAI, compatível em protocolo com agentes OpenAI, e aberto a modelos de múltiplos provedores. Se você está construindo com a API Responses hoje, migrar para o Foundry adiciona segurança empresarial, rede privada, RBAC do Entra, rastreamento completo e avaliação sobre sua lógica de agentes existente.

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = project_client.agents.create_version(
    agent_name="my-enterprise-agent",
    definition=PromptAgentDefinition(
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        instructions="You are a helpful assistant.",
    ),
)
```

Adições principais: rede privada de ponta a ponta, expansão de autenticação MCP (incluindo passthrough OAuth), preview do Voice Live para agentes de voz para voz, e agentes hospedados em 6 novas regiões.

## GPT-5.4 — confiabilidade acima de inteligência pura

GPT-5.4 não é sobre ser mais inteligente. É sobre ser mais confiável. Raciocínio mais forte em interações longas, melhor aderência a instruções, menos falhas no meio de workflows, e capacidades integradas de uso de computador. Para agentes em produção, essa confiabilidade importa muito mais do que pontuações em benchmarks.

| Modelo | Preço (por M tokens) | Ideal Para |
|--------|---------------------|------------|
| GPT-5.4 (≤272K) | $2.50 / $15 saída | Agentes em produção, código, fluxos de documentos |
| GPT-5.4 Pro | $30 / $180 saída | Análise profunda, raciocínio científico |
| GPT-5.4 Mini | Econômico | Classificação, extração, chamadas leves de ferramentas |

A jogada inteligente é uma estratégia de roteamento: GPT-5.4 Mini lida com o trabalho de alto volume e baixa latência enquanto GPT-5.4 cuida das solicitações com raciocínio pesado.

## O SDK finalmente está estável

O SDK `azure-ai-projects` lançou versões estáveis em todas as linguagens — Python 2.0.0, JS/TS 2.0.0, Java 2.0.0, e .NET 2.0.0 (1º de abril). A dependência do `azure-ai-agents` sumiu — tudo vive sob `AIProjectClient`. Instale com `pip install azure-ai-projects` e o pacote inclui `openai` e `azure-identity` como dependências diretas.

Para desenvolvedores .NET, isso significa um único pacote NuGet para toda a superfície do Foundry. Chega de malabarismo com SDKs de agentes separados.

## Fireworks AI traz modelos abertos para o Azure

Talvez a adição mais interessante arquitetonicamente: Fireworks AI processando mais de 13 trilhões de tokens por dia a ~180K requisições/segundo, agora disponível através do Foundry. DeepSeek V3.2, gpt-oss-120b, Kimi K2.5, e MiniMax M2.5 no lançamento.

A verdadeira história é o **bring-your-own-weights** — faça upload de pesos quantizados ou fine-tunados de qualquer lugar sem mudar a stack de serving. Deploy via serverless pay-per-token ou throughput provisionado.

## Outros destaques

- **Phi-4 Reasoning Vision 15B** — raciocínio multimodal para gráficos, diagramas e layouts de documentos
- **Evaluations GA** — avaliadores prontos para uso com monitoramento contínuo de produção integrado ao Azure Monitor
- **Priority Processing** (Preview) — faixa de computação dedicada para cargas de trabalho sensíveis à latência
- **Voice Live** — runtime de voz para voz que se conecta diretamente aos agentes do Foundry
- **Tracing GA** — inspeção de rastreamento de agentes de ponta a ponta com ordenação e filtragem
- **Depreciação do PromptFlow** — migração para Microsoft Framework Workflows até janeiro de 2027

## Conclusão

Março de 2026 é um ponto de virada para o Foundry. Agent Service GA, SDKs estáveis em todas as linguagens, GPT-5.4 para agentes de produção confiáveis, e inferência de modelos abertos via Fireworks AI — a plataforma está pronta para cargas de trabalho sérias.

Leia o [resumo completo](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/) e [crie seu primeiro agente](https://learn.microsoft.com/azure/foundry/quickstarts/get-started-code) para começar.
