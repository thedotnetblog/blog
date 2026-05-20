---
title: "O Seu Agente de IA Tem um Problema de Identidade (E Aqui Está o Template que o Resolve)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Um novo template azd da Curity e Microsoft mostra como construir agentes de IA que usam tokens OAuth de curta duração com escopos de granularidade fina — para que os agentes nunca possam ver dados que não deveriam ver."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

Há um momento em cada projeto de agente de IA que vai mais ou menos assim: a demo funciona perfeitamente, o agente interpreta a linguagem natural, chama as APIs certas, retorna os dados certos. Então você começa a pensar nos usuários reais.

O que impede a sessão do agente de um usuário de ver os dados de outro usuário? E se o agente for enganado por injeção de prompt? E se ele chamar uma ferramenta de uma forma inesperada?

Estes não são casos extremos. São decisões de design que você precisa tomar antes de lançar.

Um novo template `azd` da Curity e Microsoft fornece uma referência funcional para exatamente este problema.

## O Problema Central: Autenticação ≠ Autorização

A maioria dos exemplos de agentes trata bem a autenticação de usuários. Trata mal a autorização. Saber *quem* é o usuário não te diz *quais dados* ele deveria ver.

Uma aplicação cliente tradicional faz chamadas de API previsíveis. Um agente de IA é não-determinístico — interpreta a linguagem natural e decide o que chamar. Pode ser criativo. Também pode estar errado. E se for manipulado por injeção de prompt, você precisa de regras que não dependam do bom comportamento da IA.

A solução que este template demonstra: **tokens de curta duração que carregam exatamente as informações certas para cada salto**.

## Como Funciona a Cadeia de Tokens

O template usa tokens de acesso OAuth 2.0 com troca de tokens para restringir permissões a cada passo. Um token de usuário é trocado duas vezes antes de chegar ao servidor MCP:

1. **Primeira troca** — restringe o escopo e converte o token opaco em JWT
2. **Segunda troca** — adiciona a identidade do agente e um novo audience para o salto do servidor MCP

Como é o token do servidor MCP:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

O `customer_id` está incorporado no token pelo servidor de autorização, não passado como um parâmetro que o agente controla. A API verifica o token, não as instruções do agente.

Isso significa: mesmo que alguém engane o agente para tentar buscar os dados de outro cliente, o token não autorizará.

## O que o Template Implanta

Com alguns comandos `azd` você obtém:

- Um agente backend no Microsoft Foundry (C#, SDKs Microsoft A2A e MCP)
- Um servidor MCP que expõe uma API de portfólio de exemplo
- Curity Identity Server como servidor de autorização, junto com Entra ID para autenticação
- Gateways de API externos e internos que gerenciam a troca de tokens e o registro de auditoria
- Bicep para toda a infraestrutura Azure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, armazenamento

Todo o padrão é inspecionável e personalizável.

## O Princípio de Design que Vale a Pena Adotar

Mesmo se você não usar Curity, o padrão é transferível: **agentes nunca deveriam ter acesso permanente à API**. Cada ação deveria usar um token de curta duração com o escopo mínimo necessário para aquela chamada específica, emitido para a identidade específica do agente, carregando as claims de que a API precisa para tomar decisões de autorização.

Isso resiste a agentes criativos, erros e injeção de prompt de maneiras que "apenas certifique-se de que o agente não faça coisas ruins" nunca resistirá.

## Conclusão

Os padrões de segurança para agentes de IA ainda estão sendo desenvolvidos em toda a indústria. Este template é uma das implementações de referência mais completas que vi — cobre o fluxo de autorização real, não apenas a autenticação.

Post original: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
