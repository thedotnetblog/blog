---
title: ".NET 10 が Ubuntu 26.04 LTS に搭載 — 新機能まとめ"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Ubuntu 26.04 LTS (Resolute Raccoon) が .NET 10 をファーストクラスのツールチェーンとして搭載。Native AOT、Chiseled コンテナ、Linux 7.0。"
tags:
  - .NET
  - Linux
  - Ubuntu
  - Containers
  - Docker
  - Native AOT
  - .NET 10
---

*この投稿は自動翻訳されました。元の記事は[こちら]({{< ref "index.md" >}})をご覧ください。*

Ubuntu LTS の日です。[Ubuntu 26.04 (Resolute Raccoon)](https://canonical.com/blog/canonical-releases-ubuntu-26-04-lts-resolute-raccoon) が今日リリースされ、すべての Ubuntu LTS と同様に最新の .NET LTS — この場合 [.NET 10](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/) — を搭載しています。

## .NET 10 を 2 つのコマンドでインストール

```bash
sudo apt update
sudo apt install dotnet-sdk-10.0
```

.NET は [Ubuntu 公式サポートのツールチェーン](https://ubuntu.com/toolchains)の一つです。サードパーティのアドオンではありません。

## コンテナ：`-noble` を `-resolute` に更新

```bash
sed -i "s/noble/resolute/g" Dockerfile
```

[Chiseled](https://devblogs.microsoft.com/dotnet/announcing-dotnet-chiseled-containers/) を含む既存のすべてのイメージバリアントが利用可能です。

## Native AOT：3ms 起動、1.4MB バイナリ

```bash
apt install -y dotnet-sdk-aot-10.0 clang
dotnet publish app.cs
# artifacts/app/app — 1.4MB ネイティブバイナリ
# real 0m0.003s
```

コールドスタート時間が重要なクラウドネイティブワークロード — Functions、コンテナ、サーバーレス — にとって真のゲームチェンジャーです。

## .NET 8 または 9 が必要な場合

```bash
apt install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt install -y dotnet-sdk-8.0
```

[完全な記事](https://devblogs.microsoft.com/dotnet/whats-new-for-dotnet-in-ubuntu-2604/)で cgroup v2、ポスト量子暗号、Linux 7.0 の詳細を確認してください。
