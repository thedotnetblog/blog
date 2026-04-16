---
title: "Pin 聚类终于登陆 .NET MAUI Maps — 一个属性，零痛苦"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 为 Map 控件添加了原生 Pin 聚类功能。一个属性、独立的聚类分组和点击处理 — 全部内置。"
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *本文为自动翻译。查看原文请[点击这里]({{< ref "maui-maps-pin-clustering-finally.md" >}})。*

你知道那种感觉吗？在地图上加载一百个 Pin，然后整个地图变成一团看不清的东西？对，这就是 .NET MAUI Maps 一直以来的体验。现在不会了。

David Ortinau [刚刚宣布](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/) .NET MAUI 11 Preview 3 在 Android 和 iOS/Mac Catalyst 上内置了 Pin 聚类功能。而且最棒的是 — 启用它简单得不可思议。

## 一个属性统治一切

```xml
<maps:Map IsClusteringEnabled="True" />
```

就这样。相邻的 Pin 会被分组到带有计数徽章的聚类中。放大时展开，缩小时折叠。这是用户对任何现代地图都期望的行为 — 现在你只需一个属性就能获得。

## 独立的聚类分组

这才是有趣的地方。不是所有 Pin 都应该聚在一起。咖啡店和公园是不同的东西，你的地图应该知道这一点。

`ClusteringIdentifier` 属性让你可以将 Pin 分成独立的组：

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

具有相同标识符的 Pin 会聚在一起。不同的标识符即使在地理位置很近的情况下也会形成独立的聚类。没有标识符？默认分组。干净且可预测。

## 处理聚类点击

当用户点击一个聚类时，你会收到一个 `ClusterClicked` 事件，包含你需要的一切：

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

事件参数提供 `Pins`（聚类中的 Pin）、`Location`（地理中心）和 `Handled`（如果你想覆盖默认缩放行为，设置为 `true`）。简单、实用，完全符合预期。

## 值得了解的平台细节

在 Android 上，聚类使用自定义的基于网格的算法，在缩放变化时重新计算 — 没有外部依赖。在 iOS 和 Mac Catalyst 上，它利用了 MapKit 原生的 `MKClusterAnnotation` 支持，这意味着流畅的平台原生动画。

这是 MAUI 团队做出正确决策的案例之一 — 在有意义的地方依靠平台能力。

## 为什么这很重要

Pin 聚类一直是 .NET MAUI 中最受期待的功能之一（[issue #11811](https://github.com/dotnet/maui/issues/11811)），这是有充分理由的。每个在地图上显示位置的应用 — 配送追踪、门店定位、房地产 — 都需要它。以前你必须自己构建或引入第三方库。现在它是内置的。

对于我们构建跨平台移动应用的 .NET 开发者来说，这正是那种让 MAUI 成为地图密集型场景中真正实用选择的生活质量改善。

## 开始使用

安装 [.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) 并更新 .NET MAUI 工作负载。[Maps 示例](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps)包含一个新的聚类页面，你可以立即上手体验。

去用它构建点什么吧 — 让你的地图终于能喘口气。
