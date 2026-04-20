---
title: "C# 15 Krijgt Union Types — En Ze Zijn Precies Wat We Vroegen"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 introduceert het `union` sleutelwoord — door de compiler afgedwongen gediscrimineerde unions met uitputtende patroonovereenkomst. Hoe ze eruitzien, waarom ze belangrijk zijn en hoe je ze vandaag kunt uitproberen."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

Dit is degene waar ik op heb gewacht. C# 15 introduceert het `union` sleutelwoord — echte gediscrimineerde unions met door de compiler afgedwongen uitputtende patroonovereenkomst.

Bill Wagner [publiceerde de diepgaande bespreking](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/).

## Het probleem dat unions oplossen

Vóór C# 15 was het terugkeren van "een van meerdere mogelijke typen" altijd een compromis. Je kreeg nooit wat je echt wilt: een gesloten set typen waarbij de compiler garandeert dat je elk geval hebt afgehandeld.

## De syntaxis is prachtig eenvoudig

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

En hier is de magie — de compiler dwingt uitputtende overeenkomst af:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Geen `_` nodig. Als je later een vierde type aan de union toevoegt, produceert elke switch-expressie die het niet afhandelt een waarschuwing.

## Waar dit praktisch wordt

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Nu is elke consument gedwongen succes, fout en validatiemislukking te behandelen.

## Probeer het vandaag

Union types zijn beschikbaar in .NET 11 Preview 2. Bekijk de [volledige taalreferentie](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union).
