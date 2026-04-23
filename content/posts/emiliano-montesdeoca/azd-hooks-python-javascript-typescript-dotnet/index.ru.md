---
title: "Хуки azd на Python, TypeScript и .NET: прощай, shell-скрипты"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Azure Developer CLI теперь поддерживает хуки на Python, JavaScript, TypeScript и .NET. Больше не нужно переключаться на Bash ради одного скрипта миграции."
tags:
  - azure-developer-cli
  - azd
  - dotnet
  - python
  - typescript
  - developer-tools
  - cloud-native
---

*Этот пост был автоматически переведён. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

Если вы когда-нибудь вели проект полностью на .NET и всё равно писали Bash-скрипты для хуков azd — вы знаете эту боль. Зачем переходить к синтаксису shell в шаге pre-provisioning, когда весь остальной проект написан на C#?

Эта проблема теперь решена официально. Azure Developer CLI [выпустила поддержку нескольких языков для хуков](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/), и это ровно так хорошо, как звучит.

## Что такое хуки

Хуки — это скрипты, выполняемые в ключевых точках жизненного цикла `azd` — до провизионинга, после деплоя и не только. Они определяются в `azure.yaml` и позволяют внедрять пользовательскую логику без изменений в CLI.

Раньше поддерживались только Bash и PowerShell. Теперь можно использовать **Python, JavaScript, TypeScript или .NET** — остальное `azd` обрабатывает автоматически.

## Как работает определение языка

Просто укажите хук на файл, и `azd` определит язык по расширению:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.py
  postdeploy:
    run: ./hooks/seed.ts
  postprovision:
    run: ./hooks/migrate.cs
```

Дополнительная конфигурация не нужна. При неоднозначном расширении можно явно указать `kind: python` (или нужный язык).

## Важные детали по языкам

### Python

Разместите `requirements.txt` или `pyproject.toml` рядом со скриптом (или в родительской директории). `azd` автоматически создаёт виртуальное окружение, устанавливает зависимости и запускает скрипт.

### JavaScript и TypeScript

Тот же принцип — `package.json` рядом со скриптом, и `azd` сначала выполнит `npm install`. Для TypeScript используется `npx tsx` без этапа компиляции и без `tsconfig.json`.

### .NET

Два режима:

- **Режим проекта**: если рядом со скриптом есть `.csproj`, `azd` автоматически выполнит `dotnet restore` и `dotnet build`.
- **Single-file режим**: на .NET 10+ автономные `.cs`-файлы запускаются напрямую через `dotnet run script.cs`. Файл проекта не нужен.

## Конфигурация по исполнителю

Каждый язык поддерживает опциональный блок `config`:

```yaml
hooks:
  preprovision:
    run: ./hooks/setup.ts
    config:
      packageManager: pnpm
  postprovision:
    run: ./hooks/migrate.cs
    config:
      configuration: Release
      framework: net10.0
```

## Почему это важно для .NET-разработчиков

Хуки были последним местом в проекте на базе azd, где приходилось менять язык. Теперь весь деплой-пайплайн — от кода приложения до lifecycle-хуков — может жить в одном языке. Можно переиспользовать существующие .NET-утилиты, ссылаться на общие библиотеки и забыть про поддержку shell-скриптов.

## Итог

Одно из тех изменений, что выглядят незначительными, но убирают много трения из повседневной работы с azd. Поддержка нескольких языков для хуков доступна прямо сейчас — подробная документация в [официальном посте](https://devblogs.microsoft.com/azure-sdk/azd-multi-language-hooks/).
