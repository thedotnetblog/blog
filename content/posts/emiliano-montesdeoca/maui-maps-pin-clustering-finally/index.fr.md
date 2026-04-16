---
title: "Le clustering de pins arrive enfin dans .NET MAUI Maps — Une propriété, zéro prise de tête"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 ajoute le clustering natif de pins au contrôle Map. Une propriété, des groupes de clustering séparés et la gestion des taps — tout est intégré."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "maui-maps-pin-clustering-finally.md" >}}).*

Tu connais ce moment où tu charges une carte avec une centaine de pins et tout se transforme en une tache illisible ? Ouais, c'était ça l'expérience .NET MAUI Maps jusqu'à maintenant. C'est terminé.

David Ortinau [vient d'annoncer](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) que .NET MAUI 11 Preview 3 embarque le clustering de pins nativement sur Android et iOS/Mac Catalyst. Et le meilleur — c'est ridiculement simple à activer.

## Une propriété pour les gouverner tous

```xml
<maps:Map IsClusteringEnabled="True" />
```

C'est tout. Les pins proches sont regroupés en clusters avec un badge de comptage. Zoom avant, ils s'expandent. Zoom arrière, ils se regroupent. Le genre de comportement que les utilisateurs attendent de n'importe quelle carte moderne — et maintenant tu l'obtiens avec une seule propriété.

## Groupes de clustering indépendants

C'est là que ça devient intéressant. Tous les pins ne devraient pas se regrouper ensemble. Les cafés et les parcs sont des choses différentes, et ta carte devrait le savoir.

La propriété `ClusteringIdentifier` te permet de séparer les pins en groupes indépendants :

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

Les pins avec le même identifiant se regroupent ensemble. Des identifiants différents forment des clusters indépendants même quand ils sont géographiquement proches. Pas d'identifiant ? Groupe par défaut. Propre et prévisible.

## Gestion des taps sur les clusters

Quand un utilisateur tape sur un cluster, tu reçois un événement `ClusterClicked` avec tout ce dont tu as besoin :

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

Les arguments de l'événement te donnent `Pins` (les pins du cluster), `Location` (le centre géographique) et `Handled` (à mettre sur `true` si tu veux surcharger le zoom par défaut). Simple, pratique, exactement ce qu'on attend.

## Détails de plateforme à connaître

Sur Android, le clustering utilise un algorithme personnalisé basé sur une grille qui recalcule lors des changements de zoom — aucune dépendance externe. Sur iOS et Mac Catalyst, il exploite le support natif de `MKClusterAnnotation` de MapKit, ce qui signifie des animations fluides et natives de la plateforme.

C'est un de ces cas où l'équipe MAUI a fait le bon choix — s'appuyer sur la plateforme là où ça a du sens.

## Pourquoi c'est important

Le clustering de pins a été l'une des fonctionnalités les plus demandées dans .NET MAUI ([issue #11811](https://github.com/dotnet/maui/issues/11811)), et pour une bonne raison. Chaque app qui affiche des emplacements sur une carte — suivi de livraisons, localisateurs de magasins, immobilier — en a besoin. Avant, il fallait le construire soi-même ou intégrer une bibliothèque tierce. Maintenant c'est intégré.

Pour nous développeurs .NET qui construisons des apps mobiles multiplateformes, c'est exactement le type d'amélioration de qualité de vie qui fait de MAUI un choix véritablement pratique pour les scénarios lourds en cartes.

## Pour commencer

Installe [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) et mets à jour le workload .NET MAUI. L'[exemple Maps](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) inclut une nouvelle page Clustering avec laquelle tu peux jouer tout de suite.

Va construire quelque chose avec — et laisse tes cartes enfin respirer.
