---
title: ".NET MAUI Maps'e Nihayet Pin Kümeleme Geldi — Tek Özellik, Sıfır Acı"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3, Map kontrolüne yerel pin kümeleme ekliyor. Tek bir özellik, ayrı kümeleme grupları ve tap yönetimi — hepsi yerleşik."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Bu yazı otomatik olarak çevrilmiştir. Orijinal için [buraya tıklayın]({{< ref "maui-maps-pin-clustering-finally" >}}).*

Yüz pin'li bir harita yüklediğinizde ve her şeyin okunaksız bir kümreye dönüştüğü o anı bilirsiniz, değil mi? Evet, .NET MAUI Maps deneyimi şimdiye kadar tam olarak buydu. Artık değil.

David Ortinau, .NET MAUI 11 Preview 3'ün Android ve iOS/Mac Catalyst üzerinde kutudan çıkar çıkmaz pin kümeleme sunduğunu [duyurdu](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/). Ve en iyi kısım — etkinleştirmek gülünç derecede basit.

## Hepsini Yöneten Tek Özellik

```xml
<maps:Map IsClusteringEnabled="True" />
```

Hepsi bu kadar. Yakın pinler, sayı rozeti olan kümeler halinde gruplanır. Yakınlaştırın ve genişlerler. Uzaklaştırın ve daralırlar. Kullanıcıların modern bir haritadan beklediği türden davranış — ve artık tek bir özellikle elde ediyorsunuz.

## Bağımsız Kümeleme Grupları

İşte ilginçleştiği yer burası. Tüm pinler birlikte kümelenmemelidir. Kahve dükkanları ve parklar farklı şeylerdir ve haritanız bunu bilmelidir.

`ClusteringIdentifier` özelliği, pinleri bağımsız gruplara ayırmanızı sağlar:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});

map.Pins.Add(new Pin
{
    Label = "Occidental Square",
    Location = new Location(47.6064, -122.3325),
    ClusteringIdentifier = "parks"
});
```

Aynı tanımlayıcıya sahip pinler birlikte kümelenir. Farklı tanımlayıcılar, coğrafi olarak yakın olsalar bile bağımsız kümeler oluşturur. Tanımlayıcı yok mu? Varsayılan grup. Temiz ve öngörülebilir.

## Küme Tap'larını Yönetme

Bir kullanıcı kümeye dokunduğunda, ihtiyacınız olan her şeyle birlikte bir `ClusterClicked` olayı alırsınız:

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("\n", e.Pins.Select(p => p.Label));
    await DisplayAlert(
        $"Cluster ({e.Pins.Count} pins)",
        names,
        "OK");

    // Varsayılan kümeye-yakınlaştırma davranışını bastır:
    // e.Handled = true;
};
```

Olay argümanları size `Pins` (kümedeki pinler), `Location` (coğrafi merkez) ve `Handled` (varsayılanı geçersiz kılmak istiyorsanız `true` olarak ayarlayın) sunar. Basit, pratik, tam olarak beklediğiniz şey.

## Bilmeye Değer Platform Ayrıntıları

Android'de kümeleme, zoom değişikliklerinde yeniden hesaplanan özel ızgara tabanlı bir algoritma kullanır — harici bağımlılık yok. iOS ve Mac Catalyst'te, sorunsuz, platform-native animasyonlar anlamına gelen MapKit'ten yerel `MKClusterAnnotation` desteğinden yararlanır.

Bu, MAUI ekibinin doğru kararı verdiği durumlardan biri — mantıklı olduğunda platforma güvenmek.

## Neden Önemli?

Pin kümeleme, .NET MAUI'de en çok talep edilen özelliklerden biri olmuştur ([issue #11811](https://github.com/dotnet/maui/issues/11811)), ve bunun iyi bir nedeni var. Haritada konumları gösteren her uygulama — teslimat takibi, mağaza bulucu, gayrimenkul — buna ihtiyaç duyar. Daha önce bunu kendiniz oluşturmanız veya üçüncü taraf bir kütüphane getirmeniz gerekiyordu. Artık yerleşik.

Cross-platform mobil uygulamalar geliştiren .NET geliştiricileri için bu, MAUI'yi harita yoğun senaryolar için gerçekten pratik bir tercih haline getiren türden bir yaşam kalitesi iyileştirmesi.

## Başlarken

[.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0)'ü kurun ve .NET MAUI iş yükünü güncelleyin. [Maps örneği](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps), hemen oynayabileceğiniz yeni bir Clustering sayfası içeriyor.

Gidin ve onunla bir şeyler oluşturun — haritalarınızın nihayet nefes almasına izin verin.
