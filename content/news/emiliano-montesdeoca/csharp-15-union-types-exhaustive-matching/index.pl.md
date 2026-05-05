---
title: "C# 15 Dostaje Typy Unii — I Są Dokładnie Tym, O Co Prosiliśmy"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 wprowadza słowo kluczowe `union` — dyskryminowane unie egzekwowane przez kompilator z wyczerpującym dopasowaniem wzorców. Oto jak wyglądają, dlaczego mają znaczenie i jak je wypróbować."
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

Na to czekałem. C# 15 wprowadza słowo kluczowe `union` — właściwe dyskryminowane unie z wyczerpującym dopasowaniem wzorców egzekwowanym przez kompilator.

Bill Wagner [opublikował głębokie omówienie](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/).

## Problem rozwiązywany przez unie

Przed C# 15, zwracanie "jednego z kilku możliwych typów" było zawsze kompromisem. Nigdy nie dostawałeś tego, czego naprawdę chcesz: zamkniętego zbioru typów, gdzie kompilator gwarantuje, że obsłużyłeś każdy przypadek.

## Składnia jest pięknie prosta

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

A oto magia — kompilator egzekwuje wyczerpujące dopasowanie:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

Nie potrzeba `_`. Jeśli później dodasz czwarty typ do unii, każde wyrażenie switch, które go nie obsługuje, generuje ostrzeżenie.

## Zastosowanie praktyczne

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

Teraz każdy konsument jest zmuszony obsłużyć sukces, błąd i niepowodzenie walidacji.

## Wypróbuj już dziś

Typy unii są dostępne w .NET 11 Preview 2. Sprawdź [pełną dokumentację](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union).
