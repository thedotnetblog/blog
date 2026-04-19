---
title: "C# 15 obté tipus d'unió, i són exactament el que hem estat demanant"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introdueix la paraula clau union: unions discriminades aplicades pel compilador amb una concordança exhaustiva de patrons. Aquí teniu el seu aspecte, per què importen i com provar-los avui."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

Aquest és el que estava esperant. C# 15 introdueix la paraula clau `union`: unions discriminades adequades amb una concordança exhaustiva de patrons forçada pel compilador. Si alguna vegada has envejat els sindicats discriminats de F# o les enumeracions de Rust, saps exactament per què això importa.

Bill Wagner [va publicar la immersió profunda](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/) al bloc.NET, i sincerament? El disseny és net, pràctic i molt C#. Permeteu-me explicar-vos què hi ha realment aquí i per què és una cosa més gran del que pot semblar a primera vista.

## El problema que resolen els sindicats

Abans de C# 15, retornar "un dels diversos tipus possibles" d'un mètode sempre era un compromís:

- **`object`** — sense restriccions, sense ajuda del compilador, llançament defensiu a tot arreu
- **Interfícies de marcador**: millor, però qualsevol pot implementar-les. El compilador mai pot considerar el conjunt complet
- **Classes base abstractes**: el mateix problema, a més els tipus necessiten un avantpassat comú

Cap d'aquests us ofereix el que realment voleu: un conjunt tancat de tipus on el compilador garanteix que heu gestionat tots els casos. Això és el que fan els sindicats.

## La sintaxi és molt senzilla

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

Una línia. `Pet` pot contenir un `Cat`, un `Dog` o un `Bird`. Les conversions implícites es generen automàticament:

```csharp
Pet pet = new Dog("Rex");
Console.WriteLine(pet.Value); // Dog { Name = Rex }
```

I aquí està la màgia: el compilador imposa una concordança exhaustiva:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

No cal descartar `_`. El compilador sap que aquest commutador cobreix tots els casos possibles. Si més tard afegiu un quart tipus a la unió, cada expressió de commutació que no la gestioni produeix un avís. Casos que falten capturats en temps de compilació, no en temps d'execució.

## On això es fa pràctic

L'exemple `Pet` és bonic, però aquí és on els sindicats realment brillen en codi real.

### Respostes de l'API que retornen diferents formes

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Ara tots els consumidors es veuen obligats a gestionar l'èxit, l'error i el fracàs de validació. No hi ha més errors "m'he oblidat de comprovar el cas d'error".

### Valor únic o col·lecció

El patró `OneOrMore<T>` mostra com els sindicats poden tenir un cos amb mètodes auxiliars:

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

Les persones que trucen passen el formulari que sigui convenient:

```csharp
OneOrMore<string> tags = "dotnet";
OneOrMore<string> moreTags = new[] { "csharp", "unions", "preview" };

foreach (var tag in tags.AsEnumerable())
    Console.Write($"[{tag}] ");
// [dotnet]
```

### Composició de tipus no relacionats

Aquesta és la característica assassina de les jerarquies tradicionals. Podeu unir tipus que no tenen res en comú: `string` i `Exception`, `int` i `IEnumerable<T>`. No es necessita cap avantpassat comú.

## Unions personalitzades per a biblioteques existents

Aquí teniu una opció de disseny intel·ligent: qualsevol classe o estructura amb un atribut `[Union]` es reconeix com a tipus d'unió, sempre que segueixi el patró bàsic (constructors públics per a tipus de casos i una propietat `Value`). Les biblioteques com OneOf que ja proporcionen tipus d'unió poden optar al suport del compilador sense reescriure els seus elements interns.

Per a escenaris sensibles al rendiment amb tipus de valors, les biblioteques poden implementar un patró d'accés que no sigui boxing amb mètodes `HasValue` i `TryGetValue`.

## La imatge més gran

Els tipus d'unió formen part d'una història d'exhaustivitat més àmplia que arriba a C#:

- **Tipus d'unió**: concordança exhaustiva sobre un conjunt tancat de tipus (disponible ara a la vista prèvia)
- **Jerarquies tancades** — El modificador `closed` impedeix classes derivades fora del conjunt definidor (proposat)
- **Enumeracions tancades**: impedeix la creació de valors diferents dels membres declarats (proposat)

En conjunt, aquestes tres funcions donaran a C# un dels sistemes de concordança de patrons segurs de tipus més complets en qualsevol llenguatge convencional.

## Prova-ho avui

Els tipus d'unió estan disponibles a.NET 11 Preview 2:

1. Instal·leu [.NET 11 Preview SDK](https://dotnet.microsoft.com/download/dotnet)
2. Orienta `net11.0` al teu projecte
3. Establiu `<LangVersion>preview</LangVersion>`

Una advertència: a la vista prèvia 2, haureu de declarar `UnionAttribute` i `IUnion` al vostre projecte, ja que encara no estan en temps d'execució. Agafeu [RuntimePolyfill.cs](https://github.com/dotnet/docs/blob/e68b5dd1e557b53c45ca43e61b013bc919619fb9/docs/csharp/language-reference/builtin-types/snippets/unions/RuntimePolyfill.cs) del dipòsit de documents o afegiu això:

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

## Tancant

Els tipus d'unió són una d'aquestes característiques que us fan preguntar-vos com ens ho hem passat sense ells. Coincidència exhaustiva forçada pel compilador, sintaxi neta, suport genèric i integració amb la concordança de patrons existents: és tot el que hem estat demanant, fet de la manera C#.

Proveu-los a.NET 11 Preview 2, trenca coses i [compartiu els vostres comentaris a GitHub](https://github.com/dotnet/csharplang/discussions/9663). Aquesta és una vista prèvia i l'equip de C# escolta activament. Els vostres casos de punta i els vostres comentaris sobre el disseny donaran forma a la versió final.

Per obtenir la referència completa de l'idioma, consulteu els [documents de tipus unió](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) i l'[especificació de la funció](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions).
