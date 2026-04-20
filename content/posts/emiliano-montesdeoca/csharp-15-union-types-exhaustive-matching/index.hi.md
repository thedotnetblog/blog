---
title: "C# 15 में Union Types आए — और वे exactly वही हैं जो हम माँग रहे थे"
date: 2026-04-05
author: "Emiliano Montesdeoca"
description: "C# 15 `union` keyword introduce करता है — compiler-enforced discriminated unions exhaustive pattern matching के साथ। वे कैसे दिखते हैं, क्यों मायने रखते हैं, और आज उन्हें कैसे try करें।"
tags:
  - csharp
  - dotnet
  - union-types
  - pattern-matching
  - dotnet-11
  - language-features
---

> *यह पोस्ट स्वचालित रूप से अनुवादित है। मूल के लिए, [यहाँ क्लिक करें]({{< ref "csharp-15-union-types-exhaustive-matching" >}}).*

यह वह feature है जिसका मैं इंतजार कर रहा था। C# 15 `union` keyword introduce करता है — proper discriminated unions जिनमें compiler-enforced exhaustive pattern matching है।

Bill Wagner ने [deep dive publish किया](https://devblogs.microsoft.com/dotnet/csharp-15-union-types/)।

## Unions किस problem को solve करते हैं

C# 15 से पहले, method से "कई possible types में से एक" return करना हमेशा एक compromise था। आपको वह नहीं मिलता था जो आप actually चाहते थे: types का एक closed set जहाँ compiler guarantee करे कि आपने हर case handle किया।

## Syntax beautifully simple है

```csharp
public record class Cat(string Name);
public record class Dog(string Name);
public record class Bird(string Name);

public union Pet(Cat, Dog, Bird);
```

और यहाँ magic है — compiler exhaustive matching enforce करता है:

```csharp
string name = pet switch
{
    Dog d => d.Name,
    Cat c => c.Name,
    Bird b => b.Name,
};
```

कोई discard `_` नहीं चाहिए। अगर आप बाद में union में चौथा type add करते हैं, तो हर switch expression जो उसे handle नहीं करती warning produce करती है।

## Practical कहाँ है

```csharp
public union ApiResult<T>(T, ApiError, ValidationFailure);
```

अब हर consumer को success, error, और validation failure handle करना होगा।

## आज Try करें

Union types .NET 11 Preview 2 में available हैं। [Full language reference](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/union) और [feature specification](https://learn.microsoft.com/dotnet/csharp/language-reference/proposals/unions) देखें।
