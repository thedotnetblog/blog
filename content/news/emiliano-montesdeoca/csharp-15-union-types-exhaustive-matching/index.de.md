---
title: "C# 15 bekommt Union Types — und sie sind genau das, was wir uns gewünscht haben"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 führt das union-Schlüsselwort ein — compiler-erzwungene diskriminierte Unions mit erschöpfendem Pattern Matching. So sehen sie aus, warum sie wichtig sind und wie man sie heute ausprobieren kann."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}}).*

Das ist das Feature, auf das ich gewartet habe. C# 15 führt das `union`-Schlüsselwort ein — echte diskriminierte Unions mit compiler-erzwungenem erschöpfendem Pattern Matching. Wenn du jemals die diskriminierten Unions von F# oder die Enums von Rust beneidet hast, weißt du genau, warum das wichtig ist.

Bill Wagner hat [den Deep Dive veröffentlicht](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) auf dem .NET Blog, und ehrlich? Das Design ist sauber, praktisch und sehr C#. Lass mich dir zeigen, was wirklich hier ist und warum es eine größere Sache ist, als es auf den ersten Blick scheint.

## Das Problem, das Unions lösen

Vor C# 15 war die Rückgabe von "einem von mehreren möglichen Typen" aus einer Methode immer ein Kompromiss:

- **`object`** — keine Einschränkungen, keine Compiler-Hilfe, defensives Casting überall
- **Marker-Interfaces** — besser, aber jeder kann sie implementieren. Der Compiler kann die Menge nie als vollständig betrachten
- **Abstrakte Basisklassen** — gleiches Problem, plus die Typen brauchen einen gemeinsamen Vorfahren

Nichts davon gibt dir, was du eigentlich willst: eine geschlossene Menge von Typen, bei der der Compiler garantiert, dass du jeden Fall behandelt hast. Das ist es, was Union Types machen.

## Die Syntax ist wunderschön einfach

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Eine Zeile. `Pet` kann eine `Cat`, einen `Dog` oder einen `Bird` enthalten. Implizite Konvertierungen werden automatisch generiert:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

Und hier ist die Magie — der Compiler erzwingt erschöpfendes Matching:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Kein Discard `_` nötig. Der Compiler weiß, dass dieser Switch jeden möglichen Fall abdeckt. Wenn du später einen vierten Typ zur Union hinzufügst, erzeugt jeder Switch-Ausdruck, der ihn nicht behandelt, eine Warnung. Fehlende Fälle werden zur Build-Zeit erkannt, nicht zur Laufzeit.

## Wo das praktisch wird

Das `Pet`-Beispiel ist nett, aber hier glänzen Unions wirklich in echtem Code.

### API-Antworten, die verschiedene Formen zurückgeben

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Jetzt ist jeder Konsument gezwungen, Erfolg, Fehler und Validierungsfehler zu behandeln. Keine "Ich habe vergessen, den Fehlerfall zu prüfen"-Bugs mehr.

### Einzelwert oder Collection

Das `OneOrMore<T>`-Muster zeigt, wie Unions einen Body mit Hilfsmethoden haben können:

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

Aufrufer übergeben die Form, die ihnen passt:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Unrelated Typen zusammensetzen

Das ist das Killer-Feature gegenüber traditionellen Hierarchien. Du kannst Typen vereinen, die nichts gemeinsam haben — `string` und `Exception`, `int` und `IEnumerable<T>`. Kein gemeinsamer Vorfahre nötig.

## Custom Unions für bestehende Bibliotheken

Hier ist eine clevere Design-Entscheidung: Jede Klasse oder Struct mit einem `[Union]`-Attribut wird als Union-Typ erkannt, solange sie dem grundlegenden Muster folgt (öffentliche Konstruktoren für Case-Typen und eine `Value`-Property). Bibliotheken wie OneOf, die bereits Union-ähnliche Typen bereitstellen, können sich für Compiler-Unterstützung entscheiden, ohne ihre Interna umzuschreiben.

Für performance-sensitive Szenarien mit Werttypen können Bibliotheken ein Boxing-freies Zugriffsmuster mit `HasValue`- und `TryGetValue`-Methoden implementieren.

## Das große Ganze

Union Types sind Teil einer breiteren Exhaustiveness-Story, die zu C# kommt:

- **Union Types** — erschöpfendes Matching über eine geschlossene Menge von Typen (jetzt in Preview verfügbar)
- **Geschlossene Hierarchien** — der `closed`-Modifier verhindert abgeleitete Klassen außerhalb der definierenden Assembly (vorgeschlagen)
- **Geschlossene Enums** — verhindert die Erstellung von Werten außer den deklarierten Membern (vorgeschlagen)

Zusammen werden diese drei Features C# eines der umfassendsten typsicheren Pattern-Matching-Systeme in jeder Mainstream-Sprache geben.

## Probier es heute aus

Union Types sind in .NET 11 Preview 2 verfügbar:

1. Installiere das [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)
2. Setze `net11.0` als Target in deinem Projekt
3. Setze `<LangVersion>preview</LangVersion>`

Ein Hinweis: In Preview 2 musst du `UnionAttribute` und `IUnion` in deinem Projekt deklarieren, da sie noch nicht in der Runtime sind. Hol dir [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) aus dem Docs-Repo, oder füge das hinzu:

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

## Fazit

Union Types sind eines dieser Features, bei denen man sich fragt, wie wir ohne sie ausgekommen sind. Compiler-erzwungenes erschöpfendes Matching, saubere Syntax, generische Unterstützung und Integration mit bestehendem Pattern Matching — es ist alles, was wir wollten, auf die C#-Art umgesetzt.

Probier sie in .NET 11 Preview 2 aus, mach Sachen kaputt und [teile dein Feedback auf GitHub](https://github.com/dotnet/csharplang/discussions/9663). Das ist Preview, und das C#-Team hört aktiv zu. Deine Edge Cases und Design-Feedback werden die finale Version formen.

Für die vollständige Sprachreferenz, schau dir die [Union Types-Dokumentation](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) und die [Feature-Spezifikation](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions) an.
