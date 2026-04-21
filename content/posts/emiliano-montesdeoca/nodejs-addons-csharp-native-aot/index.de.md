---
title: "Node.js Native Addons in C# mit .NET Native AOT schreiben"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Das C# Dev Kit-Team ersetzte C++ Node.js-Addons durch .NET Native AOT — das Ergebnis ist sauberer, sicherer und benötigt nur das .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Dieser Beitrag wurde automatisch übersetzt. Die englische Originalversion findest du [hier]({{< ref "index.md" >}}).*

Dieses Szenario gefällt mir: Ein Team, das an .NET-Tooling arbeitet, hatte native Node.js-Addons, die in C++ geschrieben und über `node-gyp` kompiliert wurden. Es funktionierte. Aber es erforderte Python auf jeder Entwicklermaschine — eine alte Python-Version wohlgemerkt — nur um ein Paket zu bauen, das niemand im Team direkt anfassen würde.

Also stellten sie eine sehr vernünftige Frage: Wir haben das .NET SDK bereits installiert, warum schreiben wir überhaupt C++?

Die Antwort war Native AOT, und das Ergebnis ist wirklich elegant. Drew Noakes vom C# Dev Kit-Team hat dokumentiert, wie sie es gemacht haben, und ich denke, es lohnt sich, das zu verstehen — auch wenn du keine VS Code-Extensions baust.

## Die Grundidee

Ein nativer Node.js-Addon ist eine Shared Library (`.dll` unter Windows, `.so` unter Linux, `.dylib` unter macOS), die Node.js zur Laufzeit laden kann. Die Schnittstelle heißt [N-API](https://nodejs.org/api/n-api.html) — eine stabile, ABI-kompatible C-API. N-API kümmert sich nicht darum, welche Sprache die Library produziert hat, nur dass sie die richtigen Symbole exportiert.

.NET Native AOT kann genau das produzieren. Es kompiliert C#-Code ahead-of-time in eine native Shared Library mit beliebigen Einstiegspunkten. Das ist der ganze Trick.

## Projekt-Setup

Die Projektdatei ist minimal:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` weist das SDK an, bei `dotnet publish` eine Shared Library zu produzieren. `AllowUnsafeBlocks` wird für das N-API-Interop mit Funktionszeigern und Fixed Buffers benötigt.

## Den Einstiegspunkt exportieren

Node.js erwartet, dass deine Library `napi_register_module_v1` exportiert. In C# macht `[UnmanagedCallersOnly]` genau das:

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

Ein paar Dinge, die erwähnenswert sind: `nint` ist ein nativer Integer — das verwaltete Äquivalent von `intptr_t`. Das `u8`-Suffix produziert einen `ReadOnlySpan<byte>` mit einem UTF-8-String-Literal, direkt an N-API übergeben ohne jede Encoding-Allokation. Und `[UnmanagedCallersOnly]` exportiert die Methode mit genau dem Einstiegspunkt-Namen, den Node.js sucht.

## N-API gegen den Host-Prozess auflösen

N-API-Funktionen werden von `node.exe` selbst exportiert, nicht von einer separaten Library. Statt gegen etwas zu linken, werden sie beim Start gegen den laufenden Prozess aufgelöst:

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

Damit funktionieren P/Invoke-Deklarationen sauber mit `[LibraryImport]` und quellegenerierten Marshalling.

## Eine echte exportierte Funktion

Hier ist der Registry-Reader, den sie gebaut haben:

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

Wichtiger Hinweis zum `try/catch`: Eine unbehandelte Exception in einer `[UnmanagedCallersOnly]`-Methode stürzt den Host-Prozess ab. Immer abfangen und via `ThrowError` an JavaScript weiterleiten.

## Von TypeScript aufrufen

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#, kein Python, kein C++.

## Was sie gewonnen haben

Der sofortige Gewinn war die Contributor-Experience: keine bestimmte Python-Version mehr nötig, `yarn install` funktioniert mit Node.js und dem .NET SDK. CI-Pipelines wurden ebenfalls einfacher. Die Performance war vergleichbar mit der C++-Implementierung.

## Fazit

Das C# Dev Kit-Team ersetzte Python/C++-Overhead durch sauberen C#-Code, den jeder im Team schon kann. Den vollständigen Walkthrough mit allen String-Marshalling-Helfern findest du im [Originalartikel auf dem .NET-Blog](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
