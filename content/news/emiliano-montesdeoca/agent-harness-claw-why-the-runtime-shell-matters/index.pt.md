---
title: "Harnesses de Agentes Importam Porque Prompts Não São Suficientes"
date: 2026-06-20
author: "Emiliano Montesdeoca"
description: "O novo passo a passo de claw e harness do Microsoft Agent Framework é um lembrete útil de que agentes de verdade precisam de uma camada de runtime ao redor do modelo: ferramentas, planejamento, memória, sessões e um loop de execução prático."
tags:
  - Agent Framework
  - AI
  - .NET
  - Developer Experience
  - Microsoft Foundry
---

Um dos erros mais fáceis de cometer no desenvolvimento de agentes é achar que o prompt é o produto.

Não é.

O novo passo a passo de **agent harness e claw** da equipe do Microsoft Agent Framework é valioso porque mantém o foco na parte que realmente determina se um agente parece utilizável: a camada de runtime ao redor do modelo.

Isso inclui:

- ferramentas
- planejamento
- estado de sessão
- memória
- modos de execução
- um console ou interface utilizável para iteração

É aí que os agentes deixam de ser demos inteligentes e passam a parecer software de verdade.

## O padrão de harness é prático

O que eu gosto aqui é o quão acessível a ideia é.

Você começa com um chat client.

Depois envolve isso em um harness com instruções e ferramentas.

Depois roda tudo através de um shell que suporta planejamento, todos, sessões e interação em streaming.

Esse é um padrão saudável porque separa claramente as responsabilidades:

- o modelo cuida do raciocínio
- o harness cuida do comportamento em tempo de execução
- a aplicação decide quais ferramentas e experiências importam

## Isso combina muito bem com a forma como desenvolvedores .NET constroem sistemas

A ideia do harness também mapeia bem para a mentalidade .NET.

Geralmente nos saímos melhor quando o comportamento em runtime é explícito e composável. Middleware, pipelines, options, providers e adapters são todos naturais nesse mundo.

É por isso que acho que o Agent Framework tem uma boa chance de agradar aos desenvolvedores .NET. Ele não força todo mundo em uma única abstração mágica. Ele te dá peças estruturadas de runtime que você pode conectar entre si.

## Minha opinião

A parte mais útil deste post é o lembrete de que agentes precisam de mais do que um bom modelo e uma string de instrução inteligente.

Eles precisam de uma camada de runtime que dê a eles estrutura, memória, acesso a ferramentas, planejamento e um loop de desenvolvimento viável.

É isso que o harness te dá.

E, honestamente, é por isso que esse padrão vale a pena acompanhar.

Post original: [Meet your agent harness and claw](https://devblogs.microsoft.com/agent-framework/meet-your-agent-harness-and-claw/)
