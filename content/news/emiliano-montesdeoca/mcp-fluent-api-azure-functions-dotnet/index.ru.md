---
title: "MCP Apps получили Fluent API — Создавайте богатые UI для AI-инструментов на .NET за три шага"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Новый Fluent API конфигурации для MCP Apps на Azure Functions позволяет превратить любой .NET MCP-инструмент в полноценное приложение с представлениями, разрешениями и CSP-политиками всего в несколько строк кода."
tags:
  - mcp
  - dotnet
  - azure-functions
  - ai
  - azure-sdk
---

> *Этот пост был переведён автоматически. Оригинал можно прочитать [здесь]({{< ref "mcp-fluent-api-azure-functions-dotnet.md" >}}).*

MCP-инструменты отлично подходят для наделения AI-агентов возможностями. Но что, если вашему инструменту нужно показать что-то пользователю — дашборд, форму, интерактивную визуализацию? Именно для этого и существуют MCP Apps, и теперь их стало намного проще создавать.

Лилиан Касем из команды Azure SDK [представила новый Fluent API конфигурации](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) для MCP Apps на .NET Azure Functions — это такое улучшение опыта разработчика, что невольно задаёшься вопросом, почему так просто не было всегда.

## Что такое MCP Apps?

MCP Apps расширяют Model Context Protocol, позволяя инструментам нести собственные UI-представления, статические ресурсы и средства управления безопасностью. Вместо простого возврата текста ваш MCP-инструмент может отрисовывать полноценные HTML-интерфейсы — интерактивные дашборды, визуализации данных, формы конфигурации — всё это вызывается AI-агентами и отображается пользователям через MCP-клиенты.

Проблема была в том, что ручная настройка всего этого требовала глубокого знания спецификации MCP: URI `ui://`, специальные MIME-типы, координация метаданных между инструментами и ресурсами. Не сложно, но утомительно.

## Fluent API за три шага

**Шаг 1: Определите свою функцию.** Стандартный MCP-инструмент Azure Functions:

```csharp
[Function(nameof(HelloApp))]
public string HelloApp(
    [McpToolTrigger("HelloApp", "A simple MCP App that says hello.")]
    ToolInvocationContext context)
{
    return "Hello from app";
}
```

**Шаг 2: Преобразуйте его в MCP App.** В стартапе вашей программы:

```csharp
builder.ConfigureMcpTool("HelloApp")
    .AsMcpApp(app => app
        .WithView("assets/hello-app.html")
        .WithTitle("Hello App")
        .WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
        .WithCsp(csp =>
        {
            csp.AllowBaseUri("https://www.microsoft.com")
               .ConnectTo("https://www.microsoft.com");
        }));
```

**Шаг 3: Добавьте HTML-представление.** Создайте `assets/hello-app.html` с нужным вам интерфейсом.

Вот и всё. Fluent API берёт на себя всю сантехнику MCP-протокола — генерирует синтетическую ресурсную функцию, устанавливает правильный MIME-тип и внедряет метаданные, связывающие ваш инструмент с его представлением.

## API спроектирован отлично

Несколько вещей, которые мне особенно нравятся:

**Источники представлений гибкие.** Можно отдавать HTML из файлов на диске или встраивать ресурсы прямо в сборку для автономных развёртываний:

```csharp
app.WithView(McpViewSource.FromFile("assets/my-view.html"))
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
```

**CSP компонуемый.** Вы явно разрешаете источники, необходимые вашему приложению, следуя принципу наименьших привилегий. Вызывайте `WithCsp` несколько раз — источники накапливаются:

```csharp
.WithCsp(csp =>
{
    csp.ConnectTo("https://api.example.com")
       .LoadResourcesFrom("https://cdn.example.com")
       .AllowFrame("https://youtube.com");
})
```

**Управление видимостью.** Можно сделать инструмент видимым только для LLM, только для UI хоста или для обоих. Хотите инструмент, который только отрисовывает UI и не должен вызываться моделью? Легко:

```csharp
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
```

## Начало работы

Добавьте превью-пакет:

```bash
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0-preview.1
```

Если вы уже создаёте MCP-инструменты с Azure Functions, это просто обновление пакета. [Быстрый старт MCP Apps](https://learn.microsoft.com/azure/azure-functions/scenario-mcp-apps?tabs=bash%2Clinux&pivots=programming-language-csharp) — лучшее место для начала, если вы новичок в этой концепции.

## Подводя итоги

MCP Apps — одно из самых захватывающих нововведений в пространстве AI-инструментов: инструменты, которые не просто *делают что-то*, но могут *показывать что-то* пользователям. Fluent API убирает сложность протокола и позволяет сосредоточиться на главном: логике вашего инструмента и его интерфейсе.

Прочитайте [полный пост](https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/) для полного справочника по API и примеров.
