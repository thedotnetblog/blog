---
title: "Grupowanie Pinezek W Końcu Trafia do .NET MAUI Maps — Jedna Właściwość, Zero Bólu"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 dodaje natywne grupowanie pinezek do kontrolki Map. Jedna właściwość, oddzielne grupy klastrów i obsługa dotknięcia — wszystko wbudowane."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "maui-maps-pin-clustering-finally" >}}).*

Znasz ten moment, gdy ładujesz mapę ze stu pinezkami i całość zamienia się w nieczytelną masę? To było doświadczenie .NET MAUI Maps — do teraz.

David Ortinau [właśnie ogłosił](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/), że .NET MAUI 11 Preview 3 dostarcza grupowanie pinezek po wyjęciu z pudełka.

## Jedna właściwość do rządzenia wszystkimi

```xml
<maps:Map IsClusteringEnabled="True" />
```

Tyle. Pobliskie pinezki są grupowane w klastry z odznaką liczby.

## Niezależne grupy klastrów

Właściwość `ClusteringIdentifier` pozwala oddzielić pinezki na niezależne grupy:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});
```

## Obsługa dotknięcia klastra

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("
", e.Pins.Select(p => p.Label));
    await DisplayAlert($"Cluster ({e.Pins.Count} pins)", names, "OK");
};
```

## Zacznij

Zainstaluj [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) i zaktualizuj obciążenie .NET MAUI. [Przykład Maps](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) zawiera nową stronę Clustering.
