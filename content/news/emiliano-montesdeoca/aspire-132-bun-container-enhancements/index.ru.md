---
title: "Aspire 13.2: Поддержка Bun, Улучшенные Контейнеры и Меньше Трений при Отладке"
date: 2026-04-24
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 добавляет первоклассную поддержку Bun для Vite-приложений, исправляет надёжность Yarn и улучшает контейнеры, делая поведение при локальной разработке более предсказуемым."
tags:
  - "Aspire"
  - ".NET Aspire"
  - "Containers"
  - "JavaScript"
  - "Developer Productivity"
---

*Этот пост был автоматически переведён. Для оригинальной версии [нажмите здесь](https://thedotnetblog.com/posts/emiliano-montesdeoca/aspire-132-bun-container-enhancements/).*

Если вы строите .NET-бэкенды с JavaScript-фронтендами в Aspire, 13.2 — это обновление, которое тихо делает ваш день лучше.

## Bun теперь первоклассный

```typescript
await builder
  .addViteApp("frontend", "./frontend")
  .withBun();
```

Если ваша команда уже использует Bun, Aspire больше не заставляет плыть против течения.

## Yarn стал надёжнее

Пользователи Yarn получают меньше загадочных сбоев с `withYarn()` и `addViteApp()`.

## Улучшения контейнеров

`ImagePullPolicy.Never` для использования локального образа без обращения к registry. PostgreSQL 18+ с томами данных теперь работает корректно.

## Улучшения отладки

`DebuggerDisplayAttribute` на основных типах, лучшие сообщения об ошибках для `WaitFor`, `BeforeResourceStartedEvent` срабатывает в нужный момент.

Оригинальный пост Дэвида Пайна: [Aspire 13.2: Bun Support and Container Enhancements](https://devblogs.microsoft.com/aspire/aspire-bun-support-and-container-enhancements/).
