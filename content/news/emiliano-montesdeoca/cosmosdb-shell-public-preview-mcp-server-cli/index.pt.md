---
title: "Cosmos DB Shell Está em Pré-visualização Pública — E Tem um Servidor MCP Integrado"
date: 2026-05-24
author: "Emiliano Montesdeoca"
description: "Azure Cosmos DB Shell é uma nova CLI de código aberto que expõe comandos do banco de dados como ferramentas MCP. Seus agentes de IA podem navegar por containers, executar consultas e gerenciar dados usando a mesma interface que você usa."
tags:
  - Cosmos DB
  - MCP
  - AI
  - CLI
  - Open Source
  - Azure
---

Se você já teve que alternar entre uma guia do portal, um exemplo de SDK e um script pela metade apenas para responder uma pergunta sobre Cosmos DB, já conhece a fricção que este projeto foi projetado para eliminar.

Azure Cosmos DB Shell acabou de entrar em pré-visualização pública. É uma CLI de código aberto com sintaxe semelhante ao bash e — a parte que o torna interessante — um servidor MCP integrado.

## O Que o Torna Diferente de Outras CLIs de Banco de Dados

A CLI em si é útil: comandos familiares, suporte a scripts, integração CI/CD. Essa parte é o mínimo esperado para uma ferramenta de banco de dados voltada para desenvolvedores.

A parte interessante é a integração do servidor MCP. Cada comando que a CLI expõe fica disponível como uma ferramenta MCP que seus agentes de IA podem chamar. Não há camada de API personalizada, nenhum código de integração para escrever. Seu agente pode:

- Navegar por hierarquias de banco de dados com `cd`, `ls`, `pwd`
- Executar consultas SQL com `query` e obter resultados estruturados
- Criar e modificar itens com `create item`, `update`, `rm`
- Gerenciar bancos de dados e containers com `mkdb`, `mkcon`, `rmdb`, `rmcon`
- Inspecionar o contexto atual com `endpoint`, `pwd`

A mudança chave: seu agente não está falando com uma API do Cosmos DB — está falando com a mesma interface de shell que você usa. Os comandos são determinísticos, auditáveis e de código aberto para que você possa inspecionar exatamente o que está acontecendo.

## A Base de Código Aberto Importa

Isso não é um serviço gerenciado de caixa preta. O shell é de código aberto, o que significa:

- Equipes de segurança podem auditar a implementação
- Equipes de plataforma podem fazer fork e estendê-lo para seus padrões específicos
- Desenvolvedores podem contribuir com melhorias que beneficiam todos

Para equipes empresariais adotando ferramentas de IA, "podemos ver exatamente como funciona" é cada vez menos um requisito opcional. O código aberto aqui é um diferencial significativo.

## Três Cenários Que se Tornam Mais Fáceis

**Análise inteligente de dados** — conecte um agente ao shell, faça perguntas em linguagem natural, obtenha resultados de consultas estruturados. O agente cuida da construção da consulta; o shell cuida da execução.

**Gerenciamento autônomo de dados** — fluxos de trabalho que precisam criar, atualizar ou remover dados no Cosmos DB podem fazer isso através das ferramentas MCP sem precisar de uma integração personalizada.

**Monitoramento e alertas em tempo real** — um agente pode consultar containers periodicamente, comparar resultados e apresentar anomalias através do canal de notificação que fizer sentido.

A interface MCP torna esses cenários combináveis com qualquer plataforma de IA que fale MCP — não apenas as ferramentas da Microsoft.

## Para Começar

O shell está em pré-visualização pública. Instale-o, configure sua conexão com o Cosmos DB e habilite o servidor MCP. A partir daí, qualquer host de agente compatível com MCP pode descobrir e usar as ferramentas.

Post original: [Announcing the Public Preview of Azure Cosmos DB Shell: Open-Source Power Meets AI-Driven Database Automation](https://devblogs.microsoft.com/cosmosdb/azure-cosmos-db-shell-public-preview-ai-mcp-cli/)
