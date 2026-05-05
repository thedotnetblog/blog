---
title: "Azure MCP Server Теперь .mcpb — Установка без Какого-либо Runtime"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Azure MCP Server теперь доступен как MCP Bundle (.mcpb) — скачайте, перетащите в Claude Desktop, и готово. Node.js, Python или .NET не нужны."
tags:
  - MCP
  - Azure
  - AI
  - Developer Tools
  - Azure SDK
---

*Этот пост переведён автоматически. Чтобы просмотреть оригинал, [нажмите здесь]({{< ref "index.md" >}}).*

Знаете, что раздражало в настройке MCP-серверов? Нужен был runtime. Node.js для npm-версии, Python для pip/uvx, .NET SDK для dotnet-варианта.

[Azure MCP Server только что изменил это](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/). Теперь он доступен как `.mcpb` — MCP Bundle — и настройка выполняется перетаскиванием.

## Что такое MCP Bundle?

Думайте о нём как о расширении VS Code (`.vsix`) или расширении браузера (`.crx`), но для MCP-серверов. Файл `.mcpb` — это автономный ZIP-архив с бинарным файлом сервера и всеми его зависимостями.

## Как установить

**1. Скачайте bundle для вашей платформы**

Перейдите на [страницу GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server) и скачайте файл `.mcpb` для вашей ОС и архитектуры.

**2. Установите в Claude Desktop**

Самый простой способ: перетащите файл `.mcpb` в окно Claude Desktop на странице настроек расширений (`☰ → Файл → Настройки → Расширения`). Проверьте детали сервера, нажмите «Установить», подтвердите.

**3. Аутентифицируйтесь в Azure**

```bash
az login
```

Всё. Azure MCP Server использует ваши существующие учётные данные Azure.

## Что можно делать

Доступ к 100+ инструментам сервисов Azure прямо из вашего ИИ-клиента:
- Запрашивать и управлять Cosmos DB, Storage, Key Vault, App Service, Foundry
- Генерировать команды `az` CLI для любых задач
- Создавать шаблоны Bicep и Terraform

## С чего начать

- **Загрузка**: [GitHub Releases](https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-)
- **Репозиторий**: [aka.ms/azmcp](https://aka.ms/azmcp)
- **Документация**: [aka.ms/azmcp/docs](https://aka.ms/azmcp/docs)

Смотрите [полный пост](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/).
