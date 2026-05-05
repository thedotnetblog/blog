---
title: "Azure DevOps MCP Сервер Апрельское Обновление: WIQL-Запросы, PAT Аутентификация и Экспериментальные MCP Apps"
date: 2026-04-27
author: "Emiliano Montesdeoca"
description: "Azure DevOps MCP Сервер получает WIQL-запросы к рабочим элементам, аутентификацию Personal Access Token, аннотации MCP и экспериментальную функцию MCP Apps."
tags:
  - "Azure DevOps"
  - "MCP"
  - "Developer Productivity"
  - "Azure Boards"
  - "GitHub Copilot"
---

*Этот пост был автоматически переведён. Для оригинальной версии [нажмите здесь](https://thedotnetblog.com/posts/emiliano-montesdeoca/azure-devops-mcp-server-april-2026-wiql-pat-apps/).*

Azure DevOps MCP Сервер продолжает совершенствоваться. Апрельское обновление Дэна Хеллема охватывает оба сервера.

## Поддержка WIQL-Запросов

Новый инструмент `wit_query_by_wiql` позволяет запускать Work Item Query Language запросы прямо из MCP-клиента.

## Personal Access Tokens

PAT аутентификация на локальном сервере — важна для интеграционных сценариев без интерактивной аутентификации.

## Аннотации MCP

Метаданные для read-only, destructive и open-world инструментов — основа надёжности агентов.

## Консолидация Wiki-Инструментов

5 отдельных wiki-инструментов → 2 более мощных. Меньше инструментов = лучше производительность LLM.

## Экспериментально: MCP Apps

Упакованные рабочие процессы в среде MCP-сервера. Направление правильное.

Оригинальный пост Дэна Хеллема: [Azure DevOps MCP Server April Update](https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/).
