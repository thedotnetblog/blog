---
title: "C# 15 introduce i tipi union — e sono esattamente quello che stavamo chiedendo"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introduce la parola chiave union — unioni discriminate con pattern matching esaustivo imposto dal compilatore. Ecco come appaiono, perché sono importanti e come provarle oggi."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "csharp-15-union-types-exhaustive-matching.md" >}}).*

Questa è quella che stavo aspettando. C# 15 introduce la parola chiave `union` — vere unioni discriminate con pattern matching esaustivo imposto dal compilatore. Se hai mai invidiato le unioni discriminate di F# o gli enum di Rust, sai esattamente perché questo è importante.

Bill Wagner ha [pubblicato l'approfondimento](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) sul blog .NET, e onestamente? Il design è pulito, pratico e molto C#. Lascia che ti mostri cosa c'è davvero e perché è una cosa più grande di quanto possa sembrare a prima vista.

## Il problema che le union risolvono

Prima di C# 15, restituire "uno tra diversi tipi possibili" da un metodo era sempre un compromesso:

- **`object`** — nessun vincolo, nessun aiuto dal compilatore, casting difensivo ovunque
- **Interfacce marcatore** — meglio, ma chiunque può implementarle. Il compilatore non può mai considerare l'insieme completo
- **Classi base astratte** — stesso problema, in più i tipi hanno bisogno di un antenato comune

Nessuna di queste ti dà quello che vuoi veramente: un insieme chiuso di tipi dove il compilatore garantisce che hai gestito ogni caso. Questo è quello che fanno i tipi union.

## La sintassi è di una semplicità elegante

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Una riga. `Pet` può contenere un `Cat`, un `Dog` o un `Bird`. Le conversioni implicite vengono generate automaticamente:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

Ed ecco la magia — il compilatore impone il matching esaustivo:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Nessun discard `_` necessario. Il compilatore sa che questo switch copre ogni caso possibile. Se successivamente aggiungi un quarto tipo alla union, ogni espressione switch che non lo gestisce produce un avviso. Casi mancanti rilevati al momento della compilazione, non a runtime.

## Dove diventa pratico

L'esempio di `Pet` è carino, ma è qui che le union brillano davvero nel codice reale.

### Risposte API che restituiscono forme diverse

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Ora ogni consumatore è obbligato a gestire successo, errore e fallimento di validazione. Niente più bug da "ho dimenticato di controllare il caso di errore".

### Valore singolo o collection

Il pattern `OneOrMore<T>` mostra come le union possono avere un corpo con metodi di utilità:

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

I chiamanti passano la forma che preferiscono:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Comporre tipi non correlati

Questa è la funzionalità killer rispetto alle gerarchie tradizionali. Puoi unire tipi che non hanno nulla in comune — `string` e `Exception`, `int` e `IEnumerable<T>`. Nessun antenato comune necessario.

## Union personalizzate per librerie esistenti

Ecco una scelta di design intelligente: qualsiasi classe o struct con un attributo `[Union]` viene riconosciuta come tipo union, purché segua il pattern di base (costruttori pubblici per i tipi di caso e una proprietà `Value`). Librerie come OneOf che già forniscono tipi simili alle union possono optare per il supporto del compilatore senza riscrivere i loro interni.

Per scenari sensibili alle performance con tipi di valore, le librerie possono implementare un pattern di accesso senza boxing con i metodi `HasValue` e `TryGetValue`.

## Il quadro generale

I tipi union fanno parte di una storia più ampia di esaustività in arrivo in C#:

- **Tipi union** — matching esaustivo su un insieme chiuso di tipi (disponibile ora in preview)
- **Gerarchie chiuse** — il modificatore `closed` impedisce classi derivate al di fuori dell'assembly di definizione (proposto)
- **Enum chiusi** — impedisce la creazione di valori diversi dai membri dichiarati (proposto)

Insieme, queste tre funzionalità daranno a C# uno dei sistemi di pattern matching type-safe più completi in qualsiasi linguaggio mainstream.

## Provale oggi

I tipi union sono disponibili in .NET 11 Preview 2:

1. Installa il [SDK .NET 11 Preview](https://dotnet.microsoft.com/download/dotnet)
2. Imposta come target `net11.0` nel tuo progetto
3. Imposta `<LangVersion>preview</LangVersion>`

Un'avvertenza: in Preview 2, dovrai dichiarare `UnionAttribute` e `IUnion` nel tuo progetto poiché non sono ancora nel runtime. Prendi [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) dal repo docs, o aggiungi questo:

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

## Per concludere

I tipi union sono una di quelle funzionalità che ti fanno chiedere come abbiamo fatto senza. Pattern matching esaustivo imposto dal compilatore, sintassi pulita, supporto ai generici e integrazione con il pattern matching esistente — è tutto quello che abbiamo chiesto, fatto alla maniera C#.

Provale in .NET 11 Preview 2, rompi cose e [condividi il tuo feedback su GitHub](https://github.com/dotnet/csharplang/discussions/9663). Questa è una preview, e il team C# sta attivamente ascoltando. I tuoi edge case e feedback di design daranno forma alla release finale.

Per il riferimento completo del linguaggio, consulta la [documentazione dei tipi union](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) e la [specifica della funzionalità](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
