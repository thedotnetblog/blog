---
title: "El clustering de pines por fin llega a .NET MAUI Maps — Una propiedad, cero complicaciones"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 añade clustering nativo de pines al control Map. Una propiedad, grupos de clustering independientes y manejo de taps — todo integrado."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Esta publicación fue traducida automáticamente. Para la versión original, [haz clic aquí]({{< ref "maui-maps-pin-clustering-finally.md" >}}).*

¿Conoces ese momento en el que cargas un mapa con cien pines y todo se convierte en una mancha ilegible? Sí, esa ha sido la experiencia con .NET MAUI Maps hasta ahora. Se acabó.

David Ortinau [acaba de anunciar](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) que .NET MAUI 11 Preview 3 trae clustering de pines de serie en Android e iOS/Mac Catalyst. Y lo mejor — es ridículamente fácil de activar.

## Una propiedad para gobernarlos a todos

```xml
<maps:Map IsClusteringEnabled="True" />
```

Eso es todo. Los pines cercanos se agrupan en clusters con un badge de cantidad. Haces zoom y se expanden. Alejas y se colapsan. El tipo de comportamiento que los usuarios esperan de cualquier mapa moderno — y ahora lo consigues con una sola propiedad.

## Grupos de clustering independientes

Aquí es donde se pone interesante. No todos los pines deberían agruparse juntos. Las cafeterías y los parques son cosas distintas, y tu mapa debería saberlo.

La propiedad `ClusteringIdentifier` te permite separar pines en grupos independientes:

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

Los pines con el mismo identificador se agrupan juntos. Identificadores diferentes forman clusters independientes incluso cuando están geográficamente cerca. ¿Sin identificador? Grupo por defecto. Limpio y predecible.

## Manejo de taps en clusters

Cuando un usuario toca un cluster, recibes un evento `ClusterClicked` con todo lo que necesitas:

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

Los argumentos del evento te dan `Pins` (los pines del cluster), `Location` (el centro geográfico) y `Handled` (ponlo a `true` si quieres anular el zoom por defecto). Simple, práctico, exactamente lo que esperarías.

## Detalles de plataforma que vale la pena conocer

En Android, el clustering usa un algoritmo personalizado basado en rejilla que recalcula con los cambios de zoom — sin dependencias externas. En iOS y Mac Catalyst, aprovecha el soporte nativo de `MKClusterAnnotation` de MapKit, lo que significa animaciones suaves y nativas de la plataforma.

Este es uno de esos casos en los que el equipo de MAUI tomó la decisión correcta — apoyarse en la plataforma donde tiene sentido.

## Por qué esto importa

El clustering de pines ha sido una de las características más solicitadas en .NET MAUI ([issue #11811](https://github.com/dotnet/maui/issues/11811)), y con razón. Todas las apps que muestran ubicaciones en un mapa — seguimiento de envíos, localizadores de tiendas, bienes raíces — lo necesitan. Antes tenías que construirlo tú mismo o recurrir a una librería de terceros. Ahora viene integrado.

Para nosotros los desarrolladores .NET que construimos apps móviles multiplataforma, este es el tipo de mejora de calidad de vida que hace de MAUI una opción genuinamente práctica para escenarios con uso intensivo de mapas.

## Empieza ya

Instala [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) y actualiza el workload de .NET MAUI. El [ejemplo de Maps](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) incluye una nueva página de Clustering con la que puedes jugar de inmediato.

Ve y construye algo con ello — y deja que tus mapas por fin respiren.
