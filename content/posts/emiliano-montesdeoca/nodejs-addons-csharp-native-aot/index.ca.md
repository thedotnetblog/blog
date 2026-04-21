---
title: "Escrivint complements natius de Node.js en C# amb .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "L'equip de C# Dev Kit va substituir els complements de Node.js en C++ per .NET Native AOT — el resultat és més net, més segur i només necessita el .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Aquest article ha estat traduït automàticament. Per a la versió original en anglès, [feu clic aquí]({{< ref "index.md" >}}).*

Aquí teniu un escenari que m'encanta: un equip que treballa en eines .NET tenia complements natius de Node.js escrits en C++ i compilats amb `node-gyp`. Funcionava. Però requeria que Python estigués instal·lat a la màquina de cada desenvolupador — una versió antiga de Python, per cert — només per compilar un paquet que ningú de l'equip tocaria mai directament.

Llavors es van fer una pregunta molt raonable: ja tenim el .NET SDK instal·lat, per què estem escrivint C++ en absolut?

La resposta va ser Native AOT, i el resultat és genuïnament elegant. Drew Noakes de l'equip de C# Dev Kit va descriure com ho van fer, i crec que val la pena entendre-ho fins i tot si no esteu creant extensions de VS Code.

## La idea bàsica

Un complement natiu de Node.js és una biblioteca compartida (`.dll` a Windows, `.so` a Linux, `.dylib` a macOS) que Node.js pot carregar en temps d'execució. La interfície s'anomena [N-API](https://nodejs.org/api/n-api.html) — una API C estable i compatible amb ABI. N-API no li importa quin idioma ha produït la biblioteca, només que exporti els símbols correctes.

.NET Native AOT pot produir exactament això. Compila el vostre codi C# per endavant en una biblioteca compartida nativa amb punts d'entrada arbitraris. Aquest és tot el truc.

## La configuració del projecte

El fitxer de projecte és mínim:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` és el que indica al SDK que produeixi una biblioteca compartida en `dotnet publish`. `AllowUnsafeBlocks` és necessari per a l'interoperabilitat N-API amb punters de funcions i buffers fixes.

## Exportant el punt d'entrada

Node.js espera que la vostra biblioteca exporti `napi_register_module_v1`. En C#, `[UnmanagedCallersOnly]` fa exactament això:

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

`nint` és un enter de mida nativa. El sufix `u8` produeix un `ReadOnlySpan<byte>` amb un literal de cadena UTF-8, passat directament a N-API sense cap assignació d'encoding.

## Resolent N-API contra el procés amfitrió

Les funcions N-API les exporta `node.exe` en si, no una biblioteca separada. Per tant, en lloc d'enllaçar contra alguna cosa, les resoleu contra el procés en execució a l'inici:

```csharp
NativeLibrary.SetDllImportResolver(
    System.Reflection.Assembly.GetExecutingAssembly(),
    ResolveDllImport);

static nint ResolveDllImport(
    string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
{
    if (libraryName is not "node") return 0;
    return NativeLibrary.GetMainProgramHandle();
}
```

Amb això, les vostres declaracions P/Invoke funcionen neta:

```csharp
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
    nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
```

## Cridant-lo des de TypeScript

`dotnet publish` produeix la vostra biblioteca nativa específica de la plataforma. La canvieu de nom a `.node` i l'useu amb un `require()` estàndard:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

Això és tot. TypeScript cap a C#, sense Python, sense C++.

## Conclusions

L'equip de C# Dev Kit va substituir la sobrecàrrega de Python/C++ amb codi C# net que tothom a l'equip ja sap com escriure i depurar. El patró no és complicat un cop el veieu, i és un gran exemple de Native AOT resolent un problema real del qual no es parla prou.

Llegiu la [publicació original al blog de .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
