---
title: "Azure MCP Server 2.0 Chegou — Automação Agnóstica em Nuvem Self-Hosted Está Aqui"
date: 2026-04-11
author: "Emiliano Montesdeoca"
description: "Azure MCP Server 2.0 fica estável com implantações remotas self-hosted, 276 ferramentas em 57 serviços do Azure e segurança nível empresarial — aqui está o que importa para desenvolvedores .NET construindo fluxos de trabalho agnósticos."
tags:
  - mcp
  - azure
  - ai
  - agents
  - azure-sdk
  - dotnet
---

*Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "azure-mcp-server-2-self-hosted-agentic-cloud.md" >}}).*

Se você vem construindo algo com MCP e Azure ultimamente, provavelmente já sabe que a experiência local funciona bem. Coloque um servidor MCP, deixe seu agente IA falar com recursos do Azure, siga em frente. Mas no momento em que você precisa compartilhar essa configuração com um time? É aí que as coisas ficavam complicadas.

Não mais. Azure MCP Server [acabou de atingir a versão 2.0 estável](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release/), e a feature principal é exatamente o que times empresariais estão pedindo: **suporte para servidor MCP remoto self-hosted**.

## O que é Azure MCP Server?

Um rápido refresco. Azure MCP Server implementa a especificação do [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) e expõe capacidades do Azure como ferramentas estruturadas e descobríveis que agentes IA podem invocar. Pense nisto como uma ponte padronizada entre seu agente e o Azure — provisionamento, implantação, monitoramento, diagnósticos, tudo através de uma interface consistente.

Os números falam por si: **276 ferramentas MCP em 57 serviços do Azure**. Isso é cobertura séria.

## O grande destaque: implantações remotas self-hosted

Aqui está a questão. Executar MCP localmente na sua máquina é bom para dev e experimentos. Mas em um cenário real de time, você precisa de:

- Acesso compartilhado para desenvolvedores e sistemas de agentes internos
- Configuração centralizada (contexto de tenant, padrões de assinatura, telemetria)
- Limites de rede e política empresariais
- Integração em pipelines CI/CD

Azure MCP Server 2.0 aborda tudo isso. Você pode implantá-lo como um serviço interno gerenciado centralmente com transporte baseado em HTTP, autenticação apropriada e governança consistente.

Para autenticação, você tem duas opções sólidas:

1. **Managed Identity** — quando em execução junto com [Microsoft Foundry](https://aka.ms/azmcp/self-host/foundry)
2. **Fluxo On-Behalf-Of (OBO)** — delegação OpenID Connect que chama APIs do Azure usando o contexto do usuário autenticado

Esse fluxo OBO é particularmente interessante para nós desenvolvedores .NET. Significa que seus fluxos de trabalho agnósticos podem operar com as permissões reais do usuário, não alguma conta de serviço com privilégios excessivos. Princípio do menor privilégio, embutido certo.

## Endurecimento de segurança

Isso não é apenas um lançamento de feature — é um de segurança também. O lançamento 2.0 adiciona:

- Validação de endpoint mais forte
- Proteções contra padrões de injeção em ferramentas orientadas a query
- Controles de isolamento mais rigorosos para ambientes de dev

Se você vai expor MCP como um serviço compartilhado, essas salvaguardas importam. Muito.

## Onde você pode usá-lo?

A história de compatibilidade do cliente é ampla. Azure MCP Server 2.0 funciona com:

- **IDEs**: VS Code, Visual Studio, IntelliJ, Eclipse, Cursor
- **Agentes CLI**: GitHub Copilot CLI, Claude Code
- **Standalone**: servidor local para configurações simples
- **Self-hosted remoto**: a nova estrela do 2.0

Além disso há suporte a nuvem soberana para Azure US Government e Azure operado pela 21Vianet, que é crítico para implantações reguladas.

## Por que isso importa para desenvolvedores .NET

Se você está construindo aplicações agnósticas com .NET — seja com Semantic Kernel, Microsoft Agent Framework, ou sua própria orquestração — Azure MCP Server 2.0 lhe dá uma maneira pronta para produção de deixar seus agentes interagirem com infraestrutura do Azure. Sem wrappers REST customizados. Sem padrões de integração específicos do serviço. Apenas MCP.

Combinado com a [API fluente para MCP Apps](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) que saiu alguns dias atrás, o ecossistema MCP .NET está amadurecendo rapidamente.

## Começando

Escolha seu caminho:

- **[Repositório GitHub](https://aka.ms/azmcp)** — código fonte, documentação, tudo
- **[Imagem Docker](https://aka.ms/azmcp/download/docker)** — implantação containerizada
- **[Extensão VS Code](https://aka.ms/azmcp/download/vscode)** — integração de IDE
- **[Guia de self-hosting](https://aka.ms/azmcp/self-host)** — a feature principal do 2.0

## Resumindo

Azure MCP Server 2.0 é exatamente o tipo de upgrade de infraestrutura que não parece vistoso em uma demo mas muda tudo na prática. MCP remoto self-hosted com autenticação apropriada, endurecimento de segurança e suporte a nuvem soberana significa que MCP está pronto para times reais construindo fluxos de trabalho agnósticos reais no Azure. Se você estava esperando o sinal "pronto para empresas" — esse é ele.
