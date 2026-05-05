---
title: "Pisanie natywnych dodatków Node.js w C# z .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Zespół C# Dev Kit zastąpił dodatki Node.js w C++ przez .NET Native AOT — wynik jest czystszy, bezpieczniejszy i wymaga tylko .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Ten artykuł został przetłumaczony automatycznie. Oryginalną angielską wersję znajdziesz [tutaj]({{< ref "index.md" >}}).*

Oto scenariusz, który uwielbiam: zespół pracujący nad narzędziami .NET miał natywne dodatki Node.js napisane w C++ i kompilowane przez `node-gyp`. Działało. Ale wymagało zainstalowania Pythona na każdej maszynie dewelopera — starej wersji Pythona, nawiasem mówiąc — tylko po to, by skompilować pakiet, którego nikt w zespole nigdy nie dotykał bezpośrednio.

Więc zadali bardzo rozsądne pytanie: mamy już zainstalowany .NET SDK, po co w ogóle piszemy C++?

Odpowiedzią był Native AOT, a wynik jest naprawdę elegancki. Drew Noakes z zespołu C# Dev Kit opisał, jak to zrobili, i uważam, że warto to zrozumieć nawet jeśli nie budujesz rozszerzeń VS Code.

## Podstawowy pomysł

Natywny dodatek Node.js to biblioteka współdzielona (`.dll` na Windows, `.so` na Linux, `.dylib` na macOS), którą Node.js może załadować w czasie wykonywania. Interfejs nazywa się [N-API](https://nodejs.org/api/n-api.html) — stabilne, zgodne z ABI API języka C. N-API nie obchodzi, w jakim języku wyprodukowano bibliotekę, tylko żeby eksportowała właściwe symbole.

.NET Native AOT może dokładnie to zrobić. Kompiluje kod C# z wyprzedzeniem do natywnej biblioteki współdzielonej z dowolnymi punktami wejścia.

## Konfiguracja projektu

Plik projektu jest minimalny:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` mówi SDK, by przy `dotnet publish` wygenerował bibliotekę współdzieloną.

## Eksportowanie punktu wejścia

Node.js oczekuje, że biblioteka wyeksportuje `napi_register_module_v1`. W C# robi to `[UnmanagedCallersOnly]`:

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

Sufiks `u8` tworzy `ReadOnlySpan<byte>` z literałem łańcucha UTF-8, przekazywanym bezpośrednio do N-API bez żadnej alokacji kodowania.

## Rozwiązywanie N-API względem procesu hosta

Funkcje N-API są eksportowane przez sam `node.exe`, nie przez osobną bibliotekę. Zamiast linkować do czegoś, rozwiązujesz je względem działającego procesu przy starcie:

```csharp
NativeLibrary.SetDllImportResolver(
    System.Reflection.Assembly.GetExecutingAssembly(),
    ResolveDllImport);
```

Z tym deklaracje P/Invoke działają czysto:

```csharp
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
    nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
```

## Wywołanie z TypeScript

`dotnet publish` produkuje natywną bibliotekę dla twojej platformy. Zmieniasz jej nazwę na `.node` i używasz ze standardowym `require()`:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

Tyle. TypeScript do C#, bez Pythona, bez C++.

## Podsumowanie

Zespół C# Dev Kit zastąpił narzut Python/C++ czystym kodem C#, który każdy w zespole już umie pisać i debugować. Wzorzec nie jest skomplikowany po tym, jak się go zobaczy, i jest świetnym przykładem Native AOT rozwiązującego realny problem.

Przeczytaj [oryginalny wpis na blogu .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
