---
title: "C# 15 intègre les types union — et c'est exactement ce qu'on demandait"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introduit le mot-clé union — des unions discriminées avec du pattern matching exhaustif imposé par le compilateur. Voici à quoi ça ressemble, pourquoi c'est important, et comment les essayer dès aujourd'hui."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Cet article a été traduit automatiquement. Pour la version originale, [cliquez ici]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}}).*

C'est celle que j'attendais. C# 15 introduit le mot-clé `union` — de vraies unions discriminées avec du pattern matching exhaustif imposé par le compilateur. Si vous avez déjà envié les unions discriminées de F# ou les enums de Rust, vous savez exactement pourquoi c'est important.

Bill Wagner a [publié l'analyse approfondie](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) sur le blog .NET, et franchement ? Le design est propre, pratique et très C#. Laissez-moi vous montrer ce qu'il y a vraiment et pourquoi c'est plus important qu'il n'y paraît à première vue.

## Le problème que les unions résolvent

Avant C# 15, retourner "l'un des plusieurs types possibles" depuis une méthode était toujours un compromis :

- **`object`** — pas de contraintes, pas d'aide du compilateur, du casting défensif partout
- **Interfaces marqueurs** — mieux, mais n'importe qui peut les implémenter. Le compilateur ne peut jamais considérer l'ensemble comme complet
- **Classes de base abstraites** — même problème, en plus les types ont besoin d'un ancêtre commun

Aucune de ces solutions ne vous donne ce que vous voulez vraiment : un ensemble fermé de types où le compilateur garantit que vous avez géré chaque cas. C'est ce que font les types union.

## La syntaxe est d'une simplicité élégante

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Une ligne. `Pet` peut contenir un `Cat`, un `Dog` ou un `Bird`. Les conversions implicites sont générées automatiquement :

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

Et voici la magie — le compilateur impose le matching exhaustif :

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Pas besoin de discard `_`. Le compilateur sait que ce switch couvre tous les cas possibles. Si vous ajoutez plus tard un quatrième type à l'union, chaque expression switch qui ne le gère pas produit un avertissement. Les cas manquants détectés au moment de la compilation, pas à l'exécution.

## Là où ça devient pratique

L'exemple de `Pet` est mignon, mais c'est ici que les unions brillent vraiment dans du vrai code.

### Des réponses API qui retournent différentes formes

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Maintenant chaque consommateur est obligé de gérer le succès, l'erreur et l'échec de validation. Plus de bugs "j'ai oublié de vérifier le cas d'erreur".

### Valeur unique ou collection

Le pattern `OneOrMore<T>` montre comment les unions peuvent avoir un corps avec des méthodes utilitaires :

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

Les appelants passent la forme qui leur convient :

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Composer des types sans relation

C'est la fonctionnalité décisive par rapport aux hiérarchies traditionnelles. Vous pouvez unir des types qui n'ont rien en commun — `string` et `Exception`, `int` et `IEnumerable<T>`. Pas besoin d'ancêtre commun.

## Unions personnalisées pour les bibliothèques existantes

Voici un choix de design intelligent : toute classe ou struct avec un attribut `[Union]` est reconnue comme un type union, tant qu'elle suit le pattern de base (constructeurs publics pour les types de cas et une propriété `Value`). Les bibliothèques comme OneOf qui fournissent déjà des types similaires aux unions peuvent opter pour le support du compilateur sans réécrire leurs internals.

Pour les scénarios sensibles à la performance avec des types valeur, les bibliothèques peuvent implémenter un pattern d'accès sans boxing avec les méthodes `HasValue` et `TryGetValue`.

## La vision d'ensemble

Les types union font partie d'une histoire plus large d'exhaustivité qui arrive en C# :

- **Types union** — matching exhaustif sur un ensemble fermé de types (disponible maintenant en preview)
- **Hiérarchies fermées** — le modificateur `closed` empêche les classes dérivées en dehors de l'assembly de définition (proposé)
- **Enums fermés** — empêche la création de valeurs autres que les membres déclarés (proposé)

Ensemble, ces trois fonctionnalités donneront à C# l'un des systèmes de pattern matching typé les plus complets de tous les langages mainstream.

## Essayez-les aujourd'hui

Les types union sont disponibles dans .NET 11 Preview 2 :

1. Installez le [SDK .NET 11 Preview](https://dotnet.microsoft.com/download/dotnet)
2. Ciblez `net11.0` dans votre projet
3. Définissez `<LangVersion>preview</LangVersion>`

Une mise en garde : dans Preview 2, vous devrez déclarer `UnionAttribute` et `IUnion` dans votre projet car ils ne sont pas encore dans le runtime. Récupérez [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) depuis le repo docs, ou ajoutez ceci :

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

## Pour conclure

Les types union sont une de ces fonctionnalités qui vous font vous demander comment on a pu s'en passer. Du matching exhaustif imposé par le compilateur, une syntaxe propre, le support des génériques et l'intégration avec le pattern matching existant — c'est tout ce qu'on demandait, fait à la manière C#.

Essayez-les dans .NET 11 Preview 2, cassez des trucs et [partagez vos retours sur GitHub](https://github.com/dotnet/csharplang/discussions/9663). C'est une preview, et l'équipe C# écoute activement. Vos cas limites et retours de design façonneront la version finale.

Pour la référence complète du langage, consultez la [documentation des types union](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) et la [spécification de la fonctionnalité](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
