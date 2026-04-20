---
title: "C# 15 Union Type'ları Alıyor — Ve Bunlar Tam İstediğimiz Şey"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15, `union` anahtar kelimesini tanıtıyor — derleyici tarafından zorunlu kılınan kapsamlı örüntü eşleştirmeli ayrıştırılmış birleşimler. Nasıl göründükleri, neden önemli oldukları ve bugün nasıl deneyebileceğiniz."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

İşte beklediğim şey bu. C# 15, `union` anahtar kelimesini tanıtıyor — derleyici tarafından zorunlu kılınan kapsamlı örüntü eşleştirmeli gerçek ayrıştırılmış birleşimler.

Bill Wagner [derin incelemeyi yayımladı](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/).

## Birleşimlerin çözdüğü sorun

C# 15 öncesinde, bir metoddan "birçok olası türden birini" döndürmek her zaman bir uzlaşmaydı. Derleyicinin her durumu ele aldığınızı garanti ettiği kapalı bir tür kümesi hiç elde edemiyordunuz.

## Sözdizimi güzelce basit

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Ve işte sihir — derleyici kapsamlı eşleştirmeyi zorunlu kılar:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

`_` atmaya gerek yok. Birleşime dördüncü bir tür eklerseniz, onu ele almayan her switch ifadesi uyarı üretir.

## Pratik kullanım

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Artık her tüketici başarı, hata ve doğrulama başarısızlığını ele almak zorunda.

## Bugün deneyin

Union type'ları .NET 11 Preview 2'de mevcut. [Tam dil referansına](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) bakın.
