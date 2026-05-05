---
title: "Il Pin Clustering Arriva Finalmente in .NET MAUI Maps — Una Proprietà, Zero Problemi"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 aggiunge il clustering nativo dei pin al controllo Map. Una proprietà, gruppi di clustering separati e gestione dei tap — tutto integrato."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Questo articolo è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "maui-maps-pin-clustering-finally.md" >}}).*

Conosci quel momento in cui carichi una mappa con un centinaio di pin e tutto diventa una macchia illeggibile? Sì, questa è stata l'esperienza con .NET MAUI Maps fino ad ora. Non più.

David Ortinau [ha appena annunciato](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) che .NET MAUI 11 Preview 3 include il pin clustering out of the box su Android e iOS/Mac Catalyst. E la parte migliore — è ridicolmente semplice da attivare.

## Una proprietà per dominarli tutti

```xml
<maps:Map IsClusteringEnabled="True" />
```

Tutto qui. I pin vicini vengono raggruppati in cluster con un badge di conteggio. Zoom in e si espandono. Zoom out e si raggruppano. Il tipo di comportamento che gli utenti si aspettano da qualsiasi mappa moderna — e ora lo ottieni con una singola proprietà.

## Gruppi di clustering indipendenti

Ecco dove diventa interessante. Non tutti i pin dovrebbero raggrupparsi insieme. Le caffetterie e i parchi sono cose diverse, e la tua mappa dovrebbe saperlo.

La proprietà `ClusteringIdentifier` ti permette di separare i pin in gruppi indipendenti:

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

I pin con lo stesso identificatore si raggruppano insieme. Identificatori diversi formano cluster indipendenti anche quando sono geograficamente vicini. Nessun identificatore? Gruppo predefinito. Pulito e prevedibile.

## Gestione dei tap sui cluster

Quando un utente tocca un cluster, ricevi un evento `ClusterClicked` con tutto ciò di cui hai bisogno:

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

Gli argomenti dell'evento ti danno `Pins` (i pin nel cluster), `Location` (il centro geografico) e `Handled` (impostalo su `true` se vuoi sovrascrivere lo zoom predefinito). Semplice, pratico, esattamente quello che ti aspetteresti.

## Dettagli di piattaforma da conoscere

Su Android, il clustering usa un algoritmo personalizzato basato su griglia che ricalcola ai cambi di zoom — nessuna dipendenza esterna. Su iOS e Mac Catalyst, sfrutta il supporto nativo di `MKClusterAnnotation` di MapKit, il che significa animazioni fluide e native della piattaforma.

Questo è uno di quei casi in cui il team MAUI ha fatto la scelta giusta — appoggiarsi alla piattaforma dove ha senso.

## Perché è importante

Il pin clustering è stata una delle funzionalità più richieste in .NET MAUI ([issue #11811](https://github.com/dotnet/maui/issues/11811)), e a buon ragione. Ogni app che mostra posizioni su una mappa — tracciamento consegne, localizzatori di negozi, immobiliare — ne ha bisogno. Prima dovevi costruirlo da solo o integrare una libreria di terze parti. Ora è integrato.

Per noi sviluppatori .NET che costruiamo app mobile multipiattaforma, questo è il tipo di miglioramento della qualità della vita che rende MAUI una scelta genuinamente pratica per scenari con uso intensivo di mappe.

## Per iniziare

Installa [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) e aggiorna il workload .NET MAUI. L'[esempio Maps](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) include una nuova pagina Clustering con cui puoi giocare subito.

Vai a costruire qualcosa — e lascia che le tue mappe finalmente respirino.
