---
title: "Foundry Toolboxes: Единый эндпоинт для всех инструментов агентов"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Microsoft Foundry выпустила Toolboxes в Public Preview — способ централизованно управлять инструментами ИИ-агентов и предоставлять их через единый MCP-совместимый эндпоинт."
tags:
  - microsoft-foundry
  - ai
  - agents
  - mcp
  - azure
  - developer-tools
---

*Этот пост был автоматически переведён. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

Есть проблема, которая кажется скучной, пока не столкнёшься с ней лично: организация строит несколько ИИ-агентов, каждому нужны инструменты, и каждая команда настраивает их с нуля. Та же интеграция веб-поиска, та же конфигурация Azure AI Search, то же подключение к GitHub MCP-серверу — но в другом репозитории, другой командой, с другими учётными данными и без общего управления.

Microsoft Foundry только что выпустила [Toolboxes](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/) в Public Preview — прямой ответ на эту проблему.

## Что такое Toolbox?

Toolbox — это именованный, многократно используемый набор инструментов, который определяется один раз в Foundry и предоставляется через единый MCP-совместимый эндпоинт. Любая среда выполнения агента, говорящая на MCP, может его потреблять — никакой привязки к Foundry Agents.

Обещание простое: **build once, consume anywhere**. Определить инструменты, настроить аутентификацию централизованно (OAuth passthrough, управляемые удостоверения Entra), опубликовать эндпоинт. Каждый агент, которому нужны эти инструменты, подключается к эндпоинту и получает их все.

## Четыре столпа (два доступны сегодня)

| Столп | Статус | Что делает |
|-------|--------|-----------|
| **Discover** | Скоро | Находить одобренные инструменты без ручного поиска |
| **Build** | Доступен | Собирать инструменты в многократно используемый bundle |
| **Consume** | Доступен | Единый MCP-эндпоинт предоставляет все инструменты |
| **Govern** | Скоро | Централизованная аутентификация + observability для всех вызовов |

## Практический пример

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import os

client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

toolbox_version = client.beta.toolboxes.create_toolbox_version(
    toolbox_name="customer-feedback-triaging-toolbox",
    description="Поиск по документации и ответы на GitHub-issues.",
    tools=[
        {"type": "web_search", "description": "Поиск в публичной документации"},
        {"type": "azure_ai_search", "index_name": "internal-docs"},
        {"type": "mcp_server", "server_url": "https://your-github-mcp-server.com"}
    ]
)
```

После публикации Foundry предоставляет единый эндпоинт. Одно подключение — все инструменты.

## Нет привязки к Foundry Agents

Toolboxes **создаются и управляются** в Foundry, но поверхность потребления — открытый протокол MCP. Их можно использовать из кастомных агентов (Microsoft Agent Framework, LangGraph), GitHub Copilot и других MCP-совместимых IDE.

## Почему это важно сейчас

Волна мульти-агентов добирается до продакшена. Каждый новый агент — это новая поверхность для дублированной конфигурации, устаревших учётных данных и непоследовательного поведения. Основа Build + Consume достаточна, чтобы начать централизацию. Когда придёт столп Govern, появится полностью наблюдаемый, централизованно управляемый инструментальный слой для всего парка агентов.

## Итог

Пока рано — Public Preview, сначала Python SDK, Discover и Govern ещё впереди. Но модель надёжная, а MCP-нативный дизайн означает, что она работает с инструментами, которые уже строятся. Подробности в [официальном анонсе](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/).
