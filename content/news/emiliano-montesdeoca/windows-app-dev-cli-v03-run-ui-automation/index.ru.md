---
title: "Windows App Dev CLI v0.3: F5 из терминала и UI-автоматизация для агентов"
date: 2026-04-23
author: "Emiliano Montesdeoca"
description: "Windows App Development CLI v0.3 принес winapp run для отладочного запуска из терминала, winapp ui для автоматизации интерфейса и новый NuGet-пакет, позволяющий dotnet run работать с упакованными приложениями."
tags:
  - windows
  - dotnet
  - winui
  - wpf
  - developer-tools
  - cli
  - ai
---

*Этот пост был автоматически переведён. Оригинал можно найти [здесь]({{< ref "index.md" >}}).*

Опыт F5 в Visual Studio великолепен. Но открывать VS только для запуска и отладки упакованного Windows-приложения — это лишнее, особенно в CI-пайплайне, автоматизированном воркфлоу или когда AI-агент прогоняет тесты.

Windows App Development CLI v0.3 только что [вышел](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/) и решает это напрямую с двумя ключевыми функциями: `winapp run` и `winapp ui`.

## winapp run: F5 из любого места

`winapp run` принимает папку распакованного приложения и манифест, выполняя всё то, что VS делает при отладочном запуске: регистрирует loose-пакет, запускает приложение и сохраняет `LocalState` между повторными деплоями.

```bash
# Собери приложение, затем запусти как упакованное
winapp run ./bin/Debug
```

Работает для WinUI, WPF, WinForms, Console, Avalonia и других. Режимы рассчитаны как на разработчиков, так и на автоматизированные воркфлоу:

- **`--detach`**: Запускает и немедленно возвращает управление терминалу. Идеально для CI.
- **`--unregister-on-exit`**: Удаляет зарегистрированный пакет при закрытии приложения.
- **`--debug-output`**: Захватывает сообщения `OutputDebugString` и исключения в реальном времени.

## Новый NuGet-пакет: dotnet run для упакованных приложений

Для .NET-разработчиков появился новый NuGet-пакет: `Microsoft.Windows.SDK.BuildTools.WinApp`. После установки `dotnet run` берёт на себя весь inner loop: сборка, подготовка loose-layout-пакета, регистрация в Windows и запуск — всё в один шаг.

```bash
winapp init
# или
dotnet add package Microsoft.Windows.SDK.BuildTools.WinApp
```

## winapp ui: UI-автоматизация из командной строки

Это функция, открывающая агентные сценарии. `winapp ui` предоставляет полный доступ UI Automation к любому запущенному Windows-приложению — WPF, WinForms, Win32, Electron, WinUI3 — прямо из терминала.

Что можно делать:

- Перечислить все окна верхнего уровня
- Обходить полное дерево UI Automation любого окна
- Искать элементы по имени, типу или ID автоматизации
- Кликать, вызывать и устанавливать значения
- Делать снимки экрана
- Ждать появления элементов — идеально для синхронизации тестов

Сочетание `winapp ui` с `winapp run` создаёт полный воркфлоу build → запуск → проверка из терминала. Агент может запустить приложение, проверить состояние UI, программно взаимодействовать с ним и валидировать результат.

## Другие нововведения

- **`winapp unregister`**: Удаляет sideloaded-пакет после завершения работы.
- **`winapp manifest add-alias`**: Добавляет алиас для запуска приложения по имени из терминала.
- **Автодополнение**: Одна команда для настройки дополнения в PowerShell.

## Как получить

```bash
winget install Microsoft.WinAppCli
# или
npm install -g @microsoft/winappcli
```

CLI находится в публичном превью. Полная документация — в [репозитории на GitHub](https://github.com/microsoft/WinAppCli), все подробности — в [оригинальном анонсе](https://devblogs.microsoft.com/ifdef-windows/windows-app-development-cli-v0-3-new-run-and-ui-commands-plus-dotnet-run-support-for-packaged-apps/).
