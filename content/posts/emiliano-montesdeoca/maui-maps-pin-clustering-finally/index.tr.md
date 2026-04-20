---
title: "Pin Kümeleme Sonunda .NET MAUI Maps'e Geldi — Bir Özellik, Sıfır Acı"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3, Map kontrolüne native pin kümeleme ekliyor. Bir özellik, ayrı kümeleme grupları ve dokunma işleme — hepsi yerleşik."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "maui-maps-pin-clustering-finally" >}}).*

Yüz pin ile harita yüklediğinizde her şeyin okunaksız bir kütleye dönüştüğü o anı biliyor musunuz? Bu, .NET MAUI Maps deneyimiydi — ta şimdiye kadar.

David Ortinau [henüz duyurdu](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) ki .NET MAUI 11 Preview 3, Android ve iOS/Mac Catalyst'te kutusundan pin kümeleme sunuyor.

## Hepsini yönetecek tek özellik

```xml
<maps:Map IsClusteringEnabled="True" />
```

Hepsi bu. Yakın pinler, sayı rozetiyle kümelere gruplandırılır.

## Bağımsız kümeleme grupları

`ClusteringIdentifier` özelliği, pinleri bağımsız gruplara ayırmanıza olanak tanır:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});
```

## Küme dokunuşunu işleme

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("
", e.Pins.Select(p => p.Label));
    await DisplayAlert($"Cluster ({e.Pins.Count} pins)", names, "OK");
};
```

## Başlayın

[.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0)'ü yükleyin ve .NET MAUI iş yükünü güncelleyin.
