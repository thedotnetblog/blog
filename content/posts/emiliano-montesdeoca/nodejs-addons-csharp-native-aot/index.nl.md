---
title: "Native Node.js-addons schrijven in C# met .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Het C# Dev Kit-team verving C++ Node.js-addons door .NET Native AOT — het resultaat is schoner, veiliger en heeft alleen de .NET SDK nodig."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Dit artikel is automatisch vertaald. Voor de originele Engelse versie, [klik hier]({{< ref "index.md" >}}).*

Hier is een scenario dat ik geweldig vind: een team dat werkt aan .NET-tooling had native Node.js-addons geschreven in C++ en gecompileerd via `node-gyp`. Het werkte. Maar het vereiste Python op elke machine van een ontwikkelaar — een oude versie van Python, let wel — alleen om een pakket te compileren dat niemand in het team ooit rechtstreeks zou aanraken.

Dus stelden ze een heel redelijke vraag: we hebben de .NET SDK al geïnstalleerd, waarom schrijven we überhaupt C++?

Het antwoord was Native AOT, en het resultaat is oprecht elegant. Drew Noakes van het C# Dev Kit-team schreef op hoe ze het aanpakten.

## Het basisidee

Een native Node.js-addon is een gedeelde bibliotheek (`.dll` op Windows, `.so` op Linux, `.dylib` op macOS) die Node.js tijdens runtime kan laden. De interface heet [N-API](https://nodejs.org/api/n-api.html) — een stabiele, ABI-compatibele C API. N-API maakt niet uit welke taal de bibliotheek heeft geproduceerd, alleen dat die de juiste symbolen exporteert.

.NET Native AOT kan precies dat produceren. Het compileert je C#-code ahead-of-time naar een native gedeelde bibliotheek met willekeurige invoerpunten.

## De projectconfiguratie

Het projectbestand is minimaal:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` vertelt de SDK om een gedeelde bibliotheek te produceren bij `dotnet publish`.

## Het invoerpunt exporteren

Node.js verwacht dat jouw bibliotheek `napi_register_module_v1` exporteert. In C# doet `[UnmanagedCallersOnly]` precies dat:

```csharp
[UnmanagedCallersOnly(
    EntryPoint = "napi_register_module_v1",
    CallConvs = [typeof(CallConvCdecl)])]
public static nint Init(nint env, nint exports)
{
    Initialize();
    RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
    return exports;
}
```

Het `u8`-achtervoegsel produceert een `ReadOnlySpan<byte>` met een UTF-8 string-literal, rechtstreeks doorgegeven aan N-API zonder enige coderingstoewijzing.

## N-API oplossen tegen het hostproces

N-API-functies worden geëxporteerd door `node.exe` zelf, niet door een aparte bibliotheek. Dus in plaats van ergens tegen te linken, los je ze op tegen het actieve proces bij opstarten:

```csharp
NativeLibrary.SetDllImportResolver(
    System.Reflection.Assembly.GetExecutingAssembly(),
    ResolveDllImport);
```

Daarmee werken P/Invoke-declaraties netjes:

```csharp
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
    nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
```

## Aanroepen vanuit TypeScript

`dotnet publish` produceert jouw platformspecifieke native bibliotheek. Hernoem het naar `.node` en gebruik het met een standaard `require()`:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

Dat is het. TypeScript naar C#, geen Python, geen C++.

## Samenvatting

Het C# Dev Kit-team verving de overhead van Python/C++ door schone C#-code die iedereen in het team al weet hoe te schrijven en debuggen. Het patroon is niet ingewikkeld zodra je het ziet, en het is een geweldig voorbeeld van Native AOT die een echt probleem oplost dat niet genoeg wordt besproken.

Lees de [originele blogpost op het .NET-blog](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
