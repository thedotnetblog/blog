---
title: "dotnet new WinUI: Создавайте Windows-приложения без Visual Studio"
date: 2026-05-27
author: "Emiliano Montesdeoca"
description: "Шаблоны проектов WinUI теперь работают с dotnet new — пустые приложения, шаблоны NavigationView и многое другое. Поддержка VS Code, Visual Studio не нужен, с настройками Fluent Design по умолчанию."
tags:
  - WinUI
  - Windows App SDK
  - .NET
  - CLI
  - Visual Studio Code
---

Раньше для разработки WinUI требовался Visual Studio. Это меняется: Microsoft опубликовала шаблоны проектов и элементов с открытым исходным кодом для WinUI, которые работают с `dotnet new`, интегрируя разработку Windows-приложений в стандартный рабочий процесс CLI.

## Начало работы в три команды

```shell
# Установка шаблонов
dotnet new install Microsoft.WindowsAppSDK.WinUI.CSharp.Templates

# Создание приложения NavigationView
dotnet new winui-navview -n MyApp

# Запуск
cd MyApp
dotnet run
```

Никакого Visual Studio, никакой ручной настройки проекта. Приложение запускается через `dotnet run`.

## Что включено

**Пустой шаблон** (`dotnet new winui`) — современная отправная точка с уже настроенной заголовочной панелью Fluent, обновлённой иконкой приложения с ресурсом `.ico` и правильными настройками светлого/тёмного режима по умолчанию. Лучше старого пустого шаблона, где нужно было самому настраивать основы.

**Шаблон NavigationView** (`dotnet new winui-navview`) — паттерн навигации «ведущий-детальный», полностью настроенный с NavigationView, современной заголовочной панелью и многостраничной структурой навигации. Следует стандартному силуэту Windows-приложений для приложений на основе навигации. Если вы строите что-то с боковой навигацией, начните отсюда.

Оба шаблона следуют [силуэтам Windows-приложений](https://learn.microsoft.com/windows/apps/design/basics/app-silhouette) — современным паттернам Fluent Design для макета, навигации и визуальной структуры — прямо из коробки.

## Почему это важно для разработчиков не на Visual Studio

Разработчики WinUI, использующие VS Code, Rider или инструменты командной строки, были в невыгодном положении. Существующие шаблоны Visual Studio нельзя было использовать вне VS — приходилось вручную воссоздавать структуру проекта и настраивать основы.

Эти шаблоны имеют открытый исходный код (см. [WindowsAppSDK PR #6407](https://github.com/microsoft/WindowsAppSDK/pull/6407)), разработаны на основе [отзывов сообщества](https://github.com/microsoft/microsoft-ui-xaml/issues/10388) и доступны прямо сейчас. Поддержка Visual Studio в разработке — эти же шаблоны в конечном счёте будут работать и там.

Для команд, которые хотят автоматизировать настройку проектов WinUI, интегрировать её в CI или просто использовать редактор, отличный от Visual Studio, это существенное улучшение.

Оригинальный пост: [Introducing dotnet new WinUI templates](https://devblogs.microsoft.com/ifdef-windows/introducing-dotnet-new-templates-for-winui/)
