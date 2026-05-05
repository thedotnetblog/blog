---
title: "SQL Server 2025 como Banco de Dados Pronto para Agentes: Segurança, Backup e MCP em Um Motor"
date: 2026-04-26
author: "Emiliano Montesdeoca"
description: "A parte final da série Polyglot Tax aborda os problemas difíceis de produção: Row-Level Security unificada sobre dados relacionais, JSON, grafos e vetores, mais integração MCP."
tags:
  - "Azure SQL"
  - "SQL Server"
  - "MCP"
  - "Security"
  - "AI Apps"
  - "Azure"
---

*Esta postagem foi traduzida automaticamente. Para a versão original, [clique aqui](https://thedotnetblog.com/posts/emiliano-montesdeoca/sql-server-2025-agent-ready-security-mcp/).*

Acompanhei a série Polyglot Tax de Aditya Badramraju com muito interesse. A parte 4 fecha a série com as partes que realmente determinam se você confiaria nessa arquitetura em produção.

## Um Modelo de Segurança para Todos os Modelos de Dados

Uma única política de Row-Level Security que cobre todos os modelos de dados. Uma política, uma prova para o auditor.

## Backup Unificado = Recuperação Atômica

Em um stack poliglota, recuperação point-in-time em cinco bancos de dados é um pesadelo de consistência. Com um banco, é atômica por definição.

## Integração MCP: Agentes Sem Middleware

SQL Server 2025 suporta o SQL MCP Server diretamente. Agentes chamam ferramentas, o motor impõe isolamento de tenant e mascaramento de colunas automaticamente.

Post original de Aditya Badramraju: [The Polyglot Tax – Part 4](https://devblogs.microsoft.com/azure-sql/the-polyglot-tax-part-4/).
