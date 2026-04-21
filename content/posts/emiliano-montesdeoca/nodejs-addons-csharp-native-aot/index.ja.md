---
title: ".NET Native AOT を使って C# で Node.js ネイティブアドオンを書く"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "C# Dev Kit チームは C++ で書かれた Node.js アドオンを .NET Native AOT で置き換えました — 結果はよりクリーンで安全、.NET SDK だけで動きます。"
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *この記事は自動翻訳されました。英語の原文は[こちら]({{< ref "index.md" >}})からご覧いただけます。*

こんなシナリオが好きです。.NET ツールを開発するチームが、C++ で書かれネイティブ Node.js アドオンを `node-gyp` でコンパイルして使っていました。動いてはいました。でも、誰もが直接触らないパッケージをビルドするためだけに、チーム全員の開発マシンに Python（しかも古いバージョン）をインストールする必要がありました。

そこで、チームはとても合理的な疑問を持ちました。「.NET SDK はもうインストールされているのに、なぜ C++ を書いているのか？」

答えは Native AOT でした。結果は本当にエレガントです。

## 基本的なアイデア

Node.js ネイティブアドオンは、Node.js が実行時にロードできる共有ライブラリ（Windows では `.dll`、Linux では `.so`、macOS では `.dylib`）です。インターフェースは [N-API](https://nodejs.org/api/n-api.html) — 安定した ABI 互換の C API です。N-API はどの言語がライブラリを作ったかを気にせず、正しいシンボルをエクスポートするかどうかだけを確認します。

.NET Native AOT はまさにそれを作れます。C# コードを事前にネイティブ共有ライブラリにコンパイルし、任意のエントリーポイントを持たせることができます。これがトリックのすべてです。

## プロジェクトのセットアップ

プロジェクトファイルはシンプルです：

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` は `dotnet publish` 時に共有ライブラリを生成するよう SDK に指示します。`AllowUnsafeBlocks` は N-API の interop で関数ポインタと固定バッファを使うために必要です。

## エントリーポイントのエクスポート

Node.js はライブラリが `napi_register_module_v1` をエクスポートすることを期待します。C# では `[UnmanagedCallersOnly]` がまさにそれを行います：

```csharp
public static unsafe partial class RegistryAddon
{
    [UnmanagedCallersOnly(
        EntryPoint = "napi_register_module_v1",
        CallConvs = [typeof(CallConvCdecl)])]
    public static nint Init(nint env, nint exports)
    {
        Initialize();
        RegisterFunction(env, exports, "readStringValue"u8, &ReadStringValue);
        return exports;
    }
}
```

注目点：`nint` はネイティブサイズの整数 — `intptr_t` のマネージド等価物です。`u8` サフィックスは UTF-8 文字列リテラルを含む `ReadOnlySpan<byte>` を生成し、エンコーディングアロケーションなしで直接 N-API に渡します。`[UnmanagedCallersOnly]` は Node.js が探す正確なエントリーポイント名でメソッドをエクスポートします。

## N-API をホストプロセスに対して解決する

N-API 関数は別のライブラリではなく `node.exe` 自身がエクスポートします。そのため、何かにリンクする代わりに、起動時に実行中のプロセスに対して解決します：

```csharp
private static void Initialize()
{
    NativeLibrary.SetDllImportResolver(
        System.Reflection.Assembly.GetExecutingAssembly(),
        ResolveDllImport);

    static nint ResolveDllImport(
        string libraryName, Assembly assembly, DllImportSearchPath? searchPath)
    {
        if (libraryName is not "node") return 0;
        return NativeLibrary.GetMainProgramHandle();
    }
}
```

これにより、P/Invoke 宣言が `[LibraryImport]` とソース生成マーシャリングで正しく動作します。

## 実際のエクスポート関数

チームが作ったレジストリリーダーの完全な関数：

```csharp
[UnmanagedCallersOnly(CallConvs = [typeof(CallConvCdecl)])]
private static nint ReadStringValue(nint env, nint info)
{
    try
    {
        var keyPath = GetStringArg(env, info, 0);
        var valueName = GetStringArg(env, info, 1);

        if (keyPath is null || valueName is null)
        {
            ThrowError(env, "Expected two string arguments: keyPath, valueName");
            return 0;
        }

        using var key = Registry.CurrentUser.OpenSubKey(keyPath, writable: false);

        return key?.GetValue(valueName) is string value
            ? CreateString(env, value)
            : GetUndefined(env);
    }
    catch (Exception ex)
    {
        ThrowError(env, $"Registry read failed: {ex.Message}");
        return 0;
    }
}
```

`try/catch` に関する重要な注意：`[UnmanagedCallersOnly]` メソッドで未処理の例外が発生するとホストプロセスがクラッシュします。常に例外をキャッチし、`ThrowError` で JavaScript に転送してください。

## TypeScript から呼び出す

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#、Python なし、C++ なし。

## 何を得たか

即時のメリットはコントリビューター体験の向上です。特定の Python バージョンが不要になり、`yarn install` は Node.js と .NET SDK だけで動作します。CI パイプラインも簡素化されました。パフォーマンスは C++ 実装と同等でした。

## まとめ

C# Dev Kit チームは Python/C++ の複雑さを、チーム全員がすでに書けてデバッグできる Clean な C# コードに置き換えました。文字列マーシャリングヘルパーを含む完全なウォークスルーは、[.NET ブログのオリジナル記事](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/)をご覧ください。
