---
title: "ピンクラスタリングがついに .NET MAUI Maps に登場 — プロパティ1つ、手間ゼロ"
date: 2026-04-16
author: "Emiliano Montesdeoca"
description: ".NET MAUI 11 Preview 3 で Map コントロールにネイティブなピンクラスタリングが追加されました。プロパティ1つ、独立したクラスタリンググループ、タップ処理 — すべて組み込み。"
tags:
  - dotnet
  - maui
  - mobile
  - maps
  - dotnet-11
---

> *この記事は自動翻訳されています。原文は[こちら]({{< ref "maui-maps-pin-clustering-finally.md" >}})をご覧ください。*

マップに100個のピンを読み込んだら、全体が読めない塊になった — そんな経験ありませんか？そう、これまでの .NET MAUI Maps はまさにそんな感じでした。もう終わりです。

David Ortinau が[発表しました](https://devblogs.microsoft.com/dotnet/pin-clustering-in-dotnet-maui-maps/)。.NET MAUI 11 Preview 3 では、Android と iOS/Mac Catalyst でピンクラスタリングがすぐに使える状態で搭載されています。そして最高なのは — 有効にするのが驚くほど簡単だということです。

## すべてを支配する1つのプロパティ

```xml
<maps:Map IsClusteringEnabled="True" />
```

これだけです。近くのピンがカウントバッジ付きのクラスターにグループ化されます。ズームインすると展開。ズームアウトすると折りたたみ。モダンなマップならどれでも期待される動作 — それがたった1つのプロパティで手に入ります。

## 独立したクラスタリンググループ

ここからが面白いところです。すべてのピンが一緒にクラスタリングされるべきではありません。コーヒーショップと公園は別物で、マップもそれを知っているべきです。

`ClusteringIdentifier` プロパティを使えば、ピンを独立したグループに分けられます：

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

同じ識別子を持つピンは一緒にクラスタリングされます。異なる識別子は、地理的に近くても独立したクラスターを形成します。識別子なし？デフォルトグループです。シンプルで予測可能。

## クラスタータップの処理

ユーザーがクラスターをタップすると、必要なものがすべて揃った `ClusterClicked` イベントを受け取ります：

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

イベント引数には `Pins`（クラスター内のピン）、`Location`（地理的中心）、`Handled`（デフォルトのズーム動作をオーバーライドしたい場合は `true` に設定）が含まれます。シンプルで実用的、まさに期待通り。

## 知っておくべきプラットフォームの詳細

Android では、クラスタリングはズーム変更時に再計算するカスタムのグリッドベースアルゴリズムを使用します — 外部依存なし。iOS と Mac Catalyst では、MapKit のネイティブ `MKClusterAnnotation` サポートを活用しており、スムーズでプラットフォームネイティブなアニメーションを実現しています。

これは MAUI チームが正しい判断をしたケースの1つです — プラットフォームの力を活かすべきところで活かす。

## なぜこれが重要なのか

ピンクラスタリングは .NET MAUI で最もリクエストの多かった機能の1つです（[issue #11811](https://github.com/dotnet/maui/issues/11811)）。それも当然です。マップ上に場所を表示するすべてのアプリ — 配送追跡、店舗検索、不動産 — に必要です。以前は自分で実装するか、サードパーティライブラリを使う必要がありました。今は組み込みです。

クロスプラットフォームモバイルアプリを構築する .NET 開発者にとって、これはまさに MAUI をマップ中心のシナリオで実用的な選択肢にする生活の質の向上です。

## 始めよう

[.NET 11 Preview 3](https://dotnet.microsoft.com/download/dotnet/11.0) をインストールして .NET MAUI ワークロードを更新してください。[Maps サンプル](https://github.com/dotnet/maui-samples/tree/main/10.0/UserInterface/Views/Map/MapDemo/WorkingWithMaps)には新しいクラスタリングページが含まれており、すぐに試すことができます。

何か作ってみてください — そしてマップにやっと余裕を持たせましょう。
