---
title: "Поддержка SDK-стиля для проектов расширений в Visual Studio"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 добавляет официально поддерживаемый формат проекта SDK-style для расширений VSSDK, сокращая время сборки до 75% и упрощая файлы проектов до ~20 строк."
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*Этот пост был переведён автоматически. Для оригинальной версии [нажмите здесь]({{< ref "index.md" >}}).*

[Поддержка SDK-стиля для проектов расширений VSSDK](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/) теперь официально доступна в Visual Studio 18.5 — классические проекты расширений VSIX могут отказаться от старого формата `.csproj` в стиле MPF.

## Что меняется в файле проекта

Самое заметное изменение — насколько меньше становится файл проекта. Типичное расширение VSSDK теперь выглядит так:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net472</TargetFramework>
    <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup>
    <VsixDeployOnDebug>true</VsixDeployOnDebug>
    <GeneratePkgDefFile>true</GeneratePkgDefFile>
  </PropertyGroup>
  <ItemGroup><ProjectCapability Include="CreateVsixContainer" /></ItemGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.VisualStudio.SDK" Version="17.14.40265" ExcludeAssets="runtime" />
    <PackageReference Include="Microsoft.VSSDK.BuildTools" Version="18.5.38461" />
  </ItemGroup>
</Project>
```

`VSSDKBuildToolsAutoSetup=true` применяет разумные значения по умолчанию: `CreateVsixContainer=true` и устаревшее `DeployExtension=false`. Это единственное свойство заменяет значительную часть того, что раньше приходилось указывать явно.

## Улучшение времени сборки

Включены Fast Up-To-Date Check и поддержка инкрементальной сборки. Для больших решений с небольшими изменениями это даёт **сокращение времени сборки до 75%** — существенное, если вы итерируете над расширением в рамках большого хост-решения.

## Новые vs. существующие проекты

Новые проекты расширений, созданные в 18.5, автоматически используют SDK-стиль. Существующие расширения в стиле MPF продолжают работать — миграция необязательна. Важный момент при миграции: добавьте `<UseWpf>true</UseWpf>`, если расширение использует XAML. Также необходимо пометить расширение как развёртываемое в файле `.sln` или `.slnx`.

Дизайнер vsixmanifest по умолчанию заменён XML-редактором — правый клик → Открыть с помощью, если нужен старый дизайнер.

## Агентный путь миграции

Агент Modernize в [vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) может автоматизировать миграцию. Несколько реальных расширений уже были конвертированы таким образом: Smart Screen, Command Explorer, Postfix Templates и Whitespace Visualizer от Mads Kristensen.

## Важно отметить

VisualStudio.Extensibility (более новый фреймворк расширяемости) уже поддерживал SDK-стиль. Это обновление обеспечивает паритет с классическим путём VSSDK. Единственное требование — рабочая нагрузка разработки расширений Visual Studio.

Полные сведения в [официальном посте](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/).
