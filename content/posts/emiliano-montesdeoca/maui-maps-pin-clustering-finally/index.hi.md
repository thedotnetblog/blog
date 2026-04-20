---
title: ".NET MAUI Maps में Pin Clustering आखिरकार आया — एक Property, Zero परेशानी"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 Map control में native pin clustering जोड़ता है। एक property, अलग clustering groups, और tap handling — सब built in।"
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "maui-maps-pin-clustering-finally" >}}).*

आप उस moment को जानते हैं जब आप सौ pins वाला map load करते हैं और पूरी चीज़ एक unreadable blob बन जाती है? हाँ, यही तब तक .NET MAUI Maps का experience था। अब नहीं।

David Ortinau ने [अभी announce किया](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) कि .NET MAUI 11 Preview 3 Android और iOS/Mac Catalyst पर out of the box pin clustering ship करता है। और सबसे अच्छी बात — इसे enable करना बेहद simple है।

## एक property सबको control करे

```xml
<maps:Map IsClusteringEnabled="True" />
```

बस इतना। Nearby pins count badge के साथ clusters में group हो जाते हैं। Zoom in करें और वे expand होते हैं। Zoom out करें और वे collapse होते हैं। वह behavior जो users किसी भी modern map से expect करते हैं — और अब आपको यह एक single property से मिलता है।

## स्वतंत्र clustering groups

यहाँ यह interesting हो जाता है। सभी pins को एक साथ cluster नहीं होना चाहिए। Coffee shops और parks अलग-अलग चीज़ें हैं, और आपके map को यह पता होना चाहिए।

`ClusteringIdentifier` property आपको pins को independent groups में अलग करने देती है:

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

Same identifier वाले pins एक साथ cluster होते हैं। अलग-अलग identifiers independent clusters बनाते हैं भले ही वे geographically करीब हों। कोई identifier नहीं? Default group। साफ़ और predictable।

## Cluster taps handle करना

जब कोई user cluster tap करता है, तो आपको `ClusterClicked` event मिलती है जिसमें आपको जो चाहिए वह सब होता है:

```csharp
map.ClusterClicked += async (sender, e) =>
{
    string names = string.Join("\n", e.Pins.Select(p => p.Label));
    await DisplayAlert(
        $"Cluster ({e.Pins.Count} pins)",
        names,
        "OK");

    // Default zoom-to-cluster behavior suppress करने के लिए:
    // e.Handled = true;
};
```

Event args आपको `Pins` (cluster में pins), `Location` (geographic center), और `Handled` (default zoom override करने के लिए `true` set करें) देते हैं। Simple, practical, exactly वही जो आप expect करते।

## Platform से जुड़ी ज़रूरी बातें

Android पर, clustering एक custom grid-based algorithm का उपयोग करती है जो zoom changes पर recalculate होती है — कोई external dependencies नहीं। iOS और Mac Catalyst पर, यह MapKit का native `MKClusterAnnotation` support leverage करता है, जिसका मतलब है smooth, platform-native animations।

यह उन cases में से एक है जहाँ MAUI team ने सही call किया — जहाँ समझ में आए वहाँ platform पर lean करो।

## यह क्यों मायने रखता है

.NET MAUI में Pin clustering सबसे ज़्यादा requested features में से एक रही है ([issue #11811](https://github.com/dotnet/maui/issues/11811)), और इसकी वजह है। हर app जो map पर locations दिखाती है — delivery tracking, store locators, real estate — इसकी ज़रूरत होती है। पहले आपको इसे खुद बनाना पड़ता था या किसी third-party library को लाना पड़ता था। अब यह built in है।

हम .NET developers के लिए जो cross-platform mobile apps बना रहे हैं, यह उस तरह का quality-of-life improvement है जो MAUI को map-heavy scenarios के लिए genuinely practical choice बनाता है।

## शुरुआत करें

[.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) install करें और .NET MAUI workload update करें। [Maps sample](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps) में एक नया Clustering page है जिसे आप तुरंत try कर सकते हैं।

जाएं, इसके साथ कुछ बनाएं — और अपने maps को finally सांस लेने दें।
