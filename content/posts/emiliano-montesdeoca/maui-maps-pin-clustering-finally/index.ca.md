---
title: "El clúster de pins finalment arriba als mapes.NET MAUI: una propietat, zero dolor"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 afegeix un clúster de pins natius al control de mapa. Una propietat, grups d'agrupament separats i gestió de tocs, tot integrat."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

Coneixes aquell moment en què carregues un mapa amb cent agulles i tot es converteix en una taca il·legible? Sí, aquesta ha estat l'experiència de.NET MAUI Maps fins ara. No més.

David Ortinau [acaba d'anunciar](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) que.NET MAUI 11 Preview 3 inclou pins agrupats fora de la caixa a Android i iOS/Mac Catalyst. I la millor part: activar-lo és ridículament senzill.

## Una propietat per governar-les totes

```xml
<maps:Map IsClusteringEnabled="True" />
```

Això és tot. Els pins propers s'agrupen en grups amb una insígnia de recompte. Apropa i s'amplien. Allunya el zoom i es col·lapsen. El tipus de comportament que els usuaris esperen de qualsevol mapa modern, i ara ho obteniu amb una única propietat.

## Grups de agrupació independents

Aquí és on es posa interessant. No tots els pins s'han d'agrupar. Les cafeteries i els parcs són coses diferents, i el vostre mapa ho hauria de saber.

La propietat `ClusteringIdentifier` us permet separar els pins en grups independents:

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

Pins amb el mateix grup d'identificadors junts. Els diferents identificadors formen clústers independents fins i tot quan estan geogràficament propers. Sense identificador? Grup per defecte. Net i previsible.

## Gestió de les aixetes de clúster

Quan un usuari toca un clúster, obteniu un esdeveniment `ClusterClicked` amb tot el que necessiteu:

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

Els arguments de l'esdeveniment us proporcionen `Pins` (els pins del clúster), `Location` (el centre geogràfic) i `Handled` (establert a `true` si voleu anul·lar el zoom predeterminat). Senzill, pràctic, exactament el que esperaries.

## Val la pena conèixer els detalls de la plataforma

A Android, la agrupació en clúster utilitza un algorisme personalitzat basat en quadrícula que recalcula els canvis de zoom, sense dependències externes. A iOS i Mac Catalyst, aprofita el suport natiu `MKClusterAnnotation` de MapKit, que significa animacions fluides i natives de la plataforma.

Aquest és un d'aquests casos en què l'equip de MAUI va fer la trucada correcta: recolzeu-vos a la plataforma on tingui sentit.

## Per què això és important

La agrupació de pins ha estat una de les funcions més sol·licitades a.NET MAUI ([issue #11811](https://github.com/dotnet/maui/issues/11811)), i per una bona raó. Tota aplicació que mostra ubicacions en un mapa (seguiment de lliurament, localitzadors de botigues, béns immobles) ho necessita. Anteriorment, havíeu de crear-lo vosaltres mateixos o treure una biblioteca de tercers. Ara està incorporat.

Per als desenvolupadors de.NET que creem aplicacions mòbils multiplataforma, aquest és el tipus de millora de la qualitat de vida que fa que MAUI sigui una opció realment pràctica per a escenaris amb mapes pesats.

## Comença

Instal·leu [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) i actualitzeu la càrrega de treball.NET MAUI. La [mostra de mapes](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) inclou una nova pàgina de clúster amb la qual podeu jugar immediatament.

Aneu a construir alguna cosa amb ell i deixeu que els vostres mapes finalment respiren.
