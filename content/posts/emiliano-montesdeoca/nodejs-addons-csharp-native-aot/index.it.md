---
title: "Scrivere addon nativi Node.js in C# con .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Il team di C# Dev Kit ha sostituito gli addon Node.js scritti in C++ con .NET Native AOT — il risultato è più pulito, più sicuro e richiede solo il SDK .NET."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Questo articolo è stato tradotto automaticamente. Per la versione originale in inglese, [clicca qui]({{< ref "index.md" >}}).*

Uno scenario che adoro: un team che lavora su strumenti .NET aveva addon nativi Node.js scritti in C++ e compilati tramite `node-gyp`. Funzionava. Ma richiedeva Python installato su ogni macchina dello sviluppatore — una vecchia versione di Python, per giunta — solo per costruire un pacchetto che nessuno nel team avrebbe mai toccato direttamente.

Si sono quindi posti una domanda molto ragionevole: abbiamo già il SDK .NET installato, perché stiamo scrivendo C++?

La risposta è stata Native AOT, e il risultato è genuinamente elegante.

## L'idea di base

Un addon nativo Node.js è una libreria condivisa (`.dll` su Windows, `.so` su Linux, `.dylib` su macOS) che Node.js può caricare a runtime. L'interfaccia si chiama [N-API](https://nodejs.org/api/n-api.html) — una API C stabile e compatibile con ABI. A N-API non importa quale linguaggio ha prodotto la libreria, solo che esporti i simboli giusti.

.NET Native AOT può produrre esattamente questo. Compila il codice C# ahead-of-time in una libreria nativa condivisa con punti di ingresso arbitrari. Questo è tutto il trucco.

## Setup del progetto

Il file di progetto è minimale:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` dice all'SDK di produrre una libreria condivisa a `dotnet publish`. `AllowUnsafeBlocks` è necessario per l'interop N-API con puntatori a funzione e buffer fissi.

## Esportare il punto di ingresso

Node.js si aspetta che la tua libreria esporti `napi_register_module_v1`. In C#, `[UnmanagedCallersOnly]` fa esattamente questo:

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

Cose da notare: `nint` è un intero di dimensione nativa — l'equivalente gestito di `intptr_t`. Il suffisso `u8` produce un `ReadOnlySpan<byte>` con un letterale stringa UTF-8, passato direttamente a N-API senza alcuna allocazione di encoding. E `[UnmanagedCallersOnly]` esporta il metodo con esattamente il nome del punto di ingresso che Node.js cerca.

## Risolvere N-API contro il processo host

Le funzioni N-API sono esportate da `node.exe` stesso, non da una libreria separata. Quindi invece di linkare contro qualcosa, le si risolve contro il processo in esecuzione all'avvio:

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

Con questo in place, le dichiarazioni P/Invoke funzionano correttamente con `[LibraryImport]` e marshalling generato da sorgente.

## Una funzione esportata reale

Ecco il lettore del registro che hanno costruito:

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

Nota importante sul `try/catch`: un'eccezione non gestita in un metodo `[UnmanagedCallersOnly]` fa crashare il processo host. Cattura sempre e passa a JavaScript tramite `ThrowError`.

## Chiamarlo da TypeScript

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#, senza Python, senza C++.

## Cosa hanno guadagnato

La vittoria immediata è stata nell'esperienza dei contributori: nessuna versione Python specifica necessaria, `yarn install` funziona con solo Node.js e il SDK .NET. Anche le pipeline CI sono diventate più semplici. Le prestazioni sono state comparabili all'implementazione C++.

## Conclusione

Il team C# Dev Kit ha sostituito il carico di Python/C++ con codice C# pulito che tutto il team sa già scrivere e debuggare. Per il walkthrough completo con tutti gli helper di marshalling delle stringhe, dai un'occhiata all'[articolo originale sul blog .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
