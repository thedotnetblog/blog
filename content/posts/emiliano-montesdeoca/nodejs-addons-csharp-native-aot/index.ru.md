---
title: "Написание нативных аддонов Node.js на C# с .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Команда C# Dev Kit заменила аддоны Node.js на C++ аналогами на .NET Native AOT — результат чище, безопаснее и требует только .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Эта статья переведена автоматически. Оригинальную версию на английском можно найти [здесь]({{< ref "index.md" >}}).*

Вот сценарий, который мне нравится: команда, работающая над инструментами .NET, имела нативные аддоны Node.js, написанные на C++ и скомпилированные через `node-gyp`. Работало. Но для сборки пакета, который никто в команде не трогал напрямую, на каждой машине разработчика требовался Python — причём старая версия Python.

Поэтому они задали вполне разумный вопрос: SDK .NET уже установлен — зачем вообще писать C++?

Ответом стал Native AOT, и результат получился действительно элегантным.

## Основная идея

Нативный аддон Node.js — это разделяемая библиотека (`.dll` на Windows, `.so` на Linux, `.dylib` на macOS), которую Node.js может загрузить во время выполнения. Интерфейс называется [N-API](https://nodejs.org/api/n-api.html) — стабильный, ABI-совместимый C API. N-API не заботится о том, каким языком создана библиотека — только о том, что она экспортирует нужные символы.

.NET Native AOT может создать именно это. Он компилирует C#-код ahead-of-time в нативную разделяемую библиотеку с произвольными точками входа. В этом весь трюк.

## Настройка проекта

Файл проекта минимален:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` указывает SDK создать разделяемую библиотеку при `dotnet publish`. `AllowUnsafeBlocks` нужен для N-API interop с указателями на функции и фиксированными буферами.

## Экспорт точки входа

Node.js ожидает, что библиотека экспортирует `napi_register_module_v1`. В C# это делает `[UnmanagedCallersOnly]`:

```csharp
public static unsafe partial class RegistryAddon
{
    [UnmanagedCallersOnly(
        EntryPoint = "napi_register_module_v1",
        CallConvs = [typeof(CallConvCdecl)])]
    public static nint Init(nint env, nint exports)
    {
        Initialize();
        RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
        return exports;
    }
}
```

Несколько моментов стоит отметить: `nint` — целое число нативного размера, управляемый эквивалент `intptr_t`. Суффикс `u8` создаёт `ReadOnlySpan<byte>` с UTF-8 строковым литералом, передаваемым прямо в N-API без выделений памяти под кодировку. А `[UnmanagedCallersOnly]` экспортирует метод с точно тем именем точки входа, которое ищет Node.js.

## Разрешение N-API через хост-процесс

Функции N-API экспортирует сам `node.exe`, а не отдельная библиотека. Поэтому вместо линковки против чего-либо, они разрешаются против запущенного процесса при старте:

```csharp
private static void Initialize()
{
    NativeLibrary.SetDllImportResolver(
        System.Reflection.Assembly.GetExecutingAssembly(),
        ResolveDllImport);

    static nint ResolveDllImport(
        string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
    {
        if (libraryName is not "node") return 0;
        return NativeLibrary.GetMainProgramHandle();
    }
}
```

После этого объявления P/Invoke с `[LibraryImport]` и сгенерированным маршалингом работают корректно.

## Реальная экспортируемая функция

Вот ридер реестра, который они написали:

```csharp
[UnmanagedCallersOnly(CallConvs = [typeof(CallConvCdecl)])]
private static nint ReadStringValue(nint env, nint info)
{
    try
    {
        var keyPath = GetStringArg(env, info, 0);
        var valueName = GetStringArg(env, info, 1);

        if (keyPath is null || valueName is null)
        {
            ThrowError(env, "Expected two string arguments: keyPath, valueName");
            return 0;
        }

        using var key = Registry.CurrentUser.OpenSubKey(keyPath, writable: false);

        return key?.GetValue(valueName) is string value
            ? CreateString(env, value)
            : GetUndefined(env);
    }
    catch (Exception ex)
    {
        ThrowError(env, $"Registry read failed: {ex.Message}");
        return 0;
    }
}
```

Важное замечание про `try/catch`: необработанное исключение в методе `[UnmanagedCallersOnly]` обрушит хост-процесс. Всегда перехватывайте и передавайте в JavaScript через `ThrowError`.

## Вызов из TypeScript

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#, без Python, без C++.

## Что получили

Мгновенный выигрыш — опыт контрибьюторов: никакой конкретной версии Python, `yarn install` работает только с Node.js и .NET SDK. CI-пайплайны также упростились. Производительность сопоставима с реализацией на C++.

## Итоги

Команда C# Dev Kit заменила сложность Python/C++ на чистый C#-код, который каждый в команде уже умеет писать и отлаживать. Полный разбор со всеми вспомогательными методами маршалинга строк найдёте в [оригинальной статье в блоге .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
