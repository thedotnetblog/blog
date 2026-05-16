---
title: "Azure Data Studio foi descontinuado: migre seu fluxo de Azure SQL para o VS Code"
date: 2026-05-09
author: "Emiliano Montesdeoca"
description: "Azure Data Studio foi descontinuado em 6 de fevereiro de 2025, com suporte até 28 de fevereiro de 2026. Aqui está o caminho de migração completo para o VS Code com a extensão MSSQL."
tags:
  - .NET
  - Azure SQL
  - VS Code
  - Developer Tools
---

*Esta publicação foi traduzida automaticamente. Para a versão original, [clique aqui]({{< ref "index.md" >}}).*

[Azure Data Studio foi descontinuado em 6 de fevereiro de 2025](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/), com suporte até 28 de fevereiro de 2026 — o substituto recomendado é o VS Code com a extensão MSSQL.

## O que instalar

Três itens para começar:

- **Extensão MSSQL** — pesquise "SQL Server (mssql)" no Marketplace do VS Code
- **Extensão SQL Database Projects** — esquema como código, validação de build, publicação guiada
- **.NET 8 SDK** — exigido pelo sistema de build; SDK ausente é o problema mais comum no primeiro uso

## Migrar suas conexões e configurações do ADS

A extensão MSSQL inclui o **ADS Migration Toolkit**, que gerencia a migração única em um fluxo guiado: conexões salvas, grupos de conexões, configurações e atalhos de teclado são importados automaticamente.

## Recuperar a memória muscular do F5

Os usuários do ADS dependem do F5 para executar consultas. Instale a extensão **MSSQL Database Management Keymap** para recuperar os atalhos de teclado no estilo ADS, incluindo o F5.

## SQL Database Projects: esquema como código

Clique com o botão direito em um projeto → **Publicar** → configurar destino → revisar o script T-SQL gerado → implantar. A visualização prévia do script antes da implantação é o principal recurso de segurança. Os modelos de itens geram stubs para tabelas, stored procedures e views — o mesmo fluxo do SSDT.

Problema comum: uma **incompatibilidade de plataforma de destino** no arquivo `.sqlproj` causará erros de build se o projeto foi criado para uma versão diferente do SQL Server.

## Schema Compare e Schema Designer

A extensão também inclui **Schema Compare** (diff entre seu projeto e o banco de dados implantado) e **Schema Designer** (edição visual do esquema sem escrever DDL manualmente).

## Desenvolvedores do Microsoft Fabric

A configuração é idêntica, mas comece pelo **portal do Fabric** e conecte o banco de dados ao Git primeiro antes de abri-lo no VS Code. A Microsoft tem um guia dedicado: *Azure Data Studio to VS Code — What it means for SQL database in Fabric developers*.

## Conclusão

A migração é um fluxo guiado de uma única vez, não uma reconstrução manual. Instale as três ferramentas, execute o ADS Migration Toolkit, restaure seus atalhos de teclado e você estará de volta ao normal em menos de 10 minutos.

Consulte o [artigo completo](https://devblogs.microsoft.com/azure-sql/azure-data-studio-is-retired-move-your-azure-sql-workflow-to-vs-code-in-10-minutes/) para capturas de tela passo a passo e o tutorial específico do Fabric.
