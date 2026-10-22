---
title: ".NET 11 Preview 5: O Que Eu Realmente Tentaria Primeiro"
date: 2026-06-12
author: "Emiliano Montesdeoca"
description: ".NET 11 Preview 5 traz melhorias no SDK, runtime, C#, ASP.NET Core e EF Core. Aqui estão as atualizações que acho que mais valem a pena testar cedo se você constrói aplicações .NET de verdade."
tags:
  - .NET
  - .NET 11
  - ASP.NET Core
  - C#
  - Entity Framework
---

Posts de prévia do .NET são sempre lotados.

Isso é uma boa notícia para a plataforma, mas também significa que a pergunta prática fica soterrada: **o que você deveria realmente testar primeiro?**

.NET 11 Preview 5 traz muita coisa no SDK, runtime, bibliotecas, ASP.NET Core, C#, MAUI e EF Core. Em vez de transformar isso em um enorme resumo de changelog, quero focar nas partes que acho que merecem atenção real dos desenvolvedores agora mesmo.

## O template de servidor MCP estar no `dotnet new` é um sinal

Este é provavelmente o item mais estratégico na seção do SDK.

Quando um template de projeto chega diretamente no SDK, significa que a plataforma não está mais tratando o cenário como nicho. Ter um **template de MCP Server** embutido no `dotnet new` reduz o custo de experimentar o padrão e envia uma mensagem clara sobre para onde o ecossistema está indo.

Se você está construindo ferramentas de agentes, assistentes internos ou utilitários de desenvolvedor integrados a IA em .NET, esta é uma das primeiras coisas que eu testaria.

## As verificações de vulnerabilidade e fim de vida em tempo de build são exatamente o tipo de padrão que eu gosto

Consciência de segurança e ciclo de vida é muito melhor quando a plataforma ajuda você *durante o build*, não depois, em um relatório separado que ninguém lê.

As novas verificações do SDK para vulnerabilidades e pacotes em fim de vida durante o build são o tipo de recurso que eu adoro porque tornam o comportamento melhor o padrão.

Não são chamativas, mas são o tipo de melhoria que envelhece muito bem.

## O C# continua ficando mais expressivo nos lugares certos

Os itens de C# da Preview 5 são interessantes, especialmente:

- hierarquias de classe fechadas
- declarações e padrões de union
- trabalho contínuo de evolução do unsafe

Eu não adotaria tudo isso cegamente em código de produção ainda, porque recursos de linguagem em prévia sempre merecem um ciclo de teste sóbrio. Mas a direção é boa. O C# continua caminhando para uma modelagem mais rica sem perder sua identidade.

## ASP.NET Core e EF Core têm atualizações práticas que valem a pena testar cedo

Duas áreas em que eu definitivamente colocaria um spike:

### Melhorias no Blazor

Validação do lado do cliente para Blazor SSR e melhorias no QuickGrid sem interatividade são ambos o tipo de recurso de qualidade de vida que pode simplificar aplicações reais.

### Padrões e avisos do EF Core

O EF Core mudando a compatibilidade padrão para SQL Server 2022 e adicionando avisos para consultas assíncronas do EF rodando de forma síncrona são exatamente o tipo de mudança que pode revelar problemas ocultos em bases de código reais.

Isso significa que vale a pena testar mais cedo do que tarde.

## Minha lista curta para uma primeira passada

Se eu tivesse meio dia para explorar a Preview 5, eu faria isto:

1. testar o template de servidor MCP
2. rodar builds e inspecionar as novas verificações de vulnerabilidade/fim de vida
3. testar qualquer base de código que possa se beneficiar dos novos recursos de modelagem em C#
4. validar cenários de Blazor SSR se você está nessa stack
5. rodar caminhos pesados em EF Core e observar mudanças de aviso ou diferenças de SQL

É aí que acho que está o valor inicial.

## Minha opinião

.NET 11 Preview 5 parece um daqueles lançamentos em que a plataforma continua empurrando em duas direções ao mesmo tempo:

- capacidades de desenvolvedor mais ambiciosas
- padrões melhores para equipes focadas em produção

Essa combinação é o que eu quero de um ciclo de prévia.

Teste, mas teste com propósito.

Post original: [.NET 11 Preview 5 is now available!](https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/)
