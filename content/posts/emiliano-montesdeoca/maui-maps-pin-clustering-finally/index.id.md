---
title: "Pin Clustering Akhirnya Hadir di .NET MAUI Maps — Satu Properti, Nol Rasa Sakit"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 menambahkan pengelompokan pin native ke kontrol Map. Satu properti, grup clustering terpisah, dan penanganan ketukan — semuanya bawaan."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Postingan ini diterjemahkan secara otomatis. Untuk versi aslinya, [klik di sini]({{< ref "maui-maps-pin-clustering-finally" >}}).*

Anda tahu momen ketika memuat peta dengan seratus pin dan semuanya menjadi gumpalan yang tidak terbaca? Itulah pengalaman .NET MAUI Maps — sampai sekarang.

David Ortinau [baru saja mengumumkan](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) bahwa .NET MAUI 11 Preview 3 hadir dengan pin clustering bawaan di Android dan iOS/Mac Catalyst.

## Satu properti untuk menguasai semuanya

```xml
<maps:Map IsClusteringEnabled="True" />
```

Itu saja. Pin yang berdekatan dikelompokkan ke dalam cluster dengan lencana hitungan.

## Grup clustering independen

Properti `ClusteringIdentifier` memungkinkan Anda memisahkan pin ke dalam grup independen:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});
```

## Menangani ketukan cluster

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("
", e.Pins.Select(p => p.Label));
    await DisplayAlert($"Cluster ({e.Pins.Count} pins)", names, "OK");
};
```

## Mulai

Instal [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) dan perbarui workload .NET MAUI.
