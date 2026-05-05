---
title: "VS Code 1.118: Copilot CLI получает имена сессий, значки модели и TypeScript 7.0 Nightly"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Visual Studio Code 1.118 — сфокусированный релиз с улучшениями Copilot CLI: именование сессий, значки модели, автоматический выбор модели и подключение TypeScript 7.0 Nightly."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
  - TypeScript
---

*Этот пост был переведён автоматически. Для просмотра оригинала [нажмите здесь]({{< ref "index.md" >}}).*

[Visual Studio Code 1.118](https://code.visualstudio.com/updates/v1_118) — небольшой сфокусированный релиз, в основном с улучшениями Copilot CLI.

## Copilot CLI: сессии получают настоящие имена

API заголовков сессий SDK Copilot CLI теперь используются как источник истины для имён сессий. Вместо автоматически сгенерированных меток сессии показывают реальное имя из SDK.

## Быстрое переключение между сессиями

В приложение Agents теперь добавлены `Ctrl+1`, `Ctrl+2` и т.д. для быстрого переключения между сессиями.

## Значки модели в чате

Ответы Copilot CLI в панели чата теперь показывают значок модели — можно с первого взгляда понять, какая модель обработала каждый запрос.

## Автоматический выбор модели в Copilot CLI

Функция автоматического выбора модели теперь работает и в агенте Copilot CLI.

## Подключение TypeScript 7.0 Nightly

Теперь можно включить тестирование ночных сборок TypeScript 7.0 прямо из настроек VS Code. TypeScript 7.0 — значительный релиз ([бета вышла несколько дней назад](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-beta/)).

Смотрите [полные примечания к релизу](https://code.visualstudio.com/updates/v1_118).
