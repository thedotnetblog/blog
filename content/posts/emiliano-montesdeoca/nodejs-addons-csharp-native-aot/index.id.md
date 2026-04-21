---
title: "Menulis Native Addon Node.js dalam C# dengan .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "Tim C# Dev Kit mengganti addon Node.js berbasis C++ dengan .NET Native AOT — hasilnya lebih bersih, lebih aman, dan hanya butuh .NET SDK."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Artikel ini diterjemahkan secara otomatis. Untuk versi asli dalam bahasa Inggris, [klik di sini]({{< ref "index.md" >}}).*

Ini skenario yang saya suka: sebuah tim yang mengerjakan tooling .NET memiliki native addon Node.js yang ditulis dalam C++ dan dikompilasi via `node-gyp`. Berhasil. Tapi itu mengharuskan Python terinstall di setiap mesin developer — versi Python yang lama, perlu dicatat — hanya untuk membangun sebuah paket yang tidak akan pernah disentuh langsung oleh siapapun di tim.

Jadi mereka mengajukan pertanyaan yang sangat masuk akal: kita sudah punya .NET SDK terinstall, kenapa kita masih menulis C++?

Jawabannya adalah Native AOT, dan hasilnya sungguh elegan. Drew Noakes dari tim C# Dev Kit menulis bagaimana mereka melakukannya.

## Ide dasarnya

Native addon Node.js adalah shared library (`.dll` di Windows, `.so` di Linux, `.dylib` di macOS) yang bisa dimuat Node.js saat runtime. Antarmukanya disebut [N-API](https://nodejs.org/api/n-api.html) — C API yang stabil dan kompatibel dengan ABI. N-API tidak peduli bahasa apa yang menghasilkan library tersebut, hanya bahwa ia mengekspor simbol yang tepat.

.NET Native AOT bisa menghasilkan tepat itu. Ia mengkompilasi kode C# kamu ahead-of-time menjadi shared library native dengan entry point sembarang.

## Konfigurasi proyek

File proyek sangat minimal:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` memberitahu SDK untuk menghasilkan shared library saat `dotnet publish`.

## Mengekspor entry point

Node.js mengharapkan library kamu mengekspor `napi_register_module_v1`. Dalam C#, `[UnmanagedCallersOnly]` melakukan persis itu:

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

Sufiks `u8` menghasilkan `ReadOnlySpan<byte>` dengan string literal UTF-8, diteruskan langsung ke N-API tanpa alokasi encoding apapun.

## Resolving N-API terhadap proses host

Fungsi N-API diekspor oleh `node.exe` sendiri, bukan library terpisah. Jadi alih-alih melakukan linking, kamu me-resolve-nya terhadap proses yang berjalan saat startup:

```csharp
NativeLibrary.SetDllImportResolver(
    System.Reflection.Assembly.GetExecutingAssembly(),
    ResolveDllImport);
```

Dengan itu, deklarasi P/Invoke bekerja dengan bersih:

```csharp
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
    nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
```

## Memanggil dari TypeScript

`dotnet publish` menghasilkan native library spesifik platform kamu. Ganti namanya menjadi `.node` dan gunakan dengan `require()` standar:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

Itu saja. TypeScript ke C#, tanpa Python, tanpa C++.

## Kesimpulan

Tim C# Dev Kit mengganti overhead Python/C++ dengan kode C# yang bersih yang sudah bisa ditulis dan di-debug oleh semua orang di tim. Polanya tidak rumit setelah kamu melihatnya, dan ini adalah contoh bagus dari Native AOT yang memecahkan masalah nyata yang jarang dibicarakan.

Baca [posting aslinya di blog .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
