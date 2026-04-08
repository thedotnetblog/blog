---
title: "Conecte seus servidores MCP no Azure Functions aos Foundry Agents — Veja como"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Construa seu servidor MCP uma vez, faça deploy no Azure Functions e conecte-o aos agentes Microsoft Foundry com autenticação adequada. Suas ferramentas funcionam em qualquer lugar — VS Code, Cursor e agora agentes de IA empresariais."
tags:
  - mcp
  - azure-functions
  - foundry
  - ai
  - azure
  - dotnet
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "foundry-agents-mcp-servers-azure-functions.md" >}}).*

Isso é algo que eu amo no ecossistema MCP: você constrói seu servidor uma vez e ele funciona em qualquer lugar. VS Code, Visual Studio, Cursor, ChatGPT — cada cliente MCP pode descobrir e usar suas ferramentas. Agora, a Microsoft está adicionando mais um consumidor a essa lista: os agentes Foundry.

Lily Ma da equipe do Azure SDK [publicou um guia prático](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) sobre como conectar servidores MCP implantados no Azure Functions com agentes Microsoft Foundry. Se você já tem um servidor MCP, isso é puro valor agregado — sem necessidade de reconstruir nada.

## Por que essa combinação faz sentido

Azure Functions te dá infraestrutura escalável, autenticação integrada e cobrança serverless para hospedar servidores MCP. Microsoft Foundry te dá agentes de IA que podem raciocinar, planejar e agir. Conectar os dois significa que suas ferramentas personalizadas — consultar um banco de dados, chamar uma API de negócio, executar lógica de validação — se tornam capacidades que agentes de IA empresariais podem descobrir e usar autonomamente.

O ponto-chave: seu servidor MCP continua o mesmo. Você está apenas adicionando o Foundry como mais um consumidor. As mesmas ferramentas que funcionam no seu setup do VS Code agora alimentam um agente de IA com o qual sua equipe ou clientes interagem.

## Opções de autenticação

É aqui que o post realmente agrega valor. Quatro métodos de autenticação dependendo do seu cenário:

| Método | Caso de uso |
|--------|-------------|
| **Baseado em chave** (padrão) | Desenvolvimento ou servidores sem autenticação Entra |
| **Microsoft Entra** | Produção com identidades gerenciadas |
| **Passthrough de identidade OAuth** | Produção onde cada usuário se autentica individualmente |
| **Sem autenticação** | Dev/testes ou apenas dados públicos |

Para produção, Microsoft Entra com identidade do agente é o caminho recomendado. O passthrough de identidade OAuth é para quando o contexto do usuário importa — o agente solicita que os usuários façam login, e cada requisição carrega o token próprio do usuário.

## Configurando

O fluxo geral:

1. **Faça deploy do seu servidor MCP no Azure Functions** — exemplos disponíveis para [.NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet), Python, TypeScript e Java
2. **Habilite a autenticação MCP integrada** na sua function app
3. **Obtenha sua URL de endpoint** — `https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp`
4. **Adicione o servidor MCP como ferramenta no Foundry** — navegue até seu agente no portal, adicione uma nova ferramenta MCP, forneça o endpoint e as credenciais

Depois teste no playground do Agent Builder enviando um prompt que acionaria uma das suas ferramentas.

## Minha opinião

A história de composabilidade aqui está ficando realmente forte. Construa seu servidor MCP uma vez em .NET (ou Python, TypeScript, Java), faça deploy no Azure Functions, e cada cliente compatível com MCP pode usá-lo — ferramentas de programação, apps de chat, e agora agentes de IA empresariais. É um padrão "escreva uma vez, use em qualquer lugar" que realmente funciona.

Para desenvolvedores .NET especificamente, a [extensão MCP do Azure Functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) torna isso simples. Você define suas ferramentas como Azure Functions, faz deploy, e tem um servidor MCP de nível de produção com toda a segurança e escalabilidade que o Azure Functions proporciona.

## Finalizando

Se você tem ferramentas MCP rodando no Azure Functions, conectá-las aos agentes Foundry é uma vitória rápida — suas ferramentas personalizadas se tornam capacidades de IA empresarial com autenticação adequada e sem alterações de código no servidor.

Leia o [guia completo](https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/) para instruções passo a passo sobre cada método de autenticação, e confira a [documentação detalhada](https://learn.microsoft.com/azure/azure-functions/functions-mcp-foundry-tools?tabs=entra%2Cmcp-extension%2Cfoundry) para configurações de produção.
