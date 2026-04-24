---
title: "Foundry Toolboxes: Um único endpoint para todas as ferramentas dos seus agentes"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "A Microsoft Foundry lançou Toolboxes em preview pública — uma forma de curar, gerenciar e expor ferramentas de agentes IA por meio de um único endpoint compatível com MCP."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

Aqui está um problema que parece chato até você vivenciá-lo: sua organização está construindo múltiplos agentes IA, cada um precisa de ferramentas, e cada time as configura do zero. A mesma integração de busca web, a mesma config do Azure AI Search, a mesma conexão com o servidor MCP do GitHub — mas em outro repositório, por outro time, com outras credenciais e sem governança compartilhada.

A Microsoft Foundry acabou de lançar [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) em preview pública, e é uma resposta direta a esse problema.

## O que é um Toolbox?

Um Toolbox é um bundle de ferramentas nomeado e reutilizável, definido uma vez no Foundry e exposto por meio de um único endpoint compatível com MCP. Qualquer runtime de agente que fale MCP pode consumi-lo — sem lock-in no Foundry Agents.

A proposta é simples: **build once, consume anywhere**. Defina as ferramentas, configure a autenticação de forma centralizada (OAuth passthrough, identidade gerenciada do Entra), publique o endpoint. Cada agente que precisar dessas ferramentas se conecta ao endpoint e as obtém todas.

## Os quatro pilares (dois disponíveis hoje)

| Pilar | Status | O que faz |
|-------|--------|-----------|
| **Discover** | Em breve | Encontra ferramentas aprovadas sem busca manual |
| **Build** | Disponível | Agrupa ferramentas em um bundle reutilizável |
| **Consume** | Disponível | Um endpoint MCP único expõe todas as ferramentas |
| **Govern** | Em breve | Auth centralizada + observabilidade em todas as chamadas |

## Exemplo prático

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Buscar documentação e responder a issues do GitHub.",
    tools=[
        {"type": "web_search", "description": "Buscar documentação pública"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

Após a publicação, o Foundry fornece um endpoint unificado. Uma conexão, todas as ferramentas.

## Sem lock-in no Foundry Agents

Os Toolboxes são **criados e gerenciados** no Foundry, mas a superfície de consumo é o protocolo MCP aberto. Você pode usá-los de agentes personalizados com Microsoft Agent Framework ou LangGraph, GitHub Copilot e outros IDEs compatíveis com MCP.

## Por que importa agora

A onda multi-agentes está chegando à produção. Cada novo agente é uma nova superfície para configuração duplicada, credenciais desatualizadas e comportamento inconsistente. A base Build + Consume é suficiente para começar a centralizar. Quando o pilar Govern chegar, você terá uma camada de ferramentas observável e controlada centralmente para toda a sua frota de agentes.

## Conclusão

Ainda é cedo — preview pública, SDK Python primeiro, com Discover e Govern ainda por vir. Mas o modelo é sólido e o design nativo de MCP significa que funciona com as ferramentas que você já está construindo. Confira o [anúncio oficial](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) para começar.
