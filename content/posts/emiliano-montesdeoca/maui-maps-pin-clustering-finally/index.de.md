---
title: "Pin-Clustering landet endlich in .NET MAUI Maps — Eine Property, null Aufwand"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 bringt natives Pin-Clustering für das Map-Control. Eine Property, separate Clustering-Gruppen und Tap-Handling — alles eingebaut."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion findest du [hier]({{< ref "maui-maps-pin-clustering-finally.md" >}}).*

Kennst du den Moment, wenn du eine Karte mit hundert Pins lädst und das Ganze zu einem unlesbaren Klumpen wird? Ja, so war die .NET MAUI Maps-Erfahrung bisher. Damit ist jetzt Schluss.

David Ortinau [hat gerade angekündigt](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/), dass .NET MAUI 11 Preview 3 Pin-Clustering auf Android und iOS/Mac Catalyst out of the box mitliefert. Und das Beste — es ist lächerlich einfach zu aktivieren.

## Eine Property, sie alle zu beherrschen

```xml
<maps:Map IsClusteringEnabled="True" />
```

Das war's. Benachbarte Pins werden in Clustern mit einem Zähler-Badge gruppiert. Reinzoomen — sie expandieren. Rauszoomen — sie kollabieren. Genau das Verhalten, das Nutzer von jeder modernen Karte erwarten — und jetzt bekommst du es mit einer einzigen Property.

## Unabhängige Clustering-Gruppen

Hier wird es interessant. Nicht alle Pins sollten zusammen geclustert werden. Cafés und Parks sind verschiedene Dinge, und deine Karte sollte das wissen.

Die `ClusteringIdentifier`-Property ermöglicht es dir, Pins in unabhängige Gruppen zu trennen:

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

Pins mit demselben Identifier clustern zusammen. Verschiedene Identifier bilden unabhängige Cluster, selbst wenn sie geografisch nah beieinander liegen. Kein Identifier? Standardgruppe. Sauber und vorhersehbar.

## Cluster-Taps verarbeiten

Wenn ein Nutzer auf einen Cluster tippt, bekommst du ein `ClusterClicked`-Event mit allem, was du brauchst:

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("\n", e.Pins.Select(p => p.Label));
    await DisplayAlert(
        $"Cluster ({e.Pins.Count} pins)",
        names,
        "OK");

    // Suppress default zoom-to-cluster behavior:
    // e.Handled = true;
};
```

Die Event-Args liefern dir `Pins` (die Pins im Cluster), `Location` (das geografische Zentrum) und `Handled` (auf `true` setzen, wenn du den Standard-Zoom überschreiben willst). Einfach, praktisch, genau was man erwartet.

## Plattform-Details, die man kennen sollte

Auf Android verwendet das Clustering einen eigenen Grid-basierten Algorithmus, der bei Zoom-Änderungen neu berechnet — keine externen Abhängigkeiten. Auf iOS und Mac Catalyst wird die native `MKClusterAnnotation`-Unterstützung von MapKit genutzt, was flüssige, plattformnative Animationen bedeutet.

Das ist einer dieser Fälle, in denen das MAUI-Team die richtige Entscheidung getroffen hat — auf die Plattform setzen, wo es Sinn ergibt.

## Warum das wichtig ist

Pin-Clustering war eines der meistgewünschten Features in .NET MAUI ([Issue #11811](https://github.com/dotnet/maui/issues/11811)), und das aus gutem Grund. Jede App, die Standorte auf einer Karte zeigt — Lieferverfolgung, Filialfinder, Immobilien — braucht das. Vorher musstest du es selbst bauen oder eine Drittanbieter-Bibliothek einbinden. Jetzt ist es eingebaut.

Für uns .NET-Entwickler, die plattformübergreifende mobile Apps bauen, ist das genau die Art von Quality-of-Life-Verbesserung, die MAUI zu einer wirklich praktischen Wahl für kartenintensive Szenarien macht.

## Loslegen

Installiere [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) und aktualisiere den .NET MAUI Workload. Das [Maps-Sample](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) enthält eine neue Clustering-Seite, mit der du sofort loslegen kannst.

Bau etwas damit — und lass deine Karten endlich atmen.
