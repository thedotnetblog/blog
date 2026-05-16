---
title: "Visual Studio の拡張機能プロジェクトに SDK スタイルサポートが追加"
date: 2026-05-13
author: "Emiliano Montesdeoca"
description: "Visual Studio 18.5 が VSSDK ベースの拡張機能に SDK スタイルプロジェクト形式の公式サポートを追加。小さな変更のビルド時間を最大 75% 削減し、プロジェクトファイルを約 20 行に簡略化。"
tags:
  - Visual Studio
  - .NET
  - Extensions
  - SDK-Style
---

*この投稿は自動翻訳されました。元のバージョンは[こちら]({{< ref "index.md" >}})。*

[VSSDK ベースの拡張機能プロジェクトへの SDK スタイルサポート](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)が Visual Studio 18.5 で正式に利用可能になりました — クラシックな VSIX 拡張機能プロジェクトは古い MPF スタイルの `.csproj` 形式から脱却できます。

## プロジェクトファイルの変化

最も目に見える変化は、プロジェクトファイルがどれほど小さくなるかです。典型的な VSSDK 拡張機能は今このような形になります：

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net472</TargetFramework>
    <VSSDKBuildToolsAutoSetup>true</VSSDKBuildToolsAutoSetup>
    <VsixDeployOnDebug>true</VsixDeployOnDebug>
    <GeneratePkgDefFile>true</GeneratePkgDefFile>
  </PropertyGroup>
  <ItemGroup><ProjectCapability Include="CreateVsixContainer" /></ItemGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.VisualStudio.SDK" Version="17.14.40265" ExcludeAssets="runtime" />
    <PackageReference Include="Microsoft.VSSDK.BuildTools" Version="18.5.38461" />
  </ItemGroup>
</Project>
```

`VSSDKBuildToolsAutoSetup=true` は適切なデフォルト値を適用します：`CreateVsixContainer=true` とレガシーの `DeployExtension=false`。この 1 つのプロパティが、以前は明示的に指定する必要があったものの大部分を置き換えます。

## ビルド時間の改善

Fast Up-To-Date Check とインクリメンタルビルドサポートが含まれています。大規模なソリューションでの小さな変更に対して、**ビルド時間が最大 75% 削減**されます — 大規模なホストソリューション内で拡張機能を反復開発している場合に大きな意味を持ちます。

## 新規プロジェクト vs 既存プロジェクト

18.5 で作成した新しい拡張機能プロジェクトは自動的に SDK スタイルを使用します。既存の MPF スタイル拡張機能は引き続き動作します — 移行はオプションです。移行時の注意点：XAML を使用している場合は `<UseWpf>true</UseWpf>` を追加してください。また、`.sln` または `.slnx` ファイルで拡張機能をデプロイ可能としてマークする必要があります。

vsixmanifest デザイナーはデフォルトで XML エディターに置き換えられています — 古いデザイナーが必要な場合は右クリック → [プログラムから開く]。

## エージェントによる移行パス

[vs-agent-plugins](https://github.com/microsoft/vs-agent-plugins) の Modernize エージェントが移行を自動化できます。Mads Kristensen の Smart Screen、Command Explorer、Postfix Templates、Whitespace Visualizer など、複数の実際の拡張機能がすでにこの方法で変換されています。

## 補足

VisualStudio.Extensibility（新しい拡張性フレームワーク）はすでに SDK スタイルをサポートしていました。このアップデートはクラシック VSSDK パスとの同等性をもたらします。唯一の要件は Visual Studio 拡張機能開発ワークロードです。

詳細は[公式ポスト](https://devblogs.microsoft.com/visualstudio/sdk-style-support-for-extension-projects/)をご覧ください。
