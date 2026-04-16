---
title: "Pin Clustering Finally Lands in .NET MAUI Maps — One Property, Zero Pain"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 adds native pin clustering to the Map control. One property, separate clustering groups, and tap handling — all built in."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

You know that moment when you load a map with a hundred pins and the whole thing turns into an unreadable blob? Yeah, that's been the .NET MAUI Maps experience until now. No more.

David Ortinau [just announced](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) that .NET MAUI 11 Preview 3 ships pin clustering out of the box on Android and iOS/Mac Catalyst. And the best part — it's ridiculously simple to enable.

## One property to rule them all

```xml
<maps:Map IsClusteringEnabled="True" />
```

That's it. Nearby pins get grouped into clusters with a count badge. Zoom in and they expand. Zoom out and they collapse. The kind of behavior users expect from any modern map — and now you get it with a single property.

## Independent clustering groups

Here's where it gets interesting. Not all pins should cluster together. Coffee shops and parks are different things, and your map should know that.

The `ClusteringIdentifier` property lets you separate pins into independent groups:

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

Pins with the same identifier cluster together. Different identifiers form independent clusters even when they're geographically close. No identifier? Default group. Clean and predictable.

## Handling cluster taps

When a user taps a cluster, you get a `ClusterClicked` event with everything you need:

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

The event args give you `Pins` (the pins in the cluster), `Location` (the geographic center), and `Handled` (set to `true` if you want to override the default zoom). Simple, practical, exactly what you'd expect.

## Platform details worth knowing

On Android, clustering uses a custom grid-based algorithm that recalculates on zoom changes — no external dependencies. On iOS and Mac Catalyst, it leverages native `MKClusterAnnotation` support from MapKit, which means smooth, platform-native animations.

This is one of those cases where the MAUI team made the right call — lean on the platform where it makes sense.

## Why this matters

Pin clustering has been one of the most requested features in .NET MAUI ([issue #11811](https://github.com/dotnet/maui/issues/11811)), and for good reason. Every app that shows locations on a map — delivery tracking, store locators, real estate — needs this. Previously you had to build it yourself or pull in a third-party library. Now it's built in.

For us .NET developers building cross-platform mobile apps, this is the kind of quality-of-life improvement that makes MAUI a genuinely practical choice for map-heavy scenarios.

## Get started

Install [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) and update the .NET MAUI workload. The [Maps sample](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) includes a new Clustering page you can play with right away.

Go build something with it — and let your maps finally breathe.
