---
title: "Node.js için C# ile .NET Native AOT Kullanarak Yerel Eklenti Yazma"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "C# Dev Kit ekibi C++ Node.js eklentilerini .NET Native AOT ile değiştirdi — sonuç daha temiz, daha güvenli ve yalnızca .NET SDK gerektiriyor."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Bu makale otomatik olarak çevrilmiştir. Orijinal İngilizce sürüm için [buraya tıklayın]({{< ref "index.md" >}}).*

İşte sevdiğim bir senaryo: .NET araçları üzerinde çalışan bir ekibin `node-gyp` ile derlenen C++ ile yazılmış yerel Node.js eklentileri vardı. Çalışıyordu. Ama her geliştiricinin makinesinde Python'un yüklü olmasını gerektiriyordu — Python'un eski bir sürümü, dahası — sadece ekipten kimsenin hiç doğrudan dokunmayacağı bir paketi derlemek için.

Bunun üzerine çok makul bir soru sordular: zaten .NET SDK yüklüyken neden C++ yazıyoruz ki?

Cevap Native AOT oldu ve sonuç gerçekten zarif. C# Dev Kit ekibinden Drew Noakes bunu nasıl yaptıklarını anlattı.

## Temel fikir

Node.js yerel eklentisi, Node.js'nin çalışma zamanında yükleyebildiği bir paylaşılan kütüphanedir (Windows'ta `.dll`, Linux'ta `.so`, macOS'ta `.dylib`). Arayüze [N-API](https://nodejs.org/api/n-api.html) denir — kararlı, ABI uyumlu bir C API'si. N-API'nin kütüphaneyi hangi dilin ürettiğini umursamaz, sadece doğru sembolleri dışa aktarmasını önemser.

.NET Native AOT tam olarak bunu yapabilir. C# kodunuzu önceden isteğe bağlı giriş noktalarıyla yerel paylaşılan kütüphaneye derler.

## Proje kurulumu

Proje dosyası minimumdur:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot`, SDK'ya `dotnet publish`'te paylaşılan kütüphane üretmesini söyler.

## Giriş noktasını dışa aktarma

Node.js, kütüphanenizin `napi_register_module_v1`'i dışa aktarmasını bekler. C#'ta `[UnmanagedCallersOnly]` tam olarak bunu yapar:

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

`u8` soneki, herhangi bir encoding tahsisi olmadan doğrudan N-API'ye geçirilen UTF-8 string literaliyle bir `ReadOnlySpan<byte>` üretir.

## TypeScript'ten çağırma

`dotnet publish`, platforma özgü yerel kütüphanenizi üretir. Onu `.node` olarak yeniden adlandırın ve standart `require()` ile kullanın:

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk',
    'InstallLocation'
);
```

İşte bu kadar. TypeScript'ten C#'a, Python yok, C++ yok.

## Sonuç

C# Dev Kit ekibi Python/C++ yükünü, ekipteki herkesin zaten nasıl yazılacağını ve hata ayıklayacağını bildiği temiz C# koduyla değiştirdi. Bu desen göründükten sonra karmaşık değil ve Native AOT'nun yeterince konuşulmayan gerçek bir sorunu çözdüğünün harika bir örneği.

[.NET blogundaki orijinal yazıyı okuyun](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
