---
title: "Écrire des addons natifs Node.js en C# avec .NET Native AOT"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "L'équipe C# Dev Kit a remplacé des addons Node.js écrits en C++ par .NET Native AOT — le résultat est plus propre, plus sûr et ne nécessite que le SDK .NET."
tags:
  - .NET
  - C#
  - Native AOT
  - Node.js
  - VS Code
  - Interop
  - Developer Tooling
---

> *Cet article a été traduit automatiquement. Pour la version originale en anglais, [clique ici]({{< ref "index.md" >}}).*

Voilà un scénario que j'adore : une équipe qui travaille sur des outils .NET avait des addons natifs Node.js écrits en C++ et compilés via `node-gyp`. Ça fonctionnait. Mais ça nécessitait Python sur chaque machine de développeur — une vieille version de Python, par-dessus le marché — juste pour construire un package que personne dans l'équipe ne toucherait directement.

Ils se sont donc posé une question très raisonnable : on a déjà le SDK .NET installé, pourquoi écrit-on du C++ ?

La réponse était Native AOT, et le résultat est vraiment élégant. Drew Noakes de l'équipe C# Dev Kit a documenté comment ils l'ont fait, et je pense que ça vaut la peine de comprendre — même si tu ne construis pas d'extensions VS Code.

## L'idée de base

Un addon natif Node.js est une bibliothèque partagée (`.dll` sous Windows, `.so` sous Linux, `.dylib` sous macOS) que Node.js peut charger au runtime. L'interface s'appelle [N-API](https://nodejs.org/api/n-api.html) — une API C stable et compatible ABI. N-API se fiche du langage qui a produit la bibliothèque, tant qu'elle exporte les bons symboles.

.NET Native AOT peut produire exactement ça. Il compile le code C# en avance en une bibliothèque partagée native avec des points d'entrée arbitraires. C'est tout le truc.

## Configuration du projet

Le fichier projet est minimal :

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <PublishAot>true</PublishAot>
    <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
  </PropertyGroup>
</Project>
```

`PublishAot` dit au SDK de produire une bibliothèque partagée à `dotnet publish`. `AllowUnsafeBlocks` est nécessaire pour l'interop N-API avec des pointeurs de fonctions et des buffers fixes.

## Exporter le point d'entrée

Node.js s'attend à ce que ta bibliothèque exporte `napi_register_module_v1`. En C#, `[UnmanagedCallersOnly]` fait exactement ça :

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

Quelques points à noter : `nint` est un entier de taille native — l'équivalent managé de `intptr_t`. Le suffixe `u8` produit un `ReadOnlySpan<byte>` avec un littéral de chaîne UTF-8, passé directement à N-API sans aucune allocation d'encodage. Et `[UnmanagedCallersOnly]` exporte la méthode avec exactement le nom de point d'entrée que Node.js cherche.

## Résoudre N-API contre le processus hôte

Les fonctions N-API sont exportées par `node.exe` lui-même, pas une bibliothèque séparée. Donc au lieu de lier contre quelque chose, on les résout contre le processus en cours au démarrage :

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

Avec ça en place, les déclarations P/Invoke fonctionnent proprement avec `[LibraryImport]` et le marshalling généré par la source.

## Une vraie fonction exportée

Voici le lecteur de registre qu'ils ont construit :

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

Note importante sur le `try/catch` : une exception non gérée dans une méthode `[UnmanagedCallersOnly]` plante le processus hôte. Toujours attraper et transmettre à JavaScript via `ThrowError`.

## Appeler depuis TypeScript

```typescript
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon;
const sdkPath = registry.readStringValue(
    'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation');
```

TypeScript → C#, sans Python, sans C++.

## Ce qu'ils ont gagné

La victoire immédiate : l'expérience contributeur. Plus besoin d'une version Python spécifique, `yarn install` fonctionne avec Node.js et le SDK .NET. Les pipelines CI sont aussi plus simples. Les performances sont comparables à l'implémentation C++.

## Conclusion

L'équipe C# Dev Kit a remplacé la complexité Python/C++ par du C# propre que toute l'équipe sait déjà écrire et déboguer. Pour le walkthrough complet avec tous les helpers de marshalling de chaînes, consulte l'[article original sur le blog .NET](https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/).
