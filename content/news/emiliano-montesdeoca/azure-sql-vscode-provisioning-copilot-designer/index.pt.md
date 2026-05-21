---
title: "A extensão MSSQL para VS Code está silenciosamente virando uma plataforma muito maior"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "A atualização mais recente da extensão MSSQL adiciona provisionamento de Azure SQL, design de schema assistido por Copilot, Data API builder e notebooks. O mais interessante é quanto trabalho de banco de dados agora pode ficar dentro do VS Code."
tags:
  - Azure SQL
  - VS Code
  - GitHub Copilot
  - Data API Builder
  - Developer Tools
---

*Este artigo foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

A extensão MSSQL para VS Code vem crescendo há algum tempo, mas esta atualização mais recente deixa a direção muito mais clara.

Não é mais só «conectar e executar algumas queries».

Com **provisionamento de Azure SQL**, **Schema Designer com Copilot**, **SQL Notebooks** e **Data API builder** sendo avançados em uma única release, a extensão está se tornando um workspace muito mais completo para desenvolvimento centrado em bancos de dados.

## O gancho prático é o provisionamento direto do editor

O post original diz que agora você pode criar um banco de dados em nuvem totalmente gerenciado «diretamente do seu editor e sem custo» usando a camada gratuita.

Esse é o tipo de recurso que parece pequeno até você perceber quanta fricção de setup ele remove.

Para muitos desenvolvedores, a parte chata de experimentação pesada em dados não é SQL em si. É a lacuna de ambiente entre:

- ideia
- banco de dados
- schema
- API
- backend testável

Se essa lacuna encurta dentro de uma única ferramenta, o fluxo inteiro fica mais atraente.

## É assim que um inner loop mais forte para trabalho com dados se parece

O que eu gosto nesta release é que ela mantém mais do workflow de banco de dados em um só lugar:

- provisionar o banco
- desenhar o schema
- revisar mudanças
- gerar scripts ORM
- expor APIs
- testar endpoints
- documentar e consultar via notebooks

Essa é uma história muito mais convincente do que tratar SQL como uma ferramenta lateral desconectada no stack.

## O workflow de schema assistido por Copilot é onde o valor da IA parece real

As novidades do schema designer são especialmente interessantes porque parecem atingir um bom equilíbrio.

O valor não é «a IA desenha seu modelo de dados e você confia cegamente nela».

O valor é:

- pontos de partida mais rápidos
- revisão visual
- rastreamento de mudanças
- saída orientada a migração
- controles explícitos de aceitar/desfazer

Esse é um workflow de IA muito mais saudável do que geração automática completa sem caminho de inspeção.

E, em trabalho de banco de dados, revisibilidade importa muito.

## Data API builder é um multiplicador silencioso

O outro recurso que eu não ignoraria é a integração do Data API builder.

Se você consegue ir do schema para:

- REST
- GraphQL
- endpoints MCP

dentro do mesmo ambiente, isso cria um caminho muito eficiente para protótipos de backend e ferramentas internas.

Isso não substitui uma engenharia backend mais profunda. Mas encurta muito o caminho da ideia de banco de dados até uma interface funcionando.

## A minha leitura

Esta release faz a extensão MSSQL parecer mais uma pequena plataforma dentro do VS Code do que um simples add-on.

Para desenvolvedores que criam APIs, ferramentas de dados, ferramentas administrativas ou protótipos baseados em SQL, isso é uma mudança significativa.

E, se a Microsoft continuar apertando esse loop, a extensão vai se tornar muito mais estrategicamente útil do que muita gente ainda assume.

Post original: [MSSQL Extension for VS Code: Azure SQL Database Provisioning and More](https://devblogs.microsoft.com/azure-sql/vscode-mssql-june-2026/)