---
title: "Escrevendo addons nativos Node.js em C# com .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "O time do C# Dev Kit substituiu addons Node.js escritos em C++ por .NET Native AOT — o resultado é mais limpo, mais seguro e só precisa do SDK do .NET."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Este artigo foi traduzido automaticamente. Para ver a versão original em inglês, [clique aqui]({{< ref "index.md" >}}).*

Um cenário que adoro: um time que trabalha com ferramentas .NET tinha addons nativos do Node.js escritos em C++ e compilados via `node-gyp`. Funcionava. Mas exigia Python instalado na máquina de cada desenvolvedor — uma versão antiga de Python, diga-se — só para construir um pacote que ninguém no time tocaria diretamente.

Então fizeram uma pergunta muito razoável: já temos o SDK do .NET instalado, por que estamos escrevendo C++?

A resposta foi Native AOT, e o resultado é genuinamente elegante.

## A ideia básica

Um addon nativo do Node.js é uma biblioteca compartilhada (`.dll` no Windows, `.so` no Linux, `.dylib` no macOS) que o Node.js pode carregar em tempo de execução. A interface se chama [N-API](https://nodejs.org/api/n-api.html) — uma API C estável e compatível com ABI. A N-API não se importa com que linguagem produziu a biblioteca, só que ela exporte os símbolos certos.

O .NET Native AOT pode produzir exatamente isso. Ele compila o código C# ahead-of-time em uma biblioteca nativa compartilhada com pontos de entrada arbitrários. Esse é todo o truque.

## Configuração do projeto

O arquivo de projeto é mínimo:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` diz ao SDK para produzir uma biblioteca compartilhada no `dotnet publish`. `AllowUnsafeBlocks` é necessário para o interop com N-API usando ponteiros de função e buffers fixos.

## Exportar o ponto de entrada

O Node.js espera que sua biblioteca exporte `napi_register_module_v1`. Em C#, `[UnmanagedCallersOnly]` faz exatamente isso:

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

Coisas que valem destaque: `nint` é um inteiro de tamanho nativo — o equivalente gerenciado de `intptr_t`. O sufixo `u8` produz um `ReadOnlySpan<byte>` com um literal de string UTF-8, passado diretamente para a N-API sem nenhuma alocação de codificação. E `[UnmanagedCallersOnly]` exporta o método com exatamente o nome do ponto de entrada que o Node.js procura.

## Resolver N-API contra o processo host

As funções N-API são exportadas pelo próprio `node.exe`, não por uma biblioteca separada. Então, em vez de linkar contra algo, você as resolve contra o processo em execução na inicialização:

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

Com isso, as declarações P/Invoke funcionam corretamente com `[LibraryImport]` e marshalling gerado por código-fonte.

## Uma função exportada real

Aqui está o leitor de registro que construíram:

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

Nota importante sobre o `try/catch`: uma exceção não tratada em um método `[UnmanagedCallersOnly]` derruba o processo host. Sempre capture e encaminhe ao JavaScript via `ThrowError`.

## Chamando a partir do TypeScript

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#, sem Python, sem C++.

## O que ganharam

A vitória imediata foi na experiência do contribuidor: nenhuma versão específica de Python necessária, `yarn install` funciona com apenas Node.js e o SDK do .NET. Pipelines de CI também ficaram mais simples. A performance foi comparável à implementação em C++.

## Conclusão

O time do C# Dev Kit substituiu a sobrecarga Python/C++ por código C# limpo que todo o time já sabe escrever e depurar. Para o walkthrough completo com todos os helpers de marshalling de strings, veja o [artigo original no blog .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
