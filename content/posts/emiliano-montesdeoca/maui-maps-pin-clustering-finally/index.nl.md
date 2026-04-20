---
title: "Pin-clustering Landt Eindelijk in .NET MAUI Maps — Één Eigenschap, Nul Pijn"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 voegt native pin-clustering toe aan het Map-besturingselement. Één eigenschap, aparte clustergroepen en tikverwerking — allemaal ingebouwd."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "maui-maps-pin-clustering-finally" >}}).*

Ken je dat moment wanneer je een kaart laadt met honderd pins en alles een onleesbare klodder wordt? Dat was de .NET MAUI Maps-ervaring — tot nu.

David Ortinau [heeft zojuist aangekondigd](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) dat .NET MAUI 11 Preview 3 pin-clustering out-of-the-box levert op Android en iOS/Mac Catalyst.

## Één eigenschap om ze allemaal te regeren

```xml
<maps:Map IsClusteringEnabled="True" />
```

Dat is alles. Nabijgelegen pins worden gegroepeerd in clusters met een telling-badge.

## Onafhankelijke clustergroepen

De `ClusteringIdentifier`-eigenschap laat je pins scheiden in onafhankelijke groepen:

```csharp
map.Pins.Add(new Pin
{
    Label = "Pike Place Coffee",
    Location = new Location(47.6097, -122.3331),
    ClusteringIdentifier = "coffee"
});
```

## Clustertikken afhandelen

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("
", e.Pins.Select(p => p.Label));
    await DisplayAlert($"Cluster ({e.Pins.Count} pins)", names, "OK");
};
```

## Aan de slag

Installeer [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) en update de .NET MAUI-workload.
