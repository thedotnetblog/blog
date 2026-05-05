---
title: "Clustering de Pins Finalmente Chega ao .NET MAUI Maps — Uma Propriedade, Zero Dor de Cabeça"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 adiciona clustering nativo de pins ao controle Map. Uma propriedade, grupos de clustering separados e tratamento de taps — tudo integrado."
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *Este post foi traduzido automaticamente. Para a versão original, [clique aqui]({{< ref "maui-maps-pin-clustering-finally.md" >}}).*

Sabe aquele momento quando você carrega um mapa com uma centena de pins e tudo vira uma mancha ilegível? É, essa tem sido a experiência com .NET MAUI Maps até agora. Acabou.

David Ortinau [acabou de anunciar](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) que o .NET MAUI 11 Preview 3 traz clustering de pins embutido no Android e iOS/Mac Catalyst. E a melhor parte — é ridiculamente simples de ativar.

## Uma propriedade para governar todos

```xml
<maps:Map IsClusteringEnabled="True" />
```

É isso. Pins próximos são agrupados em clusters com um badge de contagem. Dá zoom e eles expandem. Afasta e eles colapsam. O tipo de comportamento que os usuários esperam de qualquer mapa moderno — e agora você consegue com uma única propriedade.

## Grupos de clustering independentes

Aqui é onde fica interessante. Nem todos os pins devem se agrupar juntos. Cafeterias e parques são coisas diferentes, e seu mapa deveria saber disso.

A propriedade `ClusteringIdentifier` permite separar pins em grupos independentes:

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

Pins com o mesmo identificador se agrupam juntos. Identificadores diferentes formam clusters independentes mesmo quando estão geograficamente próximos. Sem identificador? Grupo padrão. Limpo e previsível.

## Tratamento de taps em clusters

Quando um usuário toca em um cluster, você recebe um evento `ClusterClicked` com tudo que precisa:

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

Os argumentos do evento te dão `Pins` (os pins no cluster), `Location` (o centro geográfico) e `Handled` (defina como `true` se quiser sobrescrever o zoom padrão). Simples, prático, exatamente o que você esperaria.

## Detalhes de plataforma que vale a pena conhecer

No Android, o clustering usa um algoritmo personalizado baseado em grid que recalcula nas mudanças de zoom — sem dependências externas. No iOS e Mac Catalyst, ele aproveita o suporte nativo do `MKClusterAnnotation` do MapKit, o que significa animações suaves e nativas da plataforma.

Esse é um daqueles casos em que o time do MAUI tomou a decisão certa — apoiar-se na plataforma onde faz sentido.

## Por que isso importa

Clustering de pins tem sido uma das funcionalidades mais solicitadas no .NET MAUI ([issue #11811](https://github.com/dotnet/maui/issues/11811)), e com razão. Toda app que mostra localizações em um mapa — rastreamento de entregas, localizadores de lojas, imobiliárias — precisa disso. Antes você tinha que construir por conta própria ou usar uma biblioteca de terceiros. Agora vem integrado.

Para nós desenvolvedores .NET construindo apps móveis multiplataforma, esse é o tipo de melhoria de qualidade de vida que faz do MAUI uma escolha genuinamente prática para cenários com uso intensivo de mapas.

## Comece agora

Instale o [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) e atualize o workload do .NET MAUI. O [exemplo de Maps](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) inclui uma nova página de Clustering com a qual você pode brincar imediatamente.

Vá construir algo com isso — e deixe seus mapas finalmente respirarem.
