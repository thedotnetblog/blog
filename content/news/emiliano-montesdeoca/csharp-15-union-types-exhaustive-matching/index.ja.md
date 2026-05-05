---
title: "C# 15にユニオン型が登場 — まさに私たちが求めていたもの"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15がunionキーワードを導入 — コンパイラが強制する判別共用体と網羅的パターンマッチング。その見た目、重要な理由、そして今日試す方法を紹介します。"
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *この記事は自動翻訳されています。原文は[こちら]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}})をご覧ください。*

これこそ待ち望んでいたものです。C# 15が`union`キーワードを導入しました — コンパイラが強制する網羅的パターンマッチングを備えた本格的な判別共用体です。F#の判別共用体やRustのenumを羨ましく思ったことがあるなら、これがなぜ重要かすぐにわかるでしょう。

Bill Wagnerが.NETブログで[詳細な解説を公開しました](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/)。正直なところ、設計はクリーンで実用的、そしてとてもC#らしいです。実際に何があるのか、そしてなぜ一見した印象以上に大きな意味があるのかを見ていきましょう。

## ユニオンが解決する問題

C# 15以前では、メソッドから「複数の可能な型のうちの1つ」を返すことは常に妥協の産物でした：

- **`object`** — 制約なし、コンパイラの助けなし、あらゆるところで防御的キャスト
- **マーカーインターフェース** — より良いが、誰でも実装できる。コンパイラはセットが完全だと判断できない
- **抽象基底クラス** — 同じ問題、さらに型に共通の祖先が必要

これらのどれも本当に欲しいものを提供してくれません：コンパイラがすべてのケースを処理したことを保証する閉じた型のセット。ユニオン型がそれを実現します。

## 構文は美しくシンプル

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

1行だけ。`Pet`は`Cat`、`Dog`、または`Bird`を保持できます。暗黙的な変換は自動的に生成されます：

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

そしてここが魔法です — コンパイラが網羅的マッチングを強制します：

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

ディスカード`_`は不要です。コンパイラはこのswitchがすべての可能なケースをカバーしていることを知っています。後から4番目の型をユニオンに追加すると、それを処理しないすべてのswitch式が警告を生成します。不足しているケースがランタイムではなくビルド時にキャッチされます。

## 実用的になるところ

`Pet`の例はかわいいですが、ここからがユニオンが本当のコードで輝くところです。

### 異なる形状を返すAPIレスポンス

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

これですべてのコンシューマは成功、エラー、バリデーション失敗を処理することを強制されます。「エラーケースのチェックを忘れた」バグはもうありません。

### 単一値またはコレクション

`OneOrMore<T>`パターンは、ユニオンがヘルパーメソッドを持つボディを持てることを示しています：

```csharp
public union OneOrMore<T>(T, IEnumerable<T>)
{
    public IEnumerable<T> AsEnumerable() => Value switch
    {
        T single => [single],
        IEnumerable<T> multiple => multiple,
        null => []
    };
}
```

呼び出し側は便利な方の形式を渡します：

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### 無関係な型の合成

これは従来の階層に対するキラー機能です。共通点のない型をユニオンにできます — `string`と`Exception`、`int`と`IEnumerable<T>`。共通の祖先は不要です。

## 既存ライブラリ用のカスタムユニオン

ここにはスマートな設計判断があります：基本パターン（ケース型のパブリックコンストラクタと`Value`プロパティ）に従っている限り、`[Union]`属性を持つ任意のクラスやstructがユニオン型として認識されます。すでにユニオンライクな型を提供しているOneOfのようなライブラリは、内部を書き直すことなくコンパイラサポートにオプトインできます。

値型を使うパフォーマンスに敏感なシナリオでは、ライブラリは`HasValue`と`TryGetValue`メソッドによるボックス化なしのアクセスパターンを実装できます。

## より大きな視点

ユニオン型はC#に来るより広い網羅性ストーリーの一部です：

- **ユニオン型** — 閉じた型セットに対する網羅的マッチング（プレビューで利用可能）
- **閉じた階層** — `closed`修飾子が定義アセンブリ外の派生クラスを防止（提案中）
- **閉じたenum** — 宣言されたメンバー以外の値の作成を防止（提案中）

これら3つの機能が合わさることで、C#はあらゆるメインストリーム言語の中で最も包括的な型安全パターンマッチングシステムの1つを手に入れることになります。

## 今日試してみよう

ユニオン型は.NET 11 Preview 2で利用可能です：

1. [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)をインストール
2. プロジェクトで`net11.0`をターゲットに設定
3. `<LangVersion>preview</LangVersion>`を設定

1つ注意点：Preview 2では、ランタイムにまだ含まれていないため、プロジェクトで`UnionAttribute`と`IUnion`を宣言する必要があります。docsリポジトリから[RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs)を取得するか、以下を追加してください：

```csharp
namespace System.Runtime.CompilerServices
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Struct,
        AllowMultiple = false)]
    public sealed class UnionAttribute : Attribute;

    public interface IUnion
    {
        object? Value { get; }
    }
}
```

## まとめ

ユニオン型は、それなしでどうやってきたのか不思議に思わせる機能の1つです。コンパイラが強制する網羅的マッチング、クリーンな構文、ジェネリックサポート、既存のパターンマッチングとの統合 — 私たちが求めていたすべてが、C#のやり方で実現されています。

.NET 11 Preview 2で試して、壊して、[GitHubでフィードバックを共有してください](https://github.com/dotnet/csharplang/discussions/9663)。これはプレビューであり、C#チームは積極的に耳を傾けています。あなたのエッジケースとデザインフィードバックが最終リリースを形作ります。

完全な言語リファレンスについては、[ユニオン型のドキュメント](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union)と[機能仕様](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions)をご覧ください。
